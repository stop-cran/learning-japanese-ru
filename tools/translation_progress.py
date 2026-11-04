"""Read-only, revision-bound translation inventory and conservative drift checks."""

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

from build_manifest import build_manifest

ROOT = Path(__file__).resolve().parents[1]
MAPS = {
    "files": {"kanji", "words", "articles", "strokes", "counters", "grammar"},
    "images": {"images"}, "scenes": {"scenes"}, "curriculum": {"curriculum"},
    "listening": {"listening"}, "audio": {"audio"},
    "listeningTasks": {"listening-tasks"}, "listeningTaskAudio": {"task-audio"},
    "listeningTaskImages": {"task-images"},
}
BINARY = {"images", "audio", "listeningTaskAudio", "listeningTaskImages"}
NORMATIVE = {
    "README.md", "REVIEW.md", "docs/content-format.md", "docs/jlpt-levels.md",
    "docs/confusable-words.md", "docs/grammar-authoring-sources.md",
    "docs/listening-n5.md", "docs/listening-tasks.md", "docs/listening-n4.md",
    "docs/counter-n5.md", "docs/counter-n4.md", "docs/grammar-curriculum-sources.json",
}
PROSE = {"title", "translation", "en", "gloss", "meaning", "explanation",
         "rationale", "description", "cue", "help", "feedback", "levelRationale"}
JAPANESE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uf900-\ufaff\U00020000-\U0002fa1f]+")
SHA = re.compile(r"[0-9a-f]{64}")
COMMIT = re.compile(r"[0-9a-f]{40}")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def strict_json(data):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON field: {key}")
            result[key] = value
        return result
    return json.loads(data, object_pairs_hook=unique)


def safe_path(value):
    if not isinstance(value, str) or "\\" in value or ":" in value:
        raise ValueError(f"Invalid repository path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in ("", ".", "..") for p in value.split("/")):
        raise ValueError(f"Invalid repository path: {value!r}")
    return path


def runtime(manifest):
    unknown = set(manifest) - set(MAPS) - {
        "schemaVersion", "contentVersion", "baseLanguage", "targetLanguage"}
    if unknown:
        raise ValueError(f"Unknown manifest fields: {sorted(unknown)}")
    result = {}
    for group, folders in MAPS.items():
        for path, sha in manifest.get(group, {}).items():
            if safe_path(path).parts[0] not in folders or path in result or not SHA.fullmatch(sha):
                raise ValueError(f"Invalid/duplicate manifest entry: {path}")
            result[path] = {"map": group, "sha256": sha}
    return result


def raw_identity(path, entry):
    return entry["map"] in BINARY or path.startswith("strokes/")


def local_runtime(root):
    manifest = read_json(root / "manifest.json")
    if manifest != build_manifest(root) or manifest.get("baseLanguage") != "ru":
        raise ValueError("Russian manifest is stale or not a Russian edition")
    files = runtime(manifest)
    for path, entry in files.items():
        file = root.joinpath(*safe_path(path).parts)
        if not file.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"File escapes Russian root: {path}")
        entry["rawSha256"] = digest(file.read_bytes())
    return manifest, files


def projection(data, suffix):
    """Conservative review hints, never a proof that a changed lesson is equivalent."""
    text = data.decode("utf-8")
    if suffix == ".json":
        def non_prose(value):
            if isinstance(value, dict):
                return {k: non_prose(v) for k, v in value.items() if k not in PROSE}
            if isinstance(value, list):
                return [non_prose(v) for v in value]
            return value
        facts = non_prose(strict_json(text))
    else:
        metadata = text.split("---", 2)[1] if text.startswith("---") else ""
        facts = [line for line in metadata.splitlines() if not line.startswith("title:")]
    return digest(canonical({"nonProse": facts, "japanese": JAPANESE.findall(text)}))


class GitFiles:
    def __init__(self, root, revision):
        if not COMMIT.fullmatch(revision):
            raise ValueError("An immutable full commit SHA is required")
        self.root, self.revision = root, revision
        actual = self.git("rev-parse", revision + "^{commit}").decode().strip()
        if actual != revision:
            raise ValueError("Source revision is not the requested commit")
        self.files = {}
        for entry in self.git("ls-tree", "-rz", "--full-tree", revision).split(b"\0"):
            if entry:
                details, path = entry.split(b"\t", 1)
                mode, kind, oid = details.decode().split()
                self.files[path.decode("utf-8")] = (mode, kind, oid)
        self.process = subprocess.Popen(
            ["git", "-C", str(root), "cat-file", "--batch"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args])

    def read(self, path):
        mode, kind, oid = self.files[path]
        if kind != "blob" or mode not in ("100644", "100755"):
            raise ValueError(f"Not an ordinary tracked file: {path}")
        self.process.stdin.write((oid + "\n").encode())
        self.process.stdin.flush()
        header = self.process.stdout.readline().decode().strip().split()
        if len(header) != 3 or header[:2] != [oid, "blob"]:
            raise ValueError(f"Cannot read frozen Git object: {path}")
        data = self.process.stdout.read(int(header[2]))
        if self.process.stdout.read(1) != b"\n":
            raise ValueError("Invalid Git batch response")
        return data, oid

    def close(self):
        self.process.stdin.close()
        self.process.stdout.close()
        if self.process.wait(timeout=30):
            raise ValueError("Git object reader failed")


def inventory(root, revision):
    source = GitFiles(root, revision)
    try:
        manifest = strict_json(source.read("manifest.json")[0])
        files = runtime(manifest)
        for path, entry in files.items():
            data, oid = source.read(path)
            normalized = data if entry["map"] in BINARY else data.replace(b"\r\n", b"\n")
            if digest(normalized) != entry["sha256"]:
                raise ValueError(f"Manifest does not match frozen Git blob: {path}")
            entry.update(rawSha256=digest(data), gitBlob=oid)
            if entry["map"] not in BINARY:
                entry["invariantProjectionSha256"] = projection(normalized, PurePosixPath(path).suffix)
        guidance = {}
        for path in sorted(source.files):
            active = (path == ".github/copilot-instructions.md"
                      or path.startswith((".github/instructions/", ".github/agents/"))) and path.endswith(".md")
            if active or path in NORMATIVE or re.fullmatch(r"docs/grammar-[^/]+-sources\.json", path):
                data, oid = source.read(path)
                guidance[path] = {"sha256": digest(data.replace(b"\r\n", b"\n")), "gitBlob": oid}
        return {"schemaVersion": 1, "commit": revision, "contentVersion": manifest["contentVersion"],
                "files": dict(sorted(files.items())), "guidance": guidance}
    finally:
        source.close()


def changes(before, after):
    removed, added = set(before) - set(after), set(after) - set(before)
    old_hashes, new_hashes = defaultdict(list), defaultdict(list)
    for path in removed:
        old_hashes[before[path]["sha256"]].append(path)
    for path in added:
        new_hashes[after[path]["sha256"]].append(path)
    result = []
    for path in sorted(set(before) | set(after)):
        old, new = before.get(path), after.get(path)
        if old is None:
            item = {"path": path, "change": "added"}
            matches = old_hashes[new["sha256"]]
            if len(matches) == len(new_hashes[new["sha256"]]) == 1:
                item["possibleRenameFrom"] = matches[0]
        elif new is None:
            item = {"path": path, "change": "removed"}
        elif old["sha256"] != new["sha256"]:
            item = {"path": path, "change": "modified"}
            if "invariantProjectionSha256" in old:
                item["invariantProjectionChanged"] = (
                    old["invariantProjectionSha256"] != new.get("invariantProjectionSha256"))
        elif old.get("rawSha256") != new.get("rawSha256"):
            item = {"path": path, "change": "raw-only"}
        else:
            continue
        result.append(item)
    return result


def report(before, after, ledger, russian):
    if ledger.get("schemaVersion") != 1 or not COMMIT.fullmatch(ledger.get("targetCommit", "")):
        raise ValueError("Invalid tracking ledger")
    records = {}
    for item in ledger["records"]:
        path = item["path"]
        safe_path(path)
        if (path in records or not COMMIT.fullmatch(item.get("sourceCommit", ""))
                or not all(SHA.fullmatch(item.get(k, "")) for k in ("sourceSha256", "ruSha256"))):
            raise ValueError(f"Invalid/duplicate review record: {path}")
        records[path] = item
    drafts = {}
    for item in ledger.get("drafts", []):
        path = item["path"]
        safe_path(path)
        if path in drafts or path in records:
            raise ValueError(f"Duplicate draft/runtime review: {path}")
        drafts[path] = item
    entries = []
    for path in sorted(set(after["files"]) | set(records) | set(russian)):
        target, record, local = after["files"].get(path), records.get(path), russian.get(path)
        if target is None:
            status = "removed-upstream" if record else "ru-only"
        elif record is None:
            draft = drafts.get(path)
            if local:
                status = "unreviewed-ru"
            elif draft:
                reviewed = (draft.get("sourceSha256") == target["sha256"]
                            and draft.get("ruSha256") == draft.get("currentRuSha256")
                            and draft.get("reviewStatus") == "accepted" and draft.get("reviewEvidence"))
                status = "draft-reviewed-runtime-blocked" if reviewed else "draft-review-stale"
            else:
                status = "pending"
        elif local is None:
            status = "missing-ru"
        elif local["sha256"] != record["ruSha256"]:
            status = "ru-changed"
        elif target["sha256"] != record["sourceSha256"]:
            status = "source-changed"
        elif raw_identity(path, target) and (
                not SHA.fullmatch(record.get("sourceRawSha256", ""))
                or not SHA.fullmatch(record.get("ruRawSha256", ""))):
            status = "raw-evidence-required"
        elif raw_identity(path, target) and local.get("rawSha256") != record["ruRawSha256"]:
            status = "ru-changed"
        elif raw_identity(path, target) and target.get("rawSha256") != record["sourceRawSha256"]:
            status = "source-changed"
        elif record.get("coverage") != "complete":
            status = "partial-reviewed"
        elif record.get("reviewStatus") != "accepted" or not record.get("reviewEvidence"):
            status = "review-required"
        else:
            status = "reviewed-current"
        entries.append({"path": path, "status": status, "adopted": record is not None,
                        "sourceSha256": target["sha256"] if target else None,
                        "ruSha256": local["sha256"] if local else None,
                        "sourceRawSha256": target.get("rawSha256") if target else None,
                        "ruRawSha256": local.get("rawSha256") if local else None,
                        "reviewEvidence": record.get("reviewEvidence") if record else None})
    guidance = changes(before["guidance"], after["guidance"])
    unresolved_guidance = [
        path for path, entry in after["guidance"].items()
        if ledger.get("guidance", {}).get(path, {}).get("sha256") != entry["sha256"]
        or not ledger.get("guidance", {}).get(path, {}).get("reviewEvidence")]
    unresolved_guidance.extend(
        path for path in sorted(set(before["guidance"]) - set(after["guidance"]))
        if ledger.get("guidance", {}).get(path, {}).get("sha256", "not-disposed") is not None
        or not ledger.get("guidance", {}).get(path, {}).get("reviewEvidence"))
    target_changed = ledger["targetCommit"] != after["commit"]
    unresolved = [e for e in entries if e["adopted"] and e["status"] != "reviewed-current"]
    authority = ledger.get("checkpointAuthority")
    if not isinstance(authority, dict) or not authority.get("reviewEvidence"):
        authority = None
    ready = bool(records) and not (unresolved or unresolved_guidance or target_changed) and bool(authority)
    return {"schemaVersion": 1, "baselineCommit": before["commit"], "targetCommit": after["commit"],
            "runtimeEntries": len(after["files"]), "adoptedEntries": len(records),
            "families": dict(sorted(Counter(p.split("/")[0] for p in after["files"]).items())),
            "statuses": dict(sorted(Counter(e["status"] for e in entries).items())),
            "sourceChanges": changes(before["files"], after["files"]),
            "guidanceChanges": guidance, "unreconciledGuidance": unresolved_guidance,
            "targetChangedDuringBatch": target_changed, "checkpointReady": ready,
            "checkpointAuthority": authority, "entries": entries}


def checkpoint(progress, paths):
    if not progress["checkpointReady"]:
        raise ValueError("Checkpoint blocked by unresolved scope, guidance, target or authority")
    if not paths or len(paths) != len(set(paths)):
        raise ValueError("Checkpoint requires a nonempty distinct explicit scope")
    entries = {e["path"]: e for e in progress["entries"]}
    if any(p not in entries or not entries[p]["adopted"] or entries[p]["status"] != "reviewed-current"
           for p in paths):
        raise ValueError("Checkpoint scope includes unresolved or unadopted objects")
    return {"schemaVersion": 1, "kind": "scoped-translation-not-release-approval",
            "sourceCommit": progress["targetCommit"], "scope": sorted(paths),
            "files": {p: {k: entries[p][k] for k in (
                "sourceSha256", "ruSha256", "sourceRawSha256", "ruRawSha256", "reviewEvidence")}
                for p in sorted(paths)},
            "authority": progress["checkpointAuthority"]}


def read_json(path):
    return strict_json(path.read_text(encoding="utf-8-sig"))


def write_new(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as output:
        json.dump(value, output, ensure_ascii=False, indent=1, sort_keys=True)
        output.write("\n")


def current_report(before, after, ledger, root):
    manifest, local = local_runtime(root)
    tracking = read_json(ledger)
    for draft in tracking.get("drafts", []):
        path = root.joinpath(*safe_path(draft["draftPath"]).parts)
        if not path.resolve().is_relative_to(root.resolve()) or safe_path(draft["draftPath"]).parts[0] != "docs":
            raise ValueError("Non-runtime drafts must remain under docs")
        draft["currentRuSha256"] = digest(path.read_bytes().replace(b"\r\n", b"\n")) if path.is_file() else None
    result = report(read_json(before), read_json(after), tracking, local)
    result["russianContentVersion"] = manifest["contentVersion"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    snap = commands.add_parser("inventory")
    snap.add_argument("--upstream", type=Path, required=True)
    snap.add_argument("--revision", required=True)
    compare = commands.add_parser("report")
    gate = commands.add_parser("checkpoint")
    gate.add_argument("--scope", type=Path, required=True)
    for command in (compare, gate):
        command.add_argument("--before", type=Path, required=True)
        command.add_argument("--after", type=Path, required=True)
        command.add_argument("--ledger", type=Path, required=True)
        command.add_argument("--russian-root", type=Path, default=ROOT)
    for command in (snap, compare, gate):
        command.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "inventory":
        result = inventory(args.upstream, args.revision)
    else:
        result = current_report(args.before, args.after, args.ledger, args.russian_root)
        if args.command == "checkpoint":
            result = checkpoint(result, read_json(args.scope))
    write_new(args.output, result)
    print(f"{args.command}: {args.output}")


if __name__ == "__main__":
    main()

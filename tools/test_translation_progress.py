"""Contributor provenance regressions; fixture approvals are not real review evidence."""

from copy import deepcopy
from pathlib import Path
import subprocess
import tempfile
import unittest

from build_manifest import build_manifest
from translation_progress import (
    canonical, checkpoint, current_report, digest, inventory, local_runtime, projection, report, runtime, write_new)


class TranslationProgressTests(unittest.TestCase):
    def setUp(self):
        self.path = "words/日.md"
        self.source = "a" * 64
        self.ru = "b" * 64
        self.before = {"commit": "1" * 40, "files": {
            self.path: {"sha256": self.source, "map": "files",
                        "invariantProjectionSha256": "p"}}, "guidance": {}}
        self.after = deepcopy(self.before)
        self.after["commit"] = "2" * 40
        self.ledger = {"schemaVersion": 1, "targetCommit": self.after["commit"],
                       "checkpointAuthority": {"reviewEvidence": ["synthetic fixture only"]},
                       "records": [{"path": self.path, "sourceCommit": self.before["commit"],
                                    "sourceSha256": self.source, "ruSha256": self.ru,
                                    "coverage": "complete", "reviewStatus": "accepted",
                                    "reviewEvidence": ["synthetic fixture only"]}]}
        self.russian = {self.path: {"sha256": self.ru}}

    def progress(self):
        return report(self.before, self.after, self.ledger, self.russian)

    def test_scoped_checkpoint_does_not_claim_untranslated_additions(self):
        self.after["files"]["words/月.md"] = {"sha256": "c" * 64}
        value = self.progress()
        self.assertEqual({"pending": 1, "reviewed-current": 1}, value["statuses"])
        self.assertTrue(value["checkpointReady"])
        self.assertEqual([self.path], checkpoint(value, [self.path])["scope"])
        with self.assertRaises(ValueError):
            checkpoint(value, ["words/月.md"])

    def test_source_or_russian_change_expires_review_including_english_only_edit(self):
        self.after["files"][self.path]["sha256"] = "c" * 64
        value = self.progress()
        self.assertEqual("source-changed", value["entries"][0]["status"])
        self.assertFalse(value["sourceChanges"][0]["invariantProjectionChanged"])
        self.assertFalse(value["checkpointReady"])
        self.after = deepcopy(self.before)
        self.after["commit"] = self.ledger["targetCommit"]
        self.russian[self.path]["sha256"] = "d" * 64
        self.assertEqual("ru-changed", self.progress()["entries"][0]["status"])

    def test_partial_review_and_missing_authority_never_advance(self):
        self.ledger["records"][0]["coverage"] = "partial"
        self.assertEqual("partial-reviewed", self.progress()["entries"][0]["status"])
        with self.assertRaises(ValueError):
            checkpoint(self.progress(), [self.path])
        self.ledger["records"][0]["coverage"] = "complete"
        self.ledger["checkpointAuthority"] = None
        self.assertFalse(self.progress()["checkpointReady"])

    def test_reviewed_draft_stays_blocked_and_changed_context_expires_review(self):
        name = "listening/task.json"
        self.after["files"][name] = {"sha256": "c" * 64, "map": "listening"}
        self.ledger["drafts"] = [{"path": name, "sourceSha256": "c" * 64,
                                  "ruSha256": "d" * 64, "currentRuSha256": "d" * 64,
                                  "reviewStatus": "accepted", "reviewEvidence": ["fixture"]}]
        value = self.progress()
        draft = next(e for e in value["entries"] if e["path"] == name)
        self.assertEqual("draft-reviewed-runtime-blocked", draft["status"])
        self.assertFalse(draft["adopted"])
        self.ledger["drafts"][0]["currentRuSha256"] = "e" * 64
        self.assertEqual(1, self.progress()["statuses"]["draft-review-stale"])

    def test_exact_rename_is_only_a_candidate_and_never_rebinds_review(self):
        self.after["files"]["words/ひ.md"] = self.after["files"].pop(self.path)
        value = self.progress()
        added = next(e for e in value["sourceChanges"] if e["change"] == "added")
        self.assertEqual(self.path, added["possibleRenameFrom"])
        self.assertEqual({"pending": 1, "removed-upstream": 1}, value["statuses"])
        self.assertFalse(value["checkpointReady"])

    def test_new_instruction_or_changed_guidance_requires_exact_acknowledgement(self):
        name = ".github/instructions/new.instructions.md"
        self.after["guidance"][name] = {"sha256": "c" * 64}
        self.assertEqual([name], self.progress()["unreconciledGuidance"])
        self.ledger["guidance"] = {name: {"sha256": "c" * 64, "reviewEvidence": ["fixture"]}}
        self.assertTrue(self.progress()["checkpointReady"])
        self.after["guidance"][name]["sha256"] = "d" * 64
        self.assertFalse(self.progress()["checkpointReady"])

    def test_removed_guidance_requires_explicit_disposition(self):
        name = ".github/agents/removed.agent.md"
        self.before["guidance"][name] = {"sha256": "c" * 64}
        self.assertEqual([name], self.progress()["unreconciledGuidance"])
        self.ledger["guidance"] = {name: {"sha256": None, "reviewEvidence": ["fixture"]}}
        self.assertTrue(self.progress()["checkpointReady"])

    def test_raw_stroke_change_is_not_hidden_by_normalized_manifest_hash(self):
        self.path = "strokes/日.json"
        self.before["files"] = {self.path: {"sha256": self.source, "map": "files",
                                          "rawSha256": "c" * 64}}
        self.after["files"] = deepcopy(self.before["files"])
        self.ledger["records"][0].update(path=self.path, sourceRawSha256="c" * 64, ruRawSha256="d" * 64)
        self.russian = {self.path: {"sha256": self.ru, "rawSha256": "d" * 64}}
        self.assertTrue(self.progress()["checkpointReady"])
        self.after["files"][self.path]["rawSha256"] = "e" * 64
        self.assertEqual("raw-only", self.progress()["sourceChanges"][0]["change"])
        self.assertEqual("source-changed", self.progress()["entries"][0]["status"])
        self.assertFalse(self.progress()["checkpointReady"])

    def test_checkpoint_rechecks_current_russian_bytes_not_an_old_green_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "words").mkdir()
            (root / self.path).write_text("русский", encoding="utf-8")
            (root / "content-language.json").write_bytes(canonical({"baseLanguage": "ru", "targetLanguage": "ja"}))
            manifest = build_manifest(root)
            self.ledger["records"][0]["ruSha256"] = manifest["files"][self.path]
            paths = [root / p for p in ("before.json", "after.json", "ledger.json")]
            for path, value in zip(paths, (self.before, self.after, self.ledger)):
                write_new(path, value)
            (root / "manifest.json").write_bytes(canonical(manifest))
            self.assertTrue(current_report(*paths, root)["checkpointReady"])
            (root / self.path).write_text("изменено", encoding="utf-8")
            (root / "manifest.json").write_bytes(canonical(build_manifest(root)))
            changed = current_report(*paths, root)
            self.assertEqual("ru-changed", changed["entries"][0]["status"])
            with self.assertRaises(ValueError):
                checkpoint(changed, [self.path])

    def test_target_advance_and_duplicate_records_are_rejected(self):
        self.ledger["targetCommit"] = self.before["commit"]
        self.assertTrue(self.progress()["targetChangedDuringBatch"])
        self.assertFalse(self.progress()["checkpointReady"])
        self.ledger["records"].append(deepcopy(self.ledger["records"][0]))
        with self.assertRaises(ValueError):
            self.progress()

    def test_projection_detects_japanese_answers_dependencies_and_assets(self):
        base = {"title": "sun", "prompt": "日", "answers": ["ひ"], "requires": ["a"], "image": "images/a.webp"}
        original = projection(canonical(base), ".json")
        for field, value in [("prompt", "月"), ("answers", ["にち"]), ("requires", ["b"]),
                             ("image", "images/b.webp")]:
            with self.subTest(field=field):
                self.assertNotEqual(original, projection(canonical(base | {field: value}), ".json"))
        self.assertEqual(original, projection(canonical(base | {"title": "day"}), ".json"))

    def test_unknown_maps_path_escape_and_overwriting_receipts_fail_closed(self):
        for value in [{"newMedia": {}}, {"files": {"../private.md": "a" * 64}},
                      {"images": {"words/日.md": "a" * 64}}]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                runtime(value)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "receipt.json"
            write_new(path, {"first": True})
            with self.assertRaises(FileExistsError):
                write_new(path, {"second": True})

    def duplicate_manifest_root(self, directory):
        root = Path(directory)
        (root / "articles").mkdir()
        (root / "articles" / "test.md").write_text("# 日\n", encoding="utf-8")
        (root / "content-language.json").write_bytes(canonical({"baseLanguage": "ru", "targetLanguage": "ja"}))
        return root, canonical(build_manifest(root))

    def test_local_manifest_rejects_duplicate_and_escaped_duplicate_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self.duplicate_manifest_root(directory)
            for key in ("schemaVersion", r"\u0073chemaVersion"):
                with self.subTest(key=key):
                    (root / "manifest.json").write_bytes(('{"' + key + '":1,').encode() + manifest[1:])
                    with self.assertRaisesRegex(ValueError, "duplicate"):
                        local_runtime(root)

    def test_frozen_git_manifest_rejects_duplicate_and_escaped_duplicate_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self.duplicate_manifest_root(directory)
            def git(*args):
                return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.DEVNULL)
            git("init")
            git("config", "user.name", "Fixture")
            git("config", "user.email", "fixture@example.invalid")
            (root / ".gitattributes").write_text("* -text\n", encoding="utf-8")
            for key in ("schemaVersion", r"\u0073chemaVersion"):
                with self.subTest(key=key):
                    (root / "manifest.json").write_bytes(('{"' + key + '":1,').encode() + manifest[1:])
                    git("add", ".")
                    git("-c", "commit.gpgsign=false", "commit", "-m", "duplicate fixture")
                    revision = git("rev-parse", "HEAD").decode().strip()
                    with self.assertRaisesRegex(ValueError, "duplicate"):
                        inventory(root, revision)

    def test_inventory_reads_git_blobs_not_dirty_worktree_or_normalized_assets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.DEVNULL)
            git("init")
            git("config", "user.name", "Fixture")
            git("config", "user.email", "fixture@example.invalid")
            (root / "articles").mkdir()
            (root / "images").mkdir()
            (root / "articles" / "test.md").write_bytes("# 日\r\n".encode())
            (root / "images" / "test.webp").write_bytes(b"fixture\r\nbinary")
            (root / ".gitattributes").write_text("* -text\n", encoding="utf-8")
            (root / ".github" / "instructions").mkdir(parents=True)
            guide = root / ".github" / "instructions" / "new.instructions.md"
            guide.write_text('---\napplyTo: "articles/**"\n---\nRule.\n', encoding="utf-8")
            manifest = build_manifest(root)
            (root / "manifest.json").write_bytes(canonical(manifest))
            git("add", ".")
            git("-c", "commit.gpgsign=false", "commit", "-m", "fixture")
            revision = git("rev-parse", "HEAD").decode().strip()
            (root / "articles" / "test.md").write_text("dirty", encoding="utf-8")
            value = inventory(root, revision)
            self.assertEqual(manifest["files"]["articles/test.md"], value["files"]["articles/test.md"]["sha256"])
            self.assertEqual(digest(b"fixture\r\nbinary"), value["files"]["images/test.webp"]["rawSha256"])
            self.assertIn(".github/instructions/new.instructions.md", value["guidance"])
            with self.assertRaises(ValueError):
                inventory(root, "HEAD")


if __name__ == "__main__":
    unittest.main()

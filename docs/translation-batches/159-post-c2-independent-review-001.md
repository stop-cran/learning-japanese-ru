<!-- Publication copy of the complete prior review, with the original private-artifact classification removed and line endings normalized to LF. Original raw SHA-256: 8f61a8ef7442f3a1d4357e7dd7fc995a8f617135db40c32f653e3bfaeaa57a5a. The original report's source-object limitation and manifest-hash transcription are resolved only by its accompanying addendum. -->

# B159 post-C2 rebind packet — independent review

## Verdict

**Packet and accessible snapshot checks pass, with a material source-object limitation.** No high-confidence lexical or structural discrepancy was found in the reviewed candidate content, rebind inventory, caption inventory, or backlinks. This is not acceptance, semantic validation, or clearance to display, ship, publish, or activate anything. Every one of the 39 foil directions remains **UNVERIFIED**.

The review request and packet-manifest SHA-256 values matched the coordinator-provided pins before the request was read: `aad8741c901757a8611cd7d51a9a2a3c53d8e8aaf3374e57e00902593cf75bca` and `0c8134ea23a7af778de8ece20e0f5c68651b2f9146a9640ccf3f9b5c6da759` respectively.

## Findings

1. **Packet integrity and pinned main snapshots:** All 3,023 manifest entries match their recorded byte lengths and SHA-256 values; the manifest is the only unlisted packet file. The 2,214 bound main snapshots match the pinned main tree and their raw hashes/lengths. The isolated main checkout is clean at commit `32c0ff9e673e16340873a5f87087577f48fb12d6`, tree `f5667570121b7d2902f77db68f274207fadb8ad5`.

2. **Frozen-English source limitation:** The pinned source commit `6af98cb717755690a9ca793e5454a96ebd7a8f9f` is absent from the isolated checkout. The 732 frozen-English snapshots match packet raw hashes, byte lengths, and recorded Git-blob SHA-1s, but their Git objects could not be independently verified against that commit. Consequently, comparisons to those frozen snapshots establish internal consistency with the packet, not independent source-commit provenance.

3. **Candidate/source consistency:** All 13 candidate lessons and their 13 frozen-English counterparts were checked. Candidate source metadata and cited numeric entry-ID sets match the frozen-English copies; all 13 candidate stroke JSON files are byte-identical to their source snapshots. The stroke payload identifies KanjiVG, CC BY-SA 3.0, and source revision `70a0b7ae0c18ceb5cb358274b029cce0234a43bc`. Candidate relative links resolve. The supplementary references observed for 恋う (Wiktionary) and 承 (official Joyo table) are identified in the content. Source notes and receipts were treated as leads/supporting material, not verdicts; they do not independently establish semantic or source correctness.

4. **Foil directions:** The 39 directed rows comprise 38 published-main targets and one internal B159 target (`悩→快`). All 39 statuses are **UNVERIFIED**. The target lessons were read; there are 31 unique published target lessons. Directions, grouped by source glyph, are:

   | Source | Directed targets |
   | --- | --- |
   | 延 | 建, 庭, 近 |
   | 弱 | 強, 弟, 引 |
   | 律 | 待, 建, 洋 |
   | 復 | 待, 得, 彼 |
   | 快 | 決, 怖, 忙 |
   | 恋 | 変, 忘, 急 |
   | 患 | 中, 思, 息 |
   | 悩 | 怖, 忙, 快 |
   | 戸 | 石, 戻, 店 |
   | 承 | 水, 手, 了 |
   | 技 | 支, 持, 抜 |
   | 担 | 指, 押, 招 |
   | 拝 | 持, 指, 押 |

   The accompanying source notes describe lexical or contextual leads, not verdicts. In particular, preserve the provisional qualifications on `悩→快` and `悩→忙`; shared contexts, antonym-like cues, components, and compounds do not establish that a glyph pair is a safe distractor in any rendering or learner context. `庫` and `憎` are excluded from this derivative only.

5. **Caption screen and backlinks:** Independently recomputing the title-segment screen agrees with the packet: three Russian published overlaps (`律→法`, `患→痛`, `技→術`), two internal Russian directions (`承↔担`), and three English published overlaps (`律→法`, `復→再`, `技→術`). This is a lexical title screen only—not proof of co-display or matcher behavior. All 705 published Russian caption titles and all 718 frozen-English candidate/published titles match their bound snapshots. Of nine word overlays, eight reduce to current main after removing exactly one expected candidate-link wrapper; `冷蔵庫.md` is byte-identical to current main. No missing overlay or relative-link target was found. The historical scratch-baseline removal claim for `冷蔵庫.md` could not be independently checked because that scratch file is absent.

6. **B158/C2 qualifications:** C2 remains held: `facets.C2=UNVERIFIED`, null runtime authority, pending target, inactive runtime guard, and no runtime manifest entry. The B158 幅 qualification remains: the lesson teaches width/breadth, range/difference, and 増幅, while metadata includes an untaught “hanging scroll” sense. 幅/福 reading and voice behavior remain unverified. These qualifications are preserved; this review does not change either status.

## Checks performed

- Verified the required review-request and manifest hashes first; then checked every packet manifest entry and the private preparation index's recorded file hashes/sizes.
- Compared main snapshots against the pinned tree and checked the isolated checkout's commit, tree, and clean status.
- Parsed the frozen source batch and compared all candidate metadata, citation-ID sets, and stroke bytes against frozen-English counterparts.
- Read all 13 candidate lessons, all 13 frozen-English candidate lessons, all 31 unique published foil target lessons, relevant source notes, and B158/C2 evidence.
- Recomputed all 39 foil bindings/status counts, candidate relative links, caption title inventories and overlap screen, and word-overlay normalization/backlinks.
- Parsed pinned main translation tracking/progress and relevant B158/C2 qualification documents.
- Performed lightweight file/hash/JSON/text checks only. No repository, packet, or checkout files were changed; no staging, commits, PRs, runtime/emulator/JVM work, or heavy build work was performed.

## Files and evidence read

- Packet control files: `REVIEW-REQUEST.md`, `packet-manifest.json`, `rebind.json`, `caption-inventory.json`, and `snapshot-bindings.json`.
- Candidate package: candidate manifest and all 13 `inputs/kanji` lessons, 13 `inputs/strokes` files, nine `inputs/words` overlays, and relevant source-binding, source-check, backlink, and intake evidence.
- Snapshot content: all 13 frozen-English candidate lesson counterparts; all 31 unique published foil target lessons; the frozen-English source batch and stroke snapshots; pinned main translation tracking/progress, relevant B158/C2 documents, and caption/title inventories.
- Private preparation index and all ten narrative source/coordinator notes. The three author verification receipts were supporting material only; their coordinator-provided hashes were checked.

## Limitations and scope boundary

The missing frozen-English source commit prevents independent Git-object verification of those source snapshots. The absent historical scratch file prevents checking the stated historical `冷蔵庫.md` removal. Source-note fingerprints, fetched-source claims, and author receipts are not substitute verdict evidence.

Findings are lexical and structural only. This review does **not** clear co-display, semantic suitability, visual similarity, voice/readings, matcher behavior, learner impact, device/runtime behavior, acceptance, or publication. No conclusion should be inferred for excluded glyphs or for transitive/reverse foil directions.

> Public path-redacted projection of the reviewer task result. Only the local absolute RU and frozen-EN worktree roots were replaced; the unmodified returned report is retained privately as `ru-128-independent-review-001-private.md`. The reviewer tool returned final report text; it did not expose a distinct shell-stdout stream.



# Independent consolidated review — batch 128



**Date:** 2026-11-10

**Snapshot:** `<RU_WORKTREE>`, branch `full-ru-128-decide-water-wash-kanji`, HEAD `c8d99b2a8ae83418eb10ef8905fefddf01e0480b`; base `origin/main` `64c4f2144ae8c42ea813050470adc9d40137a629`. Frozen EN worktree HEAD: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.



**Candidate snapshot digest:** `b2b8b24f88be4d8884002ddd29b18baceceb1fe368785249261a3d9e7e5ef996`. This is SHA-256 over UTF-8 lines in requested path order: relative Windows path, tab, lowercase SHA-256 of that file’s raw bytes, LF. It covers the 28 requested content files plus `manifest.json` (29 paths total); it excludes unrelated untracked `tools/__pycache__/`. The digest was the same at final verification. No files were edited, staged, or committed.



## Coverage actually completed



Read all current RU candidate content in full:



- Lessons: `kanji/{決,治,法,泳,洗,活,流}.md`

- Raw strokes: `strokes/{決,治,法,泳,洗,活,流}.json`

- Word pages: `words/{決める,政治,泳ぐ,洗う,生活,お手洗い,文法,水泳,決して,決まる,治る,法律,泳ぎ方,洗濯}.md`



Also read all seven corresponding frozen-EN lessons and all 14 corresponding frozen-EN word pages. All four batch-128 intake/freeze/amendment JSONs were read. Applicable review contract, content-structure guidance, the three named reviewer-agent files, format reference, translation methodology, and relevant full-translation-plan ranges were read.



Verified all seven RU stroke files’ raw hashes equal the frozen-EN files and the intake’s declared hashes. The seven frozen-EN lesson files’ declared raw SHA-256 and Git blob IDs also match. All local Markdown links in the 21 lesson/word pages resolve. Diff review against `origin/main` found only the authorized navigation wrappers in the 14 existing word pages; no word text, examples, meanings, quiz metadata, or other semantics changed. The 28 manifest entries’ normalized hashes match their files (`CRLF`→`LF`); manifest is schema 2, `ru`/`ja`, contentVersion `67eb914ece3e362f`. This is metadata consistency, not language approval.



## Primary evidence inspected



- Batch-128 KANJIDIC2 capture `ru-128-metadata-primary-capture-001.json`: SHA-256 `5daf51c14d3a8724678560d568d8acb4027ae4f9dbc4c7bde708a9cbcc79cef7`; source archive `ru-019-kanjidic2.xml.gz` independently hashes to declared archive SHA-256 `e26e34c9187a786bf1f0b21f87e311a9b0ed644aefe9693d10bdc7cb8643d8e0`. Read the captured full records for all seven characters and matched their UTF-8 record-string hashes. Verified strokes/grade: 決 7/3, 治 8/4, 法 8/4, 泳 8/3, 洗 9/6, 活 9/2, 流 10/3; classical radical 85 for all. Captured Japanese on/kun readings and divisions match the lesson metadata. The cited Unicode 17 source file hashes to `2e1efc1dcb59c575eedf5ccae60f95229f706ee6d031835247d843c11d96470c`; its U+2F54 row identifies Kangxi Radical Water, decomposition 水. The frozen community N3 list includes these seven; it is not an official JLPT syllabus. KANJIDIC2’s legacy JLPT field was not used as modern-level evidence.

- Batch-128 JMdict capture `ru-128-jmdict-primary-capture-001.json`: SHA-256 `1fa471ebaf72fa9eaeeb9404b3243d41af960027822be3b044e30b30eefb8fd2`; source archive `ru-041-official-JMdict-e-001.gz` independently hashes to declared `5af39046e9579fd5e14d07a048fccce422b8df0d940ba8c086439e5a7617eab6`. All 21 captured raw-entry UTF-8 hashes match their declarations. Read the recorded forms, readings, and selected senses for: `1254180` 決める; `1591420` 決まる; `1254380` 決定; `1375970` 政治; `1316830` 治める; `1599400` 治る; `2856318` 治す; `1517090` 方法; `1517480` 法律; `1505600` 文法; `1174340` 泳ぐ; `1371320` 水泳; `1497420` 浮く; `1390930` 洗う; `1390980` 洗濯; `1399790` 掃除; `1378860` 生活; `1208360` 活動; `1552140` 流れる; `1552120` 流す; `1272580` 交流. These entries support the cited lesson examples’ readings and senses; dictionary inclusion alone does not establish example frequency or naturalness.



## Verdicts



- **C1 Japanese correctness — CLEAN, bounded.** The seven new lessons’ source-derived readings, okurigana divisions, stroke counts, grades, classical radical, and N3 qualification are consistent with the inspected evidence. The JMdict forms/senses reviewed support the relevant lesson claims: decision/result, governing/healing and transitivity, law/method, swimming versus floating, washing versus general cleaning, life/activity, and flow/transitivity. Japanese examples and translations were read in full; no supported Japanese-content finding. Confidence is high for captured metadata and listed senses, lower for naturalness beyond these reviewed examples. Existing affected word-page text was read in RU and EN and found unchanged apart from navigation; this does not renew source approval of every older word-page claim.

- **C2 Scope/dependencies/quiz — UNVERIFIED overall.** Scope and link checks found no supported defect: all 14 affected word-page edits are authorized navigation-only changes; the nine optional unavailable lesson-link wrappers are removed while their Japanese text remains; the 14 new word-page links follow the amendments. The seven target `distractors` rows at `kanji/*.md:11` match frozen EN exactly, and all direct provider cards exist. The nine existing direct providers are 注, 洋, 漢, 始, 台, 去, 先, 話, 海; their typed metadata/pool membership and target-row metadata match the frozen source. No word-level quiz exclusions/distractors were added or changed.



  **All 21 ordinary negative directions remain UNVERIFIED**, not approved by metadata preservation or matching EN:

  - `kanji/決.md:11` 決→注/洋/漢

  - `kanji/治.md:11` 治→始/台/活

  - `kanji/法.md:11` 法→去/洗/泳

  - `kanji/泳.md:11` 泳→流/治/洗

  - `kanji/洗.md:11` 洗→先/活/法

  - `kanji/活.md:11` 活→話/海/流

  - `kanji/流.md:11` 流→泳/活/法



  I did not examine an app runtime operation, actual accepted-answer path, or runtime sense constraints; therefore no direction is approved for ordinary negative/fallback use.

- **C3 Russian learner comprehension — CLEAN, bounded.** Read all candidate learner-facing text, including examples, readings, explanations, comparisons, and the 14 existing word pages. The new Russian explanations communicate the intended contrasts and particle roles without requiring English; no supported comprehension finding. This is not native-speaker certification or a learning-effectiveness claim.



**Supported findings:** None. The 21 quiz directions above are unresolved review questions, not confirmed defects.



**Not performed / limits:** No app/device/runtime, native-speaker, frequency/corpus, or handwriting-rendering review; no full-corpus approval is claimed. `tools/validate.py`, tests, manifest generator, and budget checks were not run. The report’s structural checks were limited to the specified batch files and their consequential links/providers.

# B209 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `5f015601f1ff714f7c63b0edfa85215c8f99f071` (tree `b7775854199e6bd437d9ef17989cc2a7a45ae79a`),
> the signed candidate pushed before review.
> Later reconciliation is in `209-words-batch-48-recheck-001.md`.

Snapshot: 5f015601f1ff714f7c63b0edfa85215c8f99f071 (clean tree; diff base c834ac2, 52 files).
Scope: Consistency and quiz safety for batch 209-words-batch-48. Read in full, RU and frozen EN: all 30 new cards
(心理 徹底 徹夜 微妙 得意 従兄弟 ですから 従って 従う 後者 役割 効果 影響 影 当時 当てる 当たる 弾 強調 強盗 強力 引退 引用
引っ張る 弁当 座席 床 広告 幼い 年齢). Read all 20 navigation diffs in full (kanji 効 幼 当 得; words 与える 副作用 反抗 命令
地盤 応じる 掲示 支配 有効 機能 老い 自慢 苦手 責任 逆らう 陰). Checked manifest hashes for all 50 changed .md files and
the intake JSON structure only. Reviewer model not verifiable by me.
Verdicts: consistency CLEAN; quiz safety CLEAN with optional guards (see Findings); scoped coverage CLEAN.
Findings: none that are blocking. The four Minor items below are low-risk missing-guard hypotheses, listed as Optional.
 Verified facts:
 - Front matter of all 30 cards equals EN except title and quiz_exclusions; all EN exclusions are retained.
 - No RU-only links and no dangling links. EN links to absent RU targets (底, 完全, 従姉妹, 前者, 主張, 参考, 床 kanji,
   宣伝, 齢) are plain text, as the convention allows.
 - 20 navigation files: 27 links restored (当 3, 得 3, 効 2, 幼 2, 副作用 2, the other 15 files 1 each). After stripping
   link markup the text is identical to the base in every file, so there is no prose change; LF endings are unchanged.
 - Manifest: all 50 changed .md files match their sha256 in manifest.json. tools/validate.py reports 0 errors.
 - Intake JSON has the keys baseline, batchId, held, notes, payloads, schemaVersion, sourceCommit; I did not audit its
   payload list line by line.
 RU-introduced quiz_exclusions, classified:
 - 得意→武器: required (shared segment «сильная сторона»).
 - 影響→左右: required (shared segment «влияние»).
 - 床→性: required (shared segment «пол»).
 - 効果→有効: conservative (効果がある / 効果的 vs 有効 "effective").
 - 影響→毒: conservative («вредное влияние» vs «влияние»).
 None is unjustified.
Optional (Minor, medium/low confidence; unguarded in EN too, not defects):
 - 引退 ↔ 辞める: add quiz_exclusions: [辞める] to 引退 (only that file, then re-hash the manifest).
   Evidence: 辞める «уволиться; уйти с должности» overlaps «уход от дел».
 - 徹底 ↔ 丁寧: add [丁寧] to 徹底. Evidence: 丁寧 includes "thorough" in its gloss, 徹底 is «доскональность».
 - 心理 ↔ 精神 (low), 得意 ↔ 自慢 (low; the pair is linked in 自慢).
 - Weaker: 当時↔昔, 幼い↔若い, 従う↔守る, 役割↔担当, 従兄弟↔親戚, 強盗↔犯人, 年齢↔歳, 強力↔力, 効果↔副作用.
Limits:
 - JMdict senses cited (武器, 有効, 左右, 毒, 辞める, 丁寧) come from my own knowledge, not fetched and verified.
 - 118 strokes/*.json files in the working tree do not match their manifest hashes, and the HEAD blob also mismatches
   (my naive sha256 may not be the manifest's canonical hashing for JSON). They are untouched by this batch, so I treat
   them as pre-existing or a method artifact and did not investigate.
 - I did not read the RU instruction files or content-format docs; the prompt's contract was used.
 - No linguistic fact-check beyond consistency was done.

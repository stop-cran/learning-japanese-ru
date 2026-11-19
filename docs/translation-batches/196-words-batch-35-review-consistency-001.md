# B196 consistency and quiz-safety review (batch `196-words-batch-35`)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `dd399249fe65eeba0cef005a3655cc3bc1ab874f` (tree `2585cf658a0f2479ce3fae46abb0b9c5ba55ea23`),
> the signed candidate pushed before review.
> Later reconciliation is in `196-words-batch-35-recheck-001.md`.

Snapshot: dd39924 (`dd399249fe65…`, branch `full-ru-196-words-35`, parent ccb75fd); `git status` clean before and after my checks; HEAD unchanged. (I ran `tools/validate.py` and `tools/build_manifest.py` on the tree; validate = 0 errors, build_manifest reproduced the committed manifest byte-for-byte, tree stayed clean.)

Scope: all 30 new `words/*.md` cards read in full against RU conventions and (front matter, links, exclusions) against frozen EN 6af98cb; the 21 navigation-only restorations (diffed at line level); `manifest.json`; `docs/translation-batches/196-words-batch-35-intake.json` (all 51 payload candidate/source SHA-256 recomputed against the working tree and the frozen EN files: 0 mismatches). Titles of existing RU cards screened by pattern (≈200 candidate titles of 2,533 word cards) and the named dense clusters inspected individually. Facets: consistency and quiz safety, plus cross-file integration. Did not read author reports, title-screen output, reviewer reports or batch/ledger/progress records. Model: not verifiable from inside this session. Dictionary evidence for extra exclusions: JMdict via jisho.org API (支える, 肌) plus the cards' own cited senses; others from the cards' text.

Verdicts:
- Consistency: CLEAN. Front matter (word/reading/jlpt/type/kanji/tags) is identical to EN for all 30 cards; titles/Cyrillic follow convention; every relative link resolves; `link_parity.py` passes for the 30 cards; every EN link to any of the 30 words in an RU-existing file is present in RU with the same count (42 links compared, 0 differences); the 21 navigation-only diffs change only link brackets/hrefs at the EN positions (33 links, no prose change); manifest regenerates identically; intake hashes verified; no generated/unrelated files in the commit.
- Quiz safety: NEEDS FIX (one minor, F1). All EN exclusions are retained. Every extra pair has a real basis; none is a defect.
- Scoped coverage of cross-file integration: CLEAN (no link target missing where an RU target exists; plain-text mentions such as 皮膚, 職場, 就職, 月給, 収入, 年齢, 保管, 残す, 接続, 瓶 correspond to absent RU cards).

Findings:
- F1; Minor (quiz); quiz safety; `words/老人.md` front matter (no `quiz_exclusions`); 老人 «пожилой человек» is a defensible correct answer for おじいさん «дедушка; пожилой мужчина» / おばあさん «бабушка; пожилая женщина» (title segments name the same referent: an elderly person), and the 老人 body itself says it does not specify sex. No direct pair is declared on either side (おじいさん/おばあさん list only 男/女 families). Remedy: add after the `tags:` line of `words/老人.md`: `quiz_exclusions: [おじいさん, おばあさん]` and regenerate `manifest.json`. Evidence: JMdict 老人 (1561090) "old man; old people; elderly person" overlaps おじいさん sense "old man; male senior citizen". EN has the same gap ("elderly person" vs "grandfather or elderly man"), so this is inherited, but the RU titles make the overlap more explicit. Confidence: medium (pair is direct, one-sided declaration suffices; no reverse or transitive pair is requested).

Extra exclusions beyond EN (dictionary basis; necessity classification):
- 能力→知能: 知能 title includes «умственные способности» ≈ «способность»; JMdict 能力 "ability; faculty", 知能 "intelligence; mental capacity" — required.
- 能→機能: 能 body teaches sense «функция» (JMdict 能 sense 1 incl. function); 機能 title «функция» — required.
- 育つ→伸びる: 伸びる «расти» (JMdict "to grow (hair, plants); to grow taller") vs 育つ «вырастать» — required. 育つ→成長: 成長 «рост; развитие», body says they overlap — conservative.
- 皮→革: JMdict 皮 senses 1–3 (skin/hide/rind/peel) with a "leather" nuance, 革 "leather"; titles do not share a word («кожура; шкура» vs «кожа (выделанная)») and the 皮 body teaches the contrast — conservative (harmless; unjustified if strictly judged by titles; no change requested).
- 肌→表, 肌→面: 肌 JMdict sense 3 "surface; grain; texture"; 表 sense "surface/outside", 面 "surface"; 肌 title «фактура поверхности» vs 表 «…; поверхность» / 面 «поверхность; …» — conservative (real basis, necessity unestablished; EN's 肌→表面 retained).
- 職→勤め: JMdict 勤め "service; duty; … employment/job"; 職 «работа по найму» vs 勤め «служба» — conservative.
- 考慮→尊重: 尊重 title segment «учёт» equals 考慮 «принятие во внимание; учёт» sense — required.
- 考え→意見: body teaches «мнение» (考えを聞く); 意見 «мнение» — required. 考え→見解: 見解 «точка зрения; позиция», body teaches 考え as «взгляд» — conservative. 考え→考える: derivational noun/verb pair (JMdict 考える "to think"); no defensible-answer overlap (different part of speech and title) — unjustified but harmless; optional to drop.
- 維持→支える: JMdict 支える "to support; to prop; to sustain"; 維持 "maintenance; preservation"; the 維持 body never teaches 支える and the primary sense is physical — conservative.

Optional:
- 考え body teaches 考えがある = «есть идея, есть план»; 計画 «план; планирование» and 案 «предложение; проект» (both with 考える/提案 guards) have no direct pair with 考え. EN has none either; I do not consider it required.
- 絶対 body teaches 絶対に+negative «ни за что не»; 決して «никогда не; ни в коем случае не» / 全然 «совсем не» are near; EN has the same gap; optional conservative guard 絶対→決して.
- 肌 «кожа (тела)» vs 革 «кожа (выделанная)»: qualified titles distinguish them; no guard needed.

Limits:
- Title screening was by Russian-term pattern plus the named clusters, not an exhaustive pairwise comparison of all 2,533 titles; no new card was found to equal another card's whole title or title segment without a guard (羽 «крыло» = 翼 is guarded on 羽; 綿 «хлопок» segment of 木綿 is guarded; 絶対/必ず/ぜひ guarded; 考慮/尊重 guarded; 絵画→絵 guarded).
- Quiz acceptability is judged from titles and article senses, not from the app's actual option generation.
- Linguistic correctness and comprehensibility (other reviewers' facets) were not assessed beyond what bore on consistency.

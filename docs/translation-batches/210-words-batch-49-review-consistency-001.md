# B210 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `9d9c00961ef457eac80eb8f37e9ca7e8522245fa` (tree `6ee737bce5f742105ab95f7cffbfb99f12dd0bde`),
> the signed candidate pushed before review.
> Later reconciliation is in `210-words-batch-49-recheck-001.md`.

Snapshot: RU `9d9c00961ef457eac80eb8f37e9ca7e8522245fa` (branch `full-ru-210-words-49`); `git rev-parse HEAD` matches and `git status --porcelain` is empty (no uncommitted changes). Parent `f28fc34`. Frozen EN `6af98cb`. Nothing was modified, staged or checked out; no generator was run. The one file written besides this report was a scratch dump in FILES (`b210-cons-scratch2.txt`), deleted afterwards.

Scope:
- Read in full (front matter and body, against EN front matter/headings/link sets, plus full text of the RU side): all 30 new cards `words/` 年間 年月 年寄り 年代 いつでも 常に 年中 平等 平均 平和 幕 常識 帰宅 帯 差別 巨大 巣 大陸 州 嵐 岩 屋根 届く 居間 居眠り 居る 就職 就く ボーイ 少年.
- Read in full (complete `git diff -U0`): all 22 navigation files (`kanji/和 均 居 州 帯 平 等`; `words/使用 区別 外出 戦争 等しい 繭 職業 莫大 軒 辞める 通じる 進学 達する 陸 青年`). 35 restored links confirmed (和 3, 居 3, 平 3+3, 均 2, 州 2, 帯 2, 等 2, 15 word files 1 each).
- `manifest.json`: diff and independent SHA-256 recomputation. Intake `docs/translation-batches/210-words-batch-49-intake.json`: path list and candidate hashes only (structure, no learner content read).
- Tools: `python tools/validate.py` (0 errors), `link_parity.py` on the 22 navigation files, my own scripts for title-segment collisions, exclusions on both sides, and a corpus-wide EN/RU link-count scan for the 30 titles across `words/ kanji/ articles/`.
- Comparator cards: titles and `quiz_exclusions` of all ~75 listed comparators read; collisions screened against ALL RU word titles by exact segment match.
- Reviewer model: not verifiable from inside this session.
- Facets covered: consistency, quiz safety, cross-file integration. Linguistic correctness and comprehensibility of prose were not assessed beyond what consistency needed.

Verdicts:
- Consistency (format, front matter, terminology, links, navigation-only files, manifest, intake, no stray files): CLEAN.
- Quiz safety: NEEDS FIX (one minor missing guard, F1; the rest optional). All EN exclusions are retained; every RU-introduced entry has a real basis.
- Cross-file integration: CLEAN.

Findings:
- F1; minor; quiz safety; `words/屋根.md` front matter (lines 1-9, no `quiz_exclusions`); 屋上 «площадка на крыше» vs 屋根 «крыша».
  - Claim and impact: in Russian, «крыша» is the ordinary word for a rooftop as well ("пойти на крышу"). With 屋上 shown, 屋根's title «крыша» is a defensible correct meaning. EN titles "rooftop" and "roof" are distinct, so EN had no guard. The problem is Russian-specific and neither side declares the pair. The cards themselves treat them as one-term-apart (屋根 body line 25 and 屋上 body).
  - Remedy: add after the `tags:` line of `words/屋根.md`: `quiz_exclusions: [屋上]` (a single direct pair; the app applies it symmetrically). Regenerate the manifest afterwards.
  - Evidence: JMdict 屋根 (1182700) "roof"; 屋上 "rooftop; housetop". 屋上 RU card has no exclusions. 屋根 article says the two name "related places, not one and the same structure", which is acknowledged in prose but not enforced for quiz.
  - Confidence: medium. Severity is minor because the correct answer remains more specific and the main EN-derived defence (separate English glosses) is absent only in Russian.

Classification of every RU-introduced `quiz_exclusions` entry (all absent from EN):
| Card → entry | Dictionary basis | Necessity |
|---|---|---|
| 年寄り → 老人 | JMdict 年寄り 1598750 s1 "old person; elderly person"; 老人 s1 "old man; old person; elderly person" (EN titles identical, "elderly person"). Russian «старый человек; человек в годах» vs «пожилой человек». | required |
| 平等 → 等しい | JMdict 平等 1507670 "equality; impartiality; evenness" (the card teaches the な-adjective 平等な, i.e. «равный»); 等しい "equal; equivalent; identical". Shared 等. | conservative (real basis; 平等 as adjective makes «равный» defensible but unestablished in an ordinary quiz) |
| 平和 → 世界 | Titles collide: «мир (отсутствие войны)» vs «мир». JMdict 平和 "peace; harmony", 世界 "the world; society; the universe". Russian-only homonym; the card's own line 28 warns about it. | required |
| 帰宅 → 帰る | JMdict 帰宅 1221430 "returning home"; 帰る "to return; to go home". Titles «возвращение домой» vs «возвращаться домой» (same root, verb/noun). | required |
| 帰宅 → 帰り | JMdict 帰り 1221250 "return; coming back; way back". Titles share «возвращение». | conservative (shared segment, differing focus; the card body itself separates them) |
| 居眠り → うとうと | JMdict 居眠り 1231890 "dozing; nodding off"; うとうと "dozing; drowsily". EN titles identical, "dozing; nodding off"; EN had no guard. Russian «дремота сидя» vs «дремать; клевать носом». | required |
| 居る → いらっしゃる | JMdict 居る おる (1577985) s1 "to be (humble)"; いらっしゃる "to be; to come; to go (honorific)". Shared sense "be"; register differs only by title label. Existing project precedent: いる/いらっしゃる/おいでになる are mutually guarded. | conservative-leaning-required |
| 居る → おいでになる | JMdict おいでになる "to be (honorific)". Title segment «находиться» equal. | conservative-leaning-required (same precedent) |
| 居る → 参る | JMdict 参る s1 "to go; to come (humble)". No shared sense with 居る "be"; only the shared humble register; 居る body never mentions 参る; no EN card pairs 参る with いる. | unjustified (topical/register relation; harmless over-exclusion; see Optional) |
| 就く → 習う | JMdict 就く 1331530 s4 "to study (under a teacher)"; 習う "to learn (from a teacher)". Titles «учиться у наставника» vs «учиться у преподавателя». | required |
| 就く → 就職 | JMdict 就く s1 "to take up (a post); to assume (a position)"; 就職 1331670 "finding employment; taking up a post". | required |
| 就く → 座る | Article teaches 席に就く = «занять место» (Weblio 着く, Kotobank 就く cited), not a JMdict sense 1/4 of the card. 座る «садиться; сидеть». | conservative (real basis in the article; title «вступать в должность; учиться у наставника» does not itself list «садиться») |
Retained EN-sourced exclusions all present and unchanged: 年間 [年, 毎年]; 年月 [月日]; 年代 [時代]; いつでも [いつも]; 常に [いつも]; 年中 [いつでも, いつも, 常に]; 平和 [穏やか]; 幕 [カーテン, 終わり]; 巨大 [莫大]; 州 [大陸]; 嵐 [騒ぎ]; 岩 [石]; 届く [着く, 至る, 達する]; 居る [いる]; ボーイ [男の子, 男子]; 少年 [男の子, 男子, 青年, ボーイ]. The front-matter diff against EN shows only the additions in the table above.
- Title-collision screen (all RU word titles, exact segments): shared segments exist only for 年代/時代 «эпоха», 常に/いつも «всегда», 平和/世界 «мир», 居る/いる/いらっしゃる/おいでになる «находиться/быть», ボーイ/少年/男の子 «мальчик». Every pair is guarded on at least one side. No other new title equals another card's title or segment.
- Reverse scan: no existing RU card lists any batch word in its `quiz_exclusions` that this batch needed to retain or that conflicts (all hits were substring noise from 非常に).
- No Russian-only links were added: every RU card link set is a subset of EN. The dropped links (一生, 公平, ベルト, 少女 and kanji 巨, 根, 岩, 届) have no RU file, so unlinked text follows convention. All relative links resolve.
- Navigation: every change is a bracket/href at an EN-linked position; hrefs are correct (`../words/X.md` from kanji, `X.md` from words); no prose, whitespace or line-ending change (`git diff --check` clean). A corpus-wide scan found no remaining EN/RU link-count difference for any of the 30 titles in `words/ kanji/ articles/`, so no restoration is missing.
- Manifest: 76 changed lines = `contentVersion` + 22 modified hashes + 30 new entries (×1 line each, +22 hash replacements); every entry for changed or new files matches its file's SHA-256 (118 `strokes/*.json` hash differences against raw file hashes are unchanged by this batch and presumably reflect the generator's line-ending normalisation; not a candidate defect). `validate.py`: 0 errors.
- Intake: 52 payload paths = the 30 new + 22 navigation files in the content diff, exactly; every `candidateRawSha256` equals the file's SHA-256; no learner content added.

Optional:
- O1 (`words/居る.md`): the `参る` entry is unjustified on dictionary grounds (see table); dropping it (`quiz_exclusions: [いる, いらっしゃる, おいでになる]`) would keep the distractor pool larger. Retention is harmless; I do not require removal.
- O2 (`words/差別.md`): 差別 body line 14-15 teaches the neutral sense «различие», JMdict 1291410 s2 "distinction; differentiation", which matches 区別 «разграничение; различение» and 違い «различие; разница». EN has the same titles and no guard, and the Russian title «дискриминация» is narrower, so I rate this optional: `quiz_exclusions: [区別, 違い]`.
- O3 (`words/いつでも.md` / `words/常に.md`): the in-batch pair «в любое время; когда угодно» vs «всегда; постоянно» is unguarded (JMdict both gloss "always"); EN is the same and 年中 guards both against each other's cluster, so this is not required. If wanted: `常に` add `いつでも`.
- O4 (`words/帰宅.md`): 戻る «возвращаться» is a weaker defensible answer for «возвращение домой»; EN and 戻る exclude 帰る/帰り only. Not required.

Limits:
- Pre-existing differences in navigation files, outside this batch: `kanji/和.md` (links `味`) and `kanji/居.md` (links `いる`, `今`) have RU-only links relative to EN, present identically in parent `f28fc34`; reported by `link_parity.py` as EXTRA and untouched here.
- Dictionary senses cited above come from the card sources and prior knowledge of JMdict glosses; I did not re-fetch each entry, so the sense-level basis for RU-introduced pairs is confident but not freshly re-verified online. Quiz necessity is a judgement about an unseen quiz presentation.
- The app (`Words.kt`) was not read; I relied on the contract stated in the review prompt (direct, symmetric, non-transitive pairs).
- Stroke-file hash differences noted above were not investigated further.
- Linguistic correctness, scoped coverage and comprehensibility of card prose were outside this facet.

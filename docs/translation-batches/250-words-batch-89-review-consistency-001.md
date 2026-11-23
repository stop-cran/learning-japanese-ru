# Batch 250 (250-words-batch-89) — Consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `4a5e70f1dff84c8e692a1d3c7f9c7c7bd01ce45c` (tree `bd733755f1232bb0d1e2ece9ccb4a0a15b5eeba6`),
> the signed candidate pushed before review.
> Later reconciliation is in `250-words-batch-89-recheck-001.md`.

## Snapshot
- Repo `learning-japanese-ru`, branch `full-ru-250-words-89`, commit `4a5e70f1dff84c8e692a1d3c7f9c7c7bd01ce45c` (parent `9f5e709`). Working tree was clean at start and at end. An in-memory manifest check briefly created `tools/__pycache__`; I deleted it.
- `python tools/validate.py`: 0 errors.
- Manifest: `build_manifest(Path('.'))` run in memory equals `manifest.json` (contentVersion `bddfd3e4d9e4aa9d`). Current.

## Scope
- Read in full: all 30 new RU cards, each against its frozen EN original. Read all 15 navigation-only diffs.
- Scripted checks: front matter against EN, link sets, footers and JMdict numbers, headings, and the intake path list.
- Quiz safety: classified the 18 RU-introduced exclusions and read their target cards' titles and exclusions.
- Not done, or done only partly:
  - No exhaustive title-segment screen across all 3,600+ RU titles. I ran a pattern screen of related titles, a masked-link body mention scan of the 30 cards, and `word_title_screen.py`. I only began reading the latter's noisy output.
  - Line-by-line EN-position parity for the other unlinked mentions in the 15 navigation files was not completed. The diffs themselves are link-only.
- Model: not verifiable.

## Verdicts
- CONSISTENCY: PASS. No High or Medium findings.
- QUIZ SAFETY: PASS. No missing required guard was found. One optional addition and some conservative guards are noted below.

## Findings

| ID | Sev | Facet | Location | Claim | Remedy | Evidence | Conf |
|---|---|---|---|---|---|---|---|
| F1 | Low | Quiz | `words/特長.md` (`quiz_exclusions`) | The RU-added `長短` guard is not needed. 長短 means «длина; достоинства и недостатки», and 特長 means a strong point. | Optional: drop `長短`. Harmless if kept. | 長短 title «длина; достоинства и недостатки» shares no gloss with 特長. | Med |
| F2 | Low | Quiz | `words/特長.md` (`節`, `武器`) | `武器` is justified (title «сильная сторона»). `節` is conservative: its title «примечательная черта» is close to 特長. | None needed. | Titles of 武器 «оружие; сильная сторона» and 節 «…примечательная черта». | Med |
| F3 | Low | Quiz | `words/楽器.md` (`器具`) | Conservative. Both titles contain «инструмент», but 楽器 is the musical instrument and 器具 is a tool or apparatus. The guard is harmless and arguably helpful. | None. | 器具 title «инструмент; прибор; утварь». | Med |
| F4 | Optional | Quiz | `words/生ずる.md` and `words/呼ぶ.md` | Both titles contain the segment «вызывать» (生ずる «возникать; порождать; вызывать», 呼ぶ «звать; вызывать»). Senses differ: 呼ぶ is "summon", 生ずる is "cause". A guard could be added for safety, but not requiring one. | Optional guard `呼ぶ` on 生ずる. | Title overlap. 呼ぶ body teaches call, summon and invite only. | Low |
| F5 | Optional | Consistency | `words/献立.md`:32–34 | The RU body adds a sentence saying the card is marked `kango` "по онному первому элементу, как принято в этом репозитории". EN:27 only says it is a mixed on-first reading, not ケンリツ. This is a meta-remark with no EN counterpart. It is not wrong, but it is extra. | Optional: trim to match EN. | EN:27 versus RU:32–34. | Med |

### Checks that passed (no finding)
- **Intake JSON:** it has 45 payload paths. Together with the intake file itself and `manifest.json`, that equals the 47 changed paths exactly. `held` is empty, and it has no learner content.
- **Navigation files (15):** the diffs are link-bracket and href wraps only, with no prose change. The hrefs use the correct form (`../words/X.md` in kanji files, `X.md` in word files). All targets exist.
- **Links:** none of the 30 new cards has a broken or RU-only link. The links dropped relative to EN all had absent RU targets and stay plain text, per convention:
  - 生える → 枯れる
  - 学科 → 学級
  - 甘やかす → kanji/甘
  - 瓶詰 → kanji/瓶, kanji/詰
  - 怪しい → kanji/怪 and `ayashii-and-related-words.md`
  - 倉庫 → kanji/庫
- **Front matter:** identical to EN apart from the exclusions listed below. No dropped EN guard. Footers and JMdict numbers are identical to EN in all 30 cards.
- **Headings:** they match `# 字（reading）— title`.
- **Duplicates:** the titles of the 30 new cards are unique among the RU word titles screened. 生じる and 生ずる share the title «возникать; порождать», but this pair pre-dates the batch. The «вызывать» difference is noted in F4.
- **Footer separators** (colon versus comma): both forms are widely used in RU, so this is not a defect.

### RU-introduced exclusions (12 cards, 18 distinct targets) — classification
- **Required (shared gloss or dictionary basis):**
  - 生る→実, 収穫: the 生る body is about bearing fruit.
  - 瓶詰→缶詰: both mean canning or bottling.
  - 学科→学問: 学問 «научная дисциплина» versus 学科 «учебная дисциплина».
  - 特定→具体: the title meanings «конкретный» and «конкретность» overlap.
  - 特色→癖: shared word «особенность».
  - 特長→武器: shared sense «сильная сторона».
  - 特売→発売: close sale terms.
- **Plausible or conservative:**
  - 独り言→会話, 話: 独り言 begins with «разговор…».
  - 指定→示す, 定期: 示す is the «указывать» overlap; 定期 shares the 定 kanji.
  - 危うい→重体: they differ, but the neighbouring sense is close.
  - 物置→押し入れ, 貯蔵: storage vocabulary.
  - 特長→節, 長短, 楽器→器具: F1–F3.
- **Unjustified:** none that could mislead. Exclusions are symmetric in the app, so no reverse declarations are required.
- **Missing guards:** none required. Stem-only neighbours (あげる/くれる/与える, 見せる, 預かる/預ける, 疑う, 売れる) have clearly different titles, so I did not add them. Same-batch pairs 琴–生け花 and 生る–生える have distinct meanings and are fine unguarded.

## Optional
- 現に: the title does not signal the register of the word. EN does not either. Polish only.
- 特定: the title's «выявление» covers the 特定する sense only indirectly. The body teaches it clearly. Polish only.

## Limits
- Read-only: no generators were run. I did not read the BLIND-excluded material (other FILES content, translation-batches, translation-drafts, tracking, or scratch worktrees), apart from the permitted intake path list.
- The title screen and the other-mention parity checks are partial, as described under Scope.
- Dictionary bases rest on my own JMdict knowledge, not a live lookup.

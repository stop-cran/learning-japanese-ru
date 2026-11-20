# B197 blind learner-comprehension review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `grok-4.7`
> (Grok family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `5dd9a78f4e6d2f806be09953326bf77cb8e77c47` (tree `aa153ae4edbd312c5336da1a9ad2a142f9433e60`),
> the signed candidate pushed before review.
> Later reconciliation is in `197-words-batch-36-recheck-001.md`.

Snapshot: 5dd9a78f4e6d2f806be09953326bf77cb8e77c47 on full-ru-197-words-36 (parent 59b6e51); git status --porcelain empty. Frozen EN source 6af98cb. No uncommitted changes.
Scope: comprehensibility and scoped coverage of the 30 new cards words/{結論,結果,直,今に,やがて,いずれ,結局,経由,営業,経営,経つ,組合,組む,態度,位置,地位,立場,位,段,級,納得,精々,粉,籠,範囲,節約,節,管,答案,筆}.md, each read against its EN original. Named comparison cards were used only to check contrasts, not reviewed as articles. Model: not verifiable from this runtime.
Verdicts: comprehensibility NEEDS FIX; scoped coverage CLEAN. No per-article coverage exception.

Findings:
1. Minor; comprehensibility; words/節約.md:37; the added model 手間を省く has no kana reading, while 省く（はぶく） on the same line does. A beginner cannot pronounce the collocation the card offers as the labour/steps sense of 省く. The Russian gloss «сэкономить силы» is present, so the gap is pronunciation, not meaning. This sentence is not in the EN card. Remedy: 手間（てま）を省く. Evidence: Jisho/JMdict 手間, reading てま, JLPT N3, noun sense "time; labour; effort" (https://jisho.org/api/v1/search/words?keyword=%E6%89%8B%E9%96%93). RU copilot-instructions.md:101 asks for a reading where an unfamiliar word needs one. Confidence: high.
2. Minor; comprehensibility; words/組合.md:18; the bold teaching pattern **組合の会員** has no reading, while the paired pattern in the same sentence, **組合に入る**（くみあいにはいる）, does. The gloss «член ассоциации» is clear, but the learner cannot read the model. EN line 16 has the same omission; the defect is the RU learner text, not a lost EN point. Remedy: **組合の会員**（くみあいのかいいん）. Evidence: Jisho/JMdict 会員, reading かいいん, JLPT N3, noun "member" (https://jisho.org/api/v1/search/words?keyword=%E4%BC%9A%E5%93%A1). Confidence: high that the reading is absent and that the parallel pattern makes the omission inconsistent; impact stays minor because the gloss is already there.

Optional:
- words/節.md:22 translates 不思議な節 as «что-то странное»; line 42 then says the word points to a noteworthy aspect. The joint, tune, and notable-point senses are taught. EN does the same. Not a defect.
- words/結果.md:17 glosses 調べた結果 as «в результате проверки», but line 20 translates the example as «Разобравшись, мы выяснили причину». The next sentence restores the check-to-finding link. Tense is not reversed. Aligning the example with the card's own gloss would be polish.
- words/籠.md:20 «Птица вылетела из клетки» adds flight to 出ました. EN says "came out." The basket/cage split is otherwise clear (line 38–40). Polish only.
- words/管.md:38 «Чтение くだ подтверждает именно словарная запись ниже» is residual meta wording. The EN community-list note was removed. It does not misstate the reading.
- words/経由.md:4 «путь через» is slightly awkward; «через (промежуточный пункт)» and the body are usable.
- words/経つ.md:4 «истекать (о времени)» is bookish; the examples use ordinary «прошло». The parenthesis keeps the title from meaning a liquid.
- 直 / 今に / やがて share a "soon" gloss and do not name one another. Unique senses are still recoverable: 直 is a short wait (words/直.md:21); 今に also looks back to the present (words/今に.md:21–23) and is not 今にも; やがて does not fix one interval and can compress years (words/やがて.md:21–23); いずれ keeps the separate "which" sense (words/いずれ.md:16–20) and does not promise immediacy. 結局 / 結果 / 結論, the six position/rank cards, and the other named pairs (営業/経営, 経つ/過ぎる/過ごす, 態度/様子/行儀, 納得/承知/理解, 精々/できるだけ/なるべく, 節約/けち/貯金, 答案/答, 筆/ペン, 籠 basket vs cage, 粉, 組合/会) are distinguished in prose. 範囲 vs 幅 has no prose contrast; titles differ («рамки; охват» vs «ширина; диапазон») and quiz_exclusions already lists 幅. EN also has no prose contrast. Not required to answer 範囲's own question.
- No English leftover that the learner must know, no Cyrillic transliteration of a Japanese reading, and no app-quiz behaviour sentence found in the 30 cards. JLPT in words/級.md is an accepted term.

Limits: Jisho was opened for the two findings only; dictionary IDs printed inside the cards were not re-fetched. word_title_screen.py stem hits (время, место, человек, степень, работа) were false leads, not collisions. The pre-existing counter shorthand «ранг 位（い）» in articles/numbers-and-counters.md is a different entry from noun 位（くらい）; words/位.md:43 already separates 一位（いちい）. Link-only edits in existing files were not reviewed as new teaching text. Correctness of Japanese grammar and quiz-exclusion completeness are outside these facets. This review did not read author reports, other reviews, or RU docs/translation-batches/.

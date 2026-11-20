# B207 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `ec1539c9b30591d1c207da84d96fa008d29c8e80` (tree `612e941814aefda3a8cbcf6072c15b22ba72bae2`),
> the signed candidate pushed before review.
> Later reconciliation is in `207-words-batch-46-recheck-001.md`.

Snapshot: RU ec1539c9b30591d1c207da84d96fa008d29c8e80, compared with parent 22823d6dd0491063fe3397e39ca7b4cab1b50dfc; frozen EN source 6af98cb. HEAD matched and git status --porcelain was empty both before and after review. No repository files written; only this report.

Scope: Batch 207 correctness and scoped coverage. Model identity not independently verifiable. Read in full, including front matter, all examples, notes and citations, against the full frozen EN original, file by file:
- words/不利.md — full RU + EN.
- words/損.md — full RU + EN.
- words/握手.md — full RU + EN.
- words/握る.md — full RU + EN.
- words/交換.md — full RU + EN.
- words/両替.md — full RU + EN.
- words/換える.md — full RU + EN.
- words/提出.md — full RU + EN.
- words/描く.md — full RU + EN.
- words/掴む.md — full RU + EN.
- words/掲示.md — full RU + EN.
- words/推薦.md — full RU + EN.
- words/捕まる.md — full RU + EN.
- words/振る.md — full RU + EN.
- words/指す.md — full RU + EN.
- words/持ち上げる.md — full RU + EN.
- words/抱く.md — full RU + EN.
- words/抱える.md — full RU + EN.
- words/抜ける.md — full RU + EN.
- words/抜く.md — full RU + EN.
- words/投票.md — full RU + EN.
- words/批評.md — full RU + EN.
- words/批判.md — full RU + EN.
- words/扱う.md — full RU + EN.
- words/手術.md — full RU + EN.
- words/手品.md — full RU + EN.
- words/戻す.md — full RU + EN.
- words/或.md — full RU + EN.
- words/我慢.md — full RU + EN.
- words/我々.md — full RU + EN.

Also reviewed the changed navigation hunks, not the complete pre-existing articles, in kanji/{抜,抱,術}.md and words/{叩く,攻撃,替える,有利,苦しむ,評価,震える}.md. All 16 additions resolve, occur in the corresponding EN sources, and leave the existing visible text unchanged. Read the three binding RU instruction/reference files. No author/reviewer reports, batch records, drafts or tracking ledger were consulted.

Verdicts:
- Correctness: NEEDS FIX — C1 in 提出. No other Japanese/Russian factual defect established in the 30-card scope.
- Scoped coverage: NEEDS FIX — C2, limited to the requested verbatim Japanese-reading preservation. No omitted sense, teaching rule, example, citation or required existing-target EN link established.
- Russian comprehensibility and exhaustive quiz-pool ambiguity: outside assigned facets; no verdict.

Findings:
- C1; low severity; correctness; words/提出.md:15. The definition after the colon, «то, что представляют или сдают», denotes the submitted item, whereas 提出 denotes the act of submitting it. This introduces an object/action confusion into an otherwise correct explanation. Replace the first sentence with: «提出 — существительное со значением „подача, сдача чего-либо“.» Keep the following sentence about 提出する. Evidence: frozen EN words/提出.md:15 defines “submitting or handing something in”; JMdict/Jisho sense 1 lists presentation/submission/production/filing/turning in (https://jisho.org/api/v1/search/words?keyword=%E6%8F%90%E5%87%BA); Digital Daijisen explicitly defines the action as 「書類・資料などを…差し出すこと」 (https://kotobank.jp/word/%E6%8F%90%E5%87%BA-574292). Confidence: high. Status: unresolved; no content edited.
- C2; low severity, source-fidelity only; scoped coverage; words/不利.md:29, words/握手.md:29, words/批評.md:27–28, words/批判.md:29. These passages change source hiragana component readings to katakana despite the explicit verbatim-Japanese requirement. The pronunciations are correct; this is NOT a Japanese reading error. Restore, respectively, «ふ + り», «あく + しゅ», «ひ + ひょう» (and the following standalone «ひょう»), and «ひ + はん», or obtain an explicit exception permitting script normalization. Evidence: frozen EN words/不利.md:29, words/握手.md:30, words/批評.md:24, words/批判.md:31 at 6af98cb, compared directly with the cited RU lines. Confidence: high. Status: unresolved; no content edited.

Verification:
- Inspected actual exact-written-form Jisho/JMdict API entries for all 30 words, including sense restrictions and POS, not search snippets. Initial HTTP 429 responses for nine entries were recovered using paced requests.
- In particular, 描く sense 2 is restricted to えがく; だく and いだく remain separately recorded, with formal/literary physical use marked for いだく. 換える spelling preferences, 捕まる/掴まる usage, and 抜ける sense-dependent transitivity agree with the cards.
- Checked all source metadata. IDs, readings, levels, types, kanji, tags and original exclusions are preserved. Only two new exclusion edges differ from EN: 交換–代わり and 扱う–操作; the corresponding existing RU cards and the relevant dictionary senses support those guards.
- All 30 article-level N3 labels match frozen EN docs/n3-vocabulary-sources.tsv under the vocabulary policy in docs/jlpt-levels.md:202–233. 抱く's source row is いだく, which the card explicitly teaches; lack of a Jisho level on the separate だく entry does not contradict the article-level label.
- Japanese bullet-example text and kana readings match EN; all examples were also read semantically against their Russian translations. All relative links and quiz-reference targets in the 30 cards resolve. EN links to absent RU targets were appropriately retained as plain text.
- Russian contrast checks used actual Kuznetsov dictionary entries: «сдача» sense 2 (https://gramota.ru/poisk?query=сдача&mode=slovari&dicts[]=42), «разменять» sense 1 (https://gramota.ru/meta/razmenyat), «представить» sense 1 (https://gramota.ru/poisk?query=представить&mode=slovari&dicts[]=42), «критика» senses 1, 2 and 4 (https://gramota.ru/poisk?query=критика&mode=slovari), and «операция» senses 1, 3 and 4 (https://gramota.ru/poisk?query=операция&mode=slovari). The adapted contrasts are supported.
- Ran python -X utf8 -B tools/validate.py on the candidate: exit 0, «0 error(s)». No generators, staging or Git writes.

Optional: None.

Limits: No material claim left UNVERIFIED within the stated textual scope. This is not a native-speaker, app/device, media, manifest-generation or exhaustive corpus/quiz audit. The verdicts mean no other actionable defect was established, not proof of exhaustive correctness. The JMdictDB website required authentication; usable dictionary evidence came from the actual Jisho JMdict API entries and the identified Japanese/Russian dictionary entries above.

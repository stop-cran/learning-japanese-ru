# B204 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `c4b6d94520f4755df78422eb4d06805db0b988a1`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 203 tree `20d0232` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `204-words-batch-43-recheck-001.md`.

Snapshot: Candidate staged tree c4b6d94520f4755df78422eb4d06805db0b988a1; reviewed base 20d0232; detached HEAD 5dd9a78f4e6d2f806be09953326bf77cb8e77c47. The candidate is staged/uncommitted relative to HEAD, as expected. Initial and final index/candidate checks and working-tree/index checks exit 0; no untracked files; HEAD unchanged. EN originals read from the supplied frozen 6af98cb checkout.

Scope: Independent blind READ-ONLY review of correctness and scoped coverage. Actual model identity is not independently verifiable. Full RU/EN reading, file by file, completed for every common-sample file:
- words/正式.md — full RU + EN
- words/昼食.md — full RU + EN
- words/お昼.md — full RU + EN
- words/正午.md — full RU + EN
- words/プラス.md — full RU + EN
- words/正.md — full RU + EN
- words/歓迎.md — full RU + EN
- words/歌手.md — full RU + EN
- words/事情.md — full RU + EN
- words/次第.md — full RU + EN
- words/欠席.md — full RU + EN
- words/欠ける.md — full RU + EN
- words/エンジン.md — full RU + EN
- words/機関.md — full RU + EN
- words/機嫌.md — full RU + EN
- words/横断.md — full RU + EN
- words/横切る.md — full RU + EN
- words/権利.md — full RU + EN
- words/様々.md — full RU + EN
- words/様.md — full RU + EN
- words/構成.md — full RU + EN
- words/検討.md — full RU + EN
- words/梅雨.md — full RU + EN
- words/桜.md — full RU + EN
- words/株.md — full RU + EN
- words/栄養.md — full RU + EN
- words/板.md — full RU + EN
- words/松.md — full RU + EN
- words/来.md — full RU + EN
- words/束.md — full RU + EN

Read binding RU instructions and format reference, all changed existing runtime passages, and these existing comparison cards in full: 昼御飯, 昼, 正しい, 本当, 迎える, 喜ぶ, 休む, 原因, 途端, 手段, 組む, 論じる, 食料品, 松竹梅. Other suggested comparison cards were not exhaustively rereviewed. No author prompt/report, title-screen output, other reviewer report, batch records, drafts or tracking ledger consulted.

Verdicts:
- Correctness: NEEDS FIX for words/次第.md (C204-1); CLEAN for the other 29 common-sample cards in the assigned scope.
- Scoped coverage: CLEAN for all 30 common-sample cards. All EN teaching senses, examples, attachment rules, qualifications and dictionary citations are represented; English-dependent contrasts are adapted rather than mechanically copied.

Findings:

C204-1; Minor; correctness / qualification of a Russian-only grammar claim; words/次第.md:31; OPEN.
Claim: The added comparison says that た-форма + 途端に “связывает уже случившееся событие с тем, что произошло в тот же миг”. In a contrast with the following future-action description of 次第, this presents actual past occurrence as the distinguishing rule. The た attachment identifies the preceding event's completion relative to the next event; the whole situation need not be an already-realized past event. This can cause a learner to reject a valid general/nonpast statement or mistake the attachment form for absolute past time.
Remedy: Replace “оно связывает уже случившееся событие с тем, что произошло в тот же миг, часто неожиданно” with “оно подчёркивает момент, когда вслед за одним событием сразу происходит другое, часто неожиданное”. Retain the useful attachment contrast and the 分かり次第、連絡します example. Add the construction source below; the currently cited 次第 entry does not establish a tense restriction for 途端.
Evidence:
- [JMdict-backed Jisho: 途端](https://jisho.org/api/v1/search/words?keyword=%E9%80%94%E7%AB%AF), とたん, noun/adverb sense: “just as”, “as soon as”, “at the moment that”; no past-only restriction.
- [Bunpro: たとたんに](https://bunpro.jp/grammar_points/%E3%81%9F%E3%81%A8%E3%81%9F%E3%82%93%E3%81%AB), actual Structure/About/Examples inspected: Verb[た] + とたん(に); た indicates completion. Its example “青になった途端に飛び出すのは危ないよ。” is a general warning (“It's dangerous to speed off the instant a traffic light turns green”), not a report of two past occurrences. This directly supports the narrow qualification; it does not license ordinary planned requests/promises with 途端.
- The existing RU words/途端.md correctly describes a completion/transition point and sudden development without imposing this absolute-past rule.
Confidence: High for the need to qualify the wording; impact is localized and minor, not an error in the original 次第 examples.

Optional: For evidence traceability, append the comparison-entry IDs when adding Russian-only lexical comparisons (e.g. 原因 1261190, 手段 1328110, 組む 1397590, 論じる 1561620, 食料品 1358680, 松竹梅 1349920), and cite the Russian dictionary for Russian-polysemy remarks. The inspected senses support these comparisons; this is not an additional semantic finding.

Evidence and checks:
- Inspected actual JMdict-backed Jisho entries for all 30 headwords, separating alternative readings/homonyms and Wikipedia objects from the reviewed lexical senses. Also inspected 原因, 途端, 手段, 組む, 論じる, 食料品, 正会員 and 松竹梅. Reproducible entry lookup: https://jisho.org/api/v1/search/words?keyword=<URL-encoded headword>. Checked relevant sense notes including 次第's noun/ます-stem attachments, 様's method/similarity senses, 松's ranking, 梅雨's two readings and 束's distinct archaic つか entry.
- Russian localization checks used actual Gramota entries: [мотор](https://gramota.ru/poisk?query=%D0%BC%D0%BE%D1%82%D0%BE%D1%80&mode=slovari), Kuznetsov sense 1 and Universal Dictionary 1.0; [акция](https://gramota.ru/poisk?query=%D0%B0%D0%BA%D1%86%D0%B8%D1%8F&mode=slovari&dicts[]=42), Kuznetsov's distinct financial and action entries; [питание](https://gramota.ru/poisk?query=%D0%BF%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%B5&mode=slovari), Kuznetsov senses 1–2 and Universal Dictionary 1.0–1.2.
- Main Japanese example sentences and kana strings match EN for all 30 cards. Additional whole-body Japanese-token comparison found no omitted source tokens. Surrounding EN ASCII reading delimiters/Markdown were reformatted to the established RU full-width-parenthesis convention; no claim of byte-identical complete Markdown.
- Front matter retains every EN identity/reading/level/type/kanji/tag and original exclusion. Fourteen cards add exclusions; no source exclusion was removed. These deltas are localization/quiz changes, not a byte-identical metadata claim.
- All original linked labels/targets remain except five intentionally unlinked, currently unavailable RU targets: kanji/梅.md, kanji/栄.md, kanji/板.md, kanji/松.md and words/以来.md. Their Japanese labels and substantive explanations/readings remain. No available EN link was silently dropped.
- Ran `python -X utf8 -B tools\validate.py` directly in the candidate worktree: 0 error(s).
- Manifest membership increases from 4,204 to 4,234 text files, with no removals. All 46 changed runtime files have matching manifest SHA-256 values under LF normalization; non-file manifest metadata/maps remain unchanged apart from contentVersion. No generator run.

Limits: This is not a full-corpus linguistic, quiz-safety, reciprocal-link, native-speaker or device review. Comparison-card reading is limited to the explicit list above. Jisho is a live JMdict-backed service, not a byte-pinned replay of the author's dictionary version, and its API does not expose the cited numeric entry IDs; the review verifies actual spellings/readings/senses rather than claiming fresh numeric-ID provenance. Initial HTTP 429 failures were retried successfully at a paced rate. All 30 candidate/original card pairs were fully read before final verdicts. Only this report was written.

# B206 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `6bfa34bee12a8bc1e805693a49888fb65cfd7331`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 205 tree `84dc60f` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `206-words-batch-45-recheck-001.md`.

Snapshot: RU candidate tree 6bfa34bee12a8bc1e805693a49888fb65cfd7331; base reviewed B205 tree 84dc60f; detached HEAD 5dd9a78f4e6d2f806be09953326bf77cb8e77c47. Includes staged candidate changes, not a new commit. Initial AND final checks: cached index equals candidate (exit 0), working tree equals index (exit 0), no untracked files. Frozen EN source 6af98cb717755690a9ca793e5454a96ebd7a8f9f.

Scope: Independent blind, read-only correctness and scoped-coverage review. Actual model identity is not independently verifiable.
Full RU card AND full EN original read for EACH of these 30 paths:
words/日常.md; words/日光.md; words/日付.md; words/既に.md; words/旗.md;
words/旅.md; words/方向.md; words/方々.md; words/新鮮.md; words/新た.md;
words/断る.md; words/文明.md; words/文字.md; words/文.md; words/敵.md;
words/数字.md; words/数える.md; words/敬意.md; words/教科書.md; words/教授.md;
words/教師.md; words/出身.md; words/故郷.md; words/政府.md; words/放す.md;
words/攻撃.md; words/支店.md; words/支出.md; words/操作.md; words/損害.md.
Also read the binding RU instructions/reference in full; existing 普段 and 新しい cards in full; changed regions of all 17 modified baseline cards (師, 単語, 句, 太陽, 害, 尊敬, 数, 曜日, 生まれ, 生徒, 腐る, 衝突, 被害, 計る, 計算, 議会, 離す). No author/reviewer reports or prohibited batch records read.

Verdicts: correctness NEEDS FIX (放す only; remaining 29 cards CLEAN within this scope); scoped coverage NEEDS FIX (日付 only; remaining 29 cards CLEAN within this scope).

Findings:

C206-01; Minor; correctness / argument structure; words/放す.md:21.
Claim: «Второй пример буквально описывает, как рука отпускает шарик».
The idiomatic translation on line 19 is fine, but this explicitly literal explanation reverses the Japanese roles: 子供 is the topic/agent, 手を is the object, and 風船から identifies what the hand is released from. Making the hand the literal agent and the balloon its object can misteach を/から immediately after the article's argument-structure rule.
Remedy: replace the first sentence on line 21 with «Во втором примере буквально говорится об отнятии руки от шарика: 手を — руку, 風船から — от шарика». Keep the idiomatic example translation unchanged.
Evidence: frozen EN, Meaning: “literally describes releasing one's hand from the balloon”; the unchanged Japanese 子供は風船から手を放しました. Independently inspected Digital Daijisen, はなす【放す】, sense 2, at https://www.weblio.jp/content/放す: «握ったりつかんだりしていたのをやめる», with the structurally matching example «ハンドルから手を放す». Jisho/JMdict 放す also marks the verb transitive (https://jisho.org/api/v1/search/words?keyword=放す).
Confidence: high. Status: unresolved.

C206-02; Minor; scoped coverage; words/日付.md:37–40.
The entire EN comparison with デート has disappeared, including its visible word label. Removing the explanation of English “date” polysemy is appropriate, but the assigned preservation scope specifically includes this comparator and allows it as plain text when the RU target is missing. The current text neither retains nor adapts that named lexical distinction.
Remedy: add «日付 — календарная дата; романтическая встреча, свидание — デート». Leave デート unlinked because words/デート.md is absent. Do not claim that Russian «дата» has a romantic-appointment sense.
Evidence: frozen EN 日付, Distinctive meaning, first two sentences explicitly distinguish 日付 from linked デート. Independently inspected Jisho/JMdict 日付, lexical sense 1 “date; dating”, and デート, lexical sense 1 “date (with someone); (social) outing (for two); date night”: https://jisho.org/api/v1/search/words?keyword=日付 and https://jisho.org/api/v1/search/words?keyword=デート. The latter's separate calendar-date sense does not make 日付 mean a romantic appointment.
Confidence: high about the missing comparator and prescribed preservation scope. Learning impact is localized; this is not an incorrect surviving Japanese example. Status: unresolved.

Verification and evidence:
- Read actual Jisho/JMdict lexical entries for all 30 new spellings, inspecting readings, parts of speech, senses, restrictions and available register flags; distinguished both 方々 entries and both 故郷 readings/entries, and did not treat Wikipedia-definition objects as dictionary evidence.
- Supplemental exact-entry checks: Digital Daijisen 新しい, sense 4㋐, explicitly supplies «新しい魚» for fresh fish (https://www.weblio.jp/content/新しい), supporting the RU-only addition in 新鮮:33–34; 新た, senses 1–2 (https://www.weblio.jp/content/新た), supports the new/afresh explanation; 出身, sense 1 (https://www.weblio.jp/content/出身), supports school/background origin. No actionable defect established in these additions.
- Russian comparisons checked against actual Gramota/Kuznetsov entries: предложение, senses 1.2 and 2.1 (https://gramota.ru/meta/predlozhenie), and считать, senses 1.1–1.3, together with the Japanese 数える/計算 entries (https://gramota.ru/meta/schitat). The added Russian contrasts are supported.
- Mechanical comparison corroborates all 60 main Japanese example sentences and their kana readings match EN. Formatting around the examples is localized; this is not a claim of whole-line byte identity. Stable non-title metadata retained; exclusion differences are additions, with no EN exclusion removed. Dictionary citation IDs/sense labels retained, with extra comparison citations in 文 and 数える.
- No dropped EN link whose RU target already exists was found. Other missing-target links remain visible plain text, consistently with the convention; 日付's completely removed デート label is C206-02.
- All 17 baseline-card changes are link-only. No expanded baseline linguistic audit is claimed.
- Ran the candidate worktree's tools/validate.py with Python -X utf8 -B: 0 error(s). No generator run. Final index/worktree checks remain clean relative to the candidate.

Optional: None.

Limits: This is not a quiz-safety/comprehensibility-facet audit, corpus-frequency study, historical reconstruction or native-speaker certification. Current online dictionary entries were inspected; their historical bytes were not independently reconstructed, and Jisho's API does not expose the numeric JMdict entry IDs (the IDs were compared with frozen EN). Two initially attempted Kotobank numbered URLs redirected to unrelated entries and were discarded as evidence; the relevant Daijisen entries were then inspected successfully on Weblio. An oversized combined tool read was not counted as full-read evidence; all 30 pairs were subsequently returned in bounded, complete reads. No repository file was written, no index/HEAD change made, and only this report was created/updated.

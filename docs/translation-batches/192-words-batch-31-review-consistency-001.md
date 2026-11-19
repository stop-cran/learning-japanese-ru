# B192 consistency and quiz-safety review (batch `192-words-batch-31`)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `dc2c32f8ce8a1308980a4e2b9b85c21cb758b73b` (tree `694386eaa3f4a96a292adaa19ae9e771c2e736bb`),
> the signed candidate pushed before review.
> Later reconciliation is in `192-words-batch-31-recheck-001.md`.

Snapshot: RU `dc2c32f` on `full-ru-192-words-31` (HEAD confirmed, tree clean, parent `4d79f1f`); frozen EN `6af98cb`. No uncommitted changes. My validator/manifest runs left the tree clean.

Scope: Consistency, quiz safety and scoped cross-file coverage. Reviewed all 30 new `words/*.md` front matter and bodies against EN and RU conventions, the 13 navigation-only restorations (diffed line by line), `manifest.json`, and the intake JSON (all 43 payload hashes recomputed against RU files and frozen EN sources). Ran `tools/validate.py` (0 errors, manifest 3879 files), `link_parity.py` on all 43 files, and an EN-wide scan for links to the 30 targets. Screened all titles and exclusion lists of ~100 existing RU cards. Reviewer model not verifiable from inside this session. Not reviewed: Japanese linguistic correctness or Russian prose quality (other facets).

Verdicts:
- Consistency: NEEDS FIX (one minor finding, C1). Front matter is identical to EN apart from title and exclusions. Navigation edits touch only link brackets and hrefs. No missing link restorations to existing RU targets. Manifest and intake are consistent. Validator passes.
- Quiz safety: NEEDS FIX (Q1–Q3 missing direct guards; Q4 is lower-confidence). All 13 EN exclusion entries on the batch cards are retained verbatim. No unjustified additions.
- Scoped coverage (cross-file integration): CLEAN.

Findings:

Q1; Moderate; quiz safety; `words/招く.md:9`, `words/誘う.md:9`; missing direct pairs with 呼ぶ.
- Claim: RU 呼ぶ (title «звать; вызывать») teaches «приглашать» in its body (words/呼ぶ.md, `## Значение`: "呼ぶ означает также **приглашать** человека… 誕生日に友達を家に呼びました"). 招く («приглашать (в гости)») and 誘う («приглашать (с собой)») therefore have 呼ぶ as a defensible second correct answer (and the reverse). The project already guards the same sense for 招待→呼ぶ and 頼む→呼ぶ, so the omission is inconsistent. The EN pair also lacks it, so this is an inherited gap, but the RU rule "учитывайте значения, уже объяснённые в теле старой карточки" applies.
- Remedy: `words/招く.md:9` → `quiz_exclusions: [招待, 呼ぶ]`; `words/誘う.md:9` → `quiz_exclusions: [招く, 招待, 呼ぶ]`.
- Evidence: JMdict 呼ぶ sense "to invite" (RU words/呼ぶ.md body); 招く 1349590 sense 1 "to invite".
- Confidence: high.

Q2; Minor-moderate; quiz safety; `words/語る.md:9`; missing 話す.
- Claim: 語る is «рассказывать; повествовать». RU 話す (title «говорить; разговаривать») teaches «рассказывать» in its body (話す: "рассказывать… 先生に話す — рассказать учителю"). 話す is also listed in RU 語る's own synonym text. The batch guards the weaker noun 話 («разговор; рассказ») but not the verb 話す, which is the closer match.
- Remedy: `words/語る.md:9` → `quiz_exclusions: [話, 話す]`.
- Evidence: JMdict 話す 1562350 senses 1–3 (speak; talk; tell).
- Confidence: medium-high. I found no defensible overlap with 言う/述べる/伝える (their titles and bodies do not teach «рассказывать»).

Q3; Minor-moderate; quiz safety; `words/議論.md:9`; missing 話し合う (and 論じる).
- Claim: 議論.md teaches «обсуждение» and 議論する as the action (body line "Для действия используйте 議論する"). 話し合う («обсуждать вместе») is guarded against 相談 on exactly that «обсуждение» stem, and 議論 is guarded against 相談 for the same reason. So the direct pair 議論–話し合う is the same overlap, left open. 論じる already declares 話し合う but not 議論; its body says 議論する overlaps in meaning.
- Remedy: `words/議論.md:9` → `quiz_exclusions: [論争, 相談, 話し合う, 論じる]` (話し合う is the required one; 論じる lower confidence). Do not add transitive pairs beyond these two.
- Evidence: JMdict 議論 1226160 "discussion; argument; dispute"; 話し合う 1562310 "to discuss; to talk together".
- Confidence: medium (話し合う), low-medium (論じる).

Q4; Minor; quiz safety, noun/verb or generic-stem pairs of the same type already guarded elsewhere in RU. Recommended, lower confidence:
- `words/読み.md:9`: add 読む. 読み «чтение» vs 読む «читать»; precedent 読書→読む in the baseline. → `[読書, 予想, 読む]`.
- `words/調査.md` (no exclusions field): add `quiz_exclusions: [調べる]`. 調査する teaches «расследовать/обследовать», and 調べる is «исследовать; проверять». Precedent: 研究→調べる. Evidence: JMdict 調査 1429120 and 調べる "to investigate".
- `words/説.md:9`: add 説明. The body teaches the «объяснение» sense of 説 (「теория, объяснение, взгляд」), the same string as the 説明 title. → `[意見, 説明]`.
- `words/語学.md` (no exclusions field): consider `quiz_exclusions: [勉強]`. 語学 «изучение иностранных языков» vs 勉強 «учёба; изучение» (shared стем «изуче»; precedent 研究→勉強). Lowest confidence.
- Confidence: medium-low each; the validator does not require any of them.

C1; Minor; consistency; `words/講演.md:37-38`, `words/招く.md:32-33`.
- Claim: both added learner-facing sentences about app test behaviour («поэтому в тестах эти слова не ставятся рядом с 講演»; «В тестах 招待 не ставится рядом с 招く…»). EN has no such sentences, no other RU card does, and they hard-code quiz behaviour that can become stale when exclusions change.
- Remedy: delete those clauses and keep the linguistic distinction. 講演: «演説（えんぜつ）, «речь, выступление», и スピーチ, «выступление перед слушателями», тоже выступления перед публикой, но не обязательно лекции или доклады.» 招く: end the sentence after «招待する（しょうたいする）тоже значит «приглашать».», keeping the 誘う sentences.
- Confidence: medium (convention/consistency, not factual).

Dictionary basis and necessity for every RU addition beyond the EN file (EN-retained entries all present):
- 譲る→負ける: required. Exact title word «уступать» in both («уступать (место)» / «проигрывать; уступать»); JMdict 負ける includes "to yield to; to give in". The article's contrast with 負ける does not remove the label overlap.
- 議論→相談: required. 相談 title «консультация; обсуждение» and body «обсуждение какого-либо дела»; JMdict 相談 "consultation; discussion".
- 講演→スピーチ: required. 講演 body teaches «выступление перед слушателями», identical to the スピーチ title; JMdict スピーチ "speech".
- 話し合う→相談: required. Same «обсуждение» stem; JMdict 相談.
- 語る→話: conservative (real basis: JMdict 話 sense 5 "story" vs 語る «рассказывать»; noun vs verb, necessity unestablished). Accepted; see Q2 for the stronger pair.
- 招く→招待: required. Same root, same action (RU body states it); JMdict 招待.
- 誘う→招待: required-leaning (same «приглашать/приглашение» stem). No entry is unjustified; none guards a mere topical relation or a contrast the article teaches without a label overlap.

Other pairs checked and found not to need guards (given the direct, non-transitive contract): 警告–注意 (retained); 単語/言語/語/語学 against 言葉/日本語/英語 (語→単語/言葉/言語, 単語→言葉, 言語→言葉 present; no defensible pair left); 謎–秘密 (RU title «загадка» avoids «тайна»); 諺–言葉; 止す–止める/諦める (present); 止す–止む (the «(делать)» qualifier disambiguates; optional); 論争–喧嘩 (спор/ссора; the article contrasts 口論); 議長/議員/議会 against 会議/会合/集まり/首相/社長/課長/部長 (distinct labels); 講演–講義/演説 (present); 調子–状態/具合/加減 (present), 調子–気分 (article contrasts; label «самочувствие» not in 調子's title); 課–授業 (present); 課–売り場 (shared «отдел»; the 売り場 label leads with «место продажи»); 読み–読書/予想 (present); 誤解–理解/誤り/間違い (not defensible answers; the article teaches the contrast); 豆/谷–山/川/野菜; 譲る–渡す/売る (present), 譲る–匹敵 (the «не уступать ни на шаг» sense is a different, negated meaning; optional).

Optional: C1 and the weakest Q4 items are nonblocking polish. `words/議論.md` links 相談 with `../words/` while sibling cards use bare `X.md`; both resolve (validator clean), purely stylistic.

Limits:
- Dictionary senses were taken from RU/EN card citations (JMdict entry IDs in the articles) and my knowledge of those entries; I did not re-fetch JMdict pages, so the cited sense wording above is UNVERIFIED against the live entries. Quiz necessity is judged from Russian titles and bodies, not app logs or `Words.kt` behaviour.
- I did not review the author report, other reviewers' reports, or batch records/ledger/progress (out of scope). I did not read `link_parity` EXTRA output beyond noting a pre-existing `kanji/単.md` link to 簡単 that this batch did not touch.
- Consistency of the 13 navigation-only files is confirmed for link brackets and hrefs only, by diff. Prose correctness is out of this facet.

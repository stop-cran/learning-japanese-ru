# B199 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `b99047ab07da1b5364690335e4fede1db79dca76`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 198 tree `80c7336` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `199-words-batch-38-recheck-001.md`.

Snapshot: RU candidate TREE b99047ab07da1b5364690335e4fede1db79dca76 against reviewed B198 tree 80c7336; detached HEAD 5dd9a78f4e6d2f806be09953326bf77cb8e77c47. This is staged, uncommitted content relative to HEAD, not a candidate commit. Initial index/candidate and worktree/index equality checks both exit 0; no untracked files. Frozen EN source: 6af98cb. No repository writes performed.

Scope: Independent blind READ-ONLY review, correctness and scoped coverage separately. Actual serving model is not independently verifiable; no model-family claim is made. Read all 30 RU cards and all 30 frozen EN originals completely:
確実 確かめる 硬貨 破産 砂漠 石炭 情報 知識 知事 知らせ 眺める 眺め 真剣 真似 真っ赤 県 相続 相手 直に 直ちに 直接 ゴール 目標 目的 指導 コーチ 監督 盛り 登山 発車.
Read the relevant binding RU instructions and format reference. Inspected new-card content in bounded card-pair reads and the separate existing-card/kanji patch; manifest changes were not independently audited. Read existing RU 直, すぐに, 確か, 調べる, 教育, 写す, コピー, 案内, ため, まっすぐ, 見る and 盛ん completely; inspected changed comparison passages in the other 11 existing word cards and two kanji cards, not their complete bodies.

Verdicts: correctness NEEDS FIX — localized defects in 盛り, 真似 and 指導 below; no other actionable correctness defect established in the assigned sample. Scoped coverage CLEAN for all 30 cards: source senses, teaching notes, examples, citations and substantive comparison labels are retained or appropriately adapted away from English-only ambiguity; source metadata and original exclusions are retained. CLEAN is bounded, not exhaustive correctness.

Findings:

- C1; Minor; correctness; words/盛り.md:19.
  Claim/impact: 桜は盛りを過ぎました becomes «Сакура уже отцвела», asserting that flowering has finished. The Japanese says the peak has passed; blossom can remain. This changes the event stage and obscures the target meaning.
  Remedy: replace the Russian translation with «Пик цветения сакуры уже прошёл».
  Evidence: frozen EN explicitly says “The cherry blossoms are past their peak”. Digital Daijisen, さかり sense 1, defines the height/peak and its period, not cessation: https://kotobank.jp/word/盛り-509231 . The exact Jisho 盛り/さかり entry, sense 1, includes “peak (e.g. of cherry blossom season)” and “full bloom”: https://jisho.org/api/v1/search/words?keyword=盛り . Kuznetsov, отцвести sense 1, defines «Кончить, перестать цвести»: https://gramota.ru/meta/ottsvesti .
  Confidence: high. Status: unresolved; no edits authorized.

- C2; Minor; correctness; words/真似.md:37–38.
  Claim/impact: the RU-only contrast says 写す and コピー concern making a copy of text/files/images, whereas 真似 is imitation of actions, voice or manner. Stated without a tendency qualifier, this teaches an artificial object-based boundary. Both comparison words have imitation senses; the target's own second sense is also broader conduct, already taught above.
  Remedy: for example, «写す часто употребляется о переписывании или воспроизведении, а コピー — о копиях и копировании. Но значения этих слов не ограничены текстами и изображениями и могут пересекаться с 真似. В первом примере выше 真似 описывает подражание учителю». Cite the comparison entries if retaining this added explanation.
  Evidence: Jisho/JMdict 写す sense 3 is “to imitate; to model after” (https://jisho.org/api/v1/search/words?keyword=写す); コピー sense 2 is “imitation; counterfeit”, while sense 1 includes a song cover, not just text/files/images (https://jisho.org/api/v1/search/words?keyword=コピー). The target 真似 entry also explicitly includes both imitation and conduct (https://jisho.org/api/v1/search/words?keyword=真似). Kotobank's 精選版 日本国語大辞典 写・映 ①(ハ) explicitly includes sound, words, character, state and manner, without claiming their present frequency: https://kotobank.jp/word/写す-440803 . The page's separate Digital Daijisen sense 2 also covers reproducing an object's form, beyond the three listed media.
  Confidence: high for lexical overlap; medium-high for the risk that this unqualified contrast is read as a restriction. No frequency claim is made. Status: unresolved.

- C3; Minor; correctness; words/指導.md:39–40.
  Claim/impact: the RU-only distinction identifies 教育 as «вся система обучения и воспитания» versus 指導 as concrete guidance of a person/group. 教育 is broader, but it does not have to denote the entire system: it can be the teaching/training/upbringing of an individual or employees. The proposed scale boundary misleads and conflicts with existing RU 教育.
  Remedy: «教育（きょういく）— более широкое понятие образования, обучения и воспитания; оно может относиться и к обучению конкретных людей. 指導 подчёркивает руководство их занятиями или действиями». Cite the comparison entry.
  Evidence: Jisho/JMdict 教育 sense 1 includes “training; instruction; teaching; upbringing” and is a transitive する verb: https://jisho.org/api/v1/search/words?keyword=教育 . Digital Daijisen 教育 sense 1 defines intentional development of a person and explicitly exemplifies 新入社員を教育する, not the whole system: https://kotobank.jp/word/教育-52367 . I inspected that dictionary block in the actual HTML; the initial simplified fetch instead foregrounded Nipponica. Existing words/教育.md:15–26 teaches 教育する and 新しい社員を教育します, and its final section expressly allows employee training and home education.
  Confidence: high. Status: unresolved.

Optional: None.

Evidence and completed checks:
- Inspected actual exact-form/readings and lexical senses through the Jisho API for all 30 headwords, separating 直に/じかに from 直に/じきに and 盛り/さかり from 盛り/もり. Initial HTTP 429 responses were subsequently resolved with paced reads. For kana-only entries, inspected reading-only Japanese objects rather than treating missing `word` as missing evidence. Unrelated names/historical homographs were not merged into the teaching identity.
- Source front-matter comparison found no differences in word, reading, jlpt, type, kanji or tags and no removed EN exclusion. All 60 complete source Japanese example sentences occur verbatim in RU. Manual side-by-side reads covered their kana readings, tense, polarity, argument roles and Russian translations. A Japanese-run comparison found no missing source Japanese run; that mechanical check is supplemental, not semantic proof.
- Source URLs omitted as live Markdown links point to nine unavailable RU targets; their visible Japanese labels/content remain plain text with readings as applicable. Existing target URLs and dictionary citations remain. No coverage finding is raised for deliberately not linking absent runtime cards.
- Checked the specifically requested Russian title vocabulary against actual Gramota dictionary entries: обозревать (Babenko, surveying with one's gaze, https://gramota.ru/meta/obozrevat); преемство (Kuznetsov, especially legal inherited succession, https://gramota.ru/meta/preemstvo); несостоятельный (Kuznetsov sense 1 includes a debtor unable to pay, https://gramota.ru/meta/nesostoyatelnyy); тотчас (“сейчас же, сразу”, https://gramota.ru/meta/totchas); безотлагательный/безотлагательно (Kuznetsov, no deferral, including the adverb example, https://gramota.ru/meta/bezotlagatelnyy); лично (Kuznetsov, self/personally and directly, https://gramota.ru/meta/lichno). None establishes an additional title defect.
- Inspected added contrast senses in actual Jisho entries for 堅い, 違いない, 調べる, 案内, 重大, 大変, 写す, コピー, 教育 and 管理. The new 調べる dictionary example reproduces the existing RU 調べる example and is accurate. The じか reading-history claim is supported by Digital Daijisen's actual じか block, 《「じき」の音変化》, at https://kotobank.jp/word/直-25740 .

Limits: Not a separate comprehensibility, complete quiz-pool safety, native-speaker, corpus-frequency or app/device review. Not every suggested baseline comparison card was read; the complete baseline reads are listed above. External dictionaries establish the inspected senses, not unrestricted substitution or relative frequency. The current Jisho service was inspected rather than the exact historical JMdict dump behind the frozen EN attribution; historical entry numbers/dump hashes were not independently recertified. No author/batch/ledger/other-reviewer material was read. No validator or manifest generator was run, and no structural-validation claim is made.

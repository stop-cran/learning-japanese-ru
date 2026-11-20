# B201 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `6e8f38856e4b35ab1e3322e0c66d6e16c5c39c43`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 200 tree `00107e1` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `201-words-batch-40-recheck-001.md`.

Snapshot: RU candidate tree 6e8f38856e4b35ab1e3322e0c66d6e16c5c39c43; base 00107e1; detached HEAD 5dd9a78. Staged, uncommitted content included. Initial and final index/candidate and working/index checks all exited 0; no untracked files at either check. EN comparison: supplied frozen checkout 6af98cb.

Scope: Blind, read-only correctness and scoped-coverage review. Read all 30 complete RU cards and all 30 EN originals: 現状, 現場, 王様, 王子, 王, 率, 独身, 独立, 犯罪, 犯人, 物質, 物語, 物理, 物価, 物事, 父親, 爆発, 燃える, 熱帯, 熱中, 煙, 無視, 無料, 無事, いえ, 寧ろ, 否, ノー, 無し, 無. Read the three binding RU rule/reference files. Inspected actual titles/readings/guards of the assignment's existing comparison cards (plus 布, ねっしん, 幸福); read 焼ける, ねっしん, 大丈夫 and いいえ in full. Inspected all changed passages in the four reused kanji cards and ten reused word cards: changes there only wrap existing Japanese labels in links. Actual model not independently verifiable; no nested reviewers used.

Verdicts:
- Correctness NEEDS FIX: 無し only (C1). No actionable correctness defect established in the other 29 cards.
- Scoped coverage NEEDS FIX under the assignment's explicit every-EN-note retention requirement: ノー and 無 omit source-qualification notes (C2). This is a narrow source-parity issue, not a missing Japanese sense or construction. All other cards CLEAN within this facet.

Findings:

### C1 — Minor; correctness; words/無し.md:31

Claim/impact: The RU-only contrast says «なし говорит только об отсутствии». This is an unrestricted semantic claim, contradicted by the same card's correct evaluative use それはなしです at line 35. A learner could incorrectly reject the explicitly taught “that option is out / unacceptable” sense. The useful distinction between a response word and an absence construction does not justify “only.”

Remedy: Replace line 31 with:

> Русское «нет» служит и ответом на вопрос, и сообщением об отсутствии. Для отрицательного ответа есть, например, いいえ и いえ; в конструкциях Nなしで и Nなしの слово なし обозначает отсутствие N. Об отдельном оценочном употреблении なし — ниже.

Evidence: Inspected [Jisho/JMdict 無し, entry 1529560](https://jisho.org/word/%E7%84%A1%E3%81%97): sense 1 is “without,” noun/suffix; sense 2 is “unacceptable; not alright; unsatisfactory,” colloquial noun. These are precisely the two senses cited by the card. EN words/無し.md:33 also explicitly preserves the nonliteral evaluative use. [Gramota, Kuznetsov, нет](https://gramota.ru/meta/net), sections 1.1 and 2.1, supports the Russian response/absence distinction, but not the added restriction on Japanese なし.

Confidence: High. Localized overstatement; no change to the Japanese examples or title is needed.

### C2 — Minor; scoped coverage, strict source-note parity only; words/ノー.md:33 and words/無.md:40

Claim/impact: Two EN provenance qualifications have disappeared rather than being translated:
- EN words/ノー.md:33 says the source list supplied no English gloss, so the taught interjection/prefix uses are dictionary-supported teaching choices, not a reconstruction of its compiler's intention.
- EN words/無.md:37 says the community list mismatched ぶ with “nothing,” its historical intention remains unresolved, and ぶ/む have independently assigned source rows.

The RU lexical explanations remain sound and keep the readings separate. The omission matters only because this assignment expressly requires every EN note to be retained; it does not establish a learner-facing Japanese error. Do not infer the original compiler's intent from the dictionaries.

Remedy: Restore compact translated qualifications alongside the present explanations, for example:

> ノー: В исходном списке английский перевод отсутствовал. Приведённые здесь употребления как междометия и приставки подтверждены словарём; это учебный выбор, а не восстановление намерения составителя списка.

> 無: В исходном списке чтение ぶ было сопоставлено с не соответствующим ему переводом «ничто»; что имел в виду составитель, остаётся неясным. Для ぶ и む здесь есть отдельные исходные строки, поэтому подтверждённые значения обоих чтений изучаются раздельно.

Evidence: Direct complete EN/RU comparisons at the cited lines establish the missing notes. Inspected [Jisho ノー, JMdict 2080530](https://jisho.org/word/%E3%83%8E%E3%83%BC), senses 1–2: “no” and prefix “no; without; not needed; not allowed.” Inspected [Jisho 無・ぶ, JMdict 2423740](https://jisho.org/search/%E7%84%A1%20%E3%81%B6), prefix senses 1–2 “un-; non-” and “bad ...; poor ...”; the API's separate 無・む entry gives noun “nothing; naught; nought; nil; zero” and negative prefix. These verify the lexical distinction, not the historical list intention.

Confidence: High about the textual omissions; no claim to independent reconstruction of source-list history. If authoring provenance is explicitly exempted from runtime translation scope, C2 can instead be dispositioned optional without changing the linguistic verdict.

Evidence/coverage receipt:
- Read live Jisho/JMdict lexical entries for every new word, including full returned spellings/readings, grammatical classes, restrictions and lexical senses; excluded Wikipedia objects and unrelated homonyms. For ノー, inspected the actual detail page because a word-only API filter did not select its kana-only object.
- Checked added Japanese-word contrasts against actual entries for 状態, 状況, 事態, 熱心, 焼ける, 霧, 大丈夫, 歴史 and 布. The 熱中 に construction, 無視 を construction, 燃える/燃やす argument contrast, physical/emotional 爆発, and the 王/王様 and 父親/お父さん distinctions retain the EN teaching.
- Russian localization checks used actual Gramota dictionary sections: [холостой](https://gramota.ru/meta/kholostoy), Kuznetsov sense 1 and the masculine short form; [материя](https://gramota.ru/meta/materiya), Kuznetsov senses 1/3; [материал](https://gramota.ru/meta/material), Kuznetsov sense 2; [история](https://gramota.ru/meta/istoriya), Kuznetsov senses 2–6; [скоро](https://gramota.ru/meta/skoro)/[скорый](https://gramota.ru/meta/skoryy), speed senses. The adapted warnings about gender, fabric/reference materials, story/history and “скорее” retain useful Japanese distinctions.
- Front matter comparison found no removed source field/value other than localized titles and expanded exclusion lists; all EN exclusion members remain. All cited dictionary IDs and all EN link labels remain. Eleven removed link wrappers point to currently absent RU targets; their visible Japanese words remain and readings are supplied. These are not treated as missing vocabulary explanations or broken links.
- All sentence examples were compared in the complete paired reads, including kana readings, tense, polarity and Russian argument structure. Mechanical bullet projection also matched except three mixed-language bullets in 無 that require the manual comparison already performed; no Japanese example discrepancy established.
- `python -X utf8 -B tools\validate.py` on the candidate: 0 errors, exit 0. No generator was run and no content was edited.

Optional: None beyond the explicitly conditional disposition of C2.

Limits: This is not a corpus-wide quiz-safety or Russian-comprehensibility verdict, a new audit of full reused cards, or native-speaker/device acceptance. Live dictionaries are corroboration, not a replay of archived captures. No author, peer-review, translation-batch/draft or tracking records were read. Source-list historical intent remains unresolved as EN states. Initial Gramota query endpoints returned 429; actual `/meta/` dictionary entries were then read. One Kotobank request resolved to the unrelated pear article and was discarded, not used as evidence. Large combined shell outputs were not treated as full reads; all 30 paired cards and the reused-card patches were subsequently returned in bounded complete reads. Python used `-B`/bytecode suppression; no cache creation was requested. Only this report was written.

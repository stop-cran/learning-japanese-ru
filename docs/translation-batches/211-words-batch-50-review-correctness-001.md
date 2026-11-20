# B211 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `53d6950b1b8c0d254414e1f2ba4d967b2ca3b43a` (tree `154fb77da0097183389a794e442bf915ed34d075`),
> the signed candidate pushed before review.
> Later reconciliation is in `211-words-batch-50-recheck-001.md`.

Snapshot: RU 53d6950b1b8c0d254414e1f2ba4d967b2ca3b43a, compared with frozen EN 6af98cb. HEAD matched and git status --porcelain was empty at both opening and closing; no uncommitted changes included. No repository files were written; no generators, checkout, staging or commits.

Scope: BLIND, read-only CORRECTNESS and SCOPED COVERAGE. Actual reviewer model is not independently verifiable. Every following file was read IN FULL alongside its complete frozen EN original (the prefix is words\ and suffix .md for EACH item):
少女; 小麦; 小屋; 包み; 小包; 小; 専攻; 対象; 対; 審判;
密; 寄付; 宿; 宿泊; 家賃; 家具; 実験; 実施; 実行; 実現;
実は; 宝石; 宝; 宜しく; パス; 券; 定期; 信仰; 宗教; 完成.
Also reviewed the changed 少年 synonyms line against EN and 少女, and the other runtime navigation-only diff. Full RU comparison reads: 女の子, お嬢さん, 彼女, 荷物, 近い, 泊まる, 行う, 仕舞い, 石, 玉, 切符, 経験. Other comparison cards were not exhaustively audited. Read the three binding RU instruction/format files and relevant EN n3-vocabulary-sources.tsv rows. Did not read author/title-screen/reviewer reports, prohibited RU translation records, or the scratch worktree.

Verdicts: correctness NEEDS FIX (C1); scoped coverage NEEDS FIX (C1–C4). No additional actionable defect established in the other reviewed passages; this is not exhaustive certification. C2 is an explicit teaching-distinction/coverage finding, not a claim that the Russian word камень cannot mean a gemstone. Comprehensibility and comprehensive quiz-safety adjudication are outside the assigned facets.

Findings:

C1; Minor; correctness + scoped coverage; words\包み.md:29.
Claim/impact: «[荷物] включает багаж и посылки, завёрнутые так или иначе» replaces EN's “whether wrapped this way or not” with a phrase that presupposes wrapping. It drops the very boundary the comparison is teaching: 荷物 includes carried goods irrespective of this packaging feature.
Remedy: «[荷物](荷物.md)（にもつ）включает багаж и посылки независимо от того, завёрнуты они таким образом или нет».
Evidence: frozen EN words\包み.md:29; existing RU words\荷物.md:15,25,29. Actual [Jisho/JMdict 荷物](https://jisho.org/api/v1/search/words?keyword=荷物), reading にもつ, noun sense 1 (luggage/baggage/package), has no wrapping restriction. Confidence: high. Status: unresolved.

C2; Minor; scoped coverage; words\宝石.md:18–19.
Claim/impact: both examples translate 宝石 only as «камень/камни», the same bare label as current 石 («камень»). The assignment specifically requires the examples to preserve this taught lexical boundary, and EN says “gemstone/gems.” The surrounding explanation does distinguish them, so the defect is localized, not a wrong Japanese sentence.
Remedy: «В это кольцо вставлен синий драгоценный камень»; «Продавец показал мне драгоценные камни один за другим».
Evidence: frozen EN words\宝石.md:18–19,29; current words\石.md:5,44; actual [Jisho/JMdict 宝石](https://jisho.org/api/v1/search/words?keyword=宝石), ほうせき, sense 1 (gem/jewel/precious stone). Counterevidence/calibration: [Кузнецов, камень](https://gramota.ru/poisk?query=камень&mode=slovari&dicts[]=42), sense 2 colloquial subsense, does allow a jewelry mineral. Thus these are intelligible contextual translations; the requested learning distinction, not ordinary Russian grammaticality, motivates this minor finding. Confidence: high on the omitted explicit distinction. Status: unresolved.

C3; Minor; scoped coverage; words\少女.md:4,12.
Claim/impact: the title «юная девушка» does not summarize the childhood part of the selected sense; the body correctly says «девочка или юная девушка», and its first example is a twelve-year-old child. A learner seeing only the title is given the adolescent/young-woman segment instead of the full selected “young girl” sense.
Remedy: title and H1 gloss «девочка; юная девушка». The new 少年 comparison already uses that broader gloss and needs no semantic correction.
Evidence: frozen EN words\少女.md:4,16,18; actual [Jisho/JMdict 少女](https://jisho.org/api/v1/search/words?keyword=少女), しょうじょ, sense 1, girl (usually 7–17)/young lady; [Викисловарь девушка](https://ru.wiktionary.org/wiki/девушка), Russian sense 1, the period of adolescence/youth. This is not a proposed rigid legal age boundary or an objection to the title's otherwise valid translation. Confidence: medium-high. Status: unresolved.

C4; Minor; scoped coverage; words\パス.md:4,12.
Claim/impact: the title lists the ball, exam and file senses, but omits both admission pass and passing one's turn, which EN's broad “pass” and the RU body:16,34 teach. Under this assignment's requirement not to narrow titles below the selected taught senses, those uses should remain visible in the summary too.
Remedy: one possible title/H1 gloss is «пас; сдача экзамена; пропуск (документ; хода); путь к файлу». Keep the existing separate pass/path explanation; do not merge their dictionary identities.
Evidence: frozen EN words\パス.md:4,16,34 and RU:16,34; actual [Jisho/JMdict パス](https://jisho.org/api/v1/search/words?keyword=パス), pass entry senses 1–4, plus separate パス-1 computing-path sense 1. Confidence: high on the omitted selected senses; medium on the best compact replacement wording. Status: unresolved.

Optional: Outside the assigned facets, add kana to RU-only 訓練を行う at words\実施.md:29: 訓練を行う（くんれんをおこなう）. For consistency/navigation, the newly added comparisons could link existing 彼女 in 少女:29, 行う in 実施:29/実行:29, 実際 in 実は:29 and 玉 in 宝石:29; these are not claimed as dropped EN links. Restoring «билет» to 券's title would make its main example more directly recognizable, but I have not established that «талон; купон» is an incorrect Russian summary.

Evidence checks and clean bounded observations:
- Inspected actual live Jisho/JMdict forms and lexical senses for ALL 30 headwords, not just search summaries. パス was inspected separately because its forms contain reading only. Also inspected 彼女, 近い, 泊まる, 行う, 仕舞い, 経験, 実際, 玉, 正直, 完了, 完全, 未完成 and 荷物. Wikipedia/place objects were not used as lexical proof.
- Exact frontmatter comparison found no removed original metadata/exclusions; the only non-title changes were the seven stated RU exclusion additions. These pairs were checked for relevant lexical overlap, not treated as transitive equivalence. All full-stop Japanese examples from EN were retained; manual full reads covered the inline constructions and reading-join scripts too. No dropped EN link with an existing RU target was found. Untranslated-target pointers were correctly left plain.
- Russian dictionary checks inspected [Кузнецов/Грамота](https://gramota.ru/poisk?query=опыт&mode=slovari&dicts[]=42): опыт senses 1/3 support the added experience/experiment contrast. The same dictionary's близкий 5, пожертвование 1, взнос 1–2, размещение 1, ввести 7, график 2, законченный 1 and талон 1 support the relevant qualified choices. Its вердикт entry is specifically jury/legal; JMdict 審判 sense 1 explicitly includes verdict, while the body preserves the broader decision explanation. I therefore do not call «вердикт» false.
- Actual Russian Wiktionary entries checked: [девушка](https://ru.wiktionary.org/wiki/девушка) 4 (romantic partner), [узел](https://ru.wiktionary.org/wiki/узел) 5 together with Грамота узелок→узел (wrapped bundle), [посылка I](https://ru.wiktionary.org/wiki/посылка) 2, [судья](https://ru.wiktionary.org/wiki/судья) 2, [самоцвет](https://ru.wiktionary.org/wiki/самоцвет) 1, [вообще-то](https://ru.wiktionary.org/wiki/вообще-то) 1, [благосклонность](https://ru.wiktionary.org/wiki/благосклонность) 1, [путь](https://ru.wiktionary.org/wiki/путь) 13 (computing), [проездной](https://ru.wiktionary.org/wiki/проездной) 2, [проводить I](https://ru.wiktionary.org/wiki/проводить) 9, [выполнять](https://ru.wiktionary.org/wiki/выполнять) 1 and [исполнять](https://ru.wiktionary.org/wiki/исполнять) 1. These support the contextual Russian choices, not unrestricted Japanese substitution rules. Technical «исполнение программы» additionally confirmed in the actual [Финам dictionary entry](https://dic.academic.ru/dic.nsf/fin_enc/23537), reading the raw HTML because simplified extraction omitted its main definition.
- Source-list remarks remain within the frozen source rows; the extra EN-only realization/English-gloss boundary need not be translated mechanically. No dictionary markup was found leaking into the cards. The reviewed 少年 change is accurate.
- Ran only python -X utf8 -B tools\validate.py in RU: exit 0, «0 error(s)». No generator was run. Structural success does not resolve the editorial findings.

Limits: Several Gramota requests returned HTTP 429; direct Python requests to Wiktionary returned HTTP 403, while web_fetch returned the actual fallback entries above. No conclusions were drawn from those failures. The Wiktionary самоцветный page was a definitionless stub and was not evidence; the noun самоцвет entry supplied the needed sense. One numerical Kotobank URL redirected to unrelated 小付け and was discarded; the correct 小包 page's Nipponica postal article is not proof of an unrestricted lexical exclusion. Consequently, the exclusivity of postal-only «почтовая посылка» in 小包's title remains UNVERIFIED, not an established defect or CLEAN claim; JMdict's parcel/package and the inspected Russian посылка entry do not themselves settle that restriction. Other live dictionary evidence is current, not a byte-pinned recreation of the EN dictionary snapshot; Jisho API does not expose the numeric JMdict IDs, so their retention was checked against EN, not independently reconstructed. No native-speaker, device, teaching-effectiveness, exhaustive corpus, or full independent quiz-pool certification is claimed.

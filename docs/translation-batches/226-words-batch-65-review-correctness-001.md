# B226 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `bebdf808fd419165e2b6098bd25d815f7c41c235` (tree `acea83488c876c2f725c512d68e7db0c9584fba9`),
> the signed candidate pushed before review.
> Later reconciliation is in `226-words-batch-65-recheck-001.md`.

Snapshot: RU bebdf808fd419165e2b6098bd25d815f7c41c235; no uncommitted or ignored files. HEAD and `git status --porcelain --ignored` verified before review and again after validation. Frozen EN verified at 6af98cb717755690a9ca793e5454a96ebd7a8f9f.

Scope: Independent blind, read-only CORRECTNESS and SCOPED COVERAGE review. Actual model identity is not independently verifiable; no other reviewer used. Read the three binding RU instruction/reference files. Each following RU file was read IN FULL against its complete frozen EN original, including front matter, examples, notes and citations:
- words/一流.md
- words/高級.md
- words/高度.md
- words/高等.md
- words/高層.md
- words/挙げる.md
- words/拡充.md
- words/拡張.md
- words/片付く.md
- words/固まる.md
- words/強化.md
- words/激増.md
- words/増大.md
- words/高める.md
- words/おどかす.md
- words/驚かす.md
- words/騒がしい.md
- words/騒々しい.md
- words/馴れる.md
- words/香水.md
- words/養分.md
- words/餅.md
- words/飾り.md
- words/飽くまで.md
- words/飢饉.md
- words/飢える.md
- words/食塩.md
- words/挿す.md
- words/裁縫.md
- words/刺す.md

Also read existing RU うるさい, 驚く, 慣れる and 塩 in full for conventions; reviewed the runtime-only baseline link changes in kanji/刺.md, 固.md, 塩.md and words/アクセサリー.md, 片付ける.md. Other suggested comparison cards were not read in full; their dictionary meanings were checked where relevant, not their complete editorial quality.

Verdicts:
- Correctness: NEEDS FIX — 騒がしい, 騒々しい and 裁縫 as detailed below; CLEAN for the other 27 new cards within this facet.
- Scoped coverage: NEEDS FIX — 挙げる, 驚かす and 強化 as detailed below; CLEAN for the other 27 new cards within this facet. The two title omissions are not claims that the corresponding senses disappeared from the bodies.
- Comprehensibility and full-pool quiz safety: not assigned; no blanket verdict.

Findings:

C1; Minor; correctness; words/騒がしい.md:4,12 and words/騒々しい.md:4,12.
The first title glosses narrow general environmental noise to a noise-producing agent: «шумливый» means inclined to make noise; «галдящий» means speaking/shouting noisily together. Neither is the ordinary general translation of the noisy room explicitly taught in these cards; the latter also introduces colloquial speech-noise specificity. The bodies correctly use «шумный». This is a lexical-range issue, not a requirement to make every title identical.
Remedy: use «шумный; неспокойный (о времени)» for 騒がしい and «шумный; неспокойный (об обстановке)» for 騒々しい, updating both front matter and H1. Preserve/recheck the applicable quiz exclusions rather than manufacture a Russian distinction.
Evidence: Kuznetsov, «шумливый», “Склонный шуметь”, examples children/company/birds: https://gramota.ru/meta/shumlivyy . Kuznetsov, «галдеть», colloquial, “Громко, беспорядочно говорить, кричать всем одновременно”, also birds; the page identifies «галдящий» as its active participle: https://gramota.ru/meta/galdet . Actual JMdict entries 1403000 senses 1–2 and 1596440 senses 1–2 inspected through https://jisho.org/search/騒がしい and https://jisho.org/search/騒々しい ; Daijisen expressly gives noisy room/interior usage, including nonhuman sounds, at https://kotobank.jp/word/騒騒しい-552771 .
Confidence: high.

C2; Minor; scoped coverage; words/挙げる.md:4,12,16–24 and words/驚かす.md:4,12,16–19.
The EN titles deliberately cover two different taught uses: “raise; cite an example” and “surprise; frighten”. RU replaces each with two near-synonyms for only one side: «приводить (пример); перечислять» and «удивлять; поражать». Thus the short learner/answer labels no longer cover the source title's raising and frightening uses, despite retaining 手を挙げる and the frightened-child example in the bodies. A title need not list every peripheral dictionary sense; these are explicit source-title senses.
Remedy: «поднимать (руку); приводить пример» and «удивлять; пугать», respectively, in front matter and H1.
Evidence: the frozen EN counterparts, lines 4,12,23–24 and 4,12,18; actual JMdict 2864818 sense 9 (“raise; elevate”, cross-reference 手を挙げる), sense 1 (cite/list examples), and 1238650 sense 1 (“surprise; frighten; create a stir”), inspected at https://jisho.org/search/挙げる and https://jisho.org/search/驚かす .
Confidence: high.

C3; Minor; correctness; words/裁縫.md:4,12,16.
Unqualified «рукоделие» in the bare title admits knitting and other manual crafts beyond the sewing operation taught here, while also suggesting handwork where line 33 correctly permits machine sewing. The body's «с иглой» helps but does not qualify the independently displayed title. This is not a request to delete the source's needlework concept.
Remedy: title/H1 «шитьё» or «кройка и шитьё»; define the body as «裁縫 — кройка и шитьё, работа по сшиванию ткани» rather than a general craft label.
Evidence: actual Daijisen 裁縫 defines cutting cloth and sewing it into clothing etc., 針仕事: https://www.weblio.jp/content/裁縫 . JMdict 1296200 sense 1, sewing/needlework, intransitive する; https://jisho.org/search/裁縫 . Kuznetsov «рукоделие» sense 1 explicitly includes “шитьё, вязание и т.п.” and manual work: https://gramota.ru/meta/rukodelie .
Confidence: high.

C4; Minor; correctness; words/騒々しい.md:32–35.
The RU gloss defines its assigned category as «словам китайского происхождения с онными чтениями», thereby initially asserting Chinese origin, then says that this very classification is not a historical-origin assertion. EN instead specifies an on-first mixed formation and explicitly suspends settled derivation. The later disclaimer does not make the preceding categorical definition accurate for this uncertain case.
Remedy: «В этой коллекции слово условно отнесено к канго по онной основе そうぞう; しい — японское окончание прилагательного. Это учебная классификация, а не утверждение о доказанном заимствовании всего слова». Retain the following note on competing origins/ateji.
Evidence: frozen EN lines 32–35; actual Seisenban entry and auxiliary etymological note discuss possible 当て字 and competing derivations, including さわさわ and 忩々, at https://kotobank.jp/word/騒騒しい-552771 . This does not establish one derivation as the universal answer.
Confidence: high.

C5; Minor; scoped coverage; words/強化.md:35.
The RU-only contrast introduces unlinked 固める without its reading; no RU 固める card exists. Reading 固まる immediately before it is not the reading of the second verb. This misses the binding rule requiring the reading of an unavailable comparison word, making the newly introduced transitive alternative unnecessarily inaccessible.
Remedy: «…или 固める（かためる）…». No new card or invented link is needed.
Evidence: RU scoped instruction “У слова-сравнения без доступной ссылки укажите подтверждённое чтение рядом с кандзи”; filesystem existence checked read-only; actual JMdict 1266570 lists 固める（かためる）, transitive harden/solidify/strengthen, at https://jisho.org/search/固める .
Confidence: high.

Optional: 飾り's «орнамент» could become «декоративный элемент» for clarity; this is not established as an impossible use of the broad Japanese noun. 高等's «высокого порядка» could become the plainer «высокого уровня»; Kuznetsov «порядок» permits abstract category, so no mathematical-only defect established.

Evidence and retained adaptations: Inspected Jisho/JMdict entries/senses and IDs for all 30 headwords and 39 additional numerical comparison citations; used frozen EN XML where available. Read public JMdict XML in memory for 飽くまで/飢饉/飢える labels/restrictions and 餅's search-only 餠 (omitted by Jisho's API). Inspected Daijisen entries for 高級/高度/高等/高層/香水/食塩/増大/挿す/刺す/餅 and Kotobank definitions for 拡充/拡張 and the competing-origin note.

No defect established for «один из лучших», «элитный» (Kuznetsov sense 2: best/excellent), «наращивание», «приручаться» (Kuznetsov приручиться sense 1), or «сугубо» (Wiktionary: “Сугубо личное мнение каждого”). Actual Gramota entries support «удивить»/«удивляться», «наделать шуму» (Kuznetsov «шум» sense 4), grafting («привить» sense 2), and mosquito biting (Морковкин «кусать» sense 1.3). The mochi description is attested at https://dic.academic.ru/dic.nsf/enc_japan/496/Моти ; actual puffed-rice usage at https://food.ru/products/12265-risovye-hlebcy supports the Russian-only contrast.

Mechanical checks: all source front-matter fields retained except translated titles and four added RU exclusion members (激増→急激, 高める→上がる, 驚かす→驚く, 飢饉→飢える); no EN exclusion removed. All 30 full-stop Japanese example sequences matched EN. No dropped EN link whose RU target exists, and no broken new-card Markdown target, found. Unavailable targets appropriately remain plain text. `python -X utf8 -B tools/validate.py` returned 0 errors. No generator run.

Limits: No full-pool quiz audit, native-speaker certification, frequency study or complete comparison-card review. Gender-neutral Japanese permits the contextual masculine translations; no gender rule is asserted. Live entries do not certify byte identity with the original 2026-10-21 snapshot. Initial Gramota 429s and an authenticated JMdictDB UI were replaced by successful actual-entry/public-XML reads. Initial oversized outputs were replaced by bounded complete card-pair reads. No forbidden author/reviewer reports, RU batch/draft/tracking records or scratch worktrees read. Only this report written; no repository changes, generators, commits, pushes or branch/index operations.

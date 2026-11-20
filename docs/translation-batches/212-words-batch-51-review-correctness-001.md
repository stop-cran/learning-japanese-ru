# B212 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `d5fd0d933b7590c71fceadde93af255a14c4e0c0` (tree `e25b42695c1de0f449a934e1fd3152047e1f92a3`),
> the signed candidate pushed before review.
> Later reconciliation is in `212-words-batch-51-recheck-001.md`.

Snapshot: RU d5fd0d933b7590c71fceadde93af255a14c4e0c0 against parent b16939df273766846f10d8cc6827159eb8db7214; no uncommitted changes. Initial and final HEAD matched the candidate and both git status --porcelain outputs were empty. Frozen EN HEAD independently confirmed as 6af98cb717755690a9ca793e5454a96ebd7a8f9f.

Scope: Independent BLIND, READ-ONLY review of correctness and scoped coverage. Actual model identifier is not independently verifiable in this session. No delegation. Read all three binding RU instruction/reference files.

Full-reading attestation: each following file was read in full against its entire frozen EN original, not just its diff, metadata or excerpts:
words/完全.md; words/完了.md; words/宇宙.md; words/宅.md; words/孫.md;
words/学者.md; words/学ぶ.md; words/学習.md; words/学期.md; words/学.md;
words/学問.md; words/存在.md; words/嫌う.md; words/嫁.md; words/婚約.md;
words/姿.md; words/委員.md; words/奇妙.md; words/不思議.md; words/妙.md;
words/好み.md; words/女王.md; words/俳優.md; words/女優.md; words/奪う.md;
words/奨学金.md; words/奥.md; words/契約.md; words/失業.md; words/失う.md.
All 30 bilingual pairs actually returned in full in bounded reads.

Also read every changed learner-visible line in the 21 existing cards: kanji/了.md, 在.md, 奥.md, 存.md, 孫.md, 宇.md; words/全く.md, 好む.md, 完成.md, 専攻.md, 得る.md, 徹底.md, 欠陥.md, 気に入る.md, 演技.md, 率.md, 王様.md, 習う.md, 観客.md, 語学.md, 謎.md. Compared existing Russian titles/readings across the supplied comparison list; additionally read 研究者, お宅, 奇しい, ある and いる in full. This is not a full rereview of every baseline comparison article.

Verdicts: correctness CLEAN; scoped coverage CLEAN. These verdicts apply to all 30 new cards and the reviewed existing-card navigation changes; no per-article exception. CLEAN means no actionable defect established within this scope.

Findings: None.

Evidence and checks:

- All 60 principal Japanese example sentences AND their complete kana reading strings match EN exactly, including internal kana spacing and katakana. Translations were read individually for polarity, participants, tense/aspect, passive idiom, and resulting states. The manuscript retains the distinction between incomplete solution and complete healing; completed registration versus completing work; aversion-motivated avoidance; engagement versus marriage; being unemployed versus losing employment; and financial support with versus without repayment.
- Japanese sex-neutral nouns were checked separately from contextual Russian gender: 孫 explicitly covers both grandson and granddaughter, plural «внуков» need not mean boys only, 俳優 explicitly includes women, and the 婚約 example does not invent the partner's sex. Masculine first-person Russian past forms are contextual renderings, not claims that Japanese marks the speaker male.
- Nontranslated front-matter fields match EN; all original exclusion members remain. New exclusions are additions, not replacements of EN guards. No broken new-card relative link or dropped EN link to an existing RU target was found. All 31 added links in the 21 existing cards occur as the same label/target in EN; stripping the link wrappers recovers each pre-existing RU file exactly. In particular 完成→完了/完全 and 専攻→学ぶ retain the original sentences and appropriate readings/senses.
- Confirmed that words/会員.md, kanji/委.md, kanji/奇.md and words/王女.md do not exist in RU. Their unlinked mentions are therefore correct, not missing-link findings. Removed English-only gloss-boundary sentences do not remove a Japanese rule. No source-list annotation or raw dictionary markup was found leaking into the new explanations.
- `python -X utf8 -B tools\validate.py`, run directly in the primary RU checkout: exit 0, `0 error(s)`. No generator was run.

Dictionary evidence actually inspected:

- Jisho/JMdict lexical entries for every one of the 30 new words, using `https://jisho.org/api/v1/search/words?keyword=<word>` and exact written-form matching. Inspected lexical senses, parts of speech and restrictions rather than Wikipedia blocks. These support, among others, both transitive/intransitive 完了する, scholarly/nonprofessional learned-person 学者, learning and experience senses, discipline 学問, noun/suffix 姿, both senses of 奨学金, both employment senses of 失業, and figurative 奪う. Also inspected 研究者.
- [女王, full entry](https://jisho.org/word/女王): senses 1, 2 and 5, plus the actual Notes marking じょうおう irregular; the API alone was not used to establish that form-level flag.
- [お宅, full entry](https://jisho.org/word/お宅): actual JMdict edit link identifies 1002400; sense 1 is respectful reference to the addressee's home/family. [Weblio, 宅](https://www.weblio.jp/content/宅), specifically Digital Daijisen たく senses 1–3, confirms the residential senses and wife-to-outsider husband-reference example. 嫁's actual lexical entry marks the wife sense Kansai; RU does not turn that label into a prohibition.
- [Kotobank, 宇宙](https://kotobank.jp/word/宇宙-34804), specifically Digital Daijisen's 補説 and Seisenban Nihon Kokugo Daijiten's opening definition: inspected the actual space/time account, not just the first unrelated encyclopedia discussion.
- Russian entries below were inspected on Gramota, chiefly Kuznetsov's Большой толковый словарь (`https://gramota.ru/poisk?query=<lemma>&mode=slovari&dicts[]=42`). Exact sense qualifications matter:
  - «совершенный» sense 2 also means complete/absolute; «безупречный» refers to flawlessness, with the universal dictionary additionally distinguishing quality. Thus 完全's label is not restricted solely to admiring praise; its body expressly teaches non-evaluative completeness.
  - «четверть» school-year division, «семестр» academic half-year; these fit 学期's explicit calendar-dependent qualifications. «наружность» senses 1–2 cover people and things, not exclusively faces.
  - «сторониться» sense 2 covers avoiding/keeping apart; «чудной» is conversational strange/unusual, «диковинный» unusual/astonishing/strange, «странноватый» conversational somewhat strange. These are supported gloss choices, not claimed universal substitutions or frequency rankings.
  - «эрудиция» deep or broad learning; «наличие» presence/existence; «безработица» sense 2 the individual's unemployed state; «утрачивать» cross-reference followed through to «утратить», whose examples include trust and documents.
  - «пристрастие» sense 1 liking/inclination, not sense 2 prejudice; «непостижимый» sense 1 unexplained/incomprehensible; «загадочный» seemingly inexplicable/mysterious.
  - «жилище», «внук» (including gender-inclusive plural), «невестка» (husband's relatives, including parents), noun and adjective «учёный», «дисциплина» scientific-branch homonym, «комиссия» authorized-group homonym, «ссуда», «стипендия», «отобрать» sense 1 and «лишить» sense 1 support the other checked Russian choices.
- [Wiktionary, учёность](https://ru.wiktionary.org/wiki/учёность), actual sense 1: learning/education; [освоить](https://ru.wiktionary.org/wiki/освоить), senses 1–2: learning use/acquiring knowledge; [внучка](https://ru.wiktionary.org/wiki/внучка), actual female grandchild sense; [триместр](https://ru.wiktionary.org/wiki/триместр), actual school-year sense 2. These supplied relevant definitions where a Gramota query failed or did not return the lemma.
- [Gramota, помолвка](https://gramota.ru/poisk?query=помолвка&mode=slovari), Kuznetsov, and [Wiktionary](https://ru.wiktionary.org/wiki/помолвка) emphasize the announcement/ceremony sense. This does not establish a translation error: RU explicitly explains 婚約 as commitment to marry and says the Japanese word does not specify what ceremony occurred. It does not infer a required rite from the Russian label.

Optional: None.

Limits: Correctness and scoped coverage only; no independent comprehensive quiz-pool safety verdict or Russian-comprehensibility facet is claimed. The added guards were considered as direct semantic comparisons, not as evidence of transitive exclusion groups. Existing baseline prose outside the stated reads, batch records, tracking/progress, manifest generation, publication/archive verification and device/media acceptance were not reviewed. Several initial HTTP dictionary queries returned 429; the relevant lexical evidence above was subsequently obtained from successful bounded responses or the stated alternate entries. No author/reviewer reports, author drafts, RU translation-batch directories or scratch worktree were consulted. No repository file, HEAD or index was modified; only this report was written.

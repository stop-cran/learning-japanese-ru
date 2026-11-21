# B225 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `56996a024ba2641a8d5e846d8c63e1981beeccff` (tree `cec94999a3e5496f49132267a073e5e56aa92d24`),
> the signed candidate pushed before review.
> Later reconciliation is in `225-words-batch-64-recheck-001.md`.

Snapshot: RU candidate 56996a024ba2641a8d5e846d8c63e1981beeccff, parent a195c33e1213d54f416b1cb2df6b23f422cabd36. Initial and final HEAD both match; initial and final git status --porcelain empty. No uncommitted content included. EN comparison source: supplied frozen checkout, revision 6af98cb.

Scope: Independent blind, read-only review of CORRECTNESS and SCOPED COVERAGE. Actual model identifier is not verifiable from this reviewer context; no additional reviewers used.

Full bilingual reads, file by file (each path below was read in full in both RU and frozen EN):
words/ごめんなさい.md; words/こんにちは.md; words/こんなに.md; words/これら.md; words/ぐっすり.md;
words/きつい.md; words/かわいらしい.md; words/かもしれない.md; words/お目に掛かる.md; words/お互い.md;
words/おめでとう.md; words/おまえ.md; words/おそらく.md; words/お.md; words/うなる.md;
words/うがい.md; words/いわゆる.md; words/いらっしゃい.md; words/いつまでも.md; words/いただきます.md;
words/いけない.md; words/あんまり.md; words/あんなに.md; words/ありがとう.md; words/あらゆる.md;
words/あっ.md; words/あちこち.md; words/あいにく.md; words/麓.md; words/鳴らす.md.

Also read all ten baseline word-file diffs: あまり, うとうと, すみません, すやすや, だめ, ぶかぶか, 感謝, 方々, 申し訳, 祝う. Additional complete RU convention/comparison reads: すみません, 申し訳, ぶかぶか, あまり, すやすや, いらっしゃる. Read the three binding RU instruction/format documents. No prohibited author/reviewer reports, tracking/batch/draft records or scratch worktrees read.

Verdicts:
- Correctness: NEEDS FIX for words/ぐっすり.md (C1); CLEAN for the other 29 new cards within the bounded review. No established Japanese factual defect in the restored baseline comparisons.
- Scoped coverage: CLEAN for all 30 new cards. Japanese teaching points, examples, sense distinctions, citations and source links with existing RU targets are retained. The source-list-only/English-dependent removals are within the stated adaptation allowance. All required stable metadata and EN exclusions remain; RU adds direct guards. No missing live EN-to-RU card link found.
- Russian comprehensibility and whole-pool quiz safety are not assigned verdicts; observations below do not claim those reviews.

Findings:

C1; Minor; correctness; words/ぐっすり.md:18.
Claim/impact: «Прошлой ночью я смог крепко выспаться» adds the result of obtaining sufficient restorative sleep. 昨夜はぐっすり眠れました says that sound sleep was possible/achieved, not that the speaker necessarily slept enough and emerged well rested. In a model example this blurs sleep quality with sufficiency/restoration, despite the card correctly distinguishing depth from duration elsewhere.
Remedy: replace the Russian translation with «Прошлой ночью мне удалось крепко поспать».
Evidence: [Jisho/JMdict ぐっすり](https://jisho.org/word/ぐっすり), entry 1004060, sense 1: “soundly (sleeping); fast (asleep)”; [Digital Daijisen ぐっすり](https://www.weblio.jp/content/ぐっすり), sense 1: 深く眠っているさま／熟睡するさま. The potential-past 眠れました supplies successful ability to sleep. [Kuznetsov, выспаться](https://gramota.ru/poisk?query=выспаться&mode=slovari): «Проспав достаточно, хорошо отдохнуть». The added sufficient-rest result is absent from both Japanese and EN.
Confidence: high on the added semantic result; localized minor learning impact, not an incorrect Japanese sentence.
Status: unresolved; no edits authorized or made.

Evidence checks supporting the bounded verdicts:
- Independently read the applicable full Jisho API lexical entries/senses for all 30 headwords, selecting 御-3 for お rather than the unrelated first search hit 尾. Inspected full word-page spelling notes and verified numeric JMdict IDs for all 30 plus comparison ご (1270190). Every cited ID matched. In particular: あんまり sense 1 is restricted to あまり; selected senses 2–4 support the teaching; おまえ has formerly-honorific pronoun information and a separate noun sense; お目に掛かる has modern humble sense 1 and archaic sense 2; うなる senses 1–4 and 鳴らす senses 1–3 support their extended uses.
- Actual spelling notes confirm irregular こんにちわ, rare 嗽/漱, rare 凡ゆる/有らゆる and 彼方此方. おめでとう's full entry labels the kanji spellings rare/ateji. For 梺, which Jisho's ordinary display omits, inspected frozen EN docs/n2-vocabulary-batch-sources/batch-75.json:1575–1630: entry 1611440 actually contains search-only 梺. The card does not promote it to a recommended spelling.
- [Weblio こんにちは](https://www.weblio.jp/content/こんにちは) supports the daytime greeting and retained particle は; [Digital Daijisen 麓](https://www.weblio.jp/content/麓), exact ふもと heading, supports the mountain-foot sense, separately from ろく. [Digital Daijisen 鳴らす](https://www.weblio.jp/content/鳴らす), senses 1–4, supports sound production, reputation, complaints and the explicitly excluded older flatulence sense. [御免](https://www.weblio.jp/content/御免) and [ごめんなさい](https://www.weblio.jp/content/ごめんなさい) support the apology/formula discussion; no contradicted etymology was established. [お茶](https://www.weblio.jp/content/お茶), sense 1, is explicitly 美化語; the お/ご rule is already qualified as a tendency, not a ban.
- Russian dictionary inspection succeeded despite some HTTP 429 responses. [Kuznetsov беспробудный](https://gramota.ru/poisk?query=беспробудно&mode=slovari) has both very deep/prolonged sleep and a separate drinking sense; «беспробудно спать» is explicitly exemplified, so association with drinking alone is not a defect. [Миленький](https://ru.wiktionary.org/wiki/миленький), senses 1–2, includes attractive/appealing persons and things, not just irony; [умилительный](https://ru.wiktionary.org/wiki/умилительный) means causing tender affection. Both support the chosen adjective glosses.
- [Kuznetsov урчать](https://gramota.ru/poisk?query=урчать&mode=slovari&dicts[]=42), sense 2, explicitly has «Мотор тихо урчал»; entries [гудеть](https://gramota.ru/poisk?query=гудеть&mode=slovari) and [реветь](https://gramota.ru/poisk?query=реветь&mode=slovari) support the context-dependent engine alternatives. [Изматывать](https://ru.wiktionary.org/wiki/изматывать), sense 1, supports exhausting work. [Как назло](https://ru.wiktionary.org/wiki/как_назло) supports the adverse-coincidence rendering, not literal intentional rain.
- [Kuznetsov очень](https://gramota.ru/poisk?query=очень&mode=slovari&dicts[]=42) and [вероятность](https://gramota.ru/poisk?query=вероятность&mode=slovari&dicts[]=42) were inspected for «не очень-то» and «по всей вероятности». The colloquial former title does not force the standalone rebuke sense in a negative predicate. [Иметь честь](https://kartaslov.ru/значение-слова/иметь+честь), actual MAS/Ushakov excerpts, supports a deferential formula, with dated/formal Russian register rather than an ordinary neutral equivalent. «Увидимся завтра» is a natural contextual translation; the surrounding Japanese humble-role rule remains explicit, so no categorical register-error finding.
- RU-only contrasts checked against Kuznetsov entries [можно](https://gramota.ru/poisk?query=можно&mode=slovari&dicts[]=42), [крепкий](https://gramota.ru/poisk?query=крепкий&mode=slovari&dicts[]=42), [полоскание](https://gramota.ru/poisk?query=полоскание&mode=slovari), [подножие](https://gramota.ru/poisk?query=подножие&mode=slovari&dicts[]=42), [тесный](https://gramota.ru/poisk?query=тесный&mode=slovari&dicts[]=42), [аппетит](https://gramota.ru/poisk?query=аппетит&mode=slovari&dicts[]=42), and [так называемый](https://ru.wiktionary.org/wiki/так_называемый), senses 1–2. These support the relevant permission, deep-sleep, action/liquid, landform, fit/friendship, mealtime-role and neutral/ironic distinctions. The cards do not turn these contrasts into universal substitution rules. Masculine first-person Russian examples are contextual choices, not claims that gender-neutral Japanese requires a male speaker.
- Supplemental metadata/link/Japanese-run comparison found no omitted Japanese content; the only lower run count is 申し訳ありません split by the added Markdown link. Direct bilingual reading, not that token check, grounds semantic coverage. Read-only tools/validate.py returned 0 error(s); scoped git diff --check was clean.

Optional:
- O1; outside assigned facets, Russian comprehensibility; words/いつまでも.md:33: «после стольких-то времени» is ungrammatical, not merely a stylistic preference. Replace the quoted gloss with «всё ещё, спустя столько времени». This preserves the source's complaint reading without a malformed Russian phrase.
- O2; nonblocking beginner terminology: explain «канго» (ごめんなさい:26), «онные чтения» (こんにちは:25) and «годан» (お目に掛かる:21, うなる:16, 鳴らす:16) when first used. The classifications were not established as factually wrong. «Китайско-японский элемент» and «китайские по происхождению чтения» are plainer local alternatives.

Limits: This is not exhaustive corpus/frequency, native-speaker, media, app/device or whole-pool quiz certification. Only the six named existing comparison cards received complete additional reads; the other baseline scope is their actual ten diffs. Illustration parity is outside this text batch (EN ぐっすり has image metadata absent in RU). Jisho live display is not a replacement for pinned spelling data; the 梺 qualification above used the actual frozen source capture. Some Gramota/Gufo fetches failed or omitted the requested main entry; no successful-but-irrelevant fetch was counted as verification. No generator, checkout, staging, commit or push performed; the report is the only file intentionally written.

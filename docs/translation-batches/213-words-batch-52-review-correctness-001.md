# B213 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `3c8461447a0a88352701ecb3fc7183b5c545a07b` (tree `2e363e3eaf674dd400edb587315ee26cfe455597`),
> the signed candidate pushed before review.
> Later reconciliation is in `213-words-batch-52-recheck-001.md`.

Snapshot: RU candidate 3c8461447a0a88352701ecb3fc7183b5c545a07b, parent 1269d2687978842c46baab6a8637f3c6648c8551; HEAD matched and git status --porcelain was empty. No uncommitted changes included. Compared against the supplied frozen EN checkout (6af98cb).

Scope: CORRECTNESS and SCOPED COVERAGE; blind, read-only review. Actual reviewer model identifier is not independently verifiable in this context. Each of the following files was read IN FULL in RU and IN FULL against its EN original:

- words/夫婦.md
- words/夫人.md
- words/大部分.md
- words/大臣.md
- words/大統領.md
- words/大戦.md
- words/大家.md
- words/大半.md
- words/大使.md
- words/大会.md
- words/大.md
- words/夢中.md
- words/夜明け.md
- words/夜中.md
- words/外交.md
- words/外す.md
- words/夕べ.md
- words/売れる.md
- words/墓.md
- words/境.md
- words/塔.md
- words/塀.md
- words/報告.md
- words/よる.md
- words/基づく.md
- words/城.md
- words/埃.md
- words/地球.md
- words/地域.md
- words/地方.md

Read the three binding RU rule/reference files. Also read the complete existing RU comparison cards ほとんど, たいてい, 莫大, 大小, 熱中, 下ろす, 瞬間, 次第, 州, リポート, 知らせる, 伝える and レポート. Read every changed line of the eight existing kanji cards and thirteen existing word cards in the runtime integration diff; this is not a full rereview of those baseline articles.

Verdicts: correctness CLEAN; scoped coverage CLEAN, for all 30 new cards. CLEAN means no actionable defect established within these facets, not exhaustive linguistic certification.

Findings: None.

Evidence and checks:

- Inspected actual Jisho/JMdict lexical entries for all 30 target words, plus 夫妻 and the twelve RU-added guard/comparison targets. Distinguished alternate readings and separate homonyms, and excluded Wikipedia-definition/name senses as lexical evidence. Entry access: https://jisho.org/api/v1/search/words?keyword=<URL-encoded-word>. In particular, 夫妻 explicitly carries the own-family restriction; 夫人 has the respectful wife/title sense; 大家 has a separate おおや landlord entry and たいか expert entry; 大半 has the adverbial sense; 大 has the size-label and prefix senses; 夕べ separates poetic evening, event-title evening and previous evening; 境 has the reading-qualified mental-state note; よる lists the four spellings with sense preferences; 基づく includes both foundation and origin.
- All example translations were checked against their Japanese, including completed versus ongoing states, transitivity, passive appointment/election, recipient に, を境に, を通じて, and the reported-information construction によると. Russian masculine first-person past forms are contextual renderings, not claims that the Japanese speaker is inherently male. The gender-neutral landlord explanation is preserved.
- Inspected actual Kuznetsov entries on Gramota, not search snippets: https://gramota.ru/poisk?query=<word>&mode=slovari&dicts[]=42. Relevant entries/senses: арендодатель (person letting real estate); съезд 2 (representative gathering); президент 1 (including «П. крупного концерна»); министр 1 (cabinet/government role); госпожа → господин 4 (polite title); самозабвенный, including самозабвенно, and самозабвение 1–2 (complete absorption/forgetting oneself); заря 1 (including the time of morning light); рубеж 1 and «на рубеже» (spatial division and temporal junction); гробница (burial structure); полночь 1 (24:00 and broader nighttime use); округа (local surroundings, including resident metonymy); дипломатия 1; отчёт 1–3; исходить, second entry, 2 and 4; область 1 and 3; провинция 1–2; стена 3; вечер 1–2; земля 1 and 4; снять 1–2. Also inspected the distinct Большой универсальный словарь entry for рубеж, senses 1.0 and 1.2, including an event as a before/after division: https://gramota.ru/poisk?query=рубеж&mode=slovari.
- Additional actual-entry checks: https://ru.wiktionary.org/wiki/округа (local territory/social setting) and https://ru.wiktionary.org/wiki/расстегнуть (unfastening, with the imperfective cross-reference and a button example). Several initial Gramota requests returned HTTP 429; successful subsequent exact entries or these alternatives supplied the relevant senses.
- Architectural/function contrast checked against the actual dictionary/encyclopedia sections at https://kotobank.jp/word/塀-128772 and https://kotobank.jp/word/壁-46364. The Russian title «забор; ограда» is not being read as excluding masonry: the body explicitly retains the enclosing-wall function and material qualification. The Russian «стена» remark is supported by Kuznetsov sense 3.
- The poetic marker in 夕べ applies to the simple evening noun; the card separately explains the event-name use without requiring that event to be poetic. «Полночь» is warned against only if interpreted as exactly 00:00, not categorically rejected as a possible contextual translation.
- No EN sense, teaching construction, example, citation or substantive link label was found omitted. Automated comparison of all 30 pairs found no missing Japanese lexical tokens and no differences in word, reading, jlpt, type, kanji or tags. Source quiz exclusions were retained; additions were inspected as comparison leads, not treated as proof of quiz safety. Japanese reading joins retain their original hiragana/katakana. Parenthetical/layout localization does not change the Japanese reading strings.
- Optional link_parity.py: checked 30, no lost available-target links or extra link targets reported. Read-only validator: python -X utf8 -B tools\validate.py → 0 error(s), exit 0. No generator run.

Optional:

- O1; nonblocking precision; words/地方.md:35. Consider replacing the final source-list sentence with «При чтении ちほう слово не означает „побережье“». EN explicitly says “This reading”; RU's current wording is understandable within the ちほう card, but the explicit qualifier avoids an unintended spelling-wide reading. Actual evidence: https://kotobank.jp/word/地方-72427, Digital Daijisen ちほう 1–2 versus じかた 3 («海上から見て、陸地のこと»); the separate Jisho 地方（じかた）entry also records coast/shore. This does not invalidate the reviewed ちほう meaning and does not require adding a rare-reading lesson.

Limits: No independent native-speaker, corpus-frequency, app/device or learner-outcome certification. Comprehensibility and comprehensive quiz-pool safety are outside the assigned facets; checking the added guard targets is not an exhaustive quiz audit. No batch records, tracking/drafts, scratch worktree, author material or other reviewer report was read. The repository, index and HEAD were not modified; only this report was written.

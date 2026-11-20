# B209 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `5f015601f1ff714f7c63b0edfa85215c8f99f071` (tree `b7775854199e6bd437d9ef17989cc2a7a45ae79a`),
> the signed candidate pushed before review.
> Later reconciliation is in `209-words-batch-48-recheck-001.md`.

Snapshot: RU 5f015601f1ff714f7c63b0edfa85215c8f99f071, parent c834ac201520921b6695bf6143fad3af7c31286c. Initial and final HEAD match; both git status --porcelain calls returned nothing; final cached diff exit 0. No uncommitted changes included. Frozen EN HEAD independently confirmed as 6af98cb717755690a9ca793e5454a96ebd7a8f9f; its words working tree has no tracked changes.

Scope: Independent blind, read-only correctness and scoped-coverage review. Actual model identifier is not independently verifiable. Read the three binding RU instruction/format documents. No author report, author prompt, title-screen output, other reviewer report, batch/draft/tracking record or scratch author worktree was consulted.

Full bilingual reads, file by file (each RU file from first line through EOF, against the entire same-path frozen EN original):
- words/心理.md: full RU lines 1–35; full EN.
- words/徹底.md: full RU lines 1–34; full EN.
- words/徹夜.md: full RU lines 1–34; full EN.
- words/微妙.md: full RU lines 1–39; full EN.
- words/得意.md: full RU lines 1–35; full EN.
- words/従兄弟.md: full RU lines 1–34; full EN.
- words/ですから.md: full RU lines 1–37; full EN.
- words/従って.md: full RU lines 1–33; full EN.
- words/従う.md: full RU lines 1–35; full EN.
- words/後者.md: full RU lines 1–34; full EN.
- words/役割.md: full RU lines 1–35; full EN.
- words/効果.md: full RU lines 1–35; full EN.
- words/影響.md: full RU lines 1–35; full EN.
- words/影.md: full RU lines 1–35; full EN.
- words/当時.md: full RU lines 1–34; full EN.
- words/当てる.md: full RU lines 1–35; full EN.
- words/当たる.md: full RU lines 1–44; full EN.
- words/弾.md: full RU lines 1–34; full EN.
- words/強調.md: full RU lines 1–34; full EN.
- words/強盗.md: full RU lines 1–34; full EN.
- words/強力.md: full RU lines 1–35; full EN.
- words/引退.md: full RU lines 1–34; full EN.
- words/引用.md: full RU lines 1–36; full EN.
- words/引っ張る.md: full RU lines 1–35; full EN.
- words/弁当.md: full RU lines 1–35; full EN.
- words/座席.md: full RU lines 1–35; full EN.
- words/床.md: full RU lines 1–35; full EN.
- words/広告.md: full RU lines 1–34; full EN.
- words/幼い.md: full RU lines 1–34; full EN.
- words/年齢.md: full RU lines 1–35; full EN.

Also read in full the existing RU words/武器.md, 有効.md, 左右.md, 毒.md, 性.md, 苦手.md, 自慢.md, お弁当.md and 陰.md for the actual comparison senses and labels. Inspected every changed line in the 20 pre-existing runtime files (four kanji cards and sixteen word cards): all 27 changes add links without changing the displayed teaching text. This is changed-passage review, not full re-review of those twenty files.

Verdicts: correctness CLEAN; scoped coverage CLEAN, for all 30 new cards, with no per-article exceptions. These are bounded verdicts, not an assertion of exhaustive linguistic correctness or app acceptance.

Findings: None established.

Evidence and checks:
- Compared every example and explanation bilingually, including Japanese forms and kana, argument marking, transitivity, polarity, register, temporal interpretation and event stage. The 当てる/当たる contrast retains the agent/contact distinction; 従う and 影響 retain their に constructions; the success/equivalence uses of 当たる remain separate from collisions. 心理 retains the person-state/academic-discipline distinction; 引用 and 広告 each retain act versus material; 強盗 retains offender versus offense.
- Checked all source front-matter fields except the translated title for equality, treating exclusions separately. The five added direct exclusion edges are 得意→武器, 効果→有効, 影響→左右, 影響→毒 and 床→性; original exclusions are retained. No other source metadata was lost. All EN links with available RU targets are retained, and all links in the new cards resolve. Plain-text mentions with unavailable targets are not defects, including 底 as a kanji rather than the existing word card.
- Queried the actual Jisho/JMdict lexical entries for every one of the 30 Japanese spellings using https://jisho.org/api/v1/search/words?keyword=<exact spelling>; inspected forms, lexical senses, restrictions, usage information and part-of-speech fields, excluding Wikipedia blocks and unrelated readings. This confirmed, among other things, 微妙's colloquial fourth sense and ビミョー note, 従兄弟's male-cousin/kana note, 影's nonstandard behind/background usage, 弾's spelling preference, 強力's distinct きょうりょく/ごうりき entries, and the する-verb categories. Live sense inventories can be newer than the frozen EN source; no change to the inherited selected senses is proposed.
- For the new exclusion bases, actual entries https://jisho.org/api/v1/search/words?keyword=武器 (sense 2: figurative weapon/asset), https://jisho.org/api/v1/search/words?keyword=有効 (valid/effective; na-adjective and noun), https://jisho.org/api/v1/search/words?keyword=左右 (sense 2: control/influence), https://jisho.org/api/v1/search/words?keyword=毒 (sense 2: harm/evil influence), and https://jisho.org/api/v1/search/words?keyword=性 (sex/gender) support the Japanese sides of the conservative direct guards. Actual current RU labels were read, not reconstructed from memory. No transitive closure is claimed.
- Russian-specific checks used actual entry bodies, not search summaries or the site's “other dictionaries” snippets. Where simplified Gufo extraction omitted the entry, read its raw HTML article:
  * https://gufo.me/dict/kuznetsov/сторона, sense 8: property/feature, with “Сильные и слабые стороны…”; supports the 得意 title.
  * https://gufo.me/dict/kuznetsov/второй, sense 1: “Следующий за первым”; with the explicit two-mentioned-items restriction, supports 後者 without adding a new sense.
  * https://gufo.me/dict/kuznetsov/малолетний: “Имеющий мало лет от роду, находящийся в детском возрасте.” The conversational marking belongs to another usage/substantivization, not this adjective sense; no mandatory legal/derogatory register was established for the title 幼い.
  * https://gufo.me/dict/ozhegov/пол, the separate ПОЛ¹ floor and ПОЛ² sex entries: confirms the Russian homonymy behind 床→性, without equating the Japanese words.
  * https://gufo.me/dict/ozhegov/реклама, senses 1–2: publicity and the corresponding announcement; supports both activity and item in 広告.
  * https://gufo.me/dict/kuznetsov/следовать, senses 1 and 4: following behind and acting according to guidance; supports the Russian adaptation in 従う.
  * https://gufo.me/dict/kuznetsov/попасть, sense 1, including “Камень попал в окно” and instrument-marked constructions: supports the distinct Russian renderings in 当たる/当てる.
  * https://gufo.me/dict/kuznetsov/тень, senses 1–2: cast shadow and shaded space; supports the Russian-specific overlap statement in 影 without erasing the Japanese spelling distinction.
  * https://gufo.me/dict/kuznetsov/грабеж, sense 1: taking property “обычно с насилием”, not necessarily always; supports the qualified Russian contrast in 強盗. Independently checked Digital Daijisen ごうとう at https://kotobank.jp/word/強盗-470962: violence/threats, and both act and person.
  * Actual JMdict 御（お）prefix entry returned by https://jisho.org/api/v1/search/words?keyword=御 records the honorific/polite/humble prefix, supporting 弁当's added polite-prefix explanation.
- Source-list English-only gloss warnings and contributor classification annotations were not treated as missing Japanese teaching content. The substantive distinctions survive in Russian.
- Read-only validation: `python -X utf8 -B tools\validate.py` in the RU primary checkout returned exit 0 and “0 error(s)”. No generator was run. An in-memory metadata/link comparison independently found no dropped live EN link or broken link in any of the 30 cards. Validation is structural evidence, not proof of the linguistic verdict.

Optional: None.

Limits: Correctness and scoped coverage only; this is not a full-pool quiz-safety or Russian-comprehensibility audit, nor a native-speaker, device, media or release-acceptance test. All 30 new cards and originals were fully returned and read in the smaller follow-up batches; initial oversized aggregate outputs were not counted as full reads. Gramota requests were rate-limited; the actual Kuznetsov/Ozhegov entry bodies above supplied the necessary Russian evidence instead. Live Jisho responses expose lexical forms/senses but not numeric JMdict entry IDs; the inherited IDs were checked for preservation against EN, not independently reidentified from a pinned XML release. No consequential unresolved claim was identified in the assigned scope. The only intentionally written file is this report; no repository content, HEAD or index was changed.

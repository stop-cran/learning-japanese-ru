> Original blind correctness review of `bbe4e485115525a1f4bd661960486449dbe4570b` (tree `a46d590fde1002c23b72346587efb6c17d0ea7c7`).
> Runtime identity verified by the coordinator: `gpt-6.1-sol`, agent `f8dfbe0c-bd07-49ff-b12d-6bb92e7a61e5`.
> [Reconciliation at the signed fix](253-words-batch-92-recheck-001.md). The report below is unchanged apart from LF line endings.

# Batch 253 — blind correctness review

## Snapshot

RU candidate: `bbe4e485115525a1f4bd661960486449dbe4570b`; comparison parent: `7126ab8be4bf9ea8358b57a02e673fef007278f4`. Initial and final `git rev-parse HEAD` matched the candidate; `git status --porcelain` was empty both times. No checkout, index or source-file changes were made. EN comparison source: the specified frozen `learning-japanese-en-frozen` checkout, `6af98cb`.

## Scope

Facets: **correctness** and **scoped coverage**, assessed separately. Model identity is not independently verifiable in this session.

Every file below was read **in full**, including front matter, every example/reading, comparison, note and footer, against its **complete EN original**. Both assigned facets apply to every row.

| RU file | Complete RU / EN lines read |
|---|---:|
| `words/演劇.md` | 1–43 / 1–51 |
| `words/漁師.md` | 1–40 / 1–41 |
| `words/滝.md` | 1–43 / 1–47 |
| `words/溶岩.md` | 1–47 / 1–49 |
| `words/混合.md` | 1–35 / 1–35 |
| `words/溶かす.md` | 1–46 / 1–48 |
| `words/溶く.md` | 1–48 / 1–50 |
| `words/溶け込む.md` | 1–48 / 1–48 |
| `words/満点.md` | 1–35 / 1–35 |
| `words/売り切れる.md` | 1–45 / 1–45 |
| `words/売り切れ.md` | 1–44 / 1–44 |
| `words/満員.md` | 1–35 / 1–35 |
| `words/湿る.md` | 1–44 / 1–44 |
| `words/水蒸気.md` | 1–33 / 1–33 |
| `words/湯気.md` | 1–47 / 1–47 |
| `words/湧く.md` | 1–56 / 1–58 |
| `words/測量.md` | 1–49 / 1–49 |
| `words/測定.md` | 1–50 / 1–50 |
| `words/温泉.md` | 1–33 / 1–33 |
| `words/温帯.md` | 1–33 / 1–32 |
| `words/温室.md` | 1–32 / 1–32 |
| `words/渇く.md` | 1–36 / 1–36 |
| `words/クリーニング.md` | 1–39 / 1–39 |
| `words/清掃.md` | 1–45 / 1–45 |
| `words/混ぜる.md` | 1–40 / 1–40 |
| `words/付き合う.md` | 1–56 / 1–56 |
| `words/混じる.md` | 1–41 / 1–41 |
| `words/混ざる.md` | 1–40 / 1–40 |
| `words/深夜.md` | 1–46 / 1–46 |
| `words/深まる.md` | 1–50 / 1–50 |

Also inspected the link-only changes in `kanji/乾.md`, `kanji/劇.md`, `kanji/帯.md`, `words/乾く.md`, `words/泉.md`, `words/濡らす.md`, `words/熱帯.md`, `words/芝居.md` and `words/零点.md`; current linked-card titles and relevant comparison passages; candidate runtime diff and manifest excerpt. Existing kanji cards were not re-audited beyond those changes.

Verification:

- Compared all non-title front-matter fields: original IDs, readings, levels, types, kanji, tags and exclusions are retained. The differences are additive RU quiz exclusions on ten cards; all explicit exclusion targets exist. All 30 vocabulary N2 labels have supporting Jisho entries; 付き合う also carries N1 there, which does not contradict its N2 label.
- Compared Japanese example sentences and kana strings, including spacing. No changed or missing Japanese example was found. The additional reading とく beside 解く is correct. Parenthesis typography follows the RU adaptation; the kana contents are preserved.
- Compared every Markdown link: no added RU-only hyperlink, broken link or dropped EN link to an existing RU target was found. Unavailable kanji targets and 噴火 remain plain as required. All footer source URLs are retained.
- Inspected actual primary [JMdict XML](https://www.edrdg.org/pub/Nihongo/JMdict_e.gz): every main card's cited entry ID, readings and spelling annotations, plus the named comparison entries. This confirms, among others, 瀧's outdated annotation; rare 熔岩, 融かす/解かす and 涌く; irregular 雑ぜる/雑ざる; rare 雑じる; search-only 付合う, 交る and 混る; and the separate 喉が渇く/喉が乾く phrase entry.
- Checked component reading classifications directly in [KANJIDIC2](https://www.edrdg.org/kanjidic/kanjidic2.xml.gz), separately from historical interpretation. In particular 漁 has on リョウ as well as ギョ; 気 has on ケ as well as キ; the mixed ゆ＋げ explanation is retained without reclassifying the repository's wago metadata. No new historical etymology was inferred.
- Read the actual Digital Daijisen entries for 溶岩, 溶かす, 溶く, 溶け込む, 満点, 満員, 湿る, 水蒸気, 湯気, 湧く, 沸く, 測量, 測定, 渇く, 付き合う, 混じる and 深夜. Their substantive distinctions, qualifications and footer labels survive translation apart from the findings below.
- Russian-usage checks included actual Gramota entries for [сникать](https://gramota.ru/poisk?query=сникать&mode=slovari), [съёмка](https://gramota.ru/poisk?query=съёмка&mode=slovari), [распродать](https://gramota.ru/poisk?query=распродать&mode=slovari&dicts[]=42) and [пар](https://gramota.ru/poisk?query=пар&mode=slovari), and Wiktionary entries for [отсыреть](https://ru.wiktionary.org/wiki/отсыреть), [бить](https://ru.wiktionary.org/wiki/бить) (outflow sense), [театр](https://ru.wiktionary.org/wiki/театр) (art/building senses), [-ся](https://ru.wiktionary.org/wiki/-ся), [хлынуть](https://ru.wiktionary.org/wiki/хлынуть) and [исконный](https://ru.wiktionary.org/wiki/исконный). «Топографическая съёмка местности» is explicitly exemplified in Gramota's universal dictionary. The named usages are not being left unchecked merely because the cards have no Russian-source footers.

## Verdicts

- **Correctness: NEEDS FIX** — C1. No further actionable correctness defect established in the other 29 cards.
- **Scoped coverage: NEEDS FIX** — C2. No further actionable teaching-content omission established in the other 29 cards.
- Russian comprehensibility and exhaustive quiz suitability: **outside the assigned facets**, not certified.

The omitted EN sentence in 湧く about absent kanji cards and written-kanji metadata is contributor bookkeeping, not a lost Japanese teaching rule; `kanji: [湧]` remains correct. The rebuilt English-dependent contrasts preserve the Japanese distinctions. Contextual masculine Russian forms, idiomatic thirst translations without a literal throat subject, resultative «отсырели», the fifty-point scale translation, and «Осень всё больше вступает в свои права» do not by themselves establish defects.

## Findings

### C1 — Medium — correctness — `words/湧く.md:50`

**Wrong claim:** «Значения “кипеть, нагревать” относятся к 沸く». Russian «нагревать» is transitive: heat something. 沸く's relevant sense is intransitive: water grows hot or boils. The sentence therefore assigns the wrong argument structure to the comparison verb, despite the correct contrast immediately above and the existing 沸く card's «нагреваться».

**Remedy:** replace `«кипеть, нагревать»` with `«кипеть, нагреваться»`.

**Evidence:** [Jisho/JMdict 沸く](https://jisho.org/api/v1/search/words?keyword=沸く), entry **1606680**, sense 1: “to grow hot (e.g. water); to boil”, **Intransitive verb**. [Digital Daijisen 沸く](https://www.weblio.jp/content/沸く), sense 1: 水などが熱せられて沸騰する。また、適当な熱さになる, with 湯が沸く / 風呂が沸く. Frozen EN `words/湧く.md:52–54` does not require the transitive Russian gloss.

**Confidence:** high. **Status:** unresolved.

### C2 — Low — scoped coverage / example accuracy — `words/深夜.md:21`

**Lost claim:** 深夜の電話 is translated only as «ночной телефонный звонок». This removes the example's **late/deep-night** qualification and leaves the broader meaning of 夜. The next explanation at line 23 says this very example illustrates «ночной, поздненочной», but the translation no longer shows the distinguishing part.

**Remedy:** `— Меня разбудил телефонный звонок глубокой ночью.`

**Evidence:** [Jisho/JMdict 深夜](https://jisho.org/api/v1/search/words?keyword=深夜), entry **1362810**, lexical sense: “late at night”; [Digital Daijisen 深夜](https://www.weblio.jp/content/深夜): 真夜中。よふけ。深更. Frozen EN `words/深夜.md:21` explicitly says “A late-night phone call woke me up.” Its qualifier can be retained naturally in Russian.

**Confidence:** high. **Status:** unresolved.

## Optional

- Outside the assigned facets: `words/湧く.md:4,12` uses perfective «хлынуть» among imperfective title glosses. «Хлестать наружу» would align the aspect convention and the wording already used in the body. The current word is a possible contextual translation, so this is not counted as a semantic defect.
- `words/混ぜる.md:38`: «постфиксом -ся» or simply «элементом -ся» is more precise for a novice than «частицей -ся» and avoids conflating a Russian bound element with Japanese particles. The mixing/transitivity teaching point itself remains intact.

## Limits

No blind author material, other reviewer report, prohibited scratch checkout or translation-batch/tracking content was read. Only this report was intentionally written. No generator, validator, application/device test or full quiz-pool audit was run; this is a semantic/source review, not runtime acceptance.

Live dictionaries were checked on 2026-11-23, not a supplied historical dictionary capture. Current JMdict 1597790 has three senses (association, dating, accompanying); its forms support the card's claims, but historical numbering of the EN “pinned dictionary” was not independently reconstructed. Initial transient Jisho rate limits were resolved through subsequent direct entries and primary XML. Bulk kanjiapi requests failed, so component checks used the primary KANJIDIC2 archive; a direct 気 API request also confirmed キ/ケ. General-dictionary absence of «онный» is not evidence that the established technical term is incorrect.

**Summary:** correctness **NEEDS FIX**; scoped coverage **NEEDS FIX**. Findings: **0 critical, 0 high, 1 medium, 1 low**.

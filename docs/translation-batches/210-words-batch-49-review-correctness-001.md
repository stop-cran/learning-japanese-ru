# B210 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `9d9c00961ef457eac80eb8f37e9ca7e8522245fa` (tree `6ee737bce5f742105ab95f7cffbfb99f12dd0bde`),
> the signed candidate pushed before review.
> Later reconciliation is in `210-words-batch-49-recheck-001.md`.

Snapshot: RU 9d9c00961ef457eac80eb8f37e9ca7e8522245fa, compared with parent f28fc34bea93d1843eeb6569789f144c07f67668 and the supplied frozen EN 6af98cb source. HEAD matched; git status --porcelain was empty at initial and closing checks. No uncommitted repository changes included.

Scope: Independent, blind, read-only review of correctness and scoped coverage. Actual model identifier is not exposed/verifiable here; no other reviewer was consulted or delegated to.

For EACH following file, I read the COMPLETE RU card and its COMPLETE frozen EN counterpart, including front matter, every example, all explanatory sections and citations:
- words/年間.md
- words/年月.md
- words/年寄り.md
- words/年代.md
- words/いつでも.md
- words/常に.md
- words/年中.md
- words/平等.md
- words/平均.md
- words/平和.md
- words/幕.md
- words/常識.md
- words/帰宅.md
- words/帯.md
- words/差別.md
- words/巨大.md
- words/巣.md
- words/大陸.md
- words/州.md
- words/嵐.md
- words/岩.md
- words/屋根.md
- words/届く.md
- words/居間.md
- words/居眠り.md
- words/居る.md
- words/就職.md
- words/就く.md
- words/ボーイ.md
- words/少年.md

Also read the binding RU instructions/reference; inspected all changed baseline runtime passages in the seven kanji and fifteen existing word files. Existing comparator titles and relevant passages were checked for 老人, 等しい, 帰る, 帰り, うとうと, いる, いらっしゃる, おいでになる, 参る, 習う, 座る, 世界, 職, 職業, 店員 and 男の子. Those comparator cards are not claimed as separate full-article reviews. Read the frozen EN source-list rows for 帯, 就職 and ボーイ. Did not read the forbidden author/reviewer/batch/tracking material.

Verdicts:
- Correctness: NEEDS FIX — 差別 (C1), 居眠り (C2), 帯 (C4). Other 27 assigned cards: CLEAN within this facet and scope.
- Scoped coverage: NEEDS FIX — 岩 (C3), 帯 (C4). Other 28 assigned cards: CLEAN within this facet and scope.
- Comprehensibility and exhaustive quiz-pool safety: not assigned; no verdict.

Findings:

C1; Minor; correctness; words/差別.md:20.
Claim/impact: 国籍 is translated as «национальность», changing the discrimination example's basis from citizenship/state membership to what Russian readers ordinarily understand as ethnic affiliation. The grammar with で is retained, but this lexical distinction is lost.
Remedy: replace the Russian example translation with «Нельзя дискриминировать людей по гражданству.»
Evidence: [JMdict/Jisho 国籍](https://jisho.org/api/v1/search/words?keyword=%E5%9B%BD%E7%B1%8D), lexical sense 1, “nationality; citizenship”; [日本大百科全書 国籍](https://kotobank.jp/word/%E5%9B%BD%E7%B1%8D-64086), opening definition 国家の構成員であることを示す資格. [Kuznetsov, национальность](https://gramota.ru/meta/natsionalnost), sense 1, «Принадлежность к какой-либо нации, народности», with «Русский по национальности». This is a distinction between the Japanese word and the normal Russian reading, not a claim that every historical/specialist use of «национальность» excludes citizenship.
Confidence: high.

C2; Minor; correctness; words/居眠り.md:4,12,16,21.
Claim/impact: the title «невольный сон» and the definition «сам того не собираясь» make unintendedness a condition of the word itself. This is stronger than EN and conflicts with the correctly retained line 21: the unintended/regretted result is supplied by てしまいました, not a separate lexical meaning of 居眠り.
Remedy: use «дремота; сон сидя» in title/H1; begin line 16 «居眠り — это когда человек дремлет или задрёмывает, особенно сидя.» Keep the accidental translation of the first example and its てしまいました explanation.
Evidence: [JMdict/Jisho 居眠り](https://jisho.org/api/v1/search/words?keyword=%E5%B1%85%E7%9C%A0%E3%82%8A), sense 1, “nodding off (while sitting); dozing”; [Digital Daijisen 居眠り](https://kotobank.jp/word/%E5%B1%85%E7%9C%A0%E3%82%8A-435380), 座ったり腰かけたりしたままで眠ること. [Kuznetsov, невольный](https://gramota.ru/meta/nevolnyy), senses 1–3, explicitly concerns inadvertence, involuntariness or absence of volition; [дремота](https://gramota.ru/meta/dremota), sense 1, describes a half-asleep state. These support removing the added requirement, not asserting that unintended dozing is unusual.
Confidence: high, especially for the internal contradiction.

C3; Minor; scoped coverage; words/岩.md:33.
Claim/impact: EN's note “Music called ‘rock’ is ロック” is omitted. This is a small source-note retention gap under this assignment's explicit requirement to retain EN notes/Japanese teaching points. The existing Russian rock/boulder explanation is not incorrect, and the English ambiguity is not itself a Russian learning problem.
Remedy: add «Музыкальный жанр „рок“ по-японски называется ロック.» This retains the Japanese point without importing an English-dependent pun.
Evidence: frozen EN words/岩.md, Distinctive meaning; [JMdict/Jisho ロック](https://jisho.org/api/v1/search/words?keyword=%E3%83%AD%E3%83%83%E3%82%AF), the separate lexical entry whose first sense is “rock (music)”, not the homonymous “lock” entry. The source-list-gloss exception does not apply: this is an explicit Japanese vocabulary note in the source article.
Confidence: high for the omission; low learning impact, hence Minor.

C4; Minor; correctness/scoped coverage; words/帯.md:4,11,15–17.
Claim/impact: the general “band or strip” sense is narrowed to «опоясывающая полоса» / «и вообще полосу, охватывающую что-либо». Wrapping a book or the waist is a valid instance, but the added requirement to surround something is not the general shape-based sense taught by EN.
Remedy: title/H1 «пояс кимоно; длинная узкая полоса»; replace line 17 with «и вообще длинную узкую полосу, по форме похожую на пояс.» Keep the book/CD example and the distinction from the technical suffix たい unchanged.
Evidence: [JMdict/Jisho 帯](https://jisho.org/api/v1/search/words?keyword=%E5%B8%AF), おび entry sense 3, “band; belt; strip”, separate from the たい suffix entry; [Digital Daijisen おび](https://www.weblio.jp/content/%E3%81%8A%E3%81%B3), sense 3, 1に似た形のもの (a thing similar in SHAPE to sense 1), with 帯紙. [Kuznetsov, опоясать](https://gufo.me/dict/kuznetsov/опоясать), actual entry inspected in raw HTML, sense 2 «Расположиться вокруг чего-либо; окружить, охватить»; [полоса](https://gramota.ru/meta/polosa), senses 1–2, supports the general long/narrow piece or shape without requiring enclosure. No new Japanese collocation is proposed as evidence.
Confidence: high for the added semantic restriction; impact is localized.

Optional: none.

Limits:
- All 60 Japanese example sentences were independently checked as exact retained strings; full-card reading and a Japanese-token comparison found only the missing ロック note. Original metadata is preserved except the explicit additional RU quiz exclusions; no original exclusion was dropped. No EN link to an existing RU target was lost. Unlinked pointers to unavailable RU targets were not treated as defects.
- Actual JMdict/Jisho forms, lexical senses and restrictions were inspected for all 30 words, plus the relevant comparison entries. The API initially required a second, reading-aware selection for いつでも (listed as 何時でも); kana-only ボーイ was inspected correctly. API lexical entries were distinguished from place-name and Wikipedia records. Live API inspection does not certify historical ent_seq/version bytes.
- Also inspected Daijisen おる sense 5 and 平均 sense 3, and the cited 着く / 日中辞典 就く seating entries. Russian-specific choices were checked using actual Kuznetsov entries: мир (both homonyms), трудоустройство sense 2, служащий (service-sector employee), скромный senses 1/3 and the entries cited above; several search-page requests failed, so successful meta pages/raw entry HTML were used instead of search summaries.
- The 帯/就職 source-list correction passages do not claim recovery of the compiler's intention; the frozen source rows support the mismatch descriptions. ボーイ does not add an unsupported source-list provenance claim. No source-markup leak or new Japanese sentence lacking a required reading was established.
- `python -X utf8 -B tools\validate.py` on the primary RU checkout: exit 0, `0 error(s)`. No generator, checkout, staging, commit or push was run. Structural success is not a linguistic or device certification. Only this report was written.
- No native-speaker/device review, exhaustive historical/region/register survey or full existing-pool quiz audit is claimed. No material unresolved source-access limitation remains behind a CLEAN verdict.

# B249 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `a8e87dd42d8d6fb01c89b03aa12b995550acc585` (tree `82d39083172fc5e751eed8b92d9932a1a19aa623`),
> the signed candidate pushed before review.
> Later reconciliation is in `249-words-batch-88-recheck-001.md`.

Snapshot: RU a8e87dd42d8d6fb01c89b03aa12b995550acc585, parent 35ae8ce631ae2e14c6bac809c19a529aa3d03323. Primary checkout HEAD matches; git status --porcelain is empty. Frozen EN HEAD is 6af98cb717755690a9ca793e5454a96ebd7a8f9f, also clean.

Scope: CORRECTNESS and SCOPED COVERAGE for batch 249. Model identity is not independently verifiable. The complete RU body and front matter of EACH file below were read against its complete frozen EN original:

- words/発売.md
- words/スタート.md
- words/発つ.md
- words/畳む.md
- words/住居.md
- words/住まい.md
- words/番地.md
- words/略す.md
- words/留守番.md
- words/留まる.md
- words/あてはめる.md
- words/応用.md
- words/申請.md
- words/申し訳ない.md
- words/田植え.md
- words/実用.md
- words/当番.md
- words/公務.md
- words/役目.md
- words/用途.md
- words/用語.md
- words/原産.md
- words/産地.md
- words/生長.md
- words/厚かましい.md
- words/ずうずうしい.md
- words/生意気.md
- words/生年月日.md
- words/人命.md
- words/生存.md

Also inspected the candidate's existing-card link-restoration diffs: kanji/厚.md; words/みっともない.md, ゴール.md, ストップ.md, 成長.md, 止まる.md, 相撲.md, 苗代.md, 西暦.md, 誕生日.md. These were link-only changes, not new Japanese claims. Comparison checks included current titles/readings of all 99 linked word targets and complete reused bodies of 止まる, 成長, 広げる, 留守, 公務員 and 経つ. Selected definitions/register passages of other principal neighbors were also read.

Read the three binding RU documents and the relevant frozen EN format/JLPT policies. Ran the primary checkout's validator directly with python -X utf8 -B: exit 0, "0 error(s)". No generator, checkout, staging or repository edit was performed.

Verdicts: Correctness CLEAN; scoped coverage CLEAN, for all 30 listed articles. No per-article exception. CLEAN means no actionable defect established, not proof of exhaustive correctness. Russian comprehensibility and quiz quality are not separately scored.

Findings: None.

Verification evidence and dispositions:

- All 60 Japanese example sentences and their kana readings match EN verbatim. A separate Japanese-token comparison found no lost lexical phrase except the template label 地域名 in 原産, correctly translated as "название местности". Added Japanese tokens are repeated reading/source labels, adjective-class terminology, or the new exclusion IDs; they do not introduce another example or alter a conjugation.
- Non-title front matter is preserved, except the two deliberate added guards: 住まい → 住居 and 用途 → 応用. Both are defensible direct overlap protections. The frozen docs/content-format.md explicitly says a declaration on either card protects both directions; reciprocal declarations are not required. All exclusion targets exist.
- Every EN link to an existing RU target survives. The seven absent-target links remain plain text: kanji/畳, 略, 訳, 植 and words/特売, 建つ, あてはまる. Their teaching content remains. 畳む's added 広げる link exists and its "раскладывать, разворачивать" gloss fits that card. Dictionary URLs are retained; punctuation and source-label changes do not change the cited source.
- Inspected actual Jisho/JMdict forms, senses and parts of speech for all 30 words, then checked the cited primary entry numbers against the pages' actual JMdict edit links. The IDs match: 発売 1477810; スタート 1069370; 発つ 2857436; 畳む 1356780; 住居 2841455; 住まい 1595750; 番地 1482360; 略す 1551960; 留守番 1552800; 留まる 2657130; あてはめる 1586530; 応用 1180060; 申請 1363130; 申し訳ない 1612040; 田植え 1442810; 実用 1321480; 当番 1449220; 公務 1274810; 役目 1538080; 用途 1546380; 用語 1546270; 原産 1261470; 産地 1303820; 生長 1379370; 厚かましい 1275330; ずうずうしい 1595940; 生意気 1378790; 生年月日 1379410; 人命 1369400; 生存 1379230. Sources: https://jisho.org/search/発売 and corresponding exact-word search pages; https://jisho.org/api/v1/search/words?keyword=発売 and corresponding exact-word queries.
- Independently read the named Digital Daijisen sections, not merely other dictionaries on Weblio. Particularly consequential confirmations:
  - https://www.weblio.jp/content/住まい: derivation from 住まう, living/life and dwelling senses, suffix ずまい and spelling 住居.
  - https://www.weblio.jp/content/住居: the じゅうきょ heading and 住居を定める.
  - https://www.weblio.jp/content/略す: modern godan form derived from 略する, separate from the classical conjugation.
  - https://www.weblio.jp/content/留まる: とどまる includes stopping, staying and limited scope; とまる includes perching and fixation. RU keeps the qualifications.
  - https://www.weblio.jp/content/申し訳ない: apology/imposition and the explicit note that 申し訳ありません/ございません are not categorically wrong. JMdict sense 2 independently supports gratitude.
  - https://www.weblio.jp/content/生長 and https://www.weblio.jp/content/成長: plant focus is not an absolute spelling partition.
  - https://www.weblio.jp/content/図々しい: explicit ateji note.
  - https://www.weblio.jp/content/生意気: presumptuous conduct relative to age/ability; not praise for confidence.
  - https://www.weblio.jp/content/実用, /公務, /当番, /役目, /用語, /原産, /産地, /生年月日, /人命 and /生存: the noun/usage distinctions and qualified glosses are supported.
- Checked the on/kun classification claims against actual https://kanjiapi.dev/v1/kanji/<character> responses. Examples: 留 has ル and 守 has ス as on readings; 生 has native なま; 意/気 have イ/キ as on readings; 役/目 support the on-first mixed reading やくめ. 畳 supports たた.む; 略 supports リャク. These checks establish readings, not historical etymology. RU's cautions against literal component stories preserve EN.
- All 30 jlpt: 2 labels and selected entry identities match the frozen docs/n2-vocabulary-sources.tsv rows under docs/jlpt-levels.md's vocabulary policy. They were not inferred from kanji grades or a missing Jisho level.
- The omitted English-only "on sale" ambiguity and English tense-ending warning do not remove the Japanese points: 発売 distinguishes availability from discount and permits continuing 発売中; スタート retains the する conjugation examples. Rebuilt apply/application, function, life and apology comparisons preserve the Japanese distinctions and their qualifications.
- No consequential tense, polarity, transitivity, gender or subject error was established in the Russian examples. Explicit "мы" occurs in contextual translations with implicit Japanese subjects, usually already present in EN. Masculine first-person past forms do not claim that the Japanese wording encodes gender. "уехал в командировку" can contextually convey being away; it is not evidence of a universal equivalence for ～ている.
- Checked the requested Russian words against actual Gramota entries:
  - https://gramota.ru/poisk?query=бесстыжий&mode=slovari: Kuznetsov identifies the lowered-register synonym of бесстыдный; this fits the explicitly harsh criticism described here.
  - https://gramota.ru/poisk?query=беззастенчивый&mode=slovari: acting without shame, бесцеремонный/наглый.
  - https://gramota.ru/poisk?query=произрасти&mode=slovari: plant growth and the derived noun произрастание; not solely geographical distribution.
  - https://gramota.ru/poisk?query=присмотреть&mode=slovari: sense 1 explicitly includes присмотреть за домом; присматривать is its imperfective.
  - https://gramota.ru/poisk?query=отбывать&mode=slovari: departure sense, separately from serving a sentence.
  - https://gramota.ru/poisk?query=обременить&mode=slovari: sense 2 covers imposing inconvenience, with a request example.
  - https://gramota.ru/poisk?query=оборваться&mode=slovari: sense 3 includes life ending tragically.
  - https://gramota.ru/poisk?query=исконный&mode=slovari: original/from the beginning.

Optional: None proposed within the assigned facets.

Limits: This is not an app/reader acceptance test, full-corpus synonym audit, native-speaker certification or historical-etymology study. Existing neighboring articles were not all re-reviewed in full. Quiz candidate behavior and Russian beginner readability remain outside the assigned verdicts. Initial Jisho rate limits were resolved with throttled follow-up; shell kanjiapi requests returned 403, but actual responses were obtained through web_fetch. No consequential source check remained blocked. No author/reviewer report, prohibited scratch checkout, RU batch record or tracking ledger was consulted.

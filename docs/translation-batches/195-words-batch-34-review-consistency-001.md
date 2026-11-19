# B195 consistency and quiz-safety review (batch `195-words-batch-34`)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `4a2fd76f6380d7478317c486f1042215190a5934` (tree `02afdeec8bfbf21e076e959600ab7ed18980f642`),
> the signed candidate pushed before review.
> The report's own first-level heading is replaced by this record's heading; the text below it is unchanged.
> Later reconciliation is in `195-words-batch-34-recheck-001.md`.

Snapshot: `4a2fd76f6380d7478317c486f1042215190a5934` (HEAD of `full-ru-195-words-34`; working tree clean before and after; no uncommitted changes).
Scope: all 30 new `words/*.md` cards read in full against RU conventions and EN front matter; the 10 navigation-only restorations (diff reviewed line by line); `manifest.json`; `docs/translation-batches/195-words-batch-34-intake.json`. Facets: consistency, quiz safety, cross-file integration. Reviewer model not verifiable from inside the session. Checks run: `tools/validate.py` (0 errors), `build_manifest.py` (tree stayed clean), `rutools/link_parity.py` on the 40 paths (0 errors), plus my own scripts for hashes, EN-link/RU-link counts over every existing RU file, exclusion pairs and title-segment collisions against all RU word titles.

Verdicts:
- Consistency: CLEAN. Front matter matches EN except title/quiz_exclusions; every EN link is restored where the RU target exists (the only EN link with no RU target is `kanji/腰.md`, left as plain text; `occupation-and-role-endings` article is absent and is plain text); navigation-only files change only at link positions; manifest hashes for all 40 changed/new paths match the files; intake JSON hashes (candidate, source) match the files, the frozen EN and the manifest for all 40 payloads; no generated or stray files.
- Quiz safety: NEEDS FIX (one minor missing guard, F1). All EN exclusions are retained on the new cards; all RU-only additions are justified or conservative (table below).
- Scoped coverage of cross-file integration: CLEAN (no existing RU file has fewer batch-word links than its EN counterpart; no Russian-only link; no broken link in new cards).

Findings:
- F1; Minor; quiz safety; `words/虫歯.md:1-9` (front matter, title line 3, no `quiz_exclusions`): the RU title «кариес; кариозный зуб» adds the sense "decayed tooth", so «зуб; зубы» (`歯`) is a defensible answer for 虫歯 (the card itself says 歯 is "сам зуб, здоровый или больной"). EN «tooth decay; cavity» has no such overlap, so EN needs no guard. Remedy: add after `tags:` the line `quiz_exclusions: [歯]` (or drop «кариозный зуб» from the title). Evidence: JMdict 1604850 glosses include "decayed tooth" alongside "tooth decay; cavity"; the RU title promotes that sense. Direct pair on one side suffices. Confidence: medium (necessity depends on how often 歯 appears as a distractor).

Exclusions beyond EN (dictionary basis; necessity):
| Card → target | Basis | Class |
|---|---|---|
| 表情 → 表現 | 表現 (JMdict) "expression, representation" vs 表情 "(facial) expression"; RU titles «выражение лица» / «выражение» | required (RU wording collision; EN has no guard because the glosses differ) |
| 表情 → 現れ | 現れ "indication; embodiment; expression"; RU title segment «выражение» | required (RU-only gloss collision; mild) |
| 衣服 → 洋服 | 洋服 "Western-style clothes" is a subtype of 衣服 "clothes"; existing 洋服↔服 guard | conservative |
| 衝突 → 喧嘩 | 喧嘩 "quarrel; fight" vs 衝突 sense 2 "conflict (of opinions)"; card admits «поссориться» as translation | required (RU «конфликт» ≈ «ссора») |
| 衛星 → 友, 連れ | 友 "friend; companion", 連れ "companion"; RU glosses contain «спутник» | required (RU homonym) |
| 衛星 → 月 | 月 "Moon", the Moon being an example of 衛星 (JMdict 1174760 sense 1) | conservative |
| 行動 → こと | こと "thing; event; act/deed"; RU «действие» vs «действия» | required |
| ライター → 記者 | JMdict 2844121 "writer (esp. for magazines)" vs 記者 "reporter; journalist"; card says roles overlap | conservative |
| 菓子 → ケーキ, 飴 | hypernym 菓子 "confectionery" vs hyponyms; existing guards ケーキ→お菓子, 飴→お菓子 give precedent | conservative (necessity unestablished; harmless) |
| 苦しむ → 苦痛 | 苦痛 "pain; suffering" cognate noun of the same RU root «страдание/страдать» | conservative |
| 舌 → 言葉 | 言葉 RU title includes «язык»; 舌 «язык (орган)» | required (RU segment) |
| 脇 → 横 | 横 "beside; side"; card itself says 道の横/道の脇 are both "beside the road"; RU «сбоку» in both titles | required |
None is unjustified: no antonym/contrast taught by the card is guarded, no merely topical pair.

Missing-guard screen (all RU titles, direct and stem overlap): no other required guard found. Reviewed and judged not needed: 衣服/上着/着物/着る/袖, 衝突/事故/轢く/戦争, 衛星/星, 行儀↔規律, 行き/帰り/往復, 作家/詩人/記者 and the 作家–著者–ライター triangle (each pair guarded directly), 莫大/大きい/大した/多い, 苦しむ/苦しい/苦労/困る/酔う (title «страдать от укачивания» ≠ «страдать»), 芸術/文学/技術, 芝生/草/庭, 航空/飛行/飛行機/空港/鉄道, 舞台/芝居/台/風景 («сцена для выступлений» ≠ «сцена (из жизни)»), 臭い/香り/汚い, 天然↔自然 (EN pair kept), 自殺/死ぬ, 自慢↔誇り (EN pair kept), 自動/自動車/動く, 膝/足, 腰/尻/背中/腹, 腐る/古い/悪い, 才能↔腕 (EN pair kept)/技術/知能. No new title equals another word's whole title or segment except 舌/言葉 (guarded) and 舌/言語.

Optional:
- `words/舌.md` title «язык (орган)» vs 言語 «язык (как система)»: the displayed parentheticals disambiguate; adding `言語` to 舌's exclusions would mirror the 言葉 guard, but is not required.
- 脇 («место сбоку») vs 隣 («рядом; по соседству»): the card teaches "beside" in the body but the RU title dropped EN's "beside"; no guard needed unless 隣 is shown as a distractor; EN has none.
- `words/作家.md` refers to "статье об окончаниях названий профессий и ролей" with no link because that RU article does not exist yet; acceptable now, revisit when it is translated.

Limits: dictionary bases above rely on JMdict entry IDs quoted in the cards and my recollection of the senses; I did not re-open the dictionaries online. Linguistic correctness and comprehensibility are other reviewers' facets. Batch records/ledger/progress were deliberately not read.

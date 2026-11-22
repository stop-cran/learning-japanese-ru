# B245 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `004903db88a34b30524ca68ffc5b8dfbc085bbfa` (tree `86483e2d7614ce9f762d411eb04dc4c869602984`),
> the signed candidate pushed before review.
> Later reconciliation is in `245-words-batch-84-recheck-001.md`.

Snapshot: 004903db88a34b30524ca68ffc5b8dfbc085bbfa on full-ru-245-words-84 (`git rev-parse HEAD` matches). `git status --porcelain` was empty before review. My own `python tools/validate.py` run created untracked `tools/__pycache__/`; I deleted it, and status is empty again. No tracked file was touched. I did not run build_manifest.py.

Scope: all 30 new cards (words/標識 符号 競馬 童話 立ち止まる 窓口 突き当たり 架空 空想 空中 空っぽ 税関 移転 秤 私鉄 私立 おやすみ 祭日 お参り 敬う 祭る 神話 神様 祝日 先祖 祖先 社説 社会科学 磁石 確率) were read in full (front matter and body). Each was compared with its frozen EN counterpart on front matter and link sets; I did not re-read the EN prose line by line. All three navigation diffs (休日, 突き当たる, 編集) were read in full. I also checked manifest.json, the intake record (paths only), the validator, and a title screen of the 30 new titles (run by me) against all RU titles. Model: not verifiable.

Verdicts:
- Consistency (format, links, metadata, manifest, navigation files): CLEAN.
- Quiz safety: NEEDS FIX, minor. One RU-precedent guard is missing (F1, Low). Three optional or judgement items follow below.
- Scoped coverage / cross-file integration: CLEAN.

Evidence for CLEAN items:
- validate.py: 0 errors.
- Front matter: word/reading/jlpt/type/kanji/tags equal EN on all 30. The only front-matter differences from EN are the two RU-introduced guards (社説, 社会科学).
- Every RU link target exists. Dropped EN links are all absent targets:
  - kanji cards missing in RU: 競 符 童 税 移 敬 (EN links to these are plain text or absent in RU).
  - words missing in RU: 国立 子孫.
  - 習慣: the RU target exists, but the EN sentence "customs ≠ habits" is not carried into the RU 税関. The RU text has no mention to link. See Optional.
- Only RU-added link: 祭日 → 祝日.md. It exists, is a mutual pair (祝日 lists 祭日), and is useful navigation. It is acceptable.
- Manifest: sha256 of all 33 changed words/ files equals the manifest entries. No manifest entry points to a missing file. contentVersion changed. No stale hash was found.
- Intake record: its 33 payload paths equal the 33 words/ files in the content diff (30 new + 3 restored). `candidateRawSha256` equals the manifest for each. It has no learner content. It carries a note, a baseline and a sourceCommit.
- No generated or unrelated files in the diff: only 35 paths (33 words, manifest, intake).
- Navigation restorations are byte-identical to the parent except for the link brackets:
  - 休日:26 wraps `[お休み](おやすみ.md)` and keeps the gloss «выходной; отдых».
  - 突き当たる:30 wraps `[突き当たり](突き当たり.md)`. The verb forms on lines 20–22 and 24 stay plain, as in EN.
  - 編集:33 wraps `[社説](社説.md)`.
  - Path form `X.md` matches EN. Each file has exactly one occurrence. Wrapped positions match EN. Glosses are compatible with the new titles: 休日:26 uses «выходной; отдых» next to the おやすみ title; 突き当たる:30 uses «конец улицы или коридора», the same as the 突き当たり title; 編集:33–34 uses «редакционная статья…» next to the 社説 title. This is no defect.

Findings:

F1; Low; Quiz safety; words/童話.md:8 `quiz_exclusions: [話, 物語]`.
- Claim: 童話 «сказка; история для детей» and 歴史 «история» share the Russian word «история». The Russian meaning «история» = story is a defensible reading of the 歴史 title, and 歴史 can show up as a distractor for 童話, or 童話's title as a distractor for 歴史. No direct pair exists on either side (歴史 has `[話]` only; the title screen flags this pair).
- RU precedent: words/歴史.md already carries the RU-introduced guard `[話]` for the same «история» polysemy (the EN 歴史 has no quiz_exclusions), so the project treats this overlap as guard-worthy.
- Remedy: words/童話.md line 8 → `quiz_exclusions: [話, 物語, 歴史]` (EN entries kept, one appended). Declaring it on one side is enough.
- Evidence: JMdict 童話 "children's story, fairy tale"; 歴史 "history". Overlap is lexical in Russian only.
- Confidence: medium. Severity is low because the titles differ in other words and 歴史 is the dominant sense of «история».

Classification of the two RU-introduced guards:
- 社説→論文 (words/社説.md:8 `[記事, 論文]`; EN `[記事]`). Dictionary basis: JMdict 論文 = thesis, treatise, paper; 社説 = editorial. These are different senses, so the guard is conservative: it exists only because of the title overlap «статья». Necessity in an ordinary quiz is not established. It is harmless and may stay. It is also inconsistent: see F2 (評論 «критическая статья» is closer to an editorial and is unguarded).
- 社会科学→自然科学 (words/社会科学.md:8 `[科学, 自然科学]`; EN `[科学]`). Dictionary basis: JMdict 社会科学 "social science(s)", 自然科学 "natural science(s)". The titles «общественные науки» / «естественные науки» are distinct by their modifiers, and the article teaches 自然科学 as the contrasted field, not a synonym. Classification: unjustified (guards a contrast the article itself teaches; shared «науки» only). It is harmless, and reverse-direction use does not matter (自然科学 already has `[科学, 自然]`). Optional: remove it, or keep it as conservative. Not required either way.

Optional (non-blocking):
- F2 (Low, judgement): 社説 «передовица; редакционная статья» vs words/評論.md «критический анализ…; критическая статья». Both are an opinion-article «статья», closer than 論文. 評論 has `[批評, 批判, 評価]`; EN 社説 does not guard it. If you want to keep the 論文 guard, apply the same standard: `quiz_exclusions: [記事, 論文, 評論]` (words/社説.md:8). Otherwise drop 論文 and keep EN parity. Not required.
- 上京 «поездка или переезд в столицу (в Токио)» vs 移転 «переезд (учреждения)»: shared word «переезд», but the qualifiers (в столицу / учреждения) separate them. No guard needed. Judged not required. Also 踏切 «железнодорожный переезд» is a homonym, not defensible.
- 祭日 «день празднества (обряда)…» vs 祭 «фестиваль»: close in meaning but EN also leaves it unguarded (the EN 祭日 links 祭, no guard); 祭 has `[お祭り, お祝い, 祝い]`. The difference «день» is in the title. Judged not required. Parity retained.
- 税関 (no quiz_exclusions): 税 «налог» ≠ «таможня», no conflict. 秤 «весы»: 計る «измерять» and 重量 «вес» are different types, no conflict. 私立: 公立 is an antonym, 機関 / 個人 only share a stem; not needed. 磁石 «магнит; компас»: no RU card for 方位磁針, マグネット or コンパス; 針 is «игла; стрелка (часов)». None of these four needs an exclusion.
- 税関: the RU text drops the EN sentence about 習慣 (not applicable in Russian: «customs» ≠ «обычаи»), so there is no link to restore. Fine.
- Tag vocabulary: 敬う, 祭る and 拝む have `verb` without `godan-verb`, while 立ち止まる has `godan-verb`. This is identical to EN, so it is parity, not a defect.
- All other EN exclusions are retained exactly (no DIFF vs EN except 社説 and 社会科学, which only append). The title screen had 0 exact-segment overlaps; stem-only overlaps were checked and none was a defensible correct answer apart from F1. Dense-cluster pairs listed in the task are all guarded by a direct pair on at least one side (標識, 符号, 競馬, 立ち止まる, 窓口, 突き当たり, 架空, 空想, 空中, 空っぽ, 移転, 私鉄, おやすみ, 祭日, 祝日, お参り, 敬う, 祭る, 神話, 神様, 先祖/祖先, 社説, 社会科学, 確率).

Limits:
- EN prose was not compared line by line; only front matter, link sets and exclusions were compared programmatically. Dictionary senses were taken from the cards' own cited JMdict/Daijisen references and my own knowledge. I did not re-open the dictionaries.
- Reverse direction of exclusions was not required and was not checked.
- Pre-existing differences from EN in the three navigation files are outside this batch.

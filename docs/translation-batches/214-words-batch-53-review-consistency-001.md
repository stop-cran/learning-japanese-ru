# B214 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `a371c734a15f44e674e87a3a9ea0c9f147961d90` (tree `6712ca2c3fe82adc1a20a1e86be3a7a58861d70a`),
> the signed candidate pushed before review.
> Later reconciliation is in `214-words-batch-53-recheck-001.md`.

Snapshot: a371c734a15f44e674e87a3a9ea0c9f147961d90 (HEAD confirmed; git status clean)
Scope: Batch 214-words-batch-53 (diff 0138d32..a371c73, 47 files), consistency / quiz safety / integration facet. Reviewer model not verifiable by me.
  Read in full against frozen EN originals: all 30 new words/*.md cards; all 15 navigation diffs (-U0: kanji 区 否 含 周 囲; words 敵 政府 製品 認める 議会 議員 営業 食品 金曜 除く; 22 link restorations).
  Checked mechanically: link_parity.py on 30 cards (clean); manifest.json sha256 of all 45 changed/new kanji+words files (0 mismatches; every manifest path exists); intake JSON path list only (45 paths = diff, no learner content); clean worktree.
  Not read in full: manifest.json, intake JSON (checked as above).
Verdicts:
  consistency: CLEAN
  quiz safety: CLEAN (all EN exclusions retained; RU additions classified below; no required missing guard established)
  scoped coverage (integration/links/manifest): CLEAN
Findings: None actionable. Link restorations hrefs match EN exactly; plain-text targets (線, 境, 水平線, 住民, ただ, 仲間, 加わる, 肯定) are absent in RU so unlinked is correct. Front matter, type/kanji fields and EN exclusions preserved.
  RU-introduced quiz_exclusions (direct pairs; basis = RU titles/card senses; dictionary entries not re-fetched):
  - 土曜→土曜日: identical title «суббота» — required.
  - 土産→祝い: «подарок» overlap with 祝い gift sense — conservative/likely required.
  - 商売→貿易: «торговля» vs «международная торговля» — likely required.
  - 商人→店員: «торговец» vs «продавец» (RU-only overlap) — conservative.
  - 国語→科目: «японский как школьный предмет» vs «учебный предмет» — conservative.
  - 善→道徳: «добро» vs «мораль» — conservative, necessity unestablished.
  - 吸収→夢中: shared «поглощ-» but different parts of speech — conservative, necessity unestablished.
  None unjustified enough to require removal.
Optional:
  - O1: consider 吸う in 吸収 quiz_exclusions (吸う «всасывать» vs 吸収 «впитывание»; EN had no pair; titles differ in POS) — low.
  - O2: 味方 vs 相手 («союзник» vs «партнёр») borderline; not required.
Limits: No native review; dictionaries not re-fetched. Pre-existing, unchanged by this batch: RU kanji/地.md has an extra 地図 link versus EN and leaves 土地 unlinked. A broad RU-title stem screen was aborted (slow); remaining pair candidates came from word_title_screen.py leads and counterpart-card heads only.

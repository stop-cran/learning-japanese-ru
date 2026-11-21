# B221 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `f888c34e8eb7c8d29c76c0433dbb3b0035ee8e3b` (tree `0fb4d226b4ec03bd217f2acb300a050473e1e0b1`),
> the signed candidate pushed before review.
> Later reconciliation is in `221-words-batch-60-recheck-001.md`.

Snapshot: f888c34e8eb7c8d29c76c0433dbb3b0035ee8e3b (branch full-ru-221-words-60); clean tree (git status empty before and after).
Scope: Consistency + quiz safety + scoped cross-file integration for batch 221. Read in full: all 30 new RU cards, all 8 navigation diffs
  (articles/numbers-and-counters.md:712 トン; いす:33 ベンチ; ワイン:36 ビール; 劇:35 ドラマ; 帯:33 ベルト; 泡:28 ビール; 玉:35 ボール; 球:29 ボール),
  manifest.json integration, docs/translation-batches/221-words-batch-60-intake.json. EN originals: first 10 read in full; the other 20 compared by script
  (front matter, links, line counts). Reviewer model not verifiable from inside the session. Ran validate.py (0 errors) and read-only own screens
  (title overlap, link parity); did not run build_manifest.py or any generator.
Verdicts:
  - Consistency: CLEAN
  - Quiz safety: NEEDS FIX (one minor finding, below)
  - Scoped coverage (cross-file integration): CLEAN
Findings:
  1. Minor; quiz safety; words/パイプ.md front matter/title; the RU title adds «связи, канал общения между людьми» (EN: "pipe; tube; communication
     channel"). Only 管 and 付き合い are guarded. Unguarded titles with the same meaning: 関係 «связь; отношения», 連絡 «связь; контакт»,
     仲 «взаимоотношения (между людьми)». 付き合い already declares [関係, 仲], showing this is a confusable cluster.
     Impact: a learner could defensibly choose 関係/連絡 for the パイプ title. Remedy: quiz_exclusions: [管, 付き合い, 関係, 連絡] (optionally 仲),
     or retitle closer to EN («труба; трубка; канал связи»; that still touches 連絡). Evidence: title strings read from the files; confidence: medium.
Guard classification (RU-introduced exclusions beyond retained EN ones):
  Required: ハンサム→美しい, ハンサム→きれい (shared «красивый»); バン→束 («пучок»); ドライブ→旅行 («поездка»); ド→いちばん («самый»); ド→完全 («совершенный»).
  Conservative but justified: ボール→ちゃわん («миска»); マスター→上達 («навык»); ドラマ→出来事 («событие»); ビール→酒, ビール→お酒 (hypernym; matches ワイン);
    ハイキング→観光 («туризм»); パイプ→付き合い (strong overlap of «общение/людьми»).
  Possible over-guard: プロ→職業 («профессионал» vs «профессия») - different parts of speech, not a defensible swap; harmless.
  Retained EN guards all present (ミルク, ミス, ママ, マスター, ボール, ホーム, ベルト, パイプ, バッグ, ドラマ, ドライブ). Every lexically overlapping pair from the dense-cluster
  list is guarded on at least one side; no unguarded segment overlap found otherwise. Other screens (ベンチ/席, ドレス/服, ペンキ/色, パスポート/パス, バン/パン,
  ビデオ/映画, トン/キログラム, ホーム/駅, ミルク/素, マスター/覚える/学ぶ) showed no defect.
Consistency evidence:
  - Front matter identical to EN except title and quiz_exclusions for all 30 cards; heading/section pattern matches existing RU cards.
  - Navigation diffs are single-line link wrappers at the EN link position, path forms preserved.
  - EN-link parity: no lost links. 5 RU-only extra links (ホーム→帰宅, ビール→ビル, バイオリン→弾く, ドラマ→テレビ, トン→キログラム); targets exist and
    EN mentions each unlinked in a substantive comparison, so acceptable. ソファー, 楽器, 絵の具 have no RU file and correctly stay plain text.
  - manifest.json: 4744 entries; all .md hashes match disk; no on-disk file missing.
  - Intake JSON: 38 payloads equal the candidate content diff (30 cards + 8 files); candidateRawSha256 equals disk and manifest for all 38; held empty;
    adds no learner content.
Optional: Consider dropping プロ→職業 (over-guard); no need to change.
Limits:
  - 118 strokes/*.json manifest hashes differ from the raw file hash; unchanged from the parent commit (pre-existing, probably normalized hashing); not part of this batch.
  - Pre-existing differences from EN in files touched by navigation edits (e.g. ワイン:36 plain-text ウイスキー, no RU file; EN 帯:28 links 紐, EN いす:27 links 席) are out of scope.
  - No native-speaker verification; translation accuracy belongs to other facets. EN originals of 20 cards compared mechanically, not line by line.

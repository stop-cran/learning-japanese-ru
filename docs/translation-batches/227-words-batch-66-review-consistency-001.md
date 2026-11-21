# B227 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `5cf2313776672567fd1454fffd027b253bb10278` (tree `b8e291d86716374cd700fba67aaccfa3900d3caf`),
> the signed candidate pushed before review.
> Later reconciliation is in `227-words-batch-66-recheck-001.md`.

Snapshot: RU repo 5cf2313776672567fd1454fffd027b253bb10278, clean tree (HEAD verified, `git status --porcelain` empty). Frozen EN 6af98cb.
Scope: Consistency and quiz-safety facets of batch 227 (227-words-batch-66): 30 new word cards, 5 navigation-only link restorations (kanji/区, kanji/域, words/句読点, words/意見, words/預ける), manifest, intake record. Reviewer model identity not verifiable. Blind: author reports, title-screen outputs, translation-batches/drafts/tracking not read (the intake JSON was read only to check it against the diff).
Files read in full: all 30 new cards; full diffs of the 5 nav files. EN comparison: front matter, links and line counts scripted for all 30; EN prose read in full for 突く only.
Verdicts: consistency CLEAN; scoped coverage (cross-file integration) CLEAN; quiz safety NEEDS FIX (two minor items).
Checks passed: validate.py 0 errors; intake's 35 payload paths equal the 35 changed content files, hashes match; manifest adds the 30 cards and updates the 5 nav hashes, with no missing or extra entries; all md hashes recompute equal. RU front matter equals EN except titles and one added exclusion. All EN exclusions retained. Links match EN except absent RU targets left as plain text (点く, 突き当たり, 膨らます/む, 乾燥, kanji 境 脳 領 預 順) and one RU-only link 突っ込む→引き出す (target exists; acceptable). All link targets exist. The 12 restored nav links match EN positions and path forms; no prose changes.
Findings:
- F1 minor; quiz safety; words/境界.md:10; RU-only label collision: title «разделительная линия» vs 線 «линия; провод» (EN "boundary"/"line" needed no guard). Remedy: quiz_exclusions: [境, 国境, 限界, かぎり, 制限, 限る, 線]. Basis: RU labels; classification conservative. Confidence medium.
- F2 minor; quiz safety; words/雑音.md:10; 雑音 «помехи (в сигнале)» vs じゃま «помеха; вмешательство». Remedy: add じゃま to quiz_exclusions. Classification conservative. Confidence medium.
- Classification of the only added RU exclusion 順序→決まり: REQUIRED (RU 決まり «правило; установленный порядок» collides on «порядок»; 決まり already excludes 順/順番). No other RU-only exclusions.
Optional (low confidence, no fix required): 預かる «хранение» vs 保存; 突っ込む «засовывать» vs 挿す; 頼もしい vs 堅い «надёжный»/信頼; 頭脳 vs 中心; 突く vs 突き当たる.
Limits: dictionary entries/JMdict IDs not independently rechecked; EN prose not compared line by line beyond 突く; 118 strokes/*.json manifest hash mismatches appear to be a CRLF working-tree artifact, not batch-related (unverified); check_content_budget not completed (timed out).

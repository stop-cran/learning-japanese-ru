# B190 consistency and quiz-safety review (batch `190-words-batch-29`)

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `0462ca5d05879b79e3fc4c28893b707b1c7af588`.
> Later reconciliation is in `190-words-batch-29-recheck-001.md`.

Snapshot: RU `0462ca5` on `full-ru-190-words-29` (HEAD confirmed, tree clean, no uncommitted changes); frozen EN `6af98cb`.
Scope: 30 new word cards read in full against the EN originals; 8 navigation-only files (diffed); `manifest.json`; `docs/translation-batches/190-words-batch-29-intake.json`.
  Facets: consistency, quiz safety, cross-file integration. Reviewer model not verifiable from inside the session.
  Checks run: `tools/validate.py` (0 errors); `link_parity.py` on the 38 files and on all 3,073 RU words/kanji/articles files that also exist in EN
  (no LOST/EXTRA touching any batch target); my own SHA-256 of all 40 changed `.md` files against `manifest.json` (0 mismatches);
  `build_manifest.py` rerun reproduced the same contentVersion `a368e33d8e783e8b` and left the tree clean;
  intake candidate hashes equal the committed files and source hashes equal the frozen EN files (all 38 payloads).

Verdicts:
- Consistency: CLEAN (front matter, headings, links, kana-reading convention, JMdict citation style match existing RU cards; navigation-only files change only at EN link positions; manifest and intake consistent; no generated/unrelated files).
- Quiz safety: CLEAN. All EN exclusions are retained verbatim; no missing required guard found in the all-titles screen. Extra entries are classified below; none is harmful.
- Scoped coverage of cross-file integration: CLEAN. Eight restorations are exactly the existing RU links that EN has to the new targets; every other EN link to a batch word in an existing RU file was already satisfied.

Findings: none actionable.

Extra `quiz_exclusions` beyond EN (dictionary basis; necessity in an ordinary quiz):
| Card -> entry | Basis (JMdict sense) / displayed-title overlap | Class |
|---|---|---|
| 瞬間 -> 際 | 瞬間 "instant, moment" vs 際 "time, occasion, moment"; titles share "момент" | required |
| 迷惑 -> 不便 | 迷惑 "nuisance, inconvenience" vs 不便 "inconvenience"; titles share "неудобство" | required |
| 迷惑 -> 厄介 | 迷惑 "trouble, nuisance" vs 厄介 "trouble, burden, bother"; "хлопоты"/"хлопотный" | required (strong enough; same cluster as the EN じゃま/面倒/手間/苦労) |
| 迷子 -> 子, 子供 | "lost child" vs "child"; titles share "ребёнок" | required |
| 現代 -> 時代 | 現代 "present age, modern times" vs 時代 "period, era, age"; titles share "эпоха" | required |
| 近代 -> 時代 | 近代 "modern era" vs 時代 "period, era"; share "эпоха" | required |
| 現代 -> 現在 | 現代 "present day" vs 現在 "present, now"; titles "современность" vs "настоящее время". The 現在 card itself teaches 現代 as the broader-era word | conservative (real basis, necessity unestablished) |
| 辺り -> 側, 隣 | 辺り "vicinity" vs 側 "side, nearby", 隣 "next to, neighbouring"; titles share "рядом" | required |
| 辺り -> 頃 | 辺り sense "approximately (after a time expression)" vs 頃 "about (of time)"; 頃 title "около (о времени)" but 辺り title lacks any approximation gloss | conservative |
| 迎え -> 迎える | same-root noun/verb, "meeting an arrival" vs "to meet, welcome" | conservative |
| 迎え -> 会, 会合 | 迎え "meeting (of an arrival)" vs 会/会合 "meeting, gathering"; share "встреча". Card itself teaches the contrast | conservative |
| 農家 -> 家族, 家庭 | 農家 "farming household" vs 家族/家庭 "family"; titles share "семья" | required |
| 農家 -> 家 | farmhouse sense taught in body vs 家 "house"; the title does not contain "дом" | conservative |
| 農業 -> 産業 | agriculture is an industry; no displayed-title overlap | unjustified (hypernym/topical; harmless) |
| 通す -> 極める | "доводить до конца" vs "доводить до предела"; JMdict senses (carry through vs carry to the extreme) differ; overlap is only the Russian prefix | conservative, weak |
| 轢く -> 移る | RU "переехать (о транспорте)" vs 移る "переходить; переезжать" (no disambiguator on the 移る side) | conservative (translation-level homonymy, not a JMdict overlap) |
| 轢く -> 引っ越す | RU "переезжать (менять жильё)" already carries a disambiguator | unjustified (harmless; contrast also taught in the card) |
| 輪 -> 指輪 | 輪 "ring, loop" vs 指輪 "finger ring"; titles share "кольцо" | required |
| 転ぶ -> 落ちる | 転ぶ "fall over" vs 落ちる "fall"; titles "упасть"/"падать" | required |
| 身長 -> 成長, 増加 | 身長 "height" vs 成長 "growth", 増加 "increase"; titles share "рост" | required |
| 身 -> 肉 | 身 "flesh (of fish)" vs 肉 "meat, flesh"; the card teaches this contrast | conservative |
| 身 -> 中心 | 身 "main part" vs 中心 "centre, core"; titles share "часть" | conservative |

Optional (nonblocking):
- Consistency of approximation guards on 辺り: 頃 is guarded, but equivalent approximation titles (ころ, くらい, ほど, およそ) are not. Their titles do not overlap 辺り's displayed title, so I do not require them; either keep 頃 as a conservative extra or drop it. Not a defect.
- Unjustified extras (農業 -> 産業, 轢く -> 引っ越す) may be dropped if the owner prefers minimal exclusion sets; they cost nothing but narrow the distractor pool slightly.
- Homophones 轢く / 引く / 弾く (ひく) and 辞める / 止める (やめる, confusable-words CW026) are not excluded. That is consistent with the EN contract (spelling or reading alone is not a reason; displayed Russian titles do not overlap), so no guard is required.

Limits:
- Dictionary senses above come from my knowledge of JMdict/Daijisen, not re-fetched entries; "required"/"conservative" rest on displayed Russian-title overlap plus those senses. I did not independently audit linguistic accuracy (other reviewers' facet).
- Pre-existing `words/止める.md` links `kanji/留.md` which EN does not (link_parity EXTRA); unchanged by this commit, out of scope.
- Title screen run was only a lead; I supplemented it with a Russian-keyword scan of all 2,353 RU word titles. Pairs involving words absent from RU (追い越す, 従う, 兵, 屋根, 本人, 自己, 退職) cannot be guarded and are not required.

# B203 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `d6e95d46124d66f60472825a8db483b5702688f7`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 202 tree `459ddef` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `203-words-batch-42-recheck-001.md`.

Snapshot: RU worktree C:\Users\romanko\repos\learning-japanese-ru-b198, candidate tree d6e95d46124d66f60472825a8db483b5702688f7 vs base 459ddef. Verified: `git diff-index --cached --quiet` exit 0, `git diff --quiet` exit 0, `git ls-files --others --exclude-standard` empty (index and working tree equal the candidate; no uncommitted difference). Frozen EN 6af98cb.

Scope: Facets = consistency, quiz safety, scoped coverage of cross-file integration. Read in full (front matter + body, against the EN original's front matter/links): all 30 new cards — 注目 注 泥 波 泡 泉 沖 意志 決心 汚染 汗 氷 気味 気候 かわいそう 哀れ 気の毒 好む 気に入る 氏 毛布 比較 毒 母親 殺す 残す 死亡 歩道 正確 正直. Read in full the complete diffs (every hunk) of all 13 navigation files: kanji/亡.md, kanji/殺.md, words/およそ.md, 保存.md, 天候.md, 意思.md, 汚す.md, 決定.md, 涙.md, 父親.md, 自殺.md, 覚悟.md, 霜.md; and the full manifest.json diff. Mechanical checks run: tools/validate.py (0 errors); tools/build_manifest.py regenerated with no resulting diff (manifest not stale; 30 new + 13 changed hashes only); own script comparing front matter (all fields except `title` identical to EN except the extra exclusions listed below; H1 matches `# word（reading）— title`; 4 H2 sections each); own script comparing link hrefs RU vs EN per card; own screen of every new title (segments and 5-letter stems) against all RU word titles incl. both sides' quiz_exclusions; reverse scan of all EN words/kanji/articles/strokes for links to the 30 new words. Not read: batch records/ledger/reports (blind). Model: not verifiable by me.

Verdicts:
- Consistency: CLEAN (no exception).
- Quiz safety: NEEDS FIX (one minor missing guard, F1; the rest CLEAN).
- Scoped coverage of cross-file integration: CLEAN.

Findings:
F1; minor; quiz safety; words/正確.md:9 (`quiz_exclusions: [ちょうど]`); 正確 "точный; безошибочный" and 正しい "правильный; верный" are defensible answers for each other, yet no direct pair exists on either side (正確 has only ちょうど; 正しい has [確か, 合う, まじめ]; EN has none because 正確 is new). Impact: a 正しい question can offer 正確 (or vice versa) with "безошибочный"≈"верный"; the card's own text (Синонимы: 正しい "частично совпадает по значению") concedes the overlap. Remedy: replace line 9 with `quiz_exclusions: [正しい, ちょうど]` and regenerate manifest.json. Evidence: JMdict via Jisho — 正確 "accurate; correct; precise; exact"; 正しい "correct; right; proper". Confidence: medium (necessity judged from titles + shared gloss "correct"; not a hard defect).

Extra exclusions beyond EN (basis / necessity):
- かわいそう→残念: JMdict かわいそう "poor; pitiable; pathetic; pitiful" vs 残念 "regrettable; disappointing" (cluster of EN 気の毒→残念); Russian bodies share «жаль». Conservative.
- かわいそう→貧しい: shared English gloss "poor" (かわいそう sense 1; 貧しい "poor; needy"), but Russian titles disjoint and the article itself teaches the contrast. Conservative leaning unjustified; harmless.
- 哀れ→残念: 哀れ "pity; pitiable; miserable" vs 残念 "regrettable"; Russian titles disjoint; the article teaches it as a contrast. Conservative leaning unjustified; harmless.
- 好む→好き: JMdict 好む "to like; to prefer", 好き "to like; fondness"; "находить по вкусу" ≈ «нравиться/любить». Required.
- 気に入る→好き: JMdict 気に入る "to like; to take a liking to" ; «понравиться» ≈ «нравиться». Required.
- 気に入る→大好き: same root «нрав-» («очень нравиться»); weaker. Conservative.
- 比較→比べる: JMdict 比較 "comparison" (suru, transitive) = 比べる "to compare"; the article teaches 比較する «сравнивать». Required.
- 正確→ちょうど: JMdict 正確 "exact; precise", ちょうど "exactly; precisely"; «точный» vs «точно». Conservative (different POS).
All EN exclusions retained (注目→注意, 泉→春, 意志→意思, 決心→決定/覚悟/意志, 汚染→汚す, 気味→気分/気/気持ち, 哀れ→かわいそう, 気の毒→かわいそう/哀れ/残念, 気に入る→好む, 毒→害, 母親→お母さん). No new title equals any RU title or segment (only 母親/お母さん share «мать», guarded). Screened, no guard needed (titles qualified/POS-distinct; consistent with precedent 父親/親 unguarded): 注/注意・注射, 波/海・揺れる, 泉/井戸・水, 沖/海・海岸・港, 汚染/汚れる・汚い, 汗/涙, 氷/霜・雪・冷たい, 気味/雰囲気・怖い, 気候/天候・天気・季節・温暖・気温, 氏/君・方, 毛布/布団・布・毛・毛糸, 毒/薬・危険, 母親/父親・親・両親, 殺す/死ぬ・亡くなる・自殺, 死亡/死ぬ・亡くなる・自殺, 残す/残り・保存・残念, 歩道/道・道路・通り, 正直/本当・まじめ.
Links: every EN link in each new card is present in RU at the same target, or plain text only where the RU target is absent (kanji 泥 波 泉 汚 汗 氷 毒 氏 布 毛 比; words ビール 温泉 凍る お気の毒に 好み 嫌う — all verified missing); no Russian-only link; no broken target. Reverse scan: the only EN→new-word links whose RU source exists are exactly the 13 restored files; every hunk changes only link brackets/hrefs (no prose). No generated/unrelated files in the diff apart from manifest.json.

Optional (nonblocking, not defects):
- 残す: consider `quiz_exclusions: [残る]` (transitive/intransitive pair «оставлять»/«оставаться»; the deck guards 開ける↔開く, 汚す→汚れる, 決定→決まる); EN has none.
- 泥↔土 and 沖↔海: titles' qualifiers («мокрая земля», «вдали от берега») distinguish them; a guard would only be conservative.
- 正直↔まじめ: JMdict まじめ sense 2 "honest; sincere", but the RU titles («честный» vs «серьёзный; добросовестный») do not overlap; not required.

Limits: Dictionary evidence from Jisho's JMdict API/knowledge, not a full per-entry audit; Russian linguistic correctness and comprehensibility were not assessed (other facets). Quiz-defensibility judgments rest on the displayed titles; the app's option-selection logic was not run.

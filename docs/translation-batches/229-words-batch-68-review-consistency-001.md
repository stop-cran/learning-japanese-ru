# B229 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `af5541a48700cdb110c81f127f63f226ead77ae7` (tree `c17dd3521821d417879b7f68fd6d1d74c9cd88c8`),
> the signed candidate pushed before review.
> Later reconciliation is in `229-words-batch-68-recheck-001.md`.

Snapshot: RU `af5541a48700cdb110c81f127f63f226ead77ae7` (branch full-ru-229-words-68). `git rev-parse HEAD` printed that hash; `git status --porcelain` printed nothing (no uncommitted changes). Frozen EN `6af98cb` used as source.

Scope: CONSISTENCY and QUIZ SAFETY (plus cross-file integration). Model: not verifiable from inside the session.
Read in full (front matter and body), each against its frozen-EN counterpart by script (front matter, link multiset) plus manual read of the RU text: 学会 集会 集合 障子 間隔 隙間 隔てる 随筆 険しい 期限 限度 属する 附属 差し支え 妨げる 締め切り 締め切る 終了 ストップ 防止 警備 防犯 関西 関東 関わる 間接 開通 開会 開放 閉会 (30 of 30). Also read in full: the diffs of `kanji/了.md` and `words/感覚.md` (-U0 and against EN lines 28/33 and 33), the manifest diff and a full SHA-256 recomputation, and the intake record's path list (nothing else of it).
Tools run, read-only: `git`, `tools/validate.py` (0 errors), `word_title_screen.py` (output used only as leads), a link-resolution script, a Jisho API lookup for sense evidence (雨戸 困難 大変 卒業 関連 扱う 繋ぐ 障子 隔てる 間). I did not run `build_manifest.py` or any generator and did not read any author report, other review report, `docs/translation-batches/` (apart from the intake path list) or `docs/translation-drafts/`.

Verdicts:
- Consistency (front matter, links, terminology, navigation, manifest, intake): CLEAN
- Quiz safety: NEEDS FIX (one minor missing guard, F1; everything else CLEAN)
- Scoped coverage of cross-file integration: CLEAN
  (no per-article exceptions other than F1 on 締め切り)

Findings:
F1; Minor; quiz safety; words/締め切り.md:9 (`quiz_exclusions`); the RU title «срок сдачи; окончание приёма (заявок)» introduces the bare word «срок», which EN's «deadline; closing» does not. 期間 «срок; период» (words/期間.md:4) then reads as a defensible correct answer for 締め切り («срок» alone does mean a deadline in Russian), and 締め切り has no direct pair with 期間 in either direction (期間 declares only [時間, 時代, 間]). The same lead word is why EN guards 期限→期間 and 期限→定期. Impact: in an ordinary quiz, 期間 is a plausible distractor that a learner can defend for 締め切り. Remedy: change line 9 to `quiz_exclusions: [期限, 終わり, 仕舞い, 締め切る, 期間]` (then regenerate the manifest). 定期 «установленный срок; по графику; проездной» is the weaker analogue (定期 means regular/fixed-term); I would not require it. Evidence: titles above; JMdict 期間 = "period; term", 締め切り = "closing; deadline" (the RU card cites entry 1594590); the RU title was changed from EN's. Confidence: medium (the classification of «срок» as defensible is a judgment about Russian usage; the missing direct pair is certain).

Findings on the other items you asked to classify (none is a defect):

Consistency and links
- Front matter and tags equal EN for all 30 except the eight RU-introduced guards below; every EN exclusion is retained in EN order (RU additions are appended at the end); 関西, 関東 and 間接 have no `quiz_exclusions` key, as in EN. No dangling, duplicate or self exclusions (every target has an RU word file). `tools/validate.py`: 0 errors.
- Links: the multiset of link targets equals EN in all 30 cards except these absent targets, which stay plain text per the convention (I confirmed no RU file exists for 学科, 解散, 埋める, スタート, 解放) and the kanji 筆, 防, 接 (no RU kanji file). 開会→閉会 is the single RU-only link (see below). Every RU link resolves to an existing file; the EN kanji links match the front matter (切 and 閉 in both 締め切り and 締め切る). 妨 属 接 筆 締 防 附 随 隔 隙 障 have no RU kanji file, so 附属's «Ни у одного из этих знаков пока нет карточки» (附, 属) is accurate; it also links 付, which exists.
- 開会→閉会: acceptable. It is an antonym pointer with its own gloss in the Synonyms section, both cards are in this batch, EN 閉会 already links back to 開会, and the RU content-structure rule (links to existing cards at substantive introduction/comparison; no reciprocal-link requirement) permits it.
- Navigation-only files: `kanji/了.md` lines 28 and 33 and `words/感覚.md` line 42 differ from the parent only by the added link brackets/hrefs. They match EN: EN 了 links 終了 on lines 28 and 33 (relative form `../words/終了.md`, same as RU), and EN 感覚 links 間隔 once (`間隔.md`). No other 終了 or 間隔 mention remains plain in those files. Both glosses («окончание; прекращение», «промежуток, интервал») do not mislead against the new titles.
- Plain mentions left plain: EN-unlinked 襖, 距離, 隔たる, エッセイ, 所属する, 差し支える, バス停, 開業, 再開, 近畿, 東日本 have no RU file, so they are not defects. Two mentions have an RU file and are left plain as in EN: 社会 in 学会 (the sentence compares «общество» with 社会（しゃかい）) and 開始 in 終了 (antonym line). I do not call these defects (EN leaves them plain; the rule is "at substantive introduction/comparison"), but see Optional.
- Manifest: SHA-256 recomputation matches the working tree for all 30 new files, `kanji/了.md` and `words/感覚.md` (and every non-strokes entry). The only mismatches are the `strokes/*.json` entries; they are CRLF artefacts of this machine's `core.autocrlf=true` checkout (the candidate does not touch `strokes/`), not a stale manifest. `contentVersion` changed once; no generated or unrelated files in the diff. Intake record: 32 payload paths = the 30 words + `kanji/了.md` + `words/感覚.md`, all present in the content diff, `held: []`, no learner content.

Quiz safety: classification of every exclusion beyond EN (dictionary basis from Jisho/JMdict; necessity)
1. 障子→雨戸: basis 雨戸 "sliding storm shutter", 障子 "shoji (paper sliding door)"; both are sliding closures of an opening. Necessity NOT established: the Russian titles separate them («бумажная раздвижная перегородка» vs «наружная раздвижная защитная ставня»; only «раздвижная» is shared). Conservative, effectively over-guarding but harmless (it removes one distractor). Not a defect.
2. 険しい→困難: basis 険しい sense "difficult/dangerous prospects" (the card teaches 険しい道のり «трудный путь»; Daijisen), 困難 "difficulty; hardship". Conservative with a real basis; keep (consistent with EN's 険しい→難しい).
3. 険しい→大変: basis 大変 sense 4 "difficult; hard; challenging" vs 険しい "difficult" sense; shared «трудный». Conservative with a real basis; keep.
4. 締め切り→締め切る: basis 締め切る "to close (applications)" vs 締め切り "closing; deadline"; both titles contain «приём (заявок)». Required in practice (a learner cannot separate noun and verb of one stem by the shared label). Keep.
5. 終了→卒業: basis 卒業 sense 1 "graduation; completion (of a course)" vs 終了 «окончание (мероприятия, процесса)»; shared «окончание». Conservative with a real basis (a course is a process); keep.
6. 関わる→関連: basis 関連 "relation; connection; relevance" (suru verb, "be related") vs 関わる "have to do with"; sibling 関係 is already an EN guard. Required in practice; keep.
7. 関わる→扱う: basis 扱う sense 2/5 "to deal with (a problem); to cover (a topic)" vs 関わる; shared «иметь…». Conservative; necessity not established (different senses: handle vs be involved); keep, harmless.
8. 開通→繋ぐ: basis 繋ぐ sense 1 "to connect" and sense 4 "to put a person through (phone)" vs 開通 «подключение (линии связи)»; shared «подключ-». Conservative with a real basis; keep.
None is unjustified in the sense of guarding an antonym/contrast the article teaches.

Declined-pair judgments (all acceptable; no guard needed): 開会–開通, 開会–閉会 (antonym pair), 関西–関東 (contrast), 防止–警備, 期限–締め切る, 属する–関わる, 集会–開会, 閉会–締め切る (the titles name different objects/actions). The author's declined list: 開会–会議, 閉会–会合/議会/閉まる/閉める, 締め切る–中止/止む (different part of speech or sense), 締め切り–受付 «приём; стойка регистрации», 締め切り–卒業, 防止–警告, 防犯–犯罪/犯人 (the topic of prevention, not a synonym), 関わる–付き合い/交際/態度, 間隔–離す/離れる (noun vs verb), 隔てる–立つ, 険しい–表情, 限度–以内/越える/内/可, 期限–有効, 差し支え–困る, 学会–論文/社会, 集合–数学, 障子–紙屑, 附属–機関, ストップ–通行, 開通–交通, 警備–消防: no defensible-answer collision found; declining each is acceptable. 属する–団体/集団/グループ (shared «группа»): a verb vs a group noun, not defensible. 隔てる–間 «промежуток; между» has no guard in EN either; verb vs noun, not required (see Optional).
- Title uniqueness: no new title equals or nearly duplicates another RU word title or segment (title screen showed no segment overlap without a guard); the in-batch groups (学会/集会/集合, 間隔/隙間, 期限/限度/締め切り/締め切る, 属する/附属, 差し支え/妨げる, 終了/ストップ/閉会, 防止/警備/防犯, 関西/関東, 開通/開会/開放) stay visibly distinct.
- One-way in-batch declarations suffice (the app applies each pair symmetrically): 集会→学会, 集合→集会, 集合→学会, 隙間→間隔, 限度→期限, 附属→属する, 妨げる→差し支え, 締め切り→期限, 締め切り→締め切る, 終了→締め切り, 終了→締め切る, ストップ→終了, 防止→妨げる, 防止→ストップ, 防犯→防止, 防犯→警備, 開放→開会, 開放→開通, 閉会→終了. No EN guard was dropped.

Optional:
- O1 (low value): 学会 line "как 社会（しゃかい）" and 終了 line "開始（かいし）— «начало»" could link to the existing `社会.md` and `開始.md` (both exist), since each is a comparison pointer; EN leaves both plain, so this is parity-neutral either way.
- O2 (low confidence): 隔てる–間 («стоять между» vs «между») and 差し支え–困る/困難 («затруднение» vs «быть в затруднении»/«трудность») share a Russian root or word, but the parts of speech and senses differ; I do not require guards.
- O3: 障子→雨戸 could be dropped without loss (see classification 1); keeping it is harmless.

Limits: Dictionary evidence for classification came from the JMdict entries cited in the cards and the Jisho API (senses listed above); I did not open Daijisen/Weblio pages, so 険しい's "difficult prospects" sense rests on the card's own citation and Jisho's glosses. Quiz-defensibility judgments are Russian-usage judgments about displayed titles and cannot be verified against the app's actual distractor selection or whether it shows part of speech. I did not review the Japanese linguistics, translation accuracy or comprehensibility of the cards (other facets). I did not read the app source (`Words.kt`); I relied on the exclusion contract as described in the brief. `strokes/*.json` manifest mismatches are a local CRLF artefact, not verified against a clean LF checkout.

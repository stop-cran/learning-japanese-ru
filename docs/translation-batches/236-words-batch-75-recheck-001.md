# Batch 236 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `122b0192996f8c54236941b802ee5b10a19d06fd` | `1fcb849e038d197467585c2ee4f298c482a359c5` | Initial review snapshot: the signed candidate, on `origin/full-ru-236-words-75`. |
| `8b5e2b3368a2ac727bb817c3e19076becadc6cc5` | `2f63467a88dbc554586992bb04a68b4899d3d67b` | Fix 1 (final candidate). It covers correctness C236-01–03 (C236-03 merged with comprehensibility C6), consistency F3 (adopted as a conservative guard), comprehensibility C1, C4, C5, C7, C8 and C11 (C1 and C5 with adapted wording; C11 for the example only), C2 and C3 partially, and the comprehensibility optional on 論ずる's サ変. It adds three exclusions (話し中→話し合い, 恐縮→迷惑 and 請う→招待) and removes none; it adds and removes no link. Signed; on `origin/full-ru-236-words-75`. |

Fix 1 changed twelve word files and regenerated `manifest.json` (`contentVersion` `aaeab9f0acd5f959`, 5,199 entries:
5,194 `files` + 3 images + 2 scenes; the candidate had `665aa4623102be73`). The intake was not refreshed; it still records
the candidate's 36 payload hashes.
- `誓う` (lines 41–43; correctness C236-01): «誓う означает именно давать клятву или обет, а не браниться или проклинать.»
  instead of «Русское «клясться» в разговорной речи может означать и «браниться, проклинать». Это не то значение клятвы,
  которому учит 誓う.». The replaced sentences carried EN :46's English "swear" polysemy over to Russian, where cursing
  belongs to the non-reflexive «клясть»; the Japanese point (誓う is not cursing) stays, and the following sentence about
  broken vows is unchanged apart from reflow.
- `請う` (lines 4 and 12; correctness C236-02): title and H1 «просить, умолять; приглашать» instead of «просить,
  испрашивать (наставления, прощения)», the counterpart of EN :4 "beg; request; invite". It restores the "invite" sense,
  which the body teaches at :16, :29, :37 and :42, and drops the bookish «испрашивать» and the two-object qualifier;
  «испрашивать» remains a body gloss at :16.
- `請う` (line 9; coordinator, after the post-fix screen): 招待 appended to `quiz_exclusions` (now 15 entries). The new
  segment «приглашать» has a stem lead to 招待 «приглашение»; the coordinator first decided on no exclusion and reversed
  that after the screen, following the RU-added 招待 guards on 招く and 誘う.
- `請う` (line 20; comprehensibility C11): «— Я обратился к учителю за наставлением.» instead of «— Я попросил учителя о
  наставлении.», conveying the formal register noted at :47 (EN :20 "I asked the teacher for instruction"). The proposed
  gloss for «испрашивать» at :16 was not used.
- `話し合い` (line 19; correctness C236-03 merged with comprehensibility C6): «— Завтра у нас будет семейное обсуждение.»
  instead of «— Завтра мы всей семьёй всё обсудим.»: no added «всё», no other object, and the noun frame of
  話し合いをします, as EN :19 "We will have a family discussion tomorrow." Neither reviewer's proposed wording was used.
- `話し中` (line 9; consistency F3): 話し合い appended to `quiz_exclusions` (now [忙しい, 会話, 話, 話し合い]), a
  conservative guard: 話し中's segment «идёт разговор» could describe a 話し合い in progress, and 話し中 already guards 会話
  and 話 for bare «разговор».
- `講師` (line 21; comprehensibility C1, adapted wording): «— Она работает лектором в университете.» instead of «— Она
  преподаватель в университете.»: «преподаватель» is the first word of 教師's title; EN :21 "She is a university
  lecturer". The proposed «Она лектор в университете.» was not used; «работает» avoids the bare copula.
- `有難い` (lines 21 and 23–25; comprehensibility C2, partially adopted): line 21 «… — это то, что я ценю.» instead of «… —
  это то, за что я очень признателен.» (EN :21 "something I appreciate"), and the note now reads «Русское «благодарный»
  обычно описывает того, кто чувствует благодарность, поэтому так звучит перевод первого примера. Сами японские примеры
  оценивают помощь как желанную и выражают признательность говорящего.» instead of «… чувствует благодарность. Японские
  примеры оценивают саму помощь как желанную …» (EN :23–24). Line 20 «Я благодарен, что вы мне помогли.» is kept: EN :20
  "I am grateful for your help" is also person-framed.
- `恐縮` (lines 4 and 12; comprehensibility C3, partially adopted): title and H1 «чувство неловкой признательности;
  смущение (от любезности, похвалы, доставленных хлопот)» instead of «… смущение (от чужой любезности или похвалы)», so the
  qualifier covers trouble caused, as line 16 («доставил человеку хлопоты») and EN :4 "feeling obliged; apologetic
  gratitude". The proposed «беспокойства» was not used: it is ambiguous with one's own worry (心配). Line 22 «Я очень
  признателен за ваше любезное письмо.» is kept (EN :19).
- `恐縮` (line 9; coordinator): 迷惑 «неудобство (для других); хлопоты» appended to `quiz_exclusions` (now 12 entries), an
  RU-added conservative guard because the qualifier now names «хлопоты».
- `謙虚` (line 21; comprehensibility C4): «— Я скромно принимаю совет учителя.» instead of «— Я со смирением принимаю совет
  учителя.» (EN :20 "I accept the teacher's advice with humility").
- `謙遜` (line 20; comprehensibility C5, adapted wording): «— Даже когда его хвалят, он скромно отзывается о своих
  заслугах.» instead of «— Даже когда его хвалят, он скромничает.», matching line 16 (modest words about one's
  achievements); EN :21 "He remains modest even when praised". The proposed «он принижает свои заслуги» was not used. Line
  21 «Не нужно так скромничать» is kept.
- `争う` (line 19; comprehensibility C7): «— Две команды соперничают за победу в чемпионате.» instead of «— Две команды
  борются за победу в чемпионате.»: «бороться» is in 戦う's title; EN :20 "Two teams are competing for the championship".
- `言い出す` (line 19; comprehensibility C8): «— Он вдруг заговорил о том, что хочет домой.» instead of «— Он вдруг
  заявил, что хочет домой.», keeping the onset (EN :19 "He suddenly started saying that he wanted to go home").
- `論ずる` (line 42, now lines 42–43; comprehensibility optional): «традиционные японские словари относят его к спряжению
  サ変（さへん）— неправильному спряжению по образцу する.» instead of «… описывают его как глагол спряжения サ変.» (EN :47
  "traditional Japanese dictionaries describe it under サ変"; Daijisen labels 論ずる 動サ変).

The correctness reviewer raised no optional note. The consistency reviewer's F1 (貝's dropped トップ/頂上 sentences) and
F2 (謎謎→不思議) were not adopted, nor was its optional note on long titles. The comprehensibility reviewer's C9 («исходный
список» in learner prose), C10 (N2-status text in 請う and 削る) and C12 (the predicate-like 話し中 title) were not adopted,
nor were its proposed gloss for «испрашивать», the remainder of C2 (line 20) and C3 (line 22), or its optional notes on
誓う «друг другу», 謎謎 «пазл» and 調整 «наладка». The dispositions gave the reasons (see the reconciliation table).

The coordinator's post-fix title screen of the two changed titles (`b236-postfix-screen.txt`; pool: the RU primary word
cards plus the Batch 237 lane words; parentheses stripped) found both H1s equal to their titles. 請う shares exact segments
only with guarded cards: «просить» with 頼む, 願う and 求める, «умолять» with 拝む and «приглашать» with 招く and 誘う, all EN
exclusions on 請う; its stem leads are 招待 «приглашение» (guarded by fix 1) and 詫びる «приносить извинения; просить
прощения (за проступок)», a Batch 237 lane word not in the published pool, which shares only the «проси» stem and is
unguarded. 恐縮 changed only inside its parenthetical, so its screened segments are unchanged; its stem leads are 恥ずかしい
and 感謝 (guarded) and 不安, 兆候, 思う, 愛情, 感じる, 感情, 感覚, 承認, 気持ち, 特徴 and 認める (unguarded; shared «чувст» or
«призн» stems only). The screen's note records that parenthetical stems are not screened, that 迷惑 is now guarded, and that
手間, 面倒 and 苦労 carry «хлопоты» only as a generic segment and stay as distractors. 厄介 «хлопотный; обуза; попечение»,
which the screen note and the consistency recheck also name, shares only the «хлопо» stem, with no exact segment, and also stays a distractor. Fix 1 adds no link and removes none. The four RU-only
links at the candidate, 謙虚:32 → 謙遜, 胡椒:32 → 塩, 削除:33 → 追加 and 詰まる:38 → 込む, are unchanged. The dispositions
record `tools/validate.py` 0 errors, the unit tests (124) OK, the content budget OK and a 5,199-entry manifest in the
post-fix state.

Net change from the candidate:
- titles and H1s of 請う and 恐縮;
- example translations in 講師, 有難い, 謙虚, 謙遜, 話し合い, 争う, 言い出す and 請う;
- prose in 誓う (lines 41–43), 有難い (lines 23–25) and 論ずる (line 42);
- three appended exclusions (話し中→話し合い, 恐縮→迷惑 and 請う→招待); no link change.

No Japanese example sentence, sourced reading, navigation file or kanji card changed. The content diff
`122b019..8b5e2b3 -- words` is twelve word files, 23 lines added and 21 removed; with `manifest.json` the commit changes
13 files, 36 lines added and 34 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs; the
correctness and comprehensibility reports state that the model is not independently verifiable in the session, and the
consistency report makes no statement about its model.

The rechecks ran serially, one reviewer at a time, in one round on fix 1: correctness, then consistency, then
comprehensibility. No recheck raised a new finding, so there was no fix 2.

Each reviewer appended its recheck to its own report file. The correctness section records that the supplied word diff
equals the actual Git diff and that it read all twelve revised RU cards in full, comparing every changed passage against
the candidate and the previously read frozen EN, with the original review covering the 18 unchanged cards; the
consistency section records its regression checks of titles, exclusions, links and manifest hashes against the
working tree at `8b5e2b3`; the comprehensibility section records that it read the changed passages at that commit and
reconciles each of its findings. The recheck sections do not reproduce the briefs, so this record does not claim their
contents.

All three rechecks state that no generator was run. The consistency reviewer ran `tools/validate.py` (0 errors); the
correctness reviewer states that no generator or validator was run and no repository was written, and the
comprehensibility reviewer records no validator run. The correctness section records snapshot `8b5e2b3` with HEAD
verified and a clean working tree, the consistency section `8b5e2b3` with an empty `git status --porcelain`, and the
comprehensibility section `8b5e2b3` with an empty status. The recheck records include no separate coordinator status
check after the rechecks; when these records were drafted, a read-only check showed the RU checkout on
`full-ru-236-words-75` at HEAD `8b5e2b3368a2ac727bb817c3e19076becadc6cc5` with `git status --porcelain --ignored` printing
nothing.

### Round 1 (`8b5e2b3`)

| Facet | Scope and result |
|---|---|
| Correctness | Snapshot `8b5e2b3`, HEAD verified, working tree clean; the supplied word diff equals the actual Git diff. Read all twelve revised RU cards in full (争う, 恐縮, 有難い, 言い出す, 話し中, 話し合い, 誓う, 請う, 論ずる, 謙虚, 謙遜 and 講師) and compared every changed passage against the candidate and the frozen EN. C236-01 is **resolved**: 誓う:41 removes the false Russian polysemy claim while retaining the oath/cursing distinction and the broken-vow qualification. C236-02 is **resolved**: 請う:4/12 restore inviting alongside asking and begging. C236-03 is **resolved**: 話し合い:19 removes the exhaustive "everything", and the family-discussion rendering preserves the Japanese and EN sense. The other rewrites are at least as accurate in their teaching contexts: 講師:21, 争う:19, 言い出す:19, 謙虚:21, 請う:20 and 有難い:21/23–25; 恐縮's expanded nominal title accurately includes discomfort over trouble caused; 謙遜:20 is an acceptable, narrower contextual rendering, with the broader body definition and the retained :21 intact. The 論ずる サ変 gloss is supported by Daijisen on Weblio (論ずる labelled 動サ変; サ行変格活用 includes voiced -ずる compounds). Japanese bullet text, readings and links are unchanged in all twelve files; the added guard targets 招待 and 迷惑 exist, and the 話し中–話し合い guard adds no false semantic claim. No generator or validator was run. Correctness **CLEAN** and scoped coverage **CLEAN**; no new actionable regression. |
| Consistency | Snapshot `8b5e2b3`, empty `git status --porcelain`; read-only; only `tools/validate.py` run (0 errors), no generator. F1 is **partially resolved**, kept as an acknowledged nonblocking limit (residual: the two existing targets are no longer linked from 貝); F2 is **withdrawn** (the shared «загад-» stem makes the guard defensible); F3 is **resolved**; the long-title note is **withdrawn** (恐縮's title is now 87 characters, within the existing range); the strokes-hash limit is unchanged, pre-existing and out of scope. Changed titles: 請う and 恐縮, title equal to H1; no other title changed. Exclusions: 請う 15 entries ending with 招待, 恐縮 12 entries ending with 迷惑, 話し中 [忙しい, 会話, 話, 話し合い]; no duplicate or self-reference; every target exists as an RU card; all EN guards remain. Quiz ambiguity: 請う «приглашать» covered by 招く/誘う and the now-guarded 招待; the unguarded stem lead 詫びる ("a Batch 237 draft, not in the primary pool, with no exact segment") acceptable; 恐縮 «хлопоты» guarded by 迷惑, with 手間/面倒/苦労/厄介 sharing only a generic segment, acceptable (coordinator note: 厄介 «хлопотный» shares only the stem). The diff adds or removes no link; the RU-only links remain the same four. Every `words/` and `kanji/` manifest sha256 matches the working tree; the commit changes 12 word cards plus the manifest only. Consistency **CLEAN** (F1 as an acknowledged limit), quiz safety **CLEAN**, and navigation restorations, manifest and intake path set **CLEAN**. |
| Comprehensibility | Snapshot `8b5e2b3`, empty status; read the changed passages at that commit, not all 30 cards. C1, C4, C6, C7 and C8 are **resolved**; C5 is **resolved (adapted)**; C2 and C3 are **partially resolved, remainder withdrawn** (EN is also person-framed at 有難い:20; 恐縮's title covers 恐縮ですが without the ambiguous «беспокойства», and line 22 matches EN); C11 is **resolved for the example, gloss withdrawn**; C9, C10 and C12 are **withdrawn** (EN-parallel, published RU precedent, on the follow-up list). The 論ずる サ変 optional is **resolved**; the 誓う, 謎謎 and 調整 optionals are **withdrawn**; the 貝 トップ/頂上 limit stands without being maintained. No regression: 誓う:41 keeps the not-cursing point without a claim about Russian; 請う's title restores the invite sense, with exact overlaps guarded; the 話し合い and 講師 adaptations add neither a false object nor another card's title. Comprehensibility **CLEAN** and scoped coverage **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C236-01: 誓う:41–42 claims colloquial «клясться» means «браниться, проклинать» (medium) | **Resolved** | `誓う.md:41–43`; Kuznetsov on gramota.ru (клясться); gufo.me (клясть); EN :46; JMdict 1381210 sense 1. |
| Correctness C236-02: 請う's title drops the "invite" sense and narrows to two objects (medium, scoped coverage) | **Resolved** | `請う.md:4,12`; EN :4 "beg; request; invite"; JMdict 1592920 sense 1. |
| Correctness C236-03: 話し合い:19 adds «всё» (low) | **Resolved** (merged with comprehensibility C6; coordinator wording) | `話し合い.md:19`; EN :19 "We will have a family discussion tomorrow"; JMdict 1600910 sense 1. |
| Consistency F1: 貝 drops EN's two sentences linking トップ and 頂上 (low-medium) | **Partially resolved** at recheck; declined and kept as an acknowledged nonblocking limit | English-label safeguard with no Russian counterpart («волчок» vs «верх; лидирующая позиция» / «вершина»); the Japanese facts, both EN exclusions and the footer JMdict IDs 1085030/1430220 stay; quiz_exclusions are not learner-visible; the correctness reviewer judged the omission permitted and the comprehensibility reviewer did not uphold it; the general question is on the issue #7 follow-up list. |
| Consistency F2: 謎謎→不思議 is an unnecessary over-guard (low, nonblocking) | **Withdrawn** at recheck; guard kept as conservative | The Russian titles share the «загад-» stem (загадка/загадочный); 不思議 already declares 謎. |
| Consistency F3 (optional): 話し合い–話し中 both carry «разговор», unguarded | **Resolved** (adopted as a conservative guard) | `話し中.md:9`; 話し中 already guards 会話 and 話 for bare «разговор». |
| Consistency optional: long titles (論ずる 77, 恐縮 76 characters) | **Withdrawn** at recheck | No length rule; within the existing range (パス 84); 恐縮 is now 87 characters. |
| Consistency limit: 118 strokes manifest hashes differ from the working tree | **Not a defect**; no action; pre-existing, out of scope, unchanged at recheck | `tools/build_manifest.py:19` hashes text files after CRLF→LF normalization; no strokes file changed in this batch. |
| Comprehensibility C1: 講師:21 uses 教師's title word «преподаватель» (high) | **Resolved** (adapted wording) | `講師.md:21`; 教師's title; EN :21 "university lecturer". |
| Comprehensibility C2: 有難い:20–21 use the person frame the note rejects (high) | **Partially resolved**; remainder withdrawn at recheck | `有難い.md:21,23–25`; line 20 kept as EN :20 "I am grateful for your help"; EN :21 "something I appreciate". |
| Comprehensibility C3: 恐縮's qualifier drops 恐縮ですが; :22 is plain gratitude (medium) | **Partially resolved**; remainder withdrawn at recheck | `恐縮.md:4,12`; line 16; EN :4 "feeling obliged; apologetic gratitude"; :22 kept as EN :19; «беспокойства» ambiguous with 心配. |
| Comprehensibility C4: 謙虚:21 «со смирением» (medium) | **Resolved** | `謙虚.md:21`; Ozhegov (смирение); EN :20 "with humility". |
| Comprehensibility C5: 謙遜:20 «скромничает» suggests excess or irony (medium) | **Resolved** (adapted wording) | `謙遜.md:20`; line 16; Ozhegov and Ushakov (скромничать); EN :21 "remains modest". |
| Comprehensibility C6: 話し合い:19 verbalises the noun and adds «всё» (medium) | **Resolved** (merged with correctness C236-03) | `話し合い.md:19`; EN :19. |
| Comprehensibility C7: 争う:19 «борются» is 戦う's title word (medium) | **Resolved** | `争う.md:19`; 戦う's title; EN :20 "competing". |
| Comprehensibility C8: 言い出す:19 «заявил» loses the onset (medium) | **Resolved** | `言い出す.md:19`; JMdict 1264080 senses 1–2; JapanDict; EN :19 "started saying". |
| Comprehensibility C9: «исходный список» in 圧縮:41, 削除:38, 縮める:44 and 削る:43 (medium) | **Withdrawn** at recheck; declined | All four mirror EN sentences (EN 圧縮:41, 削除:38, 縮める:49–50, 削る:44); an established RU convention (coordinator recount: 31 occurrences in 30 published word cards at `8b5e2b3`, one wrapping across a line break; the dispositions' «30» counted cards, the reviewer's «31» occurrences); on the issue #7 follow-up list. |
| Comprehensibility C10: N2-status text in 請う:42 and 削る:25 (low) | **Withdrawn** at recheck; declined | EN parity (請う:46–48, 削る:25); published RU precedent (引き出す and others); on the issue #7 follow-up list. |
| Comprehensibility C11: 請う:20 copies 頼む:20's frame; gloss «испрашивать» at :16 (medium) | **Resolved** for the example; gloss **withdrawn** at recheck | `請う.md:20`; line 47; the fixed title no longer uses «испрашивать», which stays a body gloss. |
| Comprehensibility C12: 話し中's title is non-nominal (medium) | **Withdrawn** at recheck; declined | EN "busy on the phone; in conversation" is also predicate-like; the title describes 話し中です «занято». |
| Comprehensibility optional: 論ずる:42 unexplained サ変 | **Resolved** (adopted) | `論ずる.md:42–43`; Daijisen 動サ変; EN :47. |
| Comprehensibility optionals: 誓う:21 «друг другу», 謎謎:38 «пазл» and 調整 «наладка» | **Withdrawn** at recheck; declined | Natural Russian and EN-consistent (EN 謎謎 also contrasts jigsaw puzzles; EN 調整 has "tuning"). |

Cross-batch note: links to absent targets stay plain. Seven EN link targets in this batch's new cards (7 occurrences) are
absent from RU, all kanji cards: 貝 (from 貝), 講 (from 講師), 課 and 税 (from 課税), 省 and 略 (from 省略) and 詰 (from
詰まる). The other written kanji without an RU kanji card, 削, 整, 椒, 節, 縮, 胡, 虚, 誓, 請, 謎, 謙 and 遜, have none in EN
either. No link target in the new cards is an absent word card. No links were held from Batch 235, and none is held from
this batch.

## Final exclusion set

All 151 EN exclusion entries (29 lists; 胡椒 has none in EN) are retained in EN order; 23 of them lie inside the batch,
and the other 128 target existing RU cards. Seventeen direct, one-sided entries are added on ten new cards, all appended
to existing lists: fourteen on eight cards from the authoring lane, at the candidate, which the coordinator accepted as
reported, and three from fix 1 (話し中→話し合い, consistency F3; 恐縮→迷惑 and 請う→招待, coordinator). The author and the
coordinator classed 話しかける→扱う and 縮む→座る as required and the other twelve lane entries as conservative; the fix-1
entries are conservative. The consistency reviewer classed the lane entries as follows:

- Required (5): 縮む→座る, 話しかける→扱う, 論ずる→検討, 論ずる→考慮 and 言い出す→勧める.
- Conservative/acceptable (8): 論ずる→取り上げる, 有難い→御礼/礼/ありがとう, 縮む→乗る, 詰まる→密 and 話し中→会話/話.
- Unnecessary (1): 謎謎→不思議 (F2), withdrawn at recheck; the guard stays.

At recheck it confirmed the three fix-1 entries as stated and judged 請う's «приглашать» covered and 恐縮's «хлопоты»
guarded. Every RU addition is appended at the end of its list; nothing is removed or reordered. Android applies each
declaration symmetrically, so no reverse declarations were added to baseline cards. 詫びる, a Batch 237 lane word sharing
only a stem with 請う, is not guarded (judged acceptable at recheck).

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (誓う C236-01 and 話し合い C236-03).
- Scoped coverage: **CLEAN** after fix 1 (請う C236-02); comprehensibility review scoped coverage **CLEAN** throughout.
- Comprehensibility: **CLEAN** after fix 1 (講師, 有難い, 恐縮, 謙虚, 謙遜, 話し合い, 争う, 言い出す, 請う and 論ずる); the
  remainders of C2 and C3 and the declined C9, C10 and C12 were withdrawn at recheck.
- Cross-file consistency: **CLEAN** after recheck; F1 (貝's dropped トップ/頂上 sentences) stands as an acknowledged
  nonblocking limit; the four RU-only links (謙虚:32 → 謙遜, 胡椒:32 → 塩, 削除:33 → 追加 and 詰まる:38 → 込む) and the
  eight restored navigation links in six files stand.
- Quiz safety: **CLEAN** throughout, including the 請う and 恐縮 retitles. This covers the reviewed batch and the directly
  adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed cards or passages and the lines needed to judge them; the comprehensibility
  recheck did not re-open JMdict or rerun the title screen. The unchanged cards rest on review 001, in which all three
  reviewers read all 30 cards in full (the consistency reviewer compared the EN originals mechanically and by eye).
- The correctness recheck reused previously verified dictionary evidence, adding Daijisen on Weblio for 論ずる and 謙遜; it
  ran no validator or unit tests, and its original dictionary-version, whole-pool, app and native-acceptance limits remain.
  The consistency reviewer performed no dictionary re-verification, and its necessity classes are judgements, not
  measurements. The comprehensibility review did not review the kanji diffs or the intake JSON.
- 貝 no longer links its two existing comparison targets トップ and 頂上 (consistency F1 residual).
- The two counts for «исходный список» (30 in the dispositions, 31 in the comprehensibility recheck) are reconciled by a
  coordinator recount: 31 occurrences in 30 published word cards at `8b5e2b3`, one wrapping across a line break. The phrase also occurs in kanji cards and docs, which neither count covers.
- The intake was not refreshed by fix 1, so its payload hashes describe the candidate `122b019`, not `8b5e2b3`.
- Frequency and preferred register (for example «испрашивать», «лектор», «скромно отзывается») were not certified.
  Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.

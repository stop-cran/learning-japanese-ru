# Batch 216 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `034ab7ea9034db0f24f7d8dfdad1f16af819e788` | `ca36d09f0ff3b18b6aa66d1ac4e8f2fbcf82f41c` | Initial review snapshot: the signed candidate, pushed before review. |
| `bf04fff22db1ce1e14850430595393264272541a` | `db0cc60e3e9b5819cc1b41f32b557a2331cb7473` | Fix (final candidate). It covers the two consistency findings, the four comprehensibility findings and the intake refresh. It was signed and pushed before the rechecks. |

The fix changed seven word files and regenerated `manifest.json` (`contentVersion` `0b046c094704e327`, 4,599 entries) and the
intake:
- `切れる` (line 9): `quiz_exclusions: [折れる, 無くなる, 切る, 破る, 終わる]` (consistency F1).
  - 切れる's «кончаться (о запасе)» is a near-synonym of 終わる «заканчиваться; заканчивать». The published 切る and 無くなる
    already exclude 終わる.
  - The coordinator's title screen after the edit found no exact segment overlap. The stem hits are guarded (切る, 破る) or
    false friends, such as хорош- in いい, 良い and よく, запас- in 余裕 and 非常口, and рвать in びりびり.
- `劇` (line 9): `quiz_exclusions: [芝居, 公演]`; 劇場 removed (consistency F2).
  - «театральная постановка; драма» and «театр (здание)» share no segment; the screen reports only the stem «театр».
  - The card itself glosses 劇場 at line 30, and EN 劇 has no exclusions. 劇場 has none of its own, so the pair is now
    unguarded on both sides.
- `分` (lines 4, 12): title and H1 «дробная единица; чья-либо часть» instead of «бу (дробная единица); чья-либо часть»
  (comprehensibility 1).
  - The title no longer opens with a Cyrillic transliteration of the reading ぶ. It now matches EN "fractional unit; portion".
  - The screen found no exact segment overlap. The stems «часть» (部分, already excluded, and broader titles such as 大部分)
    and «единица» (単位, メートル, 単語) were already in the old title.
- `助手` (lines 37–39): a new sentence contrasts 助手 with 手伝い, whose title «помощь; помощник» shares
  «помощник» (comprehensibility 2, with the author's wording). It says that 手伝い can name a helper but is first of all the
  help itself, for example with a house move, while 助手 names only the person who assists another in work, or such a post,
  for example under a professor.
  - Digital Daijisen via Weblio: 手伝い 「手伝うこと。また、その人。」; 助手 sense 1 「仕事の手助けをする人。」 and sense 2, a
    university post assisting professors, 「また、その人」.
  - The reviewer's proposed «не обязательно постоянная роль» was not used, because neither dictionary states it.
  - JMdict 1328170 orders 手伝い as (1) helper; assistant, (2) help; assistance. «прежде всего» follows Daijisen's order, not
    JMdict's. 助手 already excludes 手伝い.
- `到着` (line 21) and `前者` (line 18): 電車 is glossed «электропоезд», the published 電車 title, instead of «электричка»,
  which in ordinary Russian is a suburban train (comprehensibility 3). In 前者, «первый» now agrees with «электропоезд».
- `刈る` (lines 36–37): the haircut sentence now reads «[髪](髪.md)を切る（かみをきる）— обычное «подстричь волосы». Это
  выражение не изображает стрижку как срезание отросшего, подобное скашиванию травы; так её представляет 刈る.»
  (comprehensibility 4, with the author's wording).
  - Digital Daijisen via Weblio, 刈る sense 1: 「伸び茂っているものを根元を残して切り払ったり、切り取ったりする。「草を刈る」
    「髪を刈る」」. Hair cutting is therefore inside 刈る's mowing sense; the contrast is framing, not a ban on 髪を切る.
  - The proposed «в отличие от 短く刈る» was not used, because it would introduce a collocation the card does not teach.
- The intake note now names the fixed cards, and the seven candidate hashes were refreshed.

Net change from the candidate: one exclusion added (切れる→終わる), one removed (劇→劇場), one retitle (分), one added
contrast sentence (助手), two wording fixes (到着, 前者) and one rewritten contrast sentence (刈る). No Japanese example,
reading, EN exclusion or link target changed; the only new link is 助手's to the existing 手伝い card, which 助手 already
excluded.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, in the order correctness, consistency, comprehensibility. Each reviewer appended to its own report
file, which stayed in its session context. Each recheck message gave it:
- the fix commit, its parent and the read-only rules;
- the actual content diff from `034ab7e` to `bf04fff` inline;
- the coordinator's evidence for every change;
- the declined comprehensibility optional items with their reasons, without the other reviewers' reports;
- the recorded «электричка» limit;
- the coordinator's disposition of each of its own findings.

All rechecks reviewed the final candidate `bf04fff`; no second fix was needed. The recheck messages forbade running
`tools/build_manifest.py` or any other generator, and all three recheck sections state that none was run.

The consistency and comprehensibility reviewers ran `tools/validate.py` with `-B` (0 errors); the correctness recheck reports
no validator run. The comprehensibility reviewer also started one validator call by mistake in a separate local checkout of
the EN repository. That run reported 0 errors and changed nothing there; the cache directory and the unrelated modified file
it saw in that checkout predate the recheck. No cache directory appeared in the RU checkout. After every recheck the
coordinator confirmed that HEAD was unchanged and that `git status --porcelain --ignored` was empty.

### Round 1 (`bf04fff`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer compared the actual words diff against `034ab7e` and read all seven revised cards in full. For 助手 it inspected Digital Daijisen 手伝い (「手伝うこと。また、その人」, including help with a house move) and 助手 senses 1–2 afresh, and JMdict, which lists both 手伝い senses in the reverse order. The added contrast keeps both senses and introduces no permanent/temporary-role rule; «прежде всего» is acceptable as an explanatory starting point following Daijisen, not a frequency claim. For 刈る, Daijisen sense 1 groups 草 and 髪 under cutting grown material while leaving its base; the contrast concerns framing, neither banning 髪を切る nor claiming that 刈る alone specifies a short result. 分 loses neither reading nor sense, and the body still separates ぶ from ぶん and keeps 私の分 and 二日分. JMdict 電車 supports "electric train", Gramota confirms «электропоезд» as a masculine noun, and «первый» agrees. The 切れる and 劇 changes remove no sense, example or contrast, and the work/building distinction for 劇 and 劇場 remains explicit. Correctness and scoped coverage are **CLEAN**, with no findings or optional suggestions. |
| Consistency | The reviewer confirmed that the commit changes only the seven word cards, the manifest and the intake. F1 is resolved: 切れる excludes 終わる, which exists. F2 is resolved: 劇 keeps 芝居 and 公演, and the unguarded 劇/劇場 pair is acceptable because the titles share no segment, the card glosses 劇場 itself and EN has no exclusions for 劇. All seven front matters are valid. 分's new title has no exact match elsewhere; its stem overlaps existed before, and dropping «бу» adds none. 助手's link to 手伝い resolves, its reading is correct, and the pair is already guarded. The 刈る, 到着 and 前者 edits are prose-only. The manifest rebuilt in memory equals the committed one (`0b046c094704e327`), and the SHA-256 of each changed file appears in the intake. It judged the «электричка» limit acceptable as out of scope: a pre-existing wording inconsistency, not a quiz or link defect, and 後者:17 is consistent in itself. Consistency, quiz safety and cross-file integration coverage are **CLEAN**, with no open findings. |
| Comprehensibility | The reviewer reread the seven changed cards and 後者:17, and no other author, reviewer or batch-record material. Finding 1 is resolved: 分's title and H1 «дробная единица; чья-либо часть» drop the Cyrillic «бу»; the heading still shows 分（ぶ）, and the body still separates ぶ from ぶん. Finding 2 is resolved: 助手:37–39 teaches the contrast. «прежде всего» follows Daijisen's act-then-person order and keeps the person sense, the sentence adds no unsourced claim, and «должность» does not contradict the card's later statement that the word fixes no single rank. Finding 3 is resolved: «Электропоезд прибыл в три часа» and «первый из них» agree and match the 電車 card. Finding 4 is resolved: 刈る:36–37 shows a beginner the framing, matches Daijisen sense 1 rather than stating a ban, and does not clash with the card's 髪を短く刈りました; «срезание отросшего» is slightly elliptical, but the grass image and the following 草を刈る make it clear. 切れる and 劇 changed only their exclusions, and 劇:24 still says that 劇 is the work, not the building. The declined optional items stay optional. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness | **No findings** | Review 001 reported none; the recheck found no regression. |
| Consistency F1: 切れる lacks a 終わる guard (minor) | **Resolved** | `切れる.md:9`; RU titles 切れる «кончаться (о запасе)» and 終わる «заканчиваться; заканчивать». Severity unchanged. |
| Consistency F2: 劇→劇場 is an unjustified over-guard (trivial) | **Resolved** | `劇.md:9`; the titles share no segment, and the card glosses 劇場 at line 30. Severity unchanged. |
| Comprehensibility 1: 分's title begins with the Cyrillic transliteration «бу» (minor) | **Resolved** | `分.md:4,12`; EN "fractional unit; portion". |
| Comprehensibility 2: 助手 has no contrast with 手伝い (minor) | **Resolved** | `助手.md:37–39`; Digital Daijisen 手伝い and 助手 senses 1–2. The author's wording was used instead of the proposed «не обязательно постоянная роль». |
| Comprehensibility 3: 到着 and 前者 render 電車 as «электричка» (minor) | **Resolved** | `到着.md:21`, `前者.md:18`; the published 電車 title; Gramota «электропоезд». |
| Comprehensibility 4: 刈る's haircut sentence is a calque with no contrast (minor) | **Resolved** | `刈る.md:36–37`; Digital Daijisen 刈る sense 1. The author's wording was used instead of the proposed «в отличие от 短く刈る». |
| Comprehensibility optional: 分野–地方, 前者 «два предложения», 割る «вылейте», 別に–あまり, 列車's 汽車 hedge | **Optional, not adopted** | 分野's «область (знаний, деятельности)» and its 畑 contrast block 地方's geographic sense; «предложение» is the ordinary Russian for a proposal; «вылить яйцо» is the natural collocation for a broken raw egg; the reviewer judged the last two non-actionable. |
| Recorded limit: «электричка» remains in published cards outside the new files | **No action** | 後者:17 (navigation-only here; «второй» agrees with «автобус»), うとうと, ぎゅうぎゅう, 大部分, 定期, 居眠り, 模様 and 譲る. The consistency recheck judged it acceptable as out of scope. |
| Exclusion classification | **Reviewer differs from author on 4 entries** | The author called 到着→着く, 別れ→別れる and 切れる→切る conservative; the consistency reviewer rated them required. The author called 劇→劇場 conservative; the reviewer classed it unjustified (F2), and the fix removed it. The reviewer's classification is recorded as final. |

Cross-batch note: links to absent targets stay plain. The next batch includes 出会い and 優れる and will restore the links to
them from 別れ and 劣る; no other link is held.

## Final exclusion set

All 13 EN exclusion entries (11 lists) are retained. Twenty-four direct, one-sided entries are added on 15 new cards:

- Required (12): 劣る→負ける, 加わる→加える, 劇→芝居, 割る→分ける, 到着→着く, 別れ→別れる, 別に→あまり, 別に→別,
  列→順番, 列→番, 切れる→切る, 分析→検査.
- Conservative (12): 勧める→推薦, 勧める→提案, 効く→効果, 劣る→譲る, 加わる→足す, 劇→公演, 制度→機関, 別に→特に,
  列車→汽車, 刑事→警官, 切れる→破る, 切れる→終わる.

切れる→終わる is classed conservative: the consistency reviewer raised it with medium-low confidence, noting that 終わる
normally cannot take a stock as its subject and that EN has no such guard.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** throughout.
- Scoped coverage: **CLEAN** throughout.
- Comprehensibility: **CLEAN** after the fixes (分, 助手, 到着, 前者, 刈る).
- Cross-file consistency: **CLEAN** after the fix (劇).
- Quiz safety: **CLEAN** after the fix (切れる→終わる). This covers the reviewed batch and the directly adjudicated pairs.
  Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the cards needed to judge them. The unchanged cards rest on review
  001's full reading.
- Dictionary sense order supports «прежде всего» in 助手 as an explanatory starting point, not as frequency evidence.
- «электричка» remains in published cards outside this batch's new files; normalising them would be a separate sweep.
- The consistency reviewer took the 助手/手伝い dictionary evidence from the brief without re-fetching it and did not rerun
  `word_title_screen.py`. The correctness reviewer ran no validator and audited neither the manifest nor the intake.
- The comprehensibility reviewer reread only the seven changed cards and 後者:17. It judged «срезание отросшего» in 刈る
  slightly elliptical but clear in context.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.

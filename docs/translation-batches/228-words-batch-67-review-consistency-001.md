# B228 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `e2b0bdba512f72ca587ad5d2cb553b0edb22016a` (tree `4b3cf06ecc0f1d128d13dbd4629a2239bfb59bd4`),
> the signed candidate pushed before review.
> Later reconciliation is in `228-words-batch-67-recheck-001.md`.

Snapshot: e2b0bdba512f72ca587ad5d2cb553b0edb22016a (`git rev-parse HEAD` matches; `git status --porcelain` empty; no uncommitted changes). Parent f833f88; EN frozen 6af98cb.

Scope: Facets: consistency, quiz safety, scoped cross-file integration. Read in full, front matter and body, against EN front matter/link sets and the cited EN lines: all 30 new cards (スケジュール 寸法 広さ 面積 インタビュー 面接 面倒くさい しーん 静まる 青白い 青少年 鈍い 蛍光灯 電球 直流 組み合わせ 交流 合同 合流 電流 電波 乾電池 電池 電柱 電力 採点 点数 零点 雑巾 打ち合わせ). Read the full diffs (`-U0`) of all ten navigation files and compared every mention of the target in EN vs RU (10/10). Checked manifest.json (all 4,836 non-stroke entries hashed against the working tree) and the intake path list. Ran `tools/validate.py` (0 errors), `word_title_screen.py` (191 stem-only lines, 0 whole-segment overlaps) and a separate keyword screen of all RU word titles. No generator was run. Reviewer model: not verifiable from inside the session.

Verdicts:
- Consistency: CLEAN (all 30 cards; all 10 navigation files; manifest; intake record).
- Quiz safety: CLEAN (all 30 cards). Both RU-introduced guards are kept as conservative; no missing required guard found.
- Scoped cross-file integration: CLEAN.

Findings: none (0 critical / 0 major / 0 minor).

Evidence for the CLEAN verdicts:
1. Front matter. `jlpt`, `type`, `kanji`, `tags`, `reading`, `word` equal EN on all 30 cards. `quiz_exclusions` equals EN on 28 cards. The only differences are the two RU additions, 採点 (+勘定) and 打ち合わせ (+話し合う). インタビュー, 直流 and 乾電池 have no key, as in EN. しーん omits `image`/`image_scene` (EN has them). RU has 3 `images` entries against EN's 120 and ざわざわ also has no image field, so omission is the established word-only adaptation. The RU format reference forbids creating media without exact bytes/hash/licence. A RU-only guard from the validator would have appeared in the 0-error run.
2. Links. Per card, RU link sets equal EN's except as follows.
   - Targets absent in RU (plain text correct): kanji 接 鈍 灯 蛍 波 池 柱 採 零; words 体積 接近 満点; articles japanese-onomatopoeia and onomatopoeia-motion-and-sound. I confirmed each file is absent. 寸 and 巾 are unlinked in both.
   - RU-only links, six reported by the author: 広さ→面積, インタビュー→面接, 電球→明るい, 交流→直流, 交流→合流, 乾電池→電池. All six targets exist. Each sits at a substantive contrast or comparison (EN names the same word in plain text at the same position). That satisfies the content-structure rule "links to existing cards at substantive introduction or comparison"; none is wrong or misleading. 乾電池→電池 is linked at the kanji explanation, and the later synonym mention stays plain, which is acceptable.
   - No EN link was dropped where an RU target exists. Intentionally plain pointers (静める, 血色, 電信柱/電線, 充電池/太陽電池, 電圧, 分流, 取材, 湿電池, 体積) have no RU file and EN leaves them plain too, so they are fine.
   - Kanji links match EN for all listed kanji (面, 倒, 静, 青, 白, 少, 年, 光, 電, 球, 直, 流, 組, 合, 交, 同, 乾, 力, 点, 数, 雑, 打, 広, 法, 積).
3. Navigation (10 files). Each diff is exactly one line, with only link brackets/hrefs added. EN has exactly one linked mention in each counterpart, and RU wraps that same mention (number-and-counters:723 面積; 乾:44; 白:39; 青:41; ざわざわ:22; しんみり:30; 会議:30; 蛍:40; 鋭い:39; 青年:35). Path form follows EN (`../words/…` in article/kanji files, `X.md` in word files). No prose change. Pre-existing glosses untouched; none contradicts a new title in a misleading way.
4. Manifest: every non-stroke entry matches the working-tree hash (0 bad), including all 40 changed/new paths and the intake's `candidateRawSha256`. All 30 new cards are present and sorted among their neighbours. `contentVersion` changed. The 118 `strokes/*.json` entries do not match a raw working-tree SHA-256, nor the git blob. This is outside the diff (no stroke file changed), pre-existing, and the manifest tool evidently hashes strokes by another method (see Limits).
5. Intake record: 40 payload paths = exactly the 40 content-diff paths (30 new + 10 navigation); no deletions; only hashes/baseline/source commit/notes (no learner content).
6. Hygiene: no BOM, no trailing spaces, final newline present; the CR bytes match existing cards (working-tree autocrlf). Only expected files in the commit.

Quiz-safety details (symmetric, direct, non-transitive contract):
- All 27 EN guards are retained (list in the brief checked card by card). No dropped pair.
- One-way in-batch declarations suffice (the app applies them symmetrically): 寸法→スケジュール, 広さ→寸法, 面積→広さ, 面接→インタビュー, 静まる→しーん, 蛍光灯→鈍い, 電球→蛍光灯, 電流→直流/交流, 合同→組み合わせ, 合流→組み合わせ, 電池→乾電池, 点数→採点, 零点→点数. 交流↔合流 and 合同↔合流 are guarded from both sides.
- Unguarded in-batch pairs (judged from the actual Russian titles and bodies), all acceptable as in EN: 直流 «постоянный ток»–交流 «…переменный ток» (opposites, taught as a contrast; the 交流 title's «переменный ток» differs from «постоянный ток»); 電流–電力 («ток» vs «мощность», the body of each separates amperes from watts); スケジュール–合同 (shared «мероприятие» is only a qualifier; 合同 is «совместный/слияние/конгруэнтность»); 採点–零点; 電波–電池; 電池–電力; 組み合わせ–打ち合わせ; 組み合わせ–交流. None is a defensible correct answer for the other.
- Titles of the visibly confusable in-batch sets stay distinct: 広さ «протяжённость; величина (пространства)» vs 面積 «площадь (поверхности)»; インタビュー vs 面接; しーん vs 静まる; 蛍光灯 «люминесцентная лампа…» vs 電球 «лампочка»; 直流/交流/電流/電力; 組み合わせ/合同/合流; 電波/乾電池/電池; 採点/点数/零点.
- Declined author pairs (スケジュール–つもり/プラン/計; 寸法–つもり/計算; 打ち合わせ–会/約束; 合同–会/平等; 合流–会/会合; 電波–雑音/連絡/関係/関連; 点数–眼鏡/チェック/結果/評価; 採点–チェック/テスト/確認/審判; 電力–エネルギー/活気; 面倒くさい–疲れる/飽きる; 面接–試験; インタビュー–会話): I agree none is required.
  - Ordinary titles do not equate: プラン «план; пакет услуг» is no answer for スケジュール «график», and 寸法's title is «габариты; размеры» only (the figurative sense is taught in the body but is not the title).
  - 電力 «электрическая мощность; электроэнергия» vs エネルギー «энергия» is the closest. Both bodies separate power from energy, and «электроэнергия» ≠ «энергия». Optional at most; I would not add it.
  - 点数 vs 評価 is already covered by 採点 and 成績 guards; JMdict 評価 (evaluation) vs 点数 (score) is not equivalent.
- The 191 stem-only screen hits (e.g. 面積–面/表面, 交流–文化/お互い/通信/両替, 合流–グループ/道路, 電流/電力–電灯/電子/電車, 電波–ラジオ/受付/診察/食事/仕方, 鈍い–切れ/伝わる/うなる, 点数–量/多少, 零点–機能, 打ち合わせ–予約/予測/応じる/承知/詳しい, スケジュール–定期/実施/会場, 青少年–若い, 広さ–広い, 乾電池–かさかさ, 寸法–大/小) are incidental shared morphemes or qualifiers. The Russian titles do not make one an answer for the other. No whole-title or title-segment duplicate exists against any RU card.
- My own keyword screen of all RU titles (план, график, размер, ширина, комбинация, обмен, ток, лампа, мощность, оценка, баллы, тряпка, обсуждение, совещание, тишина, молодёжь, …) surfaced no additional pair where one batch title would be a defensible correct answer for another existing card beyond the guarded ones. Closest unguarded: 面倒くさい «муторный» vs 手間/苦労 «хлопоты» (adjective vs noun, EN also leaves them), 合流 vs 出会う/会 (title is «слияние потоков; присоединение к группе», not «встреча»), 青少年 vs 男の子/男子/ボーイ (not equivalent).

RU-introduced guards (both keep; neither over-guards harmfully):
- 採点→勘定. Dictionary basis: JMdict 勘定 sense 1 "calculation; counting" and sense 2 "bill; check"; 採点 "marking; grading; scoring" (RU title «подсчёт очков»). The shared Russian word «подсчёт» is the only link. Necessity in an ordinary quiz: not established, because 採点 is primarily «выставление оценок» and 勘定's quiz senses are counting money/bills. Classification: **conservative** (real lexical basis, necessity unestablished). Harmless, so keep; not unjustified, since the cards share a counting sense.
- 打ち合わせ→話し合う. Dictionary basis: JMdict 話し合う "to discuss; to talk together/confer" vs 打ち合わせ "(business) meeting; discussion; arrangement". RU titles «обсуждать вместе» vs «предварительное обсуждение; согласование деталей» share «обсуждение/обсуждать», and the EN-guarded 相談 «консультация; обсуждение» shares exactly that word. The verb/する-noun split makes the pair defensible in either direction. Classification: **conservative**, close to required by parity with the 相談 guard. Keep.
- Neither guards an antonym/contrast taught by the article, and neither is mere topical relation, so there is no "unjustified" guard.

Optional:
- O1 (consistency, inherited from EN, not a candidate defect): 広さ.md uses にじゅっへいほうメートル while 面積.md uses にじゅうへいほうメートル for the same 二十平方メートル. EN has the same split. A sibling-consistency tidy to にじゅうへいほう in 広さ.md would be harmless; I did not establish that にじゅっ is wrong, so this is not a finding.
- O2 (comprehensibility, outside my facets): 打ち合わせ.md "Оттенки значения" last sentence «например о запахе полочек одежды» renders EN's "separate clothing-overlap or archaic matching senses" with a rare Russian term (запах = overlapped garment fronts) and drops the "archaic matching" sense. This is a wording matter for the comprehension reviewer, not a quiz or consistency issue.

Limits:
- Dictionary evidence for the RU-introduced guards (JMdict 勘定, 話し合う, 採点, 打ち合わせ) comes from my knowledge of the entries and the senses the cards themselves cite; I did not re-open the dictionary pages. Necessity classifications are judgments, not measured quiz ambiguity.
- Manifest check is independent of `build_manifest.py` (forbidden). Raw SHA-256 matches for all non-stroke entries; stroke entries use another hashing, so I could not recompute them. They are untouched by the diff.
- Translation accuracy, kanji metadata and example naturalness were not assessed except where they affect links/guards (other facets).
- Did not read batch records, the ledger, progress files, other reviews or scratch worktrees (blind rule).

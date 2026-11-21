# B222 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `d0d6d08431a1e7dd81d6eaa151a8c841c37c297e` (tree `c6b8f7f32697ac0e681e2544e3deb8f92208352a`),
> the signed candidate pushed before review.
> Later reconciliation is in `222-words-batch-61-recheck-001.md`.

Snapshot: RU `d0d6d08431a1e7dd81d6eaa151a8c841c37c297e` (branch full-ru-222-words-61). `git rev-parse HEAD` printed that hash and `git status --porcelain` was empty before and after review; no uncommitted changes. EN source: learning-japanese-en-frozen (6af98cb).

Scope: Facets CONSISTENCY, QUIZ SAFETY and cross-file integration (scoped coverage). Model: not verifiable from inside the session. Read in full (front matter + body, against the EN original by script and by eye): all 30 new cards `words/{カード,トランプ,トラック,デート,デモ,テント,チーム,チーズ,チャンス,ダンス,ダイヤ,タオル,タイプライター,ソファー,センター,セット,スープ,スター,スタンド,スタイル,スケート,スキー,スイッチ,ジーンズ,ジュース,ジェット機,サービス,ゲーム,グループ,グランド}.md`; all seven navigation diffs in full (いす, ベンチ, 交際, 日付, 現金, 選手, 集団: one line each, only link brackets added, byte-identical otherwise); `manifest.json` diff in full; the intake record's path list (not its learner content, it has none). Compared RU titles of ALL RU word cards (252 titles) against each new title using my own stem screen plus the cluster list. Ran `tools/validate.py` (0 errors) and did not run any generator.

Verdicts:
- Consistency (front matter, format, terminology, links, manifest, integration): CLEAN.
- Quiz safety: NEEDS FIX (four minor under-guards, F1-F4; all 21 RU-introduced guards are justified, none is over-guarding).
- Scoped coverage of cross-file integration (link restorations, link parity, manifest, intake): CLEAN, plus one Minor consistency note (F5).

Verified facts behind CLEAN (consistency):
- Front matter keys, `word`, `reading`, `jlpt`, `type`, `kanji`, `tags` equal EN on every card; the only difference is added `quiz_exclusions` (checked below). H2 set/order, H1 reading-parenthesis form, example-bullet count and JMdict ids equal EN on all 30 (ダンス, like EN, has no kanji section). Remaining Latin words are English etymons, JLPT, kanji.
- Links: for every card the set of (text,target) pairs equals EN's, except EN-only `キャンプ.md` (テント) and `ただ.md` (サービス), whose RU files do not exist (confirmed with Test-Path/ls-files), so they stay plain text; and the seven RU-only links (F-notes below). No link in the 30 cards or the 7 navigation files is broken (script resolved every relative target). Path forms match EN (`X.md`, `../kanji/機.md`).
- Navigation: scanned EN→RU across words/, kanji/, articles/: every link an existing RU file shares with EN to a batch word is now present once (いす→ソファー l.33, ベンチ→ソファー l.28, 交際→デート l.29, 日付→デート l.39, 現金→カード l.32, 選手→チーム l.32, 集団→グループ l.36); no EN link to a batch word is left plain in an existing RU file; no prose changed.
- Manifest: diff = new hashes for 30 cards + 7 restored files + contentVersion; nothing else; validator accepts it. Intake path list (37 words/ paths) equals the content diff's 37 words/ paths exactly, candidate hashes match the files, no learner content. No other files in the commit (manifest + intake only).
- All EN `quiz_exclusions` retained on トランプ, デート, チャンス, ダンス, ダイヤ, センター, セット, スター, スタンド, スタイル, ゲーム, グループ, グランド.

RU-only links (judgement against the RU content-structure rule "link existing cards at a substantive introduction/comparison"):
- カード→地図, チャンス→望み: EN does not mention either target at all; the RU card adds a whole paragraph/sentence to compare it (the collision guard), so a link is called for. Accept (addition itself belongs to the correctness reviewer).
- ダンス→踊り: EN names 踊り unlinked in the same sentence where it links 踊る; RU compares them substantively and guards them. Accept.
- スタンド→台: EN names 台 plain (it is also EN's guarded pair); RU compares it. Accept. スタンド→ガソリンスタンド: EN names it plain; the RU card teaches it as a use of スタンド and has the card. Accept.
- ジーンズ→履く: EN uses はく plain in two places; the RU link is on the one that names the wearing verb, and 履く exists. Accept.
- ソファー→椅子 (text 椅子, target いす.md): EN plain; accept as a substantive comparison; form identical to the existing `[椅子](いす.md)` in ベンチ. But see F5 for the neighbouring ベンチ.

Findings:
- F1; Minor; quiz safety; `words/トラック.md:9` (front matter); title «грузовик; беговая дорожка» vs `words/自動車.md` «автомобиль». A truck is an automobile, so «автомобиль» is a defensible correct answer for トラック; the repo's own rule (content-structure: generic label covers a hyponym, 車–電車) and precedent (バス and タクシー each guard both 車 and 自動車; 機械 guards both) call for the same pair. Currently only 車 is guarded. Remedy: `quiz_exclusions: [車, 自動車]`. Evidence: RU titles above; precedent in `words/バス.md`, `words/タクシー.md`. Confidence: medium (necessity in an ordinary quiz is judgement; no downside to adding).
- F2; Minor; quiz safety; `words/デート.md:9`; the card's own body (Синонимы, l.~28) says the dictionary also records «календарная дата» for デート, and EN guards 月日 for exactly that sense, but `words/日付.md` title «дата» is the plainest correct form of that sense and is unguarded. Keep 日付.md byte-identical (navigation-only constraint), so declare it on デート. Remedy: `quiz_exclusions: [月日, 日付]`. Evidence: body of デート (JMdict 1081430 sense 2 cited there); 日付 title «дата». Confidence: medium. (EN has the same gap in English; this is a RU-side decision that does not change the EN guard.)
- F3; Minor; quiz safety; `words/スタンド.md:9`; the card body teaches スタンド as ガソリンスタンド («автозаправочная станция», JMdict 1069930 sense within 1–5), but the title omits it and `words/ガソリンスタンド.md` is unguarded, so «автозаправочная станция» is a defensible answer for スタンド, which the RU rule on taught senses ("учитывайте значения, объяснённые в теле") covers. Remedy: `quiz_exclusions: [台, 電灯, 受付, ガソリンスタンド]`. Confidence: medium.
- F4; Minor; quiz safety; `words/スタンド.md:9`; same lamp sense that the author guards with 電灯 is carried by `words/明かり.md` «свет; светильник» («светильник» = lamp). 明かり's own card guards 電灯, 光, 電気, so the repository already treats those as one cluster. Remedy: add 明かり: `quiz_exclusions: [台, 電灯, 受付, ガソリンスタンド, 明かり]` (combine with F3). `灯` «свет лампы; огонёк» is weaker (optional, not required). Confidence: medium-low.
- F5; Minor/optional; consistency; `words/ソファー.md` Синонимы: `[椅子](いす.md)（いす）— «стул»… ベンチ — скамья.` The author linked 椅子 (RU-only) but left the equally compared ベンチ plain, although `words/ベンチ.md` exists in RU (EN links neither). Either link both or neither. Remedy (matching the sibling form): `ベンチ — скамья.` → `[ベンチ](ベンチ.md) — скамья.` Confidence: medium-low; not a defect in learning terms.

Classification of every RU-introduced `quiz_exclusions` entry beyond EN (dictionary basis: the JMdict entries cited in the cards; I did not re-open JMdict online):
Required (title/segment collision or generic label that makes the other title a defensible answer):
- チャンス→望み (RU title «…шанс» exact; 望み sense «chance, prospect»); ダンス→踊り (exact «танец; танцы»; 踊り = dance); ジェット機→飛行機 («самолёт» contained in «реактивный самолёт»); ゲーム→遊び (exact «игра»); グランド→大きい, グランド→大きな (exact «большой»).
- カード→地図 (RU-only homograph: 地図 «карта» equals the segment «…игральная карта»/«платёжная карта»; JMdict 地図 = map; the card itself had to disclaim it). Author called it conservative; I rate it required.
- トラック→車 (generic «транспортное средство; автомобиль»; see F1 for 自動車).
- チーム→命令 (exact segment «команда»; 命令 = command/order, Russian homograph). Required.
- ダイヤ→宝石 and ダイヤ→玉 (both titles contain exact «драгоценный камень»; бриллиант is one; JMdict 宝石 gem; 玉 sense «gem, jewel»); ダイヤ→予定 (JMdict ダイヤ 2855660 train schedule vs 予定 «расписание»).
- スター→有名 (near-duplicate stems «знаменитость»/«знаменитый»); スタンド→電灯 (exact «лампа»); ジーンズ→ズボン (брюки ⊃ джинсы, generic label); ジュース→飲み物 (exact «напиток» in the title); グループ→クラス («учебная группа» contains «группа», same logic as the EN-kept 団体/集団/組).
Conservative (real basis, necessity unestablished; all harmless, keep):
- タイプライター→機械 («машинка» vs «машина»; generic hypernym; 機械 already guards 車/自動車); センター→選手 (secondary sense «центральный полевой игрок»→«игрок»); スタンド→受付 (exact word «стойка» but different senses: 受付 reception desk vs sales stand/counter); サービス→無料 (body teaches «бонус за счёт заведения»/free, 無料 «бесплатно»; leaning required).
Unjustified: none. No over-guarding where titles already separate cards.
Screen conclusions where no guard is needed (checked, not under-guarded): カード vs 切符/手紙/トランプ (EN trump guard kept); デート vs 約束 (договорённость ≠ свидание), 会う; デモ vs でも/見せる; テント vs 小屋; チーズ vs バター/牛乳; タオル vs ハンカチ; ソファー vs いす/ベンチ/席/座席; センター vs 中/半ば (no shared title segment); セット vs 準備 (title has no «подготовка»; only one of three taught action senses, so left to the EN link); スープ vs 食事; スケート/スキー vs 滑る/each other (EN); スイッチ vs ボタン; ジェット機 vs 便; ゲーム vs 演技 («актёрская игра» qualified), トランプ; チーム vs 団体/組/グループ (hypernym, EN parity, not guarded in EN); グランド vs 立派/偉大/莫大. ダンス vs 演技 (EN link).

Optional: (a) `灯` as an extra lamp pair for スタンド (see F4); (b) `トラック→乗り物` is not needed (precedent 飛行機 does not guard 乗り物).

Limits: I did not re-open JMdict entries online; sense/basis statements rely on the entries cited inside the cards plus the RU/EN card text. Quiz necessity is judged from displayed RU titles and RU-taught senses, not from the app's actual distractor sampler. The RU-only prose added to カード (map paragraph) and チャンス (望み paragraph) and ダンス/ソファー comparisons is not in EN; its linguistic correctness is outside this facet. Did not read batch records, author reports, title-screen outputs or scratch worktrees. My scratch screen output `b222-consistency-scratch-titles.txt` in FILES is a by-product of my own title scan and may be deleted.

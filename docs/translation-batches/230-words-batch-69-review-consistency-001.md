# B230 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `5ec190a7c89f162bdb1673eca213fab94aab9624` (tree `6d3c31bd01596be9b29662885a4d2cae61c73bac`),
> the signed candidate pushed before review.
> Later reconciliation is in `230-words-batch-69-recheck-001.md`.

Snapshot: RU `5ec190a7c89f162bdb1673eca213fab94aab9624` (HEAD confirmed, `git status --porcelain` empty, no uncommitted changes). Parent `8a4f655`. EN frozen `6af98cb`.

Scope: Read in full against their EN originals (front matter and body): all 30 new cards (長男 四角 四角い 正方形 長方形 長所 継続 長引く 長女 鑑賞 鐘 録音 錆 錆びる 銅 鉱物 丼 鉢 鉄砲 鉄橋 鈴 仕上がる イコール 整備 揃える 揃う 釣り合う 針金 課程 過程), the full `words/ベル.md` diff (1 line), the manifest diff, and the intake record. Facets: consistency, quiz safety, cross-file integration. Tools: scripted front-matter/link comparison RU vs EN for all 31 files; RU target existence checks; `tools/validate.py` (0 errors); my own `word_title_screen.py` run (no unguarded identical-segment overlap, 29 guarded) plus stem scans of all RU titles. `build_manifest.py` not run. Model: not verifiable by me.

Verdicts:
- Consistency: CLEAN (two minor link-opportunity notes, F2/F3, are optional-grade).
- Quiz safety: NEEDS FIX (one missing guard, F1).
- Cross-file integration (scoped coverage): CLEAN.

Findings:
- F1; minor; quiz safety; `words/長所.md:9`; 長所 «достоинство; преимущество» is not guarded against 武器 «оружие; сильная сторона». RU 武器's title and body (`武器.md` "преимущество / сильная сторона") give a figurative sense that equals 長所's own definition («сильная сторона, достоинство или преимущество»). The RU 得意↔武器 guard was added for the same «сильная сторона» collision; EN has no such pair because EN titles differ ("weapon; asset" vs "strong point; merit; advantage"). A learner could defensibly pick either answer. Remedy: `quiz_exclusions: [得意, 利益, 味噌, 武器]` (EN entries kept in order, then regenerate the manifest). Evidence: JMdict 長所 sense 1 (strong point/merit/advantage) vs 武器 figurative sense "asset/advantage"; I did not re-fetch the dictionary, so this rests on the RU card text. Confidence: medium-high.
- F2; minor (optional-grade); consistency/links; `words/四角.md:27`, `words/四角い.md:35`, `words/正方形.md:34`; 長方形（ちょうほうけい）is glossed and contrasted in the same sentence as the linked 正方形, but left plain for EN parity, although the RU card now exists in this batch. The RU rule says to link existing cards at substantive introduction or comparison. Remedy: `[長方形](長方形.md)（ちょうほうけい）` at those three positions (no prose change; regenerate the manifest). Confidence: medium (EN parity is defensible; no validator impact).
- F3; minor (optional-grade); consistency/links; `words/鐘.md:29`; 鈴（すず）is a glossed comparison next to the linked ベル, and 鈴.md now exists. Remedy: `[鈴](鈴.md)（すず）`. Same for 撮る in `words/録音.md:47` (passing contrast, weaker; link optional). Confidence: medium.

Navigation file `words/ベル.md`: PASS. The diff is exactly `鐘（かね）` → `[鐘](鐘.md)（かね）` at line 38. EN links 鐘 once, in the same sentence; 鈴 and チャイム stay plain as in EN. No other prose change. The pre-existing «более крупный колокол» matches the new card's title «колокол» and does not mislead. No other RU file has an EN link to a new card that is still plain (scanned all EN words/kanji/articles against RU).

Guards retained and added:
- All EN `quiz_exclusions` are retained in EN order on all 28 keyed cards. 錆 and 銅 have no key, as in EN. Front matter equals EN except the three RU additions below.
- One-way declarations are sufficient (pairs are symmetric in the app). 四角↔四角い is bidirectional. All 29 title-screen overlaps are guarded.
- 丼→料理: real basis (丼 sense 2 "rice dish" vs 料理 «блюдо»); conservative, necessity unestablished but plausible. Keep.
- 鉢→植木: real basis only as topic (JMdict 鉢 sense "flowerpot" vs 植木 "garden tree; potted plant"); a container is not the plant, so a learner would not defensibly confuse them. Conservative, marginal; harmless, no change required.
- 過程→途中: real basis (RU 途中 title «в процессе» vs «процесс»); conservative, plausible for an ordinary quiz. Keep. None is unjustified; there is no over-guarding of titles that already separate.
- Unguarded in-batch pairs all pass from the titles: 長男/長女, 鉄砲/鉄橋, 銅/鉱物, 銅/針金, イコール/釣り合う, 仕上がる/整備, 錆/銅. Distinctness of the in-batch pairs 四角/四角い/正方形/長方形, 長男/長女, 鐘/鈴, 錆/錆びる, 丼/鉢, 揃える/揃う/釣り合う, 継続/長引く and 課程/過程 is clear from the displayed titles.
- Declined pairs judged not required: 長男–兄, 長女–姉, 四角–角, 四角い–丸い, 長所–特徴/長短/善/立派, 継続–中止/状態, 長引く–曇る/締める, 鑑賞–感覚/作品/芸術, 録音–テープレコーダー/撮る, 錆–腐る, 錆びる–覆う, 銅–金属/銅貨, 鉱物–金属/宝石, 針金–コード/電柱/紐, 丼–皿/鍋, 鉢–花/花瓶/鍋/頭, 鉄砲–矛, 鉄橋–鉄道/列車/鉄, 整備–サービス/片付く/順序/技術, 揃える–全部/集まり, 揃う–組/構成/足りる, 課程–スケジュール/クラス/教育/学期, 過程–学習/裁判/順序/発展/発達/結果. The titles differ in sense or part of speech.

Consistency checks passed: all kanji/word links resolve; every dropped EN link has no RU target (kanji 角 賞 録 銅 鉱 鉄 橋 針 課, words 三角 仮定 学科 短所 釜 are absent; kanji 整 is absent, so the 整備 sentence is accurate); `kanji:` metadata equals EN; the manifest holds the correct sha256 for all 31 changed files and the intake record's 31 payload paths and hashes equal the candidate diff (no learner content); `validate.py` reports 0 errors; no generated or unrelated files were committed.

Optional:
- 長女→お嬢さん and 長所→プラス «положительный фактор» are weak hyponym/gloss overlaps; not required. 長女→娘 already follows the EN pattern.

Limits:
- Dictionary senses for F1 were not re-fetched. Linguistic correctness and comprehensibility are outside this facet. The model identity is unverified. The author's batch records and the other reviewers' reports were not read.

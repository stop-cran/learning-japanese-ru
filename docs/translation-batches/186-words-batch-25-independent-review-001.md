# Blind review — RU batch 186 (186-words-batch-25)

## Snapshot
- Repo: `C:\Users\romanko\repos\learning-japanese-ru`, HEAD `ff841a6` + staged index tree `4fdfa8d52a569a9e17217c477f8faab0cc715b70` (`git write-tree` matched). Uncommitted candidate; read-only review, nothing modified.
- Staged: 30 new `words/*.md`, 12 restoration files, `manifest.json`, intake JSON (not read, for blindness).
- Frozen EN source: `learning-japanese-en-frozen`.

## Scope
- I read all 30 new articles in full against EN: 食品, 食卓, 食う, 飛行, 飛び出す, 飛ばす, 除く, 風景, 題, 期間, 時, 時期, 頃, 表面, 面, 非常, 霧, 霜, 雷, 電子, 需要, 離婚, 去る, 離れる, 問い, 革, 頬, 預ける, 頼る, 省く.
- I checked the diffs of the 12 restoration files (kanji/期, kanji/除, 供給, 依頼, 底, 引き出す, 曇り, 極, 略語, 限る, 食料, 食糧). Together they add 16 `[X](path)` links and change no other text.
- `manifest.json` hashes cover all 42 files.
- Tools: `link_parity.py` passes for all 42 files. Its only note is the pre-existing extra link 曇る in 曇り, which is outside this batch. `word_title_screen.py` was run over the batch. JMdict senses were checked through the Jisho API.
- Every link dropped relative to EN points to a card that does not exist in RU, e.g. 商品, 含む, 信じる, 預かる, 任せる, 時刻, 氷, 眺め, 異常, kanji/省, kanji/卓, kanji/預.

## Verdicts
- Correctness: **CLEAN**
- Scoped coverage: **CLEAN**
- Comprehensibility: **CLEAN** (optional polish only)
- Quiz safety: **NEEDS FIX** (F1)

## Findings

### F1 — Minor, quiz safety, confidence medium
`words/預ける.md`:4 (title «отдавать на хранение; оставлять под присмотром») and :1–8 (no `quiz_exclusions`). The existing card `words/頼む.md` has the title «просить; поручать». The guard is needed because 預ける can be the right answer for «поручать».
- Basis:
  - JMdict 預ける sense 2: "to put (someone) in charge of; to leave (a matter) in someone's hands" (https://jisho.org/api/v1/search/words?keyword=預ける).
  - JMdict 頼む sense 3: "to entrust to" (https://jisho.org/api/v1/search/words?keyword=頼む).
  - Ožegov «поручить» sense 2: «предоставить чьим-н. заботам, попечению (поручить ребёнка няне)». This sense overlaps with «оставлять под присмотром».
- So when the quiz prompt is «оставлять под присмотром» and 頼む «поручать» appears as a choice, both choices are defensible.
- Remedy: `quiz_exclusions: [頼む]`.
- Conservative extra: also add 依頼 «просьба; поручение». It is weaker (a noun), but «поручение» shares the same sense.

## Optional (not defects)
**Possible extra guards.** Each has dictionary support, but none is required:
- 離れる vs 別れる «расставаться; прекращать отношения».
  - Support: 離れる sense 1 "to be separated"; Russian «расстаться с родиной» = 故郷を離れる.
  - Against: the RU 別れる card (L35) teaches the contrast, and EN has no guard.
- 非常 vs 急 «внезапный; срочный».
  - Support: 非常 sense 1 "emergency".
  - Against: 急's emergency sense is not verified here.
- 非常 vs 珍しい.
  - Support: 非常 sense 2 includes "unusual".
- 表面 vs 外 «снаружи».
  - Support: 表面 sense 2 "outside; exterior". The 表 card guards 外.
  - Against: 表面 L29 teaches the contrast itself.

**Polish:**
- 問い: the title «вопрос (в задании, в рассуждении)» is narrower than the body (L16), which also allows a question asked aloud.
- 頼る: the title says «(на кого-л.)», but the body covers maps and experience too. Suggest «на кого-л./что-л.».
- 雷 L16–18:
  - The comparison with English is unnecessary for a Russian reader.
  - «предоставить глаголу уточнять» is awkward; suggest «оставить уточнение глаголу».
- 預ける example 1: «стойки регистрации» for 受付 is acceptable; «на ресепшене» is an alternative.

**Accepted RU-specific adaptations** (all correct):
- 頬: the EN sentence about the English idiom "cheek" was dropped.
- 離婚 L21: と is explained via «развестись с мужем».
- 霜 L42: uses «выпадает иней».
- 革 L28: Russian «кожа» covers both 皮 and 革.
- 電子 L42: adapted for Russian.
- 除く L37: 〜を除いて ≈ «кроме».

**Guards added beyond EN.** All have a dictionary basis; none is unjustified. Each entry gives the card, the basis, and whether the guard is required or conservative.
- 食品
  - 食糧 «продовольствие»: shared food sense; conservative.
- 食卓
  - テーブル: shared «стол»; required.
- 食う
  - 召し上がる and いただく: JMdict "eat" (honorific/humble); conservative because of register.
  - 取る: sense 7 "to eat"; conservative.
  - 掛かる: 食う "consume time"; required.
- 飛行
  - 飛ぶ: flight overlap; required.
- 飛び出す
  - 出る: "emerge"; required.
- 除く
  - 以外: 除く "except"; required.
  - 取る: 取る "remove"; required.
- 飛ばす
  - 投げる: 飛ばす "hurl"; conservative.
- 風景
  - 山水: "landscape"; required (precedent: 景色).
- 題
  - 名前: «название»; conservative.
- 期間
  - 時代: exact «период»; required.
  - 間: «промежуток»; conservative.
- 時
  - ころ, 場合, ケース: exact title matches; required.
  - 機会: 時 sense 3 "chance"; required.
- 時期
  - 時間, ころ: «время»; required.
  - 季節: "season"; required.
  - 間: conservative.
- 頃
  - ころ: the same word in kana; required.
  - くらい, ほど, 約, ほぼ, およそ, ばかり: «около»; required (precedent: the ころ card).
  - そろそろ: «пора»; required.
  - 時間: conservative.
- 表面
  - 表: «поверхность»; required.
  - 格好: sense 3 "appearances"; required.
- 面
  - 表, 点: exact title matches; required.
- 非常
  - 非常に, 極: required.
  - 大変: conservative.
  - 特別: conservative-to-required.
- 霧
  - もやもや: required/conservative.
- 雷
  - ごろごろ: rumbling of thunder; conservative.
- 需要
  - 必要: "need"; conservative.
- 離婚
  - 別れる: JMdict "to divorce"; required.
- 去る
  - 出る, 立つ: "leave"; required (precedent: 行く).
  - 行く, 出かける: conservative.
  - 過ぎる: sense 2 "pass"; required.
  - 亡くなる: required.
- 離れる
  - 遠い, 遠く: sense 1 "be distant"; conservative.

## Limits
- No native-speaker check of the Russian or Japanese. The Ožegov wording is cited from reference knowledge; I did not fetch it.
- I did not exercise quiz behaviour in the app and did not run the full content validator.
- 急's "emergency" sense and ごろごろ's child-language "thunder" sense are not verified.
- I did not read the author's report, the batch docs, drafts, tracking files or prior reviews.

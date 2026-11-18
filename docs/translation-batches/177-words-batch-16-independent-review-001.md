Snapshot: RU repo `learning-japanese-ru`, branch `full-ru-177-words-16`, candidate commit `0abb3aa` (parent `a9d02c8`); working tree clean (no uncommitted changes). EN source: frozen `learning-japanese-en-frozen` @ 6af98cb.

Scope: 30 new word articles (救う 救助 手伝い 援助 柱 柚 枚 松竹梅 梅 杏 李 曲 増す 増加 昇る 政治家 採掘 釣り 漁業 水産 捕鯨 御殿 彗星 局 オフィス 庁 基本 基 水準 計る) read in full against the EN originals. Navigation-only restoration edits in kanji/曲, words/拡大, 支える, 桃, 橘, 発展, 竹, 鉱石, 隻, 鯨 checked by `git diff --word-diff` against EN link positions. manifest.json and the batch intake JSON checked for content and generated files. Tools used: `link_parity.py` (all 40 paths) and `word_title_screen.py` (all 30 titles vs all RU word titles), plus a manual check of neighbouring cards' titles and exclusions. Reviewer: independent read-only reviewer (Claude-family model; exact version not exposed).

Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility NEEDS FIX (one Low); quiz safety NEEDS FIX (one Medium)

Findings:

F1; Medium; quiz safety; words/増す.md:9
Claim: `quiz_exclusions: [増える, 拡大]`. 増す's title «увеличиваться; усиливаться» repeats the segment «увеличиваться» from 増える. In RU, 増える guards 上がる «подниматься; повышаться» and 上げる «поднимать; давать» on that same segment. These are RU-added guards; EN 増える has none. 増す does not carry the same guard.
Impact: «подниматься; повышаться» is a defensible answer for 増す. The card's own first example renders 川の水が増しました as «вода в реке поднялась». The transitive use (勢いを増す, スピードを増す, «поднимать скорость») also makes «поднимать» defensible, so a learner could pick a "wrong" choice that is actually right.
Remedy: `quiz_exclusions: [増える, 拡大, 上がる, 上げる]`
Evidence: RU words/増える.md front matter `quiz_exclusions: [上がる, 上げる, 付く]` (title «увеличиваться»); RU words/上がる.md title «подниматься; повышаться»; RU 増す.md:20. JMdict 増す "to increase; to grow", both transitive and intransitive: https://jisho.org/search/増す
Confidence: high that the precedent applies; medium-high for 上げる.

F2; Low; comprehensibility (transliteration consistency); words/松竹梅.md:18
Claim: «…делятся на разряды «мацу», «таке» и «умэ».» This writes たけ as «таке», but the same line writes «умэ», and the corpus uses Polivanov spelling elsewhere (сакэ, отядзукэ). In Polivanov, け is «кэ».
Impact: an inconsistent, non-standard Cyrillic reading for a learner. It can suggest the reading is たけぇ or たけ with a palatalised け.
Remedy: `- この店のコースは松竹梅に分かれています。（このみせのコースはしょうちくばいにわかれています。）— Комплексные обеды в этом ресторане делятся на разряды «мацу», «такэ» и «умэ».`
Evidence: RU words/酒.md:4 «сакэ»; words/さらさら.md:33 «отядзукэ»; Polivanov system: https://ru.wikipedia.org/wiki/Система_Поливанова (け = кэ).
Confidence: high.

No other defect established:
- Japanese examples and kana readings are verbatim in all 30 articles. Translations keep tense, polarity and register.
- Every EN sense, note, example and citation is retained. English-only contrasts are re-expressed for Russian rather than calqued:
  - 救う: "save a file / money"
  - 柱: "support", with the English "post" note dropped as English-only
  - 御殿: "court"
  - 局: "station" vs 駅, and the "court lady" note
  - オフィス: "take office"
  - 柚: citron = Citrus medica
  - 梅/杏/李: plum/apricot, with Russian botanical names verified (Абрикос японский/муме = Prunus mume; Слива китайская/иволистная = Prunus salicina; https://ru.wikipedia.org/wiki/Абрикос_муме, https://ru.wikipedia.org/wiki/Слива_китайская)
  - 水産: «морепродукты» too narrow
  - 曲: «песня» in colloquial Russian
- Every link dropped relative to EN points to an RU target that does not exist yet (link_parity: no LOST links in the 40 paths). The only EXTRA link, kanji/曲 → words/曲る.md, is pre-existing at line 51 and not part of this diff.
- The restoration edits only wrap existing words in brackets at exactly the EN link positions (曲×3, 増加×2, 援助, 梅×2, 柚, 採掘, 枚, 捕鯨); no other text changed.
- No generated files (`__pycache__`, `.pyc`) are committed. The intake JSON follows the batch 175/176 precedent.
- Quiz guards: all EN exclusions are retained. Every pair from the title screen that shares an exact segment is guarded on at least one side:
  - 救う/救助/助ける
  - 手伝い/援助 vs 世話/おかげ/手伝う/助ける/支える/賛成
  - 柱 vs 支える/援助/賛成/棒
  - 杏/李 vs 梅
  - 増加 vs 拡大/成長/増える/増す
  - 局/庁 vs 管理, 局 vs 駅, 庁 vs 局
  - オフィス vs 事務所/会社
  - 基 vs 基本
  - 釣り vs 釣る, 漁業/水産/捕鯨
  - 曲 vs 歌
  None of the added guards is unjustified: 援助→賛成 shares «поддержка»; 援助→支える/助ける/手伝う use the action sense of the する-noun; オフィス→会社 follows the 事務所 precedent and the article's «офис» = firm note; 局→駅 follows «станция»; 局/庁→管理 share «управление».

Optional:
- 昇る «…продвигаться по службе» vs 進む «двигаться вперёд; продвигаться»: there is weak overlap on «продвигаться». JMdict 進む has no promotion sense (https://jisho.org/search/進む) and EN does not guard the pair. A guard (`quiz_exclusions: [上がる, 登る, 増加, 進む]`) is optional, not required.
- 松竹梅.md:18 «Комплексные обеды» narrows コース to lunch-type set meals; «Комплексные меню» would be closer. 梅.md:39-40 «базовый комплекс» reads awkwardly; consider «самый простой вариант меню».
- 漁業.md:20 «работает в рыболовстве» could read more naturally as «занят в рыболовстве» or «работает в рыбной отрасли».
- 水産 title «продукты водного промысла» is understandable but uncommon; «рыбная продукция и морепродукты; рыбное хозяйство» or «водные биоресурсы» are alternatives. This is not a defect.

Limits: Quiz-safety screening used word titles only, via word_title_screen.py's segment/stem heuristic plus a manual check of about 50 neighbouring cards. Kanji-card distractors and generated quiz fallbacks were not simulated. The kotobank, Weblio and Nipponica citations were not re-fetched; they were checked only for faithful retention from EN. The Russian botanical names were verified on ru.wikipedia, not in a botanical reference. The author report and prior batch reviews were not read, as instructed.

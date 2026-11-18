Snapshot: learning-japanese-ru `c3f1c45` (parent `d588f49`), branch full-ru-181-words-20; HEAD = c3f1c45, worktree clean (no uncommitted changes). EN source: learning-japanese-en-frozen 6af98cb.
Scope: I read all 30 new word articles in full, side by side with the EN originals (炊事 炊く 煮える 煮る がやがや ぶるぶる わくわく 天候 陽気 うきうき ぞくぞく ざわざわ ささやく ぶつぶつ 凹凸 武士 兵士 公演 体力 亥 亀 それとも あるいは 乃至 丑 メーメー しくしく めそめそ 叫ぶ 吠える). I checked the 17 navigation-only edits with `git diff --word-diff`; every change there only adds link brackets. I ran link_parity.py (new files: 0 lost/extra; edited pages: only a pre-existing extra 兆候 link in kanji/候.md, not from this commit). I ran word_title_screen.py over all 30 titles and manually compared titles and exclusions against the named clusters (cooking, crowd noise, shiver, excitement, weather, whisper/grumble, unevenness, military, performance, strength, zodiac/animals, "or", crying, shouting). The commit stat shows no generated files (no __pycache__ or .pyc); manifest.json changes are hash entries only. Reviewer: independent read-only reviewer (Claude). I did not read the author report or any prior reviews.
Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility NEEDS FIX (minor); quiz safety NEEDS FIX

Findings:
- F1; Medium; quiz safety; words/公演.md:4,8. The title «выступление артистов; спектакль» shares the Russian word «выступление» with two existing cards: スピーチ «выступление перед слушателями» and 演説 «публичная речь; выступление». Russian «выступление» covers both a speech and a performance in front of an audience (выступить = «произнести речь, исполнить что-нибудь перед публикой»). So when the quiz asks about 公演, the 演説 gloss «выступление» and the スピーチ title «выступление перед слушателями» are both defensible answers. There is already a precedent: スピーチ guards 演説 over the same «выступление» segment. 公演 guards only 芝居. This collision exists only in Russian: EN "public performance" and "speech" do not overlap. Remedy: `quiz_exclusions: [芝居, 演説, スピーチ]`. Alternatively, retitle to «публичное представление; спектакль»; that matches the wording already used in kanji/演.md and avoids «выступление». Evidence: current RU titles of スピーチ and 演説 (words/スピーチ.md, words/演説.md); Gramota/БУС entry «выступить» (https://gramota.ru/poisk?query=выступить&mode=slovari). Confidence: high.
- F2; Low; quiz safety; words/煮える.md:9 (and optionally words/煮る.md:9). 煮える «вариться; провариться» has no guard against ぐつぐつ «булькать на огне; кипеть» or ことこと «томиться на медленном огне; тихо постукивать». The 煮える article itself says the verb can describe liquid boiling, and that is exactly why it already guards 沸く «кипеть». ぐつぐつ carries the same «кипеть», and the RU ぐつぐつ card glosses 煮える as «вариться, томиться». So «кипеть» and «томиться» are defensible answers to a 煮える question, and «вариться» is a defensible answer to a ことこと or ぐつぐつ question. ぶつぶつ already guards ぐつぐつ, ことこと, 煮る and 煮える over the simmering sense, which is precedent for this cluster. Remedy: `quiz_exclusions: [沸く, 沸かす, 炊く, 料理, 焼ける, ぐつぐつ, ことこと]`. Optionally add ことこと to 煮る («тушить» vs «томиться»). Evidence: RU titles; words/ぐつぐつ.md "ぐつぐつ煮える（にえる — вариться, томиться）"; 煮える.md "煮える тоже может описывать кипение жидкости". Confidence: medium. EN shares the same gap, so this is a precautionary guard rather than a hard ambiguity.
- F3; Low; comprehensibility; words/武士.md:28-29. «эти слова ни повсеместно не противопоставлены, ни не являются полностью взаимозаменяемыми терминами» is an ungrammatical double negation («ни … ни не являются») and is hard to parse. Remedy: «эти слова не являются ни повсеместно противоположными, ни полностью взаимозаменяемыми терминами.» Evidence: standard Russian ни…ни construction. Confidence: high.

Optional:
- 叫ぶ.md:25: «звуковое изменение в ん» reads better as «переход в ん» or «замену на ん».
- うきうき.md:26: «Образ «всплывающего» настроения». EN "floating image" (浮く) could be «Образ «плавающего, парящего» настроения». Current wording is acceptable.
- がやがや and ざわざわ against うるさい «шумный; назойливый». The overlap is weak because がやがや is chatter and need not be annoying. EN has no guard either, so this is not required. Consider [うるさい] on がやがや if you want to be conservative.
- 公演 against コンサート «концерт»: the overlap is the same in EN, so it is not raised as a defect.

Checks that came out clean:
- Japanese examples and kana readings are kept verbatim. Added full-kana readings are correct.
- Tense and polarity are correct, e.g. 肉はまだよく煮えていません → «ещё не проварилось»; めそめそしないで is kept as a request.
- English-only contrasts are re-expressed for Russian rather than calqued:
  - それとも threat «или… а не то»
  - 亀 «черепаха» covers land and water species
  - 亥 «Кабан/Свинья» in Russian horoscope naming; «кабан» male sense
  - 吠える «выть» = colloquial «громко рыдать» (Ожегов)
  - 叫ぶ: no tears implied
  - 兵士: Russian «воин»
- あるいは «аруива» follows the Polivanov system.
- All EN quiz_exclusions are retained.
- New guards are justified: 亥–豚 (Russian «Свинья» naming), 吠える–泣く (выть), しくしく–痛い, うきうき/陽気–楽しい, ぞくぞく–寒い, わくわく–楽しみ, 叫ぶ–呼ぶ (助けを求めて叫ぶ / «зовя на помощь»), ささやく–ぼそぼそ, 炊事–台所/こしらえる, 体力–力, がやがや/ざわざわ–騒ぐ, メーメー–鳴く. None looks clearly unjustified.
- EN links to missing RU targets (焚く, 気候, どきどき, 続々, しーん, くよくよ, こけこっこー, わんわん, 時刻, kanji 武/士/亥/亀/丑/凹/凸/乃) and article links are de-linked. Image fields are dropped. Both match the existing RU convention (ぐつぐつ).

Limits:
- I did not re-verify JMdict entry numbers or Daijisen/Kotobank/Kanjipedia URLs live; they are unchanged from EN.
- The quiz assessment uses current titles in the RU tree at c3f1c45. I did not run the quiz app or the repo validator.
- The extra 兆候 link in kanji/候.md predates this commit and is out of scope.

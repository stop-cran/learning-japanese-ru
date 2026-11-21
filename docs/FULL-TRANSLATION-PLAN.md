# Full Russian translation: execution after the two pilots

## Current published source milestone: batch221 thirty words (general word queue)

Batch221 adds 30 Russian word articles: ミルク ミス ママ マスター マイク ボール ホーム ペンキ ベンチ ベルト プロ ブレーキ ピクニック
ビール ビデオ パーセント パスポート パイロット パイプ バン バッグ バイオリン ハンサム ハイキング ドレス ドラマ ドライブ ド トンネル
トン. They are chunk 13 of 72 of the general remaining-word queue, recomputed after Batch207 from 2,157 remaining EN words.
Their dependency closure is exactly the 30 requested words, so every EN quiz_exclusions target resolves to an existing RU
word or a batch word.

Navigation-only link wraps restore 8 links at EN link positions in 8 files: 7 existing word pages and the
numbers-and-counters article. ワイン's link to ビール, held since Batch220, is among them. Every new card is written in kana,
so no kanji label is left plain.

The batch covers:
- food and drink: milk and infant formula (ミルク), beer (ビール), and a picnic (ピクニック);
- people and address: a mistake or "Miss" (ミス), mum and a bar proprietress (ママ), a bar owner or mastering a skill
  (マスター), a professional (プロ), a pilot (パイロット) and handsome (ハンサム);
- objects and equipment: a microphone (マイク), a ball or mixing bowl (ボール), paint (ペンキ), a bench (ベンチ), a belt
  (ベルト), a brake (ブレーキ), a video (ビデオ), a passport (パスポート), a pipe or connection (パイプ), a bag (バッグ), a
  violin (バイオリン) and a dress (ドレス);
- places, travel and media: a platform or home (ホーム), a hair bun, a van or a VAN network (バン), hiking (ハイキング), a TV
  drama (ドラマ), a drive (ドライブ) and a tunnel (トンネル);
- measures and a prefix: percent (パーセント), a tonne (トン) and the intensifying prefix ド.

All 19 EN exclusions are retained. Eighteen direct guards on 11 new cards cover the reviewed RU title overlaps and
sense neighbours:
- required: ハンサム–美しい, ハンサム–きれい, バン–束, ドライブ–旅行, ド–いちばん, ド–完全 and, added in the fix, パイプ–仲;
- conservative: ボール–ちゃわん, マスター–上達, ドラマ–出来事, ビール–酒, ビール–お酒, ハイキング–観光, パイプ–付き合い and,
  added in the fix, パイプ–関係, パイプ–連絡 and ドライブ–散歩;
- a retained harmless over-guard: プロ–職業.

Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.

The candidate was signed and pushed before review. The blind facet-split review raised the following:
- correctness: no defect, but three exact Russian labels left UNVERIFIED (ドライブ's «автопрогулка», バン's «сеть с
  добавленной стоимостью» and ボール's baseball «бол»);
- consistency: one minor quiz-safety finding: パイプ's people-relations gloss left 関係, 連絡 and 仲 unguarded;
- comprehensibility: six minor findings: ド's «совершенный», ボール's «бол»/«страйк», ママ's «по-домашнему», バン's «добавленная
  стоимость», ビデオ's unexplained «VHS» and トンネル's «выехали».

One signed fix commit addressed them:
- パイプ excludes 関係, 連絡 and 仲;
- ド's title became «усилительная приставка (самый, полный)», and ママ's qualifier «в семейной речи»;
- ボール explains the baseball sense as a pitch outside the strike zone;
- バン's title says «сеть передачи данных (VAN)», and its body and example «сеть передачи данных с дополнительными услугами»;
- ビデオ says «старую видеокассету», and トンネル says «вышли» and «в которое входят»;
- ドライブ's title became «поездка или прогулка на машине», and it also excludes 散歩.

The serial rechecks reported all facets clean. Links follow EN, with five RU-only links to existing cards at a substantive
comparison or mention: ホーム–帰宅, ドラマ–テレビ, ビール–ビル, バイオリン–弾く and トン–キログラム. ベンチ's EN link to ソファー stays
plain until ソファー lands in Batch222.

Qualified progress is **4,749 reviewed-current / 8 reviewed runtime-blocked / 3,521 pending of 8,278**,
with 3,283 words, 718 kanji and 718 strokes. See the [intake](translation-batches/221-words-batch-60-intake.json),
[independent review](translation-batches/221-words-batch-60-independent-review-001.md),
[recheck](translation-batches/221-words-batch-60-recheck-001.md),
[qualified source record](translation-batches/221-words-batch-60-reviewed-source.json) and
[final validation](translation-batches/221-words-batch-60-final-validation-001.json).

## Previous published source milestone: batch220 thirty words (general word queue)

Batch220 adds 30 Russian word articles: 世紀 世の中 不足 不自由 不正 不幸 不安 不可 不 下り 上京 一言 一般 一致 一瞬
一生 一方 一度に ますます 一層 一家 一体 一人一人 ワイン ロケット ラケット ヨーロッパ ユーモア メンバー メモ. They are chunk
12 of 72 of the general remaining-word queue, recomputed after Batch207 from 2,157 remaining EN words. Their dependency
closure is exactly the 30 requested words, so every EN quiz_exclusions target resolves to an existing RU word or a batch
word.

Navigation-only link wraps restore 19 links at EN link positions in 18 files: 16 existing word pages, the kanji page 不
(two links to 不安) and the numbers-and-counters article. 世間's link to 世の中, held since Batch219, is among them. The
kanji 可, 層, 瞬, 紀, 致 and 般 remain plain labels because they have no RU card.

The batch covers:
- centuries (世紀), the world of people (世の中), a descent or outbound direction (下り) and going to the capital (上京);
- the negative prefix 不 and its words: shortage (不足), restricted means (不自由), dishonesty (不正), misfortune (不幸),
  anxiety (不安) and "not permitted" (不可);
- words with 一: a word or two (一言), "general; ordinary" (一般), agreement (一致), an instant (一瞬), a lifetime
  (一生), one side or "on the other hand" (一方), "all at once" (一度に), the whole family (一家), "what on earth" and a
  single whole (一体) and each person individually (一人一人);
- "more and more" (ますます) and "even more" (一層);
- wine (ワイン), a rocket or locket (ロケット), a racket (ラケット), Europe (ヨーロッパ), humour (ユーモア), members (メンバー)
  and notes (メモ).

All 26 EN exclusions are retained. Thirty-two direct guards on 19 new cards cover the reviewed RU title overlaps and
sense neighbours:
- required: 不足–欠ける, 不可–禁止, 下り–下りる, 下り–方向, 上京–東京, 一致–合う, 一致–偶然, 一体–全体, ヨーロッパ–欧州,
  メモ–手紙, 一般–共通, ワイン–酒, ワイン–お酒 and メモ–記事;
- conservative: 不安–緊張, 不安–はらはら, 一生–命, 一人一人–個人, 不自由–制限, 下り–降りる, 下り–坂, 一言–要するに, 一方–方,
  一度に–同時, メンバー–委員, メモ–記録, メモ–栞, ラケット–道具, 一般–いつも, 一般–たいてい and 一般–普段;
- a retained harmless over-guard: メンバー–参加.

Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.

The candidate was signed and pushed before review. The blind facet-split review raised the following:
- correctness: one minor finding: 一人一人's comparison with 個人 made sequential order («по очереди») part of the word's
  meaning;
- consistency: two minor quiz-safety findings: ワイン had no guard against its hypernym 酒, and ラケット none against the
  generic 道具;
- comprehensibility: one moderate finding, 一般's «рядовой; всеобщий» and «посторонние посетители» did not teach the
  card's sense; and five minor findings: 不正's unqualified «злоупотребление», 一層's particle «тем более», 上京's «Я
  переехал», ロケット's reliance on English rocket and locket, and メモ's «пометка; записать для памяти».

One signed fix commit addressed them:
- 一人一人's comparison now says the word singles out each member «не обязательно задавая порядок»;
- ワイン excludes 酒 and お酒, and ラケット excludes 道具 as a conservative guard;
- 一般's title became «общий; обычный», its example says «обычные посетители», 一般的な is glossed «общий; типичный», and it
  also excludes 共通, いつも, たいてい and 普段;
- 不正's title became «нечестность; неправильность», and 一層's «ещё сильнее; ещё больше» (also an optional correctness item);
- 上京's example says «Я поехал в Токио», and ロケット explains the shared spelling through katakana's single ラ row for
  English «р» and «л»;
- メモ's title became «записка; заметка», the body follows, the English memorandum equation was dropped, and it excludes 記事;
- one optional item was adopted: ラケット's example says «Одолжите» for 貸してください.

The serial rechecks reported all facets clean. Links follow EN, with eleven RU-only links to existing cards at a substantive comparison or mention:
不足–欠ける, 不安–緊張, 下り–下りる, 上京–東京, 一致–合う, 一生–命, 一体–全体, 一人一人–個人, ヨーロッパ–欧州, メンバー–委員 and
メモ–手紙. ワイン's EN link to ビール stays plain until ビール lands in Batch221.

Qualified progress is **4,719 reviewed-current / 8 reviewed runtime-blocked / 3,551 pending of 8,278**,
with 3,253 words, 718 kanji and 718 strokes. See the [intake](translation-batches/220-words-batch-59-intake.json),
[independent review](translation-batches/220-words-batch-59-independent-review-001.md),
[recheck](translation-batches/220-words-batch-59-recheck-001.md),
[qualified source record](translation-batches/220-words-batch-59-reviewed-source.json) and
[final validation](translation-batches/220-words-batch-59-final-validation-001.json).

## Previous published source milestone: batch219 thirty words (general word queue)

Batch219 adds 30 Russian word articles: 以前 代表 代理 付き合い 仏 今後 今回 今にも 人込み 人種 人生 人工 交際 互い 事実
事務 予算 予測 予報 乗客 乗せる 主要 主義 主張 主婦 主に 中止 中学 丘 世間. They are chunk 11 of 72 of the general
remaining-word queue, recomputed after Batch207 from 2,157 remaining EN words. Their dependency closure is exactly the 30
requested words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word.

Navigation-only link wraps restore 23 links at EN link positions in 18 files: 15 existing word pages and the kanji pages
互, 仏 and 務. The kanji 丘, 測, 算, 張 and 義 remain plain labels because they have no RU card.

The batch covers:
- "before; formerly" (以前), "from now on" (今後), "this time" (今回) and "at any moment" (今にも);
- representatives and typical examples (代表), acting for someone (代理), social contact (付き合い), association and
  dating (交際) and "each other" (互い);
- the Buddha (仏), crowds of people (人込み), race (人種), a person's life (人生) and "artificial" (人工);
- facts (事実), clerical work (事務), budgets (予算), forecasting (予測) and announced forecasts (予報);
- passengers (乗客) and giving a ride or placing something on top (乗せる);
- "main" (主要), principles and doctrines (主義), assertions (主張), housewives (主婦) and "mainly" (主に);
- cancellation (中止), lower secondary school (中学), hills (丘) and the people around one (世間).

All 20 EN exclusions are retained. Thirty-eight direct guards on 18 new cards cover the reviewed RU title overlaps and
sense neighbours:
- required: 以前–先, 以前–過去, 今にも–もうすぐ, 代表–典型, 代理–代わり, 付き合い–関係, 付き合い–仲, 人生–生命, 今回–度,
  今回–場合, 人込み–混雑, 主張–見解, 主に–大半, 主に–大部分 and 事務–仕事;
- conservative: 以前–元, 以前–まず, 今後–将来, 今後–先, 今にも–今に, 人生–生, 人生–生活, 交際–関係, 交際–恋, 交際–仲,
  交際–連絡, 予測–予期, 予測–読み, 予測–天気予報, 主要–要点, 主義–思想, 主張–要求, 主に–主要, 中止–止める, 中止–止む,
  世間–人, 世間–周囲 and 世間–環境.

Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.

The candidate was signed and pushed before review. The blind facet-split review raised the following:
- correctness: three minor findings: 主義's example used «изменить» with the dative, which means betraying one's
  principles; 今にも's comparison claimed that 今に cannot describe an imminent event; and 人込み's title «толчея» is
  colloquial and implies jostling;
- consistency: no finding; its optional 世間–人 guard was adopted, and an unconfirmed strokes hash limit was withdrawn by
  evidence (CRLF stroke blobs are hashed after LF normalisation, and the batch touches no stroke file);
- comprehensibility: one moderate finding, 代表's «представительство» ordinarily names a representative office and the
  代わり card uses it for 代理; and two minor findings: 人込み's «толчея» repeated 混雑's «давка» without a contrast,
  and 世間's «общественность» names the active part of society rather than people generally.

One signed fix commit resolved them:
- 主義's example now reads «Он не изменил свои принципы.»;
- 今にも's comparison now says that 今に by itself does not emphasise immediacy as 今にも does;
- 人込み's title became «толпа людей», and a new paragraph contrasts 大勢 (a number of people, not density) and 混雑
  (overcrowding of a place, transport or road);
- 代表's title became «представитель; характерный образец», and the definition names both senses;
- 世間's title became «окружающие люди; люди вообще», its news example now says «всеобщее внимание», and it also
  excludes 人, 周囲 and 環境;
- two optional items were adopted: 予測's title replaces colloquial «оценка наперёд» with «предварительная оценка», and
  主婦's example says «не занималась оплачиваемой работой».

The serial rechecks reported all facets clean. Links follow EN, with eight RU-only links to existing cards at a
substantive comparison: 主に–だけ, 予報–天気予報, 事務–事務所, 今にも–今に, 今回–最近, 代理–本人, 人込み–大勢 and
人込み–混雑. 以来's held EN link to 今後 is restored. 世間's EN link to 世の中 stays plain until 世の中 lands in
Batch220.

Qualified progress is **4,689 reviewed-current / 8 reviewed runtime-blocked / 3,581 pending of 8,278**,
with 3,223 words, 718 kanji and 718 strokes. See the [intake](translation-batches/219-words-batch-58-intake.json),
[independent review](translation-batches/219-words-batch-58-independent-review-001.md),
[recheck](translation-batches/219-words-batch-58-recheck-001.md),
[qualified source record](translation-batches/219-words-batch-58-reviewed-source.json) and
[final validation](translation-batches/219-words-batch-58-final-validation-001.json).

## Previous published source milestone: batch218 thirty words (general word queue)

Batch218 adds 30 Russian word articles: 倒す 修理 修正 信じる 信用 信頼 保証 価値 例え 作物 作法 作曲 作品 余分 何時か
何とか 何でも 何で 体育 住民 住宅 伝統 会員 休暇 休憩 企業 任せる 仲間 仲 以来. They are chunk 10 of 72 of the general
remaining-word queue, recomputed after Batch207 from 2,157 remaining EN words. Their dependency closure is exactly the 30
requested words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word.

Navigation-only link wraps restore 31 links at EN link positions in 26 files: 23 existing word pages and the kanji pages
仲, 信 and 疑. The kanji 企, 価, 保, 修, 憩, 暇, 統 and 証 remain plain labels because they have no RU card.

The batch covers:
- knocking down and defeating (倒す), repair (修理) and correction (修正);
- believing (信じる), trust and credit (信用), reliance (信頼), guarantees (保証) and value (価値);
- examples and figurative comparisons (例え), crops (作物), etiquette (作法), composing music (作曲) and works (作品);
- surplus (余分), "some time" (何時か), "somehow" (何とか), "anything" (何でも) and "why; by what means" (何で);
- physical education (体育), residents (住民), housing (住宅), tradition (伝統) and members (会員);
- leave (休暇), rest breaks (休憩), enterprises (企業) and entrusting (任せる);
- companions (仲間), relations between people (仲) and "since" (以来).

All 28 EN exclusions are retained. Twelve direct guards on 12 new cards cover the reviewed RU title overlaps and sense
neighbours:
- required: 倒す–勝つ, 修正–直す, 作法–礼儀, 作品–曲, 住宅–自宅, 休暇–夏休み, 休憩–昼休み, 例え–比較 and 任せる–頼む;
- conservative: 住民–人口, 仲間–友達 and 会員–仲間.

Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.

The candidate was signed and pushed before review. The blind facet-split review raised the following:
- correctness: one scoped-coverage finding: 余分's reading join turned EN's hiragana よ + ぶん into katakana;
- consistency: two quiz-safety findings, missing guards for 例え–比較 and 任せる–頼む, plus a strokes manifest-hash note
  withdrawn by evidence (CRLF stroke blobs are hashed after LF normalisation);
- comprehensibility: two findings: 休憩's title offered «антракт» as an unqualified equal gloss, and 何とか's example used
  «кое-как», which can also mean «небрежно».

Three signed fix commits resolved them:
- 余分 again joins よ + ぶん;
- 休憩's title became «перерыв на отдых; антракт (в спектакле, концерте)», and its nuance section explains that neutral
  speech says «перерыв» at a meeting or on a journey, where «антракт» sounds conversational (the second fix, after the
  correctness recheck found the first wording too categorical);
- 何とか's example now reads «Я спешил и с трудом, но успел вовремя.»;
- 例え excludes 比較 and 任せる excludes 頼む;
- three optional conservative guards were adopted: 住民–人口, 仲間–友達 and 会員–仲間;
- 以来's warning now names the dictionary rendering «отныне» it qualifies (an adopted optional item); the third fix
  removed an English gloss that this wording had added in parentheses, after the comprehensibility recheck.

The serial rechecks reported all facets clean. Links follow EN, with two RU-only links to existing cards at a substantive
comparison: 倒す–勝つ and 修正–直す. 以来's EN link to 今後 stays plain until 今後 lands in Batch219.

Qualified progress is **4,659 reviewed-current / 8 reviewed runtime-blocked / 3,611 pending of 8,278**,
with 3,193 words, 718 kanji and 718 strokes. See the [intake](translation-batches/218-words-batch-57-intake.json),
[independent review](translation-batches/218-words-batch-57-independent-review-001.md),
[recheck](translation-batches/218-words-batch-57-recheck-001.md),
[qualified source record](translation-batches/218-words-batch-57-reviewed-source.json) and
[final validation](translation-batches/218-words-batch-57-final-validation-001.json).

## Previous published source milestone: batch217 thirty words (general word queue)

Batch217 adds 30 Russian word articles: 刀 出会い 出 処理 凍る 冗談 冒険 再び 円 具体 共通 共に 公平 全国 全員 全て 全
全体 党 免許 克服 先日 優勝 優れる 僅か 傷 健康 停留所 借金 候補. They are chunk 9 of 72 of the general
remaining-word queue, recomputed after Batch207 from 2,157 remaining EN words. Their dependency closure is exactly the 30
requested words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word.

Navigation-only link wraps restore 29 links at EN link positions in 24 files: 19 existing word pages and the kanji pages
停, 党, 再, 凍 and 処. The kanji 健, 傷, 僅, 克, 免, 冒, 冗, 刀, 康 and 補 remain plain labels because they have no RU card.

The batch covers:
- swords (刀), encounters (出会い), origin, graduates and outflow (出), and processing or handling (処理);
- freezing (凍る), jokes (冗談), adventure (冒険) and "once again" (再び);
- circles and yen (円), concreteness (具体), being shared in common (共通) and together or both (共に);
- fairness (公平), the whole country (全国), everyone in a group (全員), everything (全て), the prefix "all" (全) and
  the whole (全体);
- political parties (党), licences (免許), overcoming (克服) and "the other day" (先日);
- winning a championship (優勝), excelling (優れる), slightness (僅か), wounds and scratches (傷) and health (健康);
- bus and tram stops (停留所), debt (借金) and candidates (候補).

All 27 EN exclusions are retained. Eleven direct guards on 8 new cards cover the reviewed RU title overlaps and sense
neighbours:
- required: 全て–皆, 先日–このあいだ and 共に–両方;
- conservative: 優勝–勝ち, 出会い–会合, 出会い–会, 出会い–迎え, 処理–解決, 処理–治める, 借金–貸し and 共通–同じ.

Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.

The candidate was signed and pushed before review. The blind facet-split review raised the following:
- correctness: one finding: 克服's definition named an ability («способность взять её под контроль») rather than the act;
- consistency: three quiz-safety findings, missing guards for 共に–両方, 出会い–会合/紹介 and 処理–解決, plus a strokes
  manifest-hash note withdrawn by evidence (CRLF stroke blobs are hashed after LF normalisation);
- comprehensibility: one finding: 出会い's title «встреча и знакомство» equated every encounter with an acquaintance.

Two signed fix commits resolved them:
- 克服 now reads «преодоление трудности, взятие её под контроль»;
- 出会い's title became «встреча (с человеком или чем-либо)», with four glosses aligned; it excludes 会合, 会 and 迎え,
  and not 紹介, whose shared «знакомство» the retitle removed;
- 共に excludes 両方, and 処理 excludes 解決 and 治める;
- two optional conservative guards were adopted: 借金–貸し and 共通–同じ.

The serial rechecks reported all facets clean. Links follow EN, with three RU-only links to existing cards at a substantive
comparison: 円–丸, 先日–このあいだ and 借金–借りる.

Qualified progress is **4,629 reviewed-current / 8 reviewed runtime-blocked / 3,641 pending of 8,278**,
with 3,163 words, 718 kanji and 718 strokes. See the [intake](translation-batches/217-words-batch-56-intake.json),
[independent review](translation-batches/217-words-batch-56-independent-review-001.md),
[recheck](translation-batches/217-words-batch-56-recheck-001.md),
[qualified source record](translation-batches/217-words-batch-56-reviewed-source.json) and
[final validation](translation-batches/217-words-batch-56-final-validation-001.json).

## Previous published source milestone: batch216 thirty words (general word queue)

Batch216 adds 30 Russian word articles: 勧める 勢い 勝ち 勘 動詞 勇気 効く 助手 劣る 加わる 劇場 劇 割る 前者 刺激
制度 到着 利益 別れ 別に 列車 列 刑事 刈る 切れる 切れ 分野 分析 分ける 分. They are chunk 8 of 72 of the general
remaining-word queue, recomputed after Batch207 from 2,157 remaining EN words. Their dependency closure is exactly the 30
requested words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word.

Navigation-only link wraps restore 37 links at EN link positions in 23 files: 14 existing word pages and the kanji pages
列, 到, 制, 割, 劇, 刺, 効, 勇 and 勢. The kanji 刈, 刑, 劣, 勘, 勧, 析, 激, 益 and 詞 remain plain labels because they
have no RU card.

The batch covers:
- recommending (勧める), momentum (勢い), a win (勝ち), intuition (勘), verbs (動詞) and courage (勇気);
- taking effect (効く), assistants (助手), being inferior (劣る) and joining (加わる);
- theatres (劇場), plays (劇), splitting and dividing (割る) and the former of two (前者);
- stimuli (刺激), institutional systems (制度), arrival (到着) and profit (利益);
- partings (別れ) and "not particularly" or separately (別に);
- railway trains (列車), rows and queues (列), police detectives (刑事) and mowing or reaping (刈る);
- snapping, running out and cutting well (切れる), and pieces and sharpness (切れ);
- fields of activity (分野), analysis (分析), dividing and sharing out (分ける), and fractional units and portions (分).

All 13 EN exclusions are retained. Twenty-four direct guards on 15 new cards cover the reviewed RU title overlaps and
sense neighbours:
- required: 劣る–負ける, 加わる–加える, 劇–芝居, 割る–分ける, 到着–着く, 別れ–別れる, 別に–あまり, 別に–別, 列–順番,
  列–番, 切れる–切る and 分析–検査;
- conservative: 勧める–推薦, 勧める–提案, 効く–効果, 劣る–譲る, 加わる–足す, 劇–公演, 制度–機関, 別に–特に, 列車–汽車,
  刑事–警官, 切れる–破る and 切れる–終わる.

Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.

The candidate was signed and pushed before review. The blind facet-split review raised the following:
- correctness: no finding;
- consistency: two findings, a missing 切れる–終わる guard («кончаться (о запасе)» against «заканчиваться») and a
  harmless over-guard 劇–劇場;
- comprehensibility: four findings: 分's title began with «бу», a Cyrillic transliteration of its reading; 助手 had no
  contrast with 手伝い, whose title shares «помощник»; 到着 and 前者 rendered 電車 as «электричка»; and 刈る's haircut
  sentence was a calque that showed no contrast.

One signed fix commit resolved them:
- 切れる now excludes 終わる, and 劇 no longer excludes 劇場;
- 分's title became «дробная единица; чья-либо часть»;
- 助手 now contrasts the help itself (手伝い) with the person who assists another in work;
- 到着 and 前者 say «электропоезд», as the 電車 card does;
- 刈る presents 髪を切る as the ordinary «подстричь волосы» and frames 刈る as cropping grown material.

The serial rechecks reported all facets clean. Links follow EN, with four RU-only links to existing cards at a substantive
comparison: 到着–着く, 分–部分, 分ける–分かる and 列–順番.

Qualified progress is **4,599 reviewed-current / 8 reviewed runtime-blocked / 3,671 pending of 8,278**,
with 3,133 words, 718 kanji and 718 strokes. See the [intake](translation-batches/216-words-batch-55-intake.json),
[independent review](translation-batches/216-words-batch-55-independent-review-001.md),
[recheck](translation-batches/216-words-batch-55-recheck-001.md),
[qualified source record](translation-batches/216-words-batch-55-reviewed-source.json) and
[final validation](translation-batches/216-words-batch-55-final-validation-001.json).

## Previous published source milestone: batch215 thirty words (general word queue)

Batch215 adds 30 Russian word articles: 名人 同時 同僚 合わせる 叱る 可能 可 取れる 取り上げる 収穫 収入 双子 友情 及ぼす
参考 参加 原 印刷 占める 博物館 博士 単位 単に 単なる 共同 協力 医療 医師 化粧 化学. They are chunk 7 of 72 of the general
remaining-word queue, recomputed after Batch207 from 2,157 remaining EN words. Their dependency closure is exactly the 30
requested words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word.

Navigation-only link wraps restore 45 links at EN link positions in 31 files: 21 existing word pages and the kanji pages
共, 刊, 刷, 加, 協, 占, 印, 参, 双 and 収. The kanji 僚, 博, 及, 可, 叱, 士, 療, 穫 and 粧 remain plain labels because they
have no RU card.

The batch covers:
- masters of a craft (名人) and doctors and experts (博士);
- the same time (同時), colleagues (同僚) and friendship (友情);
- fitting and combining (合わせる) and scolding (叱る);
- possibility (可能) and a passing grade (可);
- coming off (取れる) and confiscating or taking up a topic (取り上げる);
- harvests and results (収穫), income (収入) and twins (双子);
- exerting an influence (及ぼす), reference material (参考) and participation (参加);
- open fields and plains (原), printing (印刷) and occupying a share (占める);
- museums (博物館);
- units and academic credits (単位), merely (単に) and mere (単なる);
- joint work (共同) and cooperation (協力);
- medical care (医療), physicians (医師), make-up (化粧) and chemistry (化学).

All 9 EN exclusions are retained. Seven direct guards on six new cards cover the reviewed RU title overlaps and sense
neighbours:
- required: 原–野, 博物館–美術館, 及ぼす–影響 and 単なる–単に;
- conservative: 叱る–注意, 単に–だけ and 単に–ばかり.

Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.

The candidate was signed and pushed before review. The blind facet-split review raised the following:
- correctness: one finding (化粧 dropped EN's statement that け + しょう are on readings) and one verification limit. No
  Russian dictionary headword was found for 単位's «зачётная единица»; Order No. 245 of the Russian Ministry of Science
  and Higher Education closed it substantively;
- consistency: no finding;
- comprehensibility: two findings, the English abbreviation «(PhD)» in 博士 and 単に's ambiguous gloss «исключительно».

One signed fix commit resolved them:
- 単に became «просто (не более того); всего лишь», with conservative guards to だけ and ばかり;
- 化粧 now says «Онные чтения»;
- 博士 dropped the abbreviation;
- 共同 took parenthesised readings.

The serial rechecks reported all facets clean. Links follow EN; the batch adds no RU-only link.

Qualified progress is **4,569 reviewed-current / 8 reviewed runtime-blocked / 3,701 pending of 8,278**,
with 3,103 words, 718 kanji and 718 strokes. See the [intake](translation-batches/215-words-batch-54-intake.json),
[independent review](translation-batches/215-words-batch-54-independent-review-001.md),
[recheck](translation-batches/215-words-batch-54-recheck-001.md),
[qualified source record](translation-batches/215-words-batch-54-reviewed-source.json) and
[final validation](translation-batches/215-words-batch-54-final-validation-001.json).

## Previous published source milestone: batch214 thirty words (general word queue)

Batch214 adds 30 Russian word articles: 地平線 地区 地下 土産 土曜 国語 国民 国家 国境 国会 図 囲む 回す 器用 善 商売
商品 商人 唯一 哲学 品 呼吸 味方 周囲 吸収 加える 含む 否定 向かい 吐く. They are chunk 6 of 72 of the general remaining-word
queue (recomputed after Batch207: 2,157 EN words remaining); the dependency closure is exactly the 30 requested words, so every
EN quiz_exclusions target resolves to an existing RU word or a batch word. Ten existing word pages and the kanji pages 区, 否,
含, 周 and 囲 receive 22 navigation-only link wraps at EN link positions. 線, 境, 器, 善, 唯, 哲 and 吐 remain plain labels
because those kanji have no RU card.

The batch covers the horizon over land (地平線), districts (地区), the underground and basements (地下), souvenir gifts
(土産), Saturday (土曜), the national language and the school subject (国語), the people of a nation (国民), the state
(国家), national borders (国境), the Diet (国会), diagrams (図), surrounding (囲む), turning and passing round (回す),
dexterity (器用), moral good (善), trade (商売), goods and articles (商品, 品), merchants (商人), the only one (唯一),
philosophy (哲学), breathing (呼吸), allies (味方), surroundings (周囲), absorption (吸収), adding and including (加える,
含む), denial (否定), the place opposite (向かい) and breathing out and vomiting (吐く). All 28 EN exclusions are retained;
ten direct guards on eight new cards cover the reviewed RU title overlaps and sense
neighbours: 土曜–土曜日, 地区–町 and 地区–辺 (required), 土産–祝い and 商売–貿易 (likely required), 地区–近所, 商人–店員,
国語–科目, 善–道徳 and 吸収–夢中 (conservative).
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
The candidate was committed signed and pushed before review. The blind facet-split review found one correctness
finding (地区's «округ» narrowed the ordinary district sense), no consistency finding and eight comprehensibility
findings (図 introduced with 絵's «рисунок»; 国語 glosses repeating 日本語's title; 囲む dropping what テーブルを marks;
an author-facing sentence in 品; a broken ateji sentence in 味方; «дух» as a gloss of 息 in 呼吸; 周囲 calling 回り the
area around; an opaque restriction sentence in 国境). One signed fix commit resolved them: 地区 became «район; выделенная
зона» with 町, 辺 and 近所 guards, 図 now uses «схема» and the other passages were reworded; 哲学 and 土産 took optional
polish. A second signed commit linked 周囲's RU-introduced 周り and 環境 comparisons to the existing cards after the
correctness recheck noted that the content-structure rules call for links at a substantive comparison. The serial
rechecks reported all facets clean.
Apart from those two 周囲 links, links follow EN.

Qualified progress is **4,539 reviewed-current / 8 reviewed runtime-blocked / 3,731 pending of 8,278**,
with 3,073 words, 718 kanji and 718 strokes. See the [intake](translation-batches/214-words-batch-53-intake.json),
[independent review](translation-batches/214-words-batch-53-independent-review-001.md),
[recheck](translation-batches/214-words-batch-53-recheck-001.md),
[qualified source record](translation-batches/214-words-batch-53-reviewed-source.json) and
[final validation](translation-batches/214-words-batch-53-final-validation-001.json).

## Previous published source milestone: batch213 thirty words (general word queue)

Batch213 adds 30 Russian word articles: 夫婦 夫人 大部分 大臣 大統領 大戦 大家 大半 大使 大会 大 夢中 夜明け 夜中 外交 外す
夕べ 売れる 墓 境 塔 塀 報告 よる 基づく 城 埃 地球 地域 地方. They are chunk 5 of 72 of the general remaining-word queue
(recomputed after Batch207: 2,157 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Thirteen existing word pages and the kanji pages 告,
城, 域, 報, 塔, 夫, 婦 and 球 receive 35 navigation-only link wraps at EN link positions. 臣, 統, 領, 墓, 境, 塀, 基 and 埃
remain plain labels because those kanji have no RU card.

The batch covers married couples and wives (夫婦, 夫人), the greater part and majority (大部分, 大半), ministers,
presidents and ambassadors (大臣, 大統領, 大使), great wars (大戦), landlords (大家), conventions and tournaments (大会),
the prefix and size 大 (大), absorption (夢中), dawn and the dead of night (夜明け, 夜中), diplomacy (外交), taking off
and unfastening (外す), evenings (夕べ), selling well (売れる), graves (墓), boundaries and turning points (境), towers (塔),
fences (塀), reports (報告), depending on and being based on (よる, 基づく), castles (城), dust (埃), the Earth (地球) and
regions and the provinces (地域, 地方). All 18 EN exclusions are retained; fifteen direct guards on nine new cards cover
the reviewed RU title overlaps and sense neighbours: 大部分–ほとんど, 大部分–たいてい, 大半–ほとんど, 大半–たいてい,
大–莫大, 大–巨大, 大–大小, 夢中–熱中, 外す–下ろす, 報告–リポート, よる–次第 and 地方–州 (required), 境–瞬間, 報告–知らせる
and 報告–伝える (conservative). Exclusions are one-sided declarations that Android applies in both directions; the batch
changes exclusions only on its new cards.
The candidate was committed signed and pushed before review. The blind facet-split review found no correctness finding,
one consistency finding (a missing 大–巨大 guard) and three comprehensibility findings (地方's sentence rejecting an
English gloss; 大統領's vocative rendered as praise; 大部分 not separated from ほとんど). One signed fix commit resolved
them: it added the guard, deleted the 地方 sentence, rendered the 大統領 vocative as «шеф!» or «дружище!» and added a
plain-text ほとんど contrast that denies 大部分 only the negative «почти не». No RU-only links were added. The serial
rechecks reported all facets clean.

Qualified progress is **4,509 reviewed-current / 8 reviewed runtime-blocked / 3,761 pending of 8,278**,
with 3,043 words, 718 kanji and 718 strokes. See the [intake](translation-batches/213-words-batch-52-intake.json),
[independent review](translation-batches/213-words-batch-52-independent-review-001.md),
[recheck](translation-batches/213-words-batch-52-recheck-001.md),
[qualified source record](translation-batches/213-words-batch-52-reviewed-source.json) and
[final validation](translation-batches/213-words-batch-52-final-validation-001.json).

## Previous published source milestone: batch212 thirty words (general word queue)

Batch212 adds 30 Russian word articles: 完全 完了 宇宙 宅 孫 学者 学ぶ 学習 学期 学 学問 存在 嫌う 嫁 婚約 姿 委員 奇妙
不思議 妙 好み 女王 俳優 女優 奪う 奨学金 奥 契約 失業 失う. They are chunk 4 of 72 of the general remaining-word queue
(recomputed after Batch207: 2,157 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Fifteen existing word pages and the kanji pages 了,
在, 奥, 存, 孫 and 宇 receive 31 navigation-only link wraps at EN link positions, including the three links held in Batch211's
完成 and 専攻. 宙, 嫌, 嫁, 姿, 委, 奇, 妙, 俳, 奪, 奨 and 契 remain plain labels because those kanji have no RU card.

The batch covers completeness and completion (完全, 完了), the universe (宇宙), homes (宅), grandchildren (孫), learning,
study and scholarship (学者, 学ぶ, 学習, 学期, 学, 学問, 奨学金), existence (存在), dislike (嫌う), brides and
daughters-in-law (嫁), engagement (婚約), figure and appearance (姿), committee members (委員), the strange and mysterious
(奇妙, 不思議, 妙), personal taste (好み), queens (女王), actors and actresses (俳優, 女優), taking away (奪う), the inner
depths of places (奥), contracts (契約), unemployment (失業) and losing things (失う). All 32 EN exclusions are retained;
sixteen direct guards on nine new cards cover the reviewed RU title overlaps and sense neighbours: 完全–全く, 完全–全然,
完全–一杯, 完了–完成, 完了–仕舞い, 宅–お宅, 学者–研究者, 存在–ある, 嫌う–避ける and 不思議–謎 (required), 完全–太い,
完了–終わる, 完了–終える, 完了–済む, 妙–奇しい and 好み–好む (conservative). Exclusions are one-sided declarations that
Android applies in both directions; the batch changes exclusions only on its new cards.
The candidate was committed signed and pushed before review. The blind facet-split review found no correctness finding,
one consistency finding (a missing 完全–全然 guard) and two comprehensibility findings (完全's title keeping only the
quality sense; 学習's title naming institutional instruction). One signed fix commit resolved them, retitled 完全 «полный
(без изъянов); совершенный» and 学習 «учёба; процесс изучения», added the 一杯 and 太い guards for the new «полный» segment
and adopted three optional notes (好み «предпочтение; личный вкус», 学者, 奥). No RU-only links were added. The serial
rechecks reported all facets clean.

Qualified progress is **4,479 reviewed-current / 8 reviewed runtime-blocked / 3,791 pending of 8,278**,
with 3,013 words, 718 kanji and 718 strokes. See the [intake](translation-batches/212-words-batch-51-intake.json),
[independent review](translation-batches/212-words-batch-51-independent-review-001.md),
[recheck](translation-batches/212-words-batch-51-recheck-001.md),
[qualified source record](translation-batches/212-words-batch-51-reviewed-source.json) and
[final validation](translation-batches/212-words-batch-51-final-validation-001.json).

## Previous published source milestone: batch211 thirty words (general word queue)

Batch211 adds 30 Russian word articles: 少女 小麦 小屋 包み 小包 小 専攻 対象 対 審判 密 寄付 宿 宿泊 家賃 家具 実験 実施
実行 実現 実は 宝石 宝 宜しく パス 券 定期 信仰 宗教 完成. They are chunk 3 of 72 of the general remaining-word queue
(recomputed after Batch207: 2,157 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Seven existing word pages, the kanji pages 券, 包, 完,
宝, 専 and 成 and the article numbers-and-counters receive 24 navigation-only link wraps at EN link positions; in 少年 the
comparison gloss for 少女 was also aligned with the new card. 麦, 攻, 象, 審, 密, 泊, 賃, 施, 宜, 仰 and 宗 remain plain labels
because those kanji have no RU card.

The batch covers young girls (少女), wheat (小麦), huts and sheds (小屋), wrapped bundles and parcels (包み, 小包), small size
(小), a university major (専攻), targets and objects of attention (対象), "versus" and score ratios (対), verdicts, umpiring and
judges (審判), density and close ties (密), donations (寄付), lodgings and overnight stays (宿, 宿泊), rent (家賃), furniture
(家具), experiments (実験), holding events and putting rules into effect (実施), carrying out plans (実行), realization (実現),
"actually" (実は), gems and treasure (宝石, 宝), "best regards" requests (宜しく), the two katakana words パス (a pass and a
file path), tickets and coupons (券), fixed terms, schedules and commuter passes (定期), religious faith and religion (信仰,
宗教) and completion (完成). All 25 EN exclusions are retained; eight direct guards on eight new cards cover the reviewed RU
title overlaps and sense neighbours: 密–近い, 宿泊–泊まる, 実施–行う, 完成–仕舞い and 少女–女子 (required), 宿–泊まる,
実行–行う and 実現–実行 (conservative). Exclusions are one-sided declarations that Android applies in both directions; the
batch changes exclusions only on its new cards.
The candidate was committed signed and pushed before review. The blind facet-split review found four correctness findings
(包み's wrapping boundary for 荷物; 宝石's examples using 石's bare «камень»; 少女's title omitting childhood; パス's title omitting
the admission pass and passing a turn), no consistency or quiz-safety finding, and five comprehensibility findings (パス's
English-dependent pass/path split, 実行's examples not contrasting with 実現, 定期's English "regular" comparison, 宝石's
glosses, and source-list clauses in 少女, 対 and 密). One signed fix commit resolved them, retitled 小包 «посылка» on
dictionary evidence and added the 少女–女子 guard; the source-list notes in 対 and 密 mirror EN and the published series,
so that part of the finding was withdrawn. No RU-only links were added. The serial rechecks reported all facets clean.

Qualified progress is **4,449 reviewed-current / 8 reviewed runtime-blocked / 3,821 pending of 8,278**,
with 2,983 words, 718 kanji and 718 strokes. See the [intake](translation-batches/211-words-batch-50-intake.json),
[independent review](translation-batches/211-words-batch-50-independent-review-001.md),
[recheck](translation-batches/211-words-batch-50-recheck-001.md),
[qualified source record](translation-batches/211-words-batch-50-reviewed-source.json) and
[final validation](translation-batches/211-words-batch-50-final-validation-001.json).

## Previous published source milestone: batch210 thirty words (general word queue)

Batch210 adds 30 Russian word articles: 年間 年月 年寄り 年代 いつでも 常に 年中 平等 平均 平和 幕 常識 帰宅 帯 差別 巨大
巣 大陸 州 嵐 岩 屋根 届く 居間 居眠り 居る 就職 就く ボーイ 少年. They are chunk 2 of 72 of the general remaining-word queue
(recomputed after Batch207: 2,157 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Fifteen existing word pages and the kanji pages 和, 均,
居, 州, 帯, 平 and 等 receive 35 navigation-only link wraps at EN link positions; 幕, 巨, 巣, 陸, 嵐, 岩, 根, 届 and 就 remain
plain labels because those kanji have no RU card.

The batch covers spans of years and eras (年間, 年月, 年代), the whole year round (年中), elderly people (年寄り), "any time"
and "always" (いつでも, 常に), equality (平等), averages (平均), peace (平和), stage curtains and acts (幕), common sense
(常識), returning home (帰宅), kimono sashes and long narrow strips (帯), discrimination (差別), huge size (巨大), nests (巣),
continents (大陸), states and provinces (州), storms (嵐), rocks (岩), roofs (屋根), reaching and being delivered (届く), living
rooms (居間), dozing (居眠り), humble "be" (居る), getting a job (就職), taking up a post or studying under a teacher (就く),
boys and hotel or restaurant staff (ボーイ) and boys and minors (少年). All 26 EN exclusions are retained; fourteen direct
guards on nine new cards cover the reviewed RU title overlaps and sense neighbours: 年寄り–老人, 平和–世界, 帰宅–帰る,
居る–いらっしゃる, 居る–おいでになる, 就く–習う, 就く–就職 and 屋根–屋上 (required), 帰宅–帰り, 平等–等しい,
居眠り–うとうと, 就く–座る, 帯–縞 and 帯–筋 (conservative). Exclusions are one-sided declarations that Android applies in both
directions; the batch changes exclusions only on its new cards.
The candidate was committed signed and pushed before review. The blind facet-split review found four correctness findings
(差別 «по национальности» read as ethnicity; 居眠り's title made unintendedness lexical; 帯 «опоясывающая» narrowed the strip
sense; 岩 omitted EN's ロック note), one quiz-safety finding (屋根 «крыша» also names the rooftop of 屋上) and five
comprehensibility findings (居る's English «-masu» label, 帯's expanded provenance passage, 居眠り «не спите», 年寄り quoting
老人's quiz title, and 就職's source-list note). One signed fix commit resolved them, partially for 帯's passage, which now
mirrors EN's single sentence; 就職's note was kept as in EN and the published series. The fix also dropped the author's
conservative 居る–参る guard. No RU-only links were added. The serial rechecks reported all facets clean, with the 帯 and
就職 remainders optional.

Qualified progress is **4,419 reviewed-current / 8 reviewed runtime-blocked / 3,851 pending of 8,278**,
with 2,953 words, 718 kanji and 718 strokes. See the [intake](translation-batches/210-words-batch-49-intake.json),
[independent review](translation-batches/210-words-batch-49-independent-review-001.md),
[recheck](translation-batches/210-words-batch-49-recheck-001.md),
[qualified source record](translation-batches/210-words-batch-49-reviewed-source.json) and
[final validation](translation-batches/210-words-batch-49-final-validation-001.json).

## Previous published source milestone: batch209 thirty words (general word queue)

Batch209 adds 30 Russian word articles: 心理 徹底 徹夜 微妙 得意 従兄弟 ですから 従って 従う 後者 役割 効果 影響 影 当時
当てる 当たる 弾 強調 強盗 強力 引退 引用 引っ張る 弁当 座席 床 広告 幼い 年齢. They are chunk 1 of 72 of the general
remaining-word queue (recomputed after Batch207: 2,157 EN words remaining); the dependency closure is exactly the 30 requested
words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Sixteen existing word pages and the
kanji pages 効, 幼, 当 and 得 receive 27 navigation-only link wraps at EN link positions; 妙, 床, 底, 弁, 張, 弾, 影, 従, 微,
徹, 響 and 齢 remain plain labels because those kanji have no RU card.

The batch covers psychology and mentality (心理), thoroughness (徹底), staying up all night (徹夜), subtlety (微妙), strong
points (得意), cousins (従兄弟), "therefore" and "accordingly" (ですから, 従って), obeying and following (従う), "the latter"
(後者), roles (役割), effects and influence (効果, 影響), shadows (影), "at that time" (当時), hitting and being hit (当てる,
当たる), bullets (弾), emphasis (強調), robbery (強盗), power (強力), retirement (引退), quotation (引用), pulling (引っ張る),
boxed lunches (弁当), seats (座席), floors (床), advertising (広告), being very young (幼い) and age (年齢). All 25 EN exclusions
are retained; five direct guards on four new cards cover the reviewed RU title overlaps: 得意–武器, 影響–左右 and 床–性
(required), 効果–有効 and 影響–毒 (conservative). Exclusions are one-sided declarations that Android applies in both
directions; the batch changes exclusions only on its new cards.
Before the candidate, the coordinator retitled 得意 from «конёк; …» to «сильная сторона; хорошо удающееся дело», because
figurative «конёк» implies fondness that the card says 得意 does not assert, and guarded the new shared segment with 武器.
The candidate was committed signed and pushed before review. The blind facet-split review found one comprehensibility
problem: 得意's example added a superlative («Лучше всего…») that 得意な科目は数学です does not have. Correctness, scoped
coverage, consistency and quiz safety were clean. One signed fix commit corrected 得意 and adopted two optional notes
(引っ張る without a comparative, 年齢 as participation rather than registration); the correctness reviewer acknowledged that
its initial CLEAN had missed these. No RU-only links were added. The serial rechecks reported all facets clean.

Qualified progress is **4,389 reviewed-current / 8 reviewed runtime-blocked / 3,881 pending of 8,278**,
with 2,923 words, 718 kanji and 718 strokes. See the [intake](translation-batches/209-words-batch-48-intake.json),
[independent review](translation-batches/209-words-batch-48-independent-review-001.md),
[recheck](translation-batches/209-words-batch-48-recheck-001.md),
[qualified source record](translation-batches/209-words-batch-48-reviewed-source.json) and
[final validation](translation-batches/209-words-batch-48-final-validation-001.json).

## Previous published source milestone: batch208 thirty words (general word queue)

Batch208 adds 30 Russian word articles: 成績 成功 成人 憲法 慎重 感じる 感覚 感動 印象 感じ 意識 意外 悲劇 悲しむ 悪魔
悪戯 悪口 息 恐怖 恐ろしい 恐れる 性 急速 急激 思想 思い出 応じる 必死 必ずしも 心臓. They are chunk 0 of 72 of the general
remaining-word queue (recomputed after Batch207: 2,157 EN words remaining); the dependency closure is exactly the 30 requested
words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Ten existing word pages and the
kanji pages 劇, 印, 恐 and 息 receive 18 navigation-only link wraps at EN link positions; 績, 功, 憲, 慎, 象, 魔, 戯, 激, 応 and
臓 remain plain labels because those kanji have no RU card.

The batch covers performance and success (成績, 成功), adulthood (成人), the constitution (憲法), caution (慎重), feeling, sensation,
being moved and impressions (感じる, 感覚, 感動, 印象, 感じ), consciousness (意識), the unexpected (意外), tragedy and grief (悲劇,
悲しむ), devils, mischief and badmouthing (悪魔, 悪戯, 悪口), breath (息), fear (恐怖, 恐ろしい, 恐れる), sex and the suffix
-ness (性), rapid and sharp change (急速, 急激), thought and ideology (思想), memories (思い出), responding and agreeing (応じる),
desperation (必死), "not necessarily" (必ずしも) and the heart as an organ (心臓). All 19 EN exclusions are retained; 20 direct guards on
15 new cards cover the reviewed RU title overlaps, including 感じる–感じ, 急速–急激/急に, 悪魔–鬼, 応じる–返事/承知 and
心臓–心/胸. Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on
its new cards.
The candidate was committed signed and pushed before review. The blind facet-split review found that 必死's example asserted
only an attempt where Japanese reports actual restraint, that 息 omitted EN's "tone" boundary sentence, and three
comprehensibility problems: 思想 equated 近代 with «Новое время» against the published 近代 card, 急激 kept an English-dependent
aside about political views, and 悪戯 asserted damage where Japanese means tampering. Consistency and quiz safety were clean.
Three signed fix commits followed serial rechecks: the first recheck found that the new 必死 wording reused the title of the
excluded 一生懸命 and that the restored 息 sentence answered an English source-list gloss the RU card never presents, so
必死 now reads «отчаянно сдерживала» and 息 returned to the candidate text, with the correctness finding withdrawn on that
evidence. The coordinator then corrected a false basis for declining an optional note and added EN 評価's kana reading to
成績's RU-only 評価 example. No RU-only links were added. The records preserve the author's and reviewer's differing
required-versus-conservative classification of the RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **4,359 reviewed-current / 8 reviewed runtime-blocked / 3,911 pending of 8,278**,
with 2,893 words, 718 kanji and 718 strokes. See the [intake](translation-batches/208-words-batch-47-intake.json),
[independent review](translation-batches/208-words-batch-47-independent-review-001.md),
[recheck](translation-batches/208-words-batch-47-recheck-001.md),
[qualified source record](translation-batches/208-words-batch-47-reviewed-source.json) and
[final validation](translation-batches/208-words-batch-47-final-validation-001.json).

## Previous published source milestone: batch207 thirty words (general word queue)

Batch207 adds 30 Russian word articles: 不利 損 握手 握る 交換 両替 換える 提出 描く 掴む 掲示 推薦 捕まる 振る 指す
持ち上げる 抱く 抱える 抜ける 抜く 投票 批評 批判 扱う 手術 手品 戻す 或 我慢 我々. They are chunk 0 of 73 of the general
remaining-word queue (recomputed after Batch206: 2,187 EN words remaining); the dependency closure is exactly the 30 requested
words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Seven existing word pages and the
kanji pages 抜, 抱 and 術 receive 16 navigation-only link wraps at EN link positions; 損, 握, 換, 替, 提, 描, 掴, 掲, 推, 薦, 振,
票, 批, 評, 扱, 或, 我 and 慢 remain plain labels because those kanji have no RU card.

The batch covers disadvantage and loss (不利, 損), handshakes and gripping (握手, 握る), exchanging and changing money (交換,
両替, 換える), submitting (提出), drawing (描く), grasping (掴む), posted notices (掲示), recommendation (推薦), being caught
(捕まる), waving and shaking (振る), pointing (指す), lifting and flattering (持ち上げる), holding in one's arms (抱く, 抱える),
coming out and pulling out (抜ける, 抜く), voting (投票), critique and criticism (批評, 批判), handling (扱う), surgery (手術),
magic tricks (手品), putting back (戻す), "a certain" (或), endurance (我慢) and "we" (我々). All 19 EN exclusions are
retained; 6 direct guards beyond EN cover 交換–代わり/両替, 扱う–操作, 掴む–捕まえる/理解 and 持ち上げる–立てる.
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
The candidate was committed signed and pushed before review. The blind facet-split review found that 提出 defined the
submitted item instead of the act, katakana reading joins where EN has hiragana in 不利, 握手, 批評 and 批判, three missing quiz
guards (交換–両替, 掴む–捕まえる/理解, 持ち上げる–立てる), a misquoted 出す gloss, a 指す title teaching an untaught sense, and an
English-dependent aside in 手品 and a dictionary-markup note in 抱く. All were fixed in a signed fix commit without RU-only
links, and an optional clearer 不利 wording was adopted. The records preserve the author's and reviewer's differing
required-versus-conservative classification of the RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **4,329 reviewed-current / 8 reviewed runtime-blocked / 3,941 pending of 8,278**,
with 2,863 words, 718 kanji and 718 strokes. See the [intake](translation-batches/207-words-batch-46-intake.json),
[independent review](translation-batches/207-words-batch-46-independent-review-001.md),
[recheck](translation-batches/207-words-batch-46-recheck-001.md),
[qualified source record](translation-batches/207-words-batch-46-reviewed-source.json) and
[final validation](translation-batches/207-words-batch-46-final-validation-001.json).

## Previous published source milestone: batch206 thirty words (general word queue)

Batch206 adds 30 Russian word articles: 日常 日光 日付 既に 旗 旅 方向 方々 新鮮 新た 断る 文明 文字 文 敵 数字 数える 敬意
教科書 教授 教師 出身 故郷 政府 放す 攻撃 支店 支出 操作 損害. They are chunk 0 of 74 of the general remaining-word queue
(recomputed after Batch205: 2,217 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Sixteen existing word pages and the kanji page 師
receive 20 navigation-only link wraps at EN link positions; 既, 旗, 鮮, 敵, 敬, 授, 身, 故, 郷, 府, 攻, 撃, 操 and 損 remain
plain labels because those kanji have no RU card.

The batch covers everyday life (日常), sunlight (日光), dates (日付), "already" (既に), flags (旗), journeys (旅), direction
(方向), respected people and "here and there" (方々), freshness and renewal (新鮮, 新た), refusing (断る), civilization
(文明), written characters and sentences (文字, 文), enemies (敵), numerals and counting (数字, 数える), respect (敬意),
textbooks, professors and teachers (教科書, 教授, 教師), origin and hometown (出身, 故郷), government (政府), letting go (放す),
attack (攻撃), branch offices (支店), expenditure (支出), operating a device (操作) and damage (損害). All 23 EN exclusions are
retained; 15 direct guards beyond EN cover 日光–光, 日付–月日, 方々–人/方, 新鮮–新しい, 断る–遠慮, 文–案/提案, 数える–計算,
教授–教える/教師, 出身–生まれ, 故郷–田舎/生まれ and 支出–支給.
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
Because the signing key's passphrase cache had expired, Batch206 was authored and reviewed as a staged tree on top of the
reviewed Batch205 tree in a scratch worktree; no unsigned commit was made. The blind facet-split review found a literal gloss
in 放す that reversed the roles of 手を and 風船から, a dropped デート comparator in 日付, schema and source-list wording in 方々,
and missing contrasts of 日常 with 生活, 暮らし and 普段 and of 支出 with 費用. All five cards were fixed without RU-only links.
An optional 日光–光 guard and a clearer 故郷 translation were adopted. After Batch205 was published, the exact reviewed tree
was committed signed on a branch from its merge. The records preserve the author's and reviewer's differing
required-versus-conservative classification of the RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **4,299 reviewed-current / 8 reviewed runtime-blocked / 3,971 pending of 8,278**,
with 2,833 words, 718 kanji and 718 strokes. See the [intake](translation-batches/206-words-batch-45-intake.json),
[independent review](translation-batches/206-words-batch-45-independent-review-001.md),
[recheck](translation-batches/206-words-batch-45-recheck-001.md),
[qualified source record](translation-batches/206-words-batch-45-reviewed-source.json) and
[final validation](translation-batches/206-words-batch-45-final-validation-001.json).

## Previous published source milestone: batch205 thirty words (general word queue)

Batch205 adds 30 Russian word articles: 札 本物 本人 未来 木曜 服装 有能 有効 有利 月曜 最高 最終 最低 最中 替える 書類 書斎
更に 曜日 暮らす 暮らし 暗記 景気 普段 時刻 昨 明後日 元 旧 日曜. They are chunk 0 of 75 of the general remaining-word queue
(recomputed after Batch204: 2,247 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Eighteen existing word pages and the kanji pages 低, 効,
暮 and 未 receive 26 navigation-only link wraps at EN link positions; 札, 装, 替, 普, 旧 and 斎 remain plain labels because those
kanji have no RU card.

The batch covers banknotes (札), the genuine article and the person concerned (本物, 本人), the future (未来), weekdays (月曜,
木曜, 日曜, 曜日), dress (服装), capability, validity and advantage (有能, 有効, 有利), the superlatives 最高, 最終 and 最低 and
the midst of an activity (最中), replacing (替える), documents and a home study (書類, 書斎), "further; moreover" (更に), living
and livelihood (暮らす, 暮らし), memorization (暗記), business conditions (景気), the everyday (普段), clock time (時刻), the
time prefix 昨, the day after tomorrow (明後日), and the former or original (元, 旧). All 18 EN exclusions are retained; 15
direct guards beyond EN cover 木曜–木曜日, 月曜–月曜日, 日曜–日曜日, 明後日–あさって, 最中–盛り, 暮らす–生きる/生活, 元–種,
本物–本当, 本人–自身/自分, 更に–それに, 暗記–覚える, 書類–紙 and 服装–格好.
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
Because the signing key's passphrase cache had expired, Batch205 was authored and reviewed as a staged tree on top of the
reviewed Batch204 tree in a scratch worktree; no unsigned commit was made. The blind facet-split review found that 札's closing
source note dropped EN's qualification about the source list's compiler and read as leftover list language, missing 暮らす–生活
and 暗記–覚える guards, and a dead pointer in 替える to the untranslated かえる article. 札, 暮らす and 暗記 were fixed; the
pointer was kept by the plain-text pointer convention and the reviewer withdrew the finding. Optional 書類–紙 and 服装–格好
guards and clearer translations on 有効 and 旧 were adopted. After Batch204 was published, the exact reviewed tree was committed
signed on a branch from its merge. The records preserve the author's and reviewer's differing required-versus-conservative
classification of the RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **4,269 reviewed-current / 8 reviewed runtime-blocked / 4,001 pending of 8,278**,
with 2,803 words, 718 kanji and 718 strokes. See the [intake](translation-batches/205-words-batch-44-intake.json),
[independent review](translation-batches/205-words-batch-44-independent-review-001.md),
[recheck](translation-batches/205-words-batch-44-recheck-001.md),
[qualified source record](translation-batches/205-words-batch-44-reviewed-source.json) and
[final validation](translation-batches/205-words-batch-44-final-validation-001.json).

## Previous published source milestone: batch204 thirty words (general word queue)

Batch204 adds 30 Russian word articles: 正式 昼食 お昼 正午 プラス 正 歓迎 歌手 事情 次第 欠席 欠ける エンジン 機関 機嫌
横断 横切る 権利 様々 様 構成 検討 梅雨 桜 株 栄養 板 松 来 束. They are chunk 0 of 76 of the general remaining-word queue
(recomputed after Batch203: 2,277 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Eleven existing word pages, the kanji pages 席, 構, 権
and 欠 and the article numbers-and-counters receive 24 navigation-only link wraps at EN link positions; 嫌, 松, 板, 栄, 株, 桜,
梅, 検, 歓, 第, 討 and 養 remain plain labels because those kanji have no RU card.

The batch covers formality (正式), lunch and noon (昼食, お昼, 正午), plus and the true, official or positive (プラス, 正), welcome
(歓迎), singers (歌手), circumstances and the "depending on / as soon as" suffix (事情, 次第), absence and lack (欠席, 欠ける),
engines and institutions (エンジン, 機関), mood (機嫌), crossing (横断, 横切る), rights (権利), variety and manner (様々, 様),
composition (構成), deliberation (検討), the rainy season and cherry trees (梅雨, 桜), shares and stumps (株), nutrition
(栄養), boards (板), pines and top ranks (松), 来 'coming; since' and bundles (束). All 28 EN exclusions are retained; 19 direct
guards beyond EN cover 昼食–昼, お昼–昼間, プラス–足す, 正–正しい, 歓迎–受付, 事情–原因, 次第–流れ/途端, 欠席–休む,
機嫌–気持ち, 横断–渡る/横切る, 様–手段, 構成–組む, 検討–考える/論じる, 栄養–食料品, 板–黒板 and 松–松竹梅.
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
Because the signing key's passphrase cache had expired, Batch204 was authored and reviewed as a staged tree on top of the
reviewed Batch203 tree in a scratch worktree; no unsigned commit was made. The blind facet-split review found an overstated
past-only restriction in 次第's Russian-added 途端 comparison, missing お昼–昼間 and プラス–足す guards, and a 歓迎 people-example
worded with 迎える's Russian «встречать; приветствовать». All were fixed; the optional comparison-entry citations on 事情, 様,
構成, 検討, 栄養 and 松 were adopted. After Batch203 was published, the exact reviewed tree was committed signed on a branch from
its merge. The records preserve the author's and reviewer's differing required-versus-conservative classification of the
RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **4,239 reviewed-current / 8 reviewed runtime-blocked / 4,031 pending of 8,278**,
with 2,773 words, 718 kanji and 718 strokes. See the [intake](translation-batches/204-words-batch-43-intake.json),
[independent review](translation-batches/204-words-batch-43-independent-review-001.md),
[recheck](translation-batches/204-words-batch-43-recheck-001.md),
[qualified source record](translation-batches/204-words-batch-43-reviewed-source.json) and
[final validation](translation-batches/204-words-batch-43-final-validation-001.json).

## Previous published source milestone: batch203 thirty words (general word queue)

Batch203 adds 30 Russian word articles: 注目 注 泥 波 泡 泉 沖 意志 決心 汚染 汗 氷 気味 気候 かわいそう 哀れ 気の毒
好む 気に入る 氏 毛布 比較 毒 母親 殺す 残す 死亡 歩道 正確 正直. They are chunk 0 of 77 of the general remaining-word queue
(recomputed after Batch202: 2,307 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Eleven existing word pages and the kanji pages 亡 and 殺
receive 17 navigation-only link wraps at EN link positions; 哀, 布, 志, 染, 毒, 比, 毛, 氏, 氷, 汗, 汚, 沖, 泉, 泡, 波, 泥 and
較 remain plain labels because those kanji have no RU card.

The batch covers attention and notes (注目, 注), mud, waves, bubbles, springs and the open sea (泥, 波, 泡, 泉, 沖), will and
resolve (意志, 決心), pollution (汚染), sweat and ice (汗, 氷), sensations and climate (気味, 気候), pity (かわいそう, 哀れ, 気の毒),
liking (好む, 気に入る), the name suffix 氏, blankets (毛布), comparison (比較), poison (毒), mothers (母親), killing, leaving and
death (殺す, 残す, 死亡), pavements (歩道), and accuracy and honesty (正確, 正直). All 17 EN exclusions are retained; 9 direct
guards beyond EN cover かわいそう–残念/貧しい, 哀れ–残念, 好む–好き, 気に入る–好き/大好き, 比較–比べる and 正確–ちょうど/正しい.
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
Because the signing key's passphrase cache had expired, Batch203 was authored and reviewed as a staged tree on top of the
reviewed Batch202 tree in a scratch worktree; no unsigned commit was made. The blind facet-split review found an overbroad ban on
着る with 毛布, the dropped Japanese contrast 手を振る in 波, a missing 正確–正しい guard and an author-style source note in
気味. All were fixed; the optional 死亡 wording improvement («само 死亡» for «китайское сложение») was adopted. After Batch202 was
published, the exact reviewed tree was committed signed on a branch from its merge. The records preserve the author's and
reviewer's differing required-versus-conservative classification of the RU-added pairs and the reviewers' differing view of
the dropped hand-wave contrast. The serial rechecks reported all facets clean.

Qualified progress is **4,209 reviewed-current / 8 reviewed runtime-blocked / 4,061 pending of 8,278**,
with 2,743 words, 718 kanji and 718 strokes. See the [intake](translation-batches/203-words-batch-42-intake.json),
[independent review](translation-batches/203-words-batch-42-independent-review-001.md),
[recheck](translation-batches/203-words-batch-42-recheck-001.md),
[qualified source record](translation-batches/203-words-batch-42-reviewed-source.json) and
[final validation](translation-batches/203-words-batch-42-final-validation-001.json).

## Previous published source milestone: batch202 thirty words (general word queue)

Batch202 adds 30 Russian word articles: 炎 灰 火災 火曜 運河 濠 演奏 滞在 滅多に 溺れる 満足 湾 温暖 気温 体温
温度 減る 減らす 清潔 深刻 涙 消防 消費 海外 流行 流れる 流れ 活用 活動 泳ぎ. They are chunk 0 of 78 of the general
remaining-word queue (recomputed after Batch201: 2,337 EN words remaining); the dependency closure is exactly the 30
requested words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Eleven existing word pages
and the kanji pages 流 and 満 receive 18 navigation-only link wraps at EN link positions; 奏, 暖, 河, 涙, 清, 減, 温, 湾, 溺,
滅, 滞, 潔, 濠, 灰, 災, 炎 and 防 remain plain labels because those kanji have no RU card.

The batch covers flames, ash, fires and firefighting (炎, 灰, 火災, 消防), Tuesday (火曜), canals, moats and bays (運河, 濠,
湾), musical performance (演奏), stays (滞在), rarity (滅多に), drowning (溺れる), satisfaction (満足), warmth and temperature
(温暖, 気温, 体温, 温度), decrease (減る, 減らす), cleanliness (清潔), seriousness (深刻), tears (涙), consumption (消費),
abroad (海外), fashion and flow (流行, 流れる, 流れ), practical use and activity (活用, 活動), and swimming (泳ぎ). All 16
EN exclusions are retained; 16 direct guards beyond EN cover 火災–火事, 火曜–火曜日, 演奏–演技/公演,
滅多に–たまに/たま, 溺れる–沈む, 温暖–ぽかぽか, 体温–熱, 温度–熱, 深刻–まじめ/真剣, 流行–回り/広がる/人気 and 泳ぎ–泳ぐ.
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
Because the signing key's passphrase cache had expired, Batch202 was authored and reviewed as a staged tree on top of the
reviewed Batch201 tree in a scratch worktree; no unsigned commit was made. The blind facet-split review found an implied spontaneous
cause in 温度 («понижается сама»), an omitted EN note on the N2 source and its spelling 堀 in 濠, Latin «na-прилагательное»
in 温暖, a reversed relation in 灰 («задаёт») and «плакала» for 涙を流しました in 涙, which conflated it with 泣く. All
were fixed; the optional 満足, 体温, 海外 and 流行 wording improvements were adopted, and no exclusion changed. After Batch201 was published, the
exact reviewed tree was committed signed on a branch from its merge. The records preserve the author's
and reviewer's differing required-versus-conservative classification of the RU-added pairs and disclose that the
consistency reviewer read all 30 cards in full only in a second pass. The serial rechecks reported all facets clean.

Qualified progress is **4,179 reviewed-current / 8 reviewed runtime-blocked / 4,091 pending of 8,278**,
with 2,713 words, 718 kanji and 718 strokes. See the [intake](translation-batches/202-words-batch-41-intake.json),
[independent review](translation-batches/202-words-batch-41-independent-review-001.md),
[recheck](translation-batches/202-words-batch-41-recheck-001.md),
[qualified source record](translation-batches/202-words-batch-41-reviewed-source.json) and
[final validation](translation-batches/202-words-batch-41-final-validation-001.json).

## Previous published source milestone: batch201 thirty words (general word queue)

Batch201 adds 30 Russian word articles: 現状 現場 王様 王子 王 率 独身 独立 犯罪 犯人 物質 物語 物理 物価 物事
父親 爆発 燃える 熱帯 熱中 煙 無視 無料 無事 いえ 寧ろ 否 ノー 無し 無. They are chunk 0 of 79 of the general
remaining-word queue (recomputed after Batch200: 2,367 EN words remaining); the dependency closure is exactly the 30
requested words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Ten existing word pages
and the kanji pages 帯, 煙, 犯 and 王 receive 21 navigation-only link wraps at EN link positions; 価, 寧, 無, 燃, 爆, 独, 率,
視 and 身 remain plain labels because those kanji have no RU card.

The batch covers the current state and work sites (現状, 現場), kings and princes (王様, 王子, 王), rates (率), single life
and independence (独身, 独立), crime and criminals (犯罪, 犯人), matter, stories, physics, prices and things (物質, 物語,
物理, 物価, 物事), fathers (父親), explosions, burning and smoke (爆発, 燃える, 煙), the tropics and absorption (熱帯, 熱中),
ignoring, free of charge and safe arrival (無視, 無料, 無事), and negation and absence (いえ, 寧ろ, 否, ノー, 無し, 無). All 19
EN exclusions are retained; 16 direct guards beyond EN cover 現状–様子, 物質–布, 物語–歴史/語る, 物事–こと/物,
燃える–焼ける, 熱中–ねっしん, 無事–大丈夫/幸福, 否–嫌, 無し–いいえ/いえ/否 and 無–無し/ノー.
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
Because the signing key's passphrase cache had expired, Batch201 was authored and reviewed as a staged tree on top of the
reviewed Batch200 tree in a scratch worktree; no unsigned commit was made. The blind facet-split review found an overstated
Russian-only contrast in 無し (なし "only" about absence, contradicting its own evaluative use), omitted EN source-provenance
qualifications in ノー and 無, two missing quiz guards (現状–様子 and 無–ノー), a nonstandard «ичидан» spelling in 燃える and a
mistranslated «действенный» in 犯罪. All were fixed; the optional 独身 and 現場 wording improvements were adopted, and the
無し–いいえ/いえ/否 guards were kept as conservative. After Batch200 was published, the exact reviewed tree was committed
signed on a branch from its merge. The records preserve the author's and reviewer's differing required-versus-conservative
classification of the RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **4,149 reviewed-current / 8 reviewed runtime-blocked / 4,121 pending of 8,278**,
with 2,683 words, 718 kanji and 718 strokes. See the [intake](translation-batches/201-words-batch-40-intake.json),
[independent review](translation-batches/201-words-batch-40-independent-review-001.md),
[recheck](translation-batches/201-words-batch-40-recheck-001.md),
[qualified source record](translation-batches/201-words-batch-40-reviewed-source.json) and
[final validation](translation-batches/201-words-batch-40-final-validation-001.json).

## Previous published source milestone: batch200 thirty words (general word queue)

Batch200 adds 30 Russian word articles: 発表 発明 疑う 疑問 異常 留学 画家 男子 申し訳 予防 用心 使用 用いる 布 生地
命 生 生命 生じる 瓶 環境 理想 玉 球 現金 現象 状況 光景 場面 事態. They are chunk 0 of 80 of the general remaining-word
queue (recomputed after Batch199: 2,397 EN words remaining); the dependency closure is exactly the 30 requested words, so
every EN quiz_exclusions target resolves to an existing RU word or a batch word. Fifteen existing word pages and the kanji
pages 命, 留, 疑 and 表 receive 27 navigation-only link wraps at EN link positions; 境, 布, 態, 況, 玉, 環, 瓶, 異, 訳, 象 and 防
remain plain labels because those kanji have no RU card.

The batch covers announcements and inventions (発表, 発明), doubt (疑う, 疑問), abnormality (異常), study abroad (留学),
painters (画家), boys and men (男子), apology (申し訳), prevention and caution (予防, 用心), using (使用, 用いる), cloth and
dough (布, 生地), life (命, 生, 生命), arising (生じる), bottles (瓶), environment (環境), ideals (理想), balls and spheres
(玉, 球), cash (現金), phenomena (現象) and situations, sights, scenes and states of affairs (状況, 光景, 場面, 事態). All 32 EN
exclusions are retained; 17 direct guards beyond EN cover 画家–作家, 男子–男の人/おじいさん/おじさん, 申し訳–謝る,
予防–防ぐ, 使用–用, 用いる–利用, 瓶–缶, 玉–硬貨, 現金–お金/金/金銭, 状況–都合, 光景–景色/眺め and 事態–状況.
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
Because the signing key's passphrase cache had expired, Batch200 was authored and reviewed as a staged tree on top of the
reviewed Batch199 tree in a scratch worktree; no unsigned commit was made. The blind facet-split review found correctness and
scoped coverage clean and two quiz-safety findings: 状況 lacked a guard against 都合, whose Russian title overlaps it through
«обстоятельства», and 玉's extra 銅貨 guard was reachable only by chaining. The comprehensibility review found reversed causal
roles in 生じる's summary, an author note with an English gloss in 生地, source adjudication instead of a learner rule in 命,
and editorial sentences in 生 and 現金. All were fixed; 生地's note was rewritten as a learner rule that 生地 read せいち or
しょうち is a separate word meaning «место рождения», checked against WWWJDIC, Jisho and Digital Daijisen. After Batch199 was
published, the exact reviewed tree was committed signed on a branch from its merge. The records preserve the author's and
reviewer's differing required-versus-conservative classification of the RU-added pairs. The serial rechecks reported all facets
clean.

Qualified progress is **4,119 reviewed-current / 8 reviewed runtime-blocked / 4,151 pending of 8,278**,
with 2,653 words, 718 kanji and 718 strokes. See the [intake](translation-batches/200-words-batch-39-intake.json),
[independent review](translation-batches/200-words-batch-39-independent-review-001.md),
[recheck](translation-batches/200-words-batch-39-recheck-001.md),
[qualified source record](translation-batches/200-words-batch-39-reviewed-source.json) and
[final validation](translation-batches/200-words-batch-39-final-validation-001.json).

## Previous published source milestone: batch199 thirty words (general word queue)

Batch199 adds 30 Russian word articles: 確実 確かめる 硬貨 破産 砂漠 石炭 情報 知識 知事 知らせ 眺める 眺め 真剣 真似 真っ赤
県 相続 相手 直に 直ちに 直接 ゴール 目標 目的 指導 コーチ 監督 盛り 登山 発車. They are chunk 0 of 81 of the general
remaining-word queue (recomputed after Batch198: 2,427 EN words remaining); the dependency closure is exactly the 30 requested
words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Eleven existing word pages and the
kanji pages 導 and 識 receive 16 navigation-only link wraps at EN link positions; 硬, 貨, 砂, 漠, 炭, 眺, 剣, 県, 接, 標, 的, 監,
督 and 盛 remain plain labels because those kanji have no RU card.

The batch covers certainty and checking (確実, 確かめる), coins (硬貨), bankruptcy (破産), deserts (砂漠), coal (石炭),
information, knowledge and notices (情報, 知識, 知らせ), prefectures and their governors (県, 知事), gazing and views (眺める,
眺め), seriousness (真剣), imitation and behaviour (真似), bright red (真っ赤), inheritance (相続), partners and opponents
(相手), directness and immediacy (直に, 直ちに, 直接), goals and purposes (ゴール, 目標, 目的), guidance, coaches and
supervisors (指導, コーチ, 監督), the peak of something (盛り), mountain climbing (登山) and vehicle departure (発車). All 23 EN
exclusions are retained; 21 direct guards beyond EN cover 確実–確か/堅い/違いない/きっと, 確かめる–調べる, 情報–案内,
知らせ–知らせる, 真剣–重大/大変, 真似–写す/コピー, 真っ赤–赤い/赤, 県–都, 直接–まっすぐ, ゴール–ため, 目標–ため,
指導–教育/教える, 監督–管理 and 登山–登る. Exclusions are one-sided declarations that Android applies in both directions; the
batch changes exclusions only on its new cards.
Because the signing key's passphrase cache had expired, Batch199 was authored and reviewed as a staged tree on top of the
reviewed Batch198 tree in a scratch worktree; no unsigned commit was made. The blind facet-split review found consistency and
quiz safety clean and three correctness defects: 盛り rendered 盛りを過ぎました as «отцвела», the Russian-added 写す/コピー
contrast in 真似 drew an unqualified object-based boundary, and 指導 described 教育 only as «вся система». The comprehensibility
review independently found the 盛り issue and two more: ゴール said the loanword «соответствует английскому goal», and 知識
turned the noun into the verb «узнать». All were fixed; the ゴール sentence now names only the English source word, as reviewed
RU loanword cards do, and an inline dictionary number in 直に was removed as optional polish. After Batch198 was published, the
exact reviewed tree was committed signed on a branch from its merge. The records preserve the author's and reviewer's differing
required-versus-conservative classification of the RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **4,089 reviewed-current / 8 reviewed runtime-blocked / 4,181 pending of 8,278**,
with 2,623 words, 718 kanji and 718 strokes. See the [intake](translation-batches/199-words-batch-38-intake.json),
[independent review](translation-batches/199-words-batch-38-independent-review-001.md),
[recheck](translation-batches/199-words-batch-38-recheck-001.md),
[qualified source record](translation-batches/199-words-batch-38-reviewed-source.json) and
[final validation](translation-batches/199-words-batch-38-final-validation-001.json).

## Previous published source milestone: batch198 thirty words (general word queue)

Batch198 adds 30 Russian word articles: 笛 章 立ち上がる 空き 穴 積極的 積む 積もる 穀物 稼ぐ 根 種 税金 税 移動 動かす 移す
秒 科目 禁煙 禁止 祭 神経 神 祝う 祝い 礼儀 感謝 礼 確認. They are chunk 0 of 82 of the general remaining-word queue (recomputed
after Batch197: 2,457 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Eleven existing word pages and the kanji pages 明 and
積 receive 15 navigation-only link wraps at EN link positions; 笛, 章, 穴, 極, 的, 穀, 稼, 根, 税, 移, 秒, 禁, 祭, 祝, 儀 and
謝 remain plain labels because those kanji have no RU card.

The batch covers flutes and whistles (笛), chapters and badges (章), standing up (立ち上がる), free space or time (空き), holes
(穴), being proactive (積極的), stacking, loading and settling in layers (積む, 積もる), grain (穀物), earning (稼ぐ), roots and
seeds (根, 種), taxes (税金, 税), moving and transferring (移動, 動かす, 移す), seconds (秒), school subjects (科目), bans
(禁煙, 禁止), festivals (祭), nerves (神経), gods (神), celebrating and celebration gifts (祝う, 祝い), etiquette (礼儀) and
gratitude, thanks and bows (感謝, 礼), and confirmation (確認). All 16 EN exclusions are retained; 28 direct guards beyond EN
cover 立ち上がる–上がる, 空き–席, 積む–折る, 穀物–米, 稼ぐ–働く, 根–原因, 種–話題, 移動–移す/移る/動かす/動く, 禁煙–禁止,
祭–お祭り/お祝い/祝い, 祝う–お祝い/祝い, 祝い–お祝い/プレゼント/贈り物/お土産/お祭り/記念, 感謝–恩, 礼–恩 and
確認–チェック/テスト/調べる. Exclusions are one-sided declarations that Android applies in both directions; the batch changes
exclusions only on its new cards.
Because the signing key's passphrase cache had expired, Batch198 was authored and reviewed as a staged tree on top of the
reviewed Batch197 tree in a scratch worktree; no unsigned commit was made. The blind facet-split review found correctness and
scoped coverage clean, one quiz-safety gap (移動 lacked a 動かす guard) and five comprehensibility defects: 穀物 rendered 米や麦
as three crops and its scope note was unclear, 積む's «одна на другую» did not fit three boxes, 積極的 kept a warning that
depended on English "positive", 神経 rejected «писание бога» without saying that 経 also means «сутра», and 祭 kept an
author-facing dictionary remark. All were fixed. A conservative 移動–動く guard was added, and optional wording for 穀物, 空き
and 積もる was adopted. After Batch197 was published, the exact reviewed tree was committed signed on a branch from its merge.
The records preserve the author's and reviewer's differing required-versus-conservative classification of the RU-added pairs.
The serial rechecks reported all facets clean.

Qualified progress is **4,059 reviewed-current / 8 reviewed runtime-blocked / 4,211 pending of 8,278**,
with 2,593 words, 718 kanji and 718 strokes. See the [intake](translation-batches/198-words-batch-37-intake.json),
[independent review](translation-batches/198-words-batch-37-independent-review-001.md),
[recheck](translation-batches/198-words-batch-37-recheck-001.md),
[qualified source record](translation-batches/198-words-batch-37-reviewed-source.json) and
[final validation](translation-batches/198-words-batch-37-final-validation-001.json).

## Previous published source milestone: batch197 thirty words (general word queue)

Batch197 adds 30 Russian word articles: 結論 結果 直 今に やがて いずれ 結局 経由 営業 経営 経つ 組合 組む 態度 位置 地位 立場
位 段 級 納得 精々 粉 籠 範囲 節約 節 管 答案 筆. They are chunk 0 of 83 of the general remaining-word queue (recomputed after
Batch196: 2,487 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN quiz_exclusions
target resolves to an existing RU word or a batch word. Seven existing word pages, the kanji pages 位, 営 and 囲 and the
numbers-and-counters article receive 16 navigation-only link wraps at EN link positions; 態, 案, 筆, 管, 節, 範, 籠, 粉, 納, 級
and 結 remain plain labels because those kanji have no RU card.

The batch covers conclusions, results and outcomes (結論, 結果, 結局), "soon" and "eventually" (直, 今に, やがて, いずれ), going
via a place (経由), business operation and management (営業, 経営), time passing (経つ), unions and teaming up (組合, 組む),
attitude (態度), position, status, standpoint and rank (位置, 地位, 立場, 位), steps and grades (段, 級), being convinced
(納得), "at most" (精々), powder (粉), baskets and cages (籠), range (範囲), saving (節約), joints, tunes and notable points
(節), pipes (管), exam answers (答案) and writing brushes (筆). All 33 EN exclusions are retained; 24 direct guards beyond EN
cover 結論–判断, 今に–もうすぐ/いずれ, いずれ–どの/どっち, 結局–末, 経由–通過, 営業–売る, 態度–行儀, 位置–所/場, 立場–見解,
位–くらい, 級–水準, 納得–承知, 精々–以下, 範囲–額, 節約–省く/貯金, 節–曲/点/特徴, 答案–答 and 筆–手. Exclusions are one-sided
declarations that Android applies in both directions; the batch changes exclusions only on its new cards.
The blind facet-split review found consistency and quiz safety clean, correctness clean, one scoped-coverage gap (結果 wrote
EN's ケッカ reading note as けっか) and two minor comprehensibility defects: 手間を省く in 節約 and the bold pattern 組合の会員
lacked kana readings. All were fixed. Optional items adopted the 結果 and 籠 example translations, a broader 途中 explanation
in 経由 and a conservative 節約–貯金 guard. The candidate was committed signed and pushed before review. Because the signing
key's passphrase cache had expired, the serial rechecks read the staged revised tree, which was then committed signed
unchanged. The records preserve the author's and reviewer's differing required-versus-conservative classification of the
RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **4,029 reviewed-current / 8 reviewed runtime-blocked / 4,241 pending of 8,278**,
with 2,563 words, 718 kanji and 718 strokes. See the [intake](translation-batches/197-words-batch-36-intake.json),
[independent review](translation-batches/197-words-batch-36-independent-review-001.md),
[recheck](translation-batches/197-words-batch-36-recheck-001.md),
[qualified source record](translation-batches/197-words-batch-36-reviewed-source.json) and
[final validation](translation-batches/197-words-batch-36-final-validation-001.json).

## Previous published source milestone: batch196 thirty words (general word queue)

Batch196 adds 30 Russian word articles: 能力 能 胃 育つ 肩 皮 肌 職業 職 考慮 考え 老人 老い 翼 羽 美人 罹る 罰する 罪 缶
繰り返す 結ぶ 繋ぐ 綿 保存 維持 絶滅 絶対 絵画 給料. They are chunk 0 of 84 of the general remaining-word queue (recomputed
after Batch195: 2,517 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Fifteen existing word pages and the kanji pages 給, 絶,
罪, 老, 職 and 育 receive 33 navigation-only link wraps at EN link positions; 保, 慮, 滅, 皮, 結, 維, 綿, 繋, 繰, 缶, 罰, 罹,
羽, 翼, 肌, 肩 and 胃 remain plain labels because those kanji have no RU card.

The batch covers ability and talent, including Noh theatre (能力, 能), the stomach and shoulder (胃, 肩), growing up (育つ),
peel, hide and skin (皮, 肌), occupations and posts (職業, 職), consideration and thoughts (考慮, 考え), old people and ageing
(老人, 老い), wings and feathers (翼, 羽), beauties (美人), falling ill (罹る), punishment and crime (罰する, 罪), cans (缶),
repeating (繰り返す), tying and connecting (結ぶ, 繋ぐ), cotton (綿), storage and maintenance (保存, 維持), extinction (絶滅),
absolute certainty (絶対), painting (絵画) and salary (給料). All 20 EN exclusions are retained; 15 direct guards beyond EN
cover 能力–知能, 能–機能, 育つ–伸びる/成長, 皮–革, 肌–表/面, 職–勤め, 考慮–尊重, 考え–意見/見解/考える, 維持–支える and
老人–おじいさん/おばあさん. Exclusions are one-sided declarations that Android applies in both directions; the batch changes
exclusions only on its new cards.
The blind facet-split review found correctness clean, one scoped-coverage gap (綿 changed EN's kana reading gloss), one
quiz-safety gap (老人 «пожилой человек» overlaps おじいさん and おばあさん) and nine minor comprehensibility and coverage
defects: 能力 called 才能 innate; «театр но» read as the conjunction «но»; 綿, 考慮, 絶対 and 老人 lacked contrasts with 木綿,
尊重, ぜひ and おじいさん/おばあさん; 羽 and 皮 kept author-facing source-list notes; and «ханэцуки» lacked context. All were
fixed with plain-text contrasts, a guard pair, «театр Но», EN-faithful «талант, одарённость» and reworded learner notes.
The candidate was committed signed and pushed before review. The records preserve the author's and reviewer's differing
required-versus-conservative classification of the RU-added pairs and the reviewers' differing dictionary evidence on
whether 才能 implies innate ability. The serial rechecks reported all facets clean.

Qualified progress is **3,999 reviewed-current / 8 reviewed runtime-blocked / 4,271 pending of 8,278**,
with 2,533 words, 718 kanji and 718 strokes. See the [intake](translation-batches/196-words-batch-35-intake.json),
[independent review](translation-batches/196-words-batch-35-independent-review-001.md),
[recheck](translation-batches/196-words-batch-35-recheck-001.md),
[qualified source record](translation-batches/196-words-batch-35-reviewed-source.json) and
[final validation](translation-batches/196-words-batch-35-final-validation-001.json).

## Previous published source milestone: batch195 thirty words (general word queue)

Batch195 adds 30 Russian word articles: 表情 衣服 衝突 衛星 行儀 行動 行き 虫歯 作家 ライター 著者 菓子 莫大 苦しむ 芸術
芝生 航空 舞台 舌 臭い 天然 自然 自殺 自慢 自動 膝 腰 腐る 脇 才能. They are chunk 0 of 85 of the general remaining-word
queue (recomputed after Batch194: 2,547 EN words remaining); the dependency closure is exactly the 30 requested words, so every
EN quiz_exclusions target resolves to an existing RU word or a batch word. Seven existing word pages and the kanji pages 才, 能
and 舞 receive 16 navigation-only link wraps at EN link positions; 衣, 衝, 衛, 星, 儀, 虫, 著, 菓, 莫, 芸, 芝, 航, 舌, 臭, 慢,
膝, 腰, 腐 and 脇 remain plain labels because those kanji have no RU card.

The batch covers facial expressions and clothing (表情, 衣服), collisions and satellites (衝突, 衛星), manners, actions and
outbound journeys (行儀, 行動, 行き), tooth decay (虫歯), writers, lighters and authors (作家, ライター, 著者), sweets (菓子),
enormous amounts (莫大), suffering (苦しむ), art (芸術), lawns (芝生), aviation (航空), the stage (舞台), the tongue (舌),
bad smells (臭い), the natural (天然, 自然), suicide (自殺), boasting (自慢), automatic operation (自動), the knee, lower back
and side (膝, 腰, 脇), rotting (腐る) and talent (才能). All 12 EN exclusions are retained; 15 direct guards beyond EN cover
表情–表現/現れ, 衣服–洋服, 衝突–喧嘩, 衛星–友/連れ/月, 行動–こと, 虫歯–歯, ライター–記者, 菓子–ケーキ/飴, 苦しむ–苦痛,
舌–言葉 and 脇–横. Exclusions are one-sided declarations that Android applies in both directions; the batch changes
exclusions only on its new cards.
The blind facet-split review found correctness clean, one scoped-coverage gap (衣服 dropped EN's rule that the word needs
no Japanese plural ending), one quiz-safety gap (虫歯's title «кариес; кариозный зуб» overlaps 歯 «зуб; зубы») and one
comprehensibility defect (自慢 shared the «гордость» frame with the existing 誇り card without separating them). 衣服 now
states the plural rule, 虫歯 is guarded against 歯, and 自慢 gains an unlinked, qualified contrast with 誇り. A smoother 衣服
example translation was accepted as an optional item. A second comprehensibility finding, 作家's plain-text pointer to the
untranslated article on occupation and role endings, was declined under the restoration convention and withdrawn on recheck.
The candidate was committed signed and pushed before review. The recheck preserves the author's and reviewer's differing
required-versus-conservative classification of the RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **3,969 reviewed-current / 8 reviewed runtime-blocked / 4,301 pending of 8,278**,
with 2,503 words, 718 kanji and 718 strokes. See the [intake](translation-batches/195-words-batch-34-intake.json),
[independent review](translation-batches/195-words-batch-34-independent-review-001.md),
[recheck](translation-batches/195-words-batch-34-recheck-001.md),
[qualified source record](translation-batches/195-words-batch-34-reviewed-source.json) and
[final validation](translation-batches/195-words-batch-34-final-validation-001.json).

## Previous published source milestone: batch194 thirty words (general word queue)

Batch194 adds 30 Russian word articles: 解決 解ける 解く 観察 観客 観光 親友 覚悟 覚める 覚ます 見解 見舞い 偉い 上等 見事
覆う 要素 要点 すなわち つまり 要するに 製品 裸 裏切る 裁判 害 被害 被る 袖 袋. They are chunk 0 of 86 of the general
remaining-word queue (recomputed after Batch193: 2,577 EN words remaining); the dependency closure is exactly the 30 requested
words, so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Eight existing word pages and the
kanji pages 偉, 害, 察 and 観 receive 20 navigation-only link wraps at EN link positions; 悟, 覆, 素, 製, 裸, 裏, 裁, 被, 袖
and 袋 remain plain labels because those kanji have no RU card.

The batch covers solving and untying (解決, 解ける, 解く), observation, spectators and sightseeing (観察, 観客, 観光), close
friends (親友), resolve and waking (覚悟, 覚める, 覚ます), views and sympathy visits (見解, 見舞い), praise and quality (偉い,
上等, 見事), covering (覆う), elements and main points (要素, 要点), the restatement words すなわち, つまり and 要するに,
products (製品), nakedness and betrayal (裸, 裏切る), trials (裁判), harm and damage (害, 被害), wearing on the head or taking
blame (被る), sleeves (袖) and bags (袋). All 20 EN exclusions are retained; 27 direct guards beyond EN cover
解決–決定/解く/解ける/決める, 解ける–解く/決まる, 解く–決める, 観察–見物, 親友–友人/友達/友, 覚ます–起す,
見舞い–訪問/訪ねる/伺う, 偉い–立派/感心/偉大/優秀/大した, 上等–すばらしい, 見事–凄い, 要素–部分, 要点–中心, 製品–品物
and 被る–着る/履く. Exclusions are one-sided declarations that Android applies in both directions; the batch changes
exclusions only on its new cards.
The blind facet-split review found correctness clean, also for a post-blind Gramota check of nine Russian lexical choices.
It found two quiz-safety gaps closed by guards (見事–凄い, 解決–決める) and three comprehensibility defects: 被害's
definition «увиденные…» could read as harm that was seen, 被る ended with the English source-list gloss "to suffer", and
覚ます's title «будить; пробуждать» repeated 起す «будить». 被害 now says «с точки зрения того, кто их понёс», 被る's
provenance note renders the gloss as «страдать», and 覚ます is retitled «пробуждать; выводить из сна». Two optional wording
items (お as the polite prefix in 見舞い, 解く's own gloss «развязывать») were accepted. The candidate was committed signed
and pushed before review. The recheck preserves the author's and reviewer's differing required-versus-conservative
classification of the RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **3,939 reviewed-current / 8 reviewed runtime-blocked / 4,331 pending of 8,278**,
with 2,473 words, 718 kanji and 718 strokes. See the [intake](translation-batches/194-words-batch-33-intake.json),
[independent review](translation-batches/194-words-batch-33-independent-review-001.md),
[recheck](translation-batches/194-words-batch-33-recheck-001.md),
[qualified source record](translation-batches/194-words-batch-33-reviewed-source.json) and
[final validation](translation-batches/194-words-batch-33-final-validation-001.json).

## Previous published source milestone: batch193 thirty words (general word queue)

Batch193 adds 30 Russian word articles: 生まれ 誕生 許す 認める 誇り 詳しい 話題 詰める 詩人 試す 試し 判断 評価 証明 検査 診察
設計 訪問 記録 記者 記憶 記念 記入 記事 訓練 訓 討つ 言わば 触れる 解釈. They are chunk 0 of 87 of the general remaining-word queue
(recomputed after Batch192: 2,607 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Eight existing word pages and the kanji pages 判, 断, 許
and 認 receive 20 navigation-only link wraps at EN link positions; 誕, 誇, 詳, 詰, 詩, 評, 価, 証, 検, 査, 診, 設, 録, 憶, 訓, 練,
討, 触 and 釈 remain plain labels because those kanji have no RU card.

The batch covers birth (生まれ, 誕生), allowing and recognising (許す, 認める), pride, detail and topics (誇り, 詳しい, 話題),
packing (詰める), poets, trying and trials (詩人, 試す, 試し), judgment, assessment and proof (判断, 評価, 証明), inspection and
medical consultation (検査, 診察), design and visits (設計, 訪問), the 記 cluster of records, reporters, memory, commemoration,
form entries and articles (記録, 記者, 記憶, 記念, 記入, 記事), training and kun readings (訓練, 訓), attacking (討つ), "so to
speak" (言わば), touching (触れる) and interpretation (解釈). All 17 EN exclusions are retained; 21 direct guards beyond EN cover
生まれ–生まれる, 誕生–生まれる, 許す–許可, 認める–承認/許可, 試し–試験, 判断–読み, 評価–読み, 検査–調査/テスト, 診察–受付,
設計–案, 訪問–訪ねる/伺う/お見舞い, 記憶–覚える/思い出す, 記念–記憶, 訓–読み, 討つ–勝つ and 触れる–関する. Exclusions are
one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new cards.
The blind facet-split review found correctness clean, one consistency defect (訓's example respelled the reading of 山 as
Cyrillic «яма», an ordinary Russian word), two quiz-safety gaps closed by guards (訪問–お見舞い, 判断–読み) and one
comprehensibility defect (記事 explained itself through the English letters a and the). All were fixed, and 試し's stiff
first translation was smoothed as an accepted optional item. The candidate was committed signed and pushed before review.
The recheck preserves the author's and reviewer's differing required-versus-conservative classification of the RU-added
pairs. The serial rechecks reported all facets clean.

Qualified progress is **3,909 reviewed-current / 8 reviewed runtime-blocked / 4,361 pending of 8,278**,
with 2,443 words, 718 kanji and 718 strokes. See the [intake](translation-batches/193-words-batch-32-intake.json),
[independent review](translation-batches/193-words-batch-32-independent-review-001.md),
[recheck](translation-batches/193-words-batch-32-recheck-001.md),
[qualified source record](translation-batches/193-words-batch-32-reviewed-source.json) and
[final validation](translation-batches/193-words-batch-32-final-validation-001.json).

## Previous published source milestone: batch192 thirty words (general word queue)

Batch192 adds 30 Russian word articles: 豆 谷 譲る 議長 論争 議論 議員 議会 警告 講演 謎 諺 止す 諦める 論文 話し合う 論じる
調査 調子 課 読み 説 誤解 語学 語る 単語 言語 語 招く 誘う. They are chunk 0 of 88 of the general remaining-word queue
(recomputed after Batch191: 2,637 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Seven existing word pages and the kanji pages 単, 招, 解,
誤, 論 and 議 receive 23 navigation-only link wraps at EN link positions; 豆, 谷, 譲, 講, 謎, 諺, 諦, 査, 課 and 誘 remain plain
labels because those kanji have no RU card.

The batch covers beans and valleys, yielding (譲る), the assembly-and-debate cluster (議長, 議員, 議会, 論争, 議論, 話し合う,
論じる, 論文), warnings and lectures (警告, 講演), riddles and proverbs, stopping and giving up (止す, 諦める), investigation and
condition (調査, 調子), lessons and sections (課), reading and theories (読み, 説), misunderstanding, the language-and-word
cluster (語学, 語る, 単語, 言語, 語) and inviting (招く, 誘う). All 22 EN exclusions are retained; 16 direct guards beyond EN
cover 譲る–負ける, 議論–相談/話し合う/論じる, 講演–スピーチ, 話し合う–相談, 調査–調べる, 読み–読む, 説–説明, 語学–勉強,
語る–話/話す, 招く–招待/呼ぶ and 誘う–招待/呼ぶ. Exclusions are one-sided declarations that Android applies in both directions;
the batch changes exclusions only on its new cards.
The blind facet-split review found one correctness defect (譲る contrasted 負ける categorically, although 負ける also means
yielding and reducing a price), quiz-safety gaps closed by nine added guards, Russian-only sentences in 講演 and 招く that
described test behaviour, and one comprehensibility defect (読み's 読書 contrast and its mismatched gloss). All were fixed.
The candidate was committed signed and pushed before review. The recheck preserves the author's and reviewer's differing
required-versus-conservative classification of the RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **3,879 reviewed-current / 8 reviewed runtime-blocked / 4,391 pending of 8,278**,
with 2,413 words, 718 kanji and 718 strokes. See the [intake](translation-batches/192-words-batch-31-intake.json),
[independent review](translation-batches/192-words-batch-31-independent-review-001.md),
[recheck](translation-batches/192-words-batch-31-recheck-001.md),
[qualified source record](translation-batches/192-words-batch-31-reviewed-source.json) and
[final validation](translation-batches/192-words-batch-31-final-validation-001.json).

## Previous published source milestone: batch191 thirty words (general word queue)

Batch191 adds 30 Russian word articles: 身体 越える 越す 起こる 与える 贈る 贅沢 質 賢い 賞 資源 資本 恩 貸し 貴重 貯金 係 機能
働き 作業 勤め 役 義務 務め 責任 責める 販売 貢献 負け 豪華. They are chunk 0 of 89 of the general remaining-word queue
(recomputed after Batch190: 2,667 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Six existing word pages and the kanji pages 与, 任, 役,
負, 責 and 越 receive 22 navigation-only link wraps at EN link positions; 身, 贈, 贅, 沢, 賢, 賞, 源, 恩, 貴, 貯, 義, 販, 貢, 献,
豪 and 華 remain plain labels because those kanji have no RU card.

The batch covers the body, crossing and exceeding (越える, 越す), occurring, giving and presenting (与える, 贈る), luxury and
splendour (贅沢, 豪華), quality, cleverness, prizes, resources and capital, favours and lending (恩, 貸し), value and savings
(貴重, 貯金), the work-and-duty cluster (係, 機能, 働き, 作業, 勤め, 役, 義務, 務め, 責任, 責める), selling, contribution and
defeat. All 37 EN exclusions are retained; 19 direct guards beyond EN cover 身体–生物, 越す–引っ越す/移る/過ぎる,
与える–くれる/くださる, 贈る–あげる/差し上げる/上げる, 恩–御礼, 貸し–貸す, 貴重–高価, 係–責任, 働き–労働/運転/動く,
責任–担当, 販売–売る and 負け–負ける. 係 is titled «ответственный (за порученное дело); ведение» because «поручение» exactly
matched the 依頼 and 用事 titles. Exclusions are one-sided declarations that Android applies in both directions; the batch
changes exclusions only on its new cards.
The blind facet-split review found one correctness defect (負け claimed without a source that 敗北 sounds more bookish), two
quiz-safety gaps (越す–過ぎる, 貴重–高価) and five comprehensibility or coverage defects: English-dependent remarks in 越す,
販売 and 貢献, a past-tense gloss of 今回は私の負けです that contradicted the card's noun-versus-verb note, and no 働き–労働
contrast. All were fixed. GPG signing timed out when the candidate was first committed, so the reviews ran on a local unsigned
commit whose tree is identical to the signed candidate; the records state this. The recheck preserves the author's and
reviewer's differing required-versus-conservative classification of the RU-added pairs. The serial rechecks reported all facets
clean.

Qualified progress is **3,849 reviewed-current / 8 reviewed runtime-blocked / 4,421 pending of 8,278**,
with 2,383 words, 718 kanji and 718 strokes. See the [intake](translation-batches/191-words-batch-30-intake.json),
[independent review](translation-batches/191-words-batch-30-independent-review-001.md),
[recheck](translation-batches/191-words-batch-30-recheck-001.md),
[qualified source record](translation-batches/191-words-batch-30-reviewed-source.json) and
[final validation](translation-batches/191-words-batch-30-final-validation-001.json).

## Previous published source milestone: batch190 thirty words (general word queue)

Batch190 adds 30 Russian word articles: 通り 通す 通じる 瞬間 途端 逆らう 逆 追う 追い付く 迷惑 迷子 述べる 現代 近代 迎え
辺り 農民 農業 農家 辞める 轢く 丸 輪 転ぶ 軒 軍隊 軍 身長 自身 身. They are chunk 0 of 90 of the general remaining-word queue
(recomputed after Batch189: 2,697 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Six existing word pages and the kanji pages 丸 and 追
receive 10 navigation-only link wraps at EN link positions; 瞬, 端, 逆, 惑, 述, 辺, 農, 轢, 輪, 軒, 軍, 隊 and 身 remain plain
labels because those kanji have no RU card.

The batch covers passing through and communicating (通り, 通す, 通じる), moments (瞬間, 途端), opposing and reversal (逆らう,
逆), chasing and catching up (追う, 追い付く), nuisance and lost children (迷惑, 迷子), stating, the present and modern eras
(現代, 近代), meeting someone, vicinity (辺り), farming (農民, 農業, 農家), quitting, running over, circles and rings (丸, 輪),
falling over, the counter for houses, armies (軍隊, 軍) and the body and self (身長, 自身, 身). All 25 EN exclusions are retained;
26 direct guards beyond EN cover 迷惑–不便/厄介, 現代–現在/時代, 近代–時代, 瞬間–際, 迎え–迎える/会/会合, 農業–産業,
農家–家族/家庭/家, 迷子–子/子供, 輪–指輪, 転ぶ–落ちる, 身長–成長/増加, 身–肉/中心, 辺り–頃/側/隣, 通す–極める and 轢く–移る.
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
The blind facet-split review found two correctness defects (通じる dropped the source's "not every communication use"
qualification of 通る, and 輪 claimed an unsupported frequency for the ornament sense), an unverified 近代 periodization
caution, and four comprehensibility defects (undemonstrated 辺り and 迷惑 contrasts, 近代's «новое время» title and a bare 円
in 丸). All were fixed; 近代 is now «эпоха модернизации», and its qualified «новое время» caution is backed by Warodai/Jardic and
ru.wikipedia periodization evidence. The consistency reviewer's 轢く–引っ越す lead was accepted and the guard withdrawn;
its 農業–産業 concern was withdrawn in recheck under the generic-label rule. The recheck preserves the author's and reviewer's
differing required-versus-conservative classification of the RU-added pairs. The serial rechecks reported all facets clean.

Qualified progress is **3,819 reviewed-current / 8 reviewed runtime-blocked / 4,451 pending of 8,278**,
with 2,353 words, 718 kanji and 718 strokes. See the [intake](translation-batches/190-words-batch-29-intake.json),
[independent review](translation-batches/190-words-batch-29-independent-review-001.md),
[recheck](translation-batches/190-words-batch-29-recheck-001.md),
[qualified source record](translation-batches/190-words-batch-29-reviewed-source.json) and
[final validation](translation-batches/190-words-batch-29-final-validation-001.json).

## Previous published source milestone: batch189 thirty words (general word queue)

Batch189 adds 30 Russian word articles: 銅貨 銃 銀 鉄道 鉄 ピン 針 金属 金 金銭 金融 金曜 金庫 数 量 野 重視 重大 酸素 都市 便
郵便 部分 避ける 選択 選手 適用 適切 適度 違反. They are chunk 0 of 91 of the general remaining-word queue (recomputed after
Batch188: 2,727 EN words remaining); the dependency closure is exactly the 30 requested words, so every EN quiz_exclusions
target resolves to an existing RU word or a batch word. Five existing word pages, the kanji pages 数 and 適 and the
numbers-and-counters article receive 12 navigation-only link wraps at EN link positions; 銅, 貨, 銃, 鉄, 針, 属, 銭, 融, 庫, 量,
視, 酸, 素, 郵, 避 and 択 remain plain labels because those kanji have no RU card.

The batch covers coins, guns, metals (銀, 鉄, 金属, 金), railways, pins and needles, money and finance (金銭, 金融), Friday,
safes, number and quantity (数, 量), fields, emphasis and seriousness (重視, 重大), oxygen, cities, mail and service (便, 郵便),
parts, avoiding, choice, athletes, application, appropriateness and moderation (適用, 適切, 適度) and violations. All 14 EN
exclusions are retained; direct guards beyond EN cover 金融–経済/金銭/お金/金, 金/金銭–経済, 金曜–金曜日, 数/量–多少,
重大–大変/まじめ/大した/相当, 便/郵便–郵便局, 選択–選ぶ, 適用–用, 適切–適する/合う/いい, 銃–武器, 都市–町, 野–畑 and 鉄/銀–金属.
Exclusions are one-sided declarations that Android applies in both directions; the batch changes exclusions only on its new
cards.
The blind facet-split review found one inherited correctness defect (避ける stated a categorical よける/さける split that
デジタル大辞泉's usage note qualifies), one quiz-safety gap (鉄/銀 lacked the generic 金属 guard) and one comprehensibility
defect (都市 glossed «городской центр», which reads as "downtown"). All were fixed; 都市 is now «город; городское поселение».
The correctness reviewer's outside-facet 鉄–鉄道 lead was declined because the railway sense is an abbreviation used in compounds; the
recheck preserves the author's and reviewer's differing required-versus-conservative classification of the RU-added pairs.
The serial rechecks reported all facets clean.

Qualified progress is **3,789 reviewed-current / 8 reviewed runtime-blocked / 4,481 pending of 8,278**,
with 2,323 words, 718 kanji and 718 strokes. See the [intake](translation-batches/189-words-batch-28-intake.json),
[independent review](translation-batches/189-words-batch-28-independent-review-001.md),
[recheck](translation-batches/189-words-batch-28-recheck-001.md),
[qualified source record](translation-batches/189-words-batch-28-reviewed-source.json) and
[final validation](translation-batches/189-words-batch-28-final-validation-001.json).

## Previous published source milestone: batch188 thirty words (general word queue)

Batch188 adds 30 Russian word articles: 違いない 道路 道徳 過去 過ごす 幸い 幸運 運 遅刻 遂に 改善 上達 前進 進歩 進学 進める 週
週間 逮捕 連続 連想 友 連れ 速度 通行 合格 通過 通学 通信 通り過ぎる. They are chunk 1 of 92 of the general remaining-word queue
(recomputed after Batch187: closure of 2,757 EN words); chunk 0 remains queued. 幸運 and 運 joined through the EN
幸い→幸運→運 exclusion chain, so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Five
existing word pages, the kanji pages 刻, 路 and 遅 and the numbers-and-counters article receive 15 navigation-only link
wraps at EN link positions; 善, 徳, 改, 逮 and 遂 remain plain labels because those kanji have no RU card.

The batch covers certainty (違いない), roads and morals, the past and spending time, good fortune, luck and fate (幸い, 幸運,
運), lateness, "at last" (遂に), improvement, progress and pushing work forward (改善, 上達, 前進, 進歩, 進める), going on to
further education, weeks and week-long periods (週, 週間), arrest, succession and association of ideas (連続, 連想), friends
and companions (友, 連れ), speed, passage and traffic (通行, 通過, 通り過ぎる), passing an exam, commuting to school and
communication. Direct guards beyond EN cover 幸い–幸福, 進歩–発展/発達, 連続–次々, 遂に–とうとう/末, 前進–進む, 通行–通る,
通過–通る/過ぎる, 通り過ぎる–通過, 通学–通う, 速度–高速, 週間–期間 and 進学–入学. Exclusions are one-sided declarations that Android
applies in both directions, so reverse entries briefly added to the baseline cards 次々, 発展 and 幸せ during the fixes were
removed; the batch changes exclusions only on its new cards.
The blind facet-split review found one correctness defect (週間 glossed 毎週 as «раз в неделю»), quiz-safety gaps
(identical 運/幸運 titles, 連続–次々, 進歩–発展) and comprehensibility issues (the 進める title/H1 mismatch and a circular
usage ban, the 通過/合格 overlap, an English «way» note in 道路). All were fixed; 運 is now «судьба; удача». A later
correctness recheck added 幸い–幸福 and 進歩–発達; the reviewers' 幸い–幸福 disagreement and its evidence-based resolution are
preserved in the recheck. The final rechecks reported all facets clean. The recheck also records process deviations:
concurrent rechecks in one round, an unaccepted draft report and a replacement comprehensibility reviewer on the same model.

Qualified progress is **3,759 reviewed-current / 8 reviewed runtime-blocked / 4,511 pending of 8,278**,
with 2,293 words, 718 kanji and 718 strokes. See the [intake](translation-batches/188-words-batch-27-intake.json),
[independent review](translation-batches/188-words-batch-27-independent-review-001.md),
[recheck](translation-batches/188-words-batch-27-recheck-001.md),
[qualified source record](translation-batches/188-words-batch-27-reviewed-source.json) and
[final validation](translation-batches/188-words-batch-27-final-validation-001.json).

## Previous published source milestone: batch187 thirty words (general word queue)

Batch187 adds 30 Russian word articles: 離す 雇う 集団 集中 会 会合 集まり 隠れる 隠す 障害 回 度 際 陰 限界 守る 防ぐ 関連 関心
関する 誤り 間違い 始まり 開始 閉じる 長期 鎖 鍋 鋭い 鋏. They are chunk 0 of 93 of the general remaining-word queue
(recomputed after Batch186: closure of 2,787 EN words; 会 joined to support 会合, and 会合 to support 集まり), so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Fifteen existing word pages and the kanji pages 団
and 守 receive 19 navigation-only link wraps at EN link positions (three 守る links on 守); 鋏, 鋭, 鍋, 鎖, 防, 陰, 障, 隠, 雇
and 離 remain plain labels because those kanji have no RU card.

The batch covers separating and hiring, groups, meetings and gatherings (集団, 会, 会合, 集まり), concentration, hiding
(隠れる, 隠す), obstacles and impairments, times, occasions and moments (回, 度, 際), shade, limits, protecting and
preventing (守る, 防ぐ), relation and interest (関連, 関心, 関する), mistakes (誤り, 間違い), beginnings (始まり, 開始), closing,
long terms, chains, pots, sharpness and scissors. Direct guards beyond EN cover 回–一度/もう一度,
度–場合/ケース/機会/一度/もう一度/今度, 際–場合, 始まり–始め/出発, 開始–最初/出発, 関する–対する/触る, 関連–連絡, 限界–かぎり,
長期–期間, 間違い–失敗, 鋭い–辛い, 鍋–料理 and 閉じる–ぱくぱく.
The independent review found two correctness defects (the 集中 particle roles and a 際 past-form timing claim),
comprehensibility issues (a garbled 関する translation and 鍋 conflated with a frying pan) and two quiz-safety advisories
(度–機会, 始まり/開始–出発), adopted as guards. All were fixed; a later recheck added the 回/度 guards against 一度, もう一度 and
今度, a final bounded pair review judged 回–今度 not directly ambiguous, and the rechecks reported all facets clean.

Qualified progress is **3,729 reviewed-current / 8 reviewed runtime-blocked / 4,541 pending of 8,278**,
with 2,263 words, 718 kanji and 718 strokes. See the [intake](translation-batches/187-words-batch-26-intake.json),
[independent review](translation-batches/187-words-batch-26-independent-review-001.md),
[recheck](translation-batches/187-words-batch-26-recheck-001.md),
[qualified source record](translation-batches/187-words-batch-26-reviewed-source.json) and
[final validation](translation-batches/187-words-batch-26-final-validation-001.json).

## Previous published source milestone: batch186 thirty words (general word queue)

Batch186 adds 30 Russian word articles: 食品 食卓 食う 飛行 飛び出す 除く 省く 飛ばす 風景 問い 題 頼る 頬 預ける 期間 時 時期
頃 革 表面 面 非常 霧 霜 需要 電子 雷 離婚 去る 離れる. They are chunk 0 of 94 of the general remaining-word queue
(recomputed after Batch185: closure of 2,817 EN words; 頃 joined through the EN 時 exclusion), so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Ten existing word pages and the kanji pages 期 and
除 receive 16 navigation-only link wraps at EN link positions, with per-file link counts to batch words matching EN; 省, 預
and 革 remain plain labels because those kanji are still pending in RU.

The batch covers food and eating (食品, 食卓, 食う), flying, jumping out and launching (飛行, 飛び出す, 飛ばす), removing and
omitting (除く, 省く), scenery, questions and titles, relying on and entrusting (頼る, 預ける), the cheek, words for time,
periods and approximate time (期間, 時, 時期, 頃), leather, surfaces and aspects (表面, 面), emergencies, fog, frost and
thunder, demand, electrons, divorce, and leaving or moving apart (去る, 離れる). Direct guards beyond EN cover pairs such as
食卓–テーブル, 食う–掛かる, 除く–以外/取る, 時–ころ/場合/機会/ケース, 時期–時間/季節, 頃–くらい/ほど/約, 表面–表/格好, 面–表/点,
非常–非常に/極, 離婚–別れる and 去る–出る/立つ/過ぎる/亡くなる. The reviewer classed several others (for example
食う–召し上がる/いただく, 需要–必要 and 離れる–遠い/遠く) as conservative: each has a dictionary basis, but ordinary-quiz
necessity is not established, so that qualification stays explicit rather than CLEAN. The independent read-only review
found correctness, scoped coverage and comprehensibility clean and one minor quiz-safety gap: 預ける now guards 頼む
(Russian «поручать» also means leaving someone in another's care). Two optional polish items were accepted: 頼る's title
now covers things as well as people, and the 雷 explanation no longer compares with English. The recheck reported all
four facets clean.

Qualified progress is **3699 reviewed-current / 8 reviewed runtime-blocked / 4571 pending of 8278**,
with 2233 words, 718 kanji and 718 strokes. See the [intake](translation-batches/186-words-batch-25-intake.json),
[independent review](translation-batches/186-words-batch-25-independent-review-001.md),
[recheck](translation-batches/186-words-batch-25-recheck-001.md),
[qualified source record](translation-batches/186-words-batch-25-reviewed-source.json) and
[final validation](translation-batches/186-words-batch-25-final-validation-001.json).

## Previous published source milestone: batch185 thirty words (general word queue)

Batch185 adds 30 Russian word articles: きょろきょろ 制限 限る かぎり かあかあ 飽きる うんざり うとうと 空 黙る 黒板 魅力 鬼 髪の毛
高速 高価 骨折 物音 騒音 騒ぎ 駐車 香り 首相 餌 飼う 飯 食糧 食料 食物 食欲. They are chunk 0 of 95 of the general
remaining-word queue (recomputed after Batch184: closure of 2,847 EN words), so every EN quiz_exclusions target resolves
to an existing RU word or a batch word. Ten existing word pages and the kanji pages 空 and 限 receive 16 navigation-only
link wraps at EN link positions, with per-file link counts to batch words matching EN; 板, 毛, 骨, 駐 and 香 remain plain
labels because those kanji are still pending in RU.

The batch covers limits and restrictions (制限, 限る, かぎり), restless glancing, a crow's caw, boredom and dozing, the sky,
falling silent, blackboards, charm, demons and the "it" of tag, hair, high speed and expensive things, fractures, noise
and commotion, parking, fragrance, the prime minister, feed and keeping animals, and words for rice, food and provisions
(飯, 食糧, 食料, 食物, 食欲). 空 is published byte-identical to its held batch-033 draft; its five Russian-only guards
(天気, 気, 気分, 遠く, 遠い) were independently assessed as conservative: each has a dictionary basis, but ordinary-quiz
necessity is not established, so that C2 qualification stays explicit rather than CLEAN. Other direct guards beyond EN
cover pairs such as かぎり–制限/以内/内/できるだけ, 髪の毛–髪/毛, 骨折–折る, 騒ぎ–混乱/ばたばた, 駐車–駐車場, 飼う–持つ and the
mutually distinct food titles. The optional image field of 3 onomatopoeic articles is omitted (word-only adaptation).
The independent read-only review found correctness, scoped coverage and comprehensibility clean and three minor
quiz-safety gaps: 高価 now guards 大切/大事 (shared «дорогой»), 食物 guards 食事 (Russian «еда» also means a meal) and
駐車 guards 止める (the article teaches 車を止める). The recheck reported all four facets clean.

Qualified progress is **3,669 reviewed-current / 8 reviewed runtime-blocked / 4,601 pending of 8,278**,
with 2,203 words, 718 kanji and 718 strokes. See the [intake](translation-batches/185-words-batch-24-intake.json),
[independent review](translation-batches/185-words-batch-24-independent-review-001.md),
[recheck](translation-batches/185-words-batch-24-recheck-001.md),
[qualified source record](translation-batches/185-words-batch-24-reviewed-source.json) and
[final validation](translation-batches/185-words-batch-24-final-validation-001.json).

## Previous published source milestone: batch184 thirty words (general word queue)

Batch184 adds 30 Russian word articles: じっと じろじろ じゅうじゅう じりじり じゃぶじゃぶ じとじと じめじめ しとしと ざあざあ ごぼごぼ
ごしごし ぐびぐび がぶがぶ ごくごく 濃い こってり 秘密 こそこそ こけこっこー 咳 げほげほ ぐるぐる ぐらぐら くんくん くるり くよくよ
くすくす ぎょっと ぎゅうぎゅう きりきり. They are chunk 0 of 96 of the general remaining-word queue (recomputed after
Batch183: closure of 2,877 EN words), so every EN quiz_exclusions target resolves to an existing RU word or a batch word.
Thirty-two existing word pages receive 36 navigation-only link wraps at EN link positions, with per-file link counts to
batch words matching EN; no kanji page changes (濃 is still pending in RU, and 秘, 密 and 咳 have no kanji page).

The batch covers stillness and staring, sizzling, scorching heat and impatience, splashing, damp and humid weather,
drizzle and downpours, gurgling, scrubbing, gulping and guzzling, rich and concentrated food or colour (濃い, こってり),
secrets and sneaking, the rooster's crow, coughing, spinning and wobbling, sniffing, quick turns, brooding, giggling,
being startled, tight cramming and gripping pain. Direct guards beyond EN cover pairs such as じりじり–暑い/そろそろ/遅い,
ごぼごぼ/ぐらぐら–沸く, ぐびぐび/がぶがぶ/ごくごく–飲む, 濃い–強い, こってり–厚い/太い, こけこっこー–鳴く/鶏, 咳–こんこん,
ぐるぐる/くるり–回る, ぎゅうぎゅう–一杯/満ちる/あふれる and きりきり–苦痛/頭痛/ずきずき/ぎゅうぎゅう. The optional image field of 21
onomatopoeic articles is omitted (word-only adaptation).
The independent read-only review found correctness, scoped coverage and comprehensibility clean and two quiz-safety
issues: ごぼごぼ «клокотать» also means «кипеть», so it now guards 沸く, and author-added ちびちび guards on ぐびぐび and ごくごく
excluded an opposite and were removed. Two optional title refinements (きりきり, じゅうじゅう) were adopted. The first recheck
found one earlier gap, the shared tight-binding sense of きりきり and ぎゅうぎゅう, which received a guard; the second recheck
reported all four facets clean.

Qualified progress is **3,639 reviewed-current / 8 reviewed runtime-blocked / 4,631 pending of 8,278**,
with 2,173 words, 718 kanji and 718 strokes. See the [intake](translation-batches/184-words-batch-23-intake.json),
[independent review](translation-batches/184-words-batch-23-independent-review-001.md),
[recheck](translation-batches/184-words-batch-23-recheck-001.md),
[qualified source record](translation-batches/184-words-batch-23-reviewed-source.json) and
[final validation](translation-batches/184-words-batch-23-final-validation-001.json).

## Previous published source milestone: batch183 thirty words (general word queue)

Batch183 adds 30 Russian word articles: ひりひり ひらひら 偶然 ひょいと ぱんぱん ぱらぱら ざぶざぶ ばしゃばしゃ はあはあ にやにや
にゃあにゃあ とぼとぼ てくてく たびたび しばしば たま ちょこちょこ 徐々に ちびちび ちくちく そよそよ ぐいぐい ずんずん ずるずる
ずけずけ ずきずき するする 睡眠 すやすや すいすい. They are chunk 0 of 97 of the general remaining-word queue
(recomputed after Batch182: closure of 2,907 EN words), so every EN quiz_exclusions target resolves to an existing RU
word or a batch word. Twenty existing word pages and the kanji pages 偶 and 然 receive 27 navigation-only link wraps at
EN link positions (three each to 偶然 on the two kanji pages), with per-file link counts to batch words matching EN.

The batch covers stinging and throbbing pain, fluttering, chance, nimble and bulging movement, sprinkling and
splashing, panting, grinning and mewing, trudging and steady walking, frequency adverbs (たびたび, しばしば, たま),
toddling and sipping, prickling, breezes, forceful and dragging movement, blunt speech, gliding, smooth swimming and
the sleep words 睡眠 and すやすや. Direct guards beyond EN cover pairs such as ひりひり/ずきずき–苦痛/頭痛/しくしく,
偶然–出会う/ふと/ばったり, ぱんぱん–一杯/込む/満ちる, たま–たまに/珍しい/時々, とぼとぼ/てくてく–歩く, するする–滑る/つるつる/ぬるぬる,
睡眠–眠る/夢 and すいすい–泳ぐ/容易. The optional image field of 20 onomatopoeic articles is omitted (word-only
adaptation).
The independent read-only review found correctness and scoped coverage clean, one comprehensibility issue (the
ざぶざぶ title taught wading as a sense; it was retitled «шумно плескать; с громким плеском») and two quiz-safety gaps
(ずけずけ–まっすぐ «напрямик» and ぱんぱん–あふれる «переполняться»). They were fixed, together with five adopted optional
wording items, and the recheck reported all four facets clean.

Qualified progress is **3,609 reviewed-current / 8 reviewed runtime-blocked / 4,661 pending of 8,278**,
with 2,143 words, 718 kanji and 718 strokes. See the [intake](translation-batches/183-words-batch-22-intake.json),
[independent review](translation-batches/183-words-batch-22-independent-review-001.md),
[recheck](translation-batches/183-words-batch-22-recheck-001.md),
[qualified source record](translation-batches/183-words-batch-22-reviewed-source.json) and
[final validation](translation-batches/183-words-batch-22-final-validation-001.json).

## Previous published source milestone: batch182 thirty words (general word queue)

Batch182 adds 30 Russian word articles: わんわん よちよち もくもく むずむず まま ぽりぽり ぽちゃん ぽたぽた あつあつ ほかほか
ぽかぽか ぺちゃんこ ぺたぺた ぺこぺこ べらべら ねばねば べたべた ぶかぶか ぴりぴり ちゅんちゅん ぴよぴよ ぴょんぴょん びりびり
びゅうびゅう ひんやり 頭痛 がんがん じんじん 苦痛 痛み. They are chunk 0 of 98 of the general remaining-word queue
(recomputed after Batch181: closure of 2,937 EN words), so every EN quiz_exclusions target resolves to an existing RU
word or a batch word. Ten existing pages (words/さらさら だらだら どろどろ ぬるぬる ばりばり べちゃべちゃ ほくほく めらめら
メーメー 苦心) receive 11 navigation-only link wraps at EN link positions, with per-file link counts to batch words
matching EN.

The batch covers animal and bird calls, toddling and hopping, smoke, itching, dripping and splashing, warmth and
coolness, stickiness, flattening, chattering and fawning, oversized clothes, stinging, tearing and buzzing, howling
wind, the grammatical noun まま, and the pain words 頭痛, 苦痛 and 痛み with throbbing and tingling. Direct guards beyond
EN cover pairs such as わんわん/ちゅんちゅん/ぴよぴよ–鳴く, ぺたぺた–貼る/べたべた, ねばねば–もちもち/付く, ぶかぶか–大きい/大きな,
びゅうびゅう–吠える/吹く and the pain cluster 頭痛/苦痛/痛み/じんじん–痛い/しくしく. The optional image field of 19
onomatopoeic articles is omitted (word-only adaptation).
The independent read-only review found correctness, scoped coverage and comprehensibility clean and one quiz-safety
gap (がんがん «грохотать» lacked a guard against ごろごろ «громыхать…», a different-root near-synonym the stem screen
missed). It was fixed, together with three adopted optional wording items, and the recheck reported all four facets
clean.

Qualified progress is **3,579 reviewed-current / 8 reviewed runtime-blocked / 4,691 pending of 8,278**,
with 2,113 words, 718 kanji and 718 strokes. See the [intake](translation-batches/182-words-batch-21-intake.json),
[independent review](translation-batches/182-words-batch-21-independent-review-001.md),
[recheck](translation-batches/182-words-batch-21-recheck-001.md),
[qualified source record](translation-batches/182-words-batch-21-reviewed-source.json) and
[final validation](translation-batches/182-words-batch-21-final-validation-001.json).

## Previous published source milestone: batch181 thirty words (general word queue)

Batch181 adds 30 Russian word articles: 炊事 炊く 煮える 煮る がやがや ぶるぶる わくわく 天候 陽気 うきうき ぞくぞく ざわざわ
ささやく ぶつぶつ 凹凸 武士 兵士 公演 体力 亥 亀 それとも あるいは 乃至 丑 メーメー しくしく めそめそ 叫ぶ 吠える.
They are chunk 0 of 99 of the general remaining-word queue (recomputed after Batch180: closure of 2,967 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Seventeen existing pages
(kanji/体 候 兵 叫 園 演; words/がたがた がちがち しょんぼり でこぼこ はらはら ひそひそ ぺらぺら 元気 公園 寅 巳) receive 24
navigation-only link wraps at EN link positions, with per-file link counts to batch words matching EN.

The batch covers cooking and boiling, weather, unevenness, warriors and soldiers, stage performances, physical
strength, two zodiac signs and the turtle, the «or» conjunctions それとも, あるいは and 乃至, shouting and barking, and ten
onomatopoeic words for crowd noise, trembling, excitement and thrill, grumbling, bleating and whimpering. Direct
guards beyond EN cover pairs such as 炊事–台所/こしらえる, 煮える–ぐつぐつ/ことこと, がやがや/ざわざわ–騒ぐ,
陽気–楽しい/賑やか, 公演–芝居/演説/スピーチ, 亥–豚 and 叫ぶ–呼ぶ. The optional image field of 5 onomatopoeic articles is
omitted (word-only adaptation).
The independent read-only review found correctness and scoped coverage clean, one comprehensibility issue (an
ungrammatical double negation in 武士) and two quiz-safety gaps (公演 «выступление артистов; спектакль» shared
«выступление» with スピーチ and 演説 without a guard; 煮える lacked guards against ぐつぐつ and ことこと). All three were
fixed, together with one adopted optional wording item, and the recheck reported all four facets clean.

Qualified progress is **3,549 reviewed-current / 8 reviewed runtime-blocked / 4,721 pending of 8,278**,
with 2,083 words, 718 kanji and 718 strokes. See the [intake](translation-batches/181-words-batch-20-intake.json),
[independent review](translation-batches/181-words-batch-20-independent-review-001.md),
[recheck](translation-batches/181-words-batch-20-recheck-001.md),
[qualified source record](translation-batches/181-words-batch-20-reviewed-source.json) and
[final validation](translation-batches/181-words-batch-20-final-validation-001.json).

## Previous published source milestone: batch180 thirty words (general word queue)

Batch180 adds 30 Russian word articles: 少しも 全く 明確 明らか はあ さっぱり すっきり ほっと あっさり きっぱり はきはき
きびきび せっせと 破る がちがち かちかち ばりばり 活気 ぴんぴん もりもり ぺろり ぺろぺろ ぱくぱく むしゃむしゃ もぐもぐ
ぽつぽつ ぐつぐつ 備える こしらえる 家事.
They are chunk 0 of 100 of the general remaining-word queue (recomputed after Batch179: closure of 2,997 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Seventeen existing pages
(kanji/備 破; words/かたかた ぐずぐず ぐったり ぐにゃぐにゃ ことこと しっかり ばきばき ぱちぱち びくびく ぶくぶく へとへと
ぼそぼそ むかむか もやもや 約束) receive 22 navigation-only link wraps at EN link positions, with per-file link counts to
batch words matching EN.

The batch covers negative-polarity «not at all» adverbs, clarity and obviousness, the interjection はあ, tearing and
breaking rules, liveliness, preparing and making things, housework, and twenty onomatopoeic words for refreshment and
relief, light taste, decisive and brisk manner, stiffness and hardness, crunching, vigour, eating and licking, scattered drops and
simmering. Every pair among the five negative-polarity «совсем не / нисколько» titles (全然, ちっとも, 少しも, 全く, さっぱり) is excluded;
other direct guards cover pairs such as 明確/明らか–はっきり, あっさり–軽い/簡単/安易, 活気–元気/賑やか, 備える–準備/用意/支度,
こしらえる–料理 and 家事–宿題. The optional image field of 17 onomatopoeic articles is omitted (word-only adaptation).
The independent read-only review found scoped coverage and comprehensibility clean, one correctness issue (破る
claimed that «сломать» lies outside its range, although its first dictionary sense includes "break") and one
quiz-safety gap (備える lacked a guard against 予習). Both were fixed, together with three adopted optional items, and
the recheck reported all four facets clean.

Qualified progress is **3,519 reviewed-current / 8 reviewed runtime-blocked / 4,751 pending of 8,278**,
with 2,053 words, 718 kanji and 718 strokes. See the [intake](translation-batches/180-words-batch-19-intake.json),
[independent review](translation-batches/180-words-batch-19-independent-review-001.md),
[recheck](translation-batches/180-words-batch-19-recheck-001.md),
[qualified source record](translation-batches/180-words-batch-19-reviewed-source.json) and
[final validation](translation-batches/180-words-batch-19-final-validation-001.json).

## Previous published source milestone: batch179 thirty words (general word queue)

Batch179 adds 30 Russian word articles: 訴える 困難 苦労 面倒 厄介 手間 努力 労働 苦心 苦情 満ちる あふれる 零れる
こぼす ひそひそ ぱさぱさ ぼそぼそ すたすた しゃきしゃき こりこり ぱりぱり ノック こんこん 順調 とんとん さくさく
むかむか いらいら かりかり ばきばき.
They are chunk 0 of 101 of the general remaining-word queue (recomputed after Batch178: closure of 3,027 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Sixteen existing pages
(kanji/働 努 労; words/うろうろ かさかさ からから しっとり そっと つやつや どたどた どんどん のろのろ ぱちぱち ぺらぺら
ぼろぼろ 緊張) receive 23 navigation-only link wraps at EN link positions, with per-file link counts matching EN.
Kanji without RU cards (厄 訴 零 順) stay plain text.

The batch covers complaining and suing, difficulty, hardship, trouble and effort, labour, filling, overflowing and
spilling, smooth progress (順調), knocking at a door (ノック), and fourteen onomatopoeic words for whispering and
mumbling, dry and crisp textures, brisk walking, knocking, smooth progress, nausea and irritation. Every pair among
the four «хлопоты»/«хлопотный» titles (苦労, 面倒, 厄介, 手間) and among the five «хрустящий» titles
(しゃきしゃき, こりこり, ぱりぱり, さくさく, かりかり) is excluded; other direct guards cover pairs such as
訴える–文句/不平, 努力–一生懸命, あふれる–込む, 零れる/こぼす–流す and こんこん/とんとん–叩く.
The optional image field of ぼそぼそ, すたすた and ばきばき is omitted (word-only adaptation). The independent
read-only review found correctness and scoped coverage clean, two comprehensibility issues (an unnatural Russian
translation in こぼす and a transitive gloss of the intransitive 水がこぼれる in 零れる) and one quiz-safety gap
(満ちる lacked a guard against 込む «быть переполненным»). All three were fixed, together with five adopted wording
suggestions, and the recheck reported all four facets clean.

Qualified progress is **3,489 reviewed-current / 8 reviewed runtime-blocked / 4,781 pending of 8,278**,
with 2,023 words, 718 kanji and 718 strokes. See the [intake](translation-batches/179-words-batch-18-intake.json),
[independent review](translation-batches/179-words-batch-18-independent-review-001.md),
[recheck](translation-batches/179-words-batch-18-recheck-001.md),
[qualified source record](translation-batches/179-words-batch-18-reviewed-source.json) and
[final validation](translation-batches/179-words-batch-18-final-validation-001.json).

## Previous published source milestone: batch178 thirty words (general word queue)

Batch178 adds 30 Russian word articles: 素 台 基準 基礎 基盤 基地 地盤 幹 巳 詩 俳句 川柳 寅 奇しい 妖しい 圧力 卯 同一
同様 匹敵 副作用 発行 出版 刊行 差 区別 幅 違い 異なる 相違.
They are chunk 0 of 102 of the general remaining-word queue (recomputed after Batch177: closure of 3,057 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Twelve existing pages
(kanji/刊 副 匹 区 圧 差 幅 規; words/柳 梓 特徴 狂う) receive 19 navigation-only link wraps at EN link positions,
with per-file link counts matching EN. Kanji without RU cards (俳 卯 句 基 奇 妖 寅 巳 幹 敵 柳 準 版 異 盤 礎 素 詩)
stay plain text.

The batch covers bases, foundations, standards and infrastructure, stands and platforms, ground and political support
bases, tree trunks, three zodiac signs (Snake, Tiger, Rabbit), poetry, haiku and senryū, strange and bewitching,
pressure, sameness and similarity, matching an equal, side effects, issuing and publishing, and difference, width and
distinction. New cards titled with «основа» (素, 基礎, 基盤) exclude 基 «основа; база» and 基本 «основы; основа», and
基地 «база» excludes 基; other direct guards cover close pairs such as 詩–句/歌, 同様–そんな, 発行/出版/刊行–出す and
違い–違う/異なる/相違/別. English source glosses that mislead in Russian ("prime", "similarity", "discrimination") are
cited and explained in Russian terms. The independent read-only review found correctness, scoped coverage and quiz safety clean, and three
comprehensibility issues: an English "base" contrast left in 基地, a 区別がつかない gloss with a personal subject, and
an ungrammatical sentence in 副作用. All three were fixed, together with an EN-inherited 幹–中心 guard, five adopted
wording suggestions, 発行–支給 and 同様–然る guards, and a follow-up removal of a repeated word in 地盤. Adding 副作用's figurative Japanese
sense was declined as beyond the EN source. The recheck resolved every item and reported all four facets clean.

Qualified progress is **3,459 reviewed-current / 8 reviewed runtime-blocked / 4,811 pending of 8,278**,
with 1,993 words, 718 kanji and 718 strokes. See the [intake](translation-batches/178-words-batch-17-intake.json),
[independent review](translation-batches/178-words-batch-17-independent-review-001.md),
[recheck](translation-batches/178-words-batch-17-recheck-001.md),
[qualified source record](translation-batches/178-words-batch-17-reviewed-source.json) and
[final validation](translation-batches/178-words-batch-17-final-validation-001.json).

## Previous published source milestone: batch177 thirty words (general word queue)

Batch177 adds 30 Russian word articles: 救う 救助 手伝い 援助 柱 柚 枚 松竹梅 梅 杏 李 曲 増す 増加 昇る 政治家
採掘 釣り 漁業 水産 捕鯨 御殿 彗星 局 オフィス 庁 基本 基 水準 計る.
They are chunk 0 of 103 of the general remaining-word queue (recomputed after Batch176: closure of 3,087 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Ten existing pages
(kanji/曲; words/拡大 支える 桃 橘 発展 竹 鉱石 隻 鯨) receive 12 navigation-only link wraps at EN link positions,
with per-file link counts matching EN. Kanji without RU cards (基 庁 彗 掘 採 援 救 昇 星 李 杏 松 枚 柚 柱 梅 殿 準 漁
竹 釣 鯨) stay plain text.

The batch covers rescue, help and aid, pillars, citrus and stone-fruit trees (yuzu, ume, apricot, plum), the flat-object
counter, the pine-bamboo-plum ranking, musical pieces, increase and rising, politicians, mining, fishing, fisheries and
whaling, palaces, comets, bureaus, offices and agencies, basics, foundations and standards, and measuring. Russian titles
that share «помощь», «поддержка», «увеличение», «рост», «управление» or «станция» receive direct guards, as do close
pairs such as 曲–歌, 釣り–釣る and オフィス–会社; 梅 is titled «умэ; японский абрикос» after its botanical identity so
that it does not collide with 李 «слива». English-only contrasts ("save money",
"post", "citron", "take office", "weigh") were recast in Russian terms. The independent read-only review found
correctness and scoped coverage clean, one comprehensibility issue (松竹梅 romanized 竹 as «таке» instead of «такэ») and
one quiz-safety gap (増す lacked 上がる/上げる guards, per the 増える precedent). Both were fixed, together with an adopted
昇る–進む guard and two menu wordings in 松竹梅 and 梅; a 漁業 rewording and 水産 title alternatives were declined as not
clearly better. The recheck resolved every item and reported all four facets clean.

Qualified progress is **3,429 reviewed-current / 8 reviewed runtime-blocked / 4,841 pending of 8,278**,
with 1,963 words, 718 kanji and 718 strokes. See the [intake](translation-batches/177-words-batch-16-intake.json),
[independent review](translation-batches/177-words-batch-16-independent-review-001.md),
[recheck](translation-batches/177-words-batch-16-recheck-001.md),
[qualified source record](translation-batches/177-words-batch-16-reviewed-source.json) and
[final validation](translation-batches/177-words-batch-16-final-validation-001.json).

## Previous published source milestone: batch176 thirty words (general word queue)

Batch176 adds 30 Russian word articles: 椋 梨 縁 端 暮れ 末 底 尻 しっぽ 頂上 トップ 先端 梢 梓 桑 桐 桂 書物 図書
冊子 栞 茶 茶色い 栗 豊富 豊か 栄える 柳 支える 助ける.
They are chunk 0 of 104 of the general remaining-word queue (recomputed after Batch175: closure of 3,117 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Six existing pages
(kanji/冊 助 頂; words/榛 蚕 貧しい) receive 10 navigation-only link wraps at EN link positions, with per-file link
counts matching EN. Kanji without RU cards (椋 梨 縁 端 底 尻 梢 梓 桑 桐 桂 栞 栗 豊 栄 柳) stay plain text.

The batch covers trees (muku, pear, azusa, mulberry, paulownia, katsura, chestnut, willow), edges, ends and tips,
dusk and the year's end, bottoms and tails, summits and the top position, books, booklets and bookmarks, tea and
brown, abundance and prosperity, and support and help. Russian titles that share «конец», «книга», «чай»,
«коричневый», «богатый» or «поддерживать» receive direct guards; English-only contrasts ("edge/rim/tip", "bottom",
"top", "rich", "help/save/support") were recast in Russian terms. The independent read-only review found scoped
coverage and comprehensibility clean, two correctness issues (a Russian-only 栗 note calling トチノキ seeds
inedible; a 豊か sentence that could read as denying its "wealthy" sense) and three quiz-safety gaps (支える–賛成,
暮れ–端, トップ–いちばん). All were fixed; a 冊子 wording option was declined for consistency with 受付. The recheck at 2ed9172 confirmed all five findings resolved, with correctness, scoped coverage, comprehensibility and quiz safety clean.

Qualified progress is **3,399 reviewed-current / 8 reviewed runtime-blocked / 4,871 pending of 8,278**,
with 1,933 words, 718 kanji and 718 strokes. See the [intake](translation-batches/176-words-batch-15-intake.json),
[independent review](translation-batches/176-words-batch-15-independent-review-001.md),
[recheck](translation-batches/176-words-batch-15-recheck-001.md),
[qualified source record](translation-batches/176-words-batch-15-reviewed-source.json) and
[final validation](translation-batches/176-words-batch-15-final-validation-001.json).

## Previous published source milestone: batch175 thirty words (general word queue)

Batch175 adds 30 Russian word articles: 岸 湖畔 流す 注ぐ 浴びせる 沈める 水稲 歳 欧州 橘 油 石油 脂 ビニール
プラスチック ナイロン 樹脂 榛 達する 至る 極める 材料 材木 木材 楠 紅葉 楓 椿 骨 椎骨.
They are chunk 0 of 105 of the general remaining-word queue (recomputed after Batch174: closure of 3,147 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Four existing pages
(kanji/岸 歳; words/畔 筋肉) receive 7 navigation-only link wraps at EN link positions, with per-file link counts
matching EN. Kanji without RU cards (湖 畔 浴 沈 稲 欧 橘 油 脂 樹 榛 至 極 材 楠 紅 楓 椿 骨 椎) stay plain text.

The batch covers shores and lakesides, flowing, pouring and sinking, wetland rice, age, Europe, trees and shrubs
(tachibana, hazel, camphor, maple, camellia), oils, fats and petroleum, plastics, vinyl, nylon and resin, reaching
and attaining, materials and timber, autumn leaves, and bones. Russian titles that share «берег», «рис», «лет»,
«масло» or «пускать» receive direct guards; English-only notes ("bank", "oil", "oily", "plastic", "materials",
"reach") were recast in Russian terms. The independent read-only review found correctness and scoped coverage
clean, one comprehensibility issue (a 脂 sentence referring to a broad «масло» translation of 石油 that the learner
never sees) and two quiz-safety gaps (ビニール–レコード via colloquial «винил», 水稲–ご飯 via «рис»). They were fixed
together with optional polish (脂 and 流す example translations, the 榛 species name); a ビニール retitle was
declined. The recheck resolved all three findings and the accepted polish with no regressions, leaving all four facets clean.

Qualified progress is **3,369 reviewed-current / 8 reviewed runtime-blocked / 4,901 pending of 8,278**,
with 1,903 words, 718 kanji and 718 strokes. See the [intake](translation-batches/175-words-batch-14-intake.json),
[independent review](translation-batches/175-words-batch-14-independent-review-001.md),
[recheck](translation-batches/175-words-batch-14-recheck-001.md),
[qualified source record](translation-batches/175-words-batch-14-reviewed-source.json) and
[final validation](translation-batches/175-words-batch-14-final-validation-001.json).

## Previous published source milestone: batch174 thirty words (general word queue)

Batch174 adds 30 Russian word articles: 額 総額 中心 中央 半ば 竹 酒 笹 稲穂 研究員 研究者 富 財産 武器 矛 内容 実
果実 ピンク 桃 白桃 いかがわしい 疑わしい 略語 畝 畔 獣医 場 地 陸.
They are chunk 0 of 106 of the general remaining-word queue (recomputed after Batch173: closure of 3,177 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Seven existing pages
(kanji/容 富 酒; words/こと 形式 獣 酔う) receive 13 navigation-only link wraps at EN link positions, with per-file
link counts matching EN. Kanji without RU cards (額 総 央 竹 笹 稲 穂 武 矛 桃 略 畝 畔 獣 陸) stay plain text.

The batch covers amounts and totals, centres and middles, bamboo and rice ears, alcohol, researchers, wealth and
property, weapons and spears, content and fruit, pink and peaches, doubtful and shady things, abbreviations, ridges
and paddy levees, veterinarians, and place, land and dry land. Russian titles that share «сумма», «центр», «середина»,
«плод», «сомнительный», «место» or «земля» receive direct guards; English-only notes ("ear", "ordinance", "vet",
"field", "earth", "furrow") were recast in Russian terms. The independent read-only review found scoped coverage
clean, two correctness issues (a 実 example note implying the discussion might concern fruit, and 地 に described as
direction instead of the endpoint) and a 場–席 quiz-safety gap; a suggested 中央–途中/間 guard was declined as only
transitive. They were fixed together with optional polish (a 地–田舎 guard, 財産 wording, the 中心 title and removal of
English glosses from 場, 地 and 畝). The recheck found all four facets clean, withdrew the transitive 中央 suggestion and judged the new «часть» overlaps of the 中心 title not to be quiz collisions.

Qualified progress is **3,339 reviewed-current / 8 reviewed runtime-blocked / 4,931 pending of 8,278**,
with 1,873 words, 718 kanji and 718 strokes. See the [intake](translation-batches/174-words-batch-13-intake.json),
[independent review](translation-batches/174-words-batch-13-independent-review-001.md),
[recheck](translation-batches/174-words-batch-13-recheck-001.md),
[qualified source record](translation-batches/174-words-batch-13-reviewed-source.json) and
[final validation](translation-batches/174-words-batch-13-final-validation-001.json).

## Previous published source milestone: batch173 thirty words (general word queue)

Batch173 adds 30 Russian word articles: 退屈 くだらない 紙屑 残り 屑 芋 ボート ヨット 典型 例 出来事 事件 ケース 舟 自宅
知恵 知能 感情 胸 腹 脳 育苗 翌日 繭 合計 提案 案 プラン 計 金額.
They are chunk 0 of 107 of the general remaining-word queue (recomputed after Batch172: closure of 3,207 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Thirteen existing pages
(kanji/件 例 型 宅 情 感 腹; words/おなか 愛情 船 苗 蚕 隻) receive 26 navigation-only link wraps at EN link positions,
with per-file link counts matching EN. Kanji without RU cards (典 屈 屑 恵 提 案 繭 翌 胸 脳 舟 芋 苗 額) stay plain text.

The batch covers boredom and worthlessness, waste and remainders, tubers, boats, typical examples and cases, events
and incidents, home, wisdom, intelligence, emotions and the mind, chest and belly, seedlings and cocoons, the next
day, totals and amounts of money, and proposals and plans. Russian titles that share «сумма», «план», «случай», «дом»
or «образец» receive direct guards; English-only notes ("case", "boat/ship/yacht", "plan/proposal/package",
"mind/brain") were recast in Russian terms. The independent read-only review found scoped coverage clean, one
correctness issue (自宅 «собственное жильё» implied ownership), one register issue (腹 «брюхо») and four quiz-safety
gaps (残り–続き, 典型–型, プラン–料金, ケース–出来事). They were fixed together with optional polish (a 計–器具 guard and
提案, 知恵 and 出来事 wording). Recheck 001 resolved all of them with no regressions and found all four facets clean.

Qualified progress is **3,309 reviewed-current / 8 reviewed runtime-blocked / 4,961 pending of 8,278**,
with 1,843 words, 718 kanji and 718 strokes. See the [intake](translation-batches/173-words-batch-12-intake.json),
[independent review](translation-batches/173-words-batch-12-independent-review-001.md),
[recheck](translation-batches/173-words-batch-12-recheck-001.md),
[qualified source record](translation-batches/173-words-batch-12-reviewed-source.json) and
[final validation](translation-batches/173-words-batch-12-final-validation-001.json).

## Previous published source milestone: batch172 thirty words (general word queue)

Batch172 adds 30 Russian word articles: 縞 一種 パターン 独特 特徴 雰囲気 大気 カラー 紐 綱 菊 戦う 戦い 反抗 抵抗 暴れる
狂う 渋滞 混雑 荒れる 茉莉花 田 畑 耕地 田んぼ 苗代 芽 稲 苗 無駄.
They are chunk 0 of 108 of the general remaining-word queue (recomputed after Batch171: closure of 3,237 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Five existing pages
(words/コード 欠点 混乱 色 荒い) receive 5 navigation-only link wraps at EN link positions, with per-file link counts
matching EN. Kanji without RU cards (徴 抗 抵 暴 混 渋 滞 無 狂 独 畑 稲 紐 綱 縞 耕 芽 苗 茉 荒 莉 菊 雰 駄) stay plain text.

The batch covers stripes, kinds and patterns, distinctive features, atmosphere, colour, cords and ropes, fighting and
resistance, rampaging and going wrong, traffic jams and crowds, rough weather, jasmine and chrysanthemums, fields and
rice farming, and waste. Russian titles that share «атмосфера», «поле», «рис», «верёвка» or «тип» receive direct
guards; English-only notes (the "bar" gloss of 縞, jasmine as чубушник, nursery and rice senses) were recast in
Russian terms. The independent read-only review found correctness and scoped coverage clean, five minor
comprehensibility issues (独特, 縞, 混雑, 大気) and one quiz-safety gap (雰囲気 vs 模様 via «обстановка»). They were
fixed with optional example polish and an owner-added 一種–型 guard. Recheck 001 resolved them and raised a 混雑–込む
guard (混雑 is a する-noun) and stray generated `tools/__pycache__` files, both fixed; recheck 002 found all four
facets clean.

Qualified progress is **3,279 reviewed-current / 8 reviewed runtime-blocked / 4,991 pending of 8,278**,
with 1,813 words, 718 kanji and 718 strokes. See the [intake](translation-batches/172-words-batch-11-intake.json),
[independent review](translation-batches/172-words-batch-11-independent-review-001.md),
[recheck](translation-batches/172-words-batch-11-recheck-001.md),
[qualified source record](translation-batches/172-words-batch-11-reviewed-source.json) and
[final validation](translation-batches/172-words-batch-11-final-validation-001.json).

## Previous published source milestone: batch171 thirty words (general word queue)

Batch171 adds 30 Russian word articles: 現在 目下 雛 雑草 隼 隻 鉱石 酉 週末 連休 迷う 辰 諸島 蝶 蛍 カーブ 蛇行 蛇 蚕
植物 植木 グラス 模様 柄 形式 癖 傾向 筋肉 筋 棒.
They are chunk 0 of 109 of the general remaining-word queue (recomputed after Batch170: closure of 3,267 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Nine existing pages
(kanji/傾 式 形 末 草 迷 連 雑 and words/生き物) receive 23 navigation-only link wraps at EN link positions, with per-file
link counts matching EN. Kanji without RU cards (島 柄 棒 植 模 癖 筋 蚕 蛇 蛍 蝶 諸 辰 酉 鉱 隻 隼 雛) stay plain text.

The batch covers time and rank (現在, 目下 read めした), weekends and holidays, getting lost, birds, insects and zodiac
signs, plants, patterns and tendencies, and muscles, lines and sticks. Russian titles that share «выходные» or
«выходной» (週末, 連休, 休み, 休日) receive direct guards; the English-only note on "plant" as a factory was dropped and
the stick/rod/pole note recast as палка/стержень/шест. The independent read-only review found correctness, scoped
coverage and comprehensibility clean and one quiz-safety gap (蚕 vs 蝶: Russian «бабочка» also covers moths, including
the silkworm imago). It was fixed together with optional polish in 傾向, 蝶, 蛍, 目下 and the 蛇行 title; the recheck
resolved every finding with no regressions and all four facets clean.

Qualified progress is **3,249 reviewed-current / 8 reviewed runtime-blocked / 5,021 pending of 8,278**,
with 1,783 words, 718 kanji and 718 strokes. See the [intake](translation-batches/171-words-batch-10-intake.json),
[independent review](translation-batches/171-words-batch-10-independent-review-001.md),
[recheck](translation-batches/171-words-batch-10-recheck-001.md),
[qualified source record](translation-batches/171-words-batch-10-reviewed-source.json) and
[final validation](translation-batches/171-words-batch-10-final-validation-001.json).

## Previous published source milestone: batch170 thirty words (general word queue)

Batch170 adds 30 Russian word articles: ほぼ くらい ころ だけ ばかり 一応 おおざっぱ どたどた 次々 ばたばた 混乱
あわてる そそっかしい のんき 鷹揚 鶴 鴻 鴻鵠 麒麟 鷹 鶏 鵬 鳳凰 鳩 鯨 鯛 鯉 鮎 非常口 後輩.
They are chunk 0 of 110 of the general remaining-word queue (recomputed after Batch169: closure of 3,297 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Six existing pages
(kanji/乱 常 非 and words/ほど 一旦 落ち着く) receive 11 navigation-only link wraps at EN link positions, with per-file
link counts matching EN. Kanji without RU cards (凰 応 揚 混 輩 鮎 鯉 鯛 鯨 鳩 鳳 鴻 鵠 鵬 鶏 鶴 鷹 麒 麟) stay plain text.

The batch covers approximation and limit particles, carelessness and temperament, hurry and confusion, birds, fish
and mythical creatures, and 非常口/後輩. Russian names follow established usage (гуменник, цилинь, Пэн, фэнхуан,
аю, морской карась, «запасный выход»); English-only notes (the lifting crane, pigeon vs dove, "chicken" as coward)
were re-expressed or dropped. The independent read-only review found correctness and scoped coverage clean, one
quiz-safety gap (ばかり «около» vs ほぼ «приблизительно») and two minor wording issues in 後輩 (an editorial «курс(ы)»
shortcut and «пожилой» for "older"). All were fixed, with optional polish in ほぼ and 一応 and conservative ころ
guards; the recheck resolved every finding with no regressions and all four facets clean.

Qualified progress is **3,219 reviewed-current / 8 reviewed runtime-blocked / 5,051 pending of 8,278**,
with 1,753 words, 718 kanji and 718 strokes. See the [intake](translation-batches/170-words-batch-09-intake.json),
[independent review](translation-batches/170-words-batch-09-independent-review-001.md),
[recheck](translation-batches/170-words-batch-09-recheck-001.md),
[qualified source record](translation-batches/170-words-batch-09-reviewed-source.json) and
[final validation](translation-batches/170-words-batch-09-final-validation-001.json).

## Previous published source milestone: batch169 thirty words (general word queue)

Batch169 adds 30 Russian word articles: 永久 永遠 悠々 もやもや めらめら ぼうっと 突然 急に ばったり 思わず ふと
うっかり でこぼこ ごつごつ かさかさ ざらざら 粗い 激しい 荒い 様子 状態 加減 見当 およそ 程度 約 ざっと 一時 少々 一旦.
They are chunk 0 of 111 of the general remaining-word queue (recomputed after Batch168: closure of 3,327 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Fifteen existing pages
(kanji/久 様 状 程 突 and 10 word pages) receive 24 navigation-only link wraps at EN link positions, with per-file
link counts matching EN. Kanji without RU cards (悠 態 旦 永 減 激 粗 荒) stay plain text; four onomatopoeia images
are omitted under the word-only convention.

The batch covers eternity, suddenness and carelessness, rough textures, state/degree and approximation clusters.
The independent read-only review found scoped coverage clean and seven quiz-safety gaps (for example ばったり–出会う,
少々–少ない/気持ち, 様子–具合/場合 and うっかり–思わず), plus low-severity wording issues: the 疲れ加減 gloss,
«на душе неспокойно» in もやもや reading as worry, and English-dependent remarks about the source glosses in
ばったり, 急に and ふと. All were fixed; ざっと and もやもや were retitled rather than guarded («навскидку; бегло
(просмотреть)», «туманный; смутно на душе»). The recheck resolved every finding with no regressions and all four
facets clean.

Qualified progress is **3,189 reviewed-current / 8 reviewed runtime-blocked / 5,081 pending of 8,278**,
with 1,723 words, 718 kanji and 718 strokes. See the [intake](translation-batches/169-words-batch-08-intake.json),
[independent review](translation-batches/169-words-batch-08-independent-review-001.md),
[recheck](translation-batches/169-words-batch-08-recheck-001.md),
[qualified source record](translation-batches/169-words-batch-08-reviewed-source.json) and
[final validation](translation-batches/169-words-batch-08-final-validation-001.json).

## Previous published source milestone: batch168 navigation-only link restoration sweep

Batch168 adds no new cards. Earlier batches translated cards while some EN link targets did not yet exist in RU, so
those mentions stayed plain text. After Batch167 a corpus scan of words/, kanji/ and articles/ found 205 (file, target)
pairs where the frozen EN file links a target that RU now has but the RU file did not. The sweep wraps existing RU
text at the corresponding EN link positions: 198 pairs restored with 202 links in 161 files (including
articles/numbers-and-counters.md). The link-stripped text of every changed file is byte-identical to the baseline; no
title, quiz exclusion or other front matter changed.

Seven pairs stay unlinked: kanji/殺 and kanji/飛 have no RU counterpart for the EN sentence, and the matching positions
in kanji/面, words/落す and words/野菜 already link a different target (a word page instead of the EN kanji page, or the
reverse). The independent read-only review checked all 202 added links against their EN positions and found all four
facets clean. Its optional notes (a link on only 子 inside 椅子 in words/いす, and the pre-existing kind mismatches)
need rewording or retargeting, so they are left for a later content batch.

Qualified progress is unchanged at **3,159 reviewed-current / 8 reviewed runtime-blocked / 5,111 pending of 8,278**
(1,693 words, 718 kanji, 718 strokes); the 161 ledger records carry the refreshed hashes and the sweep evidence. See the
[intake](translation-batches/168-navigation-sweep-01-intake.json),
[independent review](translation-batches/168-navigation-sweep-01-independent-review-001.md) and
[final validation](translation-batches/168-navigation-sweep-01-final-validation-001.json).

Future word batches restore navigation to their own new words at EN link positions in the same batch, so this sweep
should not need repeating except after article or kanji families land. This is qualified source-content progress only.

## Previous published source milestone: batch167 thirty words (general word queue)

Batch167 adds 30 Russian word articles: ぷにぷに ぐにゃぐにゃ 浮く 想像 示す 現す 表す 浮かべる 浮かぶ ふわふわ ほくほく
しっとり 明かり 灯 もちもち 軟らかい 利口 そっと おとなしい 適する 似合う 落ち着く 平気 容易 楽 単純 貧しい 粗末 安易 佚.
They are chunk 0 of 112 of the general remaining-word queue (recomputed after Batch166: closure of 3,357 EN words),
so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Twenty-two existing pages
(kanji/像 易 泳 浮 示 貧 and 16 word pages) receive navigation-only link wraps at EN link positions. Kanji without RU
cards (佚 灯 粗 純 軟) stay plain text; two onomatopoeia images are omitted under the word-only convention.

The batch covers dense soft-texture, float/appear, show/express, light, calm, suit, easy and poor clusters. The
author changed the 現す and 楽 titles to clear exact segment overlaps and added direct guards beyond EN in 15 cards.
The independent read-only review found correctness, scoped coverage and comprehensibility clean, accepted the
Russian-specific notes (for example the two senses of «плавать» for 浮く/泳ぐ), and found four minor quiz-safety gaps
(安易–楽, 単純–易しい, 似合う–いい, ぐにゃぐにゃ–べちゃべちゃ). All were fixed; the recheck resolved them with no
regressions and all four facets clean.

The review also confirmed a pre-existing navigation gap: older pages still show plain text where EN links to
targets that RU now has (a corpus scan finds 203 such link pairs in 167 files). A dedicated navigation-only sweep
batch is scheduled next.

Qualified progress is **3,159 reviewed-current / 8 reviewed runtime-blocked / 5,111 pending of 8,278**,
with 1,693 words, 718 kanji and 718 strokes. See the [intake](translation-batches/167-words-batch-07-intake.json),
[independent review](translation-batches/167-words-batch-07-independent-review-001.md),
[recheck](translation-batches/167-words-batch-07-recheck-001.md),
[qualified source record](translation-batches/167-words-batch-07-reviewed-source.json) and
[final validation](translation-batches/167-words-batch-07-final-validation-001.json).

This is qualified source-content progress only. Tag/random fallback options, voice, drawing, learner, device,
media, release, ordinary activation and full-translation approval are not implied.

## Previous published source milestone: batch166 thirty words (general word queue)

Batch166 adds 30 Russian word articles: 余裕 冷静 平ら 穏やか 管理 仕舞い しまう 済ませる 終える 得る 収める 支払う 支給
供給 配達 計算 勘定 会計 費用 価格 値 料金 代金 支払 納める 治める 安定 もこもこ ぼんやり ふかふか. They are chunk 0
of 113 of the general remaining-word queue (recomputed after Batch165: closure of 3,387 EN words), so every EN
quiz_exclusions target resolves to an existing RU word or a batch word. Eight existing pages (kanji/払 支 治 費,
words/ぶくぶく ぷくぷく 支配 請求) receive navigation-only link wraps at EN link positions. Kanji without RU cards
(価 勘 穏 算 管 納 裕) stay plain text; two onomatopoeia images are omitted under the word-only convention.

The batch is dense in near-synonym clusters (price/fee/cost, payment, finishing, the おさめる homophones, calm and
soft), so the author added direct guards beyond EN in 21 cards. The independent read-only review found correctness,
scoped coverage and comprehensibility clean, accepted the Russian-specific replacements for English-only remarks,
and found three quiz-safety gaps (支払–料金, 会計–計算, 穏やか–柔らかい/ソフト). All were fixed with optional wording
polish, and the recheck resolved everything with no regressions and all four facets clean. Exclusions added beyond
EN are listed with the titles in the qualified source record.

Qualified progress is **3,129 reviewed-current / 8 reviewed runtime-blocked / 5,141 pending of 8,278**,
with 1,663 words, 718 kanji and 718 strokes. See the [intake](translation-batches/166-words-batch-06-intake.json),
[independent review](translation-batches/166-words-batch-06-independent-review-001.md),
[recheck](translation-batches/166-words-batch-06-recheck-001.md),
[qualified source record](translation-batches/166-words-batch-06-reviewed-source.json) and
[final validation](translation-batches/166-words-batch-06-final-validation-001.json).
Next: further general word-queue chunks (recomputed after each merge), interleaved with the held N2 kanji
(B157-held 委 季 封 届 層 岩, B158-held 島 巨 布 希 干 庁 床 底 府, then 庫 and 憎).

This is qualified source-content progress only. Tag/random fallback options, voice, drawing, learner, device,
media, release, ordinary activation and full-translation approval are not implied.

## Previous published source milestone: batch165 thirty words (general word queue)

Batch165 adds 30 Russian word articles: げらげら からから ぷくぷく ぶくぶく ことこと がちゃがちゃ 緊張 おどおど びくびく
はらはら ぴかぴか ちらちら 拍手 叩く ぱちぱち かたかた ゆらゆら 震える がたがた カー ぶうぶう 豚 象 馬 鹿 鼠 兎 獣 者
個人. They are chunk 0 of 114 of the general remaining-word queue (recomputed after Batch164: closure of 3,417 EN
words), so every EN quiz_exclusions target resolves to an existing RU word or a batch word. Ten existing pages
(kanji/個 馬, words/きらきら ぎらぎら つやつや てかてか ぐずぐず ごろごろ 打つ 猪) receive navigation-only link wraps at EN
link positions; words/きらきら also regains its EN-position ぎらぎら and つやつや links. Kanji without RU cards
(兎 叩 張 拍 獣 緊 豚 象 震 鹿 鼠) stay plain text; nine onomatopoeia images are omitted under the word-only convention.

The independent read-only review found scoped coverage clean and four minor defects: the 叩く "dust" sense belongs
to the separate dictionary entry 叩く（はたく）, 震える used a non-glossary spelling of итидан, and かたかた/ことこと
lacked guards against 叩く and ことこと against からから. All were fixed; optional ぶくぶく–沸く and からから–乾く guards
and wording polish in 象 and ぶうぶう were applied, and the recheck resolved everything with no regressions and all
four facets clean. Exclusions added beyond EN are listed with the titles in the qualified source record.

Qualified progress is **3,099 reviewed-current / 8 reviewed runtime-blocked / 5,171 pending of 8,278**,
with 1,633 words, 718 kanji and 718 strokes. See the [intake](translation-batches/165-words-batch-05-intake.json),
[independent review](translation-batches/165-words-batch-05-independent-review-001.md),
[recheck](translation-batches/165-words-batch-05-recheck-001.md),
[qualified source record](translation-batches/165-words-batch-05-reviewed-source.json) and
[final validation](translation-batches/165-words-batch-05-final-validation-001.json).
Next: further general word-queue chunks (recomputed after each merge), interleaved with the held N2 kanji
(B157-held 委 季 封 届 層 岩, B158-held 島 巨 布 希 干 庁 床 底 府, then 庫 and 憎).

This is qualified source-content progress only. Tag/random fallback options, voice, drawing, learner, device,
media, release, ordinary activation and full-translation approval are not implied.

## Previous published source milestone: batch164 thirty words (first general word-queue batch)

Batch164 adds 30 Russian word articles: 生物 生き物 牛 家畜 熊 猪 馬鹿 猿 酔う 酔っ払い 虎 のんびり 回り くるくる
ふらふら うろうろ ぶらぶら ころころ ごろごろ のろのろ 怠ける だらだら 句 文句 不満 不平 ぐずぐず ぐっしょり びしょびしょ
ぐしゃぐしゃ. They are chunk 0 of 115 of the general remaining-word queue: `word_schedule.py 30 --all` orders the
full remaining word closure (3,447 EN words) into dependency-closed chunks, so every EN quiz_exclusions target
resolves to an existing RU word or a batch word. words/しっかり receives a navigation-only link wrap (ふらふら) at
its EN link position. Kanji without RU cards (句 怠 熊 猪 猿 畜 虎 酔 鹿) stay plain text; four onomatopoeia
images are omitted under the word-only convention.

The independent read-only review found correctness and scoped coverage clean and accepted the Russian-specific
replacements for English-only remarks (корова, кабан, пьяница, меня укачало, домашние животные). It found one
moderate quiz-safety gap (文句 vs 反対 «возражение») and one minor comprehensibility defect (句 glossed as «фраза»
without narrowing). Both were fixed, optional wording polish was applied, and the recheck resolved everything with
no regressions. Exclusions added beyond EN (including 生物/生き物–動物) are listed with the titles in the qualified
source record.

Qualified progress is **3,069 reviewed-current / 8 reviewed runtime-blocked / 5,201 pending of 8,278**,
with 1,603 words, 718 kanji and 718 strokes. See the [intake](translation-batches/164-words-batch-04-intake.json),
[independent review](translation-batches/164-words-batch-04-independent-review-001.md),
[recheck](translation-batches/164-words-batch-04-recheck-001.md),
[qualified source record](translation-batches/164-words-batch-04-reviewed-source.json) and
[final validation](translation-batches/164-words-batch-04-final-validation-001.json).
Next: further general word-queue chunks (recomputed after each merge), interleaved with the held N2 kanji
(B157-held 委 季 封 届 層 岩, B158-held 島 巨 布 希 干 庁 床 底 府, then 庫 and 憎).

This is qualified source-content progress only. Tag/random fallback options, voice, drawing, learner, device,
media, release, ordinary activation and full-translation approval are not implied.

## Previous published source milestone: batch163 thirty-five words (final B160 example-word closure batch)

Batch163 adds 35 Russian word articles: 愛情 愛する 愉快 悩む 患者 恋人 快適 延期 広がる 尊重 尊敬 回復 命令
命じる 受け取る 便り 伸びる 伸ばす がっかり 器具 食器 規律 瀬戸物 拝む 担ぐ 承る 戸棚 憧れる 恋しい 快晴 往復
弱点 延長 失恋 井戸. They are the final dependency-closed chunk of the quiz-exclusion closure of Batch160's
plain-text example words, so every example word of the Batch160 kanji now has a Russian article. Twenty-three
existing pages (kanji/令 伸 尊 延 弱 律 復 快 恋 患 悩 戸 承 担 拝, words/しょんぼり 依頼 失望 感心 拡大 機械 注文
見送り) receive navigation-only link wraps at EN link positions; kanji/拝 also regains its EN-position 拝見 link.
Kanji without RU cards (井 器 往 愉 憧 敬 棚 瀬) stay plain text.

The independent read-only review found correctness and scoped coverage clean, two low quiz-safety gaps
(伸びる–増える, 愉快–明るい) and one low comprehensibility defect (the 瀬戸物 literal-reading gloss). All were
fixed, optional wording polish was applied, and the recheck resolved everything with no regressions. Exclusions
added beyond EN are listed with the titles in the qualified source record.

Qualified progress is **3,039 reviewed-current / 8 reviewed runtime-blocked / 5,231 pending of 8,278**,
with 1,573 words, 718 kanji and 718 strokes. See the [intake](translation-batches/163-words-batch-03-intake.json),
[independent review](translation-batches/163-words-batch-03-independent-review-001.md),
[recheck](translation-batches/163-words-batch-03-recheck-001.md),
[qualified source record](translation-batches/163-words-batch-03-reviewed-source.json) and
[final validation](translation-batches/163-words-batch-03-final-validation-001.json).
Next: the general word queue in dependency-closed chunks, interleaved with the held N2 kanji
(B157-held 委 季 封 届 層 岩, B158-held 島 巨 布 希 干 庁 床 底 府, then 庫 and 憎).

This is qualified source-content progress only. Tag/random fallback options, voice, drawing, learner, device,
media, release, ordinary activation and full-translation approval are not implied.

## Previous published source milestone: batch162 thirty words (second B160 example-word closure batch)

Batch162 adds 30 Russian word articles: 設備 見送り 装置 苦手 芝居 続き 欠点 欠陥 粗 競技 皿 成長 発展 発達 演技
方法 手段 法 決定 決まり 機械 整理 支配 拡大 担当 技師 承認 感心 愛 恋. They form the second dependency-closed
chunk of the quiz-exclusion closure of Batch160's plain-text example words. Eight existing pages (kanji/担 承 技 恋
愛 法, words/式 許可) receive navigation-only link wraps at EN link positions. Kanji without RU cards
(展 拡 整 械 皿 競 粗 芝 装 設 陥) stay plain text.

The independent read-only review found one minor correctness defect (続き overstated that it never names a
sequel) and five minor quiz-safety gaps (皿–料理, 苦手–弱い, 方法–泳ぎ方, 決まり–約束, 法–規則), following
existing RU precedents. All were fixed and resolved in the recheck with no regressions; optional wording and
guard polish was applied or declined with reasons. Exclusions added beyond EN are listed with the titles in the
qualified source record.

Qualified progress is **3,004 reviewed-current / 8 reviewed runtime-blocked / 5,266 pending of 8,278**,
with 1,538 words, 718 kanji and 718 strokes. See the [intake](translation-batches/162-words-batch-02-intake.json),
[independent review](translation-batches/162-words-batch-02-independent-review-001.md),
[recheck](translation-batches/162-words-batch-02-recheck-001.md),
[qualified source record](translation-batches/162-words-batch-02-reviewed-source.json) and
[final validation](translation-batches/162-words-batch-02-final-validation-001.json).
The remaining 35 words of that closure (愛情 愛する 愉快 悩む 患者 恋人 快適 延期 広がる 尊重 尊敬 回復 命令
命じる 受け取る 便り 伸びる 伸ばす がっかり 器具 食器 規律 瀬戸物 拝む 担ぐ 承る 戸棚 憧れる 恋しい 快晴 往復
弱点 延長 失恋 井戸) follow in the next word batch.

This is qualified source-content progress only. Tag/random fallback options, voice, drawing, learner, device,
media, release, ordinary activation and full-translation approval are not implied.

## Previous published source milestone: batch161 thirty words (first B160 example-word closure batch)

Batch161 adds 30 Russian word articles: 予想 疲れ くたくた へとへと ぐったり ぼろぼろ しんみり 失望 沈む しょんぼり
注文 条件 予期 期待 意思 依頼 希望 望み 望む 求める 要求 請求 願い 願う 番 順番 順 頂戴 賛成 許可. They form the
first dependency-closed chunk of the quiz-exclusion closure of Batch160's plain-text example words: every EN
`quiz_exclusions`/`quiz_distractors` target is an existing RU word or a batch word. Thirteen existing kanji/word
pages receive navigation-only link wraps at EN link positions (kanji/想 also regains its EN link to 相).
ぼろぼろ, しんみり and しょんぼり are word-only adaptations without the optional image fields.

The independent read-only review found no defects and judged all 30 words CLEAN on correctness, scoped coverage,
Russian comprehensibility and quiz safety, including the 41 remaining stem overlaps. One optional consistency
exclusion (くたくた–ソフト) was applied; the other optional items were withdrawn in the recheck. Exclusions added
beyond EN are listed with the titles in the qualified source record.

Qualified progress is **2,974 reviewed-current / 8 reviewed runtime-blocked / 5,296 pending of 8,278**,
with 1,508 words, 718 kanji and 718 strokes. See the [intake](translation-batches/161-words-batch-01-intake.json),
[independent review](translation-batches/161-words-batch-01-independent-review-001.md),
[recheck](translation-batches/161-words-batch-01-recheck-001.md),
[qualified source record](translation-batches/161-words-batch-01-reviewed-source.json) and
[final validation](translation-batches/161-words-batch-01-final-validation-001.json).
The remaining 65 words of that closure (planned as chunks of 30, 30 and 5) follow in later word batches.

This is qualified source-content progress only. Tag/random fallback options, voice, drawing, learner, device,
media, release, ordinary activation and full-translation approval are not implied.

## Previous published source milestone: batch160 thirteen N2 kanji (B159 held drafts promoted)

Batch160 adds Russian lessons and byte-identical frozen strokes for 延/弱/律/復/快/恋/患/悩/戸/承/技/担/拝,
starting from the held B159 drafts, plus one required kanji link wrapper in each of eight existing words
(弱い, 復習, 戸, 承知, 技術, 拝見, 法律, 雨戸). 庫 and 憎 stay outside the batch. No quiz or grading code changed.

The independent read-only review found eight minor defects (one 延べる sense, 悩ましい sense numbering,
the ウケる direction, a 戻 gloss, two references to RU word articles that do not exist, one illogical 担う
note and an English-only pun on 患者). All were resolved in the recheck with no regressions. Every one of
the 39 declared quiz directions was judged safe against the current Russian titles. To avoid exact overlaps
introduced by the Russian wording, three titles were adapted: 患 «недуг; страдать от болезни», 承 «принимать;
соглашаться» and 技 «навык; мастерство». The overlaps inherited from EN, 律/法 «закон» and 復/再 (repetition),
are qualified; neither pair is in a distractor relation. Twenty-eight example words that have no Russian page
yet remain plain text.

Qualified progress is **2,944 reviewed-current / 8 reviewed runtime-blocked / 5,326 pending of 8,278**,
with 1,478 words, 718 kanji and 718 strokes. The checkpoint authority remains null and `Ready` remains false.
See the [intake](translation-batches/160-n2-batch-09-intake.json),
[independent review](translation-batches/160-n2-batch-09-independent-review-001.md),
[recheck and reconciliation](translation-batches/160-n2-batch-09-recheck-001.md),
[qualified source record](translation-batches/160-n2-batch-09-reviewed-source.json) and
[final validation](translation-batches/160-n2-batch-09-final-validation-001.json).
Batch158 (州/巻/帯/帽/幅/幼) was published through PR #40 with its own evidence under `translation-batches/158-*`.

This is qualified source-content progress only. Tag/random fallback options, voice, drawing, learner, device,
media, release, ordinary activation and full-translation approval are not implied.

## Continuation plan after the November 2026 takeover

The streamlined loop below follows the written rules in `.github/copilot-instructions.md`, which do not fix
a reviewer count:

1. Draft one dependency-closed batch from frozen EN `6af98cb`, using held drafts only as starting material.
2. Screen kanji closure, exact title overlaps and 5-letter stem overlaps against the whole RU pool, and EN↔RU
   link parity.
3. Make a signed candidate commit.
4. Have one independent read-only reviewer check correctness, scoped coverage, Russian comprehensibility and
   every declared distractor direction against the displayed RU titles.
5. Apply the fixes and have a reviewer of the same model family recheck them with the stored report and the
   exact diff. Write a reconciliation that marks each finding resolved, partially resolved, unresolved,
   withdrawn or optional.
6. Update the ledger and regenerate the manifest and progress files.
7. Run serial validation, open a PR, check CI on the exact `main` commit and record publication verification.

The app removes only options whose titles are exactly identical, and kanji cards have no quiz-exclusion field.
Russian kanji titles therefore avoid overlaps that the translation itself would introduce. Overlaps inherited
from EN are recorded as qualifications.

Remaining order (R4, then R5/R6):

1. Finish the N2 kanji: the B157 holds 委/季/封/届/層/岩, the B158 holds 島/巨/布/希/干/庁/床/底/府, then
   庫/憎 and the rest. The `handoff-ru-held-20261117` drafts (named b157–b162) are unreviewed starting material.
2. A word batch for missing example words, such as Batch160's 28 plain-text words, to restore kanji↔word links.
3. The 82 N1 kanji.
4. Words in the order N3 → N2 → N1/unlabelled.
5. Articles, grammar, curriculum and counters alongside the units they support.
6. Scenes and images.
7. Listening, as non-runtime drafts under `docs/` only.

The kanji `quiz_exclusions` validator support (B155), paid media, RU activation and device/IME claims remain
out of scope until the owner authorizes them.

## Previous published source milestone: batch157 nine-card qualified-source acceptance

Batch157 adds Russian lessons and byte-identical frozen strokes for 孫/宇/宝/寺/専/将/尊/導/岸,
plus three reciprocal, link-only word-page changes. Six cards (委/季/封/届/層/岩) remain held
and were not copied. No quiz or grading behavior changed.

The bounded independent review found no new substantive discrepancy. Reading/sense coverage remains
non-exhaustive for 宇/専/尊/導/岸, visual-confusion risk is untested, and this is not semantic CLEAN
or learner acceptance. The signed candidate is `d3f0907b7dbb895b948556370e789a5dde7c2094`,
content version `6eb5aadef3ed81b1`. The signed qualified-source acceptance commit
`47b599b8298307def5cfd9b2e976f23006c33cfa` was fast-forwarded directly to `main` as owner
`stop-cran`; no pull request was created. Serial manifest, validator, 124-test, and content-budget
checks passed. Exact-main CI passed in run
[43236330540](https://github.com/stop-cran/learning-japanese-ru/actions/runs/43236330540).

Qualified progress is **2,906 reviewed-current / 8 reviewed runtime-blocked / 5,364 pending of
8,278**, with 1,478 words / 699 kanji / 699 strokes. Checkpoint authority remains null and `Ready`
false. See the [independent review](translation-batches/157-nine-card-independent-review-001.md),
[qualified source record](translation-batches/157-nine-card-reviewed-source.json),
[final validation](translation-batches/157-nine-card-final-validation-001.json), and
[publication verification](translation-batches/157-nine-card-publication-verification-001.json).

All 27 direct negative/fallback directions remain **UNVERIFIED**. The one bounded synthetic pool
screen is not learner, ASR, drawing, device, semantic-CLEAN, or release evidence. This is qualified
source-content progress only; no grading, runtime, device, media, release, ordinary-activation, or
full-translation approval is implied.

## Previous published source milestone: batch145 lose, wealth, poor, blame, expense, resource and approval kanji

Batch145 adds Russian lessons and byte-identical frozen strokes for 負/財/貧/責/費/資/賛,
plus two exact reciprocal word-page links. Eleven optional links to absent Russian word pages
were omitted without removing their visible Japanese. No quiz or grading behavior changed.
The first read-only review reported one medium grade issue for 費; focused follow-up withdrew
it after the official MEXT table confirmed `費5 ヒ`. The grade-5 tag is supported, and no
lesson correction was warranted.

The signed candidate is `6cb20cdce4e657d51632dbd74665473a6de4e853`, content version
`451870c9d2acb3df`. The qualified acceptance commit
`48359a5ae815e5af7d9293eba601f2d418853b7a` was fast-forwarded directly to `main` as owner
`stop-cran`; no pull request was created. Serial manifest, validator, 124-test, and
content-budget checks passed. Qualified progress is **2,642 reviewed-current / 2 excluded
reviewed runtime-blocked / 5,634 pending of 8,278**, with 1,478 words / 567 kanji / 567
strokes. Exact-main CI passed in run
[43002902105](https://github.com/stop-cran/learning-japanese-ru/actions/runs/43002902105).
Checkpoint authority remains null and `Ready` false.

See the [independent review](translation-batches/145-lose-wealth-poor-blame-expense-resource-approval-kanji-independent-review-001.md),
[qualified source record](translation-batches/145-lose-wealth-poor-blame-expense-resource-approval-kanji-reviewed-source.json),
[final validation](translation-batches/145-lose-wealth-poor-blame-expense-resource-approval-kanji-final-validation-001.json),
and [publication verification](translation-batches/145-lose-wealth-poor-blame-expense-resource-approval-kanji-publication-verification-001.json).
All 21 direct negative/fallback directions remain **UNVERIFIED**. No runtime, device, media,
release, ordinary-activation, or full-translation approval is implied.

## Previous published source milestone: batch144 explain, investigate, discuss, argue, know, warn and deliberate kanji

Batch144 added Russian lessons and byte-identical frozen strokes for 説/調/談/論/識/警/議,
plus nine exact navigation-only word-page links. The validator exposed five reciprocal links
from existing word pages to the new kanji cards; their single-wrapper changes were authorized
in a supplemental pre-mutation amendment. Eight optional links to absent word pages were
omitted without removing their visible Japanese. No quiz or grading behavior changed.

The independent bounded review found no actionable issue. The signed candidate was
`43b1e11db458b9379bf67b5571f8d597ccdd2f46`, content version `f7f520d85e56fcab`.
Qualified progress after adoption was **2,628 reviewed-current / 2 excluded reviewed
runtime-blocked / 5,648 pending of 8,278**, with 1,478 words / 560 kanji / 560 strokes.
The signed acceptance commit `375ea10c482219a6b9dc586ba322510a03d3cd0f` was fast-forwarded
to `main`; exact-main CI passed in run
[42997309964](https://github.com/stop-cran/learning-japanese-ru/actions/runs/42997309964).
See the [publication verification](translation-batches/144-explain-investigate-discuss-argue-know-warn-deliberate-kanji-publication-verification-001.json).

## Previous published source milestone: batch143 solve, record, visit, permit, recognize and error kanji

## Batch143: published qualified source acceptance

Batch143 adds complete Russian lessons and byte-identical frozen stroke assets
for 解/記/訪/許/認/誤, plus four exact NAV-only wrappers in existing word
pages. Eleven optional wrappers to unavailable word pages were omitted with
their visible Japanese text retained. The initial independent review found one
medium reading transcription error (`も` for `もと`) in `kanji/許.md`; a
pre-mutation amendment authorized the single-line correction, and focused
follow-up review confirmed it resolved the finding. No quiz or grading behavior
changed.

The signed freeze is `fe57e10d031f9d308312c1354639df488084d237`; the signed
candidate is `d206576631135f27b43fd0136d18652cb2ba96fc`, content version
`fdcb38de679a3f19`. The exact manifest delta is 12 new lesson/stroke
registrations and four navigation word-page hash changes; no entries were
removed or unrelated hashes changed. Serial manifest, validator, 124-test, and
content-budget checks passed.

Qualified progress is now **2,614 reviewed-current / 2 excluded reviewed
runtime-blocked / 5,662 pending of 8,278**, with 1,478 words / 553 kanji / 553
strokes. The signed qualified-acceptance commit
`e82c86a6949b57394e61c7e029b99edba8db79ef` was fast-forwarded to `main`;
exact-main CI passed. See the [independent review](translation-batches/143-solve-record-visit-permit-recognize-error-kanji-independent-review-001.md),
[correction follow-up](translation-batches/143-solve-record-visit-permit-recognize-error-kanji-independent-review-follow-up-001.md),
[qualified source record](translation-batches/143-solve-record-visit-permit-recognize-error-kanji-reviewed-source.json),
[final validation](translation-batches/143-solve-record-visit-permit-recognize-error-kanji-final-validation-001.json),
and [publication verification](translation-batches/143-solve-record-visit-permit-recognize-error-kanji-publication-verification-001.json).
C1/C3 are CLEAN only within the cited bounded review scope; all 18 direct
negative/fallback directions remain **UNVERIFIED**. Checkpoint authority remains
null and `Ready` false. Runtime, device, media, release, ordinary-activation,
and full-translation approval are not implied.

## Previous published source milestone: batch142 technique, surface, necessity, standard, memory and observation kanji

## Batch142: published qualified source acceptance

Batch142 adds complete Russian lessons and byte-identical frozen stroke assets
for 術/表/要/規/覚/観, plus nine exact NAV-only wrappers in existing word
pages. Thirteen optional wrappers to unavailable word pages were omitted with
their visible Japanese text retained. The independent bounded review found no
actionable lesson or navigation-text issue; a generated-manifest scope note and
a correction to six inaccurate intake byte counts are recorded separately.

The signed pre-mutation freeze is `7948afecf4a2733bc0cd5d0f97f1b60c8b3d9832`;
the signed navigation amendment is `b54e4742295a89cf604f50b457dddd9c466d1d69`;
the signed runtime candidate is `4f5e7d6dfb1ea2b7a353081c7675a7e0b8edae17`,
content version `32c09d9b1877d294`. The reused 2026-314 dictionary captures
are supplemental and do not match the frozen dictionary snapshot.

Qualified progress is now **2,602 reviewed-current / 2 excluded reviewed
runtime-blocked / 5,674 pending of 8,278**, with 1,478 words / 547 kanji / 547
strokes. Serial manifest, validator, 124-test, and content-budget checks passed.
C1/C3 are CLEAN only within the cited bounded review scope. All 18 direct
negative/fallback directions remain **UNVERIFIED**. Checkpoint authority remains
null and `Ready` false. The signed qualified-acceptance commit
`2a6fd1a4d1e110cdb21613807f226c3784986729` was fast-forwarded to `main`;
exact-main CI passed. See the [publication verification](translation-batches/142-technique-surface-necessity-standard-memory-observation-kanji-publication-verification-001.json).
Runtime, device, media, release, ordinary-activation, and full-translation
approval are not implied.

## Batch141: published qualified source acceptance

Batch141 adds complete Russian lessons and byte-identical frozen stroke assets
for 若/苦/草/落/葉/薬. Ten existing word pages received only the exact
navigation wrappers authorized by the validator-driven amendment; six optional
wrappers to unavailable word pages were omitted. The validator reports no
errors, and the independent review found no actionable translation,
metadata/invariant, or scope issues within its bounded scope.

The signed pre-mutation freeze is `445f33898fc56d6b9761333960f418d32043c5ea`;
the signed navigation amendment is `60a55a3144c9ee622afe51dff64926b50d1bb56a`;
the signed runtime candidate is `f438d3abbe1d6335997e5af30fdae8b774dff9b2`,
content version `3cb652cb2852209a`. The reused 2026-314 dictionary captures
are supplemental and do not match the frozen dictionary snapshot.

At batch141, qualified progress was **2,590 reviewed-current / 2 excluded
reviewed runtime-blocked / 5,686 pending of 8,278**, with 1,478 words / 541
kanji / 541 strokes. The signed qualified-acceptance commit
`dd9450df35953c5faf4df8047f1ff099a9c73815` is on `main`; exact-main CI passed.
C1/C3 are CLEAN only within the cited, bounded review scope.
Ordinary quiz negative/fallback safety remains **UNVERIFIED** for all 18 direct
directions. Checkpoint authority remains null and `Ready` false; publication,
runtime, device, media, release, ordinary-activation, and full-translation
approval are not implied.

## Batch140: qualified source acceptance recorded, publication pending

Batch140 adds complete Russian lessons and byte-identical frozen stroke assets
for 育/背/能/腹/舞/船. Scope also includes seven exact NAV-only wrappers on
existing word pages, including five validator-driven wrappers frozen in signed
amendment 003. Optional wrappers to unavailable word pages were removed in 12
exact occurrences while preserving visible Japanese labels and learner text.

The signed pre-mutation freeze is `9eaef26e0541d7d626c88a8cc9e9f8a0d6938b74`;
signed runtime candidate is `5b38a2929c8684f1518f4e8deee8f30f9f7fc572`,
content version `84b0a2e1289d2257`. Independent review 001 reported C1/C2 clean
within reviewed scope and one C3 wording issue; signed amendment 004 fixed it,
and focused follow-up 002 marked the C3 issue resolved. C2 ordinary
negative/fallback safety remains **UNVERIFIED** for all 18 direct directions.

Qualified progress is now **2,578 reviewed-current / 2 excluded reviewed
runtime-blocked / 5,698 pending of 8,278**, with 1,478 words / 535 kanji / 535
strokes. Checkpoint authority remains null and `Ready` false.

Batch135 adds complete Russian lessons and byte-identical frozen-source stroke
assets for 疑/登/皆/盗/直, plus six preauthorized NAV-only wrappers on existing
word pages. No word teaching content, quiz arrays, or grading behavior changed.

The bounded review’s C2-01 source-comparison omission was resolved by restoring
only the two authorized frozen-source visual-comparison paragraphs. C1 remains
**UNVERIFIED** for the 疑う/疑問 nuance about possible person or assertion targets
and a question not necessarily already spoken; the captured lexical evidence
does not establish those distinctions, and no error was confirmed. C2 scope and
navigation are consistent, but all 15 ordinary negative/fallback directions
remain **UNVERIFIED**. C3 is CLEAN only within the five lessons’ reviewed
novice-clarity scope, not native-speaker certification.

The [qualified source record](translation-batches/135-doubt-climb-everyone-steal-repair-kanji-reviewed-source.json),
[final validation](translation-batches/135-doubt-climb-everyone-steal-repair-kanji-final-validation-001.json),
and [publication verification](translation-batches/135-doubt-climb-everyone-steal-repair-kanji-publication-verification-001.json)
record **2,516 reviewed-current / 2 excluded reviewed runtime-blocked / 5,760
pending of 8,278**, with 1,478 words / 504 kanji / 504 strokes. Content version
is `0400f33e92a4959d`; checkpoint authority remains null and `Ready` false. PR
[#21](https://github.com/stop-cran/learning-japanese-ru/pull/21) merged at main
`2c5afc95fc9cea2740f574b0d53b0603ce8d338b`; exact-main CI passed, public ZIP and
tar.gz exports matched the exact Git archive path-by-path and byte-for-byte, all
four protected refs remained unchanged, and issue #3 progress was updated.
This is qualified source-content progress only, not grading, runtime, device,
media, release, ordinary-activation, checkpoint, or full-translation approval.

## Latest published source milestone: batch136 mutual certainty, show, department, extent and kind

The next six pending kanji in the frozen N3 source order, 相/確/示/科/程/種,
have been authored as complete Russian lessons with six byte-identical frozen
stroke assets. Five existing word pages received only the preauthorized NAV
wrappers; optional links to six absent word-card targets and one absent article
cross-reference were omitted while their substantive teaching content was
preserved.

The [batch136 intake](translation-batches/136-mutual-certainty-show-department-extent-kind-kanji-intake.json),
[source adjudication and semantic freeze](translation-batches/136-mutual-certainty-show-department-extent-kind-kanji-source-adjudication-and-semantic-freeze-001.json),
and [pre-mutation navigation amendment](translation-batches/136-mutual-certainty-show-department-extent-kind-kanji-pre-mutation-navigation-amendment-001.json)
were committed and pushed before learner-content mutation in signed commit
`8aa5f8d5a98d10af7992a6a5517ae186f26aa85a`. The candidate manifest version is
`c7cdeb30962724ec`. The original independent review found C1 CLEAN within its
bounded evidence, C2 UNVERIFIED overall (including all 18 ordinary quiz
directions), and a novice-clarity C3-01 finding. A signed pre-mutation
terminology amendment (`85abf691e98b46f2320cfcf0fcb7382e1772e183`) authorized
one short explanation in each lesson; a focused C3-only follow-up found that
finding addressed, qualified. The amended runtime candidate is signed and
pushed as `b9eaf3c544ad7d232bf6c6be23ca62748262cd7a`. The [qualified source
record](translation-batches/136-mutual-certainty-show-department-extent-kind-kanji-reviewed-source.json)
and [final validation](translation-batches/136-mutual-certainty-show-department-extent-kind-kanji-final-validation-001.json)
record 2,528 reviewed-current / 2 excluded reviewed runtime-blocked / 5,748
pending of 8,278, with 1,478 words / 510 kanji / 510 strokes; content version
is `c7cdeb30962724ec`. PR [#22](https://github.com/stop-cran/learning-japanese-ru/pull/22)
merged at main `a9ba83522d20b23fd6d76bd5300b37b9a2fc9494`; exact-main CI run
[#42869365222](https://github.com/stop-cran/learning-japanese-ru/actions/runs/42869365222)
passed. Public commit/main ZIP and tar.gz exports matched the exact Git archive
path-by-path and byte-for-byte, all four protected pilot/integration refs
remained unchanged, and [issue #3 progress](https://github.com/stop-cran/learning-japanese-ru/issues/3#issuecomment-6774953297)
was updated. See the [publication verification](translation-batches/136-mutual-certainty-show-department-extent-kind-kanji-publication-verification-001.json).
All 18 ordinary negative/fallback directions remain **UNVERIFIED**. No grading,
runtime, device, media, release, ordinary-activation, checkpoint, or completion
approval is implied.

## Batch137: published qualified source milestone

From published main `a9ba83522d20b23fd6d76bd5300b37b9a2fc9494`, the first six
pending kanji in the frozen N3 order are 積/突/窓/笑/等/箱 (positions 255–260).
The direct dependency closure adds 精 (position 262) because it is a direct
distractor of 積; 米 (position 261) remains pending. The signed freeze is
`b79554c58aa172efd04bda95f0adac65887c76e2`. Amendment 001 authorized four
NAV-only word-page wrappers and eight optional-link wrapper removals.
After the candidate validator exposed five more existing word articles whose
newly available kanji cards needed navigation, amendment 002 froze those exact
five NAV-only wrappers before their mutation; it was signed and pushed as
`8a17c8101c103a70cbdded2027aa8d12f9bf493e`.

The seven complete Russian lessons and byte-identical frozen-source stroke
assets are in signed candidate commit
`fe9b22de0a65bed95387e87674861ac80f5078fa`, content version
`885c9d2367c2c322`. Nine existing word pages contain only the authorized
navigation wrappers; no word pages, quiz arrays, or grading behavior were
added or changed. The [independent review](translation-batches/137-accumulation-sudden-window-laughter-equality-box-refinement-kanji-independent-review-001.md)
and [receipt](translation-batches/137-accumulation-sudden-window-laughter-equality-box-refinement-kanji-independent-review-receipt-001.json)
record C1 CLEAN and C3 CLEAN only within the reviewed evidence/scope; C2 remains
UNVERIFIED overall. All 21 ordinary negative/fallback directions remain
**UNVERIFIED**; no grading approval is implied.

Batch137 was integrated through [PR #23](https://github.com/stop-cran/learning-japanese-ru/pull/23)
at main `4d961b89035f65cc45c4fc797bb703d8ee1f3c5e`. The owner-signed
acceptance commit `cf23544fdd8e83ce5ad5ef647044dad019f0fb6f` has the same tree
as published main. Exact-main `validate` run
[#42878097114](https://github.com/stop-cran/learning-japanese-ru/actions/runs/42878097114)
passed. The actual public commit/main ZIP and tar.gz exports matched the exact
Git archive path-by-path and byte-for-byte; all four protected pilot/integration
refs remained unchanged, and [issue #3 progress](https://github.com/stop-cran/learning-japanese-ru/issues/3#issuecomment-6776152214)
was updated. See the [publication verification](translation-batches/137-accumulation-sudden-window-laughter-equality-box-refinement-kanji-publication-verification-001.json).

The published record shows **2,542 reviewed-current / 2 excluded reviewed
runtime-blocked / 5,734 pending of 8,278**, with 1,478 words / 517 kanji / 517
strokes; checkpoint authority remains null and `Ready` false. This is qualified
source-content progress only, not grading, runtime, device, media, release,
ordinary-activation, checkpoint, or full-translation approval.

## Batch138: published qualified source acceptance

Batch138 adds complete Russian lessons and byte-identical frozen-source stroke
assets for 米/経/給/絵/絶/続, with six preauthorized NAV-only wrappers on
existing word pages. No word teaching text, quiz data, or grading behavior
changed. The signed pre-mutation freeze is
`7bc7f54548d67b2dc3ccffdf5e4187987addf60d`; the signed runtime candidate is
`688ff2f7b6d4c2f1de341ceead78a2690922eb6a`, content version
`3fdd9e27d77b03c9`. The bounded review records C1 and C2 **UNVERIFIED** overall
and C3 CLEAN only within the six reviewed lessons. All 18 ordinary
negative/fallback directions remain **UNVERIFIED**; no grading approval is
implied.

Qualified progress is **2,554 reviewed-current / 2 excluded reviewed
runtime-blocked / 5,722 pending of 8,278**, with 1,478 words / 523 kanji / 523
strokes. Owner-signed acceptance `506f04560b009d936240a906b523e0235079faa2`
was published through [PR #24](https://github.com/stop-cran/learning-japanese-ru/pull/24)
at main `e1184136fc186e5f224f1f780dfd890875f4e15c`; exact-main CI run
[#42886500479](https://github.com/stop-cran/learning-japanese-ru/actions/runs/42886500479)
passed. Actual public commit/main ZIP and tar.gz exports matched the exact Git
archive path-by-path and byte-for-byte, all four protected pilot/integration
refs remained unchanged, and issue #3 progress was updated. See the [publication
verification](translation-batches/138-rice-experience-salary-picture-end-and-continue-kanji-publication-verification-001.json).
The excluded `docs/translation-drafts/033-nature-outdoor-activity/words/空.md`
remains preserved. Continue every remaining safe batch; no runtime, device,
media, release, ordinary-activation, checkpoint, or full-translation approval
is implied.

## Batch139: qualified source acceptance recorded, publication pending

Batch139 adds complete Russian lessons and byte-identical frozen-source stroke
assets for 緒/罪/置/美/老/職, with four preauthorized NAV-only wrappers on
existing word pages. Nine optional wrappers to unavailable word targets were
omitted while preserving visible Japanese labels and all learner-facing text.
No new word pages, quiz data, or grading behavior changed.

The signed pre-mutation freeze is `3176366a836108f05398dc752c2fc037d0eb0ac4`.
Independent review 001 found bounded C1 CLEAN, C2 UNVERIFIED overall (all 18
ordinary negative/fallback directions remained UNVERIFIED), and a C3
novice-clarity finding about unexplained on/kun terminology. A signed
pre-mutation terminology amendment
`96d3484e8311bb793f5a5793a827bbdf2a93e05b` authorized only that clarification;
focused follow-up review 002 marked the finding resolved without widening C1/C2
scope. The signed runtime candidate is
`020b8fc924b33c3b132665060e80bc6b453ee86d`; content version
`87be278411d3648a`.

The [qualified source record](translation-batches/139-thread-crime-place-beauty-age-work-kanji-reviewed-source.json),
[review receipt](translation-batches/139-thread-crime-place-beauty-age-work-kanji-independent-review-receipt-001.json),
and [final validation](translation-batches/139-thread-crime-place-beauty-age-work-kanji-final-validation-001.json)
record **2,566 reviewed-current / 2 excluded reviewed runtime-blocked / 5,710
pending of 8,278**, with 1,478 words / 529 kanji / 529 strokes. This is
qualified source progress only; publication verification, exact-main CI,
public-archive checks, protected-ref checks, and issue-progress update remain
pending for this batch.

Publication completed via [PR #25](https://github.com/stop-cran/learning-japanese-ru/pull/25):
owner-signed acceptance `57866956ae4f2266d34044aa35a32931accc7268` merged at
main `106f6e54360898bc71bc8a73f4f30aa5c26702f1`; exact-main CI run
[#42896225664](https://github.com/stop-cran/learning-japanese-ru/actions/runs/42896225664)
passed. Actual public ZIP/tar.gz exports matched exact `git archive`
path-by-path and byte-for-byte, all four protected refs remained unchanged, and
issue #3 progress was updated. See the [publication verification](translation-batches/139-thread-crime-place-beauty-age-work-kanji-publication-verification-001.json).

## Previous published source milestone: batch134 smoke, cat, birth, stay and turn kanji

Batch134 was integrated through
[PR #20](https://github.com/stop-cran/learning-japanese-ru/pull/20) at main
`8f1e1900f5d5165391fb229dcaa5bee2a5ddec9c`; the exact-main `validate` check
completed successfully. A detailed public-archive/protected-ref verification
record was not found during batch135 reconciliation and is not claimed here.
Batch135 followed this milestone. This baseline does not imply
runtime/device/release approval or completion of the frozen translation.

## Previous published source milestone: batch131 heat, fatigue, pain, sleep and condition kanji

Batch131 adds ten complete Russian lessons (熱/疲/痛/眠/状/点/然/破/犯/石),
ten byte-identical frozen-source stroke assets, and thirteen NAV-only word-page
updates. No word page or quiz/grading behavior was added; five unavailable RU
word pages retain their visible Japanese terms without dangling links.

The bounded review found no supported findings. C1 is UNVERIFIED overall
despite verified source fidelity and partial primary-capture confirmation; C2
remains UNVERIFIED for all 30 ordinary negative/fallback directions; C3 is
UNVERIFIED and is not native-speaker certification.

The [qualified source record](translation-batches/131-heat-fatigue-pain-sleep-condition-kanji-reviewed-source.json)
records **2,484 reviewed-current / 2 excluded reviewed runtime-blocked / 5,792
pending of 8,278**, with 1,478 words / 488 kanji / 488 strokes. Version
`d8a791473ae509d9`; checkpoint authority remains null and `Ready` false. PR
[#15](https://github.com/stop-cran/learning-japanese-ru/pull/15) integrated at
main `5c2ac0f4a541136caeba3cbd3154fc3aba0ccc65`. Exact-main CI and actual public
ZIP/tar.gz exports passed, all four protected refs were unchanged, and issue #3
progress was updated. See the [publication verification](translation-batches/131-heat-fatigue-pain-sleep-condition-kanji-publication-verification-001.json).
This was qualified source progress only. Batch132 supersedes it as the current
published milestone; see above.

## Previous published source milestone: batch130 crossing, harbor, fullness and performance kanji

Batch130 adds four complete Russian frozen-community N3 lessons (渡/港/満/演),
four byte-identical frozen-source stroke assets, and five authorized NAV-only
wrappers on existing word pages. Seven unavailable-link wrappers were removed
while their Japanese text was retained; no word pages were added and quiz/runtime
behavior did not change.

The bounded text-only report found no supported findings, but C1, C2 and C3 all
remain **UNVERIFIED**. In particular, all 12 ordinary negative/fallback quiz
directions remain UNVERIFIED, and a supplemental JMdict capture of バス does not
establish the naturalness of the full sentence バスは満員です. No grading guard,
runtime approval, native-speaker certification or ordinary activation is claimed.

The [qualified source record](translation-batches/130-crossing-harbor-fullness-performance-kanji-reviewed-source.json)
records **2,464 reviewed-current / 2 excluded reviewed runtime-blocked drafts /
5,812 pending of 8,278**, with 1,478 words / 478 kanji / 478 strokes. Content
version is `fadd97d55a215c4d`; checkpoint authority remains null and `Ready`
false. PR [#14](https://github.com/stop-cran/learning-japanese-ru/pull/14)
integrated at main `08813d0e412a71346ac2d3f2370f90e36dae4038`. Exact-main CI
passed; the actual public ZIP and tar.gz exports matched the exact Git archive
path-by-path and byte-for-byte, all required notices/licenses were present, all
four protected refs were unchanged, and issue #3 progress was updated. See the
[publication verification](translation-batches/130-crossing-harbor-fullness-performance-kanji-publication-verification-001.json).
This is source-content qualification only, not runtime, device, release,
ordinary-activation or full-translation approval. Batch131 and batch132
subsequently completed; continue batch133 and every remaining safe frozen
family.

## Previous published source milestone: batch129 floating, depth and settlement kanji

Batch129 adds four complete Russian frozen-community N3 lessons (浮/消/深/済),
four byte-identical frozen-source stroke assets, and six authorized NAV-only
wrappers on existing word pages. Eight optional wrappers to unavailable word
pages were removed while their Japanese text was retained; no word pages were
added. The independent review found no supported Japanese-content or Russian-
comprehension issue within its stated scope. C1 and C3 are CLEAN only within
those recorded boundaries. C2 remains UNVERIFIED for all 12 ordinary
negative/fallback quiz directions, with no grading guard approved.

The [qualified source record](translation-batches/129-floating-depth-and-settlement-kanji-reviewed-source.json)
records **2,456 reviewed-current / 2 excluded reviewed runtime-blocked drafts /
5,820 pending of 8,278**, with 1,478 words / 474 kanji / 474 strokes. Content
version is `c428c2168b28da5c`; checkpoint authority remains null and `Ready`
false. PR [#13](https://github.com/stop-cran/learning-japanese-ru/pull/13)
integrated at main `6a1bb488ecfc1926f6fb2e57962b1fee40174fc2`. Exact-main CI
passed; the actual public ZIP and tar.gz exports matched the exact Git archive
path-by-path and byte-for-byte, all required notices/licenses were present, all
four protected refs were unchanged, and issue #3 progress was updated. See the
[publication verification](translation-batches/129-floating-depth-and-settlement-kanji-publication-verification-001.json).
This is source-content qualification only, not runtime, device, release,
ordinary-activation or full-translation approval. Continue batch130 and every
remaining safe frozen family.

## Previous published source milestone: batch128 decide, govern, law, swim and wash kanji

Batch128 added seven complete Russian kanji lessons (決/治/法/泳/洗/活/流),
seven byte-identical frozen-source stroke assets, and only the 14 preauthorized
navigation links on existing word pages. The qualified review found no supported
Japanese-content or Russian-comprehension issue within scope. C1 and C3 are CLEAN
only within their recorded boundaries; C2 remains UNVERIFIED for all 21 ordinary
negative quiz directions, with no grading guard approved.

The [qualified source record](translation-batches/128-decide-govern-law-swim-wash-kanji-reviewed-source.json)
records **2,448 reviewed-current / 2 excluded reviewed runtime-blocked drafts /
5,828 pending of 8,278**, with 1,478 words / 470 kanji / 470 strokes. Content
version is `67eb914ece3e362f`; checkpoint authority remains null and `Ready` false.
The [publication verification](translation-batches/128-decide-govern-law-swim-wash-kanji-publication-verification-001.json)
records owner-signed branch commits, PR #12 integration at main
`bd941bc6d71b1f21cc675efa4f2332cb524a4b4e`, exact-main CI, actual public ZIP and
tar.gz byte comparisons (including all required licenses/notices), four unchanged
protected refs, and the issue #3 progress comment. The GitHub-generated merge
commit is separately recorded with its verified `web-flow` platform identity.
This is qualified source-content acceptance only; it is not runtime, device,
release, ordinary-activation, or full-translation approval. Batch129 follows
this checkpoint; continue every remaining safe frozen family.

## Previous published source milestone: batch127 capture and search kanji

Batch127 adds five complete Russian frozen-community N3 lessons, 捕/掛/探/民/求, and five
byte-identical frozen KanjiVG stroke files. Five existing word pages receive only planned
navigation wrappers; the pre-mutation amendment authorizes removal of exactly three optional
wrappers whose `words/求める.md` target is absent. No word page was added and no Japanese form,
reading, example, or grading metadata changed.

The [whole-candidate review disposition](translation-batches/127-capture-hanging-search-population-kanji-review-qualification-dispositions-001.json)
covers all five Russian lessons and frozen English counterparts, five navigation diffs, eleven
existing direct distractor providers, source captures, and all 15 direct source-directed edges.
C1 and C3 are CLEAN only within the recorded scope. C2 is UNVERIFIED for ordinary active-negative
and fallback quiz safety; all 15 directions remain UNVERIFIED and no grading guard is approved.
All five stroke blobs match the frozen source. The reviewer did not run tests, inspect KanjiPedia
glyph pixels, or perform app/device/native-speaker review.

The original intake's 449 accepted kanji/strokes counts were stale pre-batch126 values. The
[count reconciliation](translation-batches/127-capture-hanging-search-population-kanji-baseline-count-reconciliation-001.json)
preserves the immutable intake and establishes the actual batch127 baseline as 458 kanji and 458
strokes. Batch126 added nine of each and was integrated at `1468224621c9c2092a11536d98e56ff734b883dc`;
`db368c9a0acd3dee80695d29e88d1c58c8a6797a` is its subsequent progress reconciliation.

The [qualified source record](translation-batches/127-capture-hanging-search-population-kanji-reviewed-source.json)
records 2,434 reviewed-current / 2 excluded reviewed blocked-media drafts / 5,842 pending of
8,278; 1,478 words / 463 kanji / 463 strokes. Version `7034d4c5959242d3`; checkpoint authority
remains null and `Ready` false. PR [#10](https://github.com/stop-cran/learning-japanese-ru/pull/10)
published the qualified source at main commit `aecc058a0c3c254f9fe91da532ab8eba5ccc2eec`.
Exact-main CI passed; the actual public ZIP and tar.gz exports were byte-compared with Git archive,
including LICENSE, NOTICE.md, and UNICODE-LICENSE.txt. The three owner-authored branch commits
verify under the full owner key and `stop-cran` author/committer identity. GitHub's verified merge
commit records `web-flow` as platform committer; it is not represented as an owner-key commit.
See the [publication verification](translation-batches/127-capture-hanging-search-population-kanji-publication-verification-001.json).
No runtime, device, release, or ordinary activation approval is claimed. Continue batch128 and
every remaining safe frozen family.

## Previous qualified source milestone: batch125 tooth, age and stages kanji

Batch125 adds five complete Russian frozen N3 lessons, 歯/歳/残/段/殺, and five frozen-source
byte-identical KanjiVG stroke files. Seven existing word pages receive only planned standalone-glyph
navigation links; a signed pre-mutation amendment authorizes exactly 14 wrappers around optional,
unavailable lesson links. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [qualified review disposition](translation-batches/125-tooth-age-and-stages-kanji-review-qualification-dispositions-001.json)
records a whole-candidate C1/C2/C3 review and sequential source follow-up: all five lessons, five
frozen EN lessons, seven navigation diffs, five KanjiPedia entries, 18 KANJIDIC2 records, three
radical rows, and 50 JMdict objects/22 cited form-reading pairs were read. Five new pool rows are
indices 330, 331, 333, 334, 335; index 332 is not new. No supported content finding remains.
C1 and C3 are CLEAN within the recorded scope. All 15 ordinary active-negative directions remain
**UNVERIFIED**; source-introductory mapping is not quiz-guard approval. No visual/device/runtime
acceptance is claimed.

The [qualified source record](translation-batches/125-tooth-age-and-stages-kanji-reviewed-source.json)
preserves the prior 2396 accepted runtime entries and all 1478 word metadata/quiz arrays. Current
source checkpoint: **2406 reviewed-current / 2 excluded reviewed blocked-media drafts / 5870 pending
of 8278**; 1478 words/449 kanji/449 strokes; kanji 80 N5/166 N4/**201 N3**/2 N2, with **166 N3
remaining**. Version `afe1154b96b55364`; checkpoint authority remains null and `Ready` false. The
protected 033 `空` draft remains excluded, not runtime and not a media issue. This was not finite
completion; batch126 and then batch127 were subsequently completed in sequence, and all remaining
safe frozen families remain open.

## Previous qualified source milestone: batch124 result, status, lack, next and desire kanji

Batch124 adds **five complete Russian frozen N3 lessons, 果/格/欠/次/欲, 353 file lines**, and five
RAW-identical Japanese KanjiVG assets. Six existing word bodies receive one NAV-only standalone-glyph
wrapper each (性格, 果物, 格好, 次, 欲しい, 欲張り), planned in the signed intake; no navigation amendment.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Original candidate `306f04b82f6aae104a1204424c814a9d5fdfc4db` received **one completed whole independent
review**. It read 58 whole teaching bodies (30 EN/28 CURRENT RU: five primary pairs, 15 context pairs,
eight linked-only pairs, plus two EN-only comparisons), 86 whole official TEXT units plus one header, all
444 typed rows, 15 proposals, five L/five A rulings, five outside LIMITS and all six navigation diffs in
61 complete windows with identical opening/closing gates, zero failures and zero web pages.

- [Whole review](translation-batches/124-result-status-lack-next-and-desire-kanji-independent-review-001.json) (6409-byte report, SHA256
  `3205aeccea3bb44e193b81899ba6b97c8c5383807d72726bb4b38307b7b9fae6`): **C1 CLEAN, C2 CLEAN** (reviewer verdict; canonical ordinary active-negative status
  remains U), **C3 NEEDS FIX** — finding **124-F001** (C3, medium, high confidence): the §Чтения labels
  «онное/кунное» were specialist terminology left unexplained for a novice.

A signed [pre-mutation freeze](translation-batches/124-result-status-lack-next-and-desire-kanji-review-finding-reading-type-gloss-amendment-freeze-001.json)
(`0058fcf08d53efc732cf67d86403b71022f4e208`) authorised inserting exactly one short paragraph after «## Чтения» in each of the
five lessons: «Онное чтение (онъёми) — японское чтение знака, которое восходит к китайскому
произношению; кунное чтение (кунъёми) — японское слово, закреплённое за знаком как его перевод.» (格,
which has no kun reading, receives only the on sentence). The wording is bound to actual captures of
the Britannica (ブリタニカ国際大百科事典 小項目事典, via kotobank) entries for 音読み and 訓読み. The
[corrected candidate](translation-batches/124-result-status-lack-next-and-desire-kanji-corrected-candidate-001.json) `bd97267cdf463bb20d741990cf025fbd5475020c` changes only those
five lesson files (typed metadata identical for all 444 rows; the six NAV wrappers unchanged). One later
[focused review](translation-batches/124-result-status-lack-next-and-desire-kanji-independent-review-focused-001.json) (one different reviewer, never concurrent;
25 windows, 28 commands, zero failures; 2574-byte report, SHA256 `74219eed706b834c6690e8898df01ffa66a20e547a9c9ff05d7a778b04fc7d99`) found **124-F001
RESOLVED**, bounded C1/C2/C3 CLEAN, the 格 variant and the author-record erratum accurate, and no new
findings. It is not a second whole review; the original verdicts stay immutable and the batch is not
retrospectively whole-CLEAN. The 417 earlier accepted lessons that use the same labels without a gloss
are deliberately **not** changed here; this is visible future polish, not a claim that the corpus was swept.

All 15 directions are qualified introductory/source-core comparisons only (S-intro; canonical author
mapping Q); no direction is rejected as a reading negative; all 15 ordinary uses stay **U** (metadata
retention is not guard approval). All five L rulings are SUPPORTED and all five A clarifications are
SUPPORTED-BOUNDED. Outside LIMITS (実; 合/性/客/画/質; 失/席/出; 二; 望/食/好) are observations, not new
guards.

The [qualified source record](translation-batches/124-result-status-lack-next-and-desire-kanji-reviewed-source.json) preserves 2380 baseline runtime RAWs/tracking rows
and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2396 runtime/1478 words/444
kanji/444 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged; kanji 80 N5/166 N4/**196
N3**/2 N2; **171 N3 remain**. Strict progress: **2396 reviewed-current/two excluded reviewed
blocked-media drafts/5880 pending of 8278**. Version `d1e3c1469573b505`; checkpoint authority
null/Ready false. Prior 082–123 U qualifications remain unchanged; the earlier open observations (RU 昨日
without a 昔 link, RU 時 distractors differing from EN, RU 高 distractor 本, RU
怖/青/耳/愛/強/院/留守/怒る/少) are outside this batch and remain open. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 125+ and
**ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch123 horizontal, build, manner, authority and mechanism kanji

Batch123 adds **five complete Russian frozen N3 lessons, 横/構/様/権/機, 325 file lines**, and five
RAW-identical Japanese KanjiVG assets. Four existing word bodies receive one NAV-only standalone-glyph
wrapper each (横, 機会, 結構, 飛行機), planned in the signed intake; no navigation amendment. Frozen EN
remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Candidate `088cb5d7f1f56340ed64deb84815eaa238c22910` received **one completed whole independent review**.
It read 43 whole teaching bodies (23 EN/20 CURRENT RU: five primary pairs, 10 context pairs, five
linked-only pairs, plus EN-only comparisons 構成, 様子, 権利), 72 whole official TEXT units plus one
header, all 439 typed rows, 15 proposals, five L/five A rulings, five outside LIMITS and all four
navigation diffs in 57 complete windows with identical opening/closing gates and zero reader failures
(one oversize report delivery attempt failed before printing anything and is not credited).

- [Review A](translation-batches/123-horizontal-build-manner-authority-and-mechanism-kanji-independent-review-001.json) (10777-byte report, SHA256
  `d8acd8adb3891b0d211276abdd69161756790534934fae46d58c4cdd34e2235b`): **C1 CLEAN, C2 UNVERIFIED** (unrestricted active-negative/fallback
  safety; dependencies and navigation CLEAN), **C3 CLEAN**; no confirmed findings. Optional polish
  (a shorter shared explanation of 形声 in 横/様/権) is recorded, not applied.

All 15 directions are qualified introductory/source-core comparisons only (S-intro; canonical author
mapping Q). Five shared-reading directions are **rejected as reading negatives** and retained only as
introductory shape comparisons: 横→校 and 構→横 (KanjiPedia [外] コウ of 横), 構→校 (コウ), 様→洋 (ヨウ)
and 機→杯 (archaic 杯 はた). All 15 ordinary uses stay **U** (metadata retention is not guard approval).
All five L rulings and all five A clarifications are SUPPORTED. Outside LIMITS (書/断/広; 工/成/考;
容/用/曜/子; 力/利/人/件/建/験; 幾/会/行/期/気) are observations, not new guards. 横書き, 横断, 構成, 構造,
構える, 構う, 構え, 様子, 模様, 権利, 権力, 人権 and 機械 stay plain text (no runtime word). Known author
erratum: the signed candidate commit message says 2386 accepted-main objects remain; the correct value is
2376 (as in the candidate JSON); the message is not rewritten.

The [qualified source record](translation-batches/123-horizontal-build-manner-authority-and-mechanism-kanji-reviewed-source.json) preserves 2372 baseline runtime RAWs/tracking rows
and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2386 runtime/1478 words/439
kanji/439 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged; kanji 80 N5/166 N4/**191
N3**/2 N2; **176 N3 remain**. Strict progress: **2386 reviewed-current/two excluded reviewed
blocked-media drafts/5890 pending of 8278**. Checkpoint authority null/Ready false. Prior 082–122 U
qualifications remain unchanged; the earlier open observations (RU 昨日 without a 昔 link, RU 時
distractors differing from EN, RU 高 distractor 本, RU 怖/青/耳/愛/強/院/留守/怒る/少) are outside this batch
and remain open. Protected 033 WORD空 stays excluded/runtime-absent/not media. No
device/media/default/package/release authority. Continue 124+ and **ALL remaining safe frozen
levels/families**, not finite completion.

## Previous qualified source milestone: batch122 hope, not-yet, end, bundle and cupful kanji

Batch122 adds **five complete Russian frozen N3 lessons, 望/未/末/束/杯, 325 file lines**, and five
RAW-identical Japanese KanjiVG assets. Two existing word bodies receive one NAV-only standalone-glyph
wrapper each (一杯, 約束), planned in the signed intake; no navigation amendment. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Candidate `7876a7f79c68bce4ded86203e020ea4da6760736` received **one completed whole independent review**.
It read 42 whole teaching bodies (23 EN/19 CURRENT RU: five primary pairs, 12 context pairs, two
linked-only pairs, plus EN-only comparisons 望む, 未来, 週末, 願う), 82 whole official TEXT units plus one
header, all 434 typed rows, 15 proposals, five L/five A rulings, five outside LIMITS and both navigation
diffs in 57 complete windows with identical opening/closing gates and zero failures.

- [Review A](translation-batches/122-hope-not-yet-end-bundle-and-cupful-kanji-independent-review-001.json) (5491-byte report, SHA256
  `d84e5813c547a1c13983ecd377b9666841560c9c066fd8eef25d8393ebbbc251`): **C1 CLEAN, C2 FINDING, C3 FINDING**; findings 122-R-F001..F003
  claimed that kanji/望.md (望む, 願う), kanji/未.md (未来) and kanji/末.md (週末) link to absent Russian
  word pages.

The signed [writer adjudication](translation-batches/122-hope-not-yet-end-bundle-and-cupful-kanji-review-finding-adjudication-001.json) byte-checked the candidate and
did **not reproduce** F001–F003: those words occur only as plain text, no Markdown link mentions them, and
every relative link target in the three lessons exists (the validator's link check also passes). One
later [focused review](translation-batches/122-hope-not-yet-end-bundle-and-cupful-kanji-focused-review-001.json) (one different reviewer;
1469-byte report) found **F001–F003 NOT_REPRODUCED**, the adjudication
record accurate and no new findings. No runtime file changed. Original verdicts stay immutable; the batch
is not retrospectively whole-CLEAN.

All 15 directions are qualified introductory/source-core comparisons only (S-intro; canonical author
mapping Q); no reading-negative rejections; all 15 ordinary uses stay **U** (metadata retention is not
guard approval). All five L rulings are SUPPORTED and all five A clarifications SUPPORTED-BOUNDED. Outside
LIMITS (望 vs 亡/忙/忘/夢; 未 vs 味/妹/定/来; 末 vs 終 title overlap «конец»/始; 束 vs 約/側/息/足/数; 杯 vs
否/敗/買/一) are observations, not new guards. 希望, 願望, 望む, 願う, 未来, 未定, 週末, 月末, 年末, 束ねる and
乾杯 stay plain text (no runtime word).

The [qualified source record](translation-batches/122-hope-not-yet-end-bundle-and-cupful-kanji-reviewed-source.json) preserves 2364 baseline runtime RAWs/tracking rows
and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2376 runtime/1478 words/434
kanji/434 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged; kanji 80 N5/166 N4/**186
N3**/2 N2; **181 N3 remain**. Strict progress: **2376 reviewed-current/two excluded reviewed
blocked-media drafts/5900 pending of 8278**. Checkpoint authority null/Ready false. Prior 082–121 U
qualifications remain unchanged; the earlier open observations (RU 昨日 without a 昔 link, RU 時
distractors differing from EN, RU 高 distractor 本, RU 怖/青/耳/愛/強/院/留守/怒る/少) are outside this batch
and remain open. Protected 033 WORD空 stays excluded/runtime-absent/not media. No
device/media/default/package/release authority. Continue 123+ and **ALL remaining safe frozen
levels/families**, not finite completion.

## Previous qualified source milestone: batch121 ease, dusk, melody, renewal and utmost kanji

Batch121 adds **five complete Russian frozen N3 lessons, 易/暮/曲/更/最, 321 file lines**, and five
RAW-identical Japanese KanjiVG assets. Nine existing word bodies receive one NAV-only standalone-glyph
wrapper each (変更, 易しい, 暮れる, 曲る, 最も, 最初, 最後, 最近, 貿易), planned in the signed intake; no
navigation amendment. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Candidate `fcc1fe25c7189264814ac2a96f0079da84593fbe` received **one completed whole independent review**.
It read 77 whole teaching bodies (40 EN/37 CURRENT RU: five primary pairs, 24 context pairs, eight
linked-only pairs, plus EN-only comparisons 安易, 暮らす, 曲), 105 whole official TEXT units plus one
header, all 429 typed rows, 15 proposals, five L/five A rulings, five outside LIMITS and all nine
navigation diffs in 70 complete windows with identical opening/closing gates and zero failures.

- [Review A](translation-batches/121-ease-dusk-melody-renewal-and-utmost-kanji-independent-review-001.json) (5796-byte report, SHA256
  `580eb5c4a3c81a7fd090de41e3f3d954d9d249ae2cda0a3f6cc36463cfcb22ea`): **C1 CLEAN, C2 UNVERIFIED, C3 CLEAN**; findings none; optional none.
  C2 stays UNVERIFIED only because ordinary active-negative quiz safety was not established; no defect.

All 15 directions are qualified introductory/source-core comparisons only (S-intro; canonical author
mapping Q); no reading-negative rejections; all 15 ordinary uses stay **U** (metadata retention is not
guard approval). All five L rulings are SUPPORTED and all five A clarifications SUPPORTED-BOUNDED. Outside
LIMITS (易 vs 楽 «лёгкость»; 暮 vs 暗/晩/夕/夜; 曲 vs 局/music words; 更 vs 化/変/new/夜 words; 最 vs
妻/才/切/初/後/近/取) are observations, not new guards. 安易, 容易, 暮らす, 暮らし, 暮れ, 曲, 曲がる, 曲げる,
更に and 夜更かし stay plain text (no runtime word).

The [qualified source record](translation-batches/121-ease-dusk-melody-renewal-and-utmost-kanji-reviewed-source.json) preserves 2347 baseline runtime RAWs/tracking rows
and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2366 runtime/1478 words/429
kanji/429 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged; kanji 80 N5/166 N4/**181
N3**/2 N2; **186 N3 remain**. Strict progress: **2366 reviewed-current/two excluded reviewed
blocked-media drafts/5910 pending of 8278**. Checkpoint authority null/Ready false. Prior 082–120 U
qualifications remain unchanged; the earlier open observations (RU 昨日 without a 昔 link, RU 時
distractors differing from EN, RU 高 distractor 本, RU 怖/青/耳/愛/強/院/留守/怒る/少) are outside this batch
and remain open. Protected 033 WORD空 stays excluded/runtime-absent/not media. No
device/media/default/package/release authority. Continue 122+ and **ALL remaining safe frozen
levels/families**, not finite completion.

## Previous qualified source milestone: batch120 past, scenery, evening and clear-sky kanji

Batch120 adds **five complete Russian frozen N3 lessons, 昔/景/昨/晩/晴, 310 file lines**, and five
RAW-identical Japanese KanjiVG assets. Twelve existing word bodies receive one NAV-only standalone-glyph
wrapper each (一昨年, 一昨日, 今晩, 昔, 昨夜, 昨日, 晩, 晩御飯, 景色, 晴れ, 晴れる, 毎晩), planned in the
signed intake; no navigation amendment. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Candidate `274f263c4c8ca42d2fc4f6dc3efcd3eb6fb5fd37` received **two sequential completed whole
independent reviews** (never concurrent). Each read 88 whole teaching bodies (44 EN/44 CURRENT RU: five
primary pairs, 25 context pairs, 14 linked-only pairs), 81 whole official TEXT units plus one header,
all 424 typed rows, 15 proposals, five L/five A rulings, five outside LIMITS and all 12 navigation diffs
in 69 complete windows with identical opening/closing gates and zero failures. The writer first misread
review A's unrelated short native final as a no-op and launched review B; a private erratum supersedes
that wrong record, and B is not used to outvote A.

- [Review A](translation-batches/120-past-scenery-evening-and-clear-sky-kanji-independent-review-001.json) (6472-byte report, SHA256
  `1b4dff570ecacba4bdd12d3de6ffe85539bdb58136a9a5c2f6c2c9876718d765`): **C1 CLEAN, C2 NEEDS FIX, C3 CLEAN**; findings 120-F001..F004:
  昔→借 (シャク), 景→京 (ケイ), 昨→作 (サク), 晴→青 (セイ) share an on'yomi, unsafe as unqualified reading
  negatives; N009 昨→時 ordinary **U**.
- [Review B](translation-batches/120-past-scenery-evening-and-clear-sky-kanji-independent-review-002.json) (6072-byte report, SHA256
  `355b036da3b715c5a7bc2fe474178e213629b9a657ccc724c9cfc62f447da71c`): **C1 CLEAN, C2 UNVERIFIED, C3 CLEAN**; no findings; the same four
  directions are introductory shape comparisons only, not reading negatives.

The signed [writer adjudication](translation-batches/120-past-scenery-evening-and-clear-sky-kanji-review-finding-adjudication-001.json) resolved F001–F004 **without
runtime mutation**: the four lines are identical to frozen EN; the app's committed reading-quiz code
(kanji-cards-android `10d98d0`, `KanjiReadings.kt` `excludedKeys`) removes every target on/kun reading
and its voicing/long-vowel/small-っ variants from wrong options, and the meaning mode uses distinct
Russian titles. One later [focused review](translation-batches/120-past-scenery-evening-and-clear-sky-kanji-focused-review-001.json) (one different reviewer;
2366-byte report) found **F001–F004 RESOLVED**, C1/C2 CLEAN, C3 N/A, the
adjudication record accurate and no new findings; it verified committed source only, not a device or
other app versions. Original verdicts stay immutable; the batch is not retrospectively whole-CLEAN.

Review A classified ten directions S-intro, N009 昨→時 U and the four shared-reading directions as accurate
introductory shape comparisons that are **REJECTED as reading negatives** (review B: all 15 S-intro, the same
four not reading negatives); all 15 stay retained introductory/source-core comparisons (canonical author mapping
Q) and all 15 ordinary uses stay **U** (metadata retention is not guard approval). All five L and five A rulings are SUPPORTED. Outside LIMITS
(昔 vs 去年/今/古; 景 vs 景色/色; 昨 vs 昨日/昨年/今/去; 晩 vs 夕/夜/今晩/毎晩/早; 晴 vs 晴天/天気/青) are
observations, not new guards. 昔話, 風景/夜景, 昨年 and 晴天 stay plain text (no runtime word).

The [qualified source record](translation-batches/120-past-scenery-evening-and-clear-sky-kanji-reviewed-source.json) preserves 2334 baseline runtime RAWs/tracking rows
and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2356 runtime/1478 words/424
kanji/424 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged; kanji 80 N5/166 N4/**176
N3**/2 N2; **191 N3 remain**. Strict progress: **2356 reviewed-current/two excluded reviewed
blocked-media drafts/5920 pending of 8278**. Checkpoint authority null/Ready false. Prior 082–119 U
qualifications remain unchanged; the existing RU 昨日 without a 昔 link, RU 時 distractors differing from
EN, the RU 高 distractor 本 and the earlier open observations (RU 怖/青/耳/愛/強/院/留守/怒る/少) are
outside this batch and remain open. Protected 033 WORD空 stays excluded/runtime-absent/not media. No
device/media/default/package/release authority. Continue 121+ and **ALL remaining safe frozen
levels/families**, not finite completion.

## Previous qualified source milestone: batch119 fear, emotion and feeling kanji

Batch119 adds **three complete Russian frozen N3 lessons, 恐/情/感, 194 file lines**, and three
RAW-identical Japanese KanjiVG assets. No existing word body changes (zero navigation wrappers, no
navigation amendment). Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/119-fear-emotion-and-feeling-kanji-independent-review-001.json) (one reviewer) of
original candidate `2211457052dd721178b9b70a2e0f9cbe8833908e` read **32 whole teaching bodies, 17 EN/15
CURRENT RU** (three primary pairs, 11 context pairs 工/心/必/忘/忙/念/怖/思/性/息/青, the linked-only
existing pair words/怖い, and two EN-only comparison bodies words/恐れる and 感情), **72 whole official
TEXT units** (15 KANJIDIC2, one radical-evidence unit, 53 JMdict, three KanjiPedia) plus one provider
header, all 419 CURRENT typed rows, nine original directions, three L/three A rulings, three outside
LIMITS, four guidance files and three RU rubrics — **53 complete windows**, 56 successful commands,
zero failures, identical opening/closing gates, zero glyph pixels and zero web pages. The original
**8605-byte stdout report**, SHA256 `18f15b9586eba1f56d9f4c45b426acc7750d4320a1130a853d08d27f9c845bfc`, byte-identical to the
reviewer's native final, is published verbatim. Actual verdicts: **C1 NEEDS FIX**, **C2 UNVERIFIED**
for ordinary active-negative quiz deployment (CLEAN for the bounded dependency and introductory
comparison scope), **C3 CLEAN** — finding **119-F001** (moderate, C1): the 感 lesson presented the
sense «заражаться, заболевать» itself as an abbreviation of 感冒, while KanjiPedia meaning ② lists
染まる。かかる separately from the abbreviation use 「感冒」の略.

A signed [pre-mutation wording freeze](translation-batches/119-fear-emotion-and-feeling-kanji-review-finding-illness-sense-amendment-freeze-001.json)
(`9387855ce81ff58d18adce37f712ee46906acd50`) authorised replacing exactly that line with a separated sense (感染) and
abbreviation (感冒 «простуда», e.g. 流感) statement, with an author-record erratum; the
[corrected candidate](translation-batches/119-fear-emotion-and-feeling-kanji-corrected-candidate-001.json) `edb0e3227123a0a39d9d4e778ce016ec7f34c2b1` changes only
kanji/感.md (typed metadata identical for all 419 rows). One later
[focused review](translation-batches/119-fear-emotion-and-feeling-kanji-independent-review-focused-001.json) (one different reviewer, never concurrent;
21 windows, 24 commands, zero failures; 2234-byte report) found **119-F001 RESOLVED**, bounded
C1/C2/C3 CLEAN, the erratum accurate, and no new findings. It is not a second whole review; the original
verdicts stay immutable and the batch is not retrospectively whole-CLEAN. The reviewer's optional notes
(an alternative 恐 title, an explicit 情/感 overlap note, readings for illustration compounds) are
explicitly not defects, recorded and not applied.

All nine directions are **S-intro** (introductory/source-core only, canonical author mapping Q); N004
情→青 and N005 情→性 are **REJECTED as セイ reading-negatives** (shape comparison only); all nine
ordinary uses stay **U** (metadata retention is not guard approval). L001 恐 and L002 情 are
supported; L003 感 was partial (now resolved by F001); all three A rulings are SUPPORTED. Outside
LIMITS (恐 vs 怖/忙/強/心; 情 vs 感/愛/事/思/心; 感 vs 情/想/思/心 and the partial 成 contact) are
observations, not new guards and not cleared for future options.

The [qualified source record](translation-batches/119-fear-emotion-and-feeling-kanji-reviewed-source.json) preserves 2340 baseline runtime
RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2346 runtime/1478 words/419 kanji/419 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**171 N3**/2 N2; **196 N3 remain**. Strict progress: **2346
reviewed-current/two excluded reviewed blocked-media drafts/5930 pending of 8278; 5932 runtime
paths absent**. Version `661906a3eef21dda`; checkpoint authority null/Ready false. Prior
082–118 U qualifications remain unchanged; the existing unlinked 恐 mention in RU 怖.md, the unlinked
青白い in RU 青.md, the RU 耳.md unlinked 恥 mention, the RU 愛 metadata kun かな.しい, the RU 強
metadata kun こわ.い, the existing unlinked 完 mention in RU 院.md, the RU 留守 wording, the existing
RU 怒る «официальный или литературный» wording for いかる and the RU 少.md distractor 名 (frozen EN 小)
are outside this batch and remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 120+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch118 forget, busy, wish, fear and nature kanji

Batch118 adds **five complete Russian frozen N3 lessons, 忘/忙/念/怖/性, 306 file lines**,
and five RAW-identical Japanese KanjiVG assets. Eight whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (女性→性; 忘れる→忘; 忘れ物→忘; 忙しい→忙; 怖い→怖;
性格→性; 残念→念; 男性→性), planned in the signed intake; no whole-label wrapper and no navigation
amendment. All visible prose, Japanese metadata, quiz arrays, old links, line endings and frozen
levels of those words remain unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/118-forget-busy-wish-fear-and-nature-kanji-independent-review-001.json) (one reviewer) of
candidate `b0a47569d86cf1abdd20410d7d89e6e31f6fb21d` read **65 whole teaching bodies, 33 EN/32
CURRENT RU** (five primary pairs, 16 context pairs including the eight NAV words, 11 linked-only
existing pairs 女/男/物/暇/女の人/女の子/覚える/気分/悲しい/男の人/男, and the EN-only comparison
body 恐), **86 whole official TEXT units** (17 KANJIDIC2, one radical-evidence unit, 63 JMdict, five
KanjiPedia) plus one provider header, all 416 CURRENT typed rows, 15 original directions, five
L/five A rulings, five outside LIMITS, eight exact NAV diffs, four guidance files and three RU
rubrics — **65 complete windows**, 69 successful commands including two stdout emissions (the first
a superseded format variant differing only in the 15 N-line prefixes, with identical dispositions;
the second equal to the native final), zero failed commands, identical opening/closing gates, zero
glyph pixels and zero web pages. The canonical **8128-byte stdout report**, SHA256
`25edf72eb048eec50dd1690f4be313e3a9aef41188e9c416d7812b2ec8284379` (the reviewer's native final plus one terminal LF), is published verbatim.
Actual verdicts: **C1 CLEAN**, **C2 UNVERIFIED** (all eight NAV-only wrappers and new links verified
and no shared answer found against current titles, but ordinary active quiz safety is not confirmed
without the actual prompt/render; no defect), **C3 CLEAN**; findings none. The optional note offers
stylistic title alternatives (忙 «занятость», 怖 «страшный; бояться», 性 «природа; пол») and states
they are not defects; no change.

All 15 directions are **S-intro** (introductory/source-core only, canonical author mapping Q). All
15 ordinary all-mode uses stay **U** (metadata retention is not guard approval). All five L and five
A rulings are supported; all eight NAV changes are NAV-ONLY; outside LIMITS (忘/忙 and 亡/ボウ, 失;
急 and 夢 ボウ; 念 vs 今/思/想/意; 怖 vs 強 こわ.い and 声; 性 vs 生 セイ・ショウ, 性質 and 男/女) are
observations, not new guards and not cleared for future options.

The [qualified source record](translation-batches/118-forget-busy-wish-fear-and-nature-kanji-reviewed-source.json) preserves 2322 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2340 runtime/1478 words/416 kanji/416 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**168 N3**/2 N2; **199 N3 remain**. Strict progress: **2340
reviewed-current/two excluded reviewed blocked-media drafts/5936 pending of 8278; 5938 runtime
paths absent**. Version `00404f2955d875b4`; checkpoint authority null/Ready false. Prior 082–117
U qualifications remain unchanged; the existing unlinked 恥 mention in RU 耳.md, the RU 愛 metadata
kun かな.しい, the RU 強 metadata kun こわ.い, the existing unlinked 完 mention in RU 院.md, the RU
留守 wording, the existing RU 怒る «официальный или литературный» wording for いかる and the RU 少.md
distractor 名 (frozen EN 小) are outside this batch and remain open observations. Protected 033
WORD空 stays excluded/runtime-absent/not media. No device/media/default/package/release authority.
Continue 119+ and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch117 breath, shame, thought and sorrow kanji

Batch117 adds **four complete Russian frozen N3 lessons, 息/恥/想/悲, 255 file lines**,
and four RAW-identical Japanese KanjiVG assets. Three whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (恥ずかしい→恥; 息子→息; 悲しい→悲), planned in the signed
intake; no whole-label wrapper and no navigation amendment. All visible prose, Japanese metadata,
quiz arrays, old links, LF line endings and frozen levels of those words remain unchanged. Frozen
EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/117-breath-shame-thought-and-sorrow-kanji-independent-review-001.json) (one reviewer) of
candidate `26cf950d982dcd6c4a3cad7a95c6de8c43992641` read **42 whole teaching bodies, 23 EN/19
CURRENT RU** (four primary pairs, 11 context pairs including the three NAV words, four linked-only
existing pairs 子/娘/子供/残念, and four EN-only comparison bodies 相/非/予想/息), **72 whole
official TEXT units** (17 KANJIDIC2, one radical-evidence unit, 50 JMdict, four KanjiPedia) plus
one provider header, all 411 CURRENT typed rows, 12 original directions, four L/four A rulings,
four outside LIMITS, three exact NAV diffs, four guidance files and three RU rubrics — **55
complete windows**, 58 successful commands plus one failed stdout delivery (terminal-LF assertion,
no report printed, not credited), zero reader failures, identical opening/closing gates, zero glyph
pixels and zero web pages. The original **5629-byte stdout report**, SHA256
`b43b6e7c40bdda175189d15a00ef9e5b8ee1a0f85b0eb6d548beaa531c7e246a` (the reviewer's native final plus one terminal LF), is published verbatim.
Actual verdicts: **C1 CLEAN**, **C2 CLEAN** (three NAV-only wrappers and links verified), **C3
CLEAN**; findings none; the optional note says no correction is warranted for omitting the
literary 息 そく «сын» sense.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); the
reviewer additionally found each bounded-safe as a negative against the current directed Russian
titles only (N012 悲→怒: related emotions, but «печаль» and «гнев; сердиться» are not
interchangeable answers). All 12 ordinary all-mode uses stay **U** (metadata retention is not guard
approval). All four L and four A rulings are SUPPORTED; all three NAV changes are NAV-ONLY; outside
LIMITS (息 vs 休 and breathing kanji 吸/呼/吹; 恥 vs 取 and チ homophones; 想 vs 思/考/意 and ソウ
homophones; 悲 vs 喜/愛/悪 and ヒ homophones) are observations, not new guards and not cleared for
future options.

The [qualified source record](translation-batches/117-breath-shame-thought-and-sorrow-kanji-reviewed-source.json) preserves 2319 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2330 runtime/1478 words/411 kanji/411 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**163 N3**/2 N2; **204 N3 remain**. Strict progress: **2330
reviewed-current/two excluded reviewed blocked-media drafts/5946 pending of 8278; 5948 runtime
paths absent**. Version `61339f58dd6b72be`; checkpoint authority null/Ready false. Prior 082–116
U qualifications remain unchanged; the existing unlinked 恥 mention in RU 耳.md, the RU 愛 metadata
kun かな.しい, the existing unlinked 完 mention in RU 院.md, the RU 留守 wording, the existing RU 怒る
«официальный или литературный» wording for いかる and the RU 少.md distractor 名 (frozen EN 小) are
outside this batch and remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue
118+ and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch116 necessity, anger, love and habit kanji

Batch116 adds **four complete Russian frozen N3 lessons, 必/怒/愛/慣, 279 file lines**,
and four RAW-identical Japanese KanjiVG assets. Five whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (必ず→必; 必要→必; 怒る→怒; 慣れる→慣; 習慣→慣), planned in
the signed intake; no whole-label wrapper and no navigation amendment. All visible prose, Japanese
metadata, quiz arrays, old links, LF line endings and frozen levels of those words remain unchanged.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/116-necessity-anger-love-and-habit-kanji-independent-review-001.json) (one reviewer) of
candidate `76f9e08f0ae41e721c72a488462698bfcb310a74` read **47 whole teaching bodies, 24 EN/23
CURRENT RU** (four primary pairs, 16 context pairs including the five NAV words, three linked-only
existing pairs 多分/習う/習, and one EN-only comparison body words/愛), **65 whole official TEXT
units** (19 KANJIDIC2, one radical-evidence unit, 41 JMdict, four KanjiPedia) plus one provider
header, all 407 CURRENT typed rows, 12 original directions, four L/four A rulings, four outside
LIMITS, five exact NAV diffs, four guidance files and three RU rubrics — **57 complete windows**, 60
successful commands, zero failures, identical opening/closing gates, zero glyph pixels and zero web
pages. The original **4605-byte stdout report**, SHA256 `67e793d889496bb9511ff189c245cce63ead1d2bcbddec913f16b62a27b84ae3`
(the reviewer's native final plus one terminal LF), is published verbatim. Actual verdicts: **C1
CLEAN**, **C2 CLEAN** (bounded; five NAV-only wrappers and links verified), **C3 CLEAN**; findings
none; optional none.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); the
reviewer additionally found each bounded-safe as a negative against the current directed Russian
titles only (N005 怒→安: «спокойный» is a contrast, not an anger synonym). All 12 ordinary all-mode
uses stay **U** (metadata retention is not guard approval). All four L and four A rulings are
SUPPORTED; all five NAV changes are NAV-ONLY; outside LIMITS (必 vs 用/定 and 心-shape kanji; 怒 vs
思/悪/好 and ド; 愛 vs 好/受/親/意/間; 慣 vs 習/常 and the カン homophones) are observations, not new
guards and not cleared for future options.

The [qualified source record](translation-batches/116-necessity-anger-love-and-habit-kanji-reviewed-source.json) preserves 2309 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2322 runtime/1478 words/407 kanji/407 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**159 N3**/2 N2; **208 N3 remain**. Strict progress: **2322
reviewed-current/two excluded reviewed blocked-media drafts/5954 pending of 8278; 5956 runtime
paths absent**. Version `b7c806b406302b76`; checkpoint authority null/Ready false. Prior 082–115
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md, the RU 留守
wording, the existing RU 怒る «официальный или литературный» wording for いかる (the new 怒 lesson
says «книжное или литературное») and the RU 少.md distractor 名 (frozen EN 小) are outside this
batch and remain open observations. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 117+ and **ALL remaining safe frozen
levels/families**, not finite completion.

## Previous qualified source milestone: batch115 politics, defeat, number, scatter and period kanji

Batch115 adds **five complete Russian frozen N3 lessons, 政/敗/数/散/期, 358 file lines**,
and five RAW-identical Japanese KanjiVG assets. Four whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (失敗→敗; 政治→政; 散歩→散; 数学→数), planned in the
signed intake; no whole-label wrapper and no navigation amendment. All visible prose, Japanese
metadata, quiz arrays, old links, line endings and frozen levels of those words remain unchanged.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/115-politics-defeat-number-scatter-and-period-kanji-independent-review-001.json) (one reviewer) of
original candidate `0a7f8e29da9314a477368484eeec5ce990b806ef` read **46 whole teaching bodies, 24 EN/22
CURRENT RU** (five primary pairs, 13 context pairs including the four NAV words, four linked-only
existing pairs 失/学/歩/歩く, and two EN-only comparison bodies: words/数 and 期間), **82 whole official
TEXT units** (20 KANJIDIC2, two radical-evidence units, 55 JMdict, five KanjiPedia) plus one provider
header, all 403 CURRENT typed rows, 15 original directions, five L/five A rulings, five outside LIMITS,
four exact NAV diffs, four guidance files and three RU rubrics — **58 complete windows**, 61 successful
commands, identical opening/closing gates, zero glyph pixels and zero web pages. One earlier stdout
delivery attempt failed its own size assertion before printing anything and is recorded, not credited.
The original **10796-byte stdout report**, SHA256 `61660ded5a5168d8852accab2b70e288b9a4d0d616f19c64a754855abb59abef`, byte-identical
to the reviewer's native final, is published verbatim. Actual verdicts: **C1 CLEAN**, **C2 NEEDS FIX**
(unrestricted quiz safety UNVERIFIED; all four NAV diffs and links verified), **C3 CLEAN** — finding
**115-F001** (low): the 数 lesson left 数学 unlinked in the スウ reading row and the common-words list
although words/数学.md exists, and the author lesson record L003 wrongly claimed it was linked.

A signed [pre-mutation link freeze](translation-batches/115-politics-defeat-number-scatter-and-period-kanji-review-finding-word-link-amendment-freeze-001.json)
(`d7478e5a3f446b2ea19ca468bbb433171342ee6f`) authorised exactly two `[数学](../words/数学.md)` wrappers
and recorded the L003 author-record erratum; the [corrected candidate](translation-batches/115-politics-defeat-number-scatter-and-period-kanji-corrected-candidate-001.json)
`b24d52d013aa100a75e564d33a716a2fa97c0bee` changes only those two lines (typed metadata identical for
all 403 rows). One later [focused review](translation-batches/115-politics-defeat-number-scatter-and-period-kanji-independent-review-focused-001.json) (one different
reviewer, never concurrent; 22 windows, 25 commands, zero failures; 2090-byte report) found **115-F001
RESOLVED**, bounded C1/C2/C3 CLEAN, the L003 erratum accurate, and no new findings. It is not a second
whole review; the original verdicts stay immutable and the batch is not retrospectively whole-CLEAN.
The reviewer's optional density/ちらしずし gloss note is polish, recorded and not applied.

All 15 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); N001
政→正 is **REJECTED as a reading-negative** (both read セイ/ショウ; shape comparison only); all 15
ordinary uses stay **U** (metadata retention is not guard approval). The 数 L ruling was partial
(now resolved by F001); the other four L and all five A rulings are SUPPORTED; all four NAV changes
are NAV-ONLY; outside LIMITS (政 vs 制 plus 局/御 fallback scrutiny; 敗 vs 勝/失 and weak 売; 数 vs 計;
散 vs 集, 歩 and the サン homophones; 期 vs 時/間) are observations, not new guards and not cleared
for future options.

The [qualified source record](translation-batches/115-politics-defeat-number-scatter-and-period-kanji-reviewed-source.json) preserves 2300 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2314 runtime/1478 words/403 kanji/403 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**155 N3**/2 N2; **212 N3 remain**. Strict progress: **2314
reviewed-current/two excluded reviewed blocked-media drafts/5962 pending of 8278; 5964 runtime
paths absent**. Version `2d936b9edafe0e5e`; checkpoint authority null/Ready false. Prior 082–114
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 116+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch114 talent, support, release and cut kanji

Batch114 adds **four complete Russian frozen N3 lessons, 才/支/放/断, 283 file lines**,
and four RAW-identical Japanese KanjiVG assets. Two whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (支度→支; 放送→放), planned in the signed intake; no
whole-label wrapper and no navigation amendment. All visible prose, Japanese metadata, quiz arrays,
old links, line endings and frozen levels of those words remain unchanged. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`. The signed semantic freeze `c6b0335` stated 2300
prospective runtime objects; the actual count is 2304 (the four lessons and four strokes were
omitted from that arithmetic). This bookkeeping erratum is recorded in the candidate record; the
freeze is not rewritten.

The [actual whole independent review](translation-batches/114-talent-support-release-and-cut-kanji-independent-review-001.json) (one reviewer) of
candidate `e1d097359f260a694f80214387f5be58a74bd566` read **52 whole teaching bodies, 28 EN/24
CURRENT RU** (four primary pairs, 15 context pairs, five linked-only existing pairs and four EN-only
word comparisons: 判断, 才能, 支払う, 放れる), **89 whole official TEXT units** (21 KANJIDIC2, four
Unicode key rows, 60 JMdict, four KanjiPedia) plus one provider header, all 398 CURRENT typed rows,
12 original directions, four L/four A rulings, four outside LIMITS, two exact NAV diffs, four guidance
files and three RU rubrics — **58 complete windows**, 61 successful commands, no failures, identical
opening/closing gates, zero glyph pixels and zero web pages. The original **5868-byte
stdout report**, SHA256 `4b0bbad34a9e4b07071c659c2c3ed830f1925880d150b9bbe54fc35d89ba1c9b`, equal to the reviewer's 5867-byte
native final plus one terminal LF, is published verbatim. Actual verdicts: **C1 CLEAN**, **C2 CLEAN**
(content-level: NAV wrappers, links and the 12 directions for introductory/source-core comparison
only), **C3 CLEAN**; findings none; optional none.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all 12
ordinary uses stay **U** (metadata retention is not guard approval; C2 CLEAN does not upgrade them).
N004 支→友 (a friend may help) and N007 放→方 (ホウ reading contact) are noted by the reviewer. All four
L rulings are SUPPORTED and all four A clarifications SOURCE-BOUNDED; both NAV changes are NAV-ONLY;
outside LIMITS (才 vs 歳/年 age and 力 ability; 支 vs 仕 forms and 助; 放 vs 発 and the 話 homophone;
断 vs 切/否/定/判 and 立/発 homophones) are observations, not new guards and not cleared for future
options.

The [qualified source record](translation-batches/114-talent-support-release-and-cut-kanji-reviewed-source.json) preserves 2294 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2304 runtime/1478 words/398 kanji/398 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**150 N3**/2 N2; **217 N3 remain**. Strict progress: **2304
reviewed-current/two excluded reviewed blocked-media drafts/5972 pending of 8278; 5974 runtime
paths absent**. Version `6f11296688f71eb7`; checkpoint authority null/Ready false. Prior 082–113
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 115+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch113 become, war, return and place kanji

Batch113 adds **four complete Russian frozen N3 lessons, 成/戦/戻/所, 270 file lines**,
and four RAW-identical Japanese KanjiVG assets. Eight whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (戦争→戦; 戻る→戻; 事務所, 住所, 台所, 場所, 所, 近所→所),
planned in the signed intake; no whole-label wrapper and no navigation amendment. All visible prose,
Japanese metadata, quiz arrays, old links and frozen levels of those words remain unchanged. Frozen EN
remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/113-become-war-return-and-place-kanji-independent-review-001.json) (one reviewer) of
original candidate `66316abd112bc5621fb36ccc5ad2536dc3b79d09` read **48 whole teaching bodies, 25 EN/23
CURRENT RU** (four primary pairs, 16 context pairs including the eight NAV words, three linked-only
existing word pairs 本/試合/部屋, and two EN-only comparison bodies: the かえる article and 完成),
**68 whole official TEXT units** (17 KANJIDIC2, two radical-evidence units, 45 JMdict, four KanjiPedia)
plus one provider header, all 394 CURRENT typed rows, 12 original directions, four L/four A rulings,
four outside LIMITS, eight exact NAV diffs, four guidance files and three RU rubrics — **61 complete
windows**, 64 successful commands, zero failures, identical opening/closing gates, zero glyph pixels and
zero web pages. The original **5235-byte stdout report**, SHA256
`b1e1779bdc45910ce3e420c7ae4443a5d089a5558f06f5218e661cb82475cce8`, equal to the reviewer's 5234-byte
native final plus one terminal LF, is published verbatim. Actual verdicts: **C1 NEEDS FIX**, **C2
UNVERIFIED** (all eight NAV diffs and links verified; active-negative/runtime option safety not
established), **C3 NEEDS FIX** — finding **113-F001**: the 成 lesson title and H1 «становиться;
совершаться» misdirected learners away from the core senses of 成る/成す.

A signed [pre-mutation title freeze](translation-batches/113-become-war-return-and-place-kanji-review-finding-title-gloss-amendment-freeze-001.json)
(`aa6de027cb691315c81f80e1d5e6ca0e927abd56`) authorised exactly the title and H1; the
[corrected candidate](translation-batches/113-become-war-return-and-place-kanji-corrected-candidate-001.json) `9c0d08e89b144681713397b613a5f7bda7f47619`
now reads «становиться; добиваться результата» (the reviewer's «достигать результата» adapted to avoid
overlap with the title vocabulary of 達/到). One later [focused review](translation-batches/113-become-war-return-and-place-kanji-independent-review-focused-001.json)
(one different reviewer, never concurrent; 25 windows, 28 commands, zero failures, all 394 typed titles;
2830-byte report) found **113-F001 RESOLVED**, bounded C1/C2/C3 CLEAN, the adaptation sound, and no new
findings. It is not a second whole review; the original verdicts stay immutable and the batch is not
retrospectively whole-CLEAN. The reviewer's optional 戦 «состязание» completeness note is explicitly not
a defect and is recorded, not applied.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all 12
ordinary uses stay **U** (metadata retention is not guard approval). The 成 L ruling was the partial
title finding (now resolved); the other three L and all four A rulings are SUPPORTED; all eight NAV
changes are NAV-ONLY; outside LIMITS (戻 vs 帰 (strong overlap); 所/場/席 «место»; 処 vs 所; 戦 vs 試
via 試合) are observations, not new guards and not cleared for future options.

The [qualified source record](translation-batches/113-become-war-return-and-place-kanji-reviewed-source.json) preserves 2280 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2296 runtime/1478 words/394 kanji/394 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**146 N3**/2 N2; **221 N3 remain**. Strict progress: **2296
reviewed-current/two excluded reviewed blocked-media drafts/5980 pending of 8278; 5982 runtime
paths absent**. Version `cda80c756030dd78`; checkpoint authority null/Ready false. Prior 082–112
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 114+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch112 role, he, pupil, gain and honorific kanji

Batch112 adds **five complete Russian frozen N3 lessons, 役/彼/徒/得/御, 291 file lines**,
and five RAW-identical Japanese KanjiVG assets. Nine whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (役に立つ→役; 彼/彼ら/彼女→彼; 御主人/御礼/昼御飯/晩御飯→御;
生徒→徒; 御礼/昼御飯/晩御飯 keep their CRLF line endings), planned in the signed intake; no whole-label
wrapper and no navigation amendment. All visible prose, Japanese metadata, quiz arrays, old links and
frozen levels of those words remain unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/112-role-he-pupil-gain-and-honorific-kanji-independent-review-001.json) (one reviewer) of
candidate `c0c741edfef9683315ccfc0389bb17ecd7202c40` read **44 whole teaching bodies, 23 EN/21
CURRENT RU** (five primary pairs, 16 context pairs and two EN-only word comparisons: 役, 得意),
**81 whole official TEXT units** (16 KANJIDIC2, one radical-evidence unit, 59 JMdict, five KanjiPedia)
plus one provider header, all 390 CURRENT typed rows, 15 original directions, five L/five A rulings,
five outside LIMITS, nine exact NAV diffs, four guidance files and three RU rubrics — **58 complete
windows**, 61 successful commands, identical opening/closing gates, zero glyph pixels and zero web pages.
**One command failed** (a mistyped `Set-Location` directory, exit 2, no helper output, not credited);
the reviewer reran that exact window (pool 336–373) successfully. The original **6724-byte stdout
report**, SHA256 `1f77ae0ae95d9caf7ecf5fb2cbef0b74b8f696dc6daec63f1f1e05bd47de8a20`, equal to the
reviewer's 6723-byte native final plus one terminal LF, is published verbatim. Actual verdicts:
**C1 CLEAN**, **C2 UNVERIFIED** (nine NAV-only wrappers and links verified; ordinary active-negative/runtime
guard safety not established), **C3 CLEAN**; findings none. The reviewer's optional wording polish
(«передвижение пешком» for 徒, «уважительный/вежливый префикс» for 御) is explicitly not a defect and is
recorded, not applied.

All 15 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all 15
ordinary uses stay **U** (metadata retention is not guard approval); N012 得→特 (トク) and N015 御→後 (ご)
are noted reading contacts. All five L and all five A rulings are SUPPORTED; all nine NAV changes are
NAV-ONLY; outside LIMITS (役 vs 務; 彼 people/third-person neighbours; 徒 vs 歩 (strong overlap); 得 vs
受/利/取/読/失; 御 vs 小 reading, 飯/礼/主 partners, 制) are observations, not new guards and not cleared
for future options.

The [qualified source record](translation-batches/112-role-he-pupil-gain-and-honorific-kanji-reviewed-source.json) preserves 2269 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2288 runtime/1478 words/390 kanji/390 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**142 N3**/2 N2; **225 N3 remain**. Strict progress: **2288
reviewed-current/two excluded reviewed blocked-media drafts/5988 pending of 8278; 5990 runtime
paths absent**. Version `5580c593a1f5bf7b`; checkpoint authority null/Ready false. Prior 082–111
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 113+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch111 ceremony, pull, hit and shape kanji

Batch111 adds **four complete Russian frozen N3 lessons, 式/引/当/形, 241 file lines**,
and four RAW-identical Japanese KanjiVG assets. Twelve whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (式→式; 字引, 引き出し, 引き出す, 引く, 引っ越す→引; お弁当, 本当,
相当, 適当→当; 人形, 形→形), planned in the signed intake; no whole-label wrapper and no navigation amendment.
All visible prose, Japanese metadata, quiz arrays, old links and frozen levels of those words remain
unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/111-ceremony-pull-hit-and-shape-kanji-independent-review-001.json) (one reviewer) of
original candidate `9a8b6927678fc31002c17a133ec00fa8a338cb54` read **60 whole teaching bodies, 31 EN/29
CURRENT RU** (four primary pairs, 25 context pairs including the twelve NAV words, and two EN-only
comparison bodies: 当たる, 形式), **83 whole official TEXT units** (23 KANJIDIC2, four radical-evidence
units, 52 JMdict, four KanjiPedia) plus one provider header, all 385 CURRENT typed rows, 12 original
directions, four L/four A rulings, four outside LIMITS, 12 exact NAV diffs, four guidance files and three
RU rubrics — **63 complete windows**, 66 successful commands, zero failures, identical opening/closing
gates, zero glyph pixels and zero web pages. The original **5914-byte stdout report**, SHA256
`26af0c0751ca8c33118b029f845a5d60139c2f21afd0e72d3031e606cee76c06`, equal to the reviewer's 5913-byte
native final plus one terminal LF, is published verbatim. Actual verdicts: **C1 CLEAN**, **C2 UNVERIFIED**
(all 12 NAV diffs and links verified; ordinary active-negative/fallback quiz safety not established),
**C3 NEEDS FIX** — finding **111-F001**: the sense list «формулу или установленную форму, способ» in
«Значение и происхождение» of the 式 lesson was ambiguous.

A signed [pre-mutation wording freeze](translation-batches/111-ceremony-pull-hit-and-shape-kanji-review-finding-list-wording-amendment-freeze-001.json)
(`5b286f176f08274df8ffae6bd156b5f85eb76e25`) authorised exactly that one line; the
[corrected candidate](translation-batches/111-ceremony-pull-hit-and-shape-kanji-corrected-candidate-001.json) `38b94207f9b7b950a32dd2dd1515e85c370d2c2c`
now reads «式 может обозначать церемонию, формулу, а также установленную форму или способ.» (the reviewer's
wording, adopted verbatim). One later [focused review](translation-batches/111-ceremony-pull-hit-and-shape-kanji-independent-review-focused-001.json) (one
different reviewer, never concurrent; 21 windows, 24 commands, zero failures; 1706-byte report) found
**111-F001 RESOLVED**, bounded C1/C2/C3 CLEAN, the wording accurate, and no new findings. It is not a
second whole review; the original verdicts (including C2 UNVERIFIED) stay immutable and the batch is not
retrospectively whole-CLEAN.

Ten directions are **S-intro** (introductory/source-core only, canonical author mapping Q); **N006 引→写
and N012 形→新 are U** (withheld, retained only as frozen source metadata); all 12 ordinary uses stay
**U** (metadata retention is not guard approval). All four L rulings are SUPPORTED within introductory
scope and all four A rulings SUPPORTED_BOUNDED; all 12 NAV changes are NAV-ONLY; outside LIMITS (式 vs
形/方/会; 引 vs 取/出/持; 当 vs 正/本当/真 and the 中 reading; 形 vs 体 «форма») are observations, not new
guards and not cleared for future options.

The [qualified source record](translation-batches/111-ceremony-pull-hit-and-shape-kanji-reviewed-source.json) preserves 2258 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2278 runtime/1478 words/385 kanji/385 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**137 N3**/2 N2; **230 N3 remain**. Strict progress: **2278
reviewed-current/two excluded reviewed blocked-media drafts/5998 pending of 8278; 6000 runtime
paths absent**. Version `7e0ae657bf39c8a5`; checkpoint authority null/Ready false. Prior 082–110
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 112+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch110 market, teacher, seat and usual kanji

Batch110 adds **four complete Russian frozen N3 lessons, 市/師/席/常, 242 file lines**,
and four RAW-identical Japanese KanjiVG assets. Six whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (市/市場/市民→市, 出席/席→席, 非常に→常; all six LF-only),
planned in the signed intake; no whole-label wrapper and no navigation amendment. All visible prose,
Japanese metadata, quiz arrays, old links and frozen levels of those words remain unchanged. Frozen EN
remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. The signed semantic freeze stated a prospective
runtime count of 2266 by author miscount; the actual candidate count 2270 (2262 + four lessons + four
stroke files) is recorded in the candidate record, and the freeze is not rewritten.

The [actual whole independent review](translation-batches/110-market-teacher-seat-and-usual-kanji-independent-review-001.json) (one reviewer) of
candidate `1cf02f67cd180038532ab18e1c2c0e742a3f6ca8` read **36 whole teaching bodies, 20 EN/16
CURRENT RU** (four primary pairs, 12 context pairs and four EN-only comparison bodies: the
occupation-and-role-endings article, 教師, 欠席, 非常口), **61 whole official TEXT units** (13 KANJIDIC2,
one radical-evidence unit, 43 JMdict, four KanjiPedia) plus one provider header, all 381 CURRENT typed
rows, 12 original directions, four L/four A rulings, four outside LIMITS, six exact NAV diffs, four
guidance files and three RU rubrics — **53 complete windows**, 56 successful commands, zero failures,
identical opening/closing gates, zero glyph pixels and zero web pages. The original **5190-byte stdout
report**, SHA256 `25b8eee9a548eaf085d89d1f6383ec804faad96ac950fe54638eb9a49f1f3f18`, equal to the
reviewer's 5189-byte native final plus one terminal LF, is published verbatim. Actual verdicts: **C1
CLEAN**, **C2 CLEAN** (the reviewer states this is content-level review, not runtime quiz acceptance;
NAV diffs and links verified), **C3 CLEAN**; findings none; optional none.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all 12
ordinary uses stay **U** (metadata retention is not guard approval; C2 CLEAN does not upgrade them).
All four L and all four A rulings are SUPPORTED; all six NAV changes are NAV-ONLY; outside LIMITS
(市 vs 町/場; 師 vs 先/者/教; 席 vs 座 (strong title overlap)/場/出; 常 vs 毎/日) are observations, not new
guards and not cleared for future options.

The [qualified source record](translation-batches/110-market-teacher-seat-and-usual-kanji-reviewed-source.json) preserves 2256 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2270 runtime/1478 words/381 kanji/381 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**133 N3**/2 N2; **234 N3 remain**. Strict progress: **2270
reviewed-current/two excluded reviewed blocked-media drafts/6006 pending of 8278; 6008 runtime
paths absent**. Version `c97f5998cc1e84fd`; checkpoint authority null/Ready false. Prior 082–109
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 111+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch109 seat and garden kanji

Batch109 adds **two complete Russian frozen N3 lessons, 座/庭, 116 file lines**,
and two RAW-identical Japanese KanjiVG assets. Three whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (座る→座, 庭→庭, 家庭→庭; CRLF line endings kept), planned in the
signed intake; no whole-label wrapper and no navigation amendment. All visible prose, Japanese metadata,
quiz arrays, old links and frozen levels of those words remain unchanged. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/109-seat-and-garden-kanji-independent-review-001.json) (one reviewer) of
original candidate `a38f1c4c531ae9f73757091f6e143dc778ba851e` read **20 whole teaching bodies, 10 EN/10
CURRENT RU** (two primary pairs and eight context pairs, including the three NAV words), **29 whole
official TEXT units** (9 KANJIDIC2, one radical-evidence unit, 17 JMdict, two KanjiPedia) plus one
provider header, all 377 CURRENT typed rows, six original directions, two L/two A rulings, two outside
LIMITS, three exact NAV diffs, four guidance files and three RU rubrics — **44 complete windows**, 47
successful commands, zero failures, identical opening/closing gates, zero glyph pixels and zero web
pages. The original **4623-byte stdout report**, SHA256
`af92edca08ef2493236ef04a468fd9c87a1e430271932cf782dd9f699f7a670d`, equal to the reviewer's 4622-byte native
final plus one terminal LF, is published verbatim. Actual verdicts: **C1 CLEAN**, **C2 UNVERIFIED** (NAV
diffs and links verified; ordinary active-negative quiz safety not checked), **C3 NEEDS FIX** — finding
**109-F001**: the Japanese classification label 会意形声 in «Значение и происхождение» of the 座 and 庭
lessons was not glossed in Russian.

A signed [pre-mutation term-gloss freeze](translation-batches/109-seat-and-garden-kanji-review-finding-term-gloss-amendment-freeze-001.json)
(`5a01830e8d0ddf43ea8529d477e5d4af544742a1`) authorised exactly one line in each lesson; the
[corrected candidate](translation-batches/109-seat-and-garden-kanji-corrected-candidate-001.json) `3c78c3f6fd5fe93e0ce4d03e0a43b2dd0756283c`
now reads «знак 会意形声 — части соединены по смыслу, и одна из них указывает ещё и на звучание», followed by
a «Здесь …» sentence with the unchanged component explanation. The reviewer's example gloss was adopted in
substance, not verbatim. One later [focused review](translation-batches/109-seat-and-garden-kanji-independent-review-focused-001.json) (one different
reviewer, never concurrent; 22 windows, 25 commands, zero failures; 2523-byte report) found **109-F001
RESOLVED**, bounded C1/C2/C3 CLEAN, the gloss accurate, and no new findings. It is not a second whole
review; the original verdicts (including C2 UNVERIFIED) stay immutable and the batch is not
retrospectively whole-CLEAN.

All six directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all six
ordinary uses stay **U** (metadata retention is not guard approval). Both L rulings are
SUPPORTED_WITHIN_INTRODUCTORY_SOURCE and both A rulings SOURCE_SUPPORTED_BOUNDED_CLARIFICATION; all three
NAV changes are NAV-ONLY; outside LIMITS (座 vs 場 «место»/居/立/席; 庭 vs 園 «сад»/家/公) are observations,
not new guards and not cleared for future options.

The [qualified source record](translation-batches/109-seat-and-garden-kanji-reviewed-source.json) preserves 2255 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2262 runtime/1478 words/377 kanji/377 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**129 N3**/2 N2; **238 N3 remain**. Strict progress: **2262
reviewed-current/two excluded reviewed blocked-media drafts/6014 pending of 8278; 6016 runtime
paths absent**. Version `55ad396f14ddcd39`; checkpoint authority null/Ready false. Prior 082–108
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 110+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch108 difference, peace, fortune and how-many kanji

Batch108 adds **four complete Russian frozen N3 lessons, 差/平/幸/幾, 230 file lines**,
and four RAW-identical Japanese KanjiVG assets. Six whole current word bodies receive one
**NAV-only standalone-glyph wrapper** each (交差点/差し上げる/差す→差, 幸せ/幸福→幸, 幾つ→幾; CRLF kept in
交差点/差す/幸福/幾つ, LF-only kept in 差し上げる/幸せ), planned in the signed intake; no whole-label wrapper
and no navigation amendment. All visible prose, Japanese metadata, quiz arrays, old links and frozen
levels of those words remain unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/108-difference-peace-fortune-and-how-many-kanji-independent-review-001.json) (one reviewer) of
candidate `42ba5e85bc1b35c47b21a43f377ff35079e069c4` read **45 whole teaching bodies, 24 EN/21
CURRENT RU** (four primary pairs, 17 context pairs and three EN-only comparison bodies 差/平和/平等),
**85 whole official TEXT units** (19 KANJIDIC2, three radical-evidence units, 59 JMdict, four
KanjiPedia) plus one provider header, all 375 CURRENT typed rows, 12 original directions, four L/four A
rulings, four outside LIMITS, six exact NAV diffs, four guidance files and three RU rubrics — **57
complete windows**, 61 commands: 60 successful plus one stdout delivery attempt that failed its own
11000-byte size assertion (11151 bytes, exit 1, not a report) before a successful shortened retry;
identical opening/closing gates, zero glyph pixels and zero web pages. The original **7101-byte stdout
report**, SHA256 `0f4d7d14afd930e561b4debfa9d79b81a89055528b92a9f409820f4495a81ee0`, equal to the
reviewer's 7100-byte native final plus one terminal LF, is published verbatim (its Snapshot line drops
the last hex digit of the candidate hash; both gates verified the full hash). Actual verdicts: **C1
CLEAN**, **C2 UNVERIFIED** (NAV diffs and links verified; ordinary active-negative quiz/fallback
behaviour not checked), **C3 CLEAN**; findings none confirmed; optional none.

All 12 directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all 12
ordinary uses stay **U** (metadata retention is not guard approval); the reviewer notes the real サ
reading overlap for 差→左. All four L rulings are SUPPORTED and all four A rulings
SOURCE-SUPPORTED/BOUNDED; all six NAV changes are NAV-ONLY; outside LIMITS (差 vs 間 «промежуток»/別/他/
変/交; 平 vs 和/安/世 with the Russian «мир» homonym/公; 幸 vs 福/運 «удача»/喜/楽/好/不; 幾 vs 何/多/少) are
observations, not new guards and not cleared for future options.

The [qualified source record](translation-batches/108-difference-peace-fortune-and-how-many-kanji-reviewed-source.json) preserves 2244 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2258 runtime/1478 words/375 kanji/375 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**127 N3**/2 N2; **240 N3 remain**. Strict progress: **2258
reviewed-current/two excluded reviewed blocked-media drafts/6018 pending of 8278; 6020 runtime
paths absent**. Version `2dff1832b3fa8bda`; checkpoint authority null/Ready false. Prior 082–107
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 109+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch107 bureau and reside kanji

Batch107 adds **two complete Russian frozen N3 lessons, 局/居, 117 file lines**,
and two RAW-identical Japanese KanjiVG assets. One whole current word body receives a
**NAV-only standalone-glyph wrapper** (郵便局→局; its CRLF line endings are kept), planned in the signed
intake; no whole-label wrapper and no navigation amendment. All visible prose, Japanese metadata, quiz
arrays, old links and frozen levels of that word remain unchanged. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/107-bureau-and-reside-kanji-independent-review-001.json) (one reviewer) of
candidate `5cb99596bc51a01516173816ea8385fb6b89c9e9` read **20 whole teaching bodies, 11 EN/9
CURRENT RU** (two primary pairs, five context pairs, two linked existing-word pairs いる/今 and two
EN-only comparison bodies 居間/薬局), **32 whole official TEXT units** (8 KANJIDIC2, one
radical-evidence unit, 21 JMdict, two KanjiPedia) plus one provider header, all 371 CURRENT typed rows,
six original directions, two L/two A rulings, two outside LIMITS, one exact NAV diff, four guidance files
and three RU rubrics — **44 complete windows**, 47 successful commands, zero failures, identical
opening/closing gates, zero glyph pixels and zero web pages. The original **3464-byte stdout report**,
SHA256 `365abcee9fd9fbb78dbedf4af0c81d2ae1dd5a74aef1ae7d144012a61a645061`, equal to the reviewer's
3463-byte native final plus one terminal LF, is published verbatim. Actual verdicts: **C1 CLEAN**,
**C2 CLEAN** (bounded; explicitly not a runtime quiz/fallback test), **C3 CLEAN**; findings none;
optional none.

All six directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all
six ordinary uses stay **U** (metadata retention is not guard approval). Both L rulings are
SUPPORTED_WITHIN_INTRODUCTORY_SOURCE and both A rulings SOURCE_SUPPORTED_BOUNDED_CLARIFICATION; the NAV
change is NAV-ONLY; outside LIMITS (局 vs 院/官/社/館/店; 居 vs 住/在/有/存/宅/家 and the 居間–今 homophone)
are observations, not new guards and not cleared for future options.

The [qualified source record](translation-batches/107-bureau-and-reside-kanji-reviewed-source.json) preserves 2245 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2250 runtime/1478 words/371 kanji/371 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**123 N3**/2 N2; **244 N3 remain**. Strict progress: **2250
reviewed-current/two excluded reviewed blocked-media drafts/6026 pending of 8278; 6028 runtime
paths absent**. Version `64c89d457b371b9a`; checkpoint authority null/Ready false. Prior 082–106
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 108+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch106 cold, sleep and inspect kanji

Batch106 adds **three complete Russian frozen N3 lessons, 寒/寝/察, 161 file lines**,
and three RAW-identical Japanese KanjiVG assets. Four whole current word bodies receive
**NAV-only standalone-glyph wrappers** (寒い→寒, 寝る→寝, 寝坊→寝, 警察→察; 寒い and 寝る keep their CRLF
line endings), planned in the signed intake; no whole-label wrapper and no navigation amendment. All visible
prose, Japanese metadata, quiz arrays, old links and frozen levels of those words remain unchanged. Frozen EN
remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/106-cold-sleep-and-inspect-kanji-independent-review-001.json) (one reviewer) of
original candidate `fae77012825f8e1768c75803052476e7784e7247` read **25 whole teaching bodies, 13 EN/12
CURRENT RU** (three primary pairs, nine context pairs and one EN-only comparison body), **47 whole
official TEXT units** (7 KANJIDIC2, one radical-evidence unit, 36 JMdict, three KanjiPedia) plus
one provider header, all 369 CURRENT typed rows, nine original directions, three L/three A rulings,
three outside LIMITS, four exact NAV diffs, four guidance files and three RU rubrics —
**47 complete windows**, 50 successful commands, zero failures, identical opening/closing gates, zero
glyph pixels and zero web pages. The original **4535-byte stdout report**, SHA256
`e3133ed7689332b8216564335c1f417f32f42bb67dc99990c8581cb661ea45c7`, equal to the reviewer's 4534-byte native
final plus one terminal LF, is published verbatim. Actual verdicts: **C1 CLEAN**, **C2 CLEAN** (bounded
content review; four NAV-only wrappers; runtime fallback not exercised), **C3 NEEDS FIX** — finding
**106-F001**: the 寝 lesson note «[眠る] (ねむる) сосредоточено на самом сне» was an awkward, grammatically
mismatched Russian clause.

A signed [pre-mutation wording freeze](translation-batches/106-cold-sleep-and-inspect-kanji-review-finding-wording-amendment-freeze-001.json)
(`f897efa2ae2ee2ecf1ee79f1274fec000c5f1650`) authorised exactly one line in kanji/寝.md; the
[corrected candidate](translation-batches/106-cold-sleep-and-inspect-kanji-corrected-candidate-001.json) `dc08c1aaea097d07ac905048bc703507e4c24c51`
now reads «В слове [眠る] (ねむる) акцент на самом сне, а у 寝る есть ещё значение «лежать; ложиться»». The
reviewer's replacement gloss «лечь; отправиться спать» was deliberately not adopted (the existing gloss
follows the frozen EN lying-down sense and JMdict 1360010). One later
[focused review](translation-batches/106-cold-sleep-and-inspect-kanji-independent-review-focused-001.json) (one different reviewer, never
concurrent; 21 windows, 24 commands, zero failures; 3325-byte report) found **106-F001 RESOLVED**,
bounded C1/C2/C3 CLEAN, the kept gloss acceptable, and no new findings. It is not a second whole review;
the original verdicts stay immutable and the batch is not retrospectively whole-CLEAN.

All nine directions are **S-intro** (introductory/source-core only, canonical author mapping Q); all
nine ordinary uses stay **U** (metadata retention is not guard approval). All three L and three A
rulings are SUPPORTED and bounded; all four NAV changes NAV-ONLY; outside LIMITS (寒 vs 冷/冬, 寝 vs
夢/休/起/夜, 察 vs 見/知/思/考/判) are observations, not new guards.

The [qualified source record](translation-batches/106-cold-sleep-and-inspect-kanji-reviewed-source.json) preserves 2236 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2246 runtime/1478 words/369 kanji/369 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**121 N3**/2 N2; **246 N3 remain**. Strict progress: **2246
reviewed-current/two excluded reviewed blocked-media drafts/6030 pending of 8278; 6032 runtime
paths absent**. Version `a994f0996c3cf112`; checkpoint authority null/Ready false. Prior 082–105
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 107+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch105 official, wealth, decide and approach kanji

Batch105 adds **four complete Russian frozen N3 lessons, 官/富/定/寄, 222 file lines**,
and four RAW-identical Japanese KanjiVG assets. Three whole current word bodies receive
**NAV-only standalone-glyph wrappers** (予定→定, 寄る→寄, 警官→官; 警官 keeps its CRLF line endings),
planned in the signed intake; no whole-label wrapper and no navigation amendment. All visible prose,
Japanese metadata, quiz arrays, old links and frozen levels of those words remain unchanged. Frozen EN
remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/105-official-wealth-decide-and-approach-kanji-independent-review-001.json) (one reviewer) of
candidate `033cba3aa08fe18287a5312d5e684f0be9abf6ac` read **36 whole teaching bodies, 19 EN/17
CURRENT RU** (four primary pairs, thirteen context pairs and two EN-only comparison bodies), **84 whole
official TEXT units** (18 KANJIDIC2, one radical-evidence unit, 61 JMdict, four KanjiPedia) plus
one provider header, all 366 CURRENT typed rows, twelve original directions, four L/four A rulings,
four outside LIMITS, three exact NAV diffs, three guidance files and three RU rubrics —
**52 complete windows**, 55 successful commands, zero failures, identical opening/closing gates, zero
glyph pixels and zero web pages. It **never ran the two assigned windows of
docs/content-format-reference.md**, although its Scope line claims all guidance ranges; that claim
is recorded as inaccurate and the review is not treated as complete for that file. The original
**4910-byte stdout report**, SHA256 `b61242a94acdb293fc6febfc98f78fcc9f4950ded5c2aff17ea07a37c5544daa`, equal to the reviewer's
4909-byte native final plus one terminal LF, is published verbatim.

A separate, later [focused supplementary review](translation-batches/105-official-wealth-decide-and-approach-kanji-supplementary-review-001.json)
(one different reviewer, never concurrent) read the whole 108-line content-format reference and the four
complete EN/RU primary pairs: **F1 CLEAN** (format-reference compliance), findings none. Its two
snapshot gates failed because the writer's own untracked first-review record tripped the helper's
untracked-path check; the reviewer reported the snapshot as UNVERIFIED, the writer's diagnostic gate
passed with only that file held aside, and the writer's capture verified every credited window
against the bound candidate text.

Actual verdicts: **C1 CLEAN**, **C2 CLEAN** (bounded content review; runtime fallback was not
exercised), **C3 CLEAN**; findings none; optional none. All twelve directions are **S-intro**
(introductory/source-core only, canonical author mapping Q); all twelve ordinary uses stay **U**
(metadata retention is not guard approval). All four L rulings and all four A rulings are SUPPORTED
and bounded; all three NAV changes NAV-ONLY; outside LIMITS (官 vs 公/員/者, 富 vs 福/多/金,
定 vs 立 shared title token and 予, 寄 vs 近/通/送/付) are observations, not new guards.

The [qualified source record](translation-batches/105-official-wealth-decide-and-approach-kanji-reviewed-source.json) preserves 2229 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2240 runtime/1478 words/366 kanji/366 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**118 N3**/2 N2; **249 N3 remain**. Strict progress: **2240
reviewed-current/two excluded reviewed blocked-media drafts/6036 pending of 8278; 6038 runtime
paths absent**. Version `d5851d6a5b302efe`; checkpoint authority null/Ready false. Prior 082–104
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 106+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch104 guest, harm, lodging and contents kanji

Batch104 adds **four complete Russian frozen N3 lessons, 客/害/宿/容, 221 file lines**,
and four RAW-identical Japanese KanjiVG assets. Three whole current word bodies receive
**NAV-only standalone-glyph wrappers** (下宿→宿, 客→客, 宿題→宿), planned in the signed intake; no
whole-label wrapper and no navigation amendment. All visible prose, Japanese metadata, quiz arrays,
old links and frozen levels of those words remain unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/104-guest-harm-lodging-and-contents-kanji-independent-review-001.json) (one reviewer) of
candidate `82669fd69433962ff3b9c7070da8d2222e2667c9` read **28 whole teaching bodies, 15 EN/13
CURRENT RU** (four primary pairs, nine context pairs and two EN-only comparison bodies), **70 whole
official TEXT units** (14 KANJIDIC2, one radical-evidence unit, 51 JMdict, four KanjiPedia) plus
one provider header, all 362 CURRENT typed rows, twelve original directions, four L/four A rulings,
four outside LIMITS, three exact NAV diffs, the whole guidance files and three RU rubrics —
**51 complete windows**, 54 successful commands, zero failures, identical opening/closing gates, zero
glyph pixels and zero web pages. The original **6051-byte stdout report**, SHA256
`f33af8c4b9eb7c7dd686861107308fae0c3d9982bee281b66f141e7641348377`, equal to the reviewer's
6050-byte native final plus one terminal LF, is published verbatim.

Actual verdicts: **C1 CLEAN**, **C2 CLEAN**, **C3 CLEAN**; findings none. C2 explicitly does not
certify UI fallback selection or all possible quiz compositions. All twelve directions are **S-intro**
(introductory/source-core only, canonical author mapping Q); all twelve ordinary uses stay **U**
(metadata retention is not guard approval). All four L rulings SUPPORTED within the introductory source,
all four A rulings source-supported and bounded; all three NAV changes NAV-ONLY; outside LIMITS
(客 vs 旅/店, 害 vs 悪, 宿 vs 家/宅 and 館/旅, 容 vs 内/中) are observations, not new guards. The
reviewer's optional wording note (прилагательное типа な) was not adopted: な-прилагательное is the
established term across the current Russian corpus.

The [qualified source record](translation-batches/104-guest-harm-lodging-and-contents-kanji-reviewed-source.json) preserves 2221 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2232 runtime/1478 words/362 kanji/362 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**114 N3**/2 N2; **253 N3 remain**. Strict progress: **2232
reviewed-current/two excluded reviewed blocked-media drafts/6044 pending of 8278; 6046 runtime
paths absent**. Version `172b6f6cb7374ac0`; checkpoint authority null/Ready false. Prior 082–103
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 105+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch103 residence, protect, complete and real kanji

Batch103 adds **four complete Russian frozen N3 lessons, 宅/守/完/実, 217 file lines**,
and four RAW-identical Japanese KanjiVG assets. Five whole current word bodies receive
**NAV-only standalone-glyph wrappers** (お宅→宅, 実に→実, 実際→実, 現実→実, 留守→守); no whole-label
wrapper and no navigation amendment. All visible prose, Japanese metadata, quiz arrays, old links
and frozen levels of those words remain unchanged. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/103-residence-protect-complete-and-real-kanji-independent-review-001.json) (one reviewer) of
candidate `95b1839836a0264d670a53610c97903d2c4e2de4` read **37 whole teaching bodies, 20 EN/17
CURRENT RU** (four primary pairs, 13 context pairs and three EN-only comparison bodies), **84 whole
official TEXT units** (14 KANJIDIC2, one radical-evidence unit, 65 JMdict, four KanjiPedia) plus
one provider header, all 358 CURRENT typed rows, twelve original directions, four L/four A rulings,
four dictionary clarifications, four outside LIMITS, five exact NAV diffs, the whole guidance files and
three RU rubrics — **54 complete windows**, identical opening/closing gates, zero glyph pixels and zero
web pages. The first stdout delivery failed its own terminal-LF assertion (a delivery failure, not a
reading failure); the second succeeded. The original **5053-byte stdout report**, SHA256
`0cfb31c85450e1e3df5b67c1548bac6f7c5f9a2a7c60dadc130bedd71f6d271d`, equal to the reviewer's
5052-byte native final plus one terminal LF, is published verbatim.

Actual verdicts: **C1 CLEAN**; **C2 NEEDS FIX** — all five edits are navigation-only with correct
targets, but direction **103-N010 実→完 is REJECTED** (finding **103-F001**): 完 «завершённый;
полный» can fit 実's official みち.る/content-full sense, so a learner could be marked wrong for a
defensible answer; **C3 CLEAN**. The other eleven directions are **S-intro** (introductory/source-core
only, canonical author mapping Q); all eleven ordinary uses stay **U** (metadata retention is not
guard approval). All four L and all four A rulings SUPPORTED-bounded; all five NAV changes NAV-ONLY;
outside LIMITS (宅 vs 家/住, 守 vs 助, 完 vs 終, 実 vs 真/本) are observations, not new guards. The
reviewer's optional 守 wording polish was explicitly "not required" and was not adopted.

A signed [pre-mutation distractor-amendment freeze](translation-batches/103-residence-protect-complete-and-real-kanji-review-finding-distractor-amendment-freeze-001.json)
`668c25ec91d723fd3c99d95f70447b4f200a2e0d` authorized exactly one change: removing 完 from the
distractors of kanji/実.md (now 春, 失), keeping the prose shape comparison with 完 and adding no
new direction. The [corrected candidate](translation-batches/103-residence-protect-complete-and-real-kanji-corrected-candidate-001.json)
`e1f385b741a86b1093c0666f31fe937b9e1e9d00` changes only that line plus the manifest. One
[focused independent review](translation-batches/103-residence-protect-complete-and-real-kanji-independent-review-focused-001.json) read the EN, original RU and
corrected RU 実 bodies, whole JMdict 1320800/1320810/1211490/1211510 entries, KANJIDIC2 実/完/春/失,
KanjiPedia 実/完, the current typed rows, the exact amendment and continuity, and the guidance/rubric
windows (24 complete windows, 27 successful commands, zero failures/web pages); its 2329-byte
report, SHA256 `bb75e23a449e5476e77d1eaf605e20ccbe84f3a3bbac89230baf449bd8e7ad06`, rules **F001
RESOLVED** with C1/C2/C3 CLEAN within that bounded scope and no new findings (its transcription of
the freeze hash drops one digit; the exact commit is recorded above). It is not a second whole
review; the original verdicts stay immutable and the batch is not upgraded to whole CLEAN.

The [qualified source record](translation-batches/103-residence-protect-complete-and-real-kanji-reviewed-source.json) preserves 2211 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2224 runtime/1478 words/358 kanji/358 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**110 N3**/2 N2; **257 N3 remain**. Strict progress: **2224
reviewed-current/two excluded reviewed blocked-media drafts/6052 pending of 8278; 6054 runtime
paths absent**. Version `1412246181bad4e4`; checkpoint authority null/Ready false. Prior 082–102
U qualifications remain unchanged; the existing unlinked 完 mention in RU 院.md and the RU 留守
wording outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 104+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch102 marriage, woman, existence and opposition kanji

Batch102 adds **four complete Russian frozen N3 lessons, 婚/婦/存/対, 224 file lines**,
and four RAW-identical Japanese KanjiVG assets. Six whole current word bodies receive
**NAV-only wrappers**: five standalone-glyph wrappers (反対→対, 婦人→婦, 対する→対, 看護婦→婦,
結婚→婚) and one whole-label wrapper, 存じ in words/ご存じ.md → kanji/存.md, authorized by the signed
[pre-mutation whole-label navigation amendment](translation-batches/102-marriage-woman-existence-and-opposition-kanji-pre-mutation-whole-label-navigation-amendment-001.json).
All visible prose, Japanese metadata, quiz arrays, old links and frozen levels remain unchanged;
no new guard or removed direction. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/102-marriage-woman-existence-and-opposition-kanji-independent-review-001.json) (one reviewer) of
candidate `c199d4ca7073a14c6d8a286ba5e0c6410f30f7ae` read **48 whole teaching bodies, 25 EN/23
CURRENT RU** (four primary pairs, 19 context pairs and two EN comparison bodies), **102 whole
official TEXT units** (22 KANJIDIC2, three radical-evidence units, 73 JMdict, four KanjiPedia) plus
one provider header, all 354 CURRENT typed rows, twelve original directions, four L/four A rulings,
four dictionary clarifications, four outside LIMITS, six exact NAV diffs, the whole guidance files and
three RU rubrics — **59 complete windows**, identical opening/closing gates, zero glyph pixels, zero
web pages, 62 successful commands and zero failures. The original **10286-byte stdout report**,
SHA256 `8a52d52d8576b1407fc2439069641dae84a1e79a561d91bb748c864f48a85b76`, byte-identical to the
reviewer's native final, is published verbatim.

Actual verdicts: **C1 CLEAN**; **C2 UNVERIFIED** — all six edits are navigation-only with
correct targets and the 存じ whole-label wrapper matches the amendment, but ordinary
active-negative quiz safety is not established for any direction; **C3 NEEDS FIX** with one
minor finding, **102-F001**: kanji/婦.md called 婦人 «потенциально чувствительное», an unexplained
calque that does not tell a learner whether offensiveness or emotional sensitivity is meant. All
twelve directions are **S-intro** (introductory/source-core only, canonical author mapping Q), none
withheld; all twelve ordinary uses are **U** (metadata retention is not guard approval). All four
L rulings SUPPORTED-intro; A001/A003/A004 SUPPORTED-bounded and **A002 PARTLY SUPPORTED**: the
author capture called JMdict 2857591 «literary», but its actual marker is «dated term» (sense not
taught). All six NAV changes NAV-ONLY; outside LIMITS (婚 vs 帰/妻/夫, 婦 vs 女/妻, 存 vs 在/有/知,
対 vs 反/向) are observations, not new guards.

A signed [pre-mutation register-amendment freeze](translation-batches/102-marriage-woman-existence-and-opposition-kanji-review-finding-register-amendment-freeze-001.json)
authorized exactly two lines of kanji/婦.md: «требующее осторожности из-за возможной
оскорбительности» for the 婦人 warning, and the reviewer's optional polish «один из членов
супружеской пары» in the 夫婦 explanation. The A002 characterization is corrected in that freeze and
this acceptance record only; the frozen author record is not rewritten. The
[corrected candidate](translation-batches/102-marriage-woman-existence-and-opposition-kanji-corrected-candidate-001.json) `db62612f84b8b8e9b0e4667d184ef71a3f6abc84`
changes only those two lines plus the manifest. One
[focused independent review](translation-batches/102-marriage-woman-existence-and-opposition-kanji-independent-review-focused-001.json) read the EN, original RU and
corrected RU 婦 bodies, whole JMdict 1496670/1583640/2857591 entries, the exact amendment and
continuity, and the guidance/rubric windows (21 complete windows, 24 successful commands, zero
failures/web pages); its 2027-byte report, SHA256
`5bfcc7c4884ad2f0e27b73a35d55a9a91f635d6b0ccb7cd9e687c90be2623b0d`, rules **F001 RESOLVED**, the
polish incorporated and the A002 correction accurate, with C1/C2/C3 CLEAN within that bounded scope
and no new findings. It is not a second whole review; the original verdicts stay immutable and the
batch is not upgraded to whole CLEAN.

The [qualified source record](translation-batches/102-marriage-woman-existence-and-opposition-kanji-reviewed-source.json) preserves 2202 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2216 runtime/1478 words/354 kanji/354 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**106 N3**/2 N2; **261 N3 remain**. Strict progress: **2216
reviewed-current/two excluded reviewed blocked-media drafts/6060 pending of 8278; 6062 runtime
paths absent**. Version `f0bef69f37056089`; checkpoint authority null/Ready false. Prior 082–101
U qualifications remain unchanged; the existing RU 天/夫 stroke wording and RU 時 metadata
differences outside this batch remain open observations. Protected 033 WORD空 stays
excluded/runtime-absent/not media. No device/media/default/package/release authority. Continue 103+
and **ALL remaining safe frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch101 dream, like, wife and daughter kanji

Batch101 adds **four complete Russian frozen N3 lessons, 夢/好/妻/娘, 222 file lines**,
and four RAW-identical Japanese KanjiVG assets. Six whole current word bodies receive
**NAV-only wrappers**: five standalone-glyph wrappers (夢→夢, 好き→好, 妻→妻, 娘→娘, 格好→好)
and one whole-label wrapper, 好き in words/大好き.md → kanji/好.md, authorized by the signed
[pre-mutation whole-label navigation amendment](translation-batches/101-dream-like-wife-and-daughter-kanji-pre-mutation-whole-label-navigation-amendment-001.json).
All visible prose, Japanese metadata, quiz arrays, old links and frozen levels remain unchanged;
no new guard or removed direction. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/101-dream-like-wife-and-daughter-kanji-independent-review-001.json) (one reviewer) of
candidate `b9d1be9f20d5d50c909b891ddeae9f03e74c3a81` read **44 whole teaching bodies, 22 EN/22
CURRENT RU** (four primary pairs and 18 context pairs), **100 whole official TEXT units** (19
KANJIDIC2, two radical-evidence units, 75 JMdict, four KanjiPedia) plus one provider header, all 350
CURRENT typed rows, twelve original directions, four L/four A rulings, four outside LIMITS,
six exact NAV diffs, four whole guidance files and three RU rubrics — **57 complete windows**,
identical opening/closing gates, zero glyph pixels, zero web pages; it did not read the optional
夫.md/良.md. One report emission failed (exit 1) only because the literal lacked its terminal LF;
the next emission succeeded. The original **5466-byte stdout report**, SHA256
`632dad84d074a3666e61ca257b0f1249ecd4af3cb314e3f8523ec7800f66d4de`, is published verbatim.

Actual verdicts: **C1 CLEAN**; **C2 UNVERIFIED** — all six edits are navigation-only with
correct targets and the 好き whole-label wrapper matches the amendment, but ordinary
active-negative quiz safety is not established for any direction; **C3 NEEDS FIX** with one
finding, **101-F001**: kanji/妻.md said 夫妻 is «несколько официальное», suggesting official
status rather than JMdict 1496520's "somewhat formal" register. Ten directions are **S-intro**
(introductory/source-core only, canonical author mapping Q); **N002 夢→夜 and N004 好→妹 are U**
(withheld, retained in frozen source metadata as ordinary negatives, not guard approval); all
twelve ordinary uses are **U**. All four L rulings SUPPORTED and four A clarifications
SOURCE-SUPPORTED, BOUNDED; all six NAV changes NAV-ONLY; outside LIMITS (evening/night,
favorable/good, spouse/female, child/female/component) are observations, not new guards.

A signed [pre-mutation register-amendment freeze](translation-batches/101-dream-like-wife-and-daughter-kanji-review-finding-register-amendment-freeze-001.json)
authorized exactly one word, официальное→формальное, in that line of kanji/妻.md **and in the
identical author-written line of kanji/夫.md, accepted in batch100** (same JMdict entry, same
defect). This is a disclosed cross-batch correction of accepted text; historical batch100
records are not rewritten. The [corrected candidate](translation-batches/101-dream-like-wife-and-daughter-kanji-corrected-candidate-001.json)
`b00ac8be8e4fb98be5d202cb7daf0f9ccefb7405` changes only those two lines plus the manifest. One
[focused independent review](translation-batches/101-dream-like-wife-and-daughter-kanji-independent-review-focused-001.json) read the six
EN/original/corrected 妻/夫 bodies, the whole JMdict 1496520 entry, the exact amendment diffs,
continuity and all guidance/rubric windows (22 complete windows, 25 successful commands, zero
failures/web pages); its 1963-byte report, SHA256
`a91756930e09b7ecdc70bd37806f8c990510a84e4f15e39de42582b6025669b0`, rules **F001 RESOLVED** in
both files with C1/C2/C3 CLEAN within that bounded scope and no new findings. It is not a second
whole review; the original verdicts stay immutable and the batch is not upgraded to whole CLEAN.

The [qualified source record](translation-batches/101-dream-like-wife-and-daughter-kanji-reviewed-source.json) preserves 2193 other baseline
runtime RAWs/tracking rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint:
**2208 runtime/1478 words/350 kanji/350 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled
unchanged; kanji 80 N5/166 N4/**102 N3**/2 N2; **265 N3 remain**. Strict progress: **2208
reviewed-current/two excluded reviewed blocked-media drafts/6068 pending of 8278; 6070 runtime
paths absent**. Version `036029d3a8e204ca`; checkpoint authority null/Ready false. Prior 082–100
U qualifications remain unchanged. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 102+ and **ALL remaining safe
frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch100 change, thick, husband and loss kanji

Batch100 adds **four complete Russian frozen N3 lessons, 変/太/夫/失, 242 file lines**,
and four RAW-identical Japanese KanjiVG assets. Thirteen whole current word bodies receive
**NAV-only standalone-glyph wrappers** (丈夫→夫, 変→変, 変える→変, 変わる→変, 変化→変, 変更→変,
大丈夫→夫, 大変→変, 太い→太, 太る→太, 太陽→太, 夫→夫, 失敗→失), planned in the signed intake;
no navigation amendment was needed. All visible prose, Japanese metadata, quiz arrays, old links
and frozen levels remain unchanged; no new guard or removed direction. Optional links to
articles/kaeru-change-replace-and-return.md, articles/ayashii-and-related-words.md, kanji/妻.md
and words/夫婦.md stay unwrapped because those files are EN-only. The signed semantic freeze
recorded a prospective count of 2196 runtime objects in arithmetic error (actual 2192+4+4=2200);
the erratum is disclosed in the candidate record, not rewritten, and has no semantic effect.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/100-change-thick-husband-and-loss-kanji-independent-review-001.json) (one reviewer) read **56 whole
teaching bodies, 30 EN/26 CURRENT RU**: four primary pairs, 22 current context pairs and
four EN-only comparisons (the two articles, kanji/妻.md, words/夫婦.md), including all thirteen
changed words; **89 whole official TEXT units** (15 KANJIDIC, two Unicode, 68 JMdict, four
visible KanjiPedia) plus one provider header; all 346 CURRENT typed rows, twelve original
directions, four L/four A rulings, four outside LIMITS, thirteen exact NAV diffs, four whole
guidance files and three RU rubrics — **63 complete windows** (the two long comparisons by
complete line unions), 66 successful terminal commands, zero failures/truncations/waits,
identical opening/closing gates, zero glyph pixels, zero web pages. The original **6278-byte
stdout report**, SHA256 `36ab037cdd776352c6238f889b5158d7abcdba7f296ed50b11304315e131ea24`,
is published verbatim with its final LF; the child/task native final is the identical
6277-byte text without the terminal LF. Its Scope line says "5 EN-only comparisons"; the bound
units are four, read in five windows (wording note, report not rewritten). No projection or
second review.

Actual verdicts: **C1 CLEAN** (four new lessons within bounded official evidence),
**C2 UNVERIFIED** — all thirteen edits are glyph-only wrappers to the matching new cards, with
unchanged prose/metadata, but ordinary active-negative quiz safety is not established for any
direction — and **C3 CLEAN** (Russian comprehension of new lessons and wrapper readability; not
native certification). Findings: none; optional: none. All **twelve directions are S-intro**
(introductory/source-core comparison only, canonical author mapping Q) with ordinary safety
**U**; metadata retention is not guard approval. All four L rulings SUPPORTED-intro and four A
clarifications SUPPORTED-bounded; all thirteen NAV changes NAV-ONLY. Outside LIMITS record
adjacency concerns, not guards: 化/変 shared «изменение» (disambiguated by the second gloss),
大/太 size domain, 主/男/大 near 夫, 死/失 and 礼/失礼. The existing RU kanji/天.md describes
夫's top stroke differently from the new 夫 lesson; this outside observation remains open,
unresolved and not adjudicated in batch100.

The [qualified source record](translation-batches/100-change-thick-husband-and-loss-kanji-reviewed-source.json) preserves 2179 other baseline runtime RAWs/tracking
rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2200 runtime/
1478 words/346 kanji/346 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged;
kanji 80 N5/166 N4/**98 N3**/2 N2; **269 N3 remain**. Strict progress: **2200 reviewed-current/
two excluded reviewed blocked-media drafts/6076 pending of 8278; 6078 runtime paths absent**.
Version `0311e367192bec83`; checkpoint authority null/Ready false. Prior 082–099 U
qualifications remain unchanged. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 101+ and **ALL remaining safe
frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch099 existence, report, increase and dark kanji

Batch099 adds **four complete Russian frozen N3 lessons, 在/報/増/暗, 218 file lines**,
and four RAW-identical Japanese KanjiVG assets. Four whole current word bodies receive
**NAV-only standalone-glyph wrappers** (増える→増, 天気予報→報, 暗い→暗, 電報→報),
planned in the signed intake; no navigation amendment was needed. All visible prose, Japanese metadata, quiz arrays, old links
and frozen levels remain unchanged; no new guard or removed direction. The optional 存在 and
報告 links stay unwrapped because words/存在.md and words/報告.md are EN-only. A frozen
proposal key mislabelled "prior099" (meaning prior098) is disclosed in the candidate record,
not rewritten. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/099-existence-report-increase-and-dark-kanji-independent-review-001.json) (one reviewer) read **44 whole
teaching bodies, 23 EN/21 CURRENT RU**: four primary pairs, 17 current context pairs and
two EN-only comparisons (words/報告.md, words/存在.md), including all four changed words;
**89 whole official TEXT units** (21 KANJIDIC, two Unicode, 62 JMdict, four visible
KanjiPedia) plus one provider header; all 342 CURRENT typed rows, twelve original directions,
four L/four A rulings, four outside LIMITS, four exact NAV diffs, four whole guidance files and
three RU rubrics — **57 complete windows**, 60 successful terminal commands, zero failures/
truncations/waits, identical opening/closing gates, zero glyph pixels, zero web pages. The
original **6419-byte stdout report**, SHA256
`73b5975e595210095c2bbc70653870d01ba6c71c07a83b11ea693fbbd10f7394`, is published verbatim
with its final LF; the child/task native final is the identical 6418-byte text without the
terminal LF. No projection or second review.

Actual verdicts: **C1 CLEAN** (four new lessons within bounded official evidence),
**C2 UNVERIFIED** — all four edits are standalone link wrappers to valid targets, but ordinary
active-negative quiz safety is not established for any direction, and the reviewer left
words/暗い.md whole-file raw parity unverified because the helper compared different hash
domains — and **C3 CLEAN** (Russian comprehension of new lessons and wrapper readability; not
native certification). Findings: none confirmed; optional: none. The writer's post-review
mechanical reconciliation (recorded in the review artifact, not reviewer approval) shows the
暗い working copy is exactly the CRLF projection of the LF Git blobs before and after, whose
56 lines differ only by the one wrapper. All **twelve directions are S-intro**
(introductory/source-core comparison only, canonical author mapping Q) with **ordinary U**
stated by the reviewer; metadata retention is not guard approval. All four L rulings and four
A clarifications SUPPORTED within bounded scope; all four NAV changes NAV-ONLY. Outside LIMITS
record overlap concerns, not guards: 有/在 «существовать» (inherited from EN), 報/告/伝
«сообщ-» root (introduced by Russian titles), increase/add/many/layer and dark/colour/light/
night adjacency.

The [qualified source record](translation-batches/099-existence-report-increase-and-dark-kanji-reviewed-source.json) preserves 2180 other baseline runtime RAWs/tracking
rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2192 runtime/
1478 words/342 kanji/342 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged;
kanji 80 N5/166 N4/**94 N3**/2 N2; **273 N3 remain**. Strict progress: **2192 reviewed-current/
two excluded reviewed blocked-media drafts/6084 pending of 8278; 6086 runtime paths absent**.
Version `22dd52644a6a5394`; checkpoint authority null/Ready false. Prior 082–098 U
qualifications remain unchanged. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 100+ and **ALL remaining safe
frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch098 turns, cause, trouble and garden kanji

Batch098 adds **four complete Russian frozen N3 lessons, 回/因/困/園, 226 file lines**,
and four RAW-identical Japanese KanjiVG assets. Five whole current word bodies receive
**NAV-only standalone-glyph wrappers** (公園→園, 動物園→園, 原因→因, 回る→回, 困る→困),
planned in the signed intake; no navigation amendment was needed. All visible prose,
Japanese metadata, quiz arrays, old links and frozen levels remain unchanged; no new guard
or removed direction. The optional 公演 link in kanji/園.md stays unwrapped because
words/公演.md is EN-only. Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/098-turns-cause-trouble-and-garden-kanji-independent-review-001.json) (one reviewer) read **23 whole
teaching bodies, 12 EN/11 CURRENT RU**: four primary pairs, seven current context pairs and
one EN-only comparison (words/公演.md), including all five changed words; **70 whole official
TEXT units** (nine KANJIDIC, one Unicode, 56 JMdict, four visible KanjiPedia) plus one
provider header; all 338 CURRENT typed rows, twelve original directions, four L/four A
rulings, four outside LIMITS, five exact NAV diffs, four whole guidance files and three RU
rubrics — **48 complete windows**, 51 successful terminal commands, zero failures/
truncations/waits, identical opening/closing gates, zero glyph pixels, zero web pages. The
original **5824-byte stdout report**, SHA256
`ffa466864fc28c41d6f34425b2c0aaf8531d0f073e82d2fa3f558efcb30759db`, is published verbatim
with its final LF; the child/task native final is the identical 5823-byte text without the
terminal LF. No projection or second review.

Actual verdicts: **C1 CLEAN** (four new lessons within bounded official evidence),
**C2 UNVERIFIED** — all five edits precisely NAV-only and links resolve, but ordinary
active-negative quiz safety is not established for any direction — and **C3 CLEAN**
(Russian comprehension of new lessons and wrapper readability; not native certification).
Findings: none confirmed. All **twelve directions are S-intro** (introductory/source-core
comparison only, canonical author mapping Q) with **ordinary U** stated by the reviewer;
metadata retention is not guard approval. All four L rulings and four A clarifications
SUPPORTED within bounded scope; all five NAV changes NAV-ONLY. Outside LIMITS record overlap
concerns, not guards: 回 vs current 度 on «раз» (inherited from EN), 因 vs current 由 on
«причина» (introduced by Russian titles), trouble/adversity/poverty and garden/place/facility
adjacency. One optional polish suggestion (briefly gloss «онное/кунное чтение» at first use)
was not applied in 098.

The [qualified source record](translation-batches/098-turns-cause-trouble-and-garden-kanji-reviewed-source.json) preserves 2171 other baseline runtime RAWs/tracking
rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2184 runtime/
1478 words/338 kanji/338 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged;
kanji 80 N5/166 N4/**90 N3**/2 N2; **277 N3 remain**. Strict progress: **2184 reviewed-current/
two excluded reviewed blocked-media drafts/6092 pending of 8278; 6094 runtime paths absent**.
Version `01b440869053b33c`; checkpoint authority null/Ready false. Prior 082–097 U
qualifications remain unchanged. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 099+ and **ALL remaining safe
frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch097 fitting, address and life kanji

Batch097 adds **three complete Russian frozen N3 lessons, 合/君/命, 204 file lines**,
and three RAW-identical Japanese KanjiVG assets. Ten whole current word bodies receive
**NAV-only wrappers**: nine standalone-glyph wrappers (一生懸命→命, 具合→合, 割合→合,
合う→合, 合図→合, 君→君, 場合→合, 試合→合, 都合→合) and one whole-word label wrapper,
間に合う's existing label `合う` → `../kanji/合.md`, authorized before mutation by the
[signed whole-label navigation amendment](translation-batches/097-fitting-address-and-life-kanji-pre-mutation-whole-label-navigation-amendment-001.json). All visible prose, Japanese metadata,
quiz arrays, old links and frozen levels remain unchanged; no new guard or removed direction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole independent review](translation-batches/097-fitting-address-and-life-kanji-independent-review-001.json) (one reviewer, replacement writer after
the original author session was lost) read **47 whole teaching bodies, 24 EN/23 CURRENT RU**:
three primary pairs, 20 current context pairs and one EN-only comparison (words/命.md), including
all ten changed words; **85 whole official TEXT units** (15 KANJIDIC, one Unicode, 66 JMdict,
three visible KanjiPedia) plus one provider header; all 334 CURRENT typed rows, nine
original directions, three L/three A rulings, three outside LIMITS, the amendment, ten exact
NAV diffs, four whole guidance files and three RU rubrics — **57 complete windows**, 60
successful terminal commands, zero failures/truncations/waits, identical opening/closing
gates, zero glyph pixels, zero web pages. The original **9432-byte stdout/native-final
report**, SHA256 `ca4acd2bb193d4f20bd0bbca0a32eebc26b5fd555ff573b1940cf4a46f738f34`, is published verbatim with its final LF; no projection or second review.

Actual verdicts: **C1 CLEAN** (three new lessons within bounded official evidence),
**C2 CLEAN for bounded scope/navigation but UNVERIFIED for ordinary active-negative quiz
safety**, **C3 CLEAN** (Russian comprehension of new lessons and wrapper readability).
Findings: none confirmed. All **nine directions are S-intro** (introductory/source-core
comparison only, canonical author mapping Q) with **ordinary U** stated by the reviewer;
metadata retention is not guard approval. All three L rulings and three A clarifications
SUPPORTED within bounded scope; all ten NAV changes CLEAN as NAV-only. Outside LIMITS record
real unresolved overlap concerns, not guards: 合's meeting sense vs current 会, 君's
master/ruler senses vs current 主, 命 vs current 生 «жизнь». One optional polish suggestion
(full readings for two short phrases in kanji/合.md notes) was not applied in 097.

The [qualified source record](translation-batches/097-fitting-address-and-life-kanji-reviewed-source.json) preserves 2160 other baseline runtime RAWs/tracking
rows and all 1478 word metadata/quiz arrays. Qualified source checkpoint: **2176 runtime/
1478 words/334 kanji/334 strokes**; words 671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged;
kanji 80 N5/166 N4/**86 N3**/2 N2; **281 N3 remain**. Strict progress: **2176 reviewed-current/
two excluded reviewed blocked-media drafts/6100 pending of 8278; 6102 runtime paths absent**.
Version `d6d621873d0b1741`; checkpoint authority null/Ready false. Prior 082–096 U
qualifications remain unchanged. Protected 033 WORD空 stays excluded/runtime-absent/not media.
No device/media/default/package/release authority. Continue 098+ and **ALL remaining safe
frozen levels/families**, not finite completion.

## Previous qualified source milestone: batch096 number, direction, harmony and commerce kanji

Batch096 adds **four complete Russian frozen N3 lessons,号/向/和/商,
289 file lines**,and four RAW-identical Japanese KanjiVG assets.
Seven whole current word bodies receive seven **NAV-only standalone-glyph wrappers**:
信号→号,向かう→向,向く→向,向ける→向,向こう→向,番号→号,記号→号.
All visible prose,Japanese metadata,quiz arrays,old links and frozen levels remain
unchanged;no new guard or removed direction. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual FIRST whole review](translation-batches/096-number-direction-harmony-and-commerce-kanji-independent-review-001.json)
read **46 distinct whole teaching bodies,24 EN/22 CURRENT RU**:four primary
pairs,18 current context pairs and two EN-only comparisons,including all seven
changed words. It read **138 whole official TEXT units**:20 KANJIDIC records,
one Unicode key row,113 ordered JMdict objects and four visible KanjiPedia texts;
one whole provider header is additional. All331 CURRENT typed rows,12 original
directions,four L/four A rulings,seven exact NAV diffs,four outside LIMITS,the
complete format amendment in13 logical units,four whole guidance files and three
correct RU-root rubrics were read in **65 complete windows**. Zero glyph pixels;
331 typed rows are not331 whole lessons or1478 fresh word-guard judgments.

The original **10799-byte stdout/native-final report**,SHA256
`75d29c9267c9488cab0457025bfc3f69dc42005805cb14440bc9f88e9859c491`,
is published verbatim,including its final LF: **no projection or second review**.
There were73 native PowerShell commands/74 tool returns/69 successful terminal
commands. All68 helper invocations had distinct native shells;the closing gate
initially awaited30s,then one actual `read_powershell(delay30)` retrieved complete
exit0. Opening/closing gate payloads match. All65 reading windows completed;
zero failed readings/truncations. Four report-size assertions rejected
14165/12115/11342/11011 bytes before output;one10799-byte report was emitted.
The first rejected size is an actual literal measurement by the capture audit;
the immutable original report lists attempts2/3/4 sizes,not an invented rewrite.
Author-only preparation mechanics,the initial format failure,one capture regex
failure omitting N008's explicit meaning-only qualification,and a successful
diagnostic classification erratum remain separate from reviewer reading.

Actual verdicts are **C1 SUPPORTED within introductory/source-core teaching/
C2 SUPPORTED bounded coverage and dependencies/C3 SUPPORTED within22 whole RU
bodies**,not literal CLEAN or ordinary quiz approval. No current consequential
correctable teaching/NAV/format defect was established.
All **12 actual S-intro** dispositions support introductory/source-core
comparisons ONLY;**N008和→秋 explicitly says “for meaning”**. Canonical Q is an
explicit author schema mapping,not report rewriting.
**ALL12 ordinary active-negative/all-sense/reading/fallback safety remains U**;
metadata retention,titles and structural passes do not clear it.
All four L rulings are supported-bounded,all four A clarifications supported,
all seven NAV changes accepted AS NAV-ONLY. Four outside LIMITS are not guards.
Whole KANJIDIC和 AND秋 share nanoriあい,not standalone-word synonymy or runtime
reading approval. 商しょう includes quotient;高たか/だか includes amount:
numerical affinity is not claimed synonymy and is not resolved by titles.
向く orientation/suitability,向うむかう/むこう,和やかなごやか and sum/style
limits are retained. Modern mnemonics are not etymology;provider historical JLPT
does not replace frozen community N3;exact-form misses prove no frequency/absence.
Current kanji lacks記/数/平/禾/合/対/進;words/components do not supply them.

The [explicit format amendment](translation-batches/096-number-direction-harmony-and-commerce-kanji-post-initial-mutation-format-only-amendment-001.json)
is **POST initial runtime mutation**,not retroactive premutation/EOL/semantic review.
Initial manifest2170/version`47a864f666bbaf1e` passed;validator actually found four
schema errors from synonymous noncanonical H2 labels. Tests/budget did NOT run then.
Signed amendment70ab changes **exactly eight headings** to `Частые слова`/
`Примечания`,with every other teaching/Japanese/metadata/NAV/stroke byte unchanged.
Original9052 semantic freeze,proposals001,bound helpers,initial authoring001 and
failed checks001 remain immutable. CURRENT four RU bodies match amended002,
not original001 RAWs. No EOL correction is claimed. Fresh corrected002 checks pass;
CURRENT four new RU/seven whole changed words/331 typed rows were freshly read
in13 author returns,not reviewer credits.

The [qualified source record](translation-batches/096-number-direction-harmony-and-commerce-kanji-reviewed-source.json)
preserves2155 other baseline runtime RAWs/tracking rows and all1478 word metadata/
quiz arrays. Qualified source checkpoint: **2170 runtime/1478 words/331 kanji/
331 strokes**;words671 N5/636 N4/97 N3/19 N2/55 unlabelled unchanged;
kanji80 N5/166 N4/**83 N3**/2 N2. All166 frozen N4 included;**284 N3 remain**.
Strict progress: **2170 reviewed-current/two excluded reviewed blocked-media drafts/
6106 pending of8278;6108 runtime paths absent**,no partial.
Version `4db327de9b972839`;checkpoint authority null/Ready false.
Accepted-main counts require signed normal integration;fresh final serialized
checks/public archives/signatures/four protected refs/exact-main CI/owner issue
verification have separate receipts. Runtime2170 differs from2178 exported bodies.
Prior082/091 U,093's27 ordinary U,094呼-blow/all nine ordinary U and095声→告/
all12 ordinary U remain unchanged. Broader ordinary modern necessity-frequency/
global current-future uniqueness remains UNVERIFIED.
Protected033 WORD空 stays excluded-C2U/runtime-absent/not media;KANJI空 does not
resolve it. No device/media/default/package/release authority.
Continue097+ and **ALL remaining safe frozen levels/families**,not finite completion.

## Previous qualified source milestone: batch095 negation, announcement, voice and rejoicing kanji

Batch095 adds **four complete Russian frozen N3 lessons,否/告/喜/声,
319 file lines**,and four RAW-identical Japanese KanjiVG assets.
Three existing word bodies receive three **NAV-only standalone-glyph wrappers**:
喜び→喜,喜ぶ→喜,声→声. Visible prose,Japanese metadata,quiz arrays,
old links and frozen community levels remain unchanged;no new guard or removed direction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole review](translation-batches/095-negation-announcement-voice-and-rejoicing-kanji-independent-review-001.json)
read **31 whole teaching bodies,17 EN/14 RU**:four primary pairs,ten CURRENT
context pairs and three EN-only comparisons,including all three changed words.
It read **99 whole official TEXT units**:15 KANJIDIC records,two Unicode rows,
78 ordered JMdict objects and four visible KanjiPedia entries;one whole provider
header is additional. All327 CURRENT typed metadata rows,12 original directions,
four L rulings/four A clarifications,three exact NAV diffs,four outside LIMITS,
four whole guidance files and three correct RU rubrics were read in
**51 complete successful windows**. Zero glyph pixels;327 typed rows are not
327 whole lessons or1478 fresh word-guard judgments.

The original **10776-byte stdout/native-final report**,SHA256
`9640c96d1a064310c7e225d512f2099f57234f5176a04e0dc3ef316cfe865044`,
is published verbatim,including its final LF: **no projection or second review**.
There were58 terminal tool returns:56 successes and two reviewer delivery-only
size assertions at12197/11307 bytes,not failed readings. All54 helper invocations
had distinct successful reader shells;one successful size-only measurement and
one exact report emission are separate mechanics. Complete opening/closing gate
payloads match;no unread window,truncation or nonterminal wait.
One author-only capture-prefix audit failure remains separately preserved.
Its premature alias-root diagnosis was explicitly withdrawn by actual evidence:
the stdout-only report scripts had empty prefixes,not filesystem operations.
The corrected audit accepts that form under the unchanged strict AST audit;
no reviewer/source/report mutation or second review resulted.

Actual verdicts are **C1 SUPPORT within assigned source teaching/C2 qualified
SUPPORT for bounded source authoring,dependencies and introductory comparisons/
C3 SUPPORT within14 whole CURRENT RU bodies**. These are not literal CLEAN
verdicts or ordinary quiz approval. No necessary learner-text fix was established;
the reviewer supplied no severity for the retained C2 negative-clearance qualification.
**Eleven directions have actual SQ**,qualified introductory/source-core support
only;the explicit canonical Q mapping does not rewrite the original report.
**N012声→告 remains U**:whole KanjiPedia声②言う/述べる and
告①つげる/知らせる/語る intersect,corroborated by JMdict1380440/1380540/1285990.
A voice-only title/disclosure does not resolve it.
Ordinary active-negative safety is **U for ALL12**;metadata retention is not approval.
L001–L003 and all four A rulings/three NAV changes are supported;L004 is qualified.
Four outside LIMITS are not new guards/global pairs.
否いな/いや/ひ,告げる's signalling sense,喜ぶ/喜ばす grammar,
声色こわいろ versusせいしょく and声明せいめい versusしょうみょう remain bounded.
Modern mnemonics are not etymology;exact-form misses are not frequency/absence proofs.
Prior082姉→妹 U,091割→利 U,093's27 ordinary U and094's呼/吹 overlap/
all nine ordinary U remain unchanged. Broader ordinary suitability,modern
necessity-frequency/global current-future uniqueness remain **UNVERIFIED**.
One completed one-shot reviewer is idle,not running.

All four new Markdown LF attributes were checked **before** RAW proposal binding;
all seven actual teaching RAW payloads equal those pre-mutation proposals.
No postmutation EOL amendment was required or invented. CURRENT four new RU bodies,
three changed whole words and327 typed rows were freshly read in12 author returns;
reviewer reading borrows none of those credits. Historical originals are immutable.

The [qualified source record](translation-batches/095-negation-announcement-voice-and-rejoicing-kanji-reviewed-source.json)
preserves2151 other baseline runtime RAWs/tracking rows.
Qualified source checkpoint: **2162 runtime objects/1478 words/327 kanji/327 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;kanji80 N5/166 N4/**79 N3**/2 N2.
All166 frozen N4 kanji remain included;**288 of367 frozen N3 kanji remain**.
Strict progress: **2162 reviewed-current/two excluded reviewed blocked-media drafts/
6114 pending of8278;6116 runtime paths absent**,no partial.
Version `c2909e83de70da8b`;checkpoint authority null/Ready false.
These become accepted-main counts only after signed normal integration;fresh final
serialized checks/public archives/signatures/four protected refs/exact-main CI/
owner issue verification have separate receipts.
Protected033 WORD空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 KANJI空 does not resolve it. No device/media/default/package/release authority.
Continue096+ and **ALL remaining safe frozen levels/families**,not finite completion.

## Previous qualified source milestone: batch094 absorption, breathing and blowing kanji

Batch094 adds **three complete Russian frozen N3 lessons,吸/吹/呼,
206 file lines**,and three RAW-identical Japanese KanjiVG assets.
Three existing word bodies receive three **NAV-only standalone-glyph wrappers**:
吸う→吸,吹く→吹,呼ぶ→呼. No visible prose,Japanese metadata,quiz array,
old link or frozen community level changes;no new guard or removed direction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The [actual whole review and explicitly path-redacted public projection](translation-batches/094-absorption-breathing-and-blowing-kanji-independent-review-001.json)
cover **18 whole teaching bodies,10 EN/8 RU**:three primary pairs,five CURRENT
context pairs and two EN-only comparisons,including all three changed words.
It read **92 whole official TEXT units**:seven KANJIDIC records,one Unicode row,
81 ordered JMdict objects and three visible KanjiPedia entries;one whole provider
header is additional. All323 CURRENT typed metadata rows,nine directions,
three L rulings/three A clarifications,three exact NAV diffs,three outside LIMITS,
the whole EOL amendment,four whole guidance files and three correct RU rubrics
were read in **54 complete successful windows**. Zero glyph pixels;
323 typed rows are not323 whole lessons or1478 fresh word-guard judgments.

The original **10985-byte stdout/native-final report**,SHA256
`bdb29b4f8b1c8d1f044fa3cc542d6392c64de35124783a80271b96f617da73f6`,
is immutable privately,including its final LF. Its public projection replaces
only one absolute checkout root;separate projection bytes/hash are recorded.
It is **not the original byte payload or a second review**.
There were59 terminal tool returns:57 successes and two reviewer delivery-only
size assertions at12722/11684 bytes,not failed readings. There were56 successful
reader shells and57 helper invocations:opening gate;ranges shared one semicolon-
chained shell,so its one exit0 footer is not two individually observed exit codes.
Complete opening/closing gate payloads are byte-identical;no unread assigned
window,truncation or nonterminal wait. Seven author-only preparation/capture/
diagnostic failures remain separately preserved,not reviewer reading failures.

Actual facets are **C1 source CLEAN/C2 coverage and dependencies supported,
introductory suitability QUALIFIED ONLY/C3 Russian CLEAN**.
No necessary learner-text correction was established. The medium C2 qualification
is retained: **N006吹→呼 and N008呼→吹 remain U** because whole KanjiPedia
吹① and呼③ explicitly share息をはく,corroborated by JMdict1370760/1266460.
Calling-first titles and correct disclosure do not resolve this overlap.
The other **seven directions are introductory/source-core Q ONLY**.
Ordinary active-negative safety is **U for ALL9**;metadata retention is not approval.
L001/L002 and all three A rulings/NAV changes are supported;L003 is qualified.
呼気 does not make呼ぶ mean «выдыхать»;呼吸 is whole breathing.
Wind/instrument transitivity and吹いて,吸って/呼んで,phone-action overlap,
exact味 records and noun/prefix restrictions remain explicit.
Three outside observations are limitations,not new guards/global pairs.
Prior082姉→妹 U,091割→利 U and093's27 ordinary active-negative U remain unchanged.
Broader ordinary suitability,modern necessity-frequency/global future uniqueness
remain **UNVERIFIED**. One completed one-shot reviewer is idle,not running.

The [post-initial-mutation EOL amendment](translation-batches/094-absorption-breathing-and-blowing-kanji-post-initial-mutation-eol-domain-amendment-001.json)
preserves the original001 CRLF predictions and the real author-only RAW probe failure.
Actual three new files already used LF as Git `eol=lf` requires;three NAV working
CRLF payloads were unchanged. Only the predictive RAW domain changed in002,
**after initial patches,before candidate checks/review**,not before mutation or
as semantic re-review. Original eleven prospective returns are not fresh002 reads:
323 printed typed/three NAV payloads have exact identity;three RU proposals only
console-LF-normalized identity. Later CURRENT three RU/three changed word bodies/
323 typed rows were genuinely freshly read in eleven separate author returns.

The [qualified source record](translation-batches/094-absorption-breathing-and-blowing-kanji-reviewed-source.json)
preserves2145 other baseline runtime RAWs/tracking rows.
Qualified source checkpoint: **2154 runtime objects/1478 words/323 kanji/323 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;kanji80 N5/166 N4/**75 N3**/2 N2.
All166 frozen N4 kanji remain included;**292 of367 frozen N3 kanji remain**.
Strict progress: **2154 reviewed-current/two excluded reviewed blocked-media drafts/
6122 pending of8278;6124 runtime paths absent**,no partial.
Version `012875a68bf96891`;checkpoint authority null/Ready false.
These become accepted-main counts only after signed normal integration;fresh final
serialized checks/public archives/signatures/four protected refs/exact-main CI/
owner issue verification have separate receipts.
Protected033 WORD空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 KANJI空 does not resolve it. No device/media/default/package/release authority.
Continue095+ and **ALL remaining safe frozen levels/families**,not finite completion.

## Previous qualified source milestone: batch093 transformation, simplicity, danger, origin, participation and hand-radical kanji

Batch093 adds **nine complete Russian frozen N3 lessons,化/単/危/原/参/反/収/取/受,
557 file lines**,and nine RAW-identical Japanese KanjiVG assets.
Twelve existing word bodies receive twelve **NAV-only wrappers** around existing
standalone explanatory glyphs:危ない→危,危険→危,原因→原,参る→参,反対→反,
取り替える→取,取る→取,受ける→受,受付→受,変化→化,文化→化,簡単→単.
No compound/stem split,visible semantic amendment,new word,Japanese source metadata
correction or removed direction. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Historical originals remain immutable. A private001 bibliography attribution to
2457950（夏げ）was corrected to2451270（取り/取とり）in002 **before** the signed
semantic freeze,runtime mutation,candidate or review;no incorrect citation reached them.

The [actual whole review](translation-batches/093-transformation-simplicity-danger-origin-participation-and-hand-radical-kanji-independent-review-001.json)
read **96 whole teaching bodies,51 EN/45 RU**:nine primary pairs,36 CURRENT
context pairs and six EN-only comparisons,including all twelve changed words.
It read **260 whole official TEXT units**:32 KANJIDIC records,six Unicode rows,
213 ordered JMdict objects and nine visible KanjiPedia entries;one whole header
is additional. It also read320 CURRENT typed metadata rows,all27 retained directions,
nine L rulings/nine A clarifications,twelve exact NAV diffs,nine outside observations,
the private citation-correction summary,four whole guidance files and three correct RU rubrics.
**94 successful reading windows;100 successful commands/101 tool returns**:
97 helper commands plus two stdout-only size measurements and one report emission.
One initial **nonterminal final-gate wait** received no terminal/reading credit;
one same-shell continuation returned the complete exit0 gate.
Initial/final gate payloads are byte-identical;no reviewer command or assigned reading failed.
Actual full payloads and line unions are bound,not markers alone.
Zero glyph-pixel views;320 typed rows are not320 whole lessons or1478 fresh word guards.

The one actual **10826-byte stdout/native-final report**,SHA256
`dcdf8435a591670a19a287f4b31da9211e3f24a8497887c480edc1103be2be10`,
is published verbatim,including its final LF;**no projection or second review**.
Actual facets are **C1 CLEAN within assigned Japanese/source teaching;
C2 QUALIFIED source consistency/dependencies/citations/introductory contrasts ONLY;
C3 CLEAN within45 RU bodies**. No assigned-text fix was requested.
An author-only capture parser initially assumed a space after L/A colons;it now
accepts the original no-space payload without modifying it.
That failure and a separate author receipt-probe syntax failure are preserved,
not counted as reviewer failures or hidden by a fresh report.

All27 original metadata directions remain,**not27 approved negatives**.
**23 are introductory/source-core Q;N005単→早,N008危→急,N022取→聞,N025受→学
remain U**. Ordinary active-negative safety is **U for ALL27**,not merely these four.
単simple/早いeasy-simple and危danger/急crisis-danger actually overlap;
取るaccept/adopt versus聞くpleas/arguments needs Japanese object/context judgment;
受ける's actual lesson-taking context overlaps学ぶ,without inventing a lesson gloss in1329590.
L001/L004–L007 and A001/A003/A005–A007 are supported;the other four L/four A
rulings are qualified. All twelve NAV changes are supported.
化/花 share bothカandケ,not a reading-mode guard;原 retains geography;
反るそる/かえる stay distinct;反/収 returning and収/別 settling intersections persist;
収/納 spelling restrictions and exam participation/success remain explicit.
Nine outside observations are limitations,not new guards/global pairs.
Prior091割→利 active-negative U and082姉→妹 unrestricted U remain unchanged.
No reverse/transitive inference,frequency or etymology claim.
Broader ordinary suitability,necessity-frequency and global current/future uniqueness
remain **UNVERIFIED**. One completed one-shot reviewer is idle,not running.

The [qualified source record](translation-batches/093-transformation-simplicity-danger-origin-participation-and-hand-radical-kanji-reviewed-source.json)
preserves2118 other baseline runtime RAWs/tracking rows.
Qualified source checkpoint: **2148 runtime objects/1478 words/320 kanji/320 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;kanji80 N5/166 N4/**72 N3**/2 N2.
All166 frozen N4 kanji remain included;**295 of367 frozen N3 kanji remain**.
Strict progress: **2148 reviewed-current/two excluded reviewed blocked-media drafts/
6128 pending of8278;6130 runtime paths absent**,no partial.
Version `5f24829dba357164`;checkpoint authority null/Ready false.
These become accepted-main counts only after signed normal integration;fresh final
serialized checks/public archives/signatures/four protected refs/exact-main CI/
owner issue verification have separate receipts.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue094+ and **ALL remaining safe frozen levels/families**,not finite completion.

## Previous qualified source milestone: batch092 addition, help, effort, labor, duties, victory and diligence

Batch092 adds **seven complete Russian frozen N3 lessons,加/助/努/労/務/勝/勤,
468 file lines**,and seven RAW-identical Japanese KanjiVG assets.
Four existing word bodies receive four **NAV-only wrappers** around existing
standalone explanatory glyphs:事務所→務,公務員→務,勝つ→勝,勤める→勤.
No compound/stem split,visible semantic amendment,new word,source metadata
correction or removed direction. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original intake,premutation freeze,proposals,candidate and report remain immutable.

The [actual whole review](translation-batches/092-addition-help-effort-labor-duties-victory-and-diligence-kanji-independent-review-001.json)
read **49 whole teaching bodies,27 EN/22 RU**:seven primary pairs,15 CURRENT
context pairs and five EN-only comparisons,including all four changed words.
It read **148 whole official TEXT units**:17 KANJIDIC records,one Unicode row,
123 ordered JMdict objects and seven visible KanjiPedia entries;one whole header
is additional. It also read311 CURRENT typed metadata rows,all21 original/active
directions,seven L rulings/seven A clarifications,four exact NAV diffs,seven
outside observations,four whole guidance files and three correct CURRENT RU rubrics.
**66 successful reading commands/tool returns/windows;75 terminal commands,
72 successful plus three failed report-size assertions before payload emission**.
No failed assigned reading,truncated or nonterminal return. Actual whole payloads
and guidance/rubric line unions are bound,not markers alone.
Zero glyph-pixel views;TEXT/ALT is not pixel or full-HTML inspection.
311 metadata rows are not311 whole lessons or1478 fresh word-guard judgments.

The one actual **10732-byte stdout/native-final report**,SHA256
`537de58ae7aea58e157638724332546ce38b836a509b53f124bfb4597d5b62e6`,
is published verbatim,including its final LF;**no projection or second review**.
Actual facets are **C1 CLEAN within assigned Japanese/source teaching;
C2 bounded SOURCE coverage COMPLETE,introductory contrasts QUALIFIED,evidence
consistency NEEDS FIX F1;C3 CLEAN within22 RU bodies**. The original C2 verdict
is preserved,not relabelled blanket CLEAN. F1 is an evidence-ID attribution error,
not a learner-text defect. The [separate ID erratum](translation-batches/092-addition-help-effort-labor-duties-victory-and-diligence-kanji-source-evidence-id-erratum-001.json)
adopts the actual reviewer's explicit five-object mapping and requested remedy:
**1539080勝れる/優れる;1603910勝る/優る;1171010右 including better-of-two;
1609560勝ち victory;2593990勝 victory/scenic spot/win counter,not右**.
The author actually reread all five whole bound objects;no historical freeze,
helper or report rewriting,new independent verdict,learner edit or new guard.

All **21 directions are Q only for introductory-core comparisons**,not unrestricted
ordinary/all-sense/reading-mode/fallback negatives. Six L/A rulings are supported;
**L002/A002 are qualified**:助すけ «helper» is one attested sense,not exhaustive;
whole1344370 also has colloquial «woman». No透ける transfer. All four NAV patches
are supported. 労 care/nursing overlaps help;動く operation/work constrains勤→動;
右 also means above-mentioned/better-of-two;服 retains medicine/submission/archaic
mourning and野や private/non-governmental. Seven outside observations are
limitations,not new guards. Prior091割→利's active-negative U and082姉→妹's
unrestricted U remain unchanged. No reverse/transitive inference,frequency or
etymology claim. Ordinary/all-sense/fallback suitability,modern necessity-frequency
and global current/future uniqueness remain **UNVERIFIED**. One completed/idle
reviewer,not running;no additional review is invented for the exact ID correction.

The [qualified source record](translation-batches/092-addition-help-effort-labor-duties-victory-and-diligence-kanji-reviewed-source.json)
preserves2112 other baseline runtime RAWs/tracking rows.
Qualified source checkpoint: **2130 runtime objects/1478 words/311 kanji/311 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;kanji80 N5/166 N4/**63 N3**/2 N2.
All166 frozen N4 kanji remain included;**304 of367 frozen N3 kanji remain**.
Strict progress: **2130 reviewed-current/two excluded reviewed blocked-media drafts/
6146 pending of8278;6148 runtime paths absent**,no partial.
Version `8577ac7d183281ca`;checkpoint authority null/Ready false.
Accepted-main membership requires signed normal integration;fresh final serialized
checks/public archives/signatures/four protected refs/exact-main CI/owner issue
verification remain separately evidenced. Protected033 **word**空 stays excluded/
runtime-absent/C2 UNVERIFIED,not media;accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue093+ and **ALL remaining safe frozen levels/families**,not finite completion.

## Previous qualified source milestone: batch091 rows, beginnings, judgment, benefit, arrival, regulation, carving and division

Batch091 adds **eight complete Russian frozen N3 lessons,列/初/判/利/到/制/刻/割,
584 file lines**,and eight RAW-identical Japanese KanjiVG assets.
Eight existing word bodies receive eight **NAV-only wrappers**,each around one
existing standalone explanatory glyph. No compound/stem split,visible semantic
amendment,new word,source metadata correction or removed direction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original intake,premutation freeze,proposals,candidate and report remain immutable.

The [actual whole review](translation-batches/091-rows-beginnings-judgment-benefit-arrival-regulation-carving-and-division-kanji-independent-review-001.json)
read **55 whole teaching bodies,31 EN/24 RU**:eight primary pairs,16 CURRENT
context pairs and seven EN-only comparisons,including all eight changed words.
It read **224 whole official TEXT units**:15 KANJIDIC records,one Unicode row,
200 ordered JMdict objects and eight visible KanjiPedia entries;one whole header
is additional. It also read304 CURRENT typed metadata rows,all24 original/active
directions,eight L rulings/eight A clarifications,eight exact NAV diffs,eight
outside observations,four whole guidance files and three correct CURRENT RU rubrics.
**73 successful reading commands/tool returns/windows;80 successful terminal
commands;zero failed,truncated or nonterminal returns** bind actual whole payloads
and line unions. Zero glyph-pixel views;TEXT/ALT is not pixel or full-HTML inspection.
304 metadata rows are not304 whole lessons or1478 fresh word-guard judgments.

The one actual **10976-byte stdout/native-final report**,SHA256
`ed2d2e11d5032c906131b34057baecaa6bd8e27e6a45bea21d574b78be70c000`,
is published verbatim,including its final LF;**no projection or second review**.
Actual facets are **C1 CLEAN within assigned Japanese/source teaching;
C2 QUALIFIED bounded SOURCE dependencies/suitability;C3 CLEAN within24 RU bodies**.
Seven L/A rulings are supported and **L003/A003 supported with qualification**:
paper/book-size判 allows bothはん/ばん,notバン-only. The learner body already says
this correctly;the author adopts the qualification without rewriting the freeze.
All eight NAV-only changes are supported. One completed/idle reviewer,not running.

**23 directions have introductory semantic Q only;091-N023割→利 has actual U
for active-negative suitability**,not a24th Q. Whole JMdict1606800 sense3 gives
割り profit/gain,overlapping利 advantage/benefit/profit/interest in1549460.
This is genuine lexical counterevidence,not merely an association.
The historical source array stays unchanged;**its retention is not guard approval
or activation authority**. Descriptive division/share-versus-benefit teaching can
be accepted as source text without clearing that negative answer.
091-N007判→半 sharesハン and is **not a reading-mode guard**.
到/着/達,初/始,刻/時/秋とき and利く/聞く tasting also constrain wider claims.
Eight outside observations are limitations,not new guards. No reverse/transitive
inference;old dictionary JLPT tags are not source community levels;modern-shape
mnemonics are not etymology;exact-form misses are not absence/frequency proof.
Ordinary/all-sense/fallback suitability,modern necessity-frequency/global future
uniqueness remain **UNVERIFIED**. Prior082姉→妹's original unrestricted U persists.

The [qualified source record](translation-batches/091-rows-beginnings-judgment-benefit-arrival-regulation-carving-and-division-kanji-reviewed-source.json)
preserves2092 other baseline runtime RAWs/tracking rows.
Qualified source checkpoint: **2116 runtime objects/1478 words/304 kanji/304 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;kanji80 N5/166 N4/**56 N3**/2 N2.
All166 frozen N4 kanji remain included;**311 of367 frozen N3 kanji remain**.
Strict progress: **2116 reviewed-current/two excluded reviewed blocked-media drafts/
6160 pending of8278;6162 runtime paths absent**,no partial.
Version `945eac2c7dfe171f`;checkpoint authority null/Ready false.
Accepted-main membership requires signed normal integration;fresh final serialized
checks/public archives/signatures/four protected refs/exact-main CI/owner issue
verification remain separately evidenced. Protected033 **word**空 stays excluded/
runtime-absent/C2 UNVERIFIED,not media;accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue092+ and **ALL remaining safe frozen levels/families**,not finite completion.

## Previous qualified source milestone: batch090 riding, loss, light, wholeness, sharing, tools, cold and places

Batch090 adds **eight complete Russian frozen N3 lessons,乗/亡/光/全/共/具/冷/処,
639 file lines**,and eight RAW-identical Japanese KanjiVG assets.
Fifteen existing word bodies receive15 **NAV-only wrappers**:14 existing standalone
glyphs plus **one whole existing explanatory ます-stem乗り** in乗り換える.
The exact whole-label adaptation was frozen before mutation;it splits no compound
or Markdown and changes no visible prose,metadata,example or old link.
No new word,word semantic amendment,source metadata correction or removed direction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original intake,premutation freeze,proposals,candidate and actual report stay immutable.

The [actual whole review](translation-batches/090-riding-loss-light-wholeness-sharing-tools-cold-and-places-kanji-independent-review-001.json)
read **89 whole teaching bodies,46 EN/43 RU**:eight primary pairs,35 CURRENT
context pairs and three EN-only comparisons,including all15 changed current words.
It read **315 whole official TEXT units**:27 KANJIDIC records,seven Unicode rows,
273 ordered JMdict objects and eight visible KanjiPedia entries;one whole header
is additional. It also read296 CURRENT typed metadata rows,24 original/active
directions,eight L rulings/eight A clarifications,15 exact NAV diffs,eight outside
observations,four whole guidance files and three correct CURRENT RU rubrics.
**91 successful reading commands/tool returns/windows** bind entire payloads and
guidance/rubric line unions;zero failed,truncated or nonterminal reading returns.
Of96 terminal commands,94 succeeded;two report-size assertions at11853/11255 bytes
failed **before printing report payloads**,not reading failures,findings or reviews.
Zero glyph-pixel views;TEXT/ALT reading is not whole HTML or pixel inspection.
296 metadata rows are not296 whole lessons or1478 fresh word-guard judgments.

The one actual **10451-byte stdout/native-final report**,SHA256
`201208577346bfe00548d15673c35f80a88badd174463e596bc6df2f449619d1`,
remains private/immutable. Its **10346-byte path-only public projection**,SHA256
`5d4719570f8ce01493fc60c6f40ad8790699b288a73ca9f27c66db2f786213f6`,
replaces machine roots only;original/projection bytes and hashes are distinct.
Projection is not a second review,new semantic verdict or approval.
Actual facets are **C1 CLEAN within assigned source-content scope;
C2 QUALIFIED bounded dependencies/NAV and introductory-core dispositions;
C3 CLEAN within actually read Russian teaching scope**.
No significant scoped source/Russian fix was requested;all eight L/A rulings and
clarifications are accepted boundedly,not ordinary-use certification.
One completed/idle reviewer,not running;no focused or second whole review.

All24 Qs mean **qualified forward introductory-core contrasts ONLY**.
090-N013共→具 and090-N017具→共 were independently considered as separate direct
questions;actual具する accompaniment/possession prevents blanket exclusion.
具/備える alternate spellings,全/共 collectivity and処/外 place/removal also
forbid universal semantic disjointness. No reciprocal/transitive inference.
All readings remain,including処 **ショ**,notショウ;処る is attested by KanjiPedia
despite a JMdict exact-form miss. Exact-form misses prove no absence or frequency.
Modern-shape mnemonics are not etymology;old dictionary JLPT tags are not source
community levels. Eight outside observations are limitations,not new guards.
Ordinary/all-sense/reading-mode/fallback suitability,modern necessity-frequency
and global current/future uniqueness remain **UNVERIFIED**.
Existing word guards and082姉→妹's original unrestricted U are not upgraded.

The [qualified source record](translation-batches/090-riding-loss-light-wholeness-sharing-tools-cold-and-places-kanji-reviewed-source.json)
preserves2069 other baseline runtime RAWs/tracking rows.
Qualified source checkpoint: **2100 runtime objects/1478 words/296 kanji/296 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;kanji80 N5/166 N4/**48 N3**/2 N2.
All166 frozen N4 kanji remain included;**319 of367 frozen N3 kanji remain**.
Strict progress: **2100 reviewed-current/two excluded reviewed blocked-media drafts/
6176 pending of8278;6178 runtime paths absent**,no partial.
Version `eff88314bda21342`;checkpoint authority null/Ready false.
Accepted-main membership requires signed normal integration;fresh final serialized
checks/public archives/signatures/four protected refs/exact-main CI/owner issue
verification remain separately evidenced. Protected033 **word**空 stays excluded/
runtime-absent/C2 UNVERIFIED,not media;accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue091+ and **ALL remaining safe frozen levels/families**,not finite completion.

## Previous qualified source milestone: batch089 surplus, convenience, connection, trust, preparation, work and kindness

Batch089 adds **seven complete Russian frozen N3 lessons,余/便/係/信/備/働/優,
513 file lines**,and seven RAW-identical Japanese KanjiVG assets.
Nine existing word bodies receive nine **NAV-only wrappers**;no new word,
word semantic amendment,source metadata correction or removed direction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original intake,premutation freeze,proposals,candidate and report remain immutable.

The [actual whole review](translation-batches/089-surplus-convenience-connection-trust-preparation-work-and-kindness-kanji-independent-review-001.json)
read **67 whole teaching bodies,36 EN/31 RU**:seven primary pairs,24 CURRENT
context pairs and five EN-only comparisons,including all nine changed words.
It read **238 whole official TEXT units**:24 KANJIDIC records,one Unicode row,
206 ordered JMdict objects and seven visible KanjiPedia entries;one whole header
is additional. It also read288 CURRENT whole typed metadata rows,21 original/
active directions,seven L rulings/seven A clarifications,nine exact NAV diffs,
seven outside observations,four whole guidance files and three correct CURRENT RU rubrics.
**77 successful reading commands/tool returns/windows** bind entire payloads and
guidance/rubric line unions;zero failed/truncated reads. All80 terminal commands
succeeded;82 actual tool returns include two nonterminal final-gate returns that
were not credited as terminal success;one terminal follow-up completed that gate.
Zero glyph-pixel views;TEXT/ALT reading is not whole HTML or pixel inspection.
288 metadata rows are not288 whole lessons or1478 fresh word-guard judgments.

The one actual **10716-byte stdout/native-final report**,SHA256
`4054652327a33d17e27f3d6ab9f1636f591ad76aedfd7caf062f6c9e4c417d44`,
has one successful delivery,no path projection or rewrite.
Actual facets are **C1 PASS within assigned Japanese/content/source scope;
C2 QUALIFIED bounded dependencies/NAV and introductory-core dispositions;
C3 PASS within assigned Russian teaching bodies**.
No significant scoped source/Russian defect requires correction;all seven L/A
source rulings/clarifications are accepted boundedly,not ordinary-use certification.
The reviewer is completed/idle,not actually running;no focused or second whole review.

All21 Qs mean **qualified forward introductory-core contrasts ONLY**.
In particular,089-N016働→動 retains actual function/work/movement overlap and
稼働/稼動;its introductory labor-versus-movement contrast is expressly **not
all-sense/fallback-safe foil approval**. 係る work/result,便 stool/body and
信 financial credit/borrowing also forbid universal disjointness.
Seven outside observations are not new guards or an exhaustive pool matrix.
Ordinary/all-sense/reading-mode/fallback suitability,modern necessity-frequency
and global current/future uniqueness remain **UNVERIFIED**.
Existing word guards and082姉→妹's original unrestricted U are not upgraded.
系/憂 are metadata/visible-shape components,not invented frozen EN lesson providers.

The [qualified source record](translation-batches/089-surplus-convenience-connection-trust-preparation-work-and-kindness-kanji-reviewed-source.json)
preserves2061 other baseline runtime RAWs/tracking rows.
Qualified source checkpoint: **2084 runtime objects/1478 words/288 kanji/288 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;kanji80 N5/166 N4/**40 N3**/2 N2.
All166 frozen N4 kanji remain included;**327 of367 frozen N3 kanji remain**.
Strict progress: **2084 reviewed-current/two excluded reviewed blocked-media drafts/
6192 pending of8278;6194 runtime paths absent**,no partial.
Version `744d39ac52c0452b`;checkpoint authority null/Ready false.
Accepted-main membership requires signed normal integration;fresh final serialized
checks/public archives/signatures/four protected refs/exact-main CI/owner issue
verification remain separately evidenced. Protected033 **word**空 stays excluded/
runtime-absent/C2 UNVERIFIED,not media;accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue090+ and **ALL remaining safe frozen levels/families**,not finite completion.

## Previous qualified source milestone: batch088 examples, falling, weather, values, chance and sides

Batch088 adds **seven complete Russian frozen N3 lessons,倒/候/値/偶/偉/側/例,
497 corrected file lines**,and seven RAW-identical Japanese KanjiVG assets.
Seven existing word bodies receive seven **NAV-only wrappers**;no new word,
word semantic amendment,source-directed metadata correction or removed direction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original intake,semantic freeze,493-line proposal,candidate and reviews stay immutable.

The [actual whole review](translation-batches/088-examples-falling-weather-values-chance-and-sides-kanji-independent-review-001.json)
read **56 whole teaching bodies**:seven primary EN/RU pairs,16 current context
pairs and10 EN-only comparisons,**33 EN/23 RU**,including all seven changed words.
It read **251 whole official TEXT units**:22 KANJIDIC records,one Unicode row,
221 ordered JMdict objects and seven visible KanjiPedia entries;one whole header
is additional. It also read281 whole CURRENT typed metadata rows,21 historical/
active directions,seven L rulings/seven A additions,seven NAV diffs/wrappers,
seven outside observations,four whole guidance files and three correct CURRENT RU rubrics.
**64 successful reader tool returns/72 windows** bind whole actual payloads and line
unions;two truncated bundles receive no credit and were reread completely.
281 metadata rows are not281 whole lessons or1478 fresh word-guard judgments.
Zero glyph-pixel views;source-TEXT/ALT reading is not image or full-HTML inspection.

One whole review produced two successful stdout deliveries. The earlier10582-byte
report had three bell path escapes and a warning;the reviewer corrected those paths
and added its acknowledgement. The actual corrected **10681-byte stdout/native final**,
SHA256 `a494aa0cada1a9a3a4028ea0ae9c50224d90ffa72a02e013b2e20c52652f4285`,
and the earlier bytes remain separately preserved,not failed/pre-emission or two whole reviews.
Original facets remain **C1 NEEDS FIX F1;C2 assigned dependency/NAV PASS with21
qualified forward introductory-core Qs only;C3 QUALIFIED for the practical gap**.
F1 identified missing formal/literary register guidance for standalone あたい
price/worth senses,not its mathematical/computing sense.

The signed premutation resolution freezes the exact four-Russian-line correction.
The [actual focused review](translation-batches/088-examples-falling-weather-values-chance-and-sides-kanji-independent-review-focused-002.json),
**8755 bytes**,SHA256 `9f35cb7311cb038f061dd0e2e4abbe46e84b02663b927ae535529c18809feed0`,
resolves **F1 only**:five whole teaching bodies,2 EN/3 RU,and eight official TEXT
units,six JMdict/one KANJIDIC/one KanjiPedia;25 credited read windows,zero pixels.
One oversized guidance return was not credited;both windows were reread fully.
It resolves the bounded C1/C3 usage gap and passes amendment continuity;
L003/A003's F1-dependent source qualification is resolved **without rewriting
the original verdicts or inventing a second whole review/whole-batch CLEAN**.
Both reviewers are completed one-shot,not actually running.

All21 Qs retain **original qualified forward introductory-core scope/support ONLY**.
Five 値 endpoint hashes changed;the focused check establishes no qualifier weakening
or semantic expansion,not five/21 fresh semantic judgments or281 fresh row readings.
倒→側 inclination,候→使 archaic service,偶→値 numeric-domain overlap and
側→内/右/左 generic-versus-qualified side forbid universal separation.
Seven outside observations are not new guards. Ordinary/all-sense/reading-mode/
fallback quiz safety,modern necessity-frequency and global future uniqueness remain
**UNVERIFIED**. Prior word guards and082姉→妹's unrestricted U are not upgraded.

The [qualified source record](translation-batches/088-examples-falling-weather-values-chance-and-sides-kanji-reviewed-source.json)
preserves2049 other baseline runtime RAWs/tracking rows.
Qualified source checkpoint: **2070 runtime objects/1478 words/281 kanji/281 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;kanji80 N5/166 N4/**33 N3**/2 N2.
All166 frozen N4 kanji remain included;**334 of367 frozen N3 kanji remain**.
Strict progress: **2070 reviewed-current/two excluded reviewed blocked-media drafts/
6206 pending of8278;6208 runtime paths absent**,no partial.
Version `c3357a2913cdfd26`;checkpoint authority null/Ready false.
Accepted-main membership requires signed normal integration;fresh final serialized
checks/public archives/signatures/four protected refs/exact-main CI/owner issue
verification remain separately evidenced. Protected033 **word**空 stays excluded/
runtime-absent/C2 UNVERIFIED,not media;accepted077 **kanji**空 does not resolve it.
No app/device/phone/IME/media/default/package/release authority.
Continue089+ and **ALL remaining safe frozen levels/families**,not finite completion.

## Previous qualified source milestone: batch087 otherness, attachment, duties and position kanji

Batch087 adds **seven complete Russian frozen N3 lessons,他/付/件/任/伝/似/位,
473 file lines**,and seven RAW-identical Japanese KanjiVG assets.
Ten existing word bodies receive10 **navigation-only wrappers**;
no new word,word semantic amendment or source-directed metadata correction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original signed intake,premutation freeze,proposals and candidate remain immutable.

The [actual whole review](translation-batches/087-otherness-attachment-duties-and-position-kanji-independent-review-001.json)
read **56 whole teaching bodies**:seven primary EN/RU pairs,19 current context
EN/RU pairs and four whole EN-only comparisons,30 EN/26 RU.
All10 changed word bodies are included,not extra bodies.
It read **185 whole official source-TEXT units**:16 KANJIDIC records,
one Unicode keyrow,161 ordered JMdict objects and seven visible KanjiPedia entries;
one whole provider header is additional.
Zero dictionary-glyph pixel views;historical glyphs stay UNINSPECTED.
It read274 current whole typed metadata rows,21 historical/active directions,
seven separate lesson rulings/seven clarifications,10 exact NAV diffs/10 wrappers,
seven outside observations,four whole guidance files and three correct CURRENT RU rubrics.
**70 actual successful reader commands/windows** bind whole returned payloads
and complete line unions,not markers alone.
274 metadata rows are not274 whole lessons or1478 freshly judged word guards.

One actual whole review delivered one successful **10792-byte stdout/native final**,
SHA256 `af4deffc7c9b21193220e3e5d6e78db073cdb45821bedacab35817bc5fab0dd2`.
Original public bytes are unchanged;no path projection is needed.
Two earlier size assertions failed **before any report emission**;
not earlier delivered reports or semantic reviews,and no reading credit.
The final gate's initial nonterminal output is not success;
its actual successful `read_powershell` completion is separately bound.
76 tool returns represent75 terminal commands/73 successful,two size failures.
The one-shot reviewer is completed,not actually running.
The original report exposes the **scope-binding SHA256 only**,not the separate
serialized pool/evidence hashes. Author extraction separately binds those exact
artifacts,verifies both actual snapshot gates and compares all274 returned rows;
it does not invent hash statements in the original report.

Actual verdicts are **C1 CLEAN within assigned SOURCE teaching;
C2 assigned dependency/NAV/source-invariant coverage CLEAN,quiz conclusions QUALIFIED;
C3 CLEAN within26 whole Russian bodies**,not native certification.
All seven lesson rulings and all seven dictionary clarifications are accepted boundedly.
No significant current source-text fix or M001 is established.
All21 original directions remain active,with **Q forward introductory-core contrast ONLY**.
件くだん's human-headed bovine yokai sense1255930/3 limits件→牛;
任's actual work/task senses prevent blanket任→件 separation.
付's giving/handing/entrusting and appearance sense remain;
位's actual location/位する1640530 prevent social-only or all-sense位→立/住 claims.
Broader ordinary/all-sense/reading-mode/fallback safety,modern necessity-frequency
and global current/future uniqueness remain **UNVERIFIED**,not blanket C2 CLEAN.
Seven outside observations are not new guards.
Prior word-guard scope/identity and082姉→妹's unrestricted U remain unchanged.
手伝う is not newly split:its wrapper surrounds standalone explanatory伝 elsewhere.

The [qualified source record](translation-batches/087-otherness-attachment-duties-and-position-kanji-reviewed-source.json)
preserves2032 other baseline RAWs/tracking rows.
Qualified source checkpoint: **2056 runtime objects/1478 words/274 kanji/274 strokes**.
Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**166 N4**/26 N3/2 N2.
All166 frozen N4 kanji remain included;**341 of367 frozen N3 kanji remain**.
Strict progress: **2056 reviewed-current,two excluded reviewed blocked-media
drafts,6220 pending of8278;6222 runtime paths absent**,no partial.
Version `b4655aee17d7316d`;checkpoint authority null/Ready false.
Counts become accepted-main only after signed normal integration;fresh final
serialized checks,actual public archives/signatures/four protected refs/exact-main CI
and owner issue verification have separate receipts.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue088+ and **ALL remaining safe frozen levels/families**;
this is not completion of the finite8278-object objective.

## Previous qualified source milestone: batch086 giving, preparation and interaction kanji

Batch086 adds **six complete Russian frozen N3 lessons,与/予/争/両/互/交,
369 file lines**,and six RAW-identical Japanese KanjiVG assets.
Eleven existing word bodies receive11 **navigation-only wrappers**;
no new word or existing-word semantic amendment is introduced.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original signed intake,premutation freeze,proposals and candidate remain immutable.

The [actual whole review](translation-batches/086-giving-preparation-and-interaction-kanji-independent-review-001.json)
read **65 whole teaching bodies**:six primary EN/RU pairs,24 current context
EN/RU pairs and five whole EN-only comparisons,35 EN/30 RU.
All11 changed word bodies are included,not extra bodies.
The whole201-line English kaeru article is a comparison,not a RU runtime provider.
It read **181 whole official source-TEXT units**:19 KANJIDIC records,
four Unicode keyrows,152 ordered JMdict objects and six visible KanjiPedia entries;
one whole provider header is additional.
Zero dictionary-glyph pixel views are claimed;historical glyphs stay UNINSPECTED.
It read267 current whole typed metadata rows,18 historical directions/17 active,
one explicit M001,six separate lesson rulings/six clarifications,11 exact NAV
diffs/11 wrappers,six outside observations,four whole current guidance files
and three correct CURRENT RU-root rubrics.
**72 actual successful reader commands/windows** are bound by whole returned
payloads/complete line unions,not markers alone.
267 metadata rows are not267 whole lessons or1478 freshly judged word guards.

One actual whole review delivered one successful **9945-byte stdout/native final**,
SHA256 `1446cb87e29862de94d1205d09860df7deb259f5451f29720f48d6e6ff6147fa`.
Original public payload is unchanged;no path projection is needed.
Two earlier report-size assertions failed **before any report emission**;
not earlier delivered reports or semantic reviews,and no reading credit.
The one-shot reviewer is completed,not actually running.

Actual verdicts are **C1 CLEAN within assigned SOURCE authoring;
C2 assigned SOURCE dependency/NAV coverage CLEAN,quiz conclusions QUALIFIED;
C3 CLEAN within30 whole Russian bodies**,not native certification.
All six lesson rulings and all six dictionary clarifications are supported boundedly.
No significant current source-text fix was requested.
The reviewer independently supports **086-M001 only**:
`予.distractors [子,手,与]`→`[子,手]`,withdrawing historical N006予→与.
Actual whole KanjiPedia予(B)②「あたえる。あずかる」「類 与」
and与①「あたえる」show why offered与«давать; предоставлять»
cannot be universally wrong across attested予 senses.
Retained N003与→予 is independently Q against actual offered«заранее»;
no reciprocal/replacement/transitive deletion or fallback exclusion follows.
All18 historical directions remain in immutable evidence;
**17 active directions have qualified introductory-core Q judgments only**.
Broader ordinary/all-sense/reading-mode/fallback safety,modern necessity-frequency
and global current/future uniqueness remain **UNVERIFIED**,not blanket C2 CLEAN.
Six outside observations are not new guards.
Prior word-guard scope/identity and082姉→妹's unrestricted U remain unchanged.

The [qualified source record](translation-batches/086-giving-preparation-and-interaction-kanji-reviewed-source.json)
preserves2019 other baseline RAWs/tracking rows.
Qualified source checkpoint: **2042 runtime objects/1478 words/
267 kanji/267 strokes**. Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**166 N4**/19 N3/2 N2.
All166 frozen N4 kanji remain included;**348 of367 frozen N3 kanji remain**.
Strict progress: **2042 reviewed-current,two excluded reviewed blocked-media
drafts,6234 pending of8278;6236 runtime paths absent**,no partial.
Version `7a11fb6dc2ec2efd`;checkpoint authority null/Ready false.
Counts become accepted-main only after signed normal integration;fresh final
serialized checks,actual public archives/signatures/four protected refs/exact-main CI
and owner issue verification have separate receipts.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue087+ and **ALL remaining safe frozen levels/families**;
this is not completion of the finite8278-object objective.

## Previous qualified source milestone: batch085 final frozen N4 kanji

Batch085 adds **six complete Russian N4 lessons,別/勉/真/答/親/題,
385 file lines**,and six RAW-identical Japanese KanjiVG assets.
Fifteen existing word bodies receive15 **navigation-only wrappers**;
no new word,word semantic amendment or source-directed metadata correction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original signed intake,premutation freeze,proposals and candidate remain immutable.

The [actual whole review](translation-batches/085-separation-effort-truth-answers-parents-and-topics-kanji-independent-review-001.json)
read **90 whole teaching bodies**:six primary and39 current context EN/RU
pairs,45 RU/45 EN. The15 changed word bodies are included,not extra bodies.
It read **232 whole official source-TEXT units**:35 KANJIDIC,six Unicode,
182 ordered JMdict,six visible KanjiPedia and three supplemental KanjiPedia
lexical texts. The original229-TEXT receipt and separate three-text supplement
remain distinct;one whole provider header is additional.
Zero dictionary-glyph pixel views are claimed;historical glyphs stay UNINSPECTED.
It read261 current whole typed metadata rows,18 original directions,six lesson
rulings,five clarifications,15 exact NAV diffs/15 wrappers,six outside observations,
four guidance files and three correct CURRENT RU-root rubrics.
**88 actual successful reader commands/windows** are bound by whole returned
payloads/complete guidance line unions,not markers alone.
261 typed rows are not261 whole lessons or1478 freshly judged word guards.

One actual whole review delivered one successful **10858-byte stdout/native final**,
SHA256 `721a847c031ae711b725749417ff5d73191dab50b801d48d734af1131f0f5dc3`.
The original payload is public unchanged;no path projection is needed.
Two earlier report-size assertions failed **before any report emission**;
they are neither earlier delivered reports nor semantic reviews and credit no reading.
The reviewer is completed one-shot,not actually running.

Actual verdicts are **C1 PASS within assigned source content,
C2 QUALIFIED SOURCE PASS,C3 PASS within45 whole Russian bodies**.
No substantive source fix or required optional polish was established.
All18 original directions retain independent **Q introductory-core contrast ONLY**;
all18 broader ordinary-runtime/fallback/all-sense/modern necessity-frequency/global
current-future uniqueness judgments remain **UNVERIFIED**.
This is not blanket ordinary-quiz C2 CLEAN.
Six lesson rulings and five dictionary clarifications are accepted boundedly.
In particular,勉→力 offers«сила; мощь» and題→質 offers«качество; сущность»;
rare readings/other senses do not automatically prove these offered answers or reverse safety.
真まこと's supplemental「―の道」supportsまことの;親しむ's supplemental
「土に親しむ」supports things/contact,not a fabricated exact本に親しむ quote.
Six outside-edge observations are not new guards.
Prior word-guard scope/identity and082姉→妹's unrestricted U remain unchanged.

The [qualified source record](translation-batches/085-separation-effort-truth-answers-parents-and-topics-kanji-reviewed-source.json)
preserves2003 other baseline RAWs/tracking rows.
Qualified source checkpoint: **2030 runtime objects/1478 words/
261 kanji/261 strokes**. Words671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**166 N4**/13 N3/2 N2.
**All166 frozen N4 kanji are included under qualified SOURCE scope.**
Strict progress: **2030 reviewed-current,two excluded reviewed blocked-media
drafts,6246 pending of8278;6248 runtime paths absent**,no partial.
Version `6101e469724d76b4`;checkpoint authority null/Ready false.
Counts become accepted-main only after signed normal integration;fresh final
serialized checks,actual public archives/signatures/four protected refs/exact-main CI
and owner issue verification have separate receipts.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue086+ and **ALL remaining safe frozen levels/families**;
N4 kanji closure does not complete the finite8278-object target.

## Previous qualified source milestone: batch084 world, use, water and places kanji

Batch084 adds **eight complete Russian N4 lessons,世/以/使/場/早/注/洋/漢,
509 file lines**,and eight RAW-identical Japanese KanjiVG assets.
Twenty-three existing word bodies receive23 **navigation-only wrappers**;
no new word,word semantic amendment or source-directed metadata correction.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The original intake,premutation adjudication/freeze,proposals and report persist.

The [actual whole review](translation-batches/084-world-use-water-and-places-kanji-independent-review-001.json)
read **108 whole teaching bodies**:eight primary EN/RU pairs and46 current
context EN/RU pairs,54 RU/54 EN. The23 changed word bodies are included,
not23 additional bodies.
Its **223 whole official source-TEXT units** are34 KANJIDIC records,
five Unicode rows,176 whole ordered JMdict objects and eight whole visible
KanjiPedia texts;one whole provider header is separate.
**Zero dictionary-glyph pixel views**:historical inline glyphs stay UNINSPECTED.
The review read255 current typed kanji rows,all24 original directions,
eight lesson rulings,23 exact NAV diffs/23 wrappers,eight outside observations,
seven clarifications,four guidance files and three correct CURRENT RU-root rubrics.
Entire successful returned payloads and complete guidance line unions are bound;
255 metadata rows are not255 whole lessons or1478 fresh word judgments.

There was **one actual whole review and one successful report delivery**:
**10967-byte stdout/native final**,SHA256
`30743e9d0b85a227764908faa63346e285fee322726bd49d83330f2856da5f92`,
including its terminal LF,records **89 actual successful reader commands/windows**.
Two earlier size assertions failed before emitting any report;they are not
earlier delivered reports or semantic reviews and credit no reading.
Original bytes remain private and immutable.
The public **10894-byte path-only projection**,SHA256
`6afb1d6b81432196ba5a22226d30e957811aefe688c4167196beb0f412cd5518`,
replaces only machine roots;its bytes/hash are not the original return.

All eight mandatory roots and24 original directed arrays persist.
**All24 actual independent Q dispositions are qualified introductory-core
contrasts only**,not unrestricted negatives.
使→事 was independently judged in its actual forward question:
the offered current事 title is «дело; событие»,selected kunこと;
additional provider readingsつかう/つかえる and historical史/吏/事 forms
do not alone establish a forward defect or all-sense safety.
The seven dictionary clarifications are supported:以もって/numerical limits;
independent使える;場チョウ/both工場 readings/provider dates;
早サッ/all six kun/spelling preferences;注つぐ/qualified注す spellings;
洋 and漢 selected empty kun arrays are not global absence.
No automatic reverse correction,new guard clique or transitive exclusion follows.

**C1: qualified CLEAN within new source teaching/preservation,not fresh
certification of every inherited historical claim.
C2: assigned source coverage/dependencies/NAV qualified CLEAN and24 bounded
core contrasts,not whole ordinary-quiz C2 CLEAN.
C3: qualified CLEAN within54 whole Russian bodies,not native certification.**
Broader ordinary/all-sense/fallback suitability,modern necessity/frequency
and global current/future uniqueness remain UNVERIFIED.
No consequential correction was established within assigned facets.
Eight overlap observations are not new guards;速/所 are not current typed
kanji providers. Prior word-guard scope/identity and082姉→妹's unrestricted U persist.

The [qualified source record](translation-batches/084-world-use-water-and-places-kanji-reviewed-source.json)
preserves1979 other baseline RAWs/tracking rows.
Qualified source checkpoint: **2018 runtime objects/1478 words/
255 kanji/255 strokes**. Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**160 N4**/13 N3/2 N2,leaving **six frozen N4 kanji:別/勉/真/答/親/題**.
Strict progress: **2018 reviewed-current,two excluded reviewed blocked-media
drafts,6258 pending of8278;6260 runtime paths absent**,no partial.
Version `c8dce7e6734759dd`;checkpoint authority null/Ready false.
Counts become accepted-main only after signed normal integration;
fresh final serialized checks,actual public archives/signatures/four protected
refs/exact-main CI remain separate publication evidence,not pixel/native/media approval.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue085+ and ALL remaining safe frozen levels/families;
neither this batch nor N4 closure completes the finite target.

## Previous qualified source milestone: batch083 teaching, existence, clothing and meals kanji

Batch083 adds **seven complete Russian N4 lessons,教/有/着/考/者/飯/館,
411 file lines**,and seven RAW-identical Japanese KanjiVG assets.
Twenty-two existing word bodies receive22 **navigation-only wrappers**;
no new word or existing-word semantic amendment is introduced.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The original intake,premutation adjudication/freeze,proposals and reports persist.

The [actual whole review](translation-batches/083-teaching-existence-clothing-and-meals-kanji-independent-review-001.json)
read **96 whole teaching bodies**:seven primary EN/RU pairs,39 current
context EN/RU pairs and four whole EN-only comparisons,including the entire
207-line occupation-endings article.
Its **188 whole official source-TEXT units** are28 KANJIDIC records,
five Unicode rows,135 original plus13 additional whole ordered JMdict
objects and seven whole visible KanjiPedia texts;one whole provider header
is separate. **Zero dictionary-glyph pixel views**:historical inline glyphs,
including教's phonetic glyph,remain UNINSPECTED.
The review read247 current typed kanji rows,all21 historical directions,
seven lesson rulings,22 exact NAV diffs/22 wrappers,eight outside observations,
one explicit source correction,three clarifications,four guidance files and
three correct CURRENT RU-root rubrics.
Entire successful returned payloads and complete line unions are bound;
247 metadata rows are not247 whole lessons or1478 fresh word judgments.

There was **one actual whole review,not two**. Its earlier10946-byte stdout,
SHA256 `93e84c504c1ef8f90d1679ce12ef9157dcb1589c056f6d80c00b91914c3d73b5`,
incorrectly counted85 reader commands.
The actual corrected **10803-byte stdout/native final**,SHA256
`604b54d8dfc247f2a7700c26c91cefe2370e49b2c5f592a92a25eaefe902892c`,
records the actual **82 successful reader commands/windows** and compact
wording. Both original deliveries remain immutable;this is not another
semantic review or additional reading.

The signed [premutation source freeze](translation-batches/083-teaching-existence-clothing-and-meals-kanji-source-adjudication-and-semantic-freeze-001.json)
proposes only083-S001:
`考.distractors [者,教,古]`→`[教,古]`.
Current KanjiPedia 考 meaning③死んだ父/先考 and whole JMdict2414430/1387630
support conservative one-way removal of original N010考→者,not merely an
elder-origin story. The actual reviewer supports that correction.
All seven mandatory roots and21 historical directions remain;
**20 active directions have qualified introductory-core Q judgments;
one rejected historical R is already removed**.
No replacement,reverse or transitive edge follows;者→考 was judged separately.
着→目's actual Go-count/ordinal extensions prevent all-senses separation.
The reviewer also supports retainedジャク/spelling-preference/lexical-causative
clarifications,the nonuniversal者/物 contrast and actual poetical館たて coverage.

**C1: CLEAN within new source-text teaching/preservation;reused context
reading does not freshly certify every inherited historical claim.
C2: assigned source coverage/NAV wrappers CLEAN and20 bounded core contrasts,
not whole ordinary-quiz C2 CLEAN. C3: CLEAN within assigned Russian text.**
Broader ordinary/all-sense quiz suitability,fallback safety,modern necessity/
frequency and global current/future uniqueness remain UNVERIFIED.
No significant current source-text defect was found.
Eight overlap observations are not new exclusions;prior word guards retain
their original scope/identity. Prior082姉→妹 remains its unrestricted U.

The [qualified source record](translation-batches/083-teaching-existence-clothing-and-meals-kanji-reviewed-source.json)
preserves1966 other baseline RAWs/tracking rows.
Qualified source checkpoint: **2002 runtime objects/1478 words/
247 kanji/247 strokes**. Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**152 N4**/13 N3/2 N2,leaving **14 actual frozen N4 kanji**.
Strict progress: **2002 reviewed-current,two excluded reviewed blocked-media
drafts,6274 pending of8278;6276 runtime paths absent**,no partial.
Version `944b6247fc33d54c`;checkpoint authority null/Ready false.
Counts become accepted-main only after signed normal integration;
fresh final serialized checks,actual public archives/signatures/four protected
refs/exact-main CI remain separate publication evidence,not pixel/native/media approval.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue084+ and ALL remaining safe frozen levels/families;
neither this batch nor N4 closure completes the finite target.

## Previous qualified source milestone: batch082 taste, family and beginnings kanji

Batch082 adds **four complete Russian lessons,味/妹/姉/始,287 file lines,
all actual frozen N4**,and four RAW-identical Japanese KanjiVG assets.
Thirteen existing word bodies receive14 **navigation-only wrappers**;
no new word or existing-word semantic amendment is introduced.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original intake,premutation adjudication/freeze,proposals and reports persist.

The [actual whole review](translation-batches/082-taste-family-and-beginnings-kanji-independent-review-001.json)
read **53 whole teaching bodies**:four primary EN/RU pairs,22 current
context EN/RU pairs and one whole EN-only comparison.
Its **76 whole official source-TEXT units** are14 KANJIDIC records,two Unicode
rows,56 whole ordered JMdict objects and four whole visible KanjiPedia texts;
one whole provider header is separate. **Zero dictionary-glyph pixel views**:
the missing始 historical inline glyph remains UNINSPECTED.
The review read240 current typed kanji rows,all12 individual directions,
four adjudications,13 exact NAV diffs/14 wrappers,five outside observations,
four guidance files and three correct CURRENT RU-root rubrics.
Entire successful returned payloads are bound,not markers alone.
240 metadata rows are not240 whole lessons or1478 fresh word judgments.
The actual **10827-byte stdout/final report**,SHA256
`5b9f6aaf8c8cb93e33ec15ff03784fe9765a534e0b0424c225a56b8e82513ffd`,
has C1/C3 CLEAN within its assigned scope and C2 F082-01 NEEDS FIX.
Its private original bytes remain immutable;the tracked report's explicitly
labelled **path-only public projection has a different hash/length domain**.

**F082-01:** whole JMdict2752050 attests archaic妹（いも）as one's sister
without a younger restriction. A bare-glyph question is not constrained to
modernいもうと. The signed
[source amendment](translation-batches/082-taste-family-and-beginnings-kanji-single-source-correction-freeze-001.json)
removes only invalid active082-N004妹→姉:
`妹.distractors [姉,味,始]`→`[味,始]`.
All four closure members,all12 historical directions,lesson prose,
readings,levels,Japanese examples and caveats remain.
No replacement,reverse,transitive or clique edge is invented.
**Original judgments remain10 Q +one rejected R +one U,not11 Q.**
N007姉→妹 remains U for unrestricted clearance,with its modern core contrast
supported;the dictionary evidence concerns the other glyph and does not
prove a reciprocal defect. Never reverse N004 automatically.

The [actual focused review](translation-batches/082-taste-family-and-beginnings-kanji-independent-review-002.json),
**10132 bytes**,SHA256
`2ae374b7c73e3dd3e8d9bf5d9debc1024b4d6d87f71ba60bdd27ecaf3a317bd4`,
resolves only the exact F082-01 correction.
It read five whole teaching bodies,seven whole official TEXT units,
one header,two current/two prior typed rows and the exact amendment/diff.
Its240-row identity audit is not240 fresh semantic judgments or a second
whole53-body review. Ten retained Q judgments carry only their original
qualified introductory-core scope;N007's U is not converted into Q.
**C1/C3: no remaining confirmed defect within the combined assigned scopes.
C2: exact bounded correction CLEAN;broader C2 UNVERIFIED,not whole C2 CLEAN.**
Ordinary modern quiz suitability,necessity/frequency,fallback safety and
global future uniqueness remain UNVERIFIED. Removing a curated foil does
not prove fallback can never offer it. Five outside observations are not
new exclusions;prior word guards retain earlier scope/identity only.
姉's attestedはは remains in metadata without invented ordinary usage,
register,frequency or a mother-reading example. 始's historicalなりたち
is not automatically a modern older-sister meaning.

The [qualified source record](translation-batches/082-taste-family-and-beginnings-kanji-reviewed-source.json)
preserves1967 other baseline RAWs/tracking rows.
Qualified source checkpoint: **1988 runtime objects/1478 words/
240 kanji/240 strokes**. Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**145 N4**/13 N3/2 N2,leaving **21 actual frozen N4 kanji**.
Strict progress: **1988 reviewed-current,two excluded reviewed blocked-media
drafts,6288 pending of8278;6290 runtime paths absent**,no partial.
Version `730ea51721ee7090`;checkpoint authority null/Ready false.
Counts become accepted-main only after signed normal integration;
fresh final serialized checks,actual public archives/signatures/four protected
refs/exact-main CI remain separate publication evidence.
Stroke/root-license identity is not pixel/native/media approval.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,not media;
accepted077 **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue083+ and ALL remaining safe frozen levels/families;
neither this batch nor N4 closure completes the finite target.

## Previous qualified source milestone: batch081 light, nature and daily-life kanji

Batch081 adds **17 complete Russian kanji lessons /1083 file lines,
all actual frozen N4**,and17 RAW-identical Japanese KanjiVG assets.
Existing53 word bodies receive54 **navigation-only wrappers**;
no existing-word semantic amendment or new word is introduced.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original signed intake,adjudication/freeze,proposals,candidate and reports persist.

The [actual whole review](translation-batches/081-light-nature-and-daily-life-kanji-independent-review-001.json)
read **215 whole teaching bodies**:17 primary EN/RU pairs,88 current
context EN/RU pairs and five whole EN-only comparisons.
Its **306 official source-TEXT units** are48 whole KANJIDIC records,
including append-only由,ten Unicode rows,231 whole ordered JMdict objects
and17 whole visible KanjiPedia entry-TEXT projections.
One whole provider header and one actual flower-phonetic PNG view are separate.
Only that PNG was visually inspected;other glyph pixels remain UNINSPECTED.
The review read236 current typed kanji rows,all51 original directed proposals,
18 adjudications,53 exact navigation diffs/54 wrappers,11 outside observations,
four guidance files and three correct CURRENT RU-root rubrics.
Entire successful returned payloads are bound,not markers alone.
236 metadata rows are not236 whole lessons or1478 fresh word judgments.
The actual **10889-byte stdout/final report**,SHA256
`93209116b8637757799463a0bbf560e9bfb0f4ee27dab31b2f1c8852f0f5fa08`,
requested two bounded changes;its original verdict is not rewritten.

**F081-01,C2:** attested flower meaning makes花 unsafe as an unequivocally
wrong answer to bare英. The explicit signed
[source amendment](translation-batches/081-light-nature-and-daily-life-kanji-source-correction-and-clarity-freeze-001.json)
changes only英.distractors `[茶,花,映]` to `[茶,映]`.
All17 closure and all51 historical directions remain;invalid N038 is rejected,
not silently erased from history. No replacement/reverse/transitive edge is invented.
**F081-02,C3:** 曜 now names月曜日 explicitly in the three-reading warning,
preserving the examples and correct nativeひ→び explanation.
The [actual focused review](translation-batches/081-light-nature-and-daily-life-kanji-independent-review-002.json),
**8712 bytes**,SHA256
`2fba3db032c7e4153563a8c9e77483e05976bed07088cab44cbb74bf7358c730`,
resolves these exact changes after reading eight whole teaching bodies,
nine whole official TEXT units,one header and two current/two prior typed rows.
Its236-row provenance/identity audit is not236 fresh semantic judgments
or another whole215-body review.

The first report accidentally labels the prospective pool hash as candidate.
The focused review independently confirms actual original candidate pool
`6029833da5f7ea19629fca7341ef3c1c246d332b22faf775cfad2922edb5fc56`,
corrected pool `2d2c0113ef36f86f33e61e4fd2bbe361360297c864a7137fa52b8c9ccfa227fb`,
and the original236 complete successful current-payload returns.
Original report bytes and limitations remain immutable.
**C1/C3: no remaining confirmed defect within the combined assigned scopes.
C2: exact bounded correction resolved;NOT whole C2 CLEAN.**
Fifty active directions carry only their original qualified introductory-core
contrast judgments,not50 fresh judgments or universal disjointness.
**Broader ordinary quiz/fallback suitability,modern necessity/frequency and
future global uniqueness remain UNVERIFIED.**
Eleven outside observations are limitations,not new exclusions.
Existing word guards retain earlier identity/support/limits,not1478 fresh approvals.

The [qualified source record](translation-batches/081-light-nature-and-daily-life-kanji-reviewed-source.json)
preserves1893 other baseline runtime RAWs/tracking rows.
Qualified source checkpoint: **1980 runtime objects/1478 words/
236 kanji/236 strokes**. Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**141 N4**/13 N3/2 N2,leaving **25 actual frozen N4 kanji**.
Strict progress: **1980 reviewed-current,two excluded reviewed blocked-media
drafts,6296 pending of8278;6298 runtime paths absent**,no partial.
Version `b1d5197e8fc7fe07`;checkpoint authority null/Ready false.
Counts become accepted-main only after signed normal integration;
fresh final serialized checks,actual public archives/signatures/four protected
refs/exact-main CI remain separate publication evidence.
Stroke/root-license identity is not pixel/native/media approval.
Protected033 **word**空 remains excluded/runtime-absent/C2 UNVERIFIED,
not media;accepted077 **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue082+ and ALL remaining safe frozen levels/families;
neither this batch nor N4 closure completes the finite target.

## Previous qualified source milestone: batch080 movement, routes and transitions kanji

Batch080 adds **17 complete Russian kanji lessons /1089 file lines:
16 actual frozen N4 plus unchanged source-N3達**,and17 RAW-identical
Japanese KanjiVG assets. Existing51 word bodies receive51
**navigation-only wrappers**,with no semantic amendments.
Fifty wrappers use existing standalone glyphs;売り場 wraps the existing
Russian meaning `«[продавать](../kanji/売.md)»` without splitting the compound.
Japanese text,readings,examples,metadata,quiz arrays,visible prose and
old links remain unchanged. Frozen EN remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Signed intake,premutation adjudication/freeze and original report are immutable.

The [actual whole review](translation-batches/080-movement-routes-and-transitions-kanji-independent-review-001.json)
read **199 complete teaching bodies**:17 primary EN/RU pairs,81 current
context EN/RU pairs and three whole EN-only comparisons.
Official evidence is **266 whole source-TEXT units**:46 KANJIDIC records,
nine Unicode radical rows,193 ordered whole JMdict objects,17 whole visible
KanjiPedia entry/alt-label projections and the entire selected
平凡社「普及版 字通」発 section,including source credit.
That section is visible lines[72,103)of146,not the whole Kotobank page,
raw HTML or pixels. The review also read219 current typed kanji rows,
all51 individual directed proposals,15 adjudications,51 exact navigation
patches,eight outside-edge observations,four guidance files and three
correct CURRENT RU-root rubrics. Entire successful payloads and complete
oversized line unions are bound,not markers alone.
219 metadata rows are not219 whole lessons or1478 fresh word judgments.
The **10722-byte detailed report is actual successful reviewer stdout**,
SHA256 `44fb95605bea67fa0b34220542595857adf807b1f4aed41e90c0752e4f8e892f`;
native/task final is a different52-byte generic summary.
All three actual unchanged-snapshot gates and four noncredited in-memory
report-length attempts are preserved;no reading gaps or second review are invented.

**C1/C3: no consequential defect established within assigned source-backed scope.
C2: qualified dependencies and individual lexical-core contrasts only,
NOT whole C2 CLEAN.** All51 directions have individual qualified dispositions,
not universal semantic disjointness. Eight outside-edge observations include
the actual運/福 title overlap «удача»,construction,cessation,ascertaining,
emission and passage domains;they are not new exclusions or global pair judgments.
**Broader ordinary quiz/fallback suitability,modern necessity/frequency and
future global uniqueness remain UNVERIFIED.** Character/rare-reading attestation
does not establish ordinary productive spelling or frequency.
The selected字通 section does not establish dictionary-only status or universal
modern replacement. Existing word guards retain prior identity/support/limits,
not1478 fresh semantic approvals. No learner correction or semantic repair is claimed.

The [qualified source record](translation-batches/080-movement-routes-and-transitions-kanji-reviewed-source.json)
preserves1861 other baseline runtime RAWs/tracking rows.
Qualified source checkpoint: **1946 runtime objects/1478 words/
219 kanji/219 strokes**. Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**124 N4**/13 N3/2 N2,leaving **42 actual frozen N4 kanji**.
Strict progress: **1946 reviewed-current,two excluded reviewed blocked-media
drafts,6330 pending of8278;6332 runtime paths absent**,no partial.
Version `abf49588ec0b0583`;checkpoint authority null/Ready false.
These become accepted-main counts only after signed normal integration;
fresh final serialized checks,actual public archives/signatures/four protected
refs/exact-main CI are separate publication evidence.
Stroke/root-license identity is not pixel/native/media approval.
Protected033 **word**空 remains excluded/runtime-absent/C2 UNVERIFIED,
not media;accepted077 **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue081+ and ALL remaining safe frozen levels/families;
neither this batch nor N4 word closure completes the finite target.

## Previous qualified source milestone: batch079 people, work and feelings kanji

Batch079 adds **23 complete Russian kanji lessons /1480 file lines:
22 actual frozen N4 plus unchanged source-N3供**,and23 RAW-identical
Japanese KanjiVG assets. Existing55 word bodies receive56 navigation wrappers:
**53 navigation-only and two explicit semantic amendments,子供 and旅行**.
The signed premutation amendment withdraws unsupported stronger spelling-policy/
preference/frequency claims and theこども家庭庁 narrative illustration from子供;
旅行 withdraws unsupported long/lonely/poetic/literary rankings consistently
with旅. These claims are not disproved. Original lexical metadata,readings,
grammatical Japanese example sentences and existing links persist;
not every Japanese narrative fragment is unchanged.
Frozen EN remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Original intake,premutation adjudication/freeze and actual review remain immutable.

The [actual whole review](translation-batches/079-people-work-and-feelings-kanji-independent-review-001.json)
read **226 complete teaching bodies**:23 primary EN/RU pairs,85 current
context EN/RU pairs,eight EN-only comparisons and two whole historical RU
word bodies,子供/旅行. Official evidence is **351 whole units**:
52 KANJIDIC records,nine Unicode rows,267 whole ordered JMdict entries and23
whole visible KanjiPedia entry/actual-alt-label projections,not whole HTML
or pixel inspection. It read202 current typed kanji rows,all69 individual
directed proposals,14 adjudications,55 exact patches,four guidance files and
three correct RU-root rubrics. Entire successful returned payloads and
complete oversized line unions are bound,not markers alone.
202 metadata rows are not202 whole lessons or1478 fresh word judgments.
The **10984-byte detailed report is actual successful reviewer stdout**,
SHA256 `23b72d223836aa6e4ea029cf925374201c694ec2b0b8e286047f169e7d3a47b3`;
native/task final is a different52-byte generic summary.
No native/stdout identity or second whole review is invented.

**C1/C3: no significant issue established within assigned source-backed scope.
C2: assigned dependencies,amendments and qualified core contrasts established,
NOT whole C2 CLEAN.** All69 original directions retain only stated lexical-core
scope,not universal disjointness. N005仕→土 retains service versus soil;
the author's erroneous «visible土component» wording is explicitly not adopted:
both complete EN/RU lessons already identify士 correctly.
The [append-only disposition](translation-batches/079-people-work-and-feelings-kanji-review-qualification-dispositions-001.json)
corrects that historical rationale without learner-byte changes.
借/貸 opposite roles,色/白 category/subtype,旅/行/道 travel and貸/質 pawn-domain
connections remain qualified. Outside69 flags for主/長,質す/問う,質/本/元もと,
方/人/手/道,心/気/思/意,族/組 and品/物/質 are not new runtime exclusions.
**Broader ordinary quiz/fallback suitability,modern necessity/frequency and
global future uniqueness remain UNVERIFIED.** Rare/historical attestations
do not establish ordinary productive practice;old guards retain only prior
identity/support/limitations,not1478 fresh semantic judgments.

The [qualified source record](translation-batches/079-people-work-and-feelings-kanji-reviewed-source.json)
preserves1811 other baseline runtime RAWs/tracking rows and distinguishes
53 navigation-only from two semantic updates. Qualified source checkpoint:
**1912 runtime objects/1478 words/202 kanji/202 strokes**.
Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**108 N4**/12 N3/2 N2,leaving **58 actual frozen N4 kanji**.
Strict progress: **1912 reviewed-current,two excluded reviewed blocked-media
drafts,6364 pending of8278;6366 runtime paths absent**,no partial.
Version `ae145971f3403a2b`;checkpoint authority null/Ready false.
These become accepted-main counts only after signed normal integration;
fresh final serialized checks,actual public archives/signatures/four
protected refs/exact-main CI are separate publication evidence.
Stroke/root-license identity is not pixel/native/media approval.
Protected033 **word**空 remains excluded/runtime-absent/C2 UNVERIFIED,
not media;accepted077 **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue080+ and ALL remaining safe frozen levels/families;
neither this batch nor N4 word closure completes the finite target.

## Previous qualified source milestone: batch078 home, places and everyday things kanji

Batch078 adds **16 complete Russian kanji lessons /778 file lines,all actual
frozen N4**,plus **16 RAW-identical Japanese KanjiVG assets**.
Existing54 complete word bodies receive55 navigation-only wrappers.
Their Japanese,readings,examples,metadata,quiz arrays and original word links
remain unchanged. In牛肉,the original `[肉](肉.md)` stays intact and the
adjacent existing Russian meaning becomes `«[мясо](../kanji/肉.md)»`;
an earlier private malformed proposal was caught before learner mutation.
The frozen EN target remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The original intake and signed premutation adjudication/freeze remain immutable.

The [actual whole review](translation-batches/078-home-places-and-everyday-things-kanji-independent-review-001.json)
read **221 complete teaching bodies**:16 primary EN/RU pairs,91 current
context EN/RU pairs and seven EN-only comparisons. Official evidence is
**331 whole source units plus two exact JapanPost heading sections**,
not333 whole webpages:53 whole KANJIDIC records,13 Unicode key rows,
234 whole ordered JMdict entries,16 primary KanjiPedia projections and15
supplementary semantic projections. Neither postal listing was whole-read.
It also read **179 current typed kanji metadata rows,48 original directed
contrasts,12 adjudications,54 exact navigation diffs,four complete guidance
files and three complete correct RU-root rubrics**. Entire successful
returned payloads and complete oversized line unions are bound;rows are
not whole lessons or1478 fresh word-pool judgments.
The **10843-byte detailed report is actual successful reviewer stdout**,
SHA256 `cdbb41d50df13341845070321cda3ccc9a36c2aa8662cb3b390a0d9cd5bad29d`.
The actual native/task final is a different52-byte generic summary;
no stdout/native identity or second review is invented.

**C1/C3: no consequential defect found within assigned source-backed scope.
C2: qualified core-contrast/dependency pass,NOT whole C2 CLEAN.**
All48 original directions retain only qualified lexical-core scope.
N025死→切 covers death versus cutting,not all ending senses;
N028/N029物→本/車 distinguish category names,not universally wrong answers:
books and vehicles can be objects. The other45 retain their stated core
contrasts,not universal disjointness. No D/Q reclassification,new exclusion
fields or reverse/transitive directions are invented.
**Ordinary fallback quiz suitability,modern necessity/frequency and global
future uniqueness remain UNVERIFIED**,including元/本,家/内,台/私,
画/図/計,generic物/specific objects,and ending-related死/切/終 overlaps.
Rare/historical character attestations do not establish ordinary productive
practice. Frozen花の京 remains retained without fresh phrase-specific
attestation. Existing word guards carry only prior identity/support/limits.

The [qualified source record](translation-batches/078-home-places-and-everyday-things-kanji-reviewed-source.json)
preserves1780 other baseline runtime RAWs/tracking rows and records the54
navigation-only updates separately. Qualified source checkpoint:
**1866 runtime objects/1478 words/179 kanji/179 strokes**.
Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**86 N4**/11 N3/2 N2,leaving **80 actual frozen N4 kanji**.
Strict progress: **1866 reviewed-current,two excluded reviewed blocked-media
drafts,6410 pending of8278;6412 runtime paths absent**,no partial.
Version `b29f4d5e03b8582f`;checkpoint authority null/Ready false.
These become accepted-main counts only after normal signed integration;
fresh final serialized checks,actual public archives/signatures/four
protected refs/exact-main CI remain separate publication evidence.
Stroke byte identity and root licenses are not pixel/native/media approval.
Protected033 **word**空 remains excluded/runtime-absent/C2 UNVERIFIED,
not media;accepted077 **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue079+ and ALL remaining safe frozen levels/families;
neither this batch nor N4 word closure completes the finite target.

## Previous qualified source milestone: batch077 study, writing and inquiry kanji

Batch077 adds **22 complete Russian kanji lessons /1279 file lines:
21 actual N4 and the unchanged source-N2 dependency短**,plus **22 RAW-identical
frozen Japanese KanjiVG assets**. Existing53 word bodies receive only56
navigation wrappers;their Japanese,examples,metadata and quiz arrays persist.
The frozen EN target remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The original intake,premutation adjudication/freeze and append-only
four-body Japanese-fragment restoration remain immutable.

The [actual whole review](translation-batches/077-study-writing-and-inquiry-kanji-independent-review-001.json)
read **250 whole teaching bodies**:22 primary EN/RU pairs,99 current context
EN/RU pairs and eight EN-only comparisons;**295 whole official source units**:
64 genuine RAW KANJIDIC records,17 Unicode key rows,185 whole ordered JMdict
objects,22 KanjiPedia main-entry/five lexical projections and two actual
whole Kotobank simplified returns. It also read **163 current typed kanji
metadata rows,66 individual explicit source directions,15 adjudications,
53 exact navigation diffs and three complete correct RU-root rubrics**.
The150 actual public tool returns are preserved;only entire successful
payloads receive reading credit. Rows/projections are not whole lessons/pixels.
Its **9717-byte detailed report is actual successful reviewer stdout**.
The actual native/task final is a different52-byte generic summary;
**stdout/native byte identity is not claimed or reconstructed**.
Two failed report-size print attempts receive no evidence credit.

**C1/C3: no confirmed consequential Japanese/content or Russian-comprehension
defect within assigned scope. C2: qualified dependency/explicit-direction
pass only,not blanket CLEAN.** All66 directions receive `RETAIN_CORE`;
eight have additional narrowed qualifications and58 retain only their
current-core contrasts. These are not universal semantic exclusions,
independent D/Q labels,new kanji exclusion fields or reverse/transitive edges.
**Ordinary fallback quiz safety,modern necessity/frequency and global future
uniqueness remain UNVERIFIED.** Non-explicit空/天,図/計,試/験,言/話/語
and文/字 overlaps are not cleared by differing titles.
図え and験あかし are adequate **limited character-reading references only**;
modern standalone lexical examples remain UNVERIFIED,not invented or
certified as productive training. Existing word guards carry only their
prior support/identity/limitations,not1478 fresh word-pool judgments.

The [qualified source record](translation-batches/077-study-writing-and-inquiry-kanji-reviewed-source.json)
preserves1737 unchanged baseline runtime RAWs/tracking rows and documents
the53 navigation-only updates separately. Stroke byte identity,embedded
provenance and root licenses are not new rendered/native animation approval.
Qualified source checkpoint: **1834 runtime objects /1478 words /
163 kanji /163 strokes**. Words remain671 N5/636 N4/97 N3/19 N2/55 unlabelled;
kanji80 N5/**70 N4**/11 N3/2 N2,so **96 actual frozen N4 kanji remain**.
Strict progress: **1834 reviewed-current,two excluded reviewed blocked-media
drafts,6442 pending of8278;6444 runtime paths absent**,no partial.
Version `757e4bc2daf819c8`;checkpoint authority null/Ready false.
These become accepted-main counts only after normal signed integration;
fresh final serialized checks,actual public archives/signatures/four
protected refs and exact-main CI are separate publication evidence.
Protected033 **word**空 stays excluded/runtime-absent/C2 UNVERIFIED,
not media;new **kanji**空 does not resolve its caption blocker.
No app/device/phone/IME/media/default/package/release authority.
Continue078+ and ALL remaining safe frozen levels/families;
neither this batch nor N4 word closure completes the finite target.

## Previous qualified source milestone: batch076 remaining N4 states and formal nouns

Batch076 adds **20 complete Russian lessons /1031 file lines,all actual N4**,
against unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
Japanese IDs,readings,examples,classification and the original皆–皆さん
guard remain intact;available original navigation is retained,while only
unavailable optional wrappers are unwrapped.
The [actual whole review](translation-batches/076-remaining-n4-states-and-formal-nouns-independent-review-001.json)
read **366 whole teaching bodies**:20 primary EN/RU pairs,140 contextual
EN/RU pairs,45 EN-only comparisons and one complete1708-line EN article.
It also read **403 whole official ordered projections,1478 fresh CURRENT
candidate caption/reading/type/tags/actual-level/quiz rows and three whole
correct RU-root rubrics**. No external pages were fetched/read.
The **10356-byte actual report** has identical successful stdout/native
payloads;167 actual public tool events and entire returned payloads are
bound separately. Pool rows are not whole lessons or observed quiz runs.

**C1/C3: no consequential Japanese/content or Russian-comprehension defect
established in the20 new lessons within assigned evidence.**
**C2:70 individually qualified S judgments**,including the original source
guard and69 additional direct protections. The author's5D/65Q proposals
are not independent D/Q classifications. **Q004皆–全然 adopts only the
reviewer's narrower complete-extent scope in negative-evaluation contexts,
not “not at all” or positive “very”;the stronger author affirmative-only
selection claim is withdrawn**,not the runtime guard.

The [append-only resolution](translation-batches/076-remaining-n4-states-and-formal-nouns-review-resolution-amendment-001.json)
preserves C2-1:Q061眠る–寝る wrongly cited1529330(眠い).
The correct1360010(寝る) whole object/provider was already actually read
and independently supported in the original review. Only the bound
reference is corrected by append;the valid guard,all learner bodies and
the signed original freeze/report remain unchanged.
This is **not another whole/focused review or70 fresh judgments**.
All70 carry only their actual original qualified scope/current identity.
**Broader ordinary modern quiz suitability,necessity/frequency and global
future uniqueness remain UNVERIFIED for every pair;not blanket C2 CLEAN.**
Alternate kana identities,reading restrictions,register,animacy,participant
roles and secondary-sense limits remain explicit;no transitive pair closure.

The [qualified source record](translation-batches/076-remaining-n4-states-and-formal-nouns-reviewed-source.json)
preserves all1770 baseline runtime RAWs/tracking rows/history.
Qualified source checkpoint: **1790 runtime objects /1478 words**,
671 N5/**636 N4**/97 N3/19 N2/55 unlabelled.
**All636 actual frozen N4 words now have complete reviewed source;
this is not completion of the full target or ordinary RU activation.**
Strict progress: **1790 reviewed-current,two excluded reviewed blocked-media
drafts,6486 pending of8278;6488 runtime paths absent**,no partial.
Version `051fad4e7c9dcf2b`;checkpoint authority null/Ready false.
These become accepted-main counts only after normal signed integration;
fresh final serialized checks,actual public archives/signatures/four
protected refs and exact-main CI are separate publication evidence.
Protected033空 remains the only pending N5 word,excluded/C2 UNVERIFIED,
not media. No assets/native/device/phone/IME/media/default/package/release
authority. Continue077+ and ALL remaining safe frozen levels/families;
the entire finite objective is not complete.

## Previous qualified source milestone: batch075 public life, commerce and services

Batch075 adds **20 complete Russian lessons /1164 file lines,all actual N4**,
without reclassification,against unchanged frozen EN
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/075-public-life-commerce-and-services-independent-review-001.json)
read **271 whole teaching bodies**:20 primary EN/RU pairs,81 contextual
EN/RU pairs and69 EN-only comparisons;**299 whole official ordered
projections,1458 fresh current caption/reading/type/tags/level/quiz rows
and three whole correct RU-root rubrics**. No articles or external pages
were read. Its **10933-byte stdout/native identity** remains immutable.
Rows are not whole lessons. **C1 passed within assigned teaching scope;
C2 was NOT CLEAN;C3 required a Russian agreement correction.**

A signed pre-mutation amendment preserves those findings. The
[actual focused review](translation-batches/075-public-life-commerce-and-services-independent-review-002.json)
read **11 whole teaching bodies,five whole official objects,five specific
corrected pool rows and three whole correct RU-root rubrics**,the original
report,exact two-file diff and bounded amendment.
Its **7808-byte stdout/native identity** resolves:

- F1/new Q038 **失敗–落す**,from the new owner only,as qualified conservative
  lexical protection for school/course failure or contest loss. Canonical
  runtime provider is落す/おとす,not invented落とす. Transitive participant
  and causal roles remain distinct;no unrestricted failure,physical-dropping,
  general-exam or modern-necessity proof follows.
- F2/Q030 **失敗–違う**,by withdrawal of an unsupported author proposal,
  not a source edge or proof of direct equivalence.
- 輸入 **«нужен сказуемый»→«нужно сказуемое»**,a Russian neuter-agreement
  repair,not a Japanese import-direction correction.
- **消しゴム–ゴム**,by qualifying no CURRENT pair solely by the absentゴム
  provider. Standalone eraser abbreviation is attested;material/item
  difference is not a universal negative. No absent provider is approved.

The **37 current direct protections** comprise **36 original individual S
judgments carrying only original qualified scope/current identity,plus
one newly supported Q038**. Original author3D/34K labels are **not independent
D/K classifications**. The focus is not36 fresh judgments,a second whole
review or1458 fresh focused rows. The author actually reread all1458
corrected rows and both affected whole RU lessons;the other18 new lessons
carry original whole-reading/current-identity evidence.
**Broader ordinary modern quiz suitability,necessity/frequency and global
future uniqueness remain UNVERIFIED for every current pair,including
author-labelled D and Q038;not blanket C2 CLEAN/PASS.**
C1/C3 have no new blocking issue within the actual corrective scope;
original findings and their resolution history are preserved.

The [qualified source record](translation-batches/075-public-life-commerce-and-services-reviewed-source.json)
preserves all1750 accepted baseline runtime RAWs/tracking rows/history.
Qualified source checkpoint: **1770 runtime objects /1458 words**,
671 N5/616 N4/97 N3/19 N2/55 unlabelled; **20 N4 remain**.
Strict progress: **1770 reviewed-current,two excluded reviewed blocked-media
drafts,6506 pending of8278;6508 runtime paths absent**,no partial.
Version `b54d436ba00b8218`;checkpoint authority null/Ready false.
These become accepted-main counts only after normal signed integration;
fresh final serialized checks,actual public archives/signatures/four
protected refs and exact-main CI are separate publication evidence.
Protected033空 remains the only pending N5 word,excluded/C2 UNVERIFIED,
not media. No assets/native/device/phone/IME/media/default/package/release
authority. Continue076+ and ALL remaining safe frozen levels/families;
the entire finite objective is not complete.

## Previous qualified source milestone: batch074 actions, search and handling

Batch074 adds **25 complete Russian lessons /1475 file lines**:
**20 actual N4 and five actual N3**,without reclassification,against frozen EN
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual whole review](translation-batches/074-actions-search-and-handling-independent-review-001.json)
read **381 whole teaching bodies**:25 primary EN/RU pairs,130 contextual
EN/RU pairs,70 EN-only comparisons and one complete1708-line EN article.
It also read **417 whole official ordered projections,1438 fresh current
candidate caption/reading/quiz rows,three whole current RU-root rubrics
and the whole named Digital Daijisen 見付ける entry**.
The **10828-byte stdout/native identity** is preserved. Rows are not whole
lessons;the named entry is not the whole Weblio page or modern-frequency
proof;the article does not imply fresh reading of every linked source/PDF.

**C1/C3: no blocking correction found in the25 translated primaries within
assigned whole evidence**,not universal correctness or native certification.
**C2:165 individually bounded protections,18D/147K**:
21 retained source declarations,3D/18K,and144 additional proposals,
15D/129K. Unsupported/withdrawn:none. No additional missing direct pair
was confirmed within the1438-row pool and actually read evidence.
Standalone alternate readings,secondary senses,agent/result,transitivity,
register and domain limits remain explicit;D/K is not unrestricted
substitution. **Broader ordinary modern quiz suitability,necessity/frequency
and global future uniqueness remain UNVERIFIED for all165,including D;
not blanket C2 CLEAN/PASS.**
No substantive correction finding,amendment,focused report or second whole
review is invented for acceptance.

The [qualified source record](translation-batches/074-actions-search-and-handling-reviewed-source.json)
preserves full actions/search/handling teaching and all1725 accepted
baseline runtime RAWs/tracking rows/history. 打つ keepsうつ/ぶつ forms
and sense domains distinct;気付く retains actualN3/kango/mixed reading
and the completeこと attachment rule;見つかる expresses finding result,
not static location;見つける's visual familiarity is attested,not proved frequent.
Qualified source checkpoint: **1750 runtime objects /1438 words**,
671 N5/596 N4/97 N3/19 N2/55 unlabelled; **40 N4 remain**.
Strict progress: **1750 reviewed-current,two excluded reviewed blocked-media
drafts,6526 pending of8278;6528 runtime paths absent**,no partial.
Version `113a0f93170b0594`;checkpoint authority null/Ready false.
These become accepted-main counts only after normal signed integration;
fresh final serialized checks,actual public archives/signatures/four
protected refs and exact-main CI are separate publication evidence.
Protected033空 remains the only pending N5 word,excluded/C2 UNVERIFIED,
not media. No assets/native/device/phone/IME/media/default/package/release
authority. Continue075+ and ALL remaining safe frozen levels/families;
the entire finite objective is not complete.

## Previous qualified source milestone: batch073 movement, direction and transfer

Batch073 adds **26 complete Russian lessons /1493 file lines**:
**20 actual N4,five actual N3 and one unlabelled顔**.
Classifications and absent `jlpt` remain unchanged against frozen EN
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/073-movement-direction-and-transfer-independent-review-001.json)
read **317 whole teaching bodies**:26 primary EN/RU pairs,91 contextual
EN/RU pairs,81 EN-only comparison words and two whole EN-only articles.
It also read **383 whole official ordered projections,1413 original fresh
caption/reading/quiz rows,three whole current RU-root rubrics and923
instruction lines**. No external webpage was fetched or read.
Its **10861-byte stdout/native identity** and bounded C1/C3 findings
remain immutable: no confirmed required factual correction or consequential
Russian-language defect in the26 new lessons against assigned evidence.
**C2 originally had F1–F7 unresolved,not CLEAN**:
F1 was a P2 safety gap;F2–F7 were P3 qualified safeguard questions,
not proof that all were mandatory ordinary modern exclusions.

The original **111 individual judgments:68D/43K** comprise14 retained
source declarations,12D/2K,and97 additional proposals,56D/41K.
The original whole reviewer independently supports withdrawal of the
source向かう–顔 exclusion for that candidate: the facing verb is not
the noun顔,dated nounかんばせ or suffixがお. Frozen EN,intake and all
15 original declarations remain immutable;14 are retained in the candidate.
This support carries only its original qualified scope/identity;
the three顔 objects/body were not newly read in the later focus.

A signed pre-mutation amendment adopts **24 exact direct protections,
RP098–RP121,on17 new owners**,with16 unchanged accepted providers.
The [actual focused review](translation-batches/073-movement-direction-and-transfer-independent-review-focused-002.json)
resolves **only the exact F1–F7 missing-protection questions as bounded
lexical protection**. It read **66 whole bodies/33 EN/RU pairs,32 whole
official objects,33 fresh corrected affected rows,three whole RU-root
rubrics and923 instruction lines**,the complete original report,three
complete amendment/applied/candidate records and the exact329-line diff.
Its **10994-byte stdout/native identity** is preserved.
The24 fresh individual judgments are **12D/12K**. C1/C3 find no confirmed
new substantive factual or consequential Russian regression within that
focus,not a new whole-batch certification.
Four provider pairs,一杯/落す/押す/もらう,were added to append-only
binding004 and actually read whole in this focus;they were not four
whole bilingual pairs in the original317-body scope.

The **135 current pairs:80D/55K** retain111 judgments carrying
**only original scope/identity**,not111 or135 fresh focused judgments.
Exactly **26/26 teaching-body byte tails,9/26 whole new RAW files and
1396/1413 pool rows** are unchanged. Only24 inline exclusions on17
new-owner lists changed;no baseline-provider,teaching-body,caption,
Japanese identity,classification or runtime-provider mutation.
This is not a second317-body/383-object review or1413 fresh corrected rows.
Banking verb/noun,secondary senses,orientation/controlled direction,
notification/invitation,flight,schedule,illness viewpoints and fax-specific
limitations persist;D/K is not unrestricted interchangeability.
**Broader C2 ordinary quiz suitability,modern necessity/frequency and
global future uniqueness remain UNVERIFIED,not blanket CLEAN/PASS.**

The [qualified source record](translation-batches/073-movement-direction-and-transfer-reviewed-source.json)
preserves full movement/direction/transfer teaching and all1699 accepted
baseline runtime RAWs/tracking rows/history. Qualified source checkpoint:
**1725 runtime objects /1413 words**,671 N5/576 N4/92 N3/19 N2/
55 unlabelled; **60 N4 remain**.
Strict progress: **1725 reviewed-current,two excluded reviewed blocked-media
drafts,6551 pending of8278;6553 runtime paths absent**,no partial.
Version `d57de202b04c40d6`;checkpoint authority null/Ready false.
These are accepted-main counts only after normal signed integration;
fresh final serialized checks,actual public archives/signatures/four
protected refs and exact-main CI are separate publication evidence.
Protected033空 remains the only pending N5 word,excluded/C2 UNVERIFIED,
not media. No assets/native/device/phone/IME/media/default/package/release
authority. Continue074+ and ALL remaining safe frozen levels/families;
the entire finite objective is not complete.

## Previous qualified source milestone: batch072 qualities, evaluation and manner

Batch072 adds **20 complete actual N4 Russian lessons /1053 file lines**,
without reclassification, against frozen EN
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/072-qualities-evaluation-and-manner-independent-review-001.json)
read **297 whole teaching bodies**:20 primary EN/RU pairs,98 contextual
EN/RU pairs,55 EN-only word comparisons,four EN-only articles and two
extra RU-only bodies,多い and事故.
It also read **355 whole official ordered projections,1387 original fresh
caption/reading/quiz rows,three whole current RU-root rubrics and three
historical public external payloads**.
Its10819-byte stdout/native identity and actual C1 wording,
**“No consequential new lesson-level factual error established”**,
and C3 wording,**“No consequential new Russian-language defect established”**,
remain scoped to that reading. **C2 originally had two unresolved
consequential medium findings,072-F01/F02;it was not CLEAN.**

Original122 individually judged guards comprise five source **D** and
117 additional proposals:89D/28K,totalling **94D/28K**.
These are bounded direct or qualified-conservative lexical protections,
not ordinary necessity/frequency or unrestricted interchangeability.
A signed pre-mutation amendment adds four direct pairs on new owners:
**RP118 おかしい–違う** and **RP119 凄い–多い** address F01/F02;
**RP120 しっかり–結構** and **RP121 変–事故** adopt two original
K-level questions,not additional consequential findings.

The [actual focused review](translation-batches/072-qualities-evaluation-and-manner-independent-review-focused-002.json)
resolves **only the exact missing-direct-protection findings072-F01/F02**.
It read **16 whole bodies/eight EN/RU pairs,eight whole official objects,
eight fresh affected rows,three whole RU-root rubrics and923 instruction
lines**,plus the complete original report,amendment,applied record and
exact learner/manifest diff. Its9613-byte stdout/native identity is preserved.
It independently judges **RP118/119 D** and **RP120/121 K**.
C1/C3 establish no consequential new error or correction-induced regression
within that focus,not a new whole-batch certification.
The K pairs retain their explicit construction/part-of-speech qualifications;
dictionary inclusion does not establish ordinary modern applicability.

The **126 current pairs:96D/30K** include122 retained judgments carrying
**only original scope/identity**,not122 fresh focused judgments.
Exactly **20/20 bodies,16/20 whole new RAW files and1383/1387 pool rows**
are unchanged. Only four new-owner quiz-exclusion lists changed;
no baseline provider,body,caption,Japanese identity or classification changed.
This is not a second297-body review or1387 freshly reread corrected rows.
There is no automaticどんどん–すっと speed pair,positive/degree/manner
clique or withdrawn070 guard revival. なかなか1599420.4 remains Nの,
not unrestricted な-adjective grammar.
**Broader C2 ordinary quiz suitability,modern necessity/frequency and
global future uniqueness remain UNVERIFIED,not blanket CLEAN/PASS.**

The [qualified source record](translation-batches/072-qualities-evaluation-and-manner-reviewed-source.json)
preserves evaluation/permission,correctness,simplicity/complexity,
appropriateness,strangeness/amusement,rare positive珍しい,firmness,
clarity,progression/movement,sleepiness,flourishing,smell and praise.
All1679 accepted baseline runtime RAWs/tracking rows and historical
evidence persist. Qualified source checkpoint: **1699 runtime objects /
1387 words**,671 N5/556 N4/87 N3/19 N2/54 unlabelled; **80 N4 remain**.
Strict progress: **1699 reviewed-current,two excluded reviewed blocked-media
drafts,6577 pending of8278;6579 runtime paths absent**,no partial.
Version `2aab0f69daec0c92`;checkpoint authority null/Ready false.
These are accepted-main counts only after normal signed integration;
fresh final serialized checks,actual public archives/signatures/four
protected refs and exact-main CI are separate publication evidence.
Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue073+ and ALL remaining safe frozen levels/families;the entire
finite objective is not complete.

## Previous qualified source milestone: batch071 degree, extent, sufficiency and assessment

Batch071 adds **30 complete Russian lessons /1700 file lines**:
**20 actual N4 and ten actual N3** recursive explicit providers, without
reclassification, against frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/071-degree-extent-sufficiency-and-assessment-independent-review-001.json)
read **263 whole teaching bodies**:30 primary EN/RU pairs,83 contextual
EN/RU pairs,36 EN-only word comparisons and one EN-only article.
It also read **389 whole official ordered projections,1367 original fresh
caption/reading/quiz rows and three whole current RU-root rubrics**.
The9351-byte stdout/native identity and actual **C1 PASS,C2 REVISE071-F01,
C3 REVISE071-F02 minor presentation** remain immutable.

The original **166 individually judged guards** comprise26 source
declarations:12 direct/14 qualified-conservative;140 additional proposals:
39 direct/101 qualified-conservative. Their **51D/115K** judgments
support bounded lexical protection,not unrestricted interchangeability
or ordinary necessity/frequency.
A signed pre-mutation amendment adds only **RP141 ずいぶん–実に**
on the new ずいぶん owner and the verified **足す（たす）** reading
in the new 足りる body. 足す remains unlinked,EN-only and absent
from runtime;it is not a new provider.

The [actual focused review](translation-batches/071-degree-extent-sufficiency-and-assessment-independent-review-focused-002.json)
resolves **only071-F01/F02** after reading **seven whole bodies**:
EN/RU pairs forずいぶん,実に,足りる and the EN-only足す body;
**four whole official objects,three fresh affected rows,three whole
RU-root rubrics**,the original report,exact amendment,applied record
and learner/manifest diff. Its8165-byte stdout/native identity is
preserved. **C1 PASS,C2 PASS for the exact amendment/direct lexical
subscope,C3 PASS** apply only to that bounded scope,not blanket C2.
RP141 receives a fresh **D** judgment;expectation/surprise versus
evaluation restrictions remain,without asserting universal equivalence.

The **167 current pairs:52D/115K** include166 retained judgments
carrying **only original scope/identity**,not166 fresh focused judgments.
Exactly **29/30 bodies,28/30 whole new RAW files and1365/1367 pool rows**
are unchanged. One quiz-metadata change affectsずいぶん;one RAW-only
reading change affects足りる. The three fresh affected rows also
include unchanged実に;足す has no runtime row.
This is not a second263-body review or1367 freshly reread corrected rows.
Additionalずいぶん–悪い andなかなか/かなり–ちょっと questions
remain unadopted/unverified,not required corrections.
**Broader C2 ordinary quiz suitability,modern necessity/frequency and
global future uniqueness remain UNVERIFIED.**

The [qualified source record](translation-batches/071-degree-extent-sufficiency-and-assessment-reviewed-source.json)
preserves degree/expectation/evaluation,negative polarity,sufficiency/
intransitivity,timing,inclusive bounds,set exclusion,ratios/multipliers/
approximation and formal-noun attachment. All1649 accepted baseline
runtime RAWs/tracking rows and historical evidence persist.
Qualified source membership: **1679 runtime objects /1367 words**:
671 N5/536 N4/87 N3/19 N2/54 unlabelled; **100 N4 remain**.
Strict progress: **1679 reviewed-current,two excluded reviewed blocked-media
drafts,6597 pending of8278;6599 runtime paths absent**,no partial.
Version `2bc3b24fd9aba5a3`;checkpoint authority null/Ready false.
Final serialized checks,signed integration,actual public archives/
signatures/four protected refs and exact-main CI are separate publication
evidence. Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue072+ and ALL remaining safe frozen levels/families;the entire
finite objective is not complete.

## Previous qualified source milestone: batch070 connectors, response and degree

Batch070 adds **20 complete actual N4 lessons /1114 Russian file lines**
against unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/070-connectors-response-and-degree-independent-review-001.json)
read **225 whole teaching bodies**:20 primary EN/RU pairs,74 contextual
EN/RU pairs and37 frozen-only bodies, plus **400 whole official ordered
projections,1337 original fresh caption/reading/quiz rows and three
whole current RU-root rubrics**. All101 assigned windows returned.
The10979-byte stdout/native identity and actual **C1/C3 CLEAN,
C2 NEEDS_FIX**,including070-F01/F02,remain immutable.

The original74 individual judgments were three source direct guards
and71 additional proposals:31 direct/38 qualified/one rejected/one
unverified. A signed pre-mutation amendment withdraws exactly
**Q68 全然–みんな (R)** and **Q69 全然–もう (U)**:
object totality is not degree;an independently attested extreme-emphasis
もう interjection does not establish the needed actual Japanese cue.
Withdrawal is not a categorical never-overlap or frequency claim.
All three source guards remain:それに–また,できるだけ–なるべく,
ぜひ–必ず.

The [actual focused review](translation-batches/070-connectors-response-and-degree-independent-review-focused-002.json)
resolves **only070-F01/F02 in the corrected focus**, after reading
**18 whole teaching bodies,nine whole official objects,nine affected
rows and three whole RU-root rubrics**,the exact diff,amendment and
original report. All13 assigned windows returned;the10374-byte
stdout/native identity is preserved. Its separate **C1/C2/C3 CLEAN**
verdicts apply **only to that bounded scope**,not blanket C2 approval.
It individually supports **RP72 こう–そうして (D)** and
**RP73 そう–そうして,RP74 ああ–そうして,RP75 こう–それほど,
RP76 こう–そんなに (Q)**,with manner,degree,deictic and construction
restrictions retained. These are whole-word sense/cue protections,
not transitive closure or phrase-component lifting.

The **77 current individual direct pairs:35 direct/42 qualified**
include **72 retained judgments** carrying **only original scope and
identity**,not72 fresh focused judgments. All20 learner bodies remain
RAW-identical;1333 of1337 rows are identical. The nine fresh affected
rows include four changed owners and five unchanged providers;the
other1328 are outside fresh focus,retained by identity. This is not a
second225-body review or1337 freshly reread corrected rows.
Four additional こう–そして/それに–それから/ぜひ–きっと/
ぜひ–もちろん questions remain unverified;全然–いい/良い remains
rejected as phrase-component lifting. **Broader C2 ordinary quiz
suitability,modern necessity/frequency and global future uniqueness
remain UNVERIFIED.**

The [qualified source record](translation-batches/070-connectors-response-and-degree-reviewed-source.json)
preserves manner/degree,agreement/hesitation,contrast/consequence/addition/
choice,feasible effort/eager request/strong negation distinctions.
全然's colloquial affirmative example is not categorically rejected.
All1629 baseline runtime RAWs/tracking rows and historical evidence persist.
Qualified source membership: **1649 runtime objects /1337 words**:
671 N5/516 N4/77 N3/19 N2/54 unlabelled; **120 N4 remain**.
Strict progress: **1649 reviewed-current,two excluded reviewed blocked-media
drafts,6627 pending of8278;6629 runtime paths absent**,no partial.
Version `26fc062e779f8e9e`;checkpoint authority null/Ready false.
Final serialized checks,signed integration,actual public archives/
signatures/four protected refs and exact-main CI are separate publication
evidence. Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue071+ and ALL remaining safe frozen levels/families;the entire
finite objective is not complete.

## Previous qualified source milestone: batch069 time intervals and sequencing

Batch069 adds **20 complete actual N4 lessons /1044 Russian file lines**
against unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/069-time-intervals-and-sequencing-independent-review-001.json)
read **244 whole teaching bodies**:20 primary EN/RU pairs,93 contextual
EN/RU pairs,10 frozen-only bodies and four additional question-provider
EN/RU pairs. It also read **233 whole official ordered projections,1317
original fresh candidate caption/reading/quiz rows and three whole
current RU-root rubrics**;all92 assigned windows returned completely.
The10947-byte stdout/native report identity and separate **C1/C3 CLEAN,
C2 UNVERIFIED**,with no confirmed findings,remain immutable.

Of83 original individual judgments,one source guard was direct and82
additional proposals received20 direct/57 qualified/five unverified
judgments. A pre-mutation amendment withdraws exactly the five unapproved
extras:Q14 これから–今度,Q32 そろそろ–今度,Q33 そろそろ–近く,
Q34 そろそろ–近い and Q53 まず–たいてい. Withdrawal records
insufficient standalone/current-caption evidence,not proved unrelatedness.
The source 間–部屋 guard is preserved.

The [actual focused review](translation-batches/069-time-intervals-and-sequencing-independent-review-focused-002.json)
independently supports only those withdrawals and exact identity:
**18 assigned whole bodies plus the additional whole EN/RU もうすぐ
pair =20 whole bodies,nine whole official objects,nine affected rows,
three whole RU-root rubrics**,the exact diff,amendment and original report.
All13 assigned windows and the additional complete pair returned.
Its10963-byte stdout/native identity is preserved. Its separate
**C1/C3 CLEAN_BOUNDED,C2 UNVERIFIED** are not blanket approval;
only the withdrawal/identity subscope is **CLEAN_BOUNDED**.
No confirmed consequential missing direct guard or source-acceptance
blocker was established within the inspected evidence. The three
additional これから–向こう/もうすぐ–早い/そろそろ–早い
questions remain unverified,not newly approved guards.

The **78 retained direct pairs:21 direct/57 qualified** retain only
their original judgments/scope and exact identity,not78 fresh focused
judgments. All20 learner bodies are RAW-identical;1314 of1317 pool rows
are identical. The nine fresh focused rows include three changed owners
and six unchanged providers;the other1308 are retained by identity.
This is not a second244-body review or1317 freshly read corrected rows.
**Broader C2 ordinary quiz suitability,modern necessity/frequency and
global future uniqueness remain UNVERIFIED.**

The [qualified source record](translation-batches/069-time-intervals-and-sequencing-reviewed-source.json)
preserves event/period,imminence/manner,sequence/probability,calendar-period/
duration and あいだ/ま distinctions. The temporary 一度 sense is
restricted to ひとたび,not transferred to taught いちど.
All1609 baseline runtime RAWs/tracking rows and historical evidence persist.
Qualified source membership: **1629 runtime objects /1317 words**:
671 N5/496 N4/77 N3/19 N2/54 unlabelled; **140 N4 remain**.
Strict progress: **1629 reviewed-current,two excluded reviewed blocked-media
drafts,6647 pending of8278;6649 runtime paths absent**,no partial.
Version `7380f7d1b0604a2a`;checkpoint authority null/Ready false.
Final serialized checks,signed integration,actual public archives/
signatures/four protected refs and exact-main CI are separate publication
evidence. Protected033空 stays excluded/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue070+ and ALL remaining safe frozen levels/families;the entire
finite objective is not complete.

## Previous qualified source milestone: batch068 people, address and social roles

Batch068 adds **20 complete actual N4 lessons /1023 Russian file lines**
against unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/068-people-address-and-social-roles-independent-review-001.json)
read **198 whole teaching bodies**:20 primary EN/RU pairs,73 contextual
EN/RU pairs and12 frozen-only bodies, plus **262 whole official ordered
projections,1297 original candidate caption/reading/quiz rows and three
whole current RU-root rubrics**. All84 assigned windows returned completely.
The10880-byte stdout/native report identity and original **C1/C3
CLEAN_BOUNDED,C2 NEEDS_FIX F1** remain immutable.

F1 identified five missing qualified direct protections:
お嬢さん–女,君–兄 and 彼–あそこ/そこ/向こう.
The pre-mutation amendment preserves its exact evidence and restrictions.
The [actual focused review](translation-batches/068-people-address-and-social-roles-independent-review-focused-002.json)
resolves **only F1**, after reading **16 whole teaching bodies/six whole
official objects/eight affected rows/three whole RU-root rubrics**, the
exact diff, amendment and original report; all12 assigned windows returned.
Its9743-byte stdout/native identity is preserved. Its separate
**C1/C2/C3 CLEAN_BOUNDED** verdicts apply only to that focused scope.

The original98 individual judgments (**two direct/96 qualified**) retain
their original scope, not98 fresh focused judgments. Five new individual
qualified judgments bring the total to **103 direct pairs:two direct/101
qualified**, without transitive closure. All20 learner bodies have exact
RAW identity across the metadata-only correction. Of1297 pool rows,1294
are identical; the focused eight include three changed owners and five
unchanged providers. This is **not1297 freshly reread corrected rows** or
a second whole review. **Broader C2 ordinary quiz suitability, modern
necessity/frequency and global future uniqueness remain UNVERIFIED.**

The [qualified source record](translation-batches/068-people-address-and-social-roles-reviewed-source.json)
retains standalone 女じょ daughter and written-letter 兄けい you,
not suffix-only inferences or generic human-class equivalence.
Rare written 彼あれ place protections preserve their deictic/anaphoric
limits; the taught primary reading remains かれ. Own/other spouse roles,
name suffixes and seniority are not flattened into gender or age rules.
All1589 baseline runtime RAWs/tracking rows and historical evidence persist.

Qualified source membership: **1609 runtime objects /1297 words**:
671 N5/476 N4/77 N3/19 N2/54 unlabelled; **160 N4 remain**.
Strict progress: **1609 reviewed-current,two excluded reviewed blocked-media
drafts,6667 pending of8278;6669 runtime paths absent**,no partial.
Version `b4cbcf44148ebcc6`;checkpoint authority null/Ready false.
Final serialized validation,signed integration,actual public archives/
signatures/four protected refs and exact-main CI are separate publication
evidence,not reviewer claims. Protected033空 stays excluded/C2 UNVERIFIED,
not media. No assets/native/device/phone/IME/media/default/package/release
authority. Continue069+ and ALL remaining safe frozen levels/families;
the full finite objective is not complete.

## Previous qualified source milestone: batch067 shapes, properties and comparison

Batch067 adds **19 complete lessons /993 Russian file lines**:
16 actual N4 primaries and three source-required actual N3 providers
型/式/種類, without relabelling or changing frozen EN
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual independent review](translation-batches/067-shapes-properties-and-comparison-independent-review-001.json)
read **224 whole teaching bodies**:19 primary EN/RU pairs,85 contextual
EN/RU pairs and16 frozen-only bodies, plus **233 whole official ordered
projections,1277 actual candidate caption/reading/quiz rows and three
whole current RU-root rubrics**. All94 assigned windows and both semantic
record projections returned completely. The10960-byte actual stdout/native
report identity is preserved.

The actual separate **C1/C2/C3 verdicts are CLEAN_BOUNDED**, not unqualified
global approval. No consequential defect was reported within the evidence
read. **Broader C2 ordinary quiz suitability, modern necessity/frequency
and global future uniqueness remain UNVERIFIED.**
All111 direct pairs received individual judgments:
nine preserved source guards (**7 direct/2 qualified**) and102 additional
proposals (**10 direct/92 qualified**), with their exact reasons,
Japanese senses, alternate standalone readings and restrictions retained.
Qualified conservative lexical/cue protection is not a primary-caption
duplicate, universal synonymy, a transitive clique or necessity proof.

The [qualified source record](translation-batches/067-shapes-properties-and-comparison-reviewed-source.json)
keeps predicted certainty restricted to 固い/堅い; physical コード is
2855837, not the music entry. 深い's distant-field guards are baseball-only,
not geographic synonymy or resolution of the protected 空 question.
Separate 形/体 readings, 表's information-table reading and ordinary
裏 lining/inside senses remain distinct. No English line/thread/rope or
softness-alone/wet-and-soft shortcut was adopted.
All1570 accepted baseline runtime RAWs and tracking rows are unchanged.
This is one whole independent review, not1277 whole lessons or recertification
of the entire frozen corpus.

Qualified source membership: **1589 runtime objects /1277 words**:
671 N5/456 N4/77 N3/19 N2/54 unlabelled; **180 N4 remain**.
Strict progress: **1589 reviewed-current,two excluded reviewed blocked-media
drafts,6687 pending of8278;6689 runtime paths absent**,no partial.
Version `f82172af12d5695b`;checkpoint authority null/Ready false.
Final serialized validation,signed integration,actual public archives/
signatures/four protected references and exact-main CI are separate
publication evidence,not reviewer claims.
Protected033空 remains excluded pending/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue068+ and ALL remaining safe frozen levels/families; the full finite
objective is not complete.

## Previous qualified source milestone: batch066 leisure, sports, toys and sounds

Batch066 adds **16 complete actual N4 lessons /866 Russian file lines**
against unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual independent review](translation-batches/066-leisure-sports-toys-and-sounds-independent-review-001.json)
read **113 whole teaching bodies**:16 primary EN/RU pairs,33 contextual
EN/RU pairs and15 frozen-only bodies, plus **129 whole official ordered
projections,1258 actual candidate caption/reading/quiz rows and three
whole current RU-root rubrics**. All52 assigned reading windows returned
completely. The10870-byte stdout/native report identity is preserved.

**C1/C3 CLEAN; C2 remains UNVERIFIED**, not relabelled CLEAN.
No confirmed repairable omission was reported within the evidence read.
All29 direct proposals received individual independent dispositions:
**eight direct lexical/current-caption protections and21 qualified
conservative protections**, with each reason and restriction retained.
These support only the recorded lexical/category/referent protection,
not universal synonymy or ordinary quiz necessity.
Modern necessity/frequency, broader ordinary quiz suitability and future
global uniqueness remain **UNVERIFIED**. This is one whole review,
not a review of1258 whole lessons or the entire frozen corpus.

The [qualified source record](translation-batches/066-leisure-sports-toys-and-sounds-reviewed-source.json)
preserves the separate noun/verb/method distinctions, sound production
versus audibility, separate 音 readings, and the restricted dictionary
senses behind conservative guards. No transitive clique, bare unrestricted
音 fame claim or festival/calendar-holiday identity was adopted.
All1554 previously accepted runtime RAWs and tracking rows are unchanged.

Qualified source membership: **1570 runtime objects /1258 words**:
671 N5/440 N4/74 N3/19 N2/54 unlabelled; **196 N4 remain**.
Strict progress: **1570 reviewed-current,two excluded reviewed blocked-media
drafts,6706 pending of8278;6708 runtime paths absent**,no partial.
Version `54c5285050e9254c`; checkpoint authority null/Ready false.
Final serialized validation,signed integration,actual public archives/
signatures/four protected references and exact-main CI are separate
publication evidence,not reviewer claims.
Protected033空 remains excluded pending/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue067+ and ALL remaining safe frozen levels/families; the full finite
objective is not complete.

## Previous qualified source milestone: batch065 writing, media and electronic devices

Batch065 adds **22 complete actual N4 lessons /1121 Russian file lines**
against unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/065-writing-media-and-electronic-devices-independent-review-001.json)
read **180 assigned whole teaching bodies plus two additional whole 場所
bodies:182 total,209 whole official ordered projections,1242 actual
caption/reading/quiz rows and three current RU-root rubrics**.
The assigned bodies comprise22 EN/RU primary pairs,46 EN/RU provider pairs
and44 source-only EN lessons; no article was assigned.
Rows are not1242 whole lessons. Original **C1/C3 CLEAN, C2 NEEDS_FIX F01**
remain immutable. Thirty additional guards received individual judgments:
two direct identical-variant protections and28 qualified lexical/caption
protections; two original source PC guards were also assessed explicitly.

The [actual bounded focused review](translation-batches/065-writing-media-and-electronic-devices-independent-review-002.json)
freshly read **four whole teaching bodies,four whole official objects,
two current full-metadata rows and three whole RU-root rubrics**,
the complete original report, signed pre-mutation resolution freeze,
identity proof and exact diff. It resolves **F01/Q31字–場所** only at the
qualified direct lexical/actual-caption level: separately attested bare
字/あざ and 字/あざな village-section senses can fit the actual 場所 cue
«место; местоположение». This does not teach a geographic meaning of じ,
equate all places, or derive protection transitively through 所/土地.

All22 Russian teaching-body bytes/1242 captions-readings-levels-types-tags
and1532 accepted baseline RAWs remain identical; only 字's exclusion header
appends 場所. Original30 individual judgments and two source guards carry
only their original scopes/identity, **not31 fresh judgments,a second whole
182-body review or1242 freshly reviewed corrected rows**.
Actual10969-byte original and9730-byte focused stdout/native report
identities persist. **C2 remains qualified direct protection only; all31
additional guards' ordinary modern necessity/frequency,broader ordinary
quiz suitability and global future uniqueness remain UNVERIFIED.**
Two source guards plus31 additional protections are33 direct pairs,not cliques.

The owner's explicit migration-complete/resume instruction supersedes only
the [temporary storage pause](translation-batches/065-writing-media-and-electronic-devices-owner-requested-storage-pause-001.json).
Historical evidence,review verdicts and the frozen target remain unchanged;
relocation is not semantic approval. No new review was required for relocation.

Qualified source membership: **1554 runtime objects /1242 words**:
671 N5/424 N4/74 N3/19 N2/54 unlabelled; **212 N4 remain**.
Strict progress: **1554 reviewed-current,two excluded reviewed blocked-media
drafts,6722 pending of8278;6724 runtime paths absent**,no partial.
Version `35e05ae7058fb767`; checkpoint authority null/Ready false.
Final serialized validation,signed main integration,actual public archives/
signatures/four protected references and exact-main CI are separate
publication evidence,not reviewer claims.
Protected033空 remains excluded pending/C2 UNVERIFIED,not media.
No assets/native/device/phone/IME/media/default/package/release authority.
Continue066+ and ALL remaining safe frozen levels/families; the full finite
objective is not complete.

## Previous qualified source milestone: batch064 places, institutions and geography

Batch064 adds **26 complete lessons /1487 Russian file lines**:
22 actual N4 words and four required actual N3 providers, without relabelling,
against unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/064-places-institutions-and-geography-independent-review-001.json)
read **172 whole teaching bodies,169 whole official ordered projections,
1220 current caption/reading/quiz rows and three current RU-root rubrics**.
The172 bodies are26 EN/RU primary pairs,52 EN/RU provider pairs and16
source-only EN lessons; no article was assigned. Rows are not1220 lessons.
Actual **C1/C2/C3 NEEDS_FIX**, all coupled to F1's missing direct
市民–人口 guard, remain immutable. No separate Japanese/prose defect
was established;24 original proposals were individually retained only
as qualified direct lexical/caption protection.

The [actual bounded focused review](translation-batches/064-places-institutions-and-geography-independent-review-002.json)
freshly read **four whole teaching bodies,three whole official objects,
two current full-metadata rows and three whole RU-root rubrics**,
the original report, signed resolution freeze, identity proof and exact diff.
It independently resolves **F1/Q25市民–人口**: the actual Russian cue
«население» can denote inhabitants collectively, while 人口's statistical
restriction is absent from that short cue. This is not citizens equalling
a number, generic person inclusion or unrestricted Japanese equivalence.

All26 teaching-body bytes/1220 captions-readings-levels-types-tags remain
identical; only 市民's negative field changes under the signed pre-mutation
freeze. Original24 qualified judgments and five source guards carry their
original scopes, **not25 fresh judgments, a second172-body review or1220
fresh corrected rows**. Original10931-byte/focused10009-byte actual
stdout/native identities persist. Focused CLEAN applies only to its bounded
correction; **broader C2 ordinary quiz suitability, and all25 ordinary modern
necessity/frequency/global future uniqueness, remain UNVERIFIED**.

The focused report also independently clarifies the original reader's
header-plus-file payload sizes versus actual working/Git RAW file sizes.
Original RU-root rubric hashes were correct; neither report is rewritten,
and this clarification is not another whole semantic review.
Five source guards plus25 qualified additions are30 direct protections,
not transitive cliques. All1506 baseline RAWs/tracking/history and protected
excluded033空 are preserved. No new asset or runtime provider is fabricated.

Qualified source membership: **1532 runtime objects /1220 words**:
671 N5/402 N4/74 N3/19 N2/54 unlabelled; **234 N4 remain**.
Strict progress: **1532 reviewed-current, two excluded reviewed blocked-media
drafts,6744 pending of8278;6746 runtime paths absent**, no partial.
Version `600e5cd458536a7c`; checkpoint authority null/Ready false.
Main integration, actual public archives/signatures/protected references
and exact-main CI are separate publication evidence, not reviewer claims.
No native/device/phone/IME/media/default/package/release authority.
Continue065+ and all remaining safe frozen levels/families, not one batch
or source-only completion; protected空 and release/media gates remain separate.

## Previous source milestone: batch063 giving, receiving and honorifics

Batch063 adds **20 complete actual N4 lessons /1146 Russian file lines**
against unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/063-giving-receiving-and-honorifics-independent-review-001.json)
read **199 complete teaching bodies,219 whole official projections,
1194 actual caption/reading/quiz rows and three current RU-root rubrics**.
The199 bodies comprise20 EN/RU primary pairs,64 EN/RU provider pairs,
30 source-only EN lessons and the whole1707-line EN formal-nouns article.
Rows are not1194 whole lessons; article reading is not linked-webpage reading.
Actual **C1/C2/C3 CHANGES_REQUIRED**, all coupled to F1's missing direct
あげる–やる guard, remain immutable. No separate Japanese/prose defect
was confirmed;90 original active proposals were individually retained only
as qualified lexical/frame protection.

The [actual bounded focused review](translation-batches/063-giving-receiving-and-honorifics-independent-review-002.json)
freshly read **eight complete teaching bodies, four whole official entries,
four current caption/metadata rows and three current RU-root rubrics**,
the complete original report and exact signed resolution freeze.
It resolves F1 across its three coupled facets through direct **Q94あげる–やる**,
supported by standalone1012980.4/1352320.5 and both whole bilingual teachings.
The existingやる–上げる guard cannot protect the distinct new IDあげる.
It independently adopts **Q95ご存じ–承知** only for nominal awareness:
whole1593570.1/1349480.1 and complete EN/RU承知 establish that exact gap,
not agreement, forgiving, generic comprehension or ordinaryご存じする.
The original gap was UNVERIFIED, not a confirmed missing-guard finding.

Original90 judgments carry unchanged identities, not92 fresh judgments.
All20 learner bodies/1146 lines and1194 captions/readings/levels/types/tags
are unchanged;1192 other whole-file/metadata identities are checked.
Two changed negative-field rows and their two providers were actually
returned separately, **not1194 freshly reread amended rows or a second
whole199/201-body review**. Original10925-byte and focused10845-byte actual
stdout/native report identities are preserved.
Effective C1/C2/C3 CLEAN applies only within the documented scopes.
**All92 ordinary modern necessity/frequency, broader ordinary quiz
suitability and global future uniqueness remain UNVERIFIED.**
Four otherやる interactions remain NEED_UNVERIFIED and unadopted,
neither confirmed safe nor confirmed missing guards.

Five source guards plus92 qualified additions remain direct protections,
not transitive cliques or full-caption synonym claims.
Original Q82/Q85/Q88 author withdrawals remain historical, not reviewer
resolutions: a shared gift occasion does not establish either actual full
travel/visitor-gift versus congratulations/gratitude/sympathy caption.
Optional unavailable navigation is unwrapped while supported teaching
remains self-contained; no forced provider or asset.
All1486 baseline RAWs/tracking/history and protected excluded033空 are preserved.
Signed original/amended freezes preceded their respective runtime changes.

Qualified membership: **1506 runtime objects /1194 words**:
671 N5/380 N4/70 N3/19 N2/54 unlabelled; **256 N4 remain**.
Strict progress: **1506 reviewed-current, two excluded reviewed blocked-media
drafts,6770 pending of8278;6772 runtime paths absent**, no partial.
Version `8165025f1f993ccb`; checkpoint authority null/Ready false.
Final serialized validation, signed integration, actual public archives and
exact-main CI remain separate publication evidence, not reviewer claims.
No new assets/app/device/phone/IME/media/default/package/release authority.
**Continue064+ and every remaining safe frozen level/family; full task is
not complete. Protected空 remains separate, UNVERIFIED and not media.**

## Prior source milestone: batch062 changes, breaking and continuation

Batch062 adds **25 complete lessons /1327 Russian file lines** against
the unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`:
**23 actual N4 and two actual N3 words**, with classifications preserved.
The [actual original whole review](translation-batches/062-changes-breaking-and-continuation-independent-review-001.json)
read **298 complete assigned teaching bodies,314 whole official objects,
all1174 actual candidate caption/reading/quiz rows and three current RU-root
rubrics**. The298 bodies comprise25 EN/RU root pairs,92 EN/RU provider
pairs,62 source-only EN lessons and two whole EN contextual articles;
rows are not1174 baseline teaching bodies.
Its actual **C1 PASS / C2 REVISE / C3 PASS** and64 individually qualified
retain judgments remain immutable.

The [actual bounded focused review](translation-batches/062-changes-breaking-and-continuation-independent-review-002.json)
resolves **062-R1** with direct **Q65止める–切る** protection.
It freshly read **four complete teaching bodies, two whole official entries,
two affected actual pool rows and three current RU rubrics**, plus the
complete original report, proposal, exact diff and executed identity proof.
The protection concerns stopping operation/switching off or terminating a
connection/process under the actual broad «прекращать» cue:
1310670.1 and1384830.3/4 directly support it.
It is not inferred through消す/終わる, not every stopping action is cutting,
and symmetric exclusion is not bidirectional lexical equivalence.

Original64 judgments, all25 learner bodies and all1174 captions/readings
carry verified unchanged identities; **not a second whole review,
65 fresh semantic judgments or1174 freshly reread amended rows**.
The effective facets PASS only in their documented scopes;
C2 covers assigned text/dependencies and qualified direct lexical protection,
**not global ordinary-modern quiz certification**.
**All65 ordinary modern necessity/frequency, broader ordinary quiz
suitability and global future uniqueness remain UNVERIFIED.**
Both actual stdout/native-report byte identities are preserved.

Eight original directed source guards/seven unordered pairs are preserved,
plus65 qualified additional pairs:72 unique direct pairs/73 declarations.
Eleven available original wrappers retained/30 unavailable destinations
unwrapped; supported self-contained explanations replace optional article
navigation without removing Japanese facts/readings or forcing providers.
Transitivity is not intention; suffix meanings do not freely transfer to
bare verbs; actual transitive終わる and latest/most-recent最後 remain taught.
All1461 baseline RAWs/tracking/history and protected excluded033空 are preserved.
Signed original and resolution freezes preceded their respective changes.

Qualified membership: **1486 runtime objects /1174 words**:
671 N5/360 N4/70 N3/19 N2/54 unlabelled; **276 N4 remain**.
Strict progress: **1486 reviewed-current, two excluded reviewed blocked-media
drafts,6790 pending of8278;6792 runtime paths absent**, no partial.
Version `a6c0541b79431b29`; checkpoint authority null/Ready false.
Final serialized validation, signed integration, actual public archives and
exact-main CI remain separate publication evidence, not reviewer claims.
No new assets/app/device/phone/IME/media/default/package/release authority.
**Continue063+ and every remaining safe frozen level/family; full task is
not complete. Protected空 remains separate, UNVERIFIED and not media.**

## Prior source milestone: batch061 nature and landscapes

Batch061 adds **22 complete actual N4 lessons /1134 Russian file lines**
against the same frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/061-nature-and-landscapes-independent-review-001.json)
read **228 assigned complete teaching bodies,271 whole official objects,
all1149 actual candidate caption/reading/quiz rows, two complete saved native
dictionary payloads and three current RU-root rubrics**, plus one additional
complete RU有名 lesson. The228 assigned bodies comprise22 EN/RU roots,
71 EN/RU provider pairs and42 source-only EN lessons; rows are not1149 bodies.
Its original C1/C3 **CLEAN** and C2 **NEEDS_REVISION** remain immutable.

The [actual bounded focused review](translation-batches/061-nature-and-landscapes-independent-review-002.json)
resolves **061-R1** with direct **Q33世界–有名** protection.
It freshly read **four complete teaching bodies, two whole official objects,
all1149 amended caption/reading/quiz rows and three current RU rubrics**,
plus the complete original report and mechanical identity proof.
World-famous世界 takes **の** in1373860.3;有名 is a **な-adjective**
in1541620.1. Conservative symmetric question protection does not make
the reverse caption「мир」a translation of有名 or turn世界 into aな-adjective.
Original32 qualified judgments and all22 bodies carry their unchanged
identities; this is **not a second whole review or33 fresh semantic judgments**.
Effective C2 CLEAN is only for assigned text/dependencies and qualified
lexical/caption protection, not global ordinary-modern quiz suitability.
**Ordinary modern necessity/frequency for all33 and global uniqueness
remain UNVERIFIED.** Both actual stdout/native-report byte identities remain.

Actual native景色 reading history supports the frozenkango/special-reading
classification, not productiveけ for景 or unrestricted transfer of historical
気色 feelings/manifestations. The rare appearance/state/ceramic-colour guards
retain their exact bounds. Independent alternate人間じんかん, mountain-forest山,
figurative林, dot/glyph/sumo星, specific花見 viewing, secondary光 and Internet草
protections are not transitive cliques or new everyday-frequency claims.
Cloud versus weather, destructive-fire incident versus flame, forest and
lake naming without fixed numerical thresholds, plant leaf/branch versus
paper counters/business branches remain fully taught in Russian.

Nine available original wrappers retained/26 unavailable optional destinations
unwrapped without removing Japanese facts/readings; no forced provider or asset.
All1439 baseline RAWs/tracking/history and protected excluded033空 are preserved.
Signed original and resolution freezes preceded their respective changes.
Qualified membership: **1461 runtime objects /1149 words**:
671 N5/337 N4/68 N3/19 N2/54 unlabelled;299 N4 remain.
Strict progress: **1461 reviewed-current, two excluded reviewed blocked-media
drafts,6815 pending of8278;6817 runtime paths absent**, no partial.
Version `97896ffd55fe07c2`; checkpoint authority null/Ready false.
Final serialized validation, signed integration, actual public archives and
exact-main CI remain separate publication evidence, not reviewer claims.
No new assets/app/device/phone/IME/media/default/package/release authority.
**Continue062+ and every remaining safe frozen level/family; full task is
not complete. Protected空 remains separate, UNVERIFIED and not media.**

## Prior source milestone: batch060 transport and journeys

Batch060 adds **24 complete N4 lessons /1428 Russian file lines** against
the unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual single independent report](translation-batches/060-transport-and-journeys-independent-review-001.json)
read **262 complete assigned teaching bodies,251 whole official objects,
all1127 actual candidate caption/reading/quiz rows and both complete
stored operator-page payloads**. The262 bodies comprise24 EN/RU primary
pairs,80 EN/RU provider pairs,53 source-only EN lessons and the whole
206-line contextual occupation article, not1127 baseline lessons.
C1/C3 are CLEAN in their assigned correctness/Russian-prose scopes.
C2 is CLEAN **only for assigned text, dependencies and qualified
lexical/caption protections**, not blanket corpus suitability.
All36 direct proposals are individually retained; no findings or repairs.
**Ordinary modern necessity/frequency for all36 and global uniqueness
remain UNVERIFIED.** Original stdout/native-final report bytes are preserved.

Archaic通る/知る, dated汽車/電車, selected-caption普通/大丈夫,
progression運ぶ/行く, noun急/危険 and spelling-qualified船 protections
retain their exact limitations. Neither physical running alone nor an
English-only “run” comparison justifies the independently examined走る
pairs. No transitive transport, vehicle, container or circumstance clique.
The unavailable運転手 article promise becomes supported self-contained
role/reading facts. ガソリン withdraws the unsupported gas-frequency
negative:1040060.6 genuinely records unlabelled gasoline, without a new
frequency claim. 特急 preserves genuine1454750 operator notes and two
specifically read operator examples, not all-operator tariffs or future
speed/fare guarantees. The author's premature denial of those dictionary
notes was explicitly withdrawn append-only before semantic freeze/writing;
the original private adjudication remains unchanged.

Routeを remains intransitive; recurrent attendance differs from a single
visit or hospitalization. Transfer particles, recognized普通な,急ぐ's
ぐ→いで,steam/dated train senses,港 readings,船 combining forms and
indoor/outdoor parking distinctions remain fully taught.
Eight available original wrappers retained/31 unavailable optional
destinations unwrapped without deleting Japanese facts/readings.
All24 actual N4 classifications and Japanese metadata/forms/examples remain.

Qualified membership: **1439 runtime objects /1127 words**:
671 N5/315 N4/68 N3/19 N2/54 unlabelled;321 N4 remain.
Strict progress: **1439 reviewed-current, two excluded reviewed blocked-media
drafts,6837 pending of8278;6839 runtime paths absent**, no partial.
Version `d57b831a620f33e3`; checkpoint authority null/Ready false.
All1415 baseline RAWs/tracking/history and protected excluded033空 are preserved.
The signed semantic freeze preceded learner writing.
Final serialized validation, signed integration, actual public archives and
exact-main CI are separate publication evidence, not reviewer claims.
No new assets/app/device/phone/IME/media/default/package/release authority.
**Continue every remaining safe frozen level/family; full task is not complete.
Protected空 remains separate, UNVERIFIED and not media.**

## Prior source milestone: batch059 social actions and gatherings

Batch059 adds **22 complete lessons /1221 Russian file lines** against
the unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`:
**20 actual N4 roots and the required N3スピーチ/演説**, without relabeling.
The [actual original whole review](translation-batches/059-social-actions-and-gatherings-independent-review-001.json)
read **191 assigned complete teaching bodies plus two additional質問 bodies,
189 whole official objects and all1103 candidate caption/reading/quiz rows**.
Its original C1 **NO_CONFIRMED_TEACHING_DEFECT; Q49 UNVERIFIED**,
C2 **CHANGES_REQUIRED** and C3 **CLEAN_WITHIN_READ_PROSE_SCOPE** remain immutable.
The [actual focused review](translation-batches/059-social-actions-and-gatherings-focused-review-001.json)
independently accepts F1's direct **Q52尋ねる–質問** protection and resolves
F2 by **withdrawing unverified Q49勝つ–取る**, not by claiming that取る
never means winning. Its fresh scope is **eight complete teaching bodies,
four existing entire objects and all1103 current caption/reading/quiz rows**.
Limited C1/C2/C3 CLEAN is not a second whole review.

The53 current directed fields comprise the original52 individually qualified
retain judgments and newQ52; Q49 is absent, its historical proposal unchanged.
All22 lesson bodies and all1103 captions/readings retain their exact identities.
Dated謝る/心配 components, nominal congratulations, reading-onlyたずねる,
conditionalご案内 knowledge and separate sumo/cards取る comparisons retain
their qualifications. No transitive speech/noise/media/competition clique
or English-only win/acquisition equivalence is inferred.
The one bounded native return contains the complete first DigitalDaijisen
案内 entry and separateあない, but only part of the second dictionary entry:
it is not whole-page or frequency evidence.
**Ordinary modern necessity/frequency and broader uniqueness remain UNVERIFIED.**

Apology, wishes, awareness/consent, restraint, caution/reprimand, asking/visiting,
guidance, giving/receiving care, celebration/sympathy, broadcasting, competition,
winning/losing and gathering agency remain fully taught.
試合 preserves its actual wago/ateji classification.
Nine available source wrappers remain;26 unavailable optional destinations
are unwrapped without removing their visible Japanese facts/readings.

Qualified membership: **1415 runtime objects /1103 words**:
671 N5/291 N4/68 N3/19 N2/54 unlabelled.
Strict progress: **1415 reviewed-current, two excluded reviewed blocked-media
drafts,6861 pending of8278;6863 runtime paths absent**, no partial.
Version `674da6962ef93ad7`; checkpoint authority null/Ready false.
All1393 baseline RAWs/tracking/history and protected excluded033空 are preserved.
Signed semantic and exact resolution freezes preceded their respective changes.
Final serialized validation, signed integration, actual public archives and
exact-main CI remain separate publication evidence, not reviewer claims.
No asset/app/device/phone/IME/media/default/package/release authority.
**Continue every remaining safe frozen level/family; full task is not complete.
Protected空 remains separate, UNVERIFIED and not media.**

## Prior source milestone: batch058 memory, intentions and certainty

Batch058 adds **20 complete N4 lessons /1011 Russian file lines** against
the unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual original whole review](translation-batches/058-memory-intentions-and-certainty-independent-review-001.json)
read **126 complete teaching bodies,174 whole official objects and all1081
candidate caption/reading/quiz rows**, plus two stored bounded native returns.
Its **C1/C3 CLEAN and C2 NEEDS_REVISION remain immutable**.
The [actual focused review](translation-batches/058-memory-intentions-and-certainty-focused-review-001.json)
resolves F1 with direct **訳–説明**, and F2 with BOTH independent
**やはり–また andやっぱり–また** guards.
It freshly read **10 complete teaching bodies,six entire objects and all1081
current captions/readings**, not the whole original scope again.
All20 teaching-body hashes and all1081 captions/readings are unchanged.
This is one whole review plus one exact focused resolution, not a second
whole CLEAN report or a metadata rewrite of the original verdict.

The28 qualified direct protections comprise four original source fields,
21 individually supported proposals carried from the original review,
and three independently accepted focused repairs.
Alternate/reading-only 訳/やく, bare本/もと cause, archaic instantaneousきっと,
lexical決める consumption and tentative-memory確か retain their exact limits.
No transitivity through variants,予定,場合,食べる or absentもしも is inferred.
The two bounded native definitions support only their examined prediction/
resolve question; related indexes and one failed request establish no frequency.
**Ordinary modern necessity/frequency and broader uniqueness remain UNVERIFIED.**

Remembering versus retaining, intention versus schedule, expectation versus
obligation, hypotheticalたら/ば, explanation/grounds and transitive/intransitive
decision distinctions remain explicit. The prewritingもし correction withdraws
an older planning overstatement, not a post-review body change.
Actual primary identities/readings/levels/types/tags/kanji remain unchanged.
The later parent binding has175 objects because説明's1199080 footer was also
read; it does not retroactively enlarge the original174-object review.
Nine source wrappers retained/23 unavailable optional wrappers unwrapped;
unavailable formal-noun/conditional article promises became factual prose.

Qualified membership: **1393 runtime objects /1081 words**:
671 N5/271 N4/66 N3/19 N2/54 unlabelled.
Strict progress: **1393 reviewed-current, two excluded reviewed blocked-media
drafts,6883 pending of8278;6885 runtime paths absent**, no partial.
Version `8378ce96cf6756b8`; checkpoint authority null/Ready false.
All1373 baseline RAWs/tracking/history and protected excluded033空 are preserved.
Signed semantic and exact resolution freezes preceded their respective changes.
Final serialized validation, signed integration, actual public archives and
exact-main CI remain separate publication evidence, not reviewer claims.
No asset/app/device/phone/IME/media/default/package/release authority.
**Continue every remaining safe frozen level/family; full task is not complete.
Protected空 remains separate, UNVERIFIED and not media.**

## Prior source milestone: batch057 feelings, reactions and attitudes

Batch057 adds **21 complete lessons /1211 Russian file lines** against
the unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`:
**20 actual N4 roots plus the required N3幸せ provider**, without relabeling.
The [actual single independent report](translation-batches/057-feelings-reactions-and-attitudes-independent-review-001.json)
read **138 complete teaching bodies,138 whole official objects and all1061
actual candidate caption/reading/quiz rows**. This is not1061 baseline
teaching bodies or newly fetched native definitions.
No consequential C1/C3 defect was found within assigned correctness/
Russian-prose scopes; C2 accepts the word-only dependencies and
**all nine preserved source edges plus18 individually qualified direct
proposals** against that actual pool. No findings or repairs were required.
Original report bytes and successful stdout/native-final identity are preserved.

The exact **びっくり word-only adaptation** omits only optional image/image_scene
metadata; all teaching remains. Its source image is separately pending,
not copied/generated/bound or a new blocked-media draft.
The exactねっしん adaptation removes source-internal N3-list indirection,
not the identity of熱心 or actual kanaID/reading/N4/type:kango/kanji[].
Mixed気持ち retains on-first kango without an all-on claim;
まじめ retains native/ateji treatment.
Reaction/enjoyment, surprise/causation, tears/animal calls,
kindness/easiness and state/change/particle distinctions remain explicit.
Reading-only safeguards do not equate Japanese senses;
conservative Q8/Q16/Q17/Q18 retain their exact asymmetric/POS/sense limits.
No transitive feeling/amount/work-ethic clique or ordinary necessity claim.
Broader uniqueness and ordinary modern necessity/frequency remain **UNVERIFIED**.

Qualified membership: **1373 runtime objects /1061 words**:
671 N5/251 N4/66 N3/19 N2/54 unlabelled.
Strict progress: **1373 reviewed-current, two excluded reviewed blocked-media
drafts,6903 pending of8278;6905 runtime paths absent**, no partial.
Version `00199a7e565a0693`; checkpoint authority null/Ready false.
All1352 baseline RAWs/tracking/history and protected excluded033空 are preserved.
Fifteen source wrappers retained/23 unavailable optional wrappers unwrapped.
The signed semantic freeze preceded all learner writing.
Final serialized validation, signed integration, actual public archives and
exact-main CI are separate publication evidence, not reviewer claims.
No new asset/app/device/phone/IME/media/default/package/release authority.
**The finite objective remains incomplete: continue all remaining safe
frozen levels/families; protected空 remains separate, not media.**

## Prior source milestone: batch056 health, recovery and safety

Batch056 adds **20 complete N4 lessons /1157 Russian file lines** against
the unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual single independent report](translation-batches/056-health-recovery-and-safety-independent-review-001.json)
actually read **163 complete teaching bodies**,168 whole official objects,
all1040 candidate captions/readings/quiz rows and two stored bounded native
returns. Two failed requests supplied no definitions. This is not1040
complete baseline teaching bodies or whole-page native evidence.
C1/C3 are CLEAN within assigned correctness/Russian-prose scopes.
Original **C2 NEEDS_REVISION F1/Q17** remains immutable:
the [exact append-only resolution](translation-batches/056-health-recovery-and-safety-amended-authoring-001.json)
removes only the unsupported **安全–安心** exclusion, retaining大丈夫.
Objective safety and subjective reassurance are not equated by an English
synonym or native related-word index. All20 actually reviewed teaching bodies
and1040 captions/readings remain identical.
**Seventeen individually qualified direct guards retained; Q17 withdrawn**,
none unresolved. This is the original review and its exact prescribed
metadata resolution, not a second CLEAN review or fresh semantic rereading.
The signed resolution freeze preceded implementation.

Mixed-reading歯医者 retains frozen type:wago;具合 retains type:kango and
its actual tags without an all-on claim. Deprecated看護婦 is a recognition
target, not a recommended modern job title; absent看護師 files do not mean
the Japanese word does not exist. Source-only治す remainsN2.
Medical roles, valency, change/result states and usual health/repair spelling
distinctions are preserved without denying independently attested overlap.
Rare喉/こん・こう fish and Kansai直す put-away/put-back protections retain
their restrictions; no ordinary frequency/necessity is inferred.
The returned血 character/index material is not a standaloneち definition
or evidence for bare Russianжар. Broader global uniqueness and ordinary
modern necessity/frequency remain **UNVERIFIED**.

Qualified membership: **1352 runtime objects /1040 words**:
671 N5/231 N4/65 N3/19 N2/54 unlabelled.
Strict progress: **1352 reviewed-current, two excluded reviewed blocked-media
drafts,6924 pending of8278;6926 runtime paths absent**, no partial.
Version `fc5bb42159c65874`; checkpoint authority null/Ready false.
All1332 baseline RAWs/tracking rows and protected excluded033空 are preserved.
Five source wrappers retained/26 unavailable optional wrappers unwrapped;
no source-only provider forced into runtime.
Signed main integration, actual public archives and exact-main CI are separate
publication evidence, not report claims. No new asset/app/device/phone/IME/
media/default/package/release approval.
Continue every remaining safe frozen level/family; 空 remains separately
pending/C2 UNVERIFIED, not a third media draft.

## Prior source milestone: batch055 clothing, accessories and body

Batch055 adds **20 complete N4 lessons /1035 current Russian file lines**
against the same frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual single independent report](translation-batches/055-clothing-accessories-and-body-independent-review-001.json)
read **168 complete teaching bodies**,224 whole official objects,
all1020 candidate captions/readings and six stored bounded lexical returns.
C1/C3 are CLEAN in their assigned correctness/Russian-prose scopes.
The original **C2 NEEDS_REVISION** and both findings remain immutable.
The [exact append-only resolution](translation-batches/055-clothing-accessories-and-body-amended-authoring-001.json)
implements F1's independently prescribed directサンダル–靴 protection
and F2's Q11 ability-sense reference correction to1554820:2.
**All20 reviewed teaching bodies and1020 captions/readings are unchanged**;
one header line was added. The36 qualified direct protections comprise
35 individually retained proposals and the original review's one prescribed
addition, not a second CLEAN review or transitive footwear/person/clothing clique.
The resolution freeze preceded its metadata implementation.
Historical pre-writing references, original author receipts and report are preserved.

木綿's selected material reading is separate from restrictedきわた tree
and oldゆう/thread identities; explicitもめん thread evidence is not arbitrary
compound stripping. 格好 nominal appearance is distinct from independently
attested suitability. 首's primary neck lesson does not deny head or other
separately attested identities. Archaicこのかみ and classical美しい affection/
praise evidence do not establish ordinary modern necessity or frequency.
These broader questions and global uniqueness remain **UNVERIFIED**.

Qualified membership: **1332 runtime objects /1020 words**:
671 N5/211 N4/65 N3/19 N2/54 unlabelled.
Strict progress: **1332 reviewed-current, two excluded reviewed blocked-media
drafts,6944 pending of8278;6946 runtime paths absent**, no partial.
Version `d2bb4ec8e78636e8`; checkpoint authority null/Ready false.
All1312 baseline RAWs/tracking rows and protected excluded033空 are preserved.
Ten source wrappers retained/16 unavailable optional wrappers unwrapped;
no source-only provider forced into runtime.
Signed main integration, actual public archives and exact-main CI are separate
publication evidence, not report claims. No new asset/app/device/phone/IME/
media/default/package/release approval.
Continue every remaining safe frozen level/family; 空 remains separately
pending/C2 UNVERIFIED, not a third media draft.

## Prior source milestone: batch054 meals, cooking and flavours

Batch054 adds **20 complete N4 lessons /1024 Russian lines** against unchanged
frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual single independent report](translation-batches/054-meals-cooking-and-flavours-independent-review-001.json)
actually read **179 complete teaching bodies**:20 primary complete EN/RU
pairs,60 contextual complete EN/RU pairs and19 source-only EN comparisons;
196 whole official objects, all1000 actual candidate captions/readings
and nine stored bounded public returns.
C1/C3 are CLEAN within the assigned correctness/Russian-prose scope.
C2 is CLEAN for the assigned dependencies and **all35 individually retained
conservative direct guards**; there are no findings, withdrawals or unresolved
guard IDs. This is not a second review, invented repair or fresh1000-baseline-body
rereading. Ordinary modern necessity/frequency and broader global uniqueness
remain **UNVERIFIED**.

The actual source evidence preserves 一杯 state/serving distinctions,
上手い i-adjective and exact甘い/うまい spelling identity,
separate 味 adjective/み noun-counter/suffix domains,
specialized payment senses and 焼ける independent/potential forms.
米/metre retains its rare-spelling limit; grain/prepared-rice,
generic/specific captions and psychological苦い protections remain qualified,
not universal Japanese equivalences or a transitive food/negative-state clique.
The generated Weblio味な examples and failed焼ける fetch are not lexical proof.
No phonetic spelling is promoted into historical-origin proof.
The genuine signed pre-writing freeze preceded all20 complete learner writes;
the reviewed teaching bodies and metadata are unchanged.

Qualified source membership: **1312 runtime objects /1000 words**,
including671 N5/191 N4/65 N3/19 N2/54 unlabelled.
Strict accounting: **1312 reviewed-current, two excluded reviewed runtime-
blocked media drafts,6964 pending of8278;6966 runtime paths absent**, no partial.
Version `45b56afd82c797ad`; checkpoint authority null/Ready false.
All1292 baseline RAWs/tracking rows and historical reports are preserved.
Nine source navigation wrappers are retained;14 unavailable optional wrappers
are unwrapped without losing Japanese facts or forcing absent providers.
Signed main integration, actual public archives and exact-main CI are separate
publication evidence, not established by this linguistic report.
No new assets/app/device/phone/IME/media/default/release approval.
Continue every remaining safe frozen level/family; protected excluded033空
remains the only N5 pending/C2 UNVERIFIED word, not a third media draft.

## Prior source milestone: batch053 housing and overnight routines

Batch053 adds **20 complete N4 lessons /1068 Russian lines** against unchanged
frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual single independent report](translation-batches/053-housing-overnight-stays-and-household-routines-independent-review-001.json)
read **201 assigned complete teaching bodies plus two consequential bath bodies**,
208 assigned plus one additional complete official entry, and all980 actual
candidate captions/readings. C1/C3 found no actionable defect within the
assigned change scope; this is not native or learner-outcome certification.
Original **C2 CHANGES REQUIRED** and all five findings remain immutable.
The [exact metadata-only resolution](translation-batches/053-housing-overnight-stays-and-household-routines-finding-resolution-001.json)
withdraws Q7二階建て–ビル, Q20忘れ物–忘れる,
Q21忘れ物–無くす and Q35塵–少し, and adds the independently
prescribed direct 湯–お風呂 protection.
**All20 complete teaching bodies remain identical**.
The final45 individually qualified guards comprise44 explicitly retained
proposals and one prescribed addition, not transitive bath/building closure.
Withdrawals do not invent a Japanese minimum-floor rule, 忘れ物する,
or an obligatory host for the usualちり pattern.
Separate田舎/でんしゃ rural-house evidence retains its reading/domain limit;
it does not establish ordinary modern N4 necessity/frequency.
The original47-proposal freeze and Q48 supplement remain historical;
the supplement preceded its metadata, not all initial body writing.
No second review or fresh980-baseline-body rereading is invented.
Broader whole-pool uniqueness and ordinary modern necessity/frequency
remain **UNVERIFIED** outside the actual bounded judgment.

Membership: **1292 runtime objects /980 words**, including671 N5/171 N4/
65 N3/19 N2/54 unlabelled. Only protected excluded033空 remains from N5.
Strict accounting: **1292 reviewed-current, two excluded reviewed runtime-
blocked media drafts,6984 pending of8278;6986 runtime paths absent**, no partial.
Version `74cedfd0a5a1228e`; checkpoint authority null/Ready false.
All1272 baseline RAWs/tracking rows and historical reports are preserved.
Final checks, signed integration, actual public archives and exact-main CI
are recorded separately. No new asset/app/device/IME/media/default/release approval.
Source-only comparisons do not force absent providers into runtime.
Continue every remaining safe frozen level/family; 空 stays separately
pending/C2 UNVERIFIED, not a third media draft.

## Prior source milestone: batch052 household tools and daily living

Batch052 adds **20 complete N4 lessons /1080 Russian lines** against unchanged
frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual independent report](translation-batches/052-household-tools-and-daily-living-independent-review-001.json)
read20 primary and50 contextual complete EN/RU pairs plus30 source-only
comparisons, then the complete guitar pair (**172 teaching bodies**);
172 bound plus one additional complete official entry, and all960 actual
candidate captions/readings. C1/C3 are PASS within the20 primary lessons.
Original **C2 CHANGES REQUIRED** remains immutable. The
[exact metadata-only repair](translation-batches/052-household-tools-and-daily-living-finding-resolution-001.json)
adopts the prescribed direct protections 引き出し–荷物 and道具–ギター.
**All20 complete teaching bodies remain identical**;
29 originally qualified safeguards plus two prescribed additions are adopted.
The newly obtained complete named Ожегов–Шведова entry supports figurative
Russian «багаж»; earlier literal-only returns and other-dictionary lists did not.
The guitar guard uses direct «инструмент» caption fit, not an instrument-family clique.
大事–大丈夫 retains its Tochigi-dialect-only qualification;
ordinary N4 necessity/frequency remains UNVERIFIED.
大事/大切 exact-caption deduplication does not equate all Japanese senses.
ガラス's reading warning does not deny separateグラス material usage.
The pre-bedding amendment preserves蒲団 rarity without unsupported chronology.
No second review, transitive closure or fresh940-baseline-body rereading is invented.
Broader whole-pool uniqueness, 暖房–ストーブ fit and ordinary modern
necessity/frequency remain **UNVERIFIED**.

Membership: **1272 runtime objects /960 words**, including671 N5/151 N4/
65 N3/19 N2/54 unlabelled. Only protected excluded033空 remains from N5.
Strict accounting: **1272 reviewed-current, two excluded reviewed runtime-
blocked media drafts,7004 pending of8278;7006 runtime paths absent**, no partial.
Version `57fedd851a2005e0`; checkpoint authority null/Ready false.
All1252 baseline RAWs/tracking rows and historical reports are preserved.
Final checks, signed integration, actual public archives and exact-main CI
are recorded separately. No new asset/app/device/IME/media/default/release approval.
Source-only comparisons do not force absent providers into runtime.
Continue every remaining safe frozen level/family; 空 stays separately
pending/C2 UNVERIFIED, not a third media draft.

## Prior source milestone: batch051 workplaces, roles and arrangements

Batch051 adds **21 complete N4 lessons /1136 Russian lines** against unchanged
frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual independent report](translation-batches/051-workplaces-roles-and-arrangements-independent-review-001.json)
read21 primary and35 contextual complete EN/RU pairs plus14 source-only
comparisons, then two additional complete pairs (**130 teaching bodies**);
124 bound plus two additional complete official entries, and all940 actual
candidate metadata rows. C1/C3 are CLEAN within the21 lessons.
Original **C2 NEEDS FIX** remains immutable. The
[exact bounded repair](translation-batches/051-workplaces-roles-and-arrangements-finding-resolution-001.json)
adopts five prescribed direct protections: 仕方–手/パーティー
and受付–手/道/パーティー, and the prescribed reading
泳ぎ方（およぎかた）. Twenty bodies remain identical;
all other仕方 teaching bytes remain identical.
**38 originally qualified protections plus five prescribed additions**
are adopted. Optional Q32用事–約束 is deliberately not adopted for lack
of independent caption-fit support, not independently rejected:
its underlying fit remains **UNVERIFIED**, not automatically disproved.
The受付–道 protection retains medium confidence.
Exact shared captions for課長/部長 and用意/準備/支度 follow the existing
deduplication contract, not universal Japanese equivalence.
No second review, transitive closure or fresh full-baseline rereading is invented.
Broader caption-fit questions, whole-pool uniqueness and ordinary modern
necessity/frequency remain **UNVERIFIED**.

Membership: **1252 runtime objects /940 words**, including671 N5/131 N4/
65 N3/19 N2/54 unlabelled. Only protected excluded033空 remains from N5.
Strict accounting: **1252 reviewed-current, two excluded reviewed runtime-
blocked media drafts,7024 pending of8278;7026 runtime paths absent**, no partial.
Version `a38ee7bed6b39b87`; checkpoint authority null/Ready false.
All1231 baseline RAWs/tracking rows and historical reports are preserved.
Final checks, signed integration, actual public archives and exact-main CI
are recorded separately. No new asset/app/device/IME/media/default/release approval.
Source-only comparisons do not force absent providers into runtime.
Continue every remaining safe frozen level/family; 空 stays separately
pending/C2 UNVERIFIED, not a third media draft.

## Prior source milestone: batch050 communication and polite speech

Batch050 adds **18 complete N4 lessons /950 Russian lines** against unchanged
frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual independent report](translation-batches/050-communication-and-polite-speech-independent-review-001.json)
read18 primary and34 contextual complete EN/RU pairs plus18 source-only
comparisons (**122 teaching bodies**),120 complete official entries and all919
actual candidate metadata rows. C1/C3 are CLEAN within the18 lessons.
Original **C2 NEEDS FIX** remains immutable. The
[exact metadata-only repair](translation-batches/050-communication-and-polite-speech-finding-resolution-001.json)
adopts seven independently prescribed direct guards: 伝える–知らせる,
申し上げる–表現/伝える/知らせる/教える and相談–会議/話す.
All18 complete teaching bodies are identity-preserved.
**37 originally qualified protections plus seven prescribed additions** are
adopted, not a second review or fresh full-baseline body rereading.
POS/suru, register, rare standalone readings/senses and incredulous-question
limits remain binding; the会議 addition retains medium confidence.
Broader caption-fit questions, whole-pool uniqueness and ordinary modern
necessity/frequency remain **UNVERIFIED**. No transitive or register clique.

Membership: **1231 runtime objects /919 words**, including671 N5/110 N4/
65 N3/19 N2/54 unlabelled. Only protected excluded033空 remains from N5.
Strict accounting: **1231 reviewed-current, two excluded reviewed runtime-
blocked media drafts,7045 pending of8278;7047 runtime paths absent**, no partial.
Version `f382ac4c68b299c5`; checkpoint authority null/Ready false.
All1213 baseline RAWs/tracking rows and historical reports are preserved.
Final checks, signed integration, actual public archives and exact-main CI
have separate evidence. No new asset/app/device/IME/media/default/release approval.
Source-only comparisons do not force absent providers into runtime.
Continue every remaining safe frozen level/family; 空 stays separately
pending/C2 UNVERIFIED, not a third media draft.

## Prior source milestone: batch049 disciplines, culture and society

Batch049 adds **13 complete N4 lessons** against unchanged frozen EN
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual independent report](translation-batches/049-disciplines-culture-and-society-independent-review-001.json)
read13 primary,22 contextual and three additional complete EN/RU pairs plus
ten source-only comparisons (**86 teaching bodies**),95 complete official
entries and all901 actual candidate metadata rows. C1 is CLEAN and C3
ACCEPTABLE within the13 lessons. Original **C2 NEEDS_FIX** stays immutable.
The [exact metadata-only repair](translation-batches/049-disciplines-culture-and-society-finding-resolution-001.json)
adopts the six independently prescribed direct guards: 科学–地理/数学/歴史/経済,
歴史–話 and経済–お金. All13 complete teaching bodies are identity-preserved.
**Nine originally qualified protections plus six prescribed additions** are
adopted; no automatic subject clique, transitive closure or second review.
Broader caption-fit questions, whole-pool uniqueness and ordinary modern
necessity/frequency remain **UNVERIFIED**. Rare Russian/Japanese sense and
alternate-reading qualifications in the original report remain binding.

Membership: **1213 runtime objects /901 words**, including671 N5/92 N4/
65 N3/19 N2/54 unlabelled. Only protected excluded033空 remains from N5.
Strict accounting: **1213 reviewed-current, two excluded reviewed runtime-
blocked media drafts,7063 pending of8278;7065 runtime paths absent**, no partial.
Version `de2067e8bc992b38`; checkpoint authority null/Ready false.
All1200 baseline RAWs/tracking rows and historical reports are preserved.
Final checks, signed integration, actual public archives and exact-main CI
have separate evidence. No new asset/app/device/IME/media/default/release approval.
Source-only comparisons do not force absent providers into runtime.
Continue every remaining safe frozen level/family; 空 stays separately
pending/C2 UNVERIFIED, not a third media draft.

## Prior source milestone: batch048 study, reference and school

Batch048 adds **16 complete N4 lessons /800 Russian lines** against unchanged
frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual independent report](translation-batches/048-study-reference-and-school-independent-review-001.json)
read16 primary and28 contextual complete EN/RU pairs plus two source-only
comparisons (**90 teaching bodies**),88 complete official entries and all888
actual candidate metadata rows. C1/C3 are CLEAN within the new lessons.
Original **C2 NEEDS REVISION** remains immutable: Q6教育–練習,
Q16大学生–留学生 and Q19校長–先生 lacked direct caption evidence.
The [exact metadata-only repair](translation-batches/048-study-reference-and-school-finding-resolution-001.json)
withdraws those three proposals and preserves all16 teaching bodies by identity.
**29 individually qualified direct protections** remain; broader whole-pool
uniqueness and ordinary modern necessity/frequency stay **UNVERIFIED**.
No second review or fresh full-baseline body reread is invented.
辞典/辞書/字引 share exact caption `словарь`, with deduplication verified.

Membership: **1200 runtime objects /888 words**, including671 N5/79 N4/
65 N3/19 N2/54 unlabelled. Only protected excluded033空 remains from N5.
Strict accounting: **1200 reviewed-current, two excluded reviewed runtime-
blocked media drafts,7076 pending of8278;7078 runtime paths absent**, no partial.
Version `070e2559a59b4564`; checkpoint authority null/Ready false.
All1184 baseline RAWs/tracking rows and historical reports are preserved.
Final checks, signed integration, actual public archives and exact-main CI
have separate evidence. No new asset/app/device/IME/media/default/release approval.
Source-only探す/音 and six exploratory disciplinary/translation roots were
not forced into048. Continue every remaining safe frozen level/family;
空 stays separately pending/C2 UNVERIFIED, not a third media draft.

## Prior source milestone: batch047 safe N5 text closure

Batch047 adds **12 complete N5 lessons** against the unchanged frozen EN
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The [actual independent report](translation-batches/047-n5-safe-text-closure-independent-review-001.json)
read all12 primary and25 contextual complete EN/RU pairs (**74 bodies**),
87 complete official entries and all872 actual caption/metadata rows.
C1/C3 are CLEAN within the new lessons. Original **C2 NEEDS FIX** remains
immutable: R047-1 prescribes directあの–あれ andあの–それ protections.
The [exact metadata-only repair](translation-batches/047-n5-safe-text-closure-finding-resolution-001.json)
adopts those independently assessed pairs and preserves all12 teaching bodies
by identity. It is not a second review or a fresh whole-pool body reread.
**19 individually qualified direct protections** are adopted; broader whole-pool
uniqueness and ordinary modern necessity/frequency remain **UNVERIFIED**.
字引–辞書 is exact-caption-deduped, not an omitted required provider.

Membership: **1184 runtime objects /872 words**, including **671/672 N5 words**.
Only the separately protected excluded033空 remains from N5; all other safe
frozen levels/families still require continued sequential authoring.
Strict accounting: **1184 reviewed-current, two excluded reviewed runtime-
blocked media drafts,7092 pending of8278;7094 runtime paths absent**, no partial.
Version `1ba71a9ba5033842`; checkpoint authority null/Ready false.
All1172 baseline RAWs/tracking rows and historical reports remain unchanged.
Final checks, signed integration, actual public archives and exact-main CI
have separate evidence. No new asset/app/device/IME/media/default/release approval.
空 remains pending/C2 UNVERIFIED, not a third media draft.

## Prior source milestone: batch046 time, sequence and positions

The owner's explicit 2026-11-06 restart instruction supersedes only the
temporary pause recorded in046; the frozen source and all evidence/release
protections are unchanged. Batch046 adds **16 complete N5 word lessons**.
The [actual whole review](translation-batches/046-time-sequence-positions-independent-review-001.json)
read62 assigned complete EN/RU pairs plus向こう,124 complete official entries,
860 actual captions and all16 new lessons. Its original C1/C3 CLEAN and
C2 NEEDS REVISION remain immutable. The
[actual focused review](translation-batches/046-time-sequence-positions-independent-review-002.json)
read nine complete pairs,11 complete entries and three localized RU rubrics;
this is not a second whole review. Body identity carries the original16-body
assessment forward, not fresh semantic reading of the whole pool.

The missing先–向こう protection is resolved. Four unsupported stronger
proposals are withdrawn, not retrospectively CLEAN. The historical bad-rubric-
hash diagnosis is withdrawn: original hashes were correct for RU; the reader
selected the EN root. The actual reader-domain bug is resolved without
rewriting originals. **One preserved source pair plus54 individually qualified
conservative protections** are adopted. The retained51 have original qualified
support, not a fresh51-pair pass. New先–最近 and今–先 guards retain the rare
standalone written先/さっき qualification. **Broader semantic quiz suitability
and ordinary modern necessity/frequency remain UNVERIFIED**, not global CLEAN.

Membership: **1172 runtime objects /860 words**, including **659/672 N5 words;
13 remain**:12 other safe candidates and the separately protected空.
Strict accounting: **1172 reviewed-current, two excluded reviewed runtime-
blocked media drafts,7104 pending of8278;7106 runtime paths absent**, no partial.
Version `982dcba7f94b15a8`; checkpoint authority null/Ready false.
All1156 baseline RAWs/tracking rows and historical receipts remain unchanged.
Final checks, signed integration, public archives and exact-main CI have
separate evidence. No new app/media/device/default-activation/release approval.
Excluded033空 remains pending/C2 UNVERIFIED, not a third media draft.
Continue047 and all independent safe frozen levels/families after046 integration.

## Prior source milestone: batch045 body, health and safety

Batch045 adds **13 complete N5 word lessons** against unchanged frozen
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
[Actual review](translation-batches/045-body-health-safety-independent-review.json)
and [reviewed source](translation-batches/045-body-health-safety-reviewed-source.json)
record one whole read-only review of **46 complete EN/RU pairs /92 bodies,
129 complete official entries,844 actual captions and one complete named
Russian dictionary entry**. All648 new Russian lines were read.
C1/C3 are CLEAN within the new lessons; C2 adopted coverage/dependencies are
CLEAN and all **20 individually qualified direct protections** are supported.
**Broader semantic quiz suitability remains UNVERIFIED**, not silently CLEAN.
The unadopted 死ぬ–終わる and 頭–精神/心 hypotheses have neither established
universal safety nor an established mandatory additional exclusion.
Stronger modern necessity/frequency of all20 remains UNVERIFIED/unasserted.
No transitive body, people or adjective cliques are endorsed.

The actual public stdout report payload,7681 UTF-8 bytes, matches the
independently returned base64 payload and persisted final message content.
Report-payload, wrapper, journal-record and network-wire hash domains remain
distinct. The three-line method clarification was independently assessed.
Japanese medical-language examples are not diagnosis, dosage or treatment advice.
The irregular disease spelling 風 is qualified; 風邪 keeps both metadata kanji
without inventing a kanji/邪.md card outside the frozen target.

Membership: **1156 runtime objects /844 words**, including **643/672 N5 words;
29 remain**; other word levels:63 N4/65 N3/19 N2/54 unlabelled.
Fresh strict accounting: **1156 reviewed-current, two excluded reviewed
runtime-blocked media drafts,7120 pending of8278;7122 runtime paths absent**,
no partial. Version `820f471d66840ea7`; checkpoint authority null/Ready false.
Actual final checks, signed integration, public archives and exact-main CI
have separate evidence. All1143 baseline RAWs/tracking rows and historical
receipts remain unchanged.

No new assets or app/ordinary EN/device/media/default-activation/release approval.
Canonical life/occupation/safety mapping gaps are observed only at immutable
app5c000bd; live concurrent app status remains UNVERIFIED and untouched.
Excluded033 空 remains pending/C2 UNVERIFIED, separate from the two media drafts.
Later genuine native findings may require affected-batch correction and review;
continue046 and every independent safe frozen level/family.

## Prior source milestone: batch044 arts, music and media

Batch044 adds **16 complete N5 word lessons** against unchanged frozen
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
[Actual review](translation-batches/044-arts-music-media-independent-review.json)
and [reviewed source](translation-batches/044-arts-music-media-reviewed-source.json)
preserve the genuine whole **40 complete EN/RU pairs /59 complete official
entries /831 actual captions** review: C1/C3 CLEAN, C2 NEEDS_FIX.
A sequential focused **eight-pair/eight-entry/three-Russian-primary-entry**
recheck resolves four direct safeguards and the 組 sense-reference erratum,
and assesses three method lines. These are subsets of40/59, not48/67 unique
pairs/entries. All16 complete bodies and831 captions remain unchanged.

The current 組 citation is **1397450:2**; the
[forward erratum](translation-batches/044-arts-music-media-corrective-source-adjudication-001.json)
explicitly supersedes the wrong historical sense1 citation without rewriting
signed receipts. **18 direct protections = four displayed-answer decisions
+14 limited dictionary/context safeguards**; stronger modern necessity/frequency
of the14 remains UNVERIFIED/unasserted. Russian картина/лента polysemy and the
obsolete/specialized physical-film sense retain their actual boundaries.
No transitive picture, material or audio-device cliques are asserted.
The genuine focused report returned through task and exact-ID readback is saved
as an LF transcript; its native-public-event byte identity remains UNVERIFIED.
Successful reader-return evidence is separately captured. A transcript hash is
not represented as a native-return or network-wire hash.

Membership: **1143 runtime objects /831 words**, including **630/672 N5 words;
42 remain**; other word levels:63 N4/65 N3/19 N2/54 unlabelled.
Fresh strict accounting: **1143 reviewed-current, two excluded reviewed
runtime-blocked media drafts,7133 pending of8278;7135 runtime paths absent**,
no partial. Version `2feceed6354d1b68`; checkpoint authority null/Ready false.
Actual final checks, signed integration, public archives and exact-main CI
have separate evidence. All1127 baseline RAWs/tracking rows and historical
receipts remain unchanged.

No new assets or app/ordinary EN/device/media/default-activation/release approval.
Canonical art/audio/equipment/office/sound mapping gaps are observed only at
immutable app5c000bd; live concurrent app status remains UNVERIFIED.
Excluded033 空 remains pending/C2 UNVERIFIED, separate from the two media drafts.
Later genuine native findings may require affected-batch correction and review;
continue045 and every independent safe frozen level/family.

## Prior source milestone: batch043 food, tableware and objects

Batch043 adds **16 complete N5 word lessons** against unchanged frozen
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
[Actual review](translation-batches/043-food-tableware-objects-independent-review.json)
and [reviewed source](translation-batches/043-food-tableware-objects-reviewed-source.json)
preserve the genuine whole **40 complete EN/RU pairs /47 complete official
entries /815 actual captions** review: C1/C3 CLEAN, C2 CHANGES REQUIRED.
A sequential focused **two-pair/two-entry** recheck resolves the direct
ちゃわん–カップ ambiguity and supports two new method lines. Those readings
are subsets of40/47, not42/49. All16 bodies and815 captions are unchanged.

The focused report's separate provenance finding is retained, not relabelled:
its stale premise is adjudicated against the subsequently persisted actual
public tool-result event. The preserved12253-byte UTF-8 report has the recorded
SHA256; this proves public returned-text bytes, not network-wire bytes.
[Exact provenance adjudication](translation-batches/043-food-tableware-objects-provenance-adjudication-001.json)
records the evidence and requester correction without another linguistic review.
**Seven direct protections = four taught/caption decisions +three limited
dictionary/context safeguards**; stronger modern necessity/frequency of the
three remains UNVERIFIED/unasserted. No transitive vessel or food cliques.

Membership: **1127 runtime objects /815 words**, including **614/672 N5 words;
58 remain**; other word levels:63 N4/65 N3/19 N2/54 unlabelled.
Fresh strict accounting: **1127 reviewed-current, two excluded reviewed
runtime-blocked media drafts,7149 pending of8278;7151 runtime paths absent**,
no partial. Version `5bd14414dcad4e99`; checkpoint authority null/Ready false.
Signed integration, actual public archives and exact-main CI have separate evidence.
All1111 baseline RAWs/tracking rows and historical receipts remain unchanged.

No new assets or app/ordinary EN/device/media/default-activation/release approval.
Canonical `dining`/`object`/`utensil` mapping gaps are observed only at immutable
app `5c000bd`; live concurrent app status remains UNVERIFIED.
Excluded033 空 remains pending/C2 UNVERIFIED, separate from the two media drafts.
Later genuine native findings may require affected-batch correction and review;
continue044 and every independent safe frozen level/family.

## Prior source milestone: batch042 travel, movement and places

Batch042 adds **18 complete word lessons: 16 N5 roots and two required N4
providers** against unchanged frozen `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
[Actual review](translation-batches/042-travel-movement-places-independent-review.json)
and [reviewed source](translation-batches/042-travel-movement-places-reviewed-source.json)
preserve the genuine whole **62 complete EN/RU pairs /799 compact captions /
123 complete official entries /51 proposals** review: C1/C3 CLEAN, C2 NEEDS FIX.
A fresh, strictly sequential focused reviewer reads **17 complete pairs,
18 complete entries, all799 captions, ten additions and four withdrawals**.
Those pairs/entries are subsets of the original62/123, not79/141 unique units.
The ten missing safeguards are resolved, four disputed proposals withdrawn,
and six new method lines independently assessed. All18 complete learner bodies
and titles, and1093 accepted baseline RAWs/tracking rows, remain unchanged.

**57 direct protections = two source edges +17 direct taught/caption decisions
+38 limited dictionary/context safeguards.** Stronger ordinary modern
necessity/frequency of all38 remains UNVERIFIED and unasserted.
Possible 差す–輝く and 国–外国 overlap remains explicitly UNVERIFIED;
no necessary additional guard was established in the actual caption boundary.
Neither hypothesis is asserted as an approved claim or universal impossibility.
Secondary senses, spelling restrictions and suffix requirements are not
silently promoted into primary N5 lessons or transitive exclusion cliques.

Membership: **1111 runtime objects /799 words**, including **598/672 N5 words;
74 remain**; other word levels:63 N4/65 N3/19 N2/54 unlabelled.
Fresh strict accounting: **1111 reviewed-current, two excluded reviewed
runtime-blocked media drafts,7165 pending of8278;7167 runtime paths absent**,
no partial. Version `4ee4c7df08855309`; checkpoint authority null/Ready false.
Actual candidate/corrected checks passed; final checks, signed integration,
public archives and exact-main CI have separate publication evidence.

No new assets or app/ordinary EN/device/media/default-activation/release approval.
Canonical `occupations` is preserved; its newly exposed mapping gap is bounded
to immutable app `5c000bd`, with concurrent live-app status UNVERIFIED.
Excluded033 空 remains pending/C2 UNVERIFIED, separate from the two media drafts.
Later genuine native findings can require affected-batch correction and review;
continue every independent safe frozen level/family.

## Prior source milestone: batch041 core actions, making and existence

Batch041 adds **25 complete word lessons: 18 N5 roots and seven required
providers (four N4 and three N3)** against unchanged frozen
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
[Actual review](translation-batches/041-core-actions-making-existence-independent-review.json)
and [reviewed source](translation-batches/041-core-actions-making-existence-reviewed-source.json)
preserve the whole review of **69 complete EN/RU pairs, 781 compact captions,
80 complete query objects and 67 safeguard proposals**.
Its C1/C3 CLEAN, C2 NEEDS FIX verdict remains historical.
A focused four-pair/four-object recheck independently resolves the missing
いる–要る kana-homograph and 上げる–貸す coarse «давать» protections,
and assesses six method lines. The four pairs are inside the original
**69 unique pairs**, not 73. All 25 learner bodies and 781 titles remain unchanged.

**69 direct protections = nine preserved source edges, 17 directly assessed
taught/caption decisions and 43 limited conservative/contextual safeguards.**
Stronger ordinary modern necessity/frequency of all 43 remains UNVERIFIED
and unasserted. Separate readings/homographs are not merged into primary N5 lessons.
Four targeted official JMdict spelling/reading-element sets support rare-form
annotations; this is not full reading of their official sense bodies.
All 1068 previously accepted runtime RAWs and historical tracking rows are preserved.

Membership: **1093 runtime objects /781 words**, including
**582/672 N5 words; 90 remain**. Other word levels:
61 N4/65 N3/19 N2/54 unlabelled. Fresh strict target accounting:
**1093 reviewed-current, two excluded reviewed runtime-blocked media drafts,
7183 pending of 8278; 7185 runtime paths absent**, no partial.
Version `e05eb558300d0602`; checkpoint authority null/Ready false.
Candidate and corrected checks passed; final validation, signed integration,
public archives and exact-main CI have separate evidence.

No new assets or app/ordinary EN/device/media/default-activation/release approval.
Canonical `action`/`auxiliary`/`existence`/`industry`/`infrastructure`/`transfer`
IDs remain unchanged; explicit mapping gaps are observed only at immutable app `5c000bd`.
Excluded033 空 remains pending/C2 UNVERIFIED, separate from the two blocked media drafts.
Later actual native findings can require affected-batch correction and review;
continue every independent safe frozen level/family.

## Prior source milestone: batch040 connectives, frequency and degree

Batch040 adds **25 complete word lessons: 22 N5 roots and three required
providers (たいてい N4; 現実/実際 N3)** against the unchanged frozen
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
[Actual review](translation-batches/040-connectives-frequency-degree-independent-review.json)
and [reviewed source](translation-batches/040-connectives-frequency-degree-reviewed-source.json)
preserve the original whole review: **47 full EN/RU pairs, two EN-only optional
sources, 756 actual compact captions, 55 complete query-object rows and 42 proposals**.
One Wikipedia-only object is not lexical evidence. The original C1/C2/C3 NEEDS FIX
verdict is retained. The focused review reads seven complete pairs and seven
objects, both added protections, the unsupported withdrawal, two corrected
Russian phrases, five method lines and the complete original report.
It resolves the まだ time/stage explanation and two missing よく protections;
the unsupported また–本当 proposal is withdrawn, not upgraded.
All seven focused pairs are inside the original **47 unique pairs**, not 54.

**43 direct protections = 18 source-sense +25 independently accepted limited
conservative/contextual safeguards.** Stronger ordinary modern necessity/frequency
of all 25 remains UNVERIFIED and unasserted. No neutral N5 dialect/rare meanings
or unrestricted synonyms are added. All 1043 previously accepted runtime RAWs
and historical tracking rows are preserved; all 756 actual titles are unchanged
by the corrections.

Membership: **1068 runtime objects /756 words**, including
**564/672 N5 words; 108 remain**. Other word levels:
57 N4/62 N3/19 N2/54 unlabelled. Fresh strict target accounting:
**1068 reviewed-current, two excluded reviewed runtime-blocked media drafts,
7208 pending of 8278; 7210 runtime paths absent**, no partial.
Version `20947276cf78bbe5`; checkpoint authority null/Ready false.
Actual candidate/corrected checks passed; final validation, signed integration,
public archives and exact-main CI have separate publication evidence.

No new assets or app/ordinary EN/device/media/default-activation/release approval.
Canonical `concepts`/`conjunction`/`frequency`/`reality`/`sequence` IDs remain unchanged;
their explicit mapping gap is observed only at immutable app `5c000bd`.
The excluded full033 空 draft stays pending/C2 UNVERIFIED, separate from the
two reviewed blocked media drafts. Later real native findings may require
affected-batch corrections; continue every independent safe frozen level/family.

## Prior source milestone: batch039 questions, address and responses

Batch039 adds **18 complete N5 word lessons** against the unchanged frozen
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`, not a new pilot limit.
[Actual review](translation-batches/039-questions-address-responses-independent-review.json)
and [reviewed source](translation-batches/039-questions-address-responses-reviewed-source.json)
preserve the original whole review: 39 full EN/RU pairs, 731 compact captions,
50 complete query-object rows and 32 proposed protections, plus narrow additional
嫌 evidence. C1/C3 were CLEAN; C2 needed seven direct protections.
The separately recorded focused review reads all 11 affected/endpoint pairs,
eight complete objects, seven additions, the full original report, one improved
Russian apology and five methodological lines. All seven limited additions are
accepted; the original C2 NEEDS FIX report is not rewritten.
The cumulative unique bilingual evidence is 40 pairs, not 39 plus 11 new pairs.

**39 direct protections = 17 ordinary-sense decisions + 22 independently accepted
conservative/contextual safeguards.** Ordinary modern necessity/frequency of the
22 conservative safeguards remains UNVERIFIED and unasserted. Their limited
adoption does not add neutral N5 dialect/archaic senses or unrestricted synonyms.
All 1025 previously accepted runtime RAWs and historical tracking rows are preserved;
all 731 actual titles remain unchanged by the seven corrections.

Membership: **1043 runtime objects /731 words**, including
**542/672 N5 words; 130 remain**. Other word levels remain
56 N4/60 N3/19 N2/54 unlabelled. Fresh strict target accounting:
**1043 reviewed-current, two excluded reviewed runtime-blocked media drafts,
7233 pending of 8278; 7235 runtime paths absent**, no partial.
Version `cdf164e767e453ad`; checkpoint authority null/Ready false.
Candidate and corrected-candidate manifest/validator/124 tests/budget passed;
final checks, signed main integration, actual public archives and exact-main CI
have their own evidence, not an implied device result.

No new assets or app/ordinary EN/device/media/default-activation/release approval.
`interjection`, `polite`, `request` remain canonical technical IDs;
mapping fallback is observed only at immutable app `5c000bd`.
The excluded full033 空 draft remains pending/C2 UNVERIFIED, separate from the
two reviewed blocked media drafts. Later real native findings may require
affected-batch corrections; continue every independent safe frozen level/family.
Older milestones and pilot-baseline counts below are historical.

## Frozen scope and present state

The owner's 2026-11-04 request is to review and execute the remaining roadmap, not
another arbitrarily small pilot. The target is **every runtime object in the current
English edition**, not a claim that the English edition itself completes the JLPT syllabus.
Freeze EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f` before the next work; later English
changes are drift, not moving inputs to an in-flight translation.
RU baseline is `4d84c90f7cffa70b5ee1e296595d5cc7ce306f6f`;
app baseline is `5c000bd5596d2189ef878da572687bd01ab3bb5f`.

| Family | Frozen EN objects | RU objects at pilot baseline |
| --- | ---: | ---: |
| Kanji | 1,062 | 12 |
| Words | 5,020 | 47 |
| Articles | 57 | 2, both deliberately scoped |
| Counter files | 138 | 2; legacy reverse rows deliberately omitted |
| Grammar sets | 88 | 1 |
| Curriculum catalogs | 1 | 0 |
| Word scene catalogs | 201 | 2 |
| Legacy listening passages | 36 | 0 runtime; one reviewed text draft |
| Japanese listening tasks | 40 | 0 runtime; one reviewed text draft |
| Stroke files | 1,062 | 12 |
| Word images | 398 | 3 |
| Legacy audio | 36 | 0 |
| Task audio | 128 | 0 |
| Task images | 11 | 0 |
| **Total** | **8,278** | **81** |

At that pilot baseline, 8,197 target paths were absent; presence does not establish full translation:
the two articles and legacy counter unit retain explicit partial coverage. Source kanji
levels are N5 80 / N4 166 / N3 367 / N2 367 / N1 82; word levels are
N5 672 / N4 636 / N3 1,625 / N2 1,739 / N1 2, with 346 intentionally unlabelled.
Do not infer levels for those words or invent missing upstream N1 coverage.

The complete 81-object pilot stage is independently reviewed for its adopted scope;
its original sources remain A `3196c3a...` and B `5f460b8...`, not this new target.
Preserve the old provenance/review files as historical records. A new source inventory,
tracking ledger and drift report must not relabel old work as newly translated.

## Remaining work and dependency order

1. **R0 — reconcile scope and guidance.** Inventory every manifest map and every active
   instruction/agent, including changed `applyTo` and normative references. Compare the
   fresh frozen source against both pilot sources. Independent plan review precedes new
   implementation. This inventory is not linguistic approval or a synchronization tag.
2. **R1 — finish the manual provenance loop (RU #2).** Add deterministic read-only
   fixed-revision inventory/drift/checkpoint checks, with focused tests. Track added,
   changed, removed/renamed, untranslated, RU-modified and partial objects separately.
   Preserve RU-specific adaptations and immutable old receipts. Every review record binds
   exact source and Russian hashes plus evidence; matching bytes do not create approval.
   A checkpoint rejects unresolved adopted objects and guidance. Prove a reproducible
   real two-snapshot report before considering optional scheduled automation.
3. **R2 — finish or explicitly block C6 operations (RU #6).** Five genuinely unlocked
   native Word Type paths have [already passed](https://github.com/stop-cran/learning-japanese-ru/issues/6#issuecomment-6633295530);
   additional targets still need their real reverse prerequisite. Legacy counter suffix/full typing needs a second real
   Choose day. Do not change clocks, gates or saved state. Both reviewed Russian audio
   adaptations need fresh exact-package authority before runtime publication and genuine
   playback/interruption acceptance. Prepare exact binding evidence without inventing
   approval or regenerating paid media.
4. **R3 — C7 owner-device/release acceptance.** APK `0293a7ba...`, built from app `5c000bd`,
   was copied to the physical phone and fully read back over MTP on 2026-11-04.
   This is delivery, not installation, Japanese-IME, playback or phone approval.
   Preserve the applicable API29/API35/enlarged-text/source/history acceptance matrix.
   Ordinary RU defaults remain disabled until the required gates pass.
5. **R4 — translate the complete inventory (RU #3).** The owner's subsequent
   2026-11-04 authorization starts authoring now, without waiting for C6/C7 device
   acceptance; those gates still govern release/activation and restricted media packages.
   Execute coherent dependency-closed batches, starting with remaining N5 kanji/words,
   then N4/N3/N2/N1 and unlabelled words; complete all articles, counters, grammar and
   curriculum alongside the units they support. Scenes/media/listening are separate
   exact-package lanes, never omitted from the backlog. A batch closes required examples,
   direct negative references, prerequisites and licensed media before authoring; optional
   navigation does not recursively force the whole corpus into one review.
6. **R5 — review, integrate and advance only warranted checkpoints.** Independently review
   all learner-facing branches for Japanese correctness, actual adopted coverage and
   Russian comprehensibility; adjudicate, correct and re-review affected material.
   Run the actual validators, vocabulary reviews, budgets, manifest and real-reader/native
   gates. Recheck all combined-tree Russian option ambiguity, canonical app hint vocabulary
   and source-bound history. Exact reused Japanese bytes retain licenses, not RU approval.
7. **R6 — maintain alignment.** A tested manual cycle may later support a least-privilege
   report-only Action. No report self-translates, self-approves, merges, advances immutable
   tags or affects offline study. New upstream content remains pending until adopted.

The later authorization removes C6/C7 as a prerequisite to translation authoring.
It does not authorize paid media, fabricated phone acceptance, transfer of audio-package
approval or ordinary RU activation. Reviewed text batches may be integrated while the
separate release gates remain open.
The official `ru-pilot-a` and controlled `ru-pilot-b` runtime pins remain unchanged.

## Completion evidence

Full translated-corpus coverage means every frozen target object has a complete reviewed Russian unit
or an explicit justified non-translatable asset disposition, all necessary dependencies
are closed, and all changed guidance/source semantics are reconciled. Runtime publication
of restricted packages and release/activation additionally require their applicable
authority/device gates. Report translated text, runtime parity and release readiness
separately. Partial articles, blocked drafts, absent files, copied English
prose, hashes and a generated manifest cannot satisfy that definition.

Current work items remain the authority for outstanding acceptance: RU #2 provenance,
RU #3 staged corpus, RU #5 integration, RU #6 structured/media pilot, and app #28.
Keep the historical C0–C7 evidence in IMPLEMENTATION-PLAN; update its current summary,
not the old reports. Record each verified tooling/method finding in active instructions.

## Manual provenance commands

From the RU root, with an isolated clone containing the two immutable source commits:

```powershell
python tools\translation_progress.py inventory --upstream <EN-clone> --revision 5f460b85b391404e7da01be0a0cded78243b7538 --output <artifacts>\before.json
python tools\translation_progress.py inventory --upstream <EN-clone> --revision 6af98cb717755690a9ca793e5454a96ebd7a8f9f --output <artifacts>\after.json
python tools\translation_progress.py report --before <artifacts>\before.json --after <artifacts>\after.json --ledger docs\translation-tracking.json --output <artifacts>\progress-next.json
python tools\translation_progress.py checkpoint --before <artifacts>\before.json --after <artifacts>\after.json --ledger docs\translation-tracking.json --scope <reviewed-paths.json> --output <new-checkpoint.json>
```

Outputs must be new paths: old receipts/checkpoints are never overwritten. After reviewing a
fresh report, explicitly replace the mutable current `docs/translation-progress.json` and
commit that update. Inventory hashes actual Git blobs against every manifest entry, including
raw binary/stroke identity; an uncommitted EN worktree cannot silently retarget it.
Checkpoint recomputes the current RU tree and manifest instead of trusting an old report.
It needs a nonempty explicit adopted scope, complete current review, reconciled guidance,
the exact batch target and an explicit human authority record. It records exact source/RU
hashes; it is not release approval. Renames are candidates, never automatic identity/review moves.
Changed English-only prose still expires review even when the invariant projection is unchanged.

`translation-tracking.json` retains the 51 Pilot A and30 Pilot B runtime review records and
two separately blocked audio text reviews without rewriting the historical ledgers.
Its `checkpointAuthority` remains null. No tag or checkpoint is advanced by this inventory.

## Verified execution checkpoint: 2026-11-04

R0/R1 are implemented and independently accepted, not merely planned.
[Review and regression record](full-translation-review.json) separates the initial
NEEDS FIX finding from its accepted correction: raw literal and escaped-equivalent
duplicate JSON keys now fail before decoding can collapse them. The real suite passes
124 tests with no failures, errors or skips; the actual RU validator reports zero errors.
Both immutable full inventories still regenerate exactly. The final manual report is
byte-reproducible, SHA256
`e9e549154fb17af30bab3ca7f66fa714fa8d0ac6129fcb4744428f26fdc88f28`.
It detects six added/four modified source paths, none in the adopted runtime stage.
All three changed guidance dispositions since C2 are independently accepted.
Current statuses remain 78 reviewed-current / three partial / two reviewed runtime-blocked
drafts / 8,195 pending. The actual checkpoint CLI still exits 1 and creates no checkpoint.
Runtime bytes, old provenance and both reviewed audio drafts remain unchanged.

The owned API29 lab also completed a previously missing C6 path on the exact signed
`0293a7bab3e5e0ad752e15c822c610b11d9fc2c4cc5a45de27ca31bfa3125bde` APK.
Its runtime was the authorized `stop-cran/learning-japanese-ru-integration-test`
`ru-pilot-b` at `7ce81c74e72fc189185a1bebe71d775379792124`,
content version `24362f736bc17328`, not the complete new EN target or ordinary RU main.
Four real ten-question Russian-to-Japanese extra-practice sessions earned reverse
memory normally; no clock, database, gate or daily limit was changed. Five words then
actually opened Word Type. Their reverse records are Review/reps 4/stability
2.7899488574439086 days; three correct answers on other words still yield
1.9818197930436123 days, below the unchanged two-day gate.
The actual five-question Word Type session passed 5/5, including Russian canonical
metadata labels, automatic field focus and visible IME before each helper input,
correct feedback and committed Next records.
The five actually typed words were ぺらぺら, きらきら, つやつや, つるつる and ぬるぬる;
this is not all 13 onomatopoeia words.
Every original 36 state / 90 log / 18 session row remains unchanged; legitimate new
practice yields 53 / 135 / 23. This is native UI/history evidence, not proof of
learning effectiveness or Japanese-keyboard acceptance: the lab retained its existing
Latin IME and used the disclosed input-only helper.
The lab was restored through normal validated Settings to official RU `ru-pilot-a`
at `544dd15f...`, explicit Russian, N5 and the original effective daily limit of 10.
The final private snapshot retains every original and legitimate new learning row.
The helper and 155 individually resolved remote XML files were removed, adbd was
returned to UID2000, and only the verified owned emulator was stopped; its ports closed.

Remaining R2/R3 blockers are still real: a second distinct CounterChoose day,
fresh exact-package authority for both Russian audio adaptations followed by actual
playback/interruption tests, and physical-phone/Japanese-IME/release acceptance.
[The exact authority request](pilot-b-media-authority-request.json) is prepared, not
approved. Ordinary RU activation and broad R4 authoring have not been unlocked.
At that checkpoint the complete 8,197 absent-path backlog plus partial units remained visible; this
checkpoint is not a claim that the full corpus has been translated.

## Subsequent owner authorization: sequential background authoring

The owner subsequently requested continuous background translation against the **same**
`6af98cb717755690a9ca793e5454a96ebd7a8f9f` target. ETA is not a constraint.
The earlier R2/R3 observations remain historical evidence, not a reason to idle the
independent text lane. Translate restricted listening packages as non-runtime drafts
until their actual publication authority is obtained; continue other families meanwhile.

Use one authoring lane and at most one read-only reviewer at a time, with serialized
tests/builds; do not launch fleets, extra authoring sessions or unattended competing writers.
Freeze convenient dependency-closed batches before authoring, review every adopted
learner-facing surface, resolve and recheck findings, then validate the combined tree.
Update exact per-file provenance and the mutable current report without rewriting old receipts.

Keep branches short-lived: pull/fetch before each batch and before integration, reconcile
concurrent work without overwriting it, commit recoverable progress periodically and push
without asking for confirmation. Use normal signed commits and normal pushes, never
force-push, amend or discard unrelated work. Integrate accepted batches frequently;
unreviewed WIP remains explicitly unaccepted on its own branch or excluded draft lane.
Record each completed batch and actual remaining scope so interrupted work can resume
without repeating, losing or falsely approving it. Do not silently retarget to later EN main.

## Reviewed source batches

Batch **001 — demonstratives** completes 23 full word articles from the frozen target:
20 retain N5, two retain N4 and one retains N3. All Japanese examples, readings, source
senses and qualifications survive. An independent complete three-facet review identified
Russian answer-label overlap; an independent narrow recheck accepted exactly 30 additional
direct pairs, with all earlier pairs preserved and no transitive expansion.
[Exact source/Russian hashes and review boundaries](translation-batches/001-demonstratives-review.json)
remain separate from the unchanged historical pilot receipts and release/device/media gates.
After batch 001, runtime membership was 104 objects; full-target statuses were 101 reviewed-current,
three partial, two reviewed runtime-blocked drafts and 8,172 pending. The 8,174 absent runtime
paths and three partial units remain work, not a completion claim.
Continue the remaining N5 vocabulary/kanji/support batches, then all later levels and families.

Batch **002 — people and family** adds three complete N5 kanji, 23 complete word articles
and three raw-identical KanjiVG stroke files. The dependency-closed family includes 女子/婦人;
all source levels and absent levels remain unchanged. A separately frozen amendment restores
the now-required 休 link in 休日 and includes that whole baseline article in re-review.
One independent reviewer actually read all 27 RU/EN learner pairs and all 23 captured dictionary
queries; Japanese correctness, actual adopted coverage and Russian comprehensibility are CLEAN
for this bounded scope, with no findings. The 32 direct answer pairs have individual evidence;
exact matching titles deduplicate without inventing transitive exclusions.
[Exact candidate hashes, actual scope and limits](translation-batches/002-people-family-review.json)
remain distinct from device, activation and restricted-media authority.

After batch 002, runtime membership was **133 objects**: 15 kanji, 93 words, 15 strokes and the unchanged
other baseline families. Full-target statuses were **130 reviewed-current**, three partial,
two reviewed runtime-blocked drafts and **8,143 pending**; **8,145 runtime paths remain absent**.
Continue the next safe sequential batch; neither this milestone nor source publication completes
the full translation objective.

Batch **003 — kinship and relationships** completes 19 more word articles. One full
independent review found two real quiz ambiguities: 男の子 also means «сын», and 奥さん
has a married-woman address use. An independent narrow recheck accepted exactly six new
direct guards, preserving the original 38 pairs and all learner body facts. The neutral
wife label is «жена другого человека (уважительно)».
[Full review, exact corrections and bounded recheck](translation-batches/003-kinship-relationships-review.json)
separate actual reading from unchanged-body reliance and record all limitations.

After batch 003, runtime membership was **152 objects**: 15 kanji, 112 words, 15 strokes and unchanged
other families. Full-target statuses were **149 reviewed-current**, three partial,
two reviewed runtime-blocked drafts and **8,124 pending**; **8,126 runtime paths remain absent**.
Continue sequential authoring against the same frozen source; release/device/media gates remain.

Batch **004 — entry and exit** completes two N5 kanji, 14 full word articles and two
byte-identical KanjiVG files. Independent full reading of all 16 RU/EN texts and captured
dictionary evidence returned CLEAN on all three facets, including the inherited 入り口
reading-table correction and the bounded Russian ～出す/～始める comparison. The latter is
not adoption of the whole optional source article.
[Exact hashes, actual review scope and limits](translation-batches/004-entry-exit-review.json)
remain separate from public-archive CI evidence and all release/device/media gates.

After batch 004, runtime membership was **170 objects**: 17 kanji, 126 words, 17 strokes and unchanged
other families. Full-target statuses were **167 reviewed-current**, three partial,
two reviewed runtime-blocked drafts and **8,106 pending**; **8,108 runtime paths remain absent**.

Batch **005 — books and study** completes 本, 28 full word articles and one byte-identical
KanjiVG file. The required negative-reference closure added six complete perception/calendar
articles before authoring; no source distractor was discarded to shrink scope.
Independent whole reading of all29 RU/EN texts,31 exact dictionary objects and154 actual
Russian answer labels returned CLEAN on all three facets, with no established finding.
The source-based 生 suffix clarification and six individually justified direct guards are
recorded with exact hashes and real scope/limits in the
[batch review](translation-batches/005-books-study-review.json).

After batch005, runtime membership was **200 objects**: 18 kanji,154 words,18 strokes and unchanged
other families. Full-target statuses were **197 reviewed-current**, three partial,
two reviewed runtime-blocked drafts and **8,076 pending**; **8,078 runtime paths remain absent**.

Batch **006 — listing and examples** completes the previously partial article, preserving all
469 frozen English lines' substantive coverage, examples, distinctions and citations.
The previously reviewed57-line Russian adaptation remains as an explicitly bounded supplement;
its four existing exercises and reviewed vocabulary contexts are unchanged.
Independent whole reading of source,536-line Russian candidate and prior adaptation returned
CLEAN on all three facets. One optional reviewer-proposed phrase now explicitly describes
not eating rather than possible food unavailability; all other article bytes are unchanged.
[Exact full review, optional correction and limited narrow recheck](translation-batches/006-listing-examples-review.json)
distinguish actual reading scope from the terse recheck result.

After batch006, membership remained **200 runtime objects**; full-target statuses became
**198 reviewed-current**, **two partial**, two reviewed runtime-blocked drafts and
**8,076 pending**. The other article and the legacy counter unit still require completion;
**8,078 runtime paths remain absent**. No checkpoint, media authority or release/device gate moved.

Batch **007 — numbers and counters article** completes all856 frozen source lines, preserving
all67 citation URL occurrences and the separately reviewed77-line general-count lesson.
The existing 時間 link remains; only20 genuinely absent optional destinations become plain labels,
without deleting teaching content. Broad practice descriptions and future Grammar navigation
are explicitly distinguished from the currently available Russian exercise sets.
One independent reviewer actually read all987 Russian lines, all856 source lines, all77 prior
Russian lines and the declared normative evidence; all three facets returned CLEAN, no findings.
The original reviewer's exact optional duration phrase was adopted verbatim, with a sole-replacement
proof and real corrected serial checks; no additional post-edit reread is claimed.
[Actual scope, hashes and limits](translation-batches/007-numbers-counters-article-review.json)
do not approve the counter families, grammar exercises or media merely mentioned by the article.

After batch007, membership remained **200 runtime objects**; statuses were **199 reviewed-current**,
**one partial** (`counters/tsu.json`), two reviewed runtime-blocked drafts and **8,076 pending**.
Both formerly partial articles are now complete; **8,078 runtime paths remain absent**.
No frozen pilot ref, checkpoint authority, ordinary activation or device/media/release gate moved.
Continue the finite remaining corpus without retargeting the frozen English revision.

Batch **008 — food, drinks and meals** completes27 full word articles:26 source-classified N5
words and the mandatory direct N4 食事 dependency. One independent reviewer actually read every
complete RU/EN pair, all27 captured dictionary queries/31 objects/73 senses and all181 actual
combined answer labels. A real missing 昼/昼御飯 lunch guard was found from the already taught
meaning in the baseline card's body, despite its different short title.
The guard was added only to the new card; two exact optional wording proposals were adopted.
One bounded independent recheck read all four affected/relevant full pairs, verified all27
current hash records and resolved the finding. Baseline 昼 and the other24 new cards remained
raw-identical. [Actual full reading and corrective closure](translation-batches/008-food-drinks-review.json)
distinguish their respective scopes; no whole-batch reread by the narrow reviewer is claimed.

After batch008, membership was **227 runtime objects**:18 kanji,181 words,18 strokes and unchanged other
families. Statuses were **226 reviewed-current**, **one partial** (`counters/tsu.json`),
**two reviewed runtime-blocked drafts** and **8,049 pending**; **8,051 runtime paths remain absent**.
All earlier tracking records and immutable receipts are preserved; checkpoint authority is null.

An actionable **external app-hint localization gap** is pinned in the008scope: committed
app `5c000bd...` falls back to raw IDs for `food`, `drinks`, `animal`, `polite-prefix`,
`suru-verb`, `meals`—26 occurrences across22 new cards, with some IDs already in baseline.
Canonical IDs remain unchanged; the concurrent app checkout was not edited or built.
The app owner still needs Russian mappings; no current dirty-app fix, phone rendering or ordinary
RU activation is claimed. This renderer/release follow-up does not stop independent source authoring.
Continue the remaining frozen corpus, with original media/device/release gates and pilot refs intact.

Batch **009 — clothing and accessories** completes23 full source-N5 word articles.
One independent reviewer actually read every complete RU/frozen-EN pair, all27 dictionary
queries/29 entries/96 senses/52 Japanese forms and all204 actual combined answer labels,
plus relevant baseline bodies and actual spelling/etymology evidence. The four direct symmetric
guards are individually justified, not a clothing-category clique. The previously reviewed
`時間` candidate-pool adaptation remains unchanged; `時計` explicitly names a physical device.

The full reviewer found one low-severity **provenance** error, not a learner-text defect:
an editorial receipt incorrectly claimed that an additional reading appeared in the capture.
The clarification and active evidence guidance were corrected; the original frozen receipt
remains historical. One actual bounded recheck read the complete relevant pair/query and
corrected records, resolved the finding and verified all23 learner files raw/LF-unchanged.
[Actual full and narrow review scopes](translation-batches/009-clothing-accessories-review.json)
are distinct; no second whole-batch linguistic reread or native certification is claimed.

After batch009, membership was **250 runtime objects**:18 kanji,204 words,18 strokes and unchanged
other families. Statuses were **249 reviewed-current**, **one partial** (`counters/tsu.json`),
**two reviewed runtime-blocked drafts** and **8,026 pending**; **8,028 runtime paths remain absent**.
All227 earlier tracking records are unchanged; fresh strict progress preserves null checkpoint authority.

The pinned renderer follow-up additionally records `clothing`, `sports`, `everyday`,
`special-reading`, `weather`, `irregular-reading`, `actions`:25 occurrences across23 new cards.
Canonical IDs are preserved and the concurrent app remains untouched; no current phone rendering,
native option-pool, media, activation or release acceptance follows from source review.
Continue the remaining finite frozen target; no device gate or pilot/controlled ref has moved.

Batch **010 — home and furniture** completes25 full word articles:24 source-N5 words
and the mandatory direct N4 会話 dependency. One independent read-only reviewer actually read
all25 complete Russian/frozen-English pairs, the complete frozen マンション comparison,
all32 complete dictionary queries/32 entries/82 sense records/58 forms and every one
of229 actual answer-label/metadata records. Nine relevant baseline bodies were read in full;
other baseline objects received fingerprint/metadata checks, not whole linguistic rereview.
The24 Wikipedia records are capture provenance, not lexical proof.
All three facets returned CLEAN, with no established consequential defect or optional polish.
[Exact actual scope, fingerprints and limits](translation-batches/010-home-furniture-review.json)
record100 candidate RAW/LF comparisons,50 frozen-source comparisons and all275 manifest hashes.

The seven direct Russian guards are individually justified. In particular, shared «кухня»
in 台所/料理 would be an ambiguous answer label even though the bodies distinguish a cooking
room from a culinary tradition; only the new 台所 card adds that guard and clarification.
No housing/furniture/category or transitive clique was introduced. Separate fully read
電力/汽車 evidence supports conservative electrical-power terminology and qualified
dated/rural train senses; neither auxiliary article was adopted.
A mistakenly retained provisional sentence in the signed freeze receipt is explicitly corrected
by the new adjudication; its original historical bytes are preserved. Active guidance now
requires checking stage claims before final freeze and explicit correction of immutable errors.

After batch010, membership was **275 runtime objects**:18 kanji,229 words,18 strokes and unchanged
other families. Fresh strict8278-entry progress had **274 reviewed-current**, **one partial**
(`counters/tsu.json`), **two reviewed runtime-blocked drafts** and **8,001 pending**;
**8,003 runtime paths remain absent**. All250 earlier tracking records and their non-record
sections are preserved. Checkpoint authority remains null and checkpointReady false.

Actual serialized checks:0 validator errors,124 tests passed in28.009s, final budget
282files/291entries/880178retained/893595inflated/476833localZIP bytes after manifest generation.
Version is `08b6d0fe34307bea`. The pinned external app follow-up covers17 canonical IDs,
29 occurrences across24 new cards; some IDs already existed. IDs and concurrent app checkout
remain untouched. Source review is not native, rendering, phone, package/media, ordinary activation
or release acceptance. All four frozen pilot/controlled refs remain separately fixed.
Continue the remaining finite frozen corpus; no independent safe authoring lane is blocked.

Batch **011 — stationery and personal objects** completes21 full source-N5 word articles.
One independent read-only reviewer actually read every complete Russian/frozen-English pair:
699 English lines and848 Russian lines. All23 complete queries/24entries/57sense records/36forms,
all250 actual answer-label/metadata records and four complete baseline EN/RU pairs were read.
The19 Wikipedia records and the independent same-reading ＰＥＮ organization entry were not
used as ordinary stationery lexical evidence. The complete GogenYurai origin article was freshly
read; 鞄 remains qualified as uncertain borrowing, not inferred native history from its kanji.
All three facets returned CLEAN, no consequential finding or optional polish.
[Exact actual review and limits](translation-batches/011-stationery-personal-objects-review.json)
distinguish the full assigned scope from the other229 baseline bodies, which were not freshly
linguistically rereviewed. The reviewer did not verify signature authenticity or rerun author tests.

Three direct Russian guards are individually justified: ペン/ボールペン, ペン/万年筆,
and 新聞/雑誌. The last protects broad «периодическое издание» in the displayed Russian label;
it does not assert Japanese interchangeability. No inferred ボールペン/万年筆 edge,
publication/category clique or transitive closure was added. All source teaching survives27
optional-link flattenings; 紙→新聞 remains. カメラ retains its legitimate three-section structure.
Selected fountain-pen reading does not deny captured variants; the paper homophone comparison
does not invent pitch data, and photographic spelling/mnemonics do not guarantee image truth.

At the batch011 milestone membership was **296 runtime objects**:18 kanji,250 words,18 strokes
and unchanged other families. That strict8278-entry progress had **295 reviewed-current**, **one partial**
(`counters/tsu.json`), **two reviewed runtime-blocked drafts** and **7,980 pending**;
**7,982 runtime paths remain absent**. All275 previous tracking records/non-record sections
and canonical runtime Git blobs are unchanged. Checkpoint authority remains null and
checkpointReady false. This is not completion of the full corpus.

Actual serialized checks:0 validator errors,124 tests passed in30.629s, final budget
303files/312entries/927602retained/941019inflated/502457localZIP bytes after manifest generation.
Version is `5a0e500cfdbc372d`. Pinned app follow-up covers17 canonical IDs/22occurrences/19cards,
not all newly introduced. Canonical IDs, concurrent app checkout and all frozen pilot/controlled
refs remain untouched. No ordinary activation, native/rendering/phone, package/media or release
approval follows. Continue the next safe source batch against the same finite frozen target.

Batch **012 — N5 legacy-counter dependency closure** completes the full ten-file schema1
component: nine new files and the two previously omitted reverse fixtures in `tsu.json`.
This is124 forward cards,20 reverse fixtures,80 actual referenced noun contexts and191 Russian
learner-text leaves, not124 runtime paths or completion of all N5 content.
[Actual composite review](translation-batches/012-n5-counter-closure-review.json) preserves
the initial whole254EN/259RU-line review and its genuine findings. Six source-derived
wrong `回` choices allowed ordinary action-frequency meanings; bare `お茶` was also a valid
`本` reverse answer for bottled tea. Exactly seven negative-choice sites were separately frozen,
corrected and independently adjudicated. Original prompts, quantities, accepted tiers/readings,
IDs and all191 Russian leaf values stayed unchanged. Active counter guidance records the lesson.

The narrower evidence adjudicator read12 complete current/source/initial records, the changed
fixture's four live nouns, actual direct usage/range evidence and relevant guidance.
F1/F2 and the complete `五六本`→`ごろっぽん` language/bounded-answer-policy question resolved
CLEAN. This was not a second124-pair review. A generic interim “no significant issues” result
did not supply reading scope or resolve U1 and is not substituted for the actual adjudication.
The historical range capture remains immutable even though the fresh haiku-page RAW changed;
the actual target fields were checked, and original printed-book consultation is not claimed.

At the batch012 milestone membership was **305 runtime objects**, including11 counter files. Its strict8278-entry
progress had **305 reviewed-current**, **no partial units**, **two reviewed runtime-blocked drafts**
and **7,971 pending**; **7,973 runtime paths remain absent**. Only the current partial-tsu
tracking record was replaced after real full-scope review; its Pilot B receipts remain historical.
All295 other earlier tracking records/canonical runtime blobs and all non-record sections stay
unchanged. Checkpoint authority remains null and checkpointReady false.

Actual final serialized checks:0 validator errors,124 tests passed in43.252s; final budget
312files/321entries/984818retained/998235inflated/520508localZIP bytes. Version is
`e82c69299a2d0bbe`. No word labels/guards/tags, assets/media or concurrent app files changed.
Native/editor certification, exhaustive counter alternatives, Android range/full-phrase grading
and ordinary activation/device/media/release tests remain unperformed/separately gated; source
acceptance does not erase those bounds or move any frozen pilot/controlled ref.
The next proposed lane at that time was eleven missing N5 schema2 number/time files.
It was subsequently frozen, authored and reviewed as013 below.

Batch **013 — N5 number/time expressions** completes eleven schema2 files and122 expressions:
age/floor, clock/minutes, calendar months/dates and durations in hours/days/weeks/months/years.
All255 learner-text leaves are Russian;392 written-answer and149 reading-answer occurrences retain
the exact frozen Japanese values, canonical-versus-alternate-reading boundaries, IDs and metadata.
The single already-reviewed native expression and complete numbers article are unchanged support,
not new013 acceptance objects or duplicated exercise identities.

[Actual composite review](translation-batches/013-n5-number-time-expressions-review.json) preserves
whole2064EN/2064RU-line reading, all122 complete pairs and full987RU/856EN-line article support.
Japanese correctness and adopted coverage were CLEAN; one actual Russian finding required
`24 дней` → `24 дня`. The exact one-cue repair was independently read and rechecked, together with
the two added active-guidance lines about actual numeral declensions. Other254 Russian leaves,
all Japanese/technical/accepted forms, other ten new files and all305 baseline RAW runtime objects
remain unchanged. This narrower proof is not a second whole122-expression semantic review.
The original NEEDS FIX report remains historical; all three composite source/text facets are CLEAN.

At the batch013 milestone membership was **316 runtime objects**:18 kanji,250 words,18 strokes,2 articles,22 counter
files,1 grammar set,2 scene catalogs and3 images. Its strict8278-entry progress had
**316 reviewed-current**, **no partial units**, **two reviewed runtime-blocked drafts** and
**7,960 pending**; **7,962 runtime paths remain absent**. All305 earlier tracking records and
non-record sections are unchanged. Checkpoint authority remains null and checkpointReady false.
This is not completion of the full corpus or all N5 teaching.

Actual final serialized checks:0 validator errors,124 tests passed in28.490s; final budget
323files/332entries/1077037retained/1090454inflated/534880localZIP bytes. Version is
`2d5ac8dd3491a7de`. Explicit date-validity/day-only,週間 andか月-unit constraints survive;
unlisted readings are not declared impossible. No new word-quiz guards/tags, grammar-vocabulary
contexts, media/assets or concurrent app changes were made. Original PDFs/printed dictionaries
were not newly consulted, and automated editorial evidence is not native/exhaustive/parser/
Android/phone/IME/media/activation/release approval. C6/C7 and four frozen pilot/controlled refs
remain separate and unchanged. Continue remaining N5 calendar/time words, freezing their actual
direct dependency/negative-reference closure before authoring, then continue all remaining families.

Batch **014 — calendar/time vocabulary** completes38 full word articles:34 N5 roots and four
mandatory negative-reference dependencies. Source levels remain35 N5/two N4/one N3; no N1 coverage
is invented. The15 original direct exclusions/distractors survive. Six additional individually
evidenced Russian guards protect shared morning meaning and actual breakfast/dinner senses against
the inspected baseline labels. They are not a transitive daypart/meal clique or blanket adoption
of every captured sense. All316 prior runtime RAW objects and tracking records remain unchanged.

[Actual composite review](translation-batches/014-calendar-time-words-review.json) preserves full
1302EN/1271RU-line reading, all38 titles and152 sections, all288 actual displayed meanings and seven
complete supporting baseline bodies. All45 complete dictionary entries/70 forms were inspected;
81 returned sense objects comprise64 lexical senses and17 Wikipedia pseudo-definitions, not81
lexical senses plus17. The latter are not lexical proof. Source-specific reading restrictions,
mixed on/kun classification, calendar periods versus durations and recurrence versus all-night
activity remain explicit. Optional navigation has49 retained/64 flattened references, with no
substantive teaching removed or English placeholder cards added.

One genuine minor finding narrowed夕方 to time before evening. The exact clause was corrected to
«конец дня или ранний вечер» and independently rechecked against the complete original/current/source
朝 articles and existing晩/夜 comparisons. Other37 new files, all Japanese/technical fields and
all316 baseline RAW objects are unchanged. Two active boundary-meaning guidance lines accompany the
repair; three earlier API-pseudo-definition guidance lines remain. This is a whole38 review plus
a real narrow correction proof, not two whole38 semantic reviews. The initial NEEDS FIX receipt
is preserved; all three final composite source/text facets are CLEAN.

At the batch014 milestone membership was **354 runtime objects**:18 kanji,288 words,18 strokes,2 articles,22 counter
files,1 grammar set,2 scene catalogs and3 images. That strict8278-entry progress had
**354 reviewed-current**, **no partial units**, **two reviewed runtime-blocked drafts** and
**7,922 pending**; **7,924 runtime paths remain absent**. All316 old tracking records/non-record
sections remain unchanged. Checkpoint authority remains null and checkpointReady false.
Actual final serialized checks:0 errors/124 tests32.911s; budget361files/370entries/
1163599retained/1177016inflated/581157localZIP bytes; version `636066eada6c6783`.

The immutable pinned app function exposes seven unmapped canonical IDs across21 occurrences/
20 new cards; some IDs were already known. This is a recorded app-hint follow-up, not permission
to edit the concurrent app or translate technical IDs. No grammar contexts/assets/media or app
changes were made. Source publication does not grant native/device/IME/C6/C7/media/package/
activation/release/checkpoint authority or move any frozen runtime ref. Continue the next safe
remaining N5 kanji/words/support batch, then every remaining level and source family against6af98cb.

Batch **015 — calendar/count word prerequisites** completes37 full word articles: nine calendar
months, eleven date/duration forms, nine native counts,十,一人/二人 and five numeral/currency
forms. Source23 N5/14 unlabelled classifications remain unchanged. The frozen target has no
二月/十一月/十二月 word paths; their substantive inline examples remain, with no invented files.
Source37 have zero negative-reference edges. Two individually reviewed direct Russian guards
protect一日–日 and一人–人 against actual bare singular labels, not a generic/transitive clique.

[Actual composite review](translation-batches/015-calendar-count-words-review.json) records complete
1134EN/1138RU-line reading,37 titles/148 sections, all325 actual displayed meanings and complete
日/人 source/RU supporting pairs. All56 complete dictionary query objects were read:57 entry
occurrences/177 forms/136 returned sense objects, including12 Place and4 Wikipedia objects;
120 lexical occurrences remain. Occurrences are not asserted unique or blanket learner adoption.
Counter-specific sound changes replace overgeneralized initial-letter rules; attested五日ごにち/
二十日にじゅうにち are not falsely prohibited. Actual named Japanese definitions support both
五月晴れ senses and the old-calendar link. Current BOJ denominations support bounded note claims.

One genuine minor finding exposed an unsupported added一千円 spelling claim and a false positive
attribution to the captured千円 entry. The added claim was removed; the original ordinary-use
contrast remains, without declaring the spelling universally invalid. An explicit superseding
erratum withdraws the false claims in historical scope/preauthoring/adjudication records without
rewriting them. An independent exact-delta/evidence recheck resolved B015-R1 at high confidence;
other36 new words/all354 baseline RAW objects remain unchanged. This is a whole37 review plus
a real narrow recheck, not two whole37 semantic reviews. All final composite facets are CLEAN.

At the015 milestone membership was **391 runtime objects**:18 kanji,325 words,18 strokes,2 articles,22 counter
files,1 grammar set,2 scene catalogs and3 images. Fresh strict8278-entry progress has
**391 reviewed-current**, **no partial units**, **two reviewed runtime-blocked drafts** and
**7,885 pending**; **7,887 runtime paths remain absent**. All354 prior tracking records and
non-record sections remain unchanged; checkpoint authority null/Ready false.
Actual final serialized checks:0 errors/124 tests32.014s; budget398files/407entries/
1234441retained/1248458inflated/620416localZIP bytes; version `95a8d5dc2948138c`.

The immutable pinned app function has11 unmapped canonical IDs across56 occurrences in this
batch; preserve those IDs and leave the concurrent app untouched. Eight directly related
guidance lines and the JMnedict/ENAMDICT provenance attribution accompany the work; no assets,
grammar contexts or media were added. C6/C7/native/device/IME/media/package/activation/release/
checkpoint authority and frozen runtime refs remain separate. Continue the next safe required-word
support batch for the actual57-new-kanji distractor component, then all remaining frozen families;
mandatory distractors are not dropped to shrink the scope.

Batch **016 — everyday reading-word prerequisites** completes25 full word articles:19 roots
and six mandatory source negative-reference dependencies. Source24 N5/one N3 classifications and
all eight directed source edges remain unchanged. Eight individually reviewed additional direct
Russian guards protect actual car/transport, knowledge, departure/appearance and birth-appearance
overlaps. The足–お金pair is narrowly conservative: its witness is colloquial and usually
prefixedお, not proof that ordinary bare足means money. No transitive family clique is inferred.

[Actual whole review](translation-batches/016-everyday-reading-words-review.json) records complete
820EN/844RU-line reading,25 titles/100 sections, all350 actual displayed meanings and nine complete
unchanged Russian baseline bodies totalling310lines. All73 complete dictionary query/entry
occurrences were read:126forms/289objects=270lexical+twoPlace+17Wikipedia; occurrences are not
unique lexemes or blanket sense adoption. Both complete textual Japanese Tokyo-pitch sections
confirm雨HL/飴LH, without audio-listening claims. No consequential finding or required correction
was established; all three scoped source/text facets are CLEAN after the actual whole review.

Source手–足is correctly a body-part comparison, not a strict antonym pair. Both毎年readings,
intransitive birth, know/understand qualifications, lending direction, half/minute and colour
conventions remain explicit. Two related active-guidance lines document the source-label issue.
All391 prior runtime RAW objects/tracking records and non-record sections remain unchanged.

At the016 milestone membership was **416 runtime objects**:18kanji,350words,18strokes,2articles,22counterfiles,
onegrammarset,2scenecatalogs and3images. Fresh strict8278-entry progress has **416reviewed-current**,
**no partial units**, **two reviewed runtime-blocked drafts**, **7,860pending** and **7,862runtime
paths absent**. Checkpoint authority remains null/Readyfalse.
Actual serialized checks:0errors/124tests48.039s; final budget423files/432entries/
1294859retained/1308876inflated/651417localZIPbytes; version `faa2fe07d4ce9f22`.

The immutable pinned app function has11 unmapped canonical IDs across13 occurrences in this batch.
Keep canonical IDs stable and the concurrent app untouched. All25new working texts are CRLF;
Git/public LF domains are separately verified, not falsely equated with working RAW.
No new assets/grammar contexts/media or native/device/IME/C6/C7/package/activation/release/checkpoint
authority follows. Continue the next safe required-word support batch, the real57-new-kanji
mandatory-distractor component and every remaining frozen family.

Batch **017 — places, periods and reading-word support** completes25 full word articles,
preserving2N2/5N3/2N4/oneN5/15unlabelled classifications. Its headers require no additional
source-negative closure; two individually justified direct guards cover見物–見るand読書–読む.
They protect actual viewing/book-reading overlaps, not a transitive vision/communication clique
or a rule that grammatical tags alone establish answer safety.

[Actual whole review](translation-batches/017-places-time-reading-words-review.json) records
794EN/913RU lines,25titles/100sections/all375actual labels and nine complete unchanged Russian
baseline bodies335lines. All66complete successful dictionary query objects were read:
66entryoccurrences/96forms/106objects=92nonWikiNonPlace+twoPlace+12Wiki. Seven failed exact
lookups are neither positive evidence nor proof of invalidity. Exact name revisions and the
accepted六か月counter row are separately bound; no blanket sense/API-level adoption follows.

The real official北海道FAQ supports qualified加伊→海/1869/regional道teaching. Search-generated
quotes and guessed URLs were rejected; the genuine pamphlet does not itself contain the
replacement passage. Two active-guidance lines preserve this methodological lesson.
Freedom versus price, application versus acceptance, count/nationality/clock/duration,
book-reading construction, specific sliding shutters and youth qualifications remain explicit.
The actual whole review found no consequential defect or required correction; all three scoped
source/text facets are CLEAN. All416earlier runtime RAW objects/tracking records and non-record
sections remain unchanged.

After batch017 membership was **441runtime objects**:18kanji,375words,18strokes,2articles,22counterfiles,
onegrammarset,2scenecatalogs and3images. Its fresh strict8278-entry progress had **441reviewed-current**,
**no partial units**, **two reviewed runtime-blocked drafts**, **7,835pending** and **7,837runtime
paths absent**. Checkpoint authority remains null/Readyfalse.
Actual serialized checks:0errors/124tests27.955s; final budget448files/457entries/
1352155retained/1366172inflated/680317localZIPbytes; version `d0406f8891b9ecac`.

The immutable pinned app function has16unmapped canonical IDs across21occurrences in this batch.
Current app rendering remains UNVERIFIED; IDs stable and concurrent app untouched.
All25new working texts are CRLF; normalized/Git/public domains remain distinct.
No new assets/grammar contexts/media or native/device/IME/C6/C7/package/activation/release/checkpoint
authority follows. Continue the remaining three linked roots and their21-word closed component,
then the real57-new-kanji mandatory-distractor component and every remaining frozen family.

Batch **018 — humans, signs and traces** completes21 full word articles: the remaining
three reading-linked roots and their18 source-negative dependencies, preserving15N3/3N2/
oneN4/oneN5/oneunlabelled classifications. All24 original directed references remain,
with13 separately reasoned direct Russian guards for actual person/character/collective-human/
mark/signal/expression overlaps—not a transitive people/sign clique.

[Actual whole review](translation-batches/018-people-signs-traces-words-review.json) records
816EN/1027RU lines,21titles/84sections/all396actual title/hash records and six complete
unchanged Russian baseline bodies222lines. All55complete query objects were read:
58entryoccurrences/104forms/161objects=144lexical+17Wiki. A separate complete人query
contains eight lexical senses; counts are not unique lexemes or blanket API adoption.
NamedSeisenban兆候definitions are distinguished from the aggregator's firstDaijisen block.
The actual whole three-facet review found no required correction or consequential unresolved
textual claim; all three scoped source/text facets are CLEAN. Source Japanese/readings/levels/
qualifications, mathematical homograph distinctions and direct answer safeguards remain.
All441earlier tracking records/non-record sections/runtimeRAWobjects are unchanged.

Current membership is **462runtime objects**:18kanji,396words,18strokes,2articles,22counterfiles,
onegrammarset,2scenecatalogs and3images. Fresh strict8278-entry progress has **462reviewed-current**,
**no partial units**, **two reviewed runtime-blocked drafts**, **7,814pending** and **7,816runtime
paths absent**. Checkpoint authority remains null/Readyfalse.
Actual serialized checks:0errors/124tests49.038s; final budget469files/478entries/
1413172retained/1427189inflated/710824localZIPbytes; version `2896f5c9d706c5bd`.

The immutable pinned app function has21unmapped canonical IDs across27occurrences in this batch.
Current rendering remains UNVERIFIED; IDs stable and concurrent app untouched.
All21new working texts are CRLF; normalized/Git/public domains remain distinct.
The directly related format-reference intro now points at the already committed frozen6afcontract,
not later/dirtyEN; earlier owner-test results remain explicitly historical.
No new assets/grammar contexts/media or native/device/IME/C6/C7/package/activation/release/checkpoint
authority follows. Continue the real57-new-kanji mandatory-distractor component and every
remaining frozen family; this milestone is not completion of the full corpus or allN5.

Batch **019 — foundation kanji and restored accepted-word links** completes57newkanji
(42N5/11N4/4N3),57source-identical KanjiVG stroke files and135old-word amendments restoring
152required links. These retain all169frozen direct kanji distractor edges and justified earlier
Russian adaptations. The inherited月component-attribution correction is separately scoped.
[Current accepted source record](translation-batches/019-foundation-kanji-reviewed-source.json)
binds all250affected runtime paths to current source/Russian RAW, normalized and Git hashes.

The actual review lineage consists of one whole57kanji review, three whole45word volumes,
and bounded genuine focused rechecks for円historical-reading wording, inherited月attribution,
分minute-table classification and the direct車–電車meaning-quiz overlap. All assigned learner
facets are CLEAN through this composition; no fresh192body/whole-corpus review is claimed.
The broad 車 vehicle sense and 電車 electric-train sense are preserved. Their new direct pair is
symmetric and non-transitive; existing 車–自動車 does not imply 自動車–電車.
All326unaffected baseline runtimeRAW objects remain unchanged;135words and月are intentionally
updated and re-reviewed. Immutable historical receipts and earlier justified adaptations remain.

Current membership is **576runtime objects**:75kanji,396words,75strokes,2articles,22counterfiles,
onegrammarset,2scenecatalogs and3images. This does not mean all75kanji are N5.
Fresh strict8278-entry progress has **576reviewed-current**, **no partial units**,
**two reviewed runtime-blocked drafts**, **7,700pending** and **7,702runtimepathsabsent**.
Checkpoint authority remains null/Readyfalse; the frozen EN target remains `6af98cb...`.
Actual final serialized checks:0errors/124tests32.498s; final budget584files/593entries/
1711270retained/1727952inflated/857517localZIPbytes; version `ab961b443ea10352`.

The genuine prepublication license check found that `docs/**` export-ignore omitted the Unicode
V3 license referenced by the earlier019NOTICE addition. A separately frozen packaging amendment
copies its exact1995frozen source bytes to root `UNICODE-LICENSE.txt`, fixes only that NOTICE link,
protects RAW identity and records the observed pitfall in active instructions. The historical
docs license remains. Actual local single-root archive verification includes the root license,
all576manifest hashes and57newstrokeRAWs while excluding developer directories. This adds no
learner object or media authority. Public desktop archive/exact-main CI evidence is separate.

Canonical technical IDs remain; current app rendering/native behavior is UNVERIFIED and the
concurrent app is untouched. No phone/IME/reader/grading/playback/newmedia/packageaudio/C6/C7/
activation/release/checkpoint authority follows. Continue the finite frozen target in safe
sequential batches; this source milestone is not full corpus, runtime parity or allN5 completion.

Batch **020 — motion and position kanji with their word support** adds full前・後・来・行
cards, six full word articles and four exact frozen-source KanjiVG stroke files. Nine
previously accepted bodies restore one source-linked wrapper each; all their other RAW
bytes and earlier justified Russian adaptations remain. The
[accepted source record](translation-batches/020-motion-position-reviewed-source.json)
binds all23affected runtime paths to exact frozen English and current Russian working,
normalized and canonical Git hashes.

One genuine independent whole-batch read-only review covers all31completeRU/ENpairs:
19authored/amended bodies and12additional complete contexts, plus all402word/79kanji
title/guard rows. It reports CLEAN Japanese correctness, assigned coverage/dependencies/
quiz semantics and Russian comprehensibility; no required finding. The481title rows are
not481complete bodies, and individual review-tool execution history was not exposed by
the synchronous invocation. Author recomputed the exact snapshot hashes.
All12new-kanji directed edges are reviewed. The one source edge前→先 becomes前→月
because the original displayed meanings overlap. Three direct行くdeparture guards are
individually supported; no transitive movement clique or extra unsupported pair is added.
The attributed後origin,来character-versus-word reading table and qualified銀行history
preserve the actual source/evidence boundaries.

Current membership is **590runtime objects**:79kanji,402words,79strokes,2articles,
22counterfiles,onegrammarset,2scenecatalogs and3images. Actual kanji levels62N5/13N4/4N3
leave18of the frozen80N5kanji absent. Fresh strict8278-entry progress:
**590reviewed-current**, **no partial**, **two reviewed runtime-blocked drafts**,
**7,686pending** and **7,688runtimepathsabsent**. All567unaffected baseline RAW objects
remain unchanged; historical receipts are immutable, checkpointauthoritynull/Readyfalse.
Actual final serialized checks:0errors/124tests57.027s; final budget598files/607entries/
1754286retained/1770968inflated/877733localZIPbytes; version `b4730636d151b4ee`.
Public desktop archive/exact-main CI are separate publication evidence, not inferred here.
Existing licenses/root Unicode notice remain; four strokeRAWs exactly match frozen blobs.
Canonical `irregular` ID stays unchanged; current app rendering is UNVERIFIED, app untouched.
No phone/IME/native/playback/newmedia/packageaudio/C6/C7/ordinaryactivation/release/checkpoint
authority follows. Continue sequential safe authoring across every remaining frozen family.

Batch **021 — everyday-foundation kanji and monthly/contingency words** adds complete
万・国・語・母・父・毎・海 cards, two word articles and seven exact frozen-source KanjiVG
stroke files. A separate immutable pre-authoring amendment adds今月to the initially17old
bodies: the actual18old bodies restore22source-linked wrappers, not21distinct target pairs.
All their other RAW bytes and prior justified Russian adaptations remain. The
[accepted source record](translation-batches/021-everyday-foundations-kanji-reviewed-source.json)
binds all34affected paths to frozen English and current Russian RAW/LF/canonicalGit hashes.

One genuine independent whole-batch read-only review covers all45completeRU/ENpairs:
27authored/amended bodies and18additional complete contexts, plus all404word/86kanji
title/guard rows. It reports CLEAN Japanese correctness, assigned coverage/dependencies/
quiz semantics and Russian comprehensibility; no required finding or optional polish.
The490title rows are not490complete-body reviews. The returned report records complete
reading ranges and recovered administrative truncations; individual execution history
was not exposed by the synchronous invocation. Author recomputed the exact snapshot hashes.
All21new-kanji directed edges are reviewed. The one source語→話 edge becomes語→口:
ordinary speaking meanings overlap despite different short titles. No new word exclusion
or transitive clique was required. Qualified每historical-form wording, explicit母rare-reading
dictionary-classification difference and modern/historical語らうsenses preserve the evidence
boundaries without silently migrating Japanese grading/classification metadata.

Current membership is **606runtime objects**:86kanji,404words,86strokes,2articles,
22counterfiles,onegrammarset,2scenecatalogs and3images. Actual kanji levels68N5/14N4/4N3
leave12of the frozen80N5kanji absent. Fresh strict8278-entry progress:
**606reviewed-current**, **no partial**, **two reviewed runtime-blocked drafts**,
**7,670pending** and **7,672runtimepathsabsent**. All572unaffected baseline RAW objects
remain unchanged; historical receipts are immutable, checkpointauthoritynull/Readyfalse.
Actual final serialized checks:0errors/124tests43.963s; final budget614files/623entries/
1795849retained/1812531inflated/898650localZIPbytes; version `74520d18c4425b1b`.
Public desktop archive/exact-main CI remain separate publication evidence, not inferred here.
Existing licenses/root Unicode notice remain; seven strokeRAWs exactly match frozen blobs.
New retained canonical `set-phrase` and `simplified-form` app rendering is UNVERIFIED,
not a proven defect; concurrent app untouched. No phone/IME/native/playback/newmedia/
packageaudio/C6/C7/ordinaryactivation/release/checkpoint authority follows. Continue
sequential safe authoring across every remaining frozen family, not just this milestone.

## Reviewed source milestone022: foundation contrasts

The [accepted source record](translation-batches/022-foundation-contrasts-kanji-reviewed-source.json)
adds complete友・古・右・天・左・新・気・犬・良・銀・長 cards,13complete word articles
and11RAW-identical licensed frozen-source strokes. Fourteen separately frozen wrappers
across11older bodies restore adopted navigation; all other old RAW bytes and595unaffected
baseline runtime objects remain unchanged. All46affected paths retain exact source and
current Russian workingRAW/canonicalGitRAW/LF hashes. Earlier milestone counts are historical.

Actual independent whole review read47completeRU/ENpairs:35authored/amended bodies,
12unchanged contexts, plus all417word/97kanji title/guard rows. It found one unsafe retained
長→良 meaning edge: both have ordinary positive-quality senses. The actual finding was saved,
then a separate signed pre-edit amendment froze長→銀. A focused independent3-pair recheck
read final長/銀/良, verified the one-line fix and640unchanged other runtime objects, and
confirmed all three textual facets CLEAN. The original synchronous reviewer could not receive
follow-up messages; that evidenced tool limitation required the fresh focused reviewer.
The final47-pair coverage is carried forward with unchanged proof, not a second47-pair reread.
All33directed kanji edges, six source word negative edges and three direct word guards
(子犬–犬、右手–手、左手–手) are reviewed. Four kanji source edges change in total;
there is no transitive right/left-hand or human-child/puppy clique.

気's KANJIDIC/KanjiPedia classification difference is explicit; selected grading is preserved.
The old-氣 dictionary history is distinct from the rice/steam mnemonic. Unsupported positive
ゆうがん teaching is omitted without asserting universal impossibility; right-bankうがん
andユウthrough左右 remain. 古/新/良 reading groupings,年上 and年寄り register are qualified.
長短's actual named dictionary bodies were read at canonical568822; generated URL prose
and an incomplete simplifiedHTML extraction are not used as evidence. Historical receipts
remain immutable, including their explicit later corrections.

Current membership is **641runtime objects**:97kanji/417words/97strokes/2articles/
22counterfiles/onegrammarset/2scenecatalogs/3images. Kanji74N5/18N4/5N3 leave six frozenN5
cards absent:名・子・学・小・校・高. Fresh strict8278-entry progress:
**641reviewed-current**, **no partial**, **two reviewed runtime-blocked drafts**,
**7,635pending**, **7,637runtimepathsabsent**. Checkpointauthoritynull/Readyfalse.
Actual final serialized checks:0errors/124tests37.589s; budget649files/658entries/
1886838retained/1903520inflated/944262localZIPbytes; version `add35d1a4509626b`.
Public desktop archive and exact-main CI are separate publication evidence, not inferred here.
Existing licenses/rootUnicode notice remain; no new canonical tag IDs. Concurrent app untouched.
No native/phone/IME/playback/newmedia/packageaudio/C6/C7/ordinaryactivation/release authority.
Continue all remaining safe frozen families; neither allN5 nor the full corpus is complete.

## Reviewed source milestone023: N5-support foundations

The [accepted source record](translation-batches/023-n5-support-foundations-reviewed-source.json)
adds complete会・公・力・店・持・特・社・道・駅 cards,13complete word articles and nine
RAW-identical licensed frozen-source strokes. All nine kanji retain frozenN4 classification:
this is a mandatory-support stage for the six remainingN5 roots, not an inventedN5 relabel.
Five prefrozen old wrappers are restored;636other baseline runtime RAW objects are untouched.
All36affected paths have exact frozen-source/current-workingRAW/canonicalGitRAW/LF evidence.

Actual independent whole review read49assigned completeRU/ENpairs and two followed pairs
(左右/旅行),51unique complete pairs, plus all430word/106kanji title/guard rows. One actual
cross-facet finding—力's influence sense overlaps the secondary 左右 caption—and four
consequential frequency/register qualifiers were recorded honestly. A separate signed
pre-edit amendment froze the direct 力–左右 exclusion and neutralizations. A fresh bounded
reviewer read six complete pairs, all relevant full lexical objects/readings/history texts,
and verified seven exact replacements,667unchanged runtime objects and46unchanged bodies.
All three source-text facets are CLEAN. This combines actual51whole pairs with six focused
pairs and exact continuity, not a second51-pair reading or57unique pairs. No original
reviewer reuse/model attribution is invented; its synchronous report had no resumable ID.

All27directed kanji edges and four source word negative edges are reviewed. The sole
kanji-edge change is 会:社→公; retained 社→会 is assessed directionally against actual
Russian captions. Final direct word guards are 書店–店、水道–水、道–方、力–左右.
There is no transitive force/left/right clique; 力–元気 and 道–旅行 were not demonstrated
requirements. The supported 力/強い voicing correction distinguishes the changed component.
Old會/驛 histories are qualified and separate from modern mnemonics; source-selected
reading order, phonetic metadata, types, IDs, tags and level absence remain intact.
公立's broader contrast-with-private use and 持てる's distinct senses retain named evidence.
Rarity/register modifiers on 会わせる、やしろ、リイ、たな are removed without claiming
the opposite frequency or disabling grading. Optional absent wrappers retain the complete
Japanese comparison/component teaching in plain text, not English runtime placeholders.

Current membership is **672runtime objects**:106kanji/430words/106strokes/2articles/
22counterfiles/onegrammarset/2scenecatalogs/3images. Kanji74N5/27N4/5N3 still leave six
frozenN5 cards absent:名・子・学・小・校・高. Fresh strict8278-entry progress:
**672reviewed-current**, **no partial**, **two reviewed runtime-blocked drafts**,
**7,604pending**, **7,606runtimepathsabsent**. Checkpointauthoritynull/Readyfalse.
Actual corrected serial checks:0errors/124tests33.568s; budget680files/689entries/
1969250retained/1985932inflated/984888localZIPbytes; version `2de6f16a7092c537`.
Public desktop archive/exact-main CI are separate publication evidence, not inferred here.

An actual app-hint mapping gap is pinned in the
[app follow-up](translation-batches/023-n5-support-foundations-app-tag-followup.json):
canonical `institutions` (公立), `na-adjective` (特別), `work` (会議) may render raw
English. IDs remain stable; source-text acceptance does not resolve this appUI/activation
gate, and the concurrent app writer is untouched. Existing licenses/NOTICE remain.
No native/phone/IME/playback/newmedia/packageaudio/C6/C7/ordinaryactivation/release authority.
Continue sequential safe authoring across every remaining frozen family.

Batch **024 — motion, night and space** adds complete動・夜・広・度・病,
four complete words (今度・広い・病気・病院) and five RAW-identical licensed strokes.
All five kanji retain frozenN4 classification; the words retain oneN4/threeN5.
Thirteen useful wrappers across twelve old bodies restore acquired navigation without
altering the remaining prose or earlier adaptations. All660other baseline RAW objects
are unchanged;26affected paths have exact source/current-workingRAW/canonicalGitRAW/LF
evidence in [accepted source](translation-batches/024-motion-night-space-reviewed-source.json).

The initial generic synchronous code-review result supplied no actual reading scope;
its available ID could not be messaged because the interface rejects sync follow-ups.
It was not treated as acceptance. One subsequent bounded read-only evidence review
actually read all32assigned full RU/EN pairs and 入院/時,34unique complete pairs, all
434word/111kanji title/guard rows, seven complete XML records, four radical rows,
all56lexical queries/61matching occurrences and five complete official historical texts.
All three source-text facets are CLEAN, with no actionable findings or consequential
unverified claims within that actual scope. This does not claim545whole-body reading,
native-speaker approval, historical-pixel inspection or full-corpus acceptance.

All15directed kanji edges are reviewed. Only 動:行→男 changes: car/clock 動く can have
ordinary Russian translations «едет»/«идут», overlapping 行's existing caption.
Four independently justified direct word pairs are 広い–大きい and
今度–最近/近頃/このごろ; no transitive size/temporal clique is inferred.
All original readings, Japanese examples, IDs, types, source levels and tags remain.
病's original stem examples are retained and distinguished from final 病 in 恋病,
with two attested readings and no invented separate み or universal spelling rule.
Degree/time, recovery, mild-ailment usage and outpatient/admission distinctions remain
qualified. A reusable affix-position lesson is independently reviewed in active guidance.

Current membership is **686runtime objects**:111kanji/434words/111strokes/2articles/
22counterfiles/onegrammarset/2scenecatalogs/3images. Kanji74N5/32N4/5N3 still leave six
frozenN5 cards absent:名・子・学・小・校・高. Fresh strict8278-entry progress:
**686reviewed-current**, **no partial**, **two reviewed runtime-blocked drafts**,
**7,590pending**, **7,592runtimepathsabsent**. Checkpointauthoritynull/Readyfalse.
Actual final serial checks:0errors/124tests31.403s; budget694files/703entries/
2009904retained/2026586inflated/1005053localZIPbytes; version `dc1555f59e7dc259`.
Initial validation receipts remain historical; public archive/exact-main CI are separate.

The actual [app follow-up](translation-batches/024-motion-night-space-app-tag-followup.json)
records raw fallback for canonical `i-adjective`, `health`, `place`; earlier023mapping
gaps remain unresolved. IDs are retained; no concurrent app edits, device/IME/playback,
newmedia/packageaudio/C6/C7/ordinaryactivation/release/checkpoint authority follows.
Five stroke blobs and root notices retain real KanjiVG/Unicode licensing. Continue the
remaining N5 support/words and every other safe family of the finite frozen target.

Batch **025 — heavy-support vocabulary** adds complete重,35full word articles and
one byte-identical licensed frozen重stroke. It preserves source levels acrossN5/N4/N3/N2,
rather than relabelling dependency support asN5. Thirteen useful navigation wrappers
across11old bodies retain all earlier Russian adaptations. All675other accepted runtime
RAW objects remain unchanged;48affected paths have exact source/current-workingRAW/
canonicalGitRAW/normalizedLF evidence in
[reviewed source](translation-batches/025-heavy-support-vocabulary-reviewed-source.json).

One bounded READ-ONLY reviewer actually read **58complete EN/RU pairs**, all
**581displayed title/header/direct-guard rows** (112kanji/469words),88queries with
114complete exact-matching object occurrences, full重/気XML, exactU+2FA5radical166,
the complete110-line official気page and explicit音/訓HTMLaltlabels.
It also read only the namedDaijisen毛糸entry26–32, actual喜びNotes320–337,
ちょっとNotes320–383 and the complete115-line cited quantity article.
The [actual independent report](translation-batches/025-heavy-support-vocabulary-independent-review.json)
does not claim581full bodies, all8278objects, native-human or historical-pixel review.

Japanese accuracy, adopted coverage/quiz discrimination and Russian comprehensibility
pass with an explicit historical qualification: the source claim thatおも.なうis
archaic/dictionary-only or specifically means “to take seriously” remains **UNVERIFIED**.
The actual XML proves the reading, not those qualifiers. RU preserves the full reading
list and deliberately does not assert the unsupported claim; the modern-layer mnemonic
is not etymology. No current-candidate correction was requested.

All19original directed word edges and重foils車/動/東remain. The17additional direct pairs
were independently assessed against actual adopted meanings and the combined pool,
not title uniqueness or graph transitivity. Source metadata/IDs/types/tags/readings and
substantive examples are retained. Named気classification, quantity-clause constraints,
spelling-specific rarity, mental-life/material/group meanings, promise versus booking,
documented transitive終わるand height/price/pitch distinctions remain explicit.
The first full author validator really found26unprovided optional wrappers plus oneH2error.
Its immutable failure receipt is retained; all27prefrozen fixes only removed navigation
markup or corrected the heading, preserving Japanese labels and teaching without placeholders.

Current membership is **723runtime objects**:112kanji/469words/112strokes/2articles/
22counterfiles/onegrammarset/2scenecatalogs/3images. Kanji74N5/33N4/5N3 still leave
名・子・学・小・校・高 absent. Fresh strict8278-entry progress:
**723reviewed-current**, **no partial**, **two reviewed runtime-blocked drafts**,
**7,553pending**, **7,555runtimepathsabsent**. Checkpointauthoritynull/Readyfalse.
Actual serial checks:0errors/124tests29.720s; budget731files/740entries/
2118980retained/2135662inflated/1058981localZIPbytes; version `191af32fbe5095ba`.
Public archive/exact-main CI are separate evidence, not phone acceptance.

The [observed app-tag follow-up](translation-batches/025-heavy-support-vocabulary-app-tag-followup.json)
and previous mapping gaps remain unresolved. Canonical IDs and the concurrent app stay
untouched. No new image/scene/audio adoption or paid generation occurred.
Exact frozenstroke/rootKanjiVG/Unicode notices remain intact. No device/IME/playback/
newpackage/C6/C7/ordinaryactivation/release/checkpoint authority follows.
Continue the actual29-kanji mandatory-support component, remainingN5words and every
other safe level/family of the finite frozen target; this milestone is not full completion.

## Reviewed source milestone026: N5 kanji closure

The [reviewed source record](translation-batches/026-n5-kanji-closure-reviewed-source.json)
adds29complete kanji and29exact frozen-source licensed strokes. Sixty old bodies change
only frozen navigation wrappers;日 adds its safe third foil目. All662other baseline
runtime RAW objects remain unchanged.119affected paths retain exact frozen English and
current Russian workingRAW/canonicalGitRAW/normalizedLF hashes. Historical intake,
source proposals, freezes and unreviewed candidate remain immutable.

The whole-batch independent read-only review actually read108completeEN/RUpairs:
29new and79old/context pairs. It also read141kanji answer rows,59scoped word rows,
29complete XML records,15radical rows and all13relevant dictionary main entries.
The author-prepared610-row pool is not claimed as610reviewed rows or whole bodies.
The actual final verdict is “No significant issues found in the reviewed changes.”
Separate facet grades were not returned. Public reading statements and completed
BEGIN/END/hash markers substantiate all108pairs; the report preserves that limitation.

Because the original synchronous reviewer could not receive a focused follow-up, one
subsequent read-only adjudication read ten complete pairs concerning the disputed
claims/five foil changes/reverse校→学/日 amendment. It explicitly returns C1/C2/C3 CLEAN
within that narrow scope, no actionable finding; it is not another108-pair review.
The [independent record](translation-batches/026-n5-kanji-closure-independent-review.json)
faithfully distinguishes the two actual scopes and their conclusions.

Of87directed source edges,82remain and five are independently supported replacements.
The 学/子/少 ambiguities arise from ordinary dictionary meanings. 多/高 replacements
are conservative valid alternatives, not uniquely mandatory changes or claims of
universal Russian equivalence. Retained reverse校→学 is judged against actual «учёба»,
not mechanically reversed. No transitive clique is added.

Historical claims about reading rarity/register,字-なderivation,安price etymology and
少いhistory remain UNVERIFIED and are not asserted in current Russian teaching.
The full source reading lists and substantive examples remain;學's hands, selected
dictionary no-kun scope, 子fixed vocabulary, study-field labels and高めるreading row
are qualified/corrected using actual evidence, not unseen images or English authority.

Membership is781runtime objects:141kanji/469words/141strokes/2articles/22counterfiles/
onegrammarset/2scenecatalogs/3images. Kanji80N5/49N4/11N3/1N2 includes all80frozenN5
kanji, not everyN5word or the corpus. Fresh strict8278-entry progress:
**781reviewed-current**, **no partial**, **two reviewed runtime-blocked drafts**,
**7,495pending**, **7,497runtimepathsabsent**. Checkpointauthoritynull/Readyfalse;
version `b99a20143288672b`. Actual initial serial checks:0errors/124tests27.543s;
budget789files/798entries/2264099retained/2280781inflated/1131944localZIPbytes.
Final checks, public desktop archive and exact-main CI are separately evidenced.

Root licenses/NOTICE and all strokeRAWs remain exact. No new image/scene/audio or paid
generation occurred. Existing app-tag gaps remain unresolved; concurrent app untouched.
No phone/IME/playback/newpackage/C6/C7/ordinaryactivation/release/checkpoint authority
follows. Continue remainingN5words and every safe frozen level/family; full task is
still in progress, independent of the separately blocked release/device/media gates.

## Reviewed source milestone 027: numeral words

The [reviewed source record](translation-batches/027-numeral-words-reviewed-source.json)
adds complete Russian articles for ゼロ、一、七、万、三、九、二、五、八、六、千、四、百、零.
All 781 baseline runtime RAW objects remain unchanged. The source stays frozen at
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`. Exact pre-authoring headers, scope,
source/adaptation evidence and unreviewed candidate remain immutable historical records.

One [independent read-only reviewer](translation-batches/027-numeral-words-independent-review.json)
actually read all 39 complete frozen EN/RU pairs, all 483 combined word-title/
metadata/direct-guard rows and all 14 complete selected lexical objects. It returned
explicit C1/C2/C3 CLEAN within that scope, with no actionable findings or required
corrections. This does not claim 483 complete bodies, native-human certification
or whole-corpus acceptance. The nine numeral/general-count direct exclusions are
valid conservative safeguards, not uniquely mandatory rules; ゼロ–零 is valid
and defensively redundant under existing exact-title deduplication. No numeric
category, currency, person or calendar clique was invented.

The original ゼロ query's zero literal spelling matches remain recorded honestly:
the actual selected object supplies ０/〇/零 read ゼロ and a kana-use note, not a
literal `word:ゼロ` match. 百's separate Place “Hyaku” sense is not numeral evidence.
Frozen community N5 labels and inherited attribution IDs remain; API levels and
the absence of API entry IDs do not authorize invented metadata corrections.
Japanese examples, readings, type/IDs/tags, sound changes and quantities remain.
English-dependent comparisons in 六/千 become Japanese counting explanations;
零点五 stays Japanese while its Russian decimal gloss uses 0,5. Only the absent
零 kanji navigation wrapper is omitted; its kanji metadata and teaching remain.

Membership is **795 runtime objects**: 141 kanji/483 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images. Word levels are
309 N5/49 N4/54 N3/17 N2/54 unlabelled. All 80 frozen N5 kanji are present, but
**363 of 672 frozen N5 words remain**. Fresh strict 8,278-entry progress:
**795 reviewed-current**, **no partial**, **two excluded reviewed runtime-blocked
drafts**, **7,481 pending**, **7,483 runtime paths absent**.
Checkpoint authority null/Ready false; version `d449a612af670113`.
Final serial checks: manifest regenerated without change, validator 0 errors,
124 tests OK in 37.494s; budget 803 files/812 entries/2,294,558 retained/
2,311,240 inflated/1,148,688 ZIP bytes. Publication/signatures/desktop archive/
exact-main CI are separate actual receipts, not device or release acceptance.

No new strokes/images/scenes/audio or paid generation occurred. The canonical
`quantity` tag is new to the adopted word pool; its Russian app hint is UNVERIFIED,
not an established missing mapping. The concurrent app checkout remains untouched.
Existing device/IME/playback/exact media-package/C6/C7/ordinary activation/release
gates remain separate. Continue remaining N5 and all safe frozen levels/families,
including honest excluded drafts for restricted listening packages; the full task
is still in progress.

## Reviewed source milestone 028: colour, shape and size

The [reviewed source record](translation-batches/028-colour-shape-size-reviewed-source.json)
adds 33 complete Russian word articles: 27 N5, three N3, two N2 and one N4.
Six words are actual source-negative providers, not placeholder closure cards.
The source remains frozen at `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
793 baseline runtime RAWs remain byte-identical; only the two prefrozen useful
navigation wrappers in 土地/輝く change, exactly reversible to their intake RAWs.
Their complete prior teaching and adaptations remain; old receipts are historical.

The [cumulative independent record](translation-batches/028-colour-shape-size-independent-review.json)
preserves the whole initial review and bounded correction recheck separately.
The first reviewer actually read 59 complete EN/RU pairs, all 516 combined
title/metadata/direct-guard rows, 33 complete selected lexical objects
(32 unique), three selected complete XML entries and the actual Daijisen よごす
entry. Its C1 was CLEAN; C2/C3 had findings. The synchronous agent could not
receive follow-up, so one subsequent read-only focused reviewer read ten
complete pairs, 19 focused answer rows, five complete primary objects and two
Russian meaning sections, plus the eight new guidance lines. It returned
explicit C1/C2/C3 CLEAN within its scope and supports cumulative textual
acceptance over 61 unique pairs. This is not one fresh 61-pair review,
516 complete bodies, native-human certification or whole-corpus acceptance.

The final 45 direct safeguards comprise 41 initially accepted pairs and four
independently adjudicated additions: 欲張り–けち, 色–言葉, 明るい–きれい,
色–性格. Six questionable proposals were withdrawn rather than self-approved;
薄い–少ない was removed for unsupported density-to-total-quantity reasoning.
Withdrawing an extra proposal does not assert universal impossibility.
The English soil homograph does not survive in the actual Russian 汚す/土
captions, while Russian «дорогой» creates a valid かわいい–高い ambiguity.
These observed lessons and actual-caption/entailment limits are now in active
content instructions. No transitive or semantic-category clique was added.

Japanese facts/examples/readings, canonical types/IDs/tags/levels and qualifiers
remain. The precise 明い search-only label, 長い/永い restriction and
non-absolute よごす/けがす distinction have actual selected-source support.
The cached XML is not a fresh origin authentication or frozen-dataset match.
Russian prose stands alone; only unavailable local link wrappers are omitted,
never substantive teaching or English placeholder cards. 色 cites an actual
query URL without an invented numeric dictionary ID.

Membership is **828 runtime objects**: 141 kanji/516 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images. Word levels are
336 N5/50 N4/57 N3/19 N2/54 unlabelled. All 80 frozen N5 kanji are present,
and exactly **half of 672 frozen N5 words** are adopted; **336 remain**.
Fresh strict 8,278-entry progress: **828 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked drafts**, **7,448 pending**,
**7,450 runtime paths absent**. Checkpoint authority null/Ready false;
version `01fc236dddbb5efe`.
Actual corrected-candidate serialized checks: validator 0 errors, 124 tests OK
in 32.569s; budget 836 files/845 entries/2,380,105 retained/2,396,787 inflated/
1,192,811 ZIP bytes. Final checks, public desktop archive, signatures and
exact-main CI have separate actual receipts, not device or release acceptance.

No new strokes/images/scenes/audio or paid generation occurred. The canonical
word-tag IDs `behavior`, `character`, `cleaning`, `description`, `dimension`,
`length`, `property`, `shape` are new to this adopted word pool; their app
mappings remain UNVERIFIED, not established missing. The concurrent app stays
untouched. Device/IME/playback/exact media-package/C6/C7/ordinary activation/
release gates remain separate. Continue remaining N5 and every safe frozen
level/family, including honest excluded listening drafts; the full task is
still in progress.

## Reviewed source milestone 029: weather, taste and condition

The [reviewed source record](translation-batches/029-weather-taste-condition-reviewed-source.json)
adds 25 complete Russian word articles: 24 N5 and the actual N3 source-negative
provider 苦しい. The frozen target stays
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
All 828 baseline runtime RAWs and earlier tracking rows remain unchanged.

The [cumulative independent record](translation-batches/029-weather-taste-condition-independent-review.json)
preserves two actual returns separately. The initial reviewer read all
43 complete EN/RU pairs (25 new and 18 existing), all 541 combined compact
title/metadata/direct-guard rows, 35 complete selected lexical objects and
the four new kana-only/homonym guidance lines. Seven of the eight いい
reading matches are unrelated homonyms, not seven more senses of the adjective.
The initial reviewer retained all 21 original direct guards and returned
C1 CLEAN with C2/C3 findings; that historical report is not rewritten.

The focused reviewer freshly read three complete pairs/six bodies, three
focused answer rows, one repeated complete 寒い lexical object and the three
new verified-comparison-reading guidance lines. The two exact corrections
add a direct 寒い–弱い safeguard and 下手（へた）in the comparison.
The focused return is C1/C2/C3 CLEAN and explicitly supports cumulative
scoped textual acceptance across 43 unique pair paths and 22 direct guards.
It is not a fresh 43-pair or 541-semantic-row review, 541 whole bodies,
36 unique lexical objects, or whole-corpus/native/human acceptance.

The additional guard is moderate and conservative: the actual 寒い entry
includes weak/lame jokes, while Russian слабый has a poor-quality sense.
This is not a direct Japanese–Russian dictionary entry, attestation of the
exact «слабая шутка» collocation, universal synonymy or observed device failure.
No guard follows from transitivity through 冷たい or a negative-quality clique.
The added へた reading is verified in frozen 悪い, not guessed from components.
All source examples/forms/readings and level/tag/type IDs remain; unavailable
optional wrappers become plain Japanese terms without dropping teaching.
The displayed 不味い special-reading note and neuter карри evidence retain
their exact reading boundaries; the Gramota collection-only response is not proof.

Membership is **853 runtime objects**: 141 kanji/541 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images.
Word levels are 360 N5/50 N4/58 N3/19 N2/54 unlabelled:
**360 of 672 frozen N5 words are adopted; 312 remain**.
Fresh strict 8,278-entry progress: **853 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked drafts**, **7,423 pending**,
**7,425 runtime paths absent**. Checkpoint authority null/Ready false;
version `ccfb8fceb5c857bf`.
Actual final serialized checks: validator 0 errors, 124 tests OK in 44.704s;
budget 861 files/870 entries/2,447,460 retained/2,464,142 inflated/1,227,330 ZIP bytes.
Main integration, actual public desktop archive, signatures and exact-main CI
have separate receipts, not Android/phone/IME/playback acceptance.

No new assets/media or paid generation occurred. The five canonical word-tag
IDs `condition`, `difficulty`, `evaluation`, `taste`, `temperature` are new to
this adopted word pool; app mappings remain UNVERIFIED, not established missing.
The concurrent app remains untouched. Device/exact media-package/C6/C7/ordinary
activation/release gates remain separate. Continue the remaining 312 N5 words
and every safe frozen level/family, including honest excluded listening drafts;
the entire translation objective remains in progress.

## Reviewed source milestone 030: skill, interest and evaluation

The [reviewed source record](translation-batches/030-skill-interest-evaluation-reviewed-source.json)
adds 22 complete N5 Russian word articles against unchanged frozen EN
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
All 853 accepted baseline runtime RAWs and earlier tracking rows remain unchanged.

The [cumulative independent record](translation-batches/030-skill-interest-evaluation-independent-review.json)
preserves the actual initial 54 complete EN/RU pairs/108 bodies, all 563 combined
compact answer rows, 39 required selected lexical query objects and two additional
corroborating objects. These are selected query objects, not all homonyms or 41
distinct lexemes. The initial reviewer retained all 49 direct guards and returned
C1/C3 CLEAN with one grouped C2 finding about two missing direct safeguards.
That report is immutable.

The focused reviewer freshly read three complete pairs/six bodies, three answer
rows and three repeated complete lexical objects. The exact one-line correction
adds only direct 大切–大きい/大きな exclusions; no learner body or accepted old file
changes. Both are supported by the actual «важный» answer and significant/important
uses. 大きい's complete dictionary object explicitly includes important/decisive/valuable;
大きな's concise object does not explicitly say important, but its complete frozen
source and Russian body teach abstract importance/значимость.
These are direct assessments, not transitivity through 大変 or a size-category clique.
The focused return is C1/C2/C3 CLEAN within that scope, supporting cumulative
textual acceptance across 54 unique pair paths and 51 direct guards.
It is not a fresh 54-pair/563-semantic-row review, 563 whole bodies or native acceptance.

All source examples/readings/forms, qualifiers and technical IDs/types/tags/levels
remain. The full 易しい–チョロい teaching and all same-question examples are retained.
欲しい does not acquire a universal third-person ban; 結構's evidenced noun sense
is distinguished from offer responses. The omitted 立派 subject remains unspecified;
賑やか explains workload versus liveliness without needing English “busy.”
Unavailable optional wrappers become plain Japanese terms without losing teaching.
Two independently read active guidance lines address the actually observed loss
of Japanese span/ruby text in simplified HTML; decoded complete recovery preceded
the author's source-reading claim.

Membership is **875 runtime objects**: 141 kanji/563 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images.
Word levels are 382 N5/50 N4/58 N3/19 N2/54 unlabelled:
**382 of 672 frozen N5 words are adopted; 290 remain**.
Fresh strict 8,278-entry progress: **875 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked drafts**, **7,401 pending**,
**7,403 runtime paths absent**. Checkpoint authority null/Ready false;
version `ef6742b6f5b62e67`.
Corrected-candidate serialized checks: validator 0 errors, 124 tests OK in 31.802s;
budget 883 files/892 entries/2,511,772 retained/2,528,454 inflated/1,259,693 ZIP bytes.
Final checks, main integration, actual public desktop archive, signatures and
exact-main CI have separate receipts, not Android/phone/IME/playback acceptance.

No new assets/media or paid generation occurred. The five canonical word-tag
IDs `ability`, `atmosphere`, `desire`, `preference`, `preferences` are new to this
adopted word pool; app mappings remain UNVERIFIED, not established missing.
The concurrent app remains untouched. Device/exact media-package/C6/C7/ordinary
activation/release gates remain separate. Continue the remaining 290 N5 words
and every safe frozen level/family, including honest excluded listening drafts;
the entire translation objective remains in progress.

## Reviewed source milestone 031: distance, speed and direction

The [reviewed source record](translation-batches/031-distance-speed-direction-reviewed-source.json)
adds 31 complete Russian word articles: 26 N5, three N4 and two N3, against
unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
The coupled existing 川上 correction changes only «Противоположная сторона реки»
to «Противоположное по смыслу слово» for 川下, downstream rather than the opposite bank.
The other 874 accepted runtime RAWs remain unchanged; the current 川上 tracking
row is updated after actual full-unit rereview, without rewriting historical receipts.

The [cumulative independent record](translation-batches/031-distance-speed-direction-independent-review.json)
distinguishes the actual whole review of 32 primary EN/RU pairs, all 594 combined
captions/readings, 63 retained complete lexical objects and 39 supporting Russian
bodies for C2. Those supporting English bodies were not part of that whole reading.
The initial C1/C3 CLEAN and C2 NEEDS FIX report remains immutable.
Its two grouped findings require three direct guards: 横–近く and 向こう–ほか/他.

The fresh narrower sequential reviewer read seven complete EN/RU pairs, seven
actual labels and seven repeated lexical objects, mechanically verifying all
594 current row bindings and unchanged titles/readings. The three metadata-line
edits add those safeguards and withdraw the insufficiently supported author
速い–易しい precaution: `esp. 早い` is not proof of ordinary written 速い meaning
«несложный», nor an absolute prohibition of that spelling.
All primary and supporting Russian learner bodies remain unchanged.
The focused C1/C2/C3 CLEAN return supports cumulative scoped textual acceptance,
with **67 direct guards**, not a fresh 32-primary/594-semantic-row review,
71 full bilingual pairs, native certification or a transitive exclusion clique.
The initial synchronous reviewer could not resume; only one narrower reviewer
ran afterward, never simultaneously.

The complete source lessons, Japanese examples/readings, reading-specific
qualifiers and technical IDs/types/tags/levels remain. The full 上/下/中/外
additional-reading lessons, 内's constructions, four 他人 examples and ほか's
negative/additive distinction are preserved. Optional unavailable wrappers
become plain teaching text, not English placeholders or truncated lessons.
Actual correctly decoded dictionary HTML confirmed the relevant 横/向こう
definitions when simplified extraction omitted them; generated search-URL
prose was not substituted for the actual canonical source.

Membership is **906 runtime objects**: 141 kanji/594 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images.
Word levels are 408 N5/53 N4/60 N3/19 N2/54 unlabelled:
**408 of 672 frozen N5 words are adopted; 264 remain**.
Fresh strict 8,278-entry progress: **906 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked drafts**, **7,370 pending**,
**7,372 runtime paths absent**. Checkpoint authority null/Ready false;
version `36b8a5c1bbb4b3ed`.
Corrected-candidate serialized checks: validator 0 errors, 124 tests OK in 28.994s;
budget 914 files/923 entries/2,597,051 retained/2,613,733 inflated/1,303,376 ZIP bytes.
Final checks, source integration, actual public desktop archive, signatures
and exact-main CI have separate receipts, not Android/phone/IME/playback acceptance.

No new assets/media or paid generation occurred. The canonical word-tag IDs
`comparison`, `distance`, `speed` are new to this adopted word pool;
app mappings remain UNVERIFIED, not established missing. The concurrent app is untouched.
Device/exact media-package/C6/C7/ordinary activation/release gates remain separate.
Continue the remaining 264 N5 words and every safe frozen level/family, including
honest excluded listening drafts; the entire translation objective remains in progress.

## Reviewed source milestone 032: travel, places and transport

The [reviewed source record](translation-batches/032-travel-places-transport-reviewed-source.json)
adds 27 complete Russian word articles: 26 N5 roots and the required N4 隅,
against unchanged frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
All 906 accepted baseline runtime RAWs and earlier tracking rows remain unchanged.

The [cumulative independent record](translation-batches/032-travel-places-transport-independent-review.json)
preserves the actual whole review of 27 primary and 21 supporting EN/RU pairs,
621 compact semantic answer rows and 57 complete selected dictionary-object rows.
Those include repeated objects and distinct homographs, not 57 adopted lexemes.
The initial C1/C3 CLEAN and C2 UNVERIFIED report stays immutable.
The fresh sequential focused reviewer read seven complete pairs, seven labels,
six repeated complete lexical objects, the short actual Daijisen かど subsection
and exact pinned app Git-source ranges. This supports cumulative C1/C2/C3 CLEAN,
not a fresh 27-primary/621-semantic-row review or 50 reviewed bilingual pairs.
The cumulative unique complete-pair count is 48; 書店 and 読書 have only
mechanical fingerprint verification in these independent reviews.

Actual modern dictionary evidence and the bare-word meaning prompt resolve
the 門／かど question with direct 門–家/家族/庭 safeguards. The initial 20 pairs
remain; the total is **23 direct guards**, without a transitive park/entrance clique.
Door-sense restrictions on 戸 are not transferred to another listed spelling.
The precise outer-enclosure definition does not require 門–ドア/戸 in this pool.
All 933 learner bodies and 621 captions/readings stay unchanged during the
focused metadata correction. Active guidance records the actual optional-reading
boundary and per-sense spelling restriction, not a phone-test claim.

Membership is **933 runtime objects**: 141 kanji/621 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images.
Word levels are 434 N5/54 N4/60 N3/19 N2/54 unlabelled:
**434 of 672 frozen N5 words are adopted; 238 remain**.
Fresh strict 8,278-entry progress: **933 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked drafts**, **7,343 pending**,
**7,345 runtime paths absent**. Checkpoint authority null/Ready false;
version `5d758becdc2891a3`.
Corrected-candidate serialized checks: validator 0 errors, 124 tests OK in 29.428s;
budget 941 files/950 entries/2,658,751 retained/2,675,433 inflated/1,336,507 ZIP bytes.
Final checks, source integration, actual public archive, signatures and exact-main
CI have separate receipts, not Android/phone/IME/playback acceptance.

No new assets, paid generation or media authority occurred.
At the inspected exact app commit `5c000bd`, canonical tag IDs `buildings`,
`entertainment`, `shopping`, `swimming` and previous `comparison`, `distance`,
`speed` lack explicit localized cases and fall through as raw tags.
This is a pinned-source app follow-up, not inspection or modification of concurrent
dirty app work. Keep technical IDs stable; ordinary activation/release remains gated.
Continue the remaining 238 N5 words and every safe frozen level/family,
including honest excluded listening drafts; the entire objective remains in progress.

## Reviewed source milestone 033: nature and outdoor activity

The [source record](translation-batches/033-nature-outdoor-activity-reviewed-source.json)
authors all 19 frozen N5 root texts completely and adopts **18 runtime words**.
All 933 accepted baseline runtime RAWs and earlier tracking records are unchanged.
The full unchanged [空 draft](translation-drafts/033-nature-outdoor-activity/words/空.md)
is excluded, **not C2 accepted**: its two actual remote-place caption questions
remain UNVERIFIED. Do not invent extra guards, silently drop its teaching, move
the frozen target or stop safe independent lanes. Its intended runtime-relative
links are preserved losslessly, not certified as standalone draft navigation.

The [cumulative evidence](translation-batches/033-nature-outdoor-activity-independent-review.json)
distinguishes actual reading from report delivery. The whole reviewer actually read
19 primary and 20 supporting full EN/RU pairs, all 640 compact answer rows,
41 selected complete lexical objects and five selected dictionary sections.
Its 21.4 KB native final report was auto-spooled to a forbidden OS-temp location
and was **not opened**. Visible C1/C3 CLEAN and C2 NEEDS FIX labels and observed
successful reading are retained honestly; no original full-report hash or
unread finding details are invented.

The independently returned focused report retains the original 17 direct pairs,
supports four additions — 走る–光る, 散歩–行く, 吹く–咲く/ぺらぺら —
and rejects an automatic 吹く–話す edge. Mould formation and empty/exaggerated talk
have actual source evidence, not merely a bud/flower analogy or shared vocal activity.
Dahl supplies historical attestation, not a modern-frequency claim; no Russian
rust assertion is approved. 空–遠く/遠い remain UNVERIFIED.
Actual complete Warodai articles do not support a search-generated purported
remote-place quote; their silence is not proof that the Japanese sense is impossible.

After the separately signed resolution freeze, only three new metadata lists change.
All 19 original learner bodies and 639 remaining captions/readings stay unchanged.
The exact changed-snapshot reviewer returns no significant issues after actually
reading eight complete pairs, eight semantic rows, three repeated lexical objects
and six selected new dictionary sections. Mechanical checks bind all 951 runtime
RAWs/639 pool rows and the lossless excluded draft, not fresh semantic reading
of all those objects. This supports the **18-runtime-unit boundary only**;
the original 19-unit scope is not globally CLEAN.
The excluded draft retains three of the original proposals; runtime has
**18 independently supported direct pairs**, without transitive category cliques.
Active guidance now bounds report/tool delivery without shrinking review scope.

Membership is **951 runtime objects**: 141 kanji/639 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images.
Word levels are 452 N5/54 N4/60 N3/19 N2/54 unlabelled:
**452 of 672 frozen N5 words are adopted; 220 remain**.
Fresh strict 8,278-entry progress: **951 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked media drafts**, **7,325 pending**,
**7,327 runtime paths absent**. The one complete C2-unverified word draft
is separately tracked inside pending, not counted as reviewed or as a third media draft.
Checkpoint authority null/Ready false; version `8a1515166740e2bd`.
Corrected checks: validator 0 errors, 124 tests OK in 31.551s;
budget 959 files/968 entries/2,704,908 retained/2,721,590 inflated/1,360,862 ZIP bytes.
Final checks, signed integration, public archive and exact-main CI have separate receipts.

No new assets or media authority occurred. At the exact inspected app `5c000bd`,
`activity`, `animals`, `leisure`, `motion` lack explicit localized cases and fall
through as raw tags. Preserve technical IDs; this is pinned-source follow-up only.
Concurrent dirty app and ordinary English checkouts remain untouched.
No phone/JapaneseIME/playback/new audio-package/C6/C7/default activation/release/
human-checkpoint approval follows. Continue the 220 remaining N5 words and every
other safe frozen level/family; isolate evidenced uncertainty instead of idling the corpus.

## Reviewed source milestone 034: hygiene and household

[Source 034](translation-batches/034-hygiene-household-reviewed-source.json)
adds all **12 complete N5 root lessons**: あびる, シャワー, お風呂, 風呂,
お手洗い, トイレ, せっけん, 洗う, 洗濯, 掃除, 歯, 磨く.
The exact frozen source remains `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.
All 951 accepted baseline runtime RAWs and old tracking rows remain unchanged.
The complete excluded 空 draft and its two C2-unverified questions remain intact
inside pending, not accepted or counted as a third reviewed media draft.

One [actual whole read-only review](translation-batches/034-hygiene-household-independent-review.json)
covers 12 primary and 18 supporting complete EN/RU pairs, all 651 actual compact
caption rows, 33 complete selected lexical query-object rows and nine selected
dictionary ranges from eight pages. These are not 651 complete articles, all API
response objects or whole pages. Successful reader outputs demonstrate those
exact ranges; the complete 6,185-byte native report is available, not an unread spool.
C1/C2/C3 are CLEAN within this bounded twelve-unit source review; no correction
or additional reviewer was needed.

Seven direct guards are retained: お風呂–風呂, お風呂–バス, 風呂–バス,
お手洗い–トイレ, 洗う–洗濯, 歯–年, 洗濯–休む.
The bath noun バス-1 is not the bus entry's place-name Bath.
Exact-written 歯 age readings support the bare-writing safeguard, but their
frequency remains unverified and no new primary N5 age reading is taught.
The named modern/精選 dictionaries explicitly support the refreshment/する
evidence for 洗濯–休む; this is not a blanket noun-to-する inference.
No 洗濯–遊ぶ, 磨く–練習 or automatic cleaning-family clique is established.
Natural Russian toilet/soap sense qualifiers exclude Russian-only outfit,
camera and email homonyms without deleting Japanese source meanings.
All substantive teaching behind sixteen local source links is retained:
four available/in-batch links remain, twelve absent optional wrappers alone go.

Membership is **963 runtime objects**: 141 kanji/651 words/141 strokes/2 articles/
22 counter files/one grammar set/2 scene catalogs/3 images.
Word levels: 464 N5/54 N4/60 N3/19 N2/54 unlabelled;
**464 of 672 frozen N5 words adopted, 208 remain**.
Fresh strict 8,278-entry progress: **963 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked media drafts**, **7,313 pending**,
**7,315 runtime paths absent**. Version `8544136ac90cafb4`;
checkpoint authority null/Ready false.
Candidate checks: validator 0 errors, 124 tests OK in 29.284s;
budget 971 files/980 entries/2,732,926 retained/2,749,608 inflated/1,376,093 ZIP bytes.
Final serialized checks, signed main integration, actual public archive and
exact-main CI are separately evidenced; text review is not device acceptance.

No new assets, paid media or package authority. At exact app pin `5c000bd` only,
the new canonical `facilities` tag lacks an explicit localized hint case and
falls back raw; this is app follow-up, not a claim about concurrent current app.
Concurrent dirty app and ordinary English checkouts remain untouched.
No phone/JapaneseIME/playback/C6/C7/default activation/release/human-checkpoint
approval follows. Continue the 208 remaining N5 words and every other safe
frozen level/family; keep the full objective in progress.

## Reviewed source milestone035: daily life, work and rest

[Reviewed source035](translation-batches/035-daily-life-work-rest-reviewed-source.json)
and [actual independent review](translation-batches/035-daily-life-work-rest-independent-review.json)
adopt fourteen complete N5 words: 起きる, 寝る, 座る, 仕事, 働く, 勤める,
休み, 夏休み, 住む, 家庭, 帰る, 一緒, 同じ, and required provider 返す.
All fourteen full frozen source units, Japanese examples/readings/forms, qualifiers,
canonical types/tags and attributions are preserved. In particular 仕事 retains
the source's explicit app-specific on-first mixed-reading category and its
nonhistorical reading-guide caveat, not an invented pure-on etymology.

The whole reviewer actually read 27 complete bilingual pairs, 665 compact answer
rows, 34 complete selected lexical objects and four selected dictionary ranges.
Its complete 6,796-byte native report retains all fifteen proposals and finds
one missing direct 家庭–門 safeguard: the exact-written 門（かど） noun has
a family sense. Signed evidence/resolution freeze precedes that correction.
The narrow changed-snapshot recheck reads two complete pairs, three complete
selected objects and four coupled instruction lines; its complete 2,942-byte
native report resolves F1 with bounded C1/C2/C3 CLEAN.
The whole reviewer was synchronous and could not receive a follow-up message;
only one fresh, narrower reviewer was used after it became idle, not a fleet.
Other C1/C3 and fifteen-guard decisions carry forward because all bodies/captions
and 976 other runtime RAWs are unchanged, not because a second whole review occurred.
All sixteen safeguards are direct; no rest/leisure/season/family/transitive clique.
All 28 local source links are enumerated: ten retained, eighteen absent optional
wrappers removed without losing substantive teaching or supplied readings.

All 963 baseline runtime RAWs/tracking rows and the full excluded C2-unverified
空 draft remain unchanged. Membership is **977 runtime objects**:
141 kanji/665 words/141 strokes/2 articles/22 counter files/one grammar set/
2 scene catalogs/3 images. Word levels: 478 N5/54 N4/60 N3/19 N2/54 unlabelled;
**478 of 672 frozen N5 words adopted, 194 remain**.
Fresh strict 8,278-entry progress: **977 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked media drafts**, **7,299 pending**,
**7,301 runtime paths absent**. Version `b4d1c08e122a2bbb`;
checkpoint authority null/Ready false.
Corrected candidate checks: validator 0 errors, 124 tests OK in 30.265s;
budget 985 files/994 entries/2,769,242 retained/2,785,924 inflated/1,394,984 ZIP bytes.
Final serialized checks, signed main integration, actual public archive and
exact-main CI remain separately evidenced, not device acceptance.

No new assets or canonical tags, app/ordinary EN edits, paid generation,
new media-package authority, phone/IME/playback/C6/C7/default activation/release/
human-checkpoint approval. Continue the 194 remaining N5 words and every other
safe frozen level/family; the full finite objective remains in progress.

## Reviewed source milestone036: state changes and operations

[Reviewed source036](translation-batches/036-state-changes-operations-reviewed-source.json)
and [actual independent review](translation-batches/036-state-changes-operations-independent-review.json)
accept 14 complete frozen N5 words: 開く、開ける、閉まる、閉める、消える、消す、
始まる、止まる、並ぶ、並べる、付ける、締める、押す、引く.
All Japanese examples/readings/forms, technical IDs/classification/tags/levels,
source qualifiers and substantive teaching remain. Twenty unavailable optional
link wrappers alone were removed; seven adopted links remain.

The actual whole reviewer read **34 full EN/RU pairs** (14 primary/20 supporting),
**679 compact captions**, **55 complete selected lexical objects** and
**four selected dictionary ranges**. It retained 24 direct proposals but returned
C2/C3 NEEDS_FIX plus unverified 開く–広い, not clean first-pass acceptance.
The actual narrow recheck read five full pairs, two complete opening objects,
two fresh selected dictionary ranges, both append-only errata and four new guidance lines.
It resolved «трёхзначной статье» to the intended three-sense wording and corrected
both historical rationales' misquotation of actual 終わる «заканчиваться; заканчивать»
without rewriting signed originals or the accepted baseline article.
Fresh Japanese gap-emergence/increase and Russian static considerable-width evidence
establish no additional 開く–広い guard. Two separately evidenced opening/beginning/ending
proposals are independently retained: **26 direct pairs total**.
The euphemistic ending use is a bounded conservative bare-writing safeguard;
modern frequency remains unverified, not asserted as ordinary N5 usage.
The focused verdict does not pretend to repeat the whole review.

All **977 baseline runtime RAWs/tracking rows** and the complete excluded C2-unverified
空 draft remain unchanged. Membership is **991 runtime objects**:
141 kanji, 679 words, 141 strokes, two complete articles, 22 counter files,
one grammar set, two scene catalogs and three images.
Words: **492 N5 /54 N4 /60 N3 /19 N2 /54 unlabelled**;
**492 of 672 frozen N5 words adopted, 180 remain**.
Fresh strict 8,278-entry progress: **991 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked media drafts**, **7,285 pending**,
**7,287 runtime paths absent**. Version `c7e6d0d7021e3248`;
checkpoint authority null/Ready false.
Corrected candidate: validator 0 errors, 124 tests OK in 31.927s;
budget 999 files/1008 entries/2,810,316 retained/2,828,531 inflated/1,415,548 ZIP bytes.
Final serialized checks, signed main integration, actual public archives and exact-main
CI remain separately evidenced, not device acceptance.

No new assets. Canonical `attachment` stays unchanged; its raw fallback is verified only
at pinned app `5c000bd`, not asserted for the concurrent dirty current app or a device.
Owner-requested README/old-sequence/current-C6 clarification distinguishes reviewed source
coverage from ordinary/default activation; original receipts and the five genuinely unlocked
native Word Type passes remain explicit. Later actual native findings can require
affected-batch correction and independent re-review without blocking unrelated source authoring.
No app/ordinary EN edits, paid generation, new media-package authority, phone/IME/playback/
C6/C7/default activation/release/human-checkpoint approval.
Continue the 180 remaining N5 words and every other safe frozen level/family;
the full finite objective remains in progress.

## Reviewed source milestone037: communication, learning and writing

[Reviewed source037](translation-batches/037-communication-learning-reviewed-source.json)
and [actual independent review](translation-batches/037-communication-learning-independent-review.json)
accept 16 complete frozen N5 words: 言う、話、声、呼ぶ、答える、質問、問題、意味、
教える、習う、覚える、忘れる、頼む、作文、文章、テスト.
All Japanese teaching/examples/readings/forms, stable metadata IDs/levels/tags,
qualifications and attributions remain. Seventeen adopted local links remain;
only 24 unavailable optional wrappers were removed, without deleting teaching.

The actual whole reviewer read **35 complete EN/RU pairs**, **695 compact captions**,
**61 complete selected lexical objects** and **four selected dictionary ranges**.
It returned C1/C3 CLEAN, C2 NEEDS_FIX, the missing direct 作文–書く guard and two
UNVERIFIED learning-guard rationales. The full 12,386-byte native report and successful
reading trace are preserved, including its disclosed requested transfer-limit miss.
The actual focused reviewer read **five complete pairs**, **five fresh selected ranges**,
the complete original report, proposals and three observation-bound guidance lines/one link.
It independently resolves the writing guard, retains 覚える–勉強 with new actual
Japanese/Russian acquisition-sense evidence, and approves withdrawing unestablished
覚える–習う. It considered the rehearsal sense, not a blanket never-overlap claim.
The Russian acquisition definition has no usage example; none is invented as attested.
Other 22 original direct decisions carry on unchanged content: **24 guards total**.
The focused verdict does not pretend to repeat the whole review.

All **991 accepted baseline RAWs/tracking rows**, all 16 full learner bodies/695 captions
and the complete excluded C2-unverified 空 draft remain unchanged by the correction.
Membership is **1007 runtime objects**: 141 kanji, 695 words, 141 strokes,
two complete articles, 22 counter files, one grammar set, two scene catalogs and three images.
Words: **508 N5 /54 N4 /60 N3 /19 N2 /54 unlabelled**;
**508 of 672 frozen N5 words adopted, 164 remain**.
Fresh strict 8,278-entry progress: **1007 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked media drafts**, **7,269 pending**,
**7,271 runtime paths absent**. Version `78b9999fcefcb597`; checkpoint authority null/Ready false.
Actual corrected checks: validator 0 errors, 124 tests OK in 30.812s and budget passed.
Final serialized checks, signed integration, actual archives and exact-main CI
remain separate publication evidence, not native/device acceptance.

No new assets. Canonical `memory`, `requests`, `study` IDs remain unchanged;
raw fallback is observed only at pinned app `5c000bd`, not concurrent app/device rendering.
Historical native passes and outstanding C6/C7/media/default-activation gates remain
separate. Later actual findings may require affected-batch corrections/re-review,
not a speculative stop to unrelated authoring.
Continue the 164 remaining N5 words and every other safe frozen level/family;
the entire finite objective remains in progress.

## Reviewed source milestone038: quantities, measurements and comparison

[Reviewed source038](translation-batches/038-quantities-measurements-reviewed-source.json)
and [actual independent evidence](translation-batches/038-quantities-measurements-independent-review.json)
cover 18 complete frozen word lessons: キロ、キログラム、グラム、メートル、
キロメートル、いくら、幾つ、たくさん、大勢、全部、みんな、皆さん、
いろいろ、いちばん、もっと、より、最も、最初.
The first 16 are N5 roots; the last two are N4 providers required by the actual
source いちばん negative references, frozen before authoring.
All source examples/readings/forms, stable metadata/classification/tags/levels,
qualifications and attributions remain. Four adopted local links remain;
only twelve unavailable optional wrappers were removed, without deleting teaching.

The initial reviewer actually read 39 complete pairs, 713 compact captions,
68 complete candidate objects and six ranges, but returned only 52 bytes with
no linguistic facets/scope/rationale. Its report remains NOT_REPORTED, not acceptance;
the synchronous reviewer could not receive the actual report-completion follow-up.
The subsequent linguistic adjudicator actually read **all 18 new pairs plus 12 full
support pairs**, **713 compact rows**, **68 candidate query-object rows**
(65 lexical and three non-adopted Wikipedia-only, not 65 unique lemmas),
all 24 proposals and six selected dictionary ranges.
Its actual 8,806-byte report gives C1/C3 CLEAN and supports 21 direct necessities,
but leaves three ordinary-present-day necessities UNVERIFIED.

The bounded recheck actually read **six full pairs**, **five selected ranges**,
all three evidence-qualified proposals, both complete prior reports and four new
methodological lines. Its actual 5,062-byte report independently accepts
大勢–力, 大勢–左右 and 最も–一 solely as **conservative, directly dictionary-grounded
protections for bare-written prompts**. It does not establish modern frequency or
ordinary N5-quiz necessity; those three stronger claims remain UNVERIFIED and unasserted.
No older report is relabelled CLEAN. This is substantive independent assessment
of a smaller adoption boundary, not a title-only or administrative status change.
There are **24 direct guards: 21 supported necessities and three qualified conservative
adoptions**, not a transitive clique. No current usage example is invented.

All **1007 accepted baseline RAWs/tracking rows**, all 18 new full learner bodies/metadata,
713 captions and the complete excluded C2-unverified 空 draft remain unchanged by the
documentation-only qualification. Membership is **1025 runtime objects**:
141 kanji, 713 words, 141 strokes, two complete articles, 22 counter files,
one grammar set, two scene catalogs and three images.
Words: **524 N5 /56 N4 /60 N3 /19 N2 /54 unlabelled**;
**524 of 672 frozen N5 words adopted, 148 remain**.
Fresh strict 8,278-entry progress: **1025 reviewed-current**, **no partial**,
**two excluded reviewed runtime-blocked media drafts**, **7,251 pending**,
**7,253 runtime paths absent**. Version `c3444eaf9a65b497`; checkpoint authority null/Ready false.
Actual candidate manifest/validator/124 tests/budget passed. Final accepted-tree checks,
signed integration, actual public archives and exact-main CI remain separate receipts.

No new assets. Canonical `address`, `degree`, `measurement`, `order`, `particle`,
`prefix`, `unit`, `usually-kana` IDs remain unchanged; unmapped fallback is observed
only at immutable app `5c000bd`, not concurrent app/device rendering.
The failed generic キロ dictionary URL returned HTTP404, not lexical absence evidence;
actual captured prefix/kg/km evidence remains. EN-only 何 is still pending, not an
invented Russian pair or runtime placeholder.

Append-only historical erratum: the 037 publication receipt's `limits[3]` says
`508/672N5words and991/8278objects`. Its object subtotal should be **1007**, as established
by the actual 037 membership/manifest/archive evidence; the N5 subtotal 508 is unchanged.
The immutable 037 receipt is preserved rather than rewritten.

Historical native passes and specific remaining C6/C7/media/default-activation gates
remain separate. Later actual findings may require affected-batch correction/review,
not a speculative stop to unrelated authoring.
Continue the 148 remaining N5 words and every other safe frozen level/family;
the entire finite objective remains in progress.

## Current continuation status after batch 128

The qualified batch-128 source candidate adds complete Russian lessons and exact
frozen stroke assets for 決, 治, 法, 泳, 洗, 活 and 流, plus only the 14
preauthorized navigation links on existing word pages. Its signed candidate
commit is `c21b01f4e1d2c1247d89ae4d5951ab00bf9b5c0a`; source remains frozen at
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`. Candidate and qualified review
receipts are in `docs/translation-batches/128-decide-govern-law-swim-wash-kanji-*`.

The current branch progress is **2,448 reviewed-current**, **2 reviewed but
runtime-blocked media drafts**, and **5,828 pending** of 8,278 frozen runtime
entries. It includes 470 kanji, 470 stroke files and 1,478 words. This is a
qualified source-content checkpoint only: C1/C3 are bounded to the seven
lessons and the authorized navigation changes; C2 remains UNVERIFIED for all
21 ordinary active-negative quiz directions. No grading guard, runtime
activation, device or release approval is implied. `checkpointAuthority` remains
null, `checkpointReady` remains false, and full translation is not complete.

Batch128 is now integrated and verified as recorded above. Batch129 begins from
the exact published main baseline; its pre-mutation freeze selects the first four
remaining frozen N3 roots, 浮/消/深/済, and their direct provider closure. This is
not N3 completion: continue through every remaining safe frozen family and do not
treat a candidate milestone or a convenient batch boundary as completion.

## Previous continuation after batch 133

Batch 133's qualified source candidate is `a003aac9d3c0659d5d5d72ec1a220e43567e3d5c`,
based on published baseline `dcb272dec45c8a64ba951d7fff56209ae1945660`, with source
still frozen at `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. It adds complete lessons
and byte-identical frozen strokes for 王, 現 and 球, plus only the five
preauthorized NAV-only word-page changes. The initial reviewer identified an
unexplained on’yomi/kun’yomi terminology issue; a focused, read-only follow-up
confirmed that the three concise explanations resolve that finding. The original
review’s C1 evidence boundary remains; C2 remains UNVERIFIED for all nine direct
ordinary quiz directions. Neither review grants grading, runtime, device, media,
release or ordinary-activation approval.

The candidate progress snapshot is **2,496 reviewed-current**, **2 reviewed but
runtime-blocked media drafts**, and **5,780 pending** of 8,278 frozen runtime
entries: 494 kanji, 494 strokes and 1,478 words. Content version is
`9889ff4126ffc763`; fresh candidate manifest, validator, 124 tests and content
budget checks passed. `checkpointAuthority` remains null and `checkpointReady`
false.

Batch 133 is integrated via PR #19 at merge commit
`e87fcd4b5f68a4babe069549e87b7fe5c9e0c61a`. The exact-main
`Validate Russian content` push run completed successfully. Actual public commit
and main ZIP and tar.gz exports each match all 2,504 local Git-archive file
bodies; all 2,496 runtime manifest hashes and 494 frozen stroke RAWs were
verified, and root license/notice files are present. All four protected refs
remain unchanged. Details and distinct archive hash domains are recorded in
`docs/translation-batches/133-king-presence-ball-kanji-publication-verification-001.json`.
No grading, runtime activation, device, media, release, or ordinary-activation
approval is implied. The finite translation remains in progress; continue with
batch 134 and all remaining safe frozen families.

## Historical batch 134 candidate checkpoint

Batch134 selects the next five frozen N3 kanji in source order: 煙, 猫, 産,
留 and 番. Its signed pre-mutation freeze is `01c7952e6b53f858a8f4e362b73c4a05952a5f06`;
the complete candidate is `f0926bed8a77f0bd6582e4853b0b1a44beca0192` on
`full-ru-134-smoke-cat-birth-stay-turn-kanji`. The frozen EN source remains
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

The candidate contains five complete Russian lessons, five byte-identical
frozen strokes, and 14 preauthorized navigation-only word-page changes. The
independent review found no confirmed correction: C1 and C3 are CLEAN within
their exact read scope; C2 scope/navigation is consistent, while all 15
ordinary negative/fallback directions remain **UNVERIFIED**. No grading,
runtime, media, device, release or ordinary-activation approval is implied.
Fresh serial checks passed: manifest `f522e673bf62e03a`, validator 0 errors,
124 unit tests, and budget 2,514 files / 2,523 entries.

Candidate progress is 2,506 reviewed-current, 2 runtime-blocked drafts and
5,770 pending of 8,278. `checkpointAuthority` remains null and
`checkpointReady` false. The candidate is pushed but integration, exact-main
CI and public archive verification are pending. After completing those steps,
continue with batch135 and every remaining safe frozen family; this is not
finite completion.

## Current continuation after batch 146 publication

Batch 146 (`越`, `路`, `辞`, `込`, `迎`, `返`, `迷`, `追`, `退`, `逃`) is
qualified and published from frozen source commit
`6af98cb717755690a9ca793e5454a96ebd7a8f9f`. The corrected candidate
`8788270a25458e6eb06e41eaf8af0e7cb6e32eba` preserves the previously omitted
comparison character `還る`; its independent review found no remaining
actionable findings. Signed owner acceptance commit
`ae33e2bb5634298db274e95f4cec64380f8e5cc5` is on `main` and the short-lived
batch branch. Exact-main `Validate Russian content` run
[43008572740](https://github.com/stop-cran/learning-japanese-ru/actions/runs/43008572740)
completed successfully. Protected pilot refs are unchanged.

The published progress ledger records 2,662 reviewed-current, two
runtime-blocked drafts and 5,614 pending of 8,278. `checkpointAuthority`
remains null and `checkpointReady` false. All 30 direct negative/fallback
directions remain **UNVERIFIED**; no transitive closure or quiz-safety claim is
made. No runtime, device, media, activation, release or full-completion
approval is implied. Continue with the next contiguous dependency-closed
frozen-source batch; this is not finite completion.

## Current continuation after batch 147 publication

Batch 147 (`途`, `速`, `連`, `進`, `遅`, `遊`, `過`, `違`, `遠`) is qualified
against frozen source commit `6af98cb717755690a9ca793e5454a96ebd7a8f9f` and
published at `3d422af3892917a69321a98cade065aff102eb4d`. The candidate
`918a5e8ad3045fe181a1e18cf0196d4e58f7ea7b` passed independent review with no
actionable findings, and exact-main `Validate Russian content` run
[43012517674](https://github.com/stop-cran/learning-japanese-ru/actions/runs/43012517674)
completed successfully. Its 15 existing word-page changes are reciprocal
navigation only; the unavailable `連休` and `遅刻` targets remain visible
Japanese text, with no word pages added.

The progress ledger records 2,680 reviewed-current, two runtime-blocked drafts
and 5,596 pending of 8,278. `checkpointAuthority` remains null and
`checkpointReady` false. All 27 direct negative/fallback directions remain
**UNVERIFIED**; no transitive closure or quiz-safety claim is made. No runtime,
device, media, activation, release or full-completion approval is implied.
Continue with the next contiguous dependency-closed frozen-source batch; this
is not finite completion.

## Previous continuation after batch 150 publication

Batch 150 (`靴`, `頂`, `頭`, `頼`, `顔`, `願`, `類`, `飛`, `首`, `馬`) is
qualified against frozen source commit `6af98cb717755690a9ca793e5454a96ebd7a8f9f`
and published by pull request
[#32](https://github.com/stop-cran/learning-japanese-ru/pull/32) at
`48dbf194db2c6e6d6cbaab0b3cba47fdf715d9bd`. Candidate
`724547d29590c06c8ab2d461c164a51df97b42c5`, content version
`befb7eb96f13cee1`, passed independent read-only review with no actionable
findings. All 20 new registrations and 13 navigation-only word changes match
the authorized manifest delta. The validator, all 124 unit tests, and the
content-budget check passed; exact-main CI run
[43043911004](https://github.com/stop-cran/learning-japanese-ru/actions/runs/43043911004)
completed successfully.

The progress ledger records 2,740 reviewed-current, two runtime-blocked drafts
and 5,536 pending of 8,278. `checkpointAuthority` remains null and
`checkpointReady` false. All 30 direct negative/fallback directions remain
**UNVERIFIED**; no transitive closure or quiz-safety claim is made. No runtime,
device, media, activation, release or full-completion approval is implied. The
Kolobok lead for the protected 空 question remains separately qualified in
[the post-publication lead record](translation-batches/149-sora-kolobok-lead-qualification-001.json);
both 空 pairs remain C2 **UNVERIFIED**. At that point the next source slice was
N3 positions 366–367; Batch 151 and the subsequent N2 transition supersede that
continuation below. This is not finite completion.

## Current continuation after Batch 152 publication

Batch 152 is published through [PR #35](https://github.com/stop-cran/learning-japanese-ru/pull/35)
at `0a9efd6f401ea6312e43876c5b7b07471200dbd0`. The owner-signed runtime
candidate is `80e4e1d0d13caea2fcadb80345fc272441f3dcc4`; the signed acceptance
head is `e130049afddf7291fbf276a85699dbd0b3f301aa`. PR validation run
[43062985009](https://github.com/stop-cran/learning-japanese-ru/actions/runs/43062985009)
and exact-main CI run
[43063177706](https://github.com/stop-cran/learning-japanese-ru/actions/runs/43063177706)
passed. The publication record is
[152-n2-batch-01-publication-verification-001.json](translation-batches/152-n2-batch-01-publication-verification-001.json).
Qualified progress is **2,774 reviewed-current / 2 runtime-blocked /
5,502 pending of 8,278**, with content version `34b5c4ac31854637`.

Continue with Batch 153, the next 15 entries in the frozen community-N2
snapshot: 個倍停傾像億兆児党兵冊再凍刊刷 (positions 16–30 of 365 additions;
珍 and 短 remain pre-existing). This community list is not an official JLPT
syllabus. Freeze and review this next scope against the same source revision
before authoring.

All 45 Batch 152 direct distractor directions remain **UNVERIFIED** for
negative/fallback behavior; no transitive closure or quiz-safety claim is made.
The protected 空 pairs, runtime/device/media/activation/release gates, and
full-completion status remain separate and unchanged.

## Protected 空 draft amendment after Batch 153 merge

At the user's request the excluded
[空 draft](translation-drafts/033-nature-outdoor-activity/words/空.md) gains the
required `[空](../kanji/空.md)` link and one JMdict-sourced paragraph on the
secondary sense «далёкое место» with the expression 旅の空. See the
[amendment](translation-batches/033-nature-outdoor-activity-sky-draft-amendment-001.json)
and [dictionary evidence](translation-batches/033-nature-outdoor-activity-sky-sense-evidence-qualification-001.json).
The draft stays excluded and runtime-absent, `words/空.md` stays pending, and no
quiz guard, activation or release authority is added.

The independent focused review of this amendment is complete:
[review 004](translation-batches/033-nature-outdoor-activity-independent-review-004.md)
approved it for the excluded draft only and left both 空–遠く and 空–遠い
**UNVERIFIED** in the Japanese→Russian and Russian→Japanese directions, with no
clean or exclusion inference and no new guard. Source-handling corrections made
to the supporting records after that review, and their independent follow-up
review, are recorded in the
[provenance follow-up](translation-batches/033-nature-outdoor-activity-independent-review-004-followup.md).
Review 004 does not resolve C2.
Resolving it still needs direct Russian-usage evidence or adjudication of the
actual quiz titles of 遠く and 遠い against 空, and none has been found so far.
Until then both pairs stay C2 **UNVERIFIED** and runtime acceptance stays blocked.

Snapshot: learning-japanese-ru `4abbf09` (parent `9ee57cf`, branch full-ru-176-words-15); working tree clean (no uncommitted changes). EN source: learning-japanese-en-frozen `6af98cb`.
Scope: all 30 new word articles (椋 梨 縁 端 暮れ 末 底 尻 しっぽ 頂上 トップ 先端 梢 梓 桑 桐 桂 書物 図書 冊子 栞 茶 茶色い 栗 豊富 豊か 栄える 柳 支える 助ける) read in full beside their EN originals; word-diff of the 6 navigation-only edits (kanji/冊, 助, 頂; words/榛, 蚕, 貧しい); manifest diff and file list. The intake JSON was not read (blind review; author rationale). Tools: rutools/link_parity.py (36 paths, no output = parity), rutools/word_title_screen.py (all 30 words vs whole RU pool), plus my own scan of inbound EN→RU link counts to the 30 words across every RU page that has an EN counterpart (no mismatches). Reviewer: blind single reviewer; model not recorded.
Verdicts: correctness NEEDS FIX (2 low); scoped coverage CLEAN; comprehensibility CLEAN; quiz safety NEEDS FIX (1 medium, 2 low).

Findings:
F1; Medium; quiz safety; words/支える.md:9 (and words/賛成.md:3 title «одобрение; поддержка»). 支える «поддерживать; подпирать» and 賛成 «одобрение; поддержка» share «поддерж-». 賛成 is a する-noun (賛成する = support a proposal), so under the する-noun action rule (RU instructions ~266) «поддерживать» is a defensible answer for 賛成 and «поддержка» a defensible answer for 支える (emotional support, example 家族が私を支えてくれました). No direct pair on either side; the overlap is inherited from EN ("support; hold up" vs "agreement; support"), which left it unguarded. Remedy: `quiz_exclusions: [持つ, 助ける, 賛成]`. Evidence: JMdict 賛成 "approval; agreement; support; favour", Suru verb (https://jisho.org/word/賛成); 支える "to support; to prop; to sustain" (https://jisho.org/word/支える). Confidence: high.

F2; Low-Medium; quiz safety; words/暮れ.md:9. 暮れ is guarded against every RU «конец» title (終わり, 最後, 仕舞い; 末 guards it from its side), but not against 端 «край; конец; кончик», which carries the same bare «конец» segment. JMdict gives 暮れ sense 2 "end; close", so a bare «конец» option is defensible for the 暮れ prompt by the same reasoning the author used for the other three. The 端 body limits its «конец» to a spatial meaning, but quiz answers show only the title. Remedy: `quiz_exclusions: [夕方, 暮れる, 終わり, 最後, 仕舞い, 端]`. Evidence: https://jisho.org/word/暮れ (sense 2); word_title_screen output "!! 暮れ ~ 端 stem=['конец']". Confidence: medium.

F3; Low; quiz safety; words/トップ.md:9. トップ «верх; лидирующая позиция» vs いちばん «первый; самый»: both dictionaries list "first place" (JMdict 一番 "number one; first; first place"; トップ "top position"), and the RU body itself says «первое или лидирующее положение». The guard is optional but conservative; EN left this pair unguarded too. Remedy: `quiz_exclusions: [頂上, 上, いちばん]`. Evidence: https://jisho.org/word/一番 , https://jisho.org/search/トップ . Confidence: medium (whether the guard is needed is a judgement call).

F4; Low; correctness; words/栗.md:43-44. The text says «конский каштан — другое растение с несъедобными плодами, по-японски トチノキ». The usual Russian «конский каштан» (Aesculus hippocastanum) is セイヨウトチノキ/マロニエ in Japanese. トチノキ (A. turbinata) seeds are toxic raw but are eaten after leaching (栃餅), so «несъедобные плоды, по-японски トチノキ» is inaccurate. The 栗 teaching point itself is unaffected. Remedy: «Русское «каштан» часто означает конский каштан (род *Aesculus*; по-японски トチノキ, европейский вид — マロニエ); его сырые семена ядовиты. 栗 — это съедобный каштан.» Evidence: ja.wikipedia トチノキ ("有毒"; "澱粉質の大きな種子を付け、食用にした記録が全国的に残る"; マロニエ = セイヨウトチノキ). Confidence: high.

F5; Low; correctness/comprehensibility; words/豊か.md:40-41. «В отличие от русского «богатый», 豊か само по себе не называет человека с деньгами: для этого есть 金持ち». A learner can read this as "豊か cannot describe a wealthy person". That contradicts JMdict sense 2 "rich; wealthy; affluent; well-off" and the card's own title «зажиточный». The intended point is part of speech: Russian «богатый» can be a noun, 豊か cannot. Remedy: «Русское «богатый» может употребляться и как существительное («богатые»); 豊か — только な-прилагательное, а человека с деньгами называет существительное 金持ち（かねもち）.» Evidence: https://jisho.org/word/豊か . Confidence: medium-high.

Checked and found clean:
- Japanese examples and readings in all 30 files match EN verbatim.
- Every EN sense, note, example and citation is kept.
- EN links are dropped only where the RU target does not exist: 境, 表面, 腰, 印刷, 出版, 杉, 不足, たっぷり, 川柳, 援助, 無し, and the kanji pages for 梨/椋/梓/桑/桐/桂/梢/栗/柳/栄/端/縁/尻/底/栞/豊 (all absent).
- The 6 navigation edits add brackets only, at EN link positions; no other text changed.
- No generated files (`__pycache__`/.pyc) are committed; manifest hashes cover the edited pages.
- Added guards all have a basis: 端→終わり/最後/仕舞い; 暮れ→夕方/暮れる/終わり/最後/仕舞い; 末→とうとう («в итоге»); 尻→後ろ («зад»); 書物→図書; 茶→お茶 (identical «чай»); 茶色い→茶色; 豊か→金持ち (conservative); 栄える→発展 (JMdict 発展 includes "flourishing"); 支える→持つ/助ける. None is clearly unjustified.
- Russian plant names are established: багрянник японский, берёза граболистная, павловния войлочная/императорское дерево (ru.wikipedia).
- English-only contrasts are re-expressed in Russian rather than calqued: «конец»/«край» in 端, «сумерки» in 暮れ, «зад» vs 後ろ in 尻, «верхушка» in 梢, «верх/топ» in トップ, «богатый» in 豊富/豊か, «держать» vs 持つ in 支える, dative «помогать кому» vs を in 助ける.

Optional:
- words/冊子.md:18 «На стойке регистрации» for 受付 sounds hotel/airport-specific. «На ресепшене» or «В регистратуре» would fit general reception better.
- 豊富 «обильный» vs 多い «много; многочисленный»: EN left this unguarded and it is borderline, so no change is required.
- 暮れ «сумерки» vs 晩 «вечер; ночь» (夕方 already guards 晩/夜): JMdict glosses 暮れ as dusk/nightfall, not evening, so no guard is required.

Limits:
- The hedged claim about the Russian name of *Aphananthe aspera* in 椋 is not verified against a Russian botanical source; ru.wikipedia has no «Афананте» page.
- Kotobank/Weblio citation URLs were not re-fetched; they are unchanged from EN.
- No validator, generator or budget commands were run.
- Grammar and naturalness were judged by the reviewer, not by a native speaker.

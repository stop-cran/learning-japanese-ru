Snapshot: RU `C:\Users\romanko\repos\learning-japanese-ru`, branch `full-ru-175-words-14`, candidate e6c63f6 (parent 5c4f4fe); worktree clean (no uncommitted changes). EN frozen source 6af98cb.
Scope: All 30 new word articles (岸 湖畔 流す 注ぐ 浴びせる 沈める 水稲 歳 欧州 橘 油 石油 脂 ビニール プラスチック ナイロン 樹脂 榛 達する 至る 極める 材料 材木 木材 楠 紅葉 楓 椿 骨 椎骨) read in full side by side with EN originals; navigation diffs in kanji/岸.md, kanji/歳.md, words/畔.md, words/筋肉.md (word-diff); manifest.json diff; commit file list. Tools: rutools/word_title_screen.py (30 words), rutools/link_parity.py (34 paths), grep of all RU word titles for the cluster terms. Blind: author report and prior reviews not read. Reviewer model: not stated by harness.

Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility NEEDS FIX (1 minor); quiz safety NEEDS FIX (2 minor).

Findings:
F1; minor; quiz safety; words/ビニール.md:8 (front matter has no quiz_exclusions).
  Claim/impact: title «винил; полиэтилен». In Russian «винил» colloquially means vinyl records (the card itself says so at line 39), and RU レコード has title «грампластинка». So a レコード prompt can offer «винил; полиэтилен», and a learner could defend it as correct. The reverse direction is not correct, because JMdict limits the record sense to バイナル. EN has no guard, because this is a Russian-specific polysemy.
  Remedy: insert after line 8: `quiz_exclusions: [レコード]`
  Evidence: ru.wiktionary «винил» sense 2, разг. «то же, что грампластинка» (https://ru.wiktionary.org/wiki/винил); JMdict 1105580 via https://jisho.org/api/v1/search/words?keyword=ビニール (sense 2 «vinyl record» restricted to バイナル).
  Confidence: medium. The second segment «полиэтилен» marks the label as a material, which reduces the risk.
F2; minor; quiz safety (precedent consistency); words/水稲.md:8.
  Claim/impact: existing 稲 «рис (растение)» directly guards ご飯 «приготовленный рис; приём пищи» over the shared «рис». The new 水稲 «заливной рис» guards 稲, 米 and 田んぼ but not ご飯. Under the precedent rule, the same «рис»-segment guard is expected. A ご飯 prompt offering «заливной рис» is a weak but real risk for beginners who read only «рис».
  Remedy: `quiz_exclusions: [稲, 米, ご飯, 田んぼ]`
  Evidence: words/稲.md quiz_exclusions [米, ご飯]; words/米.md [ご飯, メートル]; words/ご飯.md title.
  Confidence: medium-low. Precedent-based; semantically 水稲 is a crop, not cooked rice.
F3; minor; comprehensibility; words/脂.md:37-38.
  Claim/impact: «Широкий перевод «масло» не делает его обычным японским словом для пищевого жира.» This calques EN "Its broad English oil label". The RU 石油 card is titled «нефть» and is never translated as «масло», so the sentence refers to a translation the learner has never seen.
  Remedy, replace lines 37-38 with: `[石油](石油.md)（せきゆ）относится к нефти, а в разговорной речи — к керосину. Знак 油 «масло» в его записи не делает его обычным японским словом для пищевого жира. 脂肪 — ещё одно полезное слово для жира, но`
  Evidence: words/石油.md:4 title «нефть»; EN words/脂.md "Its broad English oil label".
  Confidence: high.

Verified without defect (selected):
- Japanese examples and kana readings are kept verbatim in all 30 files. Tense, polarity and register of the translations are correct.
- Russian-specific replacements of English-only contrasts are true and keep the Japanese teaching rule:
  - 岸: «берег» does not specify the body of water.
  - 油: «маслянистый»; also «масло» = バター.
  - 石油: «каменное масло».
  - 歳: «лет» is used for both age and a period of time.
  - 水稲: Russian «рис» covers both plant and grain.
  - 樹脂: «смола» also covers tar and bitumen.
  - ビニール: «винил» = record.
  - プラスチック: «пластичный».
  - 材料: «материалы» = 資料.
  - 極める: に vs を with Russian «достичь».
- «заливной/суходольный рис» is established terminology (agroatlas.ru, Oryza sativa). «ликвидамбар формозский», «камелия сасанква», «лещина обыкновенная» and «позвонок» are standard.
- Coverage: every EN sense, note, example and dictionary citation is kept. Link drops (湖/畔/浴/欧/ヨーロッパ/流れる/涙/袋 etc.) correspond only to absent RU cards; link_parity reports no LOST over 34 files.
- Navigation edits: the word-diff shows only `[X](...)` brackets added at EN link positions; no other text changed. The kanji/歳 EXTRA 二十歳 link is pre-existing and not in this diff.
- Quiz guards:
  - All EN exclusions are retained.
  - RU-specific additions are justified: 流す→浮かべる (shared «пускать … вод-»), 油→バター («масло»), 歳→年/二十歳 («возраст/лет»), 水稲→米/田んぼ (shared «рис», «залив-»).
  - Checked pairs that need no guard: 湖畔/海岸 (lake ≠ sea), 楠/大木, 材料/木綿, 達する/手段, 極める/以内, 紅葉/赤・色・緑, 欧州/外国, 骨/肉・体, 椎骨/背中.
  - 紅葉–楓 (もみじ = maple) is guarded on the 楓 side.
- No generated files (no `__pycache__`/.pyc) in the commit.

Optional:
- ビニール:4 «полиэтилен» names a specific polymer that differs from vinyl. It is hedged at lines 22-23 and is the usual Russian equivalent of ビニール袋, so it is acceptable. «винил; полиэтиленовая плёнка» would be slightly more exact.
- 榛: the established Russian species name for *Corylus heterophylla* is «лещина разнолистная». It could be added beside «азиатская лещина» (line 15).
- 脂:19 «срезал» over-specifies 取りました. «убрал/снял немного жира» is closer.
- 流す:21 «проливала» could be «пролила (слёзы)» to match the single completed event; both are acceptable.

Limits:
- No repository validator, generator or manifest-hash recomputation was run. The manifest diff was checked only for which paths changed.
- JMdict entry numbers and Kotobank/Weblio citations were carried over from EN. They were spot-checked (ビニール 1105580), not re-fetched individually.
- F1 and F2 are judgements about learner ambiguity; no learner data is available.

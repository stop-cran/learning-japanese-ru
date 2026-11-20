# B204 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `c4b6d94520f4755df78422eb4d06805db0b988a1`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 203 tree `20d0232` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `204-words-batch-43-recheck-001.md`.

Snapshot: RU scratch worktree C:\Users\romanko\repos\learning-japanese-ru-b198, candidate tree c4b6d94520f4755df78422eb4d06805db0b988a1 vs base tree 20d0232. Confirmed: `git diff-index --cached --quiet <tree>` exit 0, `git diff --quiet` exit 0, `git ls-files --others --exclude-standard` empty. No uncommitted difference from the candidate. 47 files changed (30 new words, 16 navigation files, manifest.json). `tools\validate.py`: 0 errors. No generator run; nothing edited.

Scope: Facets CONSISTENCY, QUIZ SAFETY, cross-file integration. Read IN FULL (front matter + body): all 30 new cards (正式 昼食 お昼 正午 プラス 正 歓迎 歌手 事情 次第 欠席 欠ける エンジン 機関 機嫌 横断 横切る 権利 様々 様 構成 検討 梅雨 桜 株 栄養 板 松 来 束) against frozen EN; all sixteen navigation diffs in full via `git diff -U0` (numbers-and-counters article, kanji 席 構 権 欠, words 拍手 松竹梅 梅 検査 状況 竹 義務 考慮 見当 遅刻 黒板). Scripted checks: front matter parity vs EN (all keys except title/exclusions), heading count, CR/EOL, link-target parity vs EN per card, broken targets, full EN->RU scan of every EN file that links to any new word, segment-equality screen of all 2773 RU titles, stem screen (word_title_screen.py), EN-vs-RU exclusion diff, reverse EN-exclusions on other cards, manifest hash check for all non-strokes entries and presence of the 30 keys. Model: not verifiable from inside the session. Dictionary senses spot-checked via jisho.org (JMdict-derived) for お昼, 論じる, 食料品, 横断, 機嫌, 途端; other senses rely on the cards' own cited JMdict entries.

Verdicts:
- Consistency: CLEAN. Front matter/tags/type/kanji/jlpt equal EN for all 30; section structure equal; no CR; validator clean. Link parity exact: the only EN-only links are to targets absent in RU (kanji/梅 栄 板 松, words/以来), left as plain text. No Russian-only links. All 16 navigation files change only by link brackets/hrefs at EN link positions (one-line or per-position hunks, hrefs correct relative paths; article diff is the single 株 link). Full EN->RU scan found no unrestored link to a new word in any existing RU file. Manifest: 30 new keys + 16 changed entries + contentVersion; every non-strokes entry hashes correctly (the strokes/*.json mismatches are untouched files, apparently CRLF-checkout artefacts, unchanged by this diff, out of scope). No unrelated or generated files.
- Quiz safety: NEEDS FIX (two minor, body-taught-sense gaps; no missing guard for an exact title/segment collision, all EN exclusions retained).
- Scoped coverage of cross-file integration: CLEAN.

Findings:
F1; Minor; quiz safety; words/お昼.md:5 (title), :12-13, :20 (body) / quiz_exclusions line; お昼 teaches «может обозначать и дневное время», and 昼間 has title «дневное время». JMdict お昼 has a separate sense "daytime" (jisho: lunch / noon; midday / daytime). So 昼間 is a defensible correct answer for お昼 although the title omits that sense. Only 昼 is guarded (EN-derived); no お昼<->昼間 declaration on either side. Remedy: `quiz_exclusions: [昼食, 昼御飯, 昼, 昼間]` on お昼 (alternative: drop the daytime sentence from the body, but that departs from EN). Evidence: JMdict sense 3 of お昼 (jisho "daytime"); 昼間 title «дневное время»; same logic already guards 昼<->昼間. Confidence: medium.
F2; Minor (low); quiz safety; words/プラス.md:5 / body "AにBをプラスする = прибавить B к A". プラス is taught as a する-noun with the action sense «прибавить» while 足す is «прибавлять; добавлять»; neither side declares the pair (EN has none either, only プラス<->正). Defensible alternative answer is arguable because the POS differs. Remedy: `quiz_exclusions: [足す]` on プラス (conservative). Confidence: low-medium (necessity unestablished).

Extra quiz_exclusions beyond the EN file (basis; classification):
- 昼食->昼: 昼 «дневное время; полдень», its body teaches "обед" sense (JMdict 昼 has lunch sense); also 昼御飯 already guards 昼. Required.
- 正->正しい: 正 body teaches it as a correctness mark (example translated «верно»); JMdict 正しい "right; correct". Conservative (basis real; title «истина (в логике)» is not a segment of «правильный; верный»), leaning required.
- 歓迎->受付: JMdict 受付 "reception; acceptance"; RU 受付 title segment «приём» sits inside 歓迎 «радушный приём»; the 歓迎 body names 受付. Conservative.
- 事情->原因: JMdict 原因 "cause; origin"; 事情 teaches «причины», 原因 «причина», and 理由 (same sense) is an EN pair. Required.
- 次第->流れ: JMdict 流れ "flow; course (of events)"; 次第 title «ход дела» vs 流れ «ход (событий)». Conservative, leaning required.
- 次第->途端: 途端 segment «как только» exactly equals a 次第 segment (JMdict 途端 "as soon as"). Required (exact segment collision).
- 欠席->休む: JMdict 休む "to be absent; take a day off"; 欠席 body glosses «отсутствовать», equal to a 休む segment. Required.
- 機嫌->気持ち: 気持ち segment «настроение» equals 機嫌 segment (気分/気 are EN pairs). Required.
- 横断->横切る: JMdict 横断 "crossing; traversing", 横切る "to cross; traverse"; shared «пересеч-/пересек-» stems and each card names the other. Conservative, leaning required (reasonable decision of the shared-stem question; EN lacked it).
- 横断->渡る: 渡る «пересекать; переходить» vs 横断 body «перейти дорогу». Conservative, leaning required.
- 様->手段: JMdict 手段 "means; way; measure"; 手段 «средство; способ достижения» and 様 «способ (сделать что-то)»; 様 body names 手段. Conservative.
- 構成->組む: 組む «составлять (из частей)» equals the 構成 body gloss «составлять целое из частей». Required.
- 検討->考える: JMdict 考える "to consider; think"; 検討 body names it. Conservative (EN pair is 考慮 only).
- 検討->論じる: JMdict 論じる "to discuss; deal with (a topic); take into consideration"; 論じる title «рассматривать (вопрос)» matches 検討 «рассмотрение; разбор (вопроса)» and 案を検討する «рассмотреть». Required.
- 栄養->食料品: JMdict 食料品 "foodstuff; groceries"; 食料品 «продукты питания» shares «питани-» with 栄養 and the body names it. Conservative (necessity unestablished; 食品/食べ物 not guarded, so the choice is somewhat arbitrary but harmless).
- 板->黒板: 黒板 «классная доска» vs 板 «доска; пластина»; a bare «доска» segment is the near collision. Required.
- 松->松竹梅: JMdict 松竹梅 "pine, bamboo and plum"; title contains «сосна» and «разряд(ы)»; body contrasts them. Conservative, leaning required.
No exclusion is unjustified (none guards a pure antonym/contrast such as 権利<->義務 or 欠席<->出席).

Cluster decisions with no guard needed (no equal segment and no shared defensible answer): 正式 vs 正しい/本当; 歌手 vs 歌/歌う; 事情 vs 場合/様子/状態 (already covered by 状況/事態 pairs; titles share no segment); 欠席 vs 留守/遅刻/出席; 欠ける vs 割れる/壊れる/欠点; エンジン vs 機械; 機関 vs 機械; 機嫌 vs 加減; 権利 vs 義務/自由; 様々 vs 種類/異なる; 様 vs 様子; 構成 vs 組織 (title has no «структура» segment); 検討 vs 研究/議論/見当/検査; 梅雨 vs 雨/季節/梅; 桜 vs 花見/花/木; 株 vs 会社; 栄養 vs 食べ物/栄える; 束 vs 包む (EN pair kept); 来 vs 来年/来る. No new title equals another card's whole title or segment without a guard (checked all 2773 titles; every hit is guarded).

Optional:
- 正: consider `本当` (title «правда; настоящий»; 正 «истина (в логике)»); «истина»≈«правда» is a near-synonym pair in Russian, but the logic qualifier keeps it low risk (EN has no pair).
- 来: consider `次` (the body glosses 来 as «следующий; наступающий»; 次 «следующий (по порядку)»); low risk because the 来 title lacks «следующий».
- 横断: consider `越える` (EN pairs 越える with 横切る); low risk.
- 欠ける vs 割れる («откалываться» vs «раскалываться»): contrasted in the body, no guard required.
- Terminology: 松.md and 桜.md call 梅 «японская слива», while the RU 梅 card uses «умэ; японский абрикос» and warns that not every «слива» is 梅. Optional polish to «умэ (японский абрикос)».
- Future obligation (not a defect now): EN exclusions on cards not yet in RU that target new words (e.g. モーター, ランチ, 交差, 公式, 構造, 以来, 文脈, 踏切) must be carried when those cards are translated.

Limits: JMdict senses outside the six jisho spot checks are taken from the cards' own cited entries or general knowledge. Quiz displays were judged from titles and body-taught senses, not from the app's actual option generation. Manifest check covers hashes of non-strokes entries and key presence; contentVersion derivation was not recomputed (generator not run, per instructions). Translation fidelity/Russian correctness and comprehensibility are other reviewers' facets. Blind constraints were followed (no author/prior reports or batch records read).

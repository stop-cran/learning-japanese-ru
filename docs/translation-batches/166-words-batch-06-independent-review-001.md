Snapshot: 4b77b04 (branch full-ru-166-words-06; parent d8b0d37; working tree clean)
Scope: 30 new words/*.md (余裕 冷静 平ら 穏やか 管理 仕舞い しまう 済ませる 終える 得る 収める 支払う 支給 供給 配達 計算 勘定 会計 費用 価格 値 料金 代金 支払 納める 治める 安定 もこもこ ぼんやり ふかふか), each read in full against the frozen EN card; 8 restorations (kanji/払 支 治 費; words/ぶくぶく ぷくぷく 支配 請求) checked by diff. Quiz screen: all 1663 RU word titles screened by stem, plus a direct-pair exclusion check by script. Reviewer: Claude (exact version unknown).
Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety NEEDS FIX

Findings:
Q1; Minor-Moderate; quiz safety; words/支払.md:9 (also words/料金.md:9)
- Claim and impact: 支払 «оплата; платёж» and 料金 «плата (за услугу); тариф» have no direct exclusion on either side. Russian «платёж» also means the sum to be paid: «коммунальные платежи» is the standard rendering of 公共料金. And «плата» is used for payment. So each title is a defensible answer when the other word is asked. A learner who picks it would be marked wrong.
- Remedy: words/支払.md:9 -> `quiz_exclusions: [会計, 勘定, 代金, 支給, 払う, 料金]`
- Evidence: Jisho 料金 "fee; charge; fare"; Jisho 支払い "payment"; Ožegov «платёж» sense 2 «уплачиваемые деньги».
- Confidence: medium-high.

Q2; Minor; quiz safety; words/会計.md:9
- Claim and impact: 会計 «бухгалтерия; счёт (в ресторане)» vs 計算 «вычисление; расчёт» has no exclusion on either side. JMdict/Jisho 会計 includes "reckoning" (sense 1) and "settlement (of a bill), payment" (sense 4). Russian «расчёт» is exactly that settlement sense, and the RU 会計 card itself glosses 会計する with «расчёт» (line 18). The batch already guards the parallel pair 勘定–計算.
- Remedy: words/会計.md:9 -> `quiz_exclusions: [勘定, 請求, 計算]`
- Evidence: https://jisho.org/word/会計 ; RU 会計.md:18.
- Confidence: medium.

Q3; Minor; quiz safety; words/穏やか.md:9
- Claim and impact: 穏やか «спокойный; мирный» has no exclusion against 柔らかい «мягкий; гибкий» or ソフト «мягкий; программное обеспечение», and neither of those cards excludes 穏やか. Jisho gives 穏やか as "gentle; mild". The RU 穏やか card itself renders it with «мягк-»: «мягкой манеры» (l.16), «спокойно и мягко» (l.22), «мягкую … погоду» (l.45). The RU 柔らかい card (l.44) and ソフト card (ll.16-17, 23) both cover a gentle voice or manner. So «мягкий» is a defensible answer for 穏やか. The author left this guard open; the evidence favours adding it.
- Remedy: words/穏やか.md:9 -> `quiz_exclusions: [冷静, 優しい, 静か, 安心, 柔らかい, ソフト]`
- Evidence: https://jisho.org/word/穏やか ; RU cards cited.
- Confidence: medium.

Author's Russian-specific claims (all confirmed, no defect):
- 管理 ≠ «управлять станком» (operating a machine is 操作).
- 供給 = «предложение» in «спрос и предложение».
- 配達 ≠ «доставить удовольствие/хлопот».
- 会計 ≠ a bank or website «счёт» (those are 口座 / アカウント).
- 費用 vs «стоимость», and 価格 vs «стоимость поездки»: the distinctions are sound.
- 治める ≠ «уладить формальности».
- 支給 «платить пособие» and 料金 «сбор/тариф/стоимость проезда» are natural.

Every EN sense is kept. The glossary terms (итидан, годан, онные чтения, атэдзи) are used. All 60 EN example lines were found verbatim, with readings, by script. The added full kana for もこもこ/ふかふか is correct.

Guards: none in the batch is clearly unjustified. These were reviewed and found defensible:
- 余裕–暇; 冷静–静か/安心; 穏やか–静か/安心;
- 得る–the получать family; 支給–払う/支払う; 配達–届ける;
- 勘定/会計–請求; 代金–勘定/会計/請求; 料金–値段/価格/値;
- 治める–済む; 管理–支配; 価格–値;
- 仕舞い–終える/終わる/済む; もこもこ/ふかふか–ソフト.

The 無くなる guards are conservative but harmless. The author's open pairs need no guard:
- 支払–請求: the roles are opposite.
- もこもこ–ぷくぷく/ぶくぶく.
- 仕舞い–夕方.

Optional:
- words/平ら.md:44-45: the sentence «Плоскость — не то же самое, что мягкость, прямизна или гладкость на ощупь, и так не в каждом контексте.» is garbled. Suggest: «Ровность поверхности — не всегда то же самое, что мягкость, прямизна или гладкость на ощупь.»
- words/治める.md:45-47: «обустроиться» reads as if it were a sense of «уладить». Suggest: «Русское «уладить» тоже шире: «уладить формальности» — не 治める. А «устроиться, обжиться на новом месте» по-японски скорее 落ち着く（おちつく）.»
- words/仕舞い.md:21: «понемногу заканчивать» -> «Пора потихоньку заканчивать работу».
- words/値.md:41: «а качество вещи — нет» -> «а качество вещи при этом не изменится» (closer to EN "quality does not change").
- Borderline, unguarded pairs, not established as defects. Consider guarding:
  - 料金–費用;
  - 供給–配達 («поставка» vs «доставка»);
  - 余裕–穏やか.

Limits:
- No native-speaker check of the Russian.
- Jisho was used as the JMdict proxy; JMdict ent_seq numbers were not individually verified.
- Restoration link positions were checked by diff against the author's EN mapping, plus a script check of link-count parity to the new words across all shared files. Positions inside the 8 files were not re-diffed line by line against the EN.
- Validator and manifest builds were not rerun by the reviewer.

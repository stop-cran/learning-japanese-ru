# B243 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `73cef33b421a2937376b84f06ad0c9908bc93346` (tree `0dc620083dfbf22c3f2b5550ecb4b76d3ebcbe2e`),
> the signed candidate pushed before review.
> Later reconciliation is in `243-words-batch-82-recheck-001.md`.

Snapshot: RU primary checkout, branch full-ru-243-words-82, `git rev-parse HEAD` = 73cef33b421a2937376b84f06ad0c9908bc93346 (matches). `git status --porcelain` was empty at start and at end. (Running `tools/validate.py` created an untracked `tools/__pycache__/`; I deleted it, so the tree is clean again. No tracked file was touched, no generator was run; the manifest was recomputed in memory only.)

Scope: Facets CONSISTENCY and QUIZ SAFETY (plus cross-file integration). Read in full (front matter and body): all 30 new cards `words/{群れ 美容 羊毛 缶詰 接続 繋げる 繋がる 繋がり 縫う 縛る 緯度 のろい 下降 傾く 斜め なだらか 緩い 編む 編集 編物 線路 総理大臣 続々 くれぐれも 再三 始終 絶えず 絵の具 統計 絨毯}.md`. All ten navigation diffs read in full (`-U0` diffs of kanji/傾, kanji/再, kanji/物, words/ぞくぞく, ペンキ, 井戸, 繋ぐ, 缶, 赤道, 首相). Intake JSON checked for path list only. Machine checks run on the working tree: validate.py (0 errors); EN-frozen vs RU front matter/links/exclusions for all 30; link label/target existence for the 30 cards plus the 10 nav files; EN-link-to-batch-word parity across every file that exists in both repos; in-memory manifest rebuild; Russian-title screening of each batch word against all RU titles (lexical tool as a lead, plus my own stem/keyword screen read by hand). Fidelity to the EN text and Russian linguistic quality are other reviewers' facets and were not judged. Model: not verifiable by me.

Verdicts:
- Consistency (format, front matter, terminology, links, navigation-only files, manifest, no stray files): CLEAN.
- Quiz safety: NEEDS FIX (two low-severity missing direct guards, F1 and F2; all EN exclusions retained; every RU-introduced guard has a real basis).
- Cross-file integration / coverage of the ten navigation restorations: CLEAN.

Findings:

F1; Low; quiz safety; words/繋がり.md:9 (`quiz_exclusions`); 交際 is not guarded.
Claim: 繋がり title «взаимосвязь; связи (с людьми)» can be a defensible correct answer for 交際 «социальные контакты; романтические отношения» (and vice versa), and 交際's own list [付き合い, 関係, 恋, 仲, 連絡] does not contain 繋がり. The batch already guards the sibling people-relations words 仲, 付き合い and パイプ against 繋がり; 交際 is the same cluster but was missed. Impact: a plausible distractor can be a second correct answer.
Remedy: `quiz_exclusions: [関係, 関連, 接続, 仲, 連絡, パイプ, 付き合い, 交際]`.
Evidence: JMdict 繋がり (1251870) "connection; link; relationship"; 交際 "association; company; friendship; acquaintance; dating". RU titles as above. Confidence: medium (title overlap «связи» vs «контакты» is partial).

F2; Low; quiz safety; words/編集.md:9; 修正 is not guarded.
Claim: 編集 title «редактирование; монтаж (фильма, видео)» vs 修正 «исправление; правка». In Russian «правка» is the ordinary rendering of "editing" (e.g. the Edit/Правка menu), and the 編集 article itself says that fixing errors can be part of editing. Neither 編集 [編む] nor 修正 [変更, 直す] declares the pair. Impact: 修正 is a defensible correct answer for 編集.
Remedy: `quiz_exclusions: [編む, 修正]`.
Evidence: JMdict 修正 "amendment; correction; revision; modification"; 編集 "editing; compilation". Confidence: medium.

Classification of every exclusion beyond EN (all 10 entries; each target card exists, none is a self-reference, none is duplicated):
- 群れ → 混雑 «давка; скопление людей»: basis 混雑 "congestion, crowdedness" vs 群れ «толпа»/«скопление» (title and body); parity with the EN-guarded 人込み «толпа людей». REQUIRED by parity.
- 缶詰 → 滞在 «временное пребывание»: basis 缶詰 sense 2 «пребывание взаперти» (JMdict 1214560) vs 滞在 "stay, sojourn". Real basis, shared word «пребывание»; CONSERVATIVE.
- 繋がり → パイプ «…связи, канал общения между людьми»: basis JMdict パイプ sense "channel of communication/connection"; the title of パイプ literally says «связи … между людьми». REQUIRED.
- 繋がり → 付き合い «общение; отношения с людьми»: basis 付き合い "association; socializing; relationship"; same footing as the EN-guarded 仲. REQUIRED by parity (CONSERVATIVE at minimum).
- 編物 → 製品 «изделие; продукция»: basis 編物 title «вязаное изделие» vs 製品 "manufactured goods; product". Shared word «изделие»; CONSERVATIVE.
- 総理大臣 → 政府 «правительство»: basis 政府 "government" vs 総理大臣 "prime minister; head of the cabinet". Only a topical relation (the word «правительство» sits inside the title «глава правительства»); the head of a government is not a defensible answer for "government". UNJUSTIFIED (harmless, over-restrictive; no fix required; optional removal).
- くれぐれも → 要求 «требование; настойчивая просьба»: the 要求 title itself says «настойчивая просьба» vs くれぐれも «настоятельно; убедительно (о просьбе)»; JMdict 要求 "demand; request". REQUIRED/CONSERVATIVE (real title overlap).
- 始終 → 飽くまで «упорно, до конца; сугубо»: JMdict 飽くまで "to the end; persistently"; 始終 title «от начала до конца». Shared «до конца»; CONSERVATIVE.
- 絶えず → 継続 «продолжение (дела, состояния); непрерывность»: 継続 "continuation" gives «непрерывность» vs 絶えず «непрерывно». Real basis (derivation, near-same gloss); CONSERVATIVE. Note the matching 始終 «беспрестанно» has no 継続 guard; not needed, but the two are not parallel.
All other EN exclusions are present in RU for all 30 cards (script: EN-missing = empty for every card). 絨毯, 緯度 have no exclusions in EN or RU.

Dense-cluster screen against ALL RU titles (batch word vs every RU word title; pairs where a direct exclusion exists on at least one side count as satisfied): 群れ cluster (集団 団体 組 グループ クラス 集まり 人込み 大勢 会 会合 パーティー 学校 混雑) satisfied; 美容/化粧; 羊毛/ウール 毛 毛糸; 缶詰/缶 滞在; 接続 (繋ぐ 結ぶ くっつける 付ける 付く 乗り換える 連絡 合同 合流 開通 関係 関連 接する 節 続く, and each of 繋げる/繋がる/繋がり guard 接続) satisfied; 繋げる; 繋がる; 繋がり (F1 aside); 縫う; 縛る; のろい; 下降; 傾く; 斜め (declared on 斜め→傾く); なだらか; 緩い; 編む (組む; 編集 and 編物 declare 編む); 続々, 再三, 始終, 絶えず, くれぐれも all satisfied. No title or sense in the bodies of 緯度, 線路 (線, 鉄道; 道/道路 are not defensible), 統計 (数字, 資料), 絵の具 (ペンキ), 絨毯, 縫う vs 編む, 美容 vs とこや/格好 produced a defensible pair beyond those listed. Leads I rejected as not defensible: 総理大臣 vs 大臣 (title «министр (член кабинета)» vs «глава правительства»), なだらか vs ふわふわ/はらはら («плавно парящий/опадать»), 繋がり vs 連想 («ассоциативная связь»), 紅葉 «осенние краски» vs 絵の具.

Optional:
- 下降 «снижение; понижение» vs 下げる «опускать; снижать»: same Russian root, noun vs transitive verb; 下降 already guards its intransitive sibling 下がる (EN). Consider adding 下げる to 下降's list; low confidence, not required.
- 編集/編む body senses «составление / составлять сборник» vs 作成 «составление (документа, плана)»: 作成 has its own large exclusion list; consider adding 作成 to 編集's list together with F2. Low confidence.
- 編む (words/編む.md) links 編集, and 編物 links 縫う, where EN has plain text: allowed (links to existing cards at substantive comparisons; targets exist and are correct), no action.

Link and navigation checks (all passed):
- All relative `.md` links in the 30 cards and 10 navigation files resolve; every label equals its target stem; path forms follow EN (`../words/X.md` in kanji files, `X.md` in word files, `../kanji/X.md` in cards).
- Every EN link to an existing RU target is present in RU. EN links whose RU target is absent (kanji 群 毛 缶 詰 接 鈍 編 線 総 臣; words 毛皮 火口 片寄る 社説) stay unlinked plain text, as the repository convention allows.
- Parity scan over every file present in both repos: the only link differences against EN involving batch words are the two RU-added ones above (編む→編集, 編物→縫う). No missed restoration anywhere (e.g. nothing else in RU still mentions a batch word as plain text where EN links it).
- Ten navigation files: exactly 12 link occurrences, at the stated lines (傾 31, 40; 再 30, 38; 物 40; ぞくぞく 26; ペンキ 28; 井戸 39; 繋ぐ 35; 缶 35; 赤道 33; 首相 33 with 内閣 outside the link), only brackets/hrefs changed, no prose change, EN-position parity as described (傾 20 and 33, 再度, 繋がる, ペンキ line 32 stay plain). Adjacent glosses do not mislead beside the new titles.
- Kanji coverage: every `kanji:` list matches the written kanji of the headword (のろい, なだらか, くれぐれも have `kanji: []`); front matter keys (word, reading, jlpt, type, kanji, tags) equal EN for all 30; the app's scalar/inline-list subset is used; H1 `# 字（reading）— title` (for かな-only headwords `# なだらか — …` / `# くれぐれも — …`, as in EN, which also omits the kanji section for くれぐれも), the same four H2 sections in the RU names as EN, tables and bullets render; LF endings, single trailing newline; no BOM.
- Terminology: 年中 etc. not touched; verb-class vocabulary (годан/итидан, окуригана) matches existing RU cards; Japanese forms in text are used as in the RU cards. No glossary conflict found.
- Manifest: rebuilt in memory with `tools/build_manifest.py`'s `build_manifest`; result equals the committed `manifest.json` (contentVersion 1cd2bb5be75b134a; 40 changed content entries = 30 new cards + 10 restored files). No stale hash.
- Intake record `docs/translation-batches/243-words-batch-82-intake.json`: its 40 payload paths are exactly the 40 `words/` and `kanji/` paths of the content diff; the only other changed files are the intake and `manifest.json`; the record adds no learner content; `held` is empty. 42 files changed in total, no generated/unrelated files committed.

Limits:
- Dictionary evidence is from my knowledge of JMdict/Daijisen senses (and the cards' own cited entry numbers), not fresh lookups; F1 and F2 rest on Russian-title overlap and are judgment calls (medium confidence).
- Translation fidelity to EN and Russian prose quality (including cards where RU is longer than EN, e.g. 縛る, のろい, 下降, 再三, 傾く) were not assessed in this facet.
- I did not run `build_manifest.py` to write; the manifest equality is an in-memory comparison.
- Stroke data and kanji cards are not part of this batch; kanji files other than the three navigation files were not reviewed.

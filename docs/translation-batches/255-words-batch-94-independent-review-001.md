# B255 — independent review of word batch 94

**Blind candidate:** `8f4707c36e5d79d004c808e633c03c2cfaa4ae11`, tree `02468341eec95db807578daf86fd723a98478e6e`. **Frozen EN:** `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. **Published RU input:** `bd8dd45099922888a55b8e17fd8c6b771dcd1a7a`. The candidate's parent `650d46660be4ff7c10c5ee8067ae9034f5c36fc1` adds only the signed B254 publication-verification record above that input. The authoring snapshot `747a6fa7644f74719aaaaa8c26d8652074b5f9f9` (parent `1e7bb647b912c455185af2bc3504438bc1de2265`) supplied 39 preflighted content blobs, not a manifest or a merge parent.

The [intake](255-words-batch-94-intake.json) fixes the 30 new words and nine existing navigation files by path and raw EN/RU hash. The requested word set equals its closure; no additional or held word and no deferred guard. Before signing, a mechanical source-layout patch restored 59 Japanese sentence–reading layouts on all 30 new words (parentheses, spacing and line layout only; no Russian gloss changed). The intake records those post-patch hashes separately from the scratch hashes; the restoration is part of the reviewed bytes, not a review. Relative to its parent the signed candidate changes those 39 files, the rebuilt manifest and the intake only. Tracking and generated progress still describe B254 at this stage.

### Common sample and independent returns

Each reviewer had the same 30 complete EN/RU pairs verified against the intake, the 30 attributed dictionary packets from the frozen N2 index, the frozen EN repository, a generated mechanical-facts file with existing RU labels and the related words each card links or guards, the complete diff of the nine navigation files and the full signed candidate/parent diff. The mechanical input named existing exclusions and links, not a judgement of their necessity. Initial reviewers were not given the author's notes or adjudication, other reviewers' findings or the coordinator's later reconciliation. The signed candidate did not change between assignments.

| Assignment and original report | Runtime model and reviewer ID | Initial run, UTC on 2026-11-23 | Original report: bytes / raw SHA-256 |
|---|---|---|---|
| [Correctness and source coverage](255-words-batch-94-review-correctness-001.md) | `gpt-6.2-sol` · `895be00c-092b-4b22-bd4a-423cc22af432` | 22:46:14.674–22:54:44.337 | 9,969 · `a7231b0d4081a5eb58444c00ace49d2dc0479a0aa6271fca7b5067646e766d6a` |
| [Consistency, quiz safety and integration](255-words-batch-94-review-consistency-001.md) | `claude-opus-5.5` · `8231b23d-2231-45c6-8669-d7bc2814c2f7` | 22:55:56.454–23:13:44.057 | 10,998 · `3864c6e648f8fe0a03067f28bbcf5a2b30df881ce83352ad442dea292802858a` |
| [Russian comprehensibility and scoped coverage](255-words-batch-94-review-comprehensibility-001.md) | `grok-4.7` · `2d1a19ce-5627-41f8-983e-70b0fa41ce4f` | 23:14:51.160–23:31:00.427 | 5,664 · `06e09e2a48bda060026fd67244e210c73cd307f678d40e968c2dd9c3697db143` |

Each initial `subagent.completed` preceded the next `subagent.started`. The completed-agent metadata identified the three distinct serving families. All three reviewers reported reading the 30 pairs and nine navigation diffs in full. Separately, the execution records contain each complete numbered pair and each navigation file's complete diff block in a single returned tool result, not merely commands requesting those reads, and each public report also appears in returned tool output. The coordinator independently repeated this match on the actual Git inputs and returned `result.content` (whitespace-normalized contiguous blocks, original report hashes, runtime model events, non-overlapping intervals); its session evidence `b255-blind-returns-visible-001.json`, SHA-256 `2172aaba4f17c5d9f0f430937349f578462a519badf8876eaf5957eebc9f17dd`, is outside this repository and covers the initial candidate only, not the fix or the rechecks. The hashes above identify the saved original report files, **not** the stdout wrapper, network bytes or the Git files with their provenance prefixes. The consistency original was saved with CRLF line endings. Completeness of the returned text is not proof of comprehension.

### Initial results and coordination decisions

The tables preserve each reviewer's assignment, including overlaps and unverified claims. “Accepted” here means implemented at signed fix `46f7089e8d6257686cd4af522595ec7455c107ed` (tree `973ca257d8082965aa82b68a01f56016f9cb473e`). The correctness recheck of that fix raised R01 (汁) and R02 (正味), applied in the second signed fix `c4d64291556bb0cc4ee7457febb567dea37df433`; the [separate recheck record](255-words-batch-94-recheck-001.md) reports what was found on both.

| Correctness finding | Decision and source-specific reason |
|---|---|
| F01 汁, medium | Accepted; overrides the comprehension optional that judged the narrowing harmless. JMdict 1335520 §1 and [Digital Daijisen しる①](https://www.weblio.jp/content/汁) define liquid squeezed or seeping out of a thing (物), lemon being an example, not a restriction. Title/H1 «выжатый или выделившийся сок; бульон; похлёбка»; :16 «сок, выжатый из чего-либо или выделившийся из него, а также бульон или похлёбка». The first fix kept the existing «похлёбка», judging it outside this defect; recheck R01 showed it narrower than しる③ (吸い物, 味噌汁), and the second fix uses the reviewer's «суп» throughout (:4, :12, :16, :20, :42). :42 already taught generic «сок». EN guards ジュース/スープ unchanged; the latter covers the shared «суп». |
| F02 残らず, medium | Accepted. :27 now names intransitive 残る and gives the literal «так, что ничего не остаётся»; no human agent is implied. |
| F03 毎度, medium | Accepted with the reviewer's label: «каждый раз; спасибо, что снова выбираете нас (клиенту)». JMdict 1524710 §2 and [Daijisen 毎度②](https://www.weblio.jp/content/毎度) concern thanks for continued patronage, not a current purchase or a face-to-face greeting. :20 «Спасибо, что снова выбираете нас.» (parallel to the label rather than the suggested «обращаетесь»). The short form's greeting senses at :22–23 are unchanged. |
| F04 公共/民間, low | Accepted. 公共:36 公立 «обычно … создано и содержится местными властями; в противопоставлении частным так иногда называют и государственные учреждения» ([Daijisen 公立](https://www.weblio.jp/content/公立): 私立に対して国立を含めていうこともある). 民間:34 私立 «которые создали и содержат частные лица или негосударственные организации» ([Daijisen 私立１](https://www.weblio.jp/content/私立)). |
| F05 正味, low | Accepted. :35 first «цена без наценки; закупочная цена» ([Daijisen 正味４](https://www.weblio.jp/content/正味): 掛け値のない値段。また、仕入れの値段), not an accounting cost total. Recheck R02: «наценка» also excludes ordinary markup, whereas [掛け値](https://www.weblio.jp/content/掛け値) is a price padded for bargaining; second fix «фактическая цена продажи без завышения в расчёте на торг; закупочная цена». |
| F06 元気でね, low | Accepted. また会おう proposes meeting again: «Давай ещё встретимся.» |
| F07 水分, low | Accepted. :22 «пить жидкость; речь не обязательно о простой воде» — no presupposed deficit. |
| F08 歌謡, low | Accepted; also comprehension F3. «каёкёку» for かようきょく. |
| F09 正門/歯磨き, low | Accepted. «Пока идут строительные работы, …» (工事 is not necessarily repair); «Я нанёс зубную пасту на щётку» (つける is application, not squeezing). |
| Optional «эстрада» | Declined. ステージ:16 already explains the platform sense; the title's second segment covers performance. |

Correctness was **NEEDS FIX** and scoped coverage **NEEDS FIX** (汁 in F01); all nine navigation diffs were CLEAN. The reviewer reported that all 60 Japanese example blocks matched frozen EN; 59 of them carry a reading (the 59 restored layouts), the remaining いってきます line of a dialogue has none in EN either.

The consistency reviewer reported **NEEDS FIX** on quiz safety (one minor and one low finding); format, links, navigation and manifest **CLEAN**; integration coverage **CLEAN**.

| Consistency finding or optional | Disposition at fix |
|---|---|
| F1 ステージ–演説/スピーチ, minor | Accepted: `[舞台, 公演, 演技, 演奏, 芝居, 水準, 演説, スピーチ]`, the EN prefix unchanged and in order. 演説 is **required**: its label «публичная речь; выступление» contains an unqualified «выступление», a defensible answer for the performance sense (JMdict 1070320 §2). スピーチ is **conservative**, matching the existing RU 公演 guards [芝居, 演説, スピーチ]. Ordinary-quiz frequency is not measured. |
| F2 over-guarding, low | Accepted with the primary remedy. Removed four RU-added pairs whose contrast the article itself teaches and whose other label is not a defensible answer: 水平線–地平線 (water vs land horizon, :31), 歯車–車輪 (gear vs vehicle wheel, :33; the line is deleted because EN has no exclusions), 欧米–欧州 and 欧米–ヨーロッパ (Europe is only part of the connected label «Европа и Америка», :36). No EN exclusion was removed; the body contrasts remain. |
| Optional 欧米–西, 元気でね–健康 | Not added. «запад» is not a defensible answer for 欧米. 元気でね «всего хорошего; будь здоров (при прощании)» is a farewell formula, 健康 «здоровье; здоровый» a state; neither whole label answers the other. 元気でね–元気 is kept as a conservative guard on the shared written base. The candidate-stage reason (that the 健康 label lacks «здоров») was imprecise, as the consistency recheck noted; the decision is unchanged. |
| Optional 水筒 «Во 水筒» | Adopted: «В 水筒». The 水平線 «горизонтальная линия» basis is Daijisen, not the JMdict capture; noted, unchanged. Future 割と/割合に cards must check pairs with 比較的. |

RU-added direct pairs after the fix: **required** — いってらっしゃい–さようなら, 元気でね–さようなら, 公衆–観客, 正味–中身, ステージ–演説; **conservative** — 水平線–横, 元気でね–元気, 民間–私立, 比較的–比較, ステージ–スピーチ; **removed** — 水平線–地平線, 歯車–車輪, 欧米–欧州, 欧米–ヨーロッパ. Classification is a reviewer and coordinator judgement on the actual whole labels and taught secondary senses, not empirical necessity. No transitive closure: frozen EN `docs/content-format.md` lines 162–167 make each declared pair symmetric, and nothing more.

The comprehension reviewer reported **NEEDS FIX** for Russian and **CLEAN** for scoped coverage.

| Comprehension finding or optional | Disposition at fix |
|---|---|
| F1 おだいじに, medium | Accepted: «пожелание беречь себя, а также скорее поправиться». The corrective «или» withdrew the first wish (JMdict 1002390 §1 co-glosses). |
| F2 民謡, low | Accepted: «`[民間](民間.md)（みんかん）тоже связано с обычными людьми и народом, но само не означает песню.`» The neuter agrees with «слово» implied for 民間. |
| F3 歌謡, low | Same fix as correctness F08. |
| F4 毎度, low | Accepted in a shorter form: «Чтения — まい + ど: «в каждом случае».» The title already gives «каждый раз». |
| Optional 垂直:29 «ровный» | Not changed: pre-existing wording in a navigation file whose only B255 change is the link. |
| Optional 正門 «не прямой» | Not added; the required point (which gate, not «правильные») is present. |
| Optional 汁 narrowing | Superseded by correctness F01 on dictionary evidence. |

No cross-facet model ranking or learner test.

### Integration and limits

All nine navigation links are wrapper-only and remain at the same bytes in both signed fixes: `kanji/圧` → 気圧; `words/お帰り` → いってらっしゃい; `地平線` → 水平線; `垂直` → 水平; `毛糸` → 毛皮; `羊毛` → 毛皮; `血圧` → 気圧; `西洋` → 欧米; `門` → 正門. ステージ→段階 is a valid RU-only link inside the batch; 毛糸→毛 and 門→ドア/入口 are existing RU-only links on unchanged lines.

Frozen EN links from the 30 new cards to targets without an RU file: 11 occurrences, 11 distinct targets — kanji 欧 門 磨 階 比 毛 皮 革 線 筒 and the word 公式; they stay plain text. The nine navigation cards carry five such existing occurrences to four targets (線, 毛 twice, 血, 門); `kanji/血.md` appears only there. Twelve distinct unavailable targets across all 39 files; no EN link to an available RU target is missing. The 30 cards keep all 121 EN exclusion entries in EN order; the candidate appended 12 RU entries (133), the fix 10 (131), always after the inherited ordered prefix.

Qualified source-content evidence only. A validator, title screen, successful recheck or manifest membership does not certify every fallback choice, voice or drawing prompt, device, learner outcome, ordinary activation or release.

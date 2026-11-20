# Batch 211 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `53d6950b1b8c0d254414e1f2ba4d967b2ca3b43a` | `154fb77da0097183389a794e442bf915ed34d075` | Initial review snapshot: the signed candidate, pushed before review. |
| `37c0c96b2b48eb96240549fd1312492c14424505` | `bb7357ce6217df611aa4f904b50272afc1ba5155` | Fix 1 (final candidate): correctness and comprehensibility findings, one resolved correctness limit, one adopted optional note and the intake refresh, committed signed and pushed before the rechecks. |

Fix 1 changed eight word files and regenerated `manifest.json` (`contentVersion` `a0ea17aa518e8664`, 4,444 entries) and the
intake:
- `包み` (line 29): «[荷物] включает багаж и посылки независимо от того, завёрнуты они таким образом или нет» instead of
  «…завёрнутые так или иначе» (correctness C1); the closing RU pointer «Почтовая посылка — 小包» became «Посылка как
  отправление — 小包（こづつみ）», following the 小包 retitle.
- `宝石` (lines 16, 18, 19): «драгоценный камень» / «драгоценные камни» instead of bare «камень» / «камни» in the definition
  and both example translations (correctness C2, merged with comprehensibility K4). The reviewer's «самоцвет» was not used;
  «драгоценный камень» is the title's primary segment and the more ordinary Russian, and both avoid 石's title.
- `少女`: title and H1 «девочка; юная девушка» instead of «юная девушка» (correctness C3), now equal to the 少年:33 gloss.
  New direct guard 少女→女子 (`quiz_exclusions: [女の子, お嬢さん, 女子]`), because «девочка» now stems with 女子 «девочки;
  женщины»; it parallels EN's 少年→男子. Line 33's source-list sentence became «Перевод в исходном списке слов в обоих
  случаях заходит дальше, чем позволяет словарь.», mirroring EN "The source gloss overreaches on both points" instead of
  naming «девственница» (comprehensibility K5, partially accepted). The ritsuryō age note is unchanged.
- `パス`: title and H1 «пас (мяча; отказ от хода); успешная сдача экзамена; пропуск (документ); путь к файлу» instead of
  «пас (мяча); успешная сдача экзамена; путь к файлу» (correctness C4, modified wording). Russian «пас» also names a
  player's refusal in card games (ru.wiktionary «пас» sense 2); «пропуск (документ)» is qualified so it is not read as
  the «пропускать» verbs of 省く and 飛ばす. Lines 16 and 26 now state the two-word split in Russian, keeping the loan origin
  from English pass and path as the reason there are two words, without bold English labels (comprehensibility K1,
  partially accepted). Line 34 says «каждому из этих двух слов» instead of «каждому омографу» (adopted optional note).
- `小包`: title and H1 «посылка» instead of «почтовая посылка», resolving the correctness limit. Daijisen (Weblio デジタル大辞泉
  こ‐づつみ【小包】) gives sense 1 小さな包み and sense 2 「小包郵便物」の略; EN "parcel; package" and the body's «особенно
  отправленная или полученная» do not restrict the word to the post. 荷物:25 and kanji 包 already gloss 小包 «посылка».
- `実施` (line 29): kana for the RU-only example, 訓練を行う（くんれんをおこなう） (adopted correctness optional note).
- `実行` (lines 18, 21): «В следующем месяце мы выполним этот план.» instead of «…претворим этот план в жизнь», and 実行に移す
  «приступить к выполнению, перейти к делу» instead of «перейти к делу, претворить в жизнь» (comprehensibility K2,
  modified). The title and line 16 keep «претворение в жизнь», the standard collocation for implementing plans, paired
  with «переход от замысла к делу»; 実現 is unchanged.
- `定期` (line 29): «[普通](普通.md)（ふつう）— «обычный» — говорит об обычном, привычном, а не о повторении по графику, как
  定期.» instead of the comparison through Russian «регулярный» (comprehensibility K3, modified). The link position is
  unchanged.
- The intake note now names the fixed cards.

Net change from the candidate: three titles with their H1 headings (少女, 小包, パス), three example translations (宝石 ×2,
実行), the 実行に移す phrase gloss, five explanatory passages (包み:29, パス:16, 26 and 34, 定期:29), one definition sentence
(宝石:16), one condensed provenance sentence (少女:33), one kana addition and one added exclusion. No Japanese example,
reading or internal link changed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially. Each reviewer appended to its own report file, which stayed in its session context, and each
recheck message gave it:
- the revised snapshot, its parent and the read-only rules;
- the actual content diff (`git diff 53d6950 37c0c96 -- words`);
- the coordinator's evidence for every change, and the declined items from all three facets with their reasons, without
  the other reviewers' reports;
- the coordinator's disposition of each of its own findings and optional notes.

The shared opening said that the edits came from the correctness and comprehensibility reviewers and one coordinator
resolution of a correctness limit, and asked each reviewer to judge every change on its evidence rather than its origin.

The recheck prompts forbade running `tools/build_manifest.py` or any other generator; all three recheck sections state that
none was run. The correctness and consistency reviewers ran `tools/validate.py` (0 errors); the comprehensibility reviewer
states that it did not. After every recheck the coordinator confirmed that HEAD was unchanged and that
`git status --porcelain --ignored` was empty.

### Round 1 (`37c0c96`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer read all eight revised cards in full and checked every changed passage and title against its context and the frozen EN passages. C1–C4 are resolved: 包み includes luggage regardless of wrapping; 宝石 consistently says gemstone; 少女's title covers childhood and adolescence, the 女子 guard has genuine overlap, and the shortened line 33 keeps both source-gloss cautions and the historical qualification; パス covers passing a turn and the admission document, and lines 16, 26 and 34 keep the separate pass/path identities without requiring English. The 実施 kana note is resolved; the RU-only links and 券 «билет» remain optional. It newly fetched Weblio/Daijisen 小包 (sense 1 small bundle; sense 2 postal parcel), resolving its 小包 limit, and ru.wiktionary «пас» senses 1–2. No regression: 実行 keeps time, subject and object roles, and 実行に移す expresses starting implementation, not a guaranteed result; 定期 contrasts ordinary with scheduled recurrence. `tools/validate.py` reported 0 errors. Correctness and scoped coverage are **CLEAN**. |
| Consistency | The reviewer confirmed that the fix touches ten files (eight cards, the manifest and the intake) and that every Markdown manifest hash matches its file. It screened the new titles against all current RU titles: 少女's exact segment «девочка» with 女の子 is EN-guarded, and its «девоч» stem with 女子 is now guarded directly, parallel to 少年→男子; パス shares no exact segment with any title; «посылк» occurs in no other title, and 包み/小包 are guarded. 宝石→玉 is kept, and front matter still differs from EN only in titles and RU-added exclusions. It accepted the declined O1–O5 as optional and O6 as consistent. Consistency, quiz safety and cross-file integration are **CLEAN**. |
| Comprehensibility | The reviewer read the eight changed cards and the unchanged 対, 密 and 実現. K1–K4 are resolved: パス states the split in Russian and leaves pass/path only as loan labels; 実行 «выполним» and 実現 «воплотим … в реальность» now show doing versus the result arriving, and the kept title «претворение в жизнь» is not the example gloss; 定期 no longer passes through «регулярный»; 宝石's «такой камень» refers back to «драгоценный камень». K5 is resolved for 少女 and **withdrawn** for 対 and 密: their rules work in Russian without the source-list clauses, which are opaque but do not mis-teach, so removal is a series question. No regression in 包み, 小包 or the 少女 title. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 包み presupposes wrapping for 荷物 | **Resolved** | `包み.md:29`; frozen EN `包み.md:29`; JMdict 荷物 sense 1. |
| Correctness C2: 宝石 examples use 石's bare «камень» | **Resolved** | `宝石.md:16,18,19`; frozen EN `宝石.md:18–19`; JMdict 宝石. |
| Correctness C3: 少女 title omits childhood | **Resolved** | `少女.md:4,9,12`; JMdict 少女 sense 1; frozen EN `少女.md:4,16,18`. |
| Correctness C4: パス title omits the admission pass and passing a turn | **Resolved** | `パス.md:4,12`; JMdict パス senses 1–4; ru.wiktionary «пас» senses 1–2. |
| Correctness limit: 小包 postal-only title UNVERIFIED | **Resolved** | `小包.md:4,12`; Weblio デジタル大辞泉 こ‐づつみ senses 1–2; frozen EN `小包.md:4,16`. |
| Correctness optional: kana for 訓練を行う | **Resolved** (adopted) | `実施.md:29`. |
| Correctness optional: RU-only links to 彼女, 行う, 実際, 玉 | **Optional, not adopted** | RU-added comparison mentions with no EN link at that position; adding links would break EN link parity. Reviewer kept them optional. |
| Correctness optional: «билет» in 券's title | **Optional, not adopted** | «билет» is the whole title of 切符, which 券 guards; «талон; купон» was not shown to be wrong. |
| Consistency O1–O4: guards 定期→期間, 実験→試験, パス→道, 小屋→家 | **Optional, not adopted** | EN declares none; no exact title segment is shared; the bodies teach each contrast; the app deduplicates exact titles only. Reviewer accepted the decline. |
| Consistency O5: «девушка» and «размер» stems | **Optional, not adopted** | Qualifiers distinguish 少女, 彼女 and 恋人, and 小 and 大小; the new «девочка» stem with 女子 is guarded under C3. |
| Consistency O6: 少年:33 gloss | **No change needed** | The gloss now equals the 少女 title. |
| Consistency limit: 110 strokes raw-hash differences | **No action** | `tools/build_manifest.py` hashes text after CRLF→LF normalization, as recorded in Batch 209; untouched by this batch. |
| Comprehensibility K1: パス split depends on English | **Resolved** | `パス.md:16,26,34`; RU instructions on English-independent learner text. |
| Comprehensibility K2: 実行/実現 examples do not contrast | **Resolved** | `実行.md:18,21`; `実現.md:19,29`; Kuznetsov «претворить» sense 2. |
| Comprehensibility K3: 定期's 普通 contrast relies on English "regular" | **Resolved** | `定期.md:29`; frozen EN `定期.md:37`; 普通's title «обычный». |
| Comprehensibility K4: 宝石 glosses use «камень» | **Resolved** | Merged with C2. |
| Comprehensibility K5: source-list clauses in 少女, 対, 密 | 少女 **resolved**; 対 and 密 **withdrawn** | `少女.md:33` mirrors frozen EN; `対.md:34` and `密.md:33` mirror EN's source sentences; series precedent `便.md:44-47`, `変化.md:58`, `はあ.md:34` and Batch 210 帯/就職. Reviewer withdrew 対 and 密. |
| Comprehensibility optional notes on 宜しく's title and wago/kango naming in 家賃 and 実は | **Optional, not adopted** | No defect shown; established series terms. |
| Exclusion classification | **No differences** | The author, coordinator and consistency reviewer classified all seven candidate entries alike; 宿泊→泊まる was rated "required, or at least strongly justified". |

Cross-batch note: `完成.md:27,31` and `専攻.md:28` keep plain mentions of 完了, 完全 and 学ぶ, which have no RU card yet.
Batch 212 introduces those cards and restores the links at the EN-linked positions; the wraps are reviewed with that batch.

## Final exclusion set

All 25 EN exclusion entries (14 lists) are retained. Eight direct, one-sided entries are added on eight new cards:

- Required (5): 密→近い, 宿泊→泊まる, 実施→行う, 完成→仕舞い, 少女→女子.
- Conservative (3): 宿→泊まる, 実行→行う, 実現→実行.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fixes (包み).
- Scoped coverage: **CLEAN** after fixes (包み, 宝石, 少女, パス, with the 小包 limit resolved).
- Comprehensibility: **CLEAN** after fixes (パス, 実行, 定期, 宝石, 少女; the 対 and 密 notes withdrawn).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** throughout, with the 少女→女子 guard added with the C3 retitle, for the reviewed batch and the
  directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

Limits: the rechecks reread only the changed passages and the cards needed to judge them; unchanged cards rest on review
001's full reading. Only the correctness reviewer inspected new dictionary entries in the recheck; the consistency and
comprehensibility reviewers did not re-fetch dictionaries. The consistency reviewer did not re-verify the intake hashes in
the recheck and did not read the app's `Words.kt`; its JMdict senses came from its own knowledge. The comprehensibility
reviewer did not run `tools/validate.py`. No native-speaker, learner, app-import, device, media, activation or release
acceptance is claimed.

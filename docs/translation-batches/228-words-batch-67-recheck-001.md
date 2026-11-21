# Batch 228 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `e2b0bdba512f72ca587ad5d2cb553b0edb22016a` | `4b3cf06ecc0f1d128d13dbd4629a2239bfb59bd4` | Initial review snapshot: the signed candidate, pushed before review. |
| `955a4e9f1379c8711126c80f3f394abf57dac703` | `1f032600530510aced6f3ff78494483fbaa74377` | Fix 1. It covers correctness C1–C3, comprehensibility F1, F2 and F4–F7 (F7 merged with C1 and partially adopted), consistency's optional O2 (through C3), the two adopted correctness optional items and the intake refresh. Signed and pushed before the rechecks. |
| `b281154eb4b523cc6b54d1965ba0b93ef782a690` | `96be2be788a7b7a4d186c7ec1ca037091e562cdc` | Fix 2 (final candidate). It covers the comprehensibility recheck finding R1 on 広さ and refreshes the intake. Signed and pushed before the second comprehensibility recheck. |

Fix 1 changed nine word files and regenerated `manifest.json` (`contentVersion` `f1dd4c24449119b7`; the candidate had
`7a0ab3a14eee3339`) and the intake:
- `交流` (lines 25 and 27; comprehensibility F4): «— Этот механизм работает на переменном токе.» instead of «— Эта машина
  работает на переменном токе.», and «…что механизм с кем-то общается.» instead of «…что машина…». 機械's RU title is
  «машина; механизм», and bare «машина» can be read as a car.
- `合同` (line 22; comprehensibility F5): «— Две компании провели совместную информационную встречу.» instead of «…совместную
  презентацию.», matching EN "joint information session" for 説明会.
- `広さ` (comprehensibility F2, which also adopts correctness's optional title item):
  - lines 4 and 12: title and H1 «величина (пространства); ширина» instead of «протяжённость; величина (пространства)»,
    following EN "spatial extent; width";
  - line 16: «…площадь, размер, величина или ширина.» instead of «…площадь, протяжённость, величина или ширина.»;
  - line 19: «— Размер этой комнаты — двадцать квадратных метров.» instead of «— Площадь этой комнаты — двадцать
    квадратных метров.», which repeated 面積's example translation word for word;
  - line 22: «В сочетании Nの広さ N указывает, величина чего имеется в виду.» instead of «…N указывает, о чьей протяжённости
    идёт речь.» (replaced again by fix 2).
- `打ち合わせ` (lines 46–47; correctness C3 merged with comprehensibility F1 and consistency O2, adapted wording): «Карточка
  учит значению «согласование», а не отдельному значению «нахлёст пол одежды» (портновское «запа́х») и не устаревшему
  значению «точное совпадение одного с другим».» instead of «Карточка учит значению «согласование»; в текстах встречаются
  и другие употребления слова, например о запахе полочек одежды.» (JMdict 1588140 senses 1–3; Digital Daijisen 打ち合わせ).
- `鈍い` (line 59; correctness C2): the source footer now ends «…; отдельная статья のろい — 2838553; статьи для сравнения —
  1174890, 1421970, 1010040, 1013050, 1008190, 1596750 и 2121270.», restoring EN's seven comparison-entry citations.
- `零点` (line 20; correctness optional item): «— К сожалению, я получил ноль баллов за тест.» instead of «— Я получил ноль
  баллов за тест.», for 取ってしまいました (EN "I ended up getting zero").
- `電力` (comprehensibility F6): title and H1 (lines 4 and 12) «электрическая мощность» instead of «электрическая мощность;
  электроэнергия», following EN's single gloss "electric power" and Digital Daijisen 電力 (work per unit time, unit watt);
  line 17 now reads «Её измеряют в ваттах (Вт). Слово встречается и в разговорах о подаче и потреблении электричества.»
  instead of «…о снабжении электроэнергией и её потреблении.» The supply example «Подача электроэнергии» is kept.
- `青少年` (new lines 44–46; correctness C1 merged with comprehensibility F7, adapted wording): «Словарь в общем значении
  указывает возраст примерно 12–25 лет, а в контексте постановлений об охране молодёжи — младше 18 лет. Это определения
  источника, а не единая действующая юридическая граница.» (JMdict 1381570 senses 1–2; Digital Daijisen 青少年). F7's
  «не состоящих в браке» is not in EN and was not added.
- `面積` (line 30; follows F2): «…тоже описывает величину пространства и может означать измеренную площадь.» instead of
  «…тоже описывает протяжённость пространства…».
- The intake note now names the fixed cards, and the nine candidate hashes were refreshed.

Fix 2 changed only `広さ` and regenerated `manifest.json` (`contentVersion` `7f78407f669660fb`, 4,959 entries) and the
intake (comprehensibility R1, adapted wording):
- Line 22: «В сочетании Nの広さ N называет то, о величине чего идёт речь.» instead of fix 1's «…N указывает, величина чего
  имеется в виду.», which did not parse. The reviewer suggested «N указывает, чья величина имеется в виду»; the adopted
  wording follows EN 広さ:23 "Nの広さ identifies what has that extent".

Comprehensibility F3 (DC, AC and LED), consistency's optional O1 (にじゅっ and にじゅう) and comprehensibility's optional
note on the shared 乾電池/電池 translation were not adopted; the dispositions gave the reasons, which the recheck briefs
put to the reviewers (see the reconciliation table).

Before fix 1 the coordinator re-ran its title screen on the two changed titles (広さ and 電力). The only exact title
segment shared with another card is 広さ's «ширина», the first segment of 幅 «ширина; диапазон», which 広さ's EN
exclusion of 幅 already guards; «величина (пространства)» and «электрическая мощность» are each unique to their card.
Fix 2 changed no title. No link changed in either fix, so link parity was unchanged from the candidate: no EN link lost
where the RU target exists, and the same six RU-only links. `tools/validate.py` reported 0 errors before each fix commit.

Net change from the candidate:
- titles and H1s of 広さ and 電力;
- body wording in 広さ, 面積, 電力 and 交流;
- source notes in 青少年 (restored age definitions), 鈍い (restored citations) and 打ち合わせ (excluded senses);
- example translations in 交流, 合同, 広さ and 零点.

No Japanese example sentence, sourced reading, exclusion, link or navigation file changed. Across both fixes the content
diff `e2b0bdb..b281154 -- words` is nine word files, 20 lines added and 16 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, one reviewer at a time, in this order:
1. Correctness, on fix 1.
2. Consistency, on fix 1.
3. Comprehensibility round 1, on fix 1. Its finding R1 led to fix 2.
4. Comprehensibility round 2, on fix 2, for R1 only.

Each brief was sent only after the previous reviewer had replied. Correctness and consistency raised no new finding on
fix 1, and fix 2 changed one sentence that only the comprehensibility reviewer had raised, so they did not recheck fix 2.

Each reviewer appended to its own report file, which stayed in its session context. Each round-1 brief gave the reviewer:
- the fix commit, the reviewed candidate as the base, and the read-only rules;
- the actual content diff `e2b0bdb..955a4e9 -- words`;
- the coordinator's evidence for every change, the post-fix title screen and the declined items, stated without the
  other reviewers' reports;
- the reviewer's original verdicts and the disposition of each of its own findings and optional items. The
  comprehensibility brief asked whether the reviewer maintained its points against the declined F3 and the partial
  adoption of F7, stating that an unresolved disagreement would be recorded as such.

The three round-1 briefs, `b228-recheck-msg-{correctness,consistency,comprehensibility}.txt`, were delivered as session
files that the reviewers were told to read in full. The round-2 brief asked the comprehensibility reviewer to judge R1
and check the changed sentence for regressions against the diff `955a4e9..b281154`.

All recheck messages forbade running `tools/build_manifest.py` or any other generator. Every recheck section states that
none was run. The correctness and consistency reviewers each ran `tools/validate.py` (0 errors each); the consistency
reviewer then deleted the untracked `tools/__pycache__` its run had left. The comprehensibility reviewer ran no validator
in either round. Each recheck section records its snapshot with a clean tree. The fix scripts checked
`git status --porcelain` after each fix commit, and after the last recheck the coordinator confirmed that HEAD was
`b281154` and that `git status --porcelain --ignored` was empty.

### Round 1 (`955a4e9`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer read the complete brief and independently checked the actual nine-card diff against the original review and frozen EN; it did not re-review unchanged cards in full. C1 is **resolved**: 青少年 restores both approximate source ranges as source definitions rather than universal current law, and no marital-status rule is required by frozen EN. C2 is **resolved**: 鈍い restores all seven comparison ids exactly (citation retention, not a fresh audit of those entries). C3 is **resolved**: 打ち合わせ explicitly excludes the clothing overlap and archaic exact matching; its own proposed wording was not mandatory. All three optional items are **resolved** by adoption: 零点 adds regret fitting てしまう; 打ち合わせ explains the overlap and stresses the tailoring term, removing the smell reading; 広さ foregrounds spatial size and width instead of linear extent. No regression: 広さ keeps its spatial scope, square metres still identify area, and 面積's comparison keeps the distinction; 電力's single power gloss agrees with watts while the supply prose and example keep the contextual use; 交流's «механизм» fits 機械; 合同's information session fits 説明会. It found no correctness or coverage defect in the declined items. Validator 0 errors. Correctness and scoped coverage are **CLEAN**. |
| Consistency | Snapshot `955a4e9` with a clean tree; only `tools/validate.py` was run (0 errors). O1 is **optional, declined**: both readings are inherited unchanged from EN and neither is established as wrong. O2 is **resolved**: 打ち合わせ names the clothing overlap and the archaic matching sense and no longer reads as a smell. Titles match their H1s on 広さ and 電力. Across the full RU word pool, «ширина» is shared only by 幅 and 広さ and is guarded by 広さ's EN exclusion of 幅; «величина (пространства)» and «электрическая мощность» are unique. 面積's wording agrees with 広さ, and 面積 still excludes 広さ. The diff touches no exclusion or link, so the RU-added exclusions stay at two and navigation stays 10 files and 10 links; 交流's «механизм» matches the 機械 title. No non-stroke manifest hash mismatches; the intake's 40 hashes match the manifest. Consistency, quiz safety and scoped coverage are **CLEAN**. |
| Comprehensibility | Snapshot `955a4e9` with a clean tree; read the nine changed passages. F1 is **resolved**: the smell reading is gone and both excluded senses are named; «нахлёст пол одежды» is compressed, but with «портновское «запа́х»» and the exclusion frame it no longer teaches a smell (not maintained). F2 is **resolved**: the room lines now differ («Размер» and «Площадь»), and the title and H1 match EN's extent and width. F3 is **withdrawn**: the reviewer accepted the decline, since the Russian terms lead, DC is labelled an international abbreviation and LED電球 is a Japanese spelling with a reading and a Russian gloss. F4, F5 and F6 are **resolved**: «механизм» removes the car reading, «информационную встречу» is an information session, and 電力's title no longer equates it with stored energy while lines 16, 22 and 39 still separate watts from energy. F7 is **resolved**: the two ranges are present as source definitions; «не состоящих в браке» is not maintained, because EN teaches only the two ranges. The 乾電池/電池 item stays **optional**; 零点's «К сожалению» keeps tense and polarity. **R1** (minor; high confidence that the sentence is ungrammatical, medium on learning impact), `広さ.md:22`: «N указывает, величина чего имеется в виду» does not parse, which makes the Nの広さ point harder to read than EN "identifies what has that extent"; remedy «N указывает, чья величина имеется в виду». Comprehensibility **NEEDS FIX** (R1 only); scoped coverage **CLEAN**. |

### Round 2 (`b281154`)

| Facet | Scope and result |
|---|---|
| Comprehensibility | R1 only: snapshot `b281154` with a clean tree; the reviewer read the full revised 広さ and re-reviewed no other card. R1 is **resolved**: «N называет то, о величине чего идёт речь.» parses, and N is the thing whose extent is under discussion, matching EN "identifies what has that extent"; the next sentence still says the unit is named separately. No regression: the room example keeps «Размер», not 面積's «Площадь», and the synonym section still separates width from measured area. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 青少年 drops EN's two source age definitions (minor, coverage) | **Resolved** (adapted wording; merged with comprehensibility F7) | `青少年.md:44–46`; frozen EN 青少年:39–44; JMdict 1381570 senses 1–2; Digital Daijisen 青少年. |
| Correctness C2: 鈍い drops EN's seven comparison-entry citations (minor, coverage) | **Resolved** | `鈍い.md:59–60`; frozen EN 鈍い:42; Jisho 鈍い (1582430). |
| Correctness C3: 打ち合わせ loses the archaic matching boundary (minor, coverage) | **Resolved** (adapted wording; merged with comprehensibility F1 and consistency O2) | `打ち合わせ.md:46–47`; frozen EN 打ち合わせ:43; JMdict 1588140 senses 1–3; Digital Daijisen 打ち合わせ. |
| Correctness optional: 零点 «К сожалению» | **Optional, adopted**; resolved at recheck | `零点.md:20`; 取ってしまいました, EN "I ended up getting zero". |
| Correctness optional: «запа́х (наложение пол одежды)» | **Optional, adopted** (through C3); resolved at recheck | `打ち合わせ.md:46–47`; Kuznetsov запах (tailoring sense). |
| Correctness optional: 広さ title foregrounding area and width | **Optional, adopted** (through F2); resolved at recheck | `広さ.md:4,12`; EN "spatial extent; width". |
| Consistency optional O1: 広さ にじゅっ and 面積 にじゅう | **Optional, not adopted**; kept declined at recheck | Both readings are inherited unchanged from EN; にじゅっ before a voiceless consonant is a standard variant. |
| Consistency optional O2: 打ち合わせ «запахе» wording | **Resolved** (through C3) | `打ち合わせ.md:46–47`. |
| Comprehensibility F1: 打ち合わせ «запахе полочек» reads as a smell (moderate, also coverage) | **Resolved** (merged with C3); not maintained at recheck | `打ち合わせ.md:46–47`; Digital Daijisen 打ち合わせ. |
| Comprehensibility F2: 広さ «протяжённость» and the room example shared with 面積 (minor) | **Resolved** (by fix 1, with fix 2 for the replacement sentence) | `広さ.md:4,12,16,19,22`; `面積.md:30`; EN "spatial extent; width" and "measured area". |
| Comprehensibility F3: unexplained DC, AC and LED (minor) | **Declined; withdrawn** by the reviewer at recheck | EN teaches DC and AC itself ("direct current; DC", "exchange; interaction; AC"); the Russian terms lead, DC is labelled the international abbreviation, and LED電球 is a Japanese word shown with its reading. |
| Comprehensibility F4: 交流 «машина» for 機械 (minor) | **Resolved** | `交流.md:25,27`; 機械 «машина; механизм». |
| Comprehensibility F5: 合同 «презентацию» for 説明会 (minor) | **Resolved** (alternative wording) | `合同.md:22`; EN "joint information session". |
| Comprehensibility F6: 電力 title «электроэнергия» (minor) | **Resolved** | `電力.md:4,12,17`; EN "electric power"; Digital Daijisen 電力. |
| Comprehensibility F7: 青少年 age ranges missing (minor, coverage) | **Resolved** (merged with C1; partially adopted); the remainder not maintained at recheck | `青少年.md:44–46`; EN teaches only the two ranges, so «не состоящих в браке» was not added. |
| Comprehensibility optional: shared 乾電池/電池 translation «Я заменил батарейки в пульте» | **Optional, not adopted**; kept optional at recheck | The reviewer marked it non-blocking; the titles differ. |
| Comprehensibility R1 (recheck of fix 1): fix 1's 広さ:22 sentence does not parse (minor) | **Resolved** by fix 2 (adapted wording) | `広さ.md:22`; EN 広さ:23 "identifies what has that extent"; the reviewer's second recheck. |
| Consistency limit: 118 `strokes/*.json` manifest entries do not match working-tree bytes | **Not a defect**; pre-existing and outside the batch | `tools/build_manifest.py` hashes text files after CRLF→LF normalization; the 118 files are CRLF byte copies of EN blobs kept by `.gitattributes` (`strokes/*.json -text`), as established in Batch 226. The batch touches no `strokes/` file. The reviewer did not recompute them at recheck. |
| Exclusion classification: 採点→勘定 and 打ち合わせ→話し合う | **Agreed: conservative**; kept | The author and the consistency reviewer both classed them conservative; the reviewer called 打ち合わせ→話し合う close to required by parity with the EN guard on 相談 and confirmed at recheck that both are unchanged. |

Cross-batch note: links to absent targets stay plain. Fourteen EN link targets in this batch's new cards (15 occurrences)
are absent from RU: the kanji cards 接 (from 面接), 鈍 (from 鈍い), 蛍 and 灯 (from 蛍光灯), 波 (from 電波), 池 (from 乾電池 and
電池), 柱 (from 電柱), 採 (from 採点) and 零 (from 零点); the word cards 体積 (from 面積), 接近 (from 面接) and 満点 (from 零点);
and the articles japanese-onomatopoeia and onomatopoeia-motion-and-sound (from しーん). EN has kanji cards for all nine of
those kanji; the other written kanji without an RU kanji card, 寸 and 巾, have none in EN either. No links were held from
Batch 227.

## Final exclusion set

All 140 EN exclusion entries (27 lists) are retained in EN order. Two direct, one-sided entries are added on two new cards
(no new list):

- Conservative (2): 採点→勘定 and 打ち合わせ→話し合う, both added at the candidate; neither fix changed an exclusion.

Every RU addition is appended at the end of its list; nothing is removed or reordered. Android applies each declaration
symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** throughout; the 零点 optional item and the 広さ title item were adopted.
- Scoped coverage: **CLEAN** after fix 1 (青少年, 鈍い, 打ち合わせ).
- Comprehensibility: **CLEAN** after the fixes (打ち合わせ, 交流, 合同, 電力; 広さ and 面積 after fix 2); the declined F3 was
  withdrawn, and the shared 乾電池/電池 translation remains optional.
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** throughout, including the 広さ and 電力 retitles. This covers the reviewed batch and the directly
  adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them; the second comprehensibility recheck
  read only 広さ. The unchanged cards rest on review 001, in which the correctness and comprehensibility reviewers read
  all 30 cards in full against EN and the consistency reviewer read all 30 cards in full and compared their front matter
  and links with EN.
- Correctness and consistency did not recheck fix 2, which changed only one sentence of 広さ with no title, exclusion,
  link or navigation change.
- The correctness recheck was a bounded diff recheck on the original evidence, not a fresh dictionary audit; it did not
  re-audit the seven 鈍い comparison entries. The consistency reviewer did not reopen dictionary pages, did not recompute
  the stroke hashes, and its necessity classes are judgements, not measurements. The comprehensibility reviewer did not
  re-fetch dictionaries, run the validator or audit quiz exclusions at recheck.
- The correctness reviewer's initial API requests met HTTP 429 and its raw JMdict archive request failed TLS validation;
  failed responses were not used, and no raw-XML check is claimed. The comprehensibility reviewer fetched Daijisen only
  for 打ち合わせ, 青少年 and 電力.
- The consistency reviewer saw CR bytes in the working tree, which uses checkout line-ending conversion; the committed
  blobs of all 40 content paths contain no CR.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.

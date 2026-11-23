# Batch 248 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `14cc61a3526acddf05f23db55318f168a6d55b44` | `6813010a904c7b243be5fd05a86333b6e79affa8` | Initial review snapshot: the signed candidate, on `origin/full-ru-248-words-87`. |
| `c43dd9f5c1f42eae861f7365dbd0d00600378d3a` | `7a976ec6d23be9b5ae055aaeda9cd8b69685ca44` | Fix 1 (final candidate). It covers correctness F1 and F2, consistency O1 and O2 and comprehensibility C1–C10 (C1, C2 for 盛る, C4, C6, C7 and C8 with modification), plus the comprehensibility optional notes on 盛る:37 and 皮膚:35 and the correctness optional notes on English glosses and source-list wording. It retitles 中身, 発想 and 皮膚, rewrites example translations and prose in 目次, 目立つ, 発想, 盆地, 派手, 発射, 発揮, 盗難, 白髪, 百科事典, 盛る, 中身 and 皮膚, adds four exclusions (中身→要旨, 皮膚→革, 登場→誕生 and 発射→飛ばす) and changes no link or navigation-only file. Signed; on `origin/full-ru-248-words-87`. |

The fix regenerated `manifest.json`; both snapshots record 5,559 entries (5,554 `files` + 3 images + 2 scenes).
`contentVersion` is `b4e194062bc4c700` at the candidate and `637830dcf28ab97b` after fix 1. The intake was not
refreshed; it still records the candidate's payload hashes. The commit message reads "Batch 248 fix 1: apply
blind-review dispositions", followed only by the co-author trailer.

Fix 1:
- `目次` (line 18; correctness F1, verbatim): «Я искал в оглавлении главу, которую хотел прочитать.» instead of «Я нашёл в
  оглавлении главу, которую хотел прочитать.»
- `目立つ` (line 19; correctness F2, verbatim, which also covers comprehensibility C4): «Он высокий, поэтому хорошо
  заметен.» instead of «Он высокий, поэтому всегда на виду.»
- `中身` (lines 4, 9, 12 and 25; comprehensibility C5, and C6 with modification): title and H1 «содержимое; суть» instead
  of «содержимое; наполнение»; `quiz_exclusions` appends 要旨; «…словарь помечает это написание как атэдзи: знак выбран по
  звучанию, а не по значению «вкус».» instead of «…словарь помечает это написание как атэдзи.»
- `発想` (lines 4, 12 and 18; comprehensibility C7, with modification): title and H1 «идея; подход (к задаче)» instead of
  «образ мысли; подход (к задаче); концепция»; the example reads «Интересная идея.» instead of the coordinator's candidate
  wording «Интересная мысль.»
- `皮膚` (lines 4, 9, 12 and 35; comprehensibility C10 and the optional on line 35): title and H1 «кожа; кожный покров»
  instead of «кожный покров»; `quiz_exclusions` appends 革; «…а не так, будто 皮 и 膚 называют два разных слоя кожи.»
  instead of «…а не как два технических слоя кожи.»
- `派手` (line 31; comprehensibility C3, verbatim): «Перед существительным нужно 派手な, а не форма на い.» instead of «Не
  путайте его грамматику な-прилагательного с окончанием い-прилагательного: перед существительным нужно な.»
- `発射` (line 9 added and candidate line 30, now 31; consistency O1 and comprehensibility C1 with modification, in the
  correctness reviewer's optional wording): `quiz_exclusions: [飛ばす]` added (the card had no key); «発射 называет действие
  запуска, а не пусковое устройство.» instead of «Английский перевод catapult в источнике относится к запуску, а не к
  самому устройству как предмету.»
- `発揮` (line 31; comprehensibility C1, with modification): «発揮 — не общее слово для выставки: выставку называет
  [展覧会](展覧会.md)（てんらんかい）.» instead of «Английский перевод exhibition («показ, выставка») в словаре не делает 発揮
  общим словом для [展覧会](展覧会.md)（てんらんかい）.»
- `盗難` (line 33; comprehensibility C1, with modification): the sentence «Широкий английский перевод robbery
  («ограбление») в словаре не означает, что каждая 盗難 связана со столкновением.» is deleted rather than replaced.
- `白髪` (line 33; comprehensibility C2, verbatim): the sentence «Дополнительный перевод в списке источника о модном
  обесцвечивании не подтверждается проверенной записью как отдельное значение.» is deleted.
- `百科事典` (line 15; comprehensibility C2, verbatim): the sentence «Кана источника ひゃっかじてん обозначает именно это
  слово.» is deleted.
- `盛る` (lines 21, 23 and 37; comprehensibility C2 and C8 with modification, and the optional on line 37 with
  modification): «Но 盛る — не обычный глагол для врача, выписывающего рецепт: для этого есть 処方する（しょほうする）.» instead
  of «Перевод «прописывать» в источнике не стоит понимать как обычный глагол для врача, выписывающего рецепт: это
  処方する（しょほうする）.»; «Дополнительное сленговое значение — …» instead of «Дополнительное разговорное значение — …»;
  «…разные употребления, а не указание переводить каждое 盛る словом «накладывать».» instead of «…каждое из них как
  «подавать».», and «Медицинское и сленговое значения не делают все употребления зловещими или сленговыми.» instead of
  «Медицинское и разговорное значения … просторечными.»
- `盆地` (line 18; comprehensibility C9, verbatim): «В котловине, окружённой горами, поднялся туман.» instead of «В
  межгорной впадине, окружённой горами, поднялся туман.»
- `登場` (line 9; consistency O2): `quiz_exclusions` appends 誕生 (`[現れる, 出る, 紹介, 誕生]`); no prose changed.

All fourteen are new Batch 248 cards. No navigation-only file changed, so navigation stays at 4 files / 4 links, all
EN-position restorations. The coordinator's candidate edits stand except where listed above (発想:18 and the 盛る:23
register word; 皮膚's example «Кожа сухая.» and the split paragraphs are unchanged).

Declined, modified or partially adopted, with the dispositions' reasons (see the reconciliation table):
- Correctness F2 / comprehensibility C4: the comprehensibility remedy «часто бросается в глаза» is not used, "because the
  frequency reading is the one F2 disputes". At recheck the correctness reviewer qualified this: "Daijisen よく sense 2
  supports degree; sense 6 permits frequency, so the disposition must not categorically reject that sense." It still
  judged F2 resolved, and the comprehensibility recheck judged C4 "resolved, modified". The adopted wording is not
  affected; the qualification concerns the stated reason.
- Comprehensibility C1 was accepted with modification: 発射 uses the correctness reviewer's Russian-only sentence; "the
  robbery sentence is deleted rather than replaced. Line 29 already states «[強盗](強盗.md)（ごうとう）— грабёж с применением
  силы или угроз; для 盗難 это не обязательно», which is the proposed replacement's content."; for 発揮 "The subject is
  named because the preceding sentence is about the object; the EN link to 展覧会 is kept."
- Comprehensibility C2 was accepted, "盛る with modification": the 盛る sentence is reworded rather than following the
  reviewer's text.
- Comprehensibility C6 was accepted with modification: "The deck term «атэдзи» is kept (45 published cards use it) but
  explained in place".
- Comprehensibility C7 was accepted with modification: "The «подход (к задаче)» parenthetical is kept because line 19
  teaches 発想を変える as changing one's approach." The reviewer's title was «идея; подход».
- Comprehensibility C8 was accepted with modification: «сленговое» instead of the reviewer's «жаргонное» ("JMdict sense 6
  tag Slang; EN "slang use""), and line 37 changed "so the card uses one register label".
- Comprehensibility optional 盛る:37 was accepted with modification: "EN "serve" corresponds to the RU title's first
  gloss."
- The other comprehensibility optionals were declined: "目安 title length, 狙い «нацеленность», 的確:19 «по существу»,
  中身:33, 狙う:25 «окуригана», 発電/能率 «выработка» — DECLINE. Each is correct Russian faithful to EN; «окуригана» is the
  deck's established term (150 word/kanji files); 中身:33 follows EN lines 51–52 and the reviewer's proposed other entry is
  unverified; 発電 «выработка электроэнергии» and 能率 «… выработка» share no exact title segment."
- The consistency reviewer's note on the inherited missing `kango` tag on 的確 and 盆地 needed no action (EN parity).

Post-fix screen: a saved rerun at the committed `c43dd9f` over all 30 batch words (`b248-postfix-screen.txt`, 267 lines)
has 34 `OK` lines for pairs already guarded by an exclusion and 233 `!!` lines. Its nine exact-segment lines are all
`OK`: 中身–内容, 実 and 要旨 («суть»), 狙い–考え («замысел»), 皮膚–肌 and 革 («кожа»), and 発想–アイデア, アイディア and 考え
(«идея»). Against the candidate screen (284 lines) it removes 40 lines and adds 23: 発想 32 removed and 15 added, 中身 7
and 5, 皮膚 0 and 2, and 登場 1 and 1, the 登場–誕生 stem-only line («появл») changing from `!!` to `OK`. The dispositions
record "every exact-segment hit is now guarded (中身–内容/実/要旨 «суть»; 発想–アイデア/アイディア/考え «идея»; 皮膚–肌/革
«кожа»)".

Net change from the candidate:
- titles and H1s of 中身, 発想 and 皮膚;
- example translations in 目次, 目立つ, 発想 and 盆地;
- prose in 派手 (line 31), 発射 (line 31), 発揮 (line 31), 盗難 (line 33), 白髪 (line 33), 百科事典 (line 15), 盛る (lines 21,
  23 and 37), 中身 (line 25) and 皮膚 (line 35);
- four exclusions added (中身→要旨, 皮膚→革, 登場→誕生 and 発射→飛ばす), none removed;
- no link added, removed or retargeted.

No Japanese example sentence, sourced reading, kanji card, EN exclusion or link target changed. The content diff
`14cc61a..c43dd9f -- words` is 14 word files, 25 lines added and 24 removed (the extra line is 発射's new exclusion key);
with `manifest.json` the fix changes 15 files, 40 lines added and 39 removed.

Fix 1 validation, as recorded in the dispositions: "`tools/validate.py` 0 errors; manifest rebuilt (5,559 files incl. 3
images and 2 scene catalogs); 124 unit tests OK; content budget OK; `git diff --check` clean; link parity unchanged from
the candidate (34 paths; only the reviewed RU-only 狙う → 目指す link)." For this record link parity was verified again
over the 34 batch paths at `c43dd9f` (no LOST link; one EXTRA, the RU-only `words/狙う.md` → `words/目指す.md`), and the
link targets in the fix diff were compared: fix 1 adds, removes and retargets none.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks were sent to the original reviewer agents, so each reviewer retained its own blind report. They kept the same
model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are the variants the coordinator assigned at launch. Reviewer prose did not expose separate serving
IDs; the correctness recheck says "Model identity not independently verifiable." and the comprehensibility recheck
"Model: not verifiable."; the consistency recheck makes no statement about model identity. The dispositions label each reviewer's model "per
runtime status".

The rechecks ran serially, one reviewer at a time, in one round: comprehensibility, then correctness, then consistency,
each on the fix diff `14cc61a..c43dd9f` (14 word files and `manifest.json`). The initial reviews had run correctness,
then consistency, then comprehensibility. These orderings rest on the coordinator's session records; the recheck reports
do not record times. There was no second fix and no follow-up exchange.

Rechecks were returned as separate reports rather than appended to the initial review files: the full texts are in
`b248-recheck-correctness.md`, `b248-recheck-consistency.md` and `b248-recheck-comprehensibility.md` in the
coordinator's session folder, and their content is recorded in the round table below. The recheck briefs were sent
through the agent-messaging channel and were not saved as files; each recheck's scope is described here from its own
Snapshot and Scope lines.

No recheck ran a generator. The correctness recheck records "Only this report was written; no repository changes or
generators."; the consistency recheck called `build_manifest` in memory ("nothing written") and ran `tools/validate.py`
and `word_title_screen.py`; the comprehensibility recheck makes no statement about generators or the validator. The
correctness recheck records `c43dd9f5c1f42eae861f7365dbd0d00600378d3a` with parent
`14cc61a3526acddf05f23db55318f168a6d55b44` and "HEAD matches and git status --porcelain is empty at start and end."; the
consistency recheck records HEAD `c43dd9f5` with "`git status --porcelain --ignored` empty at start and end." and "No
`__pycache__` found in the repo."; the comprehensibility recheck records `c43dd9f5c1f42eae861f7365dbd0d00600378d3a` with
"git status --porcelain empty at start and at this write." When these records were drafted, a read-only check showed the
RU checkout at HEAD `c43dd9f5c1f42eae861f7365dbd0d00600378d3a` with `git status --porcelain --ignored` printing nothing.

### Round 1 (`c43dd9f`)

| Facet | Scope and result |
|---|---|
| Comprehensibility | `c43dd9f`, parent `14cc61a`, porcelain empty at start and at the write. "recheck of C1–C10 and the optional notes against the fix diff and the changed text. Read in full:" the 14 changed cards; "Titles checked for the new exclusions: 飛ばす, 誕生, 要旨, 革, and for the retitles also 内容, 実, 肌." C1, C2, C3, C5, C9 and C10 **resolved**, for example C1 "the action-versus-device point, with no English gloss; the modified wording holds. The 盗難 robbery sentence is deleted; synonyms already say 強盗 is force or threats, so a second sentence was redundant."; C5 "要旨 is excluded because its title contains «суть»; the visible answers still differ … Not a regression."; C10 "matching «Кожа сухая.» 肌 and 革 are excluded. The body still separates 皮 and 肌; not naming 革 does not teach leather as 皮膚." C4, C6, C7 and C8 **resolved, modified**: C4 "«よく» is degree, not «всегда» and not «часто». Holds"; C6 "«атэдзи» stays, now glossed as a character chosen for sound, not for «вкус»"; C7 "«концепцию» is no longer a quiz answer. Holds."; C8 "«жаргонное» was not required. Holds." Optional: "盛る.md:37 resolved"; "皮膚.md:35 resolved — it names 皮 and 膚."; the declined optionals: "None is a false teaching point." New text in 目次, 登場 and 発射 checked: "発射→飛ばす is metadata; the new device sentence does not collide with «запускать (в воздух)»." "Findings: none". Verdicts: "comprehensibility CLEAN; scoped coverage CLEAN". Limits: "unchanged cards were not reread in full. JMdict was not re-queried. Exclusion direction was not retested. Model not verifiable." |
| Correctness | `c43dd9f` against `14cc61a`, porcelain empty at start and end. "Supplied diff matches committed words diff (newline-normalized)."; "Full RU/EN reread attestation, each path:" the 14 changed cards; "added exclusion targets 要旨, 革, 飛ばす, 誕生 exist and have relevant taught senses." F1 "RESOLVED, high confidence" ("Reopened Daijisen 探す defines attempting to find; remedy accepted verbatim."); F2 "RESOLVED, high confidence" ("Daijisen よく sense 2 supports degree; sense 6 permits frequency, so the disposition must not categorically reject that sense. Correction: EN says “He stands out because he is tall”, not my earlier “stands out easily”; the finding remains supported."). Changed-passage checks: 中身 (JMdict 1599430 senses 1–2; :25 "phonetic spelling, not a historical etymology"), 発想 (1477660 senses 1–2), 皮膚 (1483920 sense 1; :35 "not an anatomical assertion"), 盛る (Daijisen もる sense 3, 処方 sense 2; «сленговое» matches 1379740 sense 6's Slang tag and Daijisen's 俗に), 派手, 盆地, 発揮, 発射 and the deletions ("No necessary sourced claim lost."). "Base/fix checks passed in all 14: Japanese examples/kana, front matter except titles/exclusions, complete footers and ordered link destinations identical; local targets exist. Original exclusions retained; only 要旨/革/飛ばす/誕生 added." Its six original optional notes (発射 "catapult", 盗難 "robbery", 発揮 "exhibition", 盛る and 白髪 source-list wording, 百科事典 «Кана источника») all **RESOLVED**: "No original optional note remains unresolved; no new optional finding." Reopened: Jisho/JMdict for 中身, 発想, 皮膚, 盛る, 処方, 発揮, 発射, 派手, 盆地, 盗難, 白髪 and 百科事典, and Digital Daijisen via weblio.jp for 探す, よく, 盛る, 処方 and 盗難. Verdicts: "correctness CLEAN; scoped coverage CLEAN for all 14 changed cards. F1/F2 resolved; no new actionable defect established. CLEAN is bounded absence of established defects, not exhaustive correctness." Limits: "manifest/tests/device claims in dispositions not independently validated. No generators, full-corpus quiz audit or repeat review of unchanged cards. Original limits remain outside changed passages." |
| Consistency | HEAD `c43dd9f5` (parent `14cc61a3`), `--ignored` porcelain empty at start and end. "Diff: 14 word cards + manifest.json." O1 "RESOLVED. 発射 now has `quiz_exclusions: [飛ばす]`; target exists."; O2 "RESOLVED. 登場 is now `[現れる, 出る, 紹介, 誕生]`; target exists, earlier guards retained."; 中身, 皮膚 and 発想 notes "RESOLVED"; the wording fixes "RESOLVED" ("I judged them on the diff text."); declined remedies "OPTIONAL. These were cosmetic or style choices; I found no consistency or quiz risk, so declining them is sound."; inherited `kango` "OPTIONAL, inherited from EN and unchanged." Title screen of 中身, 発想 and 皮膚: "shared-segment hits are all guarded"; "All new exclusion targets exist as word cards … No self-guards or duplicates."; old titles: "grep of words/kanji/articles/grammar/counters found no remaining «образ мысли», «кожный покров» (outside 皮膚) or «содержимое; наполнение»." Manifest: "`build_manifest` in memory equals the committed manifest.json."; "same file set, 14 entries differ, and only `contentVersion` changed at top level."; "`tools/validate.py`: 0 errors." Links: "No fix-diff line changed any link markup … (the only RU-only link remains 狙う→目指す, no LOST links). I did not re-run `link_parity.py`; this is by diff inspection."; navigation diff empty, "so the 4 nav files and 4 links are unchanged." Verdicts: "Consistency: CLEAN"; "Quiz safety: CLEAN"; "Navigation: CLEAN (unchanged)"; "Manifest: CLEAN"; "New findings: none". Optional: "None open." Limits: "Did not run `link_parity.py`."; "Other reviewers' reports were not read. Linguistic correctness is outside this scope." |

No recheck raised a new finding or left an optional note open. The correctness reviewer's qualification of the よく
disposition reason is recorded above; it did not reopen F2. There was no second fix.

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 目次:18 «нашёл» asserts a successful find (medium) | **Resolved** | `目次.md:18`; Daijisen 探す; correctness recheck "RESOLVED, high confidence". |
| Correctness F2: 目立つ:19 «всегда» adds "always" (low) | **Resolved** | `目立つ.md:19`; Daijisen よく sense 2; correctness recheck "RESOLVED", with the sense 6 qualification of the dispositions' reason. |
| Correctness optional: 発射 "catapult" | **Resolved** | `発射.md:31`; the reviewer's remedy used. |
| Correctness optional: 盗難 "robbery", 発揮 "exhibition" | **Resolved** (with C1) | `盗難.md:33`, `発揮.md:31`; correctness recheck "RESOLVED". |
| Correctness optional: source-list wording in 盛る, 百科事典 and 白髪 | **Resolved** (with C2) | `盛る.md:21`, `百科事典.md:15`, `白髪.md:33`; correctness recheck "RESOLVED". |
| Consistency O1: 発射–飛ばす | **Resolved** | `発射.md:9`; JMdict 飛ばす launch sense per the dispositions; consistency recheck "RESOLVED". |
| Consistency O2: 登場–誕生 | **Resolved** | `登場.md:9`; titles share «появление»; consistency recheck "RESOLVED". |
| Consistency note: 中身 «наполнение» thin for «суть» | **Resolved** (with C5) | `中身.md:4,12`. |
| Consistency note: 皮膚 «кожный покров» chosen to avoid 肌 | **Resolved** (superseded by C10) | `皮膚.md:4,9,12`; 肌 and 革 excluded. |
| Consistency note: inherited missing `kango` on 的確 and 盆地 | **Optional**; no action (EN parity) | Consistency recheck "OPTIONAL, inherited from EN and unchanged." |
| Comprehensibility C1: English glosses in 発射, 盗難 and 発揮 (medium) | **Resolved** (with modification) | `発射.md:31`, `盗難.md:33`, `発揮.md:31`; comprehensibility recheck "the modified wording holds". |
| Comprehensibility C2: unseen-source references in 白髪, 盛る and 百科事典 (medium) | **Resolved** (盛る with modification) | `白髪.md:33`, `盛る.md:21`, `百科事典.md:15`; comprehensibility recheck "Holds." |
| Comprehensibility C3: 派手:31 い-adjective warning (medium) | **Resolved** | `派手.md:31`. |
| Comprehensibility C4: 目立つ:19 frequency (medium) | **Resolved** (with modification, via F2) | `目立つ.md:19`; comprehensibility recheck "resolved, modified". |
| Comprehensibility C5: 中身 title drops substance (medium) | **Resolved** | `中身.md:4,9,12`; JMdict 1599430 senses 1–2; 要旨 excluded. |
| Comprehensibility C6: 中身:25 «атэдзи» unexplained (medium) | **Resolved** (with modification) | `中身.md:25`; correctness recheck "phonetic spelling, not a historical etymology". |
| Comprehensibility C7: 発想 title and line 18 (medium) | **Resolved** (with modification) | `発想.md:4,12,18`; JMdict 1477660 senses 1–2. |
| Comprehensibility C8: 盛る:23 register (medium) | **Resolved** (with modification) | `盛る.md:23,37`; JMdict 1379740 sense 6 Slang; Daijisen 俗に. |
| Comprehensibility C9: 盆地:18 repeats the mountains (low) | **Resolved** | `盆地.md:18`. |
| Comprehensibility C10: 皮膚 title (low) | **Resolved** | `皮膚.md:4,9,12`; JMdict 1483920 sense 1; 革 excluded. |
| Comprehensibility optionals: 盛る:37 «подавать», 皮膚:35 | **Resolved** (盛る:37 with modification) | `盛る.md:37`, `皮膚.md:35`; comprehensibility recheck "resolved". |
| Comprehensibility optionals: 目安 title length, 狙い «нацеленность», 的確:19, 中身:33, 狙う:25 «окуригана», 発電/能率 «выработка» | **Optional**; declined, no defect | Comprehensibility recheck "None is a false teaching point."; consistency recheck "declining them is sound". |
| Coordinator's unverified Russian (Lopatin spelling of «Бон/Обон») | **UNVERIFIED** by the coordinator; not a defect | The correctness review verified ru.wikipedia usage («Обон … или Бон») but "normative Russian spelling-dictionary attestation remains unverified"; no Russian dictionary was reopened at recheck. |
| Consistency reviewer's extra plain targets (仮説, 上司, 予想どおり, 退場, トレー, 撃つ, 部下) | **Reviewer error**; no action | These are not EN link targets; link parity lists five plain targets. |

Cross-batch note: links to absent targets stay plain. Six EN link occurrences in this batch's new cards, to 5 targets,
are absent from RU: kanji 準 (from 標準), 皮 (from 皮膚 and 皮肉) and 膚 (from 皮膚), and words 地味 (from 派手) and 平野
(from 盆地). The other written kanji without an RU kanji card, 仮, 典, 射, 推, 揮, 案, 標, 派, 狙, 的, 盆, 盛 and 身, have
none in EN either. No EN link to an existing card is dropped. The one RU-only link, 狙う:29 → 目指す, is to a card of this
batch and is unchanged by fix 1. No link was held from an earlier batch, and none is held for a later one. The four
navigation-only restorations (kanji/外.md line 41 to 案外; words/目下.md line 33 to 目上; words/課程.md and words/過程.md
line 33 to 仮定) are unchanged by fix 1; their existing glosses «неожиданно» and «предположение» are consistent with the
final 案外 and 仮定 titles. Every exclusion target resolves to a card published at the baseline or to a batch card.

## Final exclusion set

All 145 EN exclusion entries (26 lists; EN has none on 盆地, 百科事典, 発電 or 発射) are retained in EN order; 14 of them lie
inside the batch, and the other 131 target existing RU cards. Ten direct, one-sided entries are added on eight new
cards, none targeting a batch word; each is appended at the end of its list:

- 中身→内容 and 中身→要旨: `[実, 身, 中, 内, 内側, 内容, 要旨]`;
- 推定→観測 and 推定→読み: `[仮定, 予測, 予想, 見当, 予算, 判断, 想像, 計算, 予定, 観測, 読み]`;
- 目安→観測: `[基準, 標準, 水準, 参考, 目標, 目的, 狙い, 見当, 予測, 推定, 程度, 予算, 観測]`;
- 案外→ところが: `[意外, ふと, ばったり, ひょいと, ところが]`;
- 発揮→現れ: `[現す, 表す, 示す, デモ, 活用, 現れ]`;
- 皮膚→革: `[肌, 皮, 革]`;
- 登場→誕生: `[現れる, 出る, 紹介, 誕生]`;
- 発射→飛ばす: `[飛ばす]` (the only RU-added list).

Six were present at the candidate and accepted by the coordinator ("発揮→現れ (required: shared «проявление»); 中身→内容,
推定→観測, 推定→読み, 目安→観測, 案外→ところが (conservative)"); the consistency reviewer classed 中身→内容, 案外→ところが and
発揮→現れ as required and the three 観測/読み entries as conservative, adding "None is unjustified." Fix 1 added 中身→要旨
(C5) and 皮膚→革 (C10), each for an exact title segment («суть», «кожа»), and 発射→飛ばす (O1) and 登場→誕生 (O2), which
the consistency reviewer raised as low-confidence optionals; the consistency recheck resolved both. The guarded
exact-segment pairs in the post-fix screen are covered by entries in the batch card's own list. Every RU addition is
appended at the end of its list, and no EN entry is removed or reordered. Android applies each declaration
symmetrically (EN `docs/content-format.md`, lines 162–165), so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fix 1 (目次 F1, 目立つ F2); CLEAN at recheck for all 14 changed cards.
- Scoped coverage: **CLEAN** throughout in the correctness and comprehensibility reviews and rechecks.
- Comprehensibility: **CLEAN** after fix 1 (派手, 目立つ, 中身, 発想, 盛る, 盗難, 盆地, 皮膚, 百科事典, 白髪, 発揮 and 発射);
  the modified dispositions of C1, C2 (盛る), C4, C6, C7 and C8 stand as accepted.
- Cross-file consistency: **CLEAN** throughout; the four restored navigation links in four files and the RU-only
  狙う→目指す link stand.
- Quiz safety: **CLEAN** throughout, including the three retitles; the ten RU additions stand. This covers the reviewed
  batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread the changed cards and the lines needed to judge them; the unchanged cards rest on review 001, in
  which all three reviewers read all 30 cards in full. The correctness recheck did no "repeat review of unchanged
  cards", and the comprehensibility recheck states "unchanged cards were not reread in full."
- In review 001 the consistency reviewer compared EN programmatically ("It was not a line-by-line prose read.") and cited
  dictionary senses from memory; the comprehensibility reviewer cited JMdict from the public Jisho API and did not
  re-query it at recheck. The consistency recheck judged the wording fixes "on the diff text" and did not re-run
  `link_parity.py`; link parity at the fix was rerun for this record. Necessity classes are judgements, not measurements.
- The correctness recheck did not independently validate the dispositions' manifest, test or device claims.
- The recheck briefs were not saved as files; each recheck's scope is taken from its own report.
- The serial order of the reviews and rechecks rests on the coordinator's session records.
- The intake was not refreshed by the fix, so its payload hashes describe the candidate `14cc61a`, not `c43dd9f`.
- Frequency and preferred register (for example «сленговое», «котловина», «атэдзи» and the «Бон/Обон» spelling) were not
  certified. Online dictionaries were current observations, not pinned archives. The app's quiz selection was not
  inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.

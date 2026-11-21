# Batch 226 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `bebdf808fd419165e2b6098bd25d815f7c41c235` | `acea83488c876c2f725c512d68e7db0c9584fba9` | Initial review snapshot: the signed candidate, pushed before review. |
| `199a6941e882d68db6e9c685d74529b6d93af804` | `d06acb1ccf4c53f4aee18e22871f403795e3edf8` | Fix 1 (final candidate). It covers correctness C1–C5, comprehensibility C1–C9, the adopted optional items (two from correctness, four from comprehensibility and the consistency item on 刺す), three conservative guards and the intake refresh. Signed and pushed before the rechecks. |

Fix 1 changed 14 word files and regenerated `manifest.json` (`contentVersion` `768b61617da5f468`, 4,899 entries; the
candidate had `016ea287bd61d6c7`) and the intake:
- `騒がしい` (lines 4 and 12; correctness C1, the reviewer's wording, and the comprehensibility optional item): title and
  H1 «шумный; неспокойный (о времени)» instead of «шумливый; …», which means inclined to make noise. Kuznetsov шумливый;
  JMdict 1403000 senses 1–2.
- `騒々しい` (lines 4 and 12; correctness C1 and comprehensibility C3, partially accepted): title and H1 «шумный;
  беспокойный (об обстановке)» instead of «галдящий; …», a colloquial word for people talking loudly together. The
  comprehensibility reviewer's «крикливый» lead was not used: Digital Daijisen 騒騒しい covers noisy rooms and nonhuman
  sounds, and the correctness reviewer found the voice-only reading too narrow. The overlap with うるさい «шумный;
  назойливый» is guarded on both cards, and 騒々しい excludes 騒がしい.
- `騒々しい` (lines 32 and 34; correctness C4, adapted): «В этой коллекции слово условно отнесено к канго (словам,
  построенным на онных чтениях):» instead of «Здесь это слово отнесено к канго — словам китайского происхождения с онными
  чтениями:», and «Это учебная классификация, а не утверждение об установленном историческом происхождении:». The
  following note on competing origins and ateji is kept (Seisenban on Kotobank).
- `挙げる` (lines 4, 9 and 12; correctness C2): title and H1 «поднимать (руку); приводить (пример)» instead of «приводить
  (пример); перечислять», restoring EN "raise" (JMdict 2864818 senses 9 and 1). The body already taught 手を挙げる. New
  conservative guards 挙げる→上がる (inserted after EN's 上げる) and 挙げる→立てる (appended): `quiz_exclusions: [上げる,
  上がる, 持ち上げる, 捕まえる, 逮捕, 推薦, 勧める, 示す, 収める, 得る, 立てる]`.
- `驚かす` (lines 4 and 12; correctness C2): title and H1 «удивлять; пугать» instead of «удивлять; поражать», restoring
  EN "frighten" (JMdict 1238650 sense 1). The existing 驚かす→おどかす guard covers «пугать».
- `裁縫` (lines 4, 12 and 16; correctness C3, alternative wording, and the comprehensibility optional item): title and H1
  «кройка и шитьё» instead of «шитьё; рукоделие»; the definition now reads «裁縫 — кройка и шитьё: ткань раскраивают и
  сшивают из неё одежду и другие вещи.», adding the cutting step of Daijisen 裁縫. Line 29 keeps 針's own sense.
- `強化` (line 35; correctness C5): «…это [固まる](固まる.md)（かたまる）или 固める（かためる）, а не 強化…», adding the
  reading of the unlinked 固める (JMdict 1266570).
- `高層` (lines 4, 9, 12, 17 and 21; comprehensibility C1 and optional item): title and H1 «высотный; верхние слои
  атмосферы» instead of «многоэтажный; …»; line 17 «а также к высотному зданию» instead of «к высокому многоэтажному
  зданию»; the example «— Мы изучаем движение воздушных течений на большой высоте.» instead of «…высотных воздушных
  течений». Digital Daijisen 高層. New conservative guard 高層→高度 (shared «высот-»; 高度 «высота; передовой уровень»):
  `quiz_exclusions: [高い, 上, ビル, 高度]`.
- `飾り` (lines 4, 12 and 16; comprehensibility C2 and the correctness optional item): title and H1 «украшение» instead
  of «украшение; орнамент»; the definition «飾り — украшение: то, что украшает предмет, человека или место.» (Gramota
  орнамент). EN "decoration; ornament" maps to «украшение»; アクセサリー and 飾る stay excluded.
- `高等` (lines 4 and 12; comprehensibility C4, alternative wording, and the correctness optional item): title and H1
  «высшей ступени; высокого уровня» instead of «…; высокого порядка», matching line 16 «высокий разряд, ступень или
  уровень»; 高度 «передовой уровень» is mutually excluded.
- `高級` (lines 4 and 12; comprehensibility C5): title and H1 «высокого класса; класса люкс» instead of «…; элитный»,
  matching line 16. クラス, クラシック and 黒板 share only the «класс» stem in another sense, so no guard was added.
- `飽くまで` (lines 23 and 41–42; comprehensibility C7, alternative wording, and C6, the reviewer's wording): «Написание
  飽くまで в заголовке карточки — **редкое написание кандзи**.» instead of «…из исходного списка…», and «Не переводите
  каждое употребление как «упрямо». Ограничительное значение не делает あくまで автоматической заменой
  [やはり](やはり.md), «как и ожидалось».», without the English gloss "after all".
- `挿す` (line 23; comprehensibility C8): «Это не обязательно прививка, то есть соединение ветки с другим растением.»,
  without the English gloss "graft" (JMdict 1399830 sense 2).
- `餅` (line 29; comprehensibility C9, the reviewer's wording): «餠 — редкий вариант написания, его не нужно учить.»
  instead of «…вариант только для поиска в закреплённом словаре».
- `刺す` (line 32; comprehensibility optional item): «Написание 螫す встречается редко и не нужно для обычного примера с
  комаром.» instead of «…лишь как поисковый вариант…».
- `刺す` (line 44; consistency optional item): «Это отдельное употребление, а не тот же «укус» насекомого.» instead of
  «Это не просто ещё один способ сказать, что её кусает насекомое.» (EN "not merely another way to say that an insect
  bites it").
- The intake note now names the fixed cards, and the 14 candidate hashes were refreshed.

Comprehensibility's optional 一流, 馴れる and «атэдзи» suggestions were not adopted, and its outside-facet Q1 (a reverse
ビル–高層 exclusion) was withdrawn; the dispositions gave the reasons, which the recheck briefs put to the reviewers (see
the reconciliation table).

Titles changed on nine cards, so the coordinator re-ran its title screen on them: no unguarded exact title-segment
overlap; the remaining stem-only hits are different senses (время, беспокойство, пример, атмосфера, ступень, класс). No
link changed, so link parity was unchanged from the candidate: no EN link lost where the RU target exists, and the same
single RU-only link. `tools/validate.py` reported 0 errors.

Net change from the candidate:
- titles and H1s of 騒がしい, 騒々しい, 挙げる, 驚かす, 裁縫, 高層, 飾り, 高等 and 高級;
- definitions in 裁縫, 高層 and 飾り, and one example translation in 高層;
- note wording in 騒々しい, 強化 (a reading in plain text), 飽くまで, 挿す, 餅 and 刺す;
- three added exclusion entries (挙げる→上がる and 立てる, 高層→高度).

No Japanese example sentence was altered, and no sourced reading, EN exclusion or link changed; 飽くまで's link line was
only re-wrapped. The content diff is 14 word files, 34 lines added and 34 removed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime status. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially, one reviewer at a time, all on fix 1, in this order: correctness, consistency, comprehensibility.
No recheck raised a new finding, so no second fix was needed.

Each reviewer appended to its own report file, which stayed in its session context. Each recheck brief gave the reviewer:
- the fix commit, the reviewed candidate as the base, and the read-only rules;
- the actual content diff `bebdf80..199a694`;
- the coordinator's evidence for every change and the declined items, stated without the other reviewers' reports;
- the reviewer's original verdicts and the disposition of each of its own findings and optional items. The
  comprehensibility brief stated why 騒々しい leads with «шумный» rather than «крикливый», why the alternative wordings
  for 高等 and 飽くまで were used, and why Q1 and the 一流 suggestion were not adopted.

The three briefs were delivered as session files that the reviewers were told to read in full.

All recheck messages forbade running `tools/build_manifest.py` or any other generator. Every recheck section states that
none was run. The correctness and consistency reviewers each ran `tools/validate.py` (0 errors each); the
comprehensibility reviewer did not run it. Each recheck section records HEAD `199a694` with a clean tree (the
correctness reviewer before its recheck and after validation).

### Round 1 (`199a694`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer checked every changed passage in the 14-card diff against `bebdf80`, rereading the surrounding text. C1–C5 are **resolved**: both noise titles use the general environmental-noise gloss; raising a hand and frightening are restored; cutting and sewing replace the overbroad craft label, matching Daijisen without imposing hand-sewing; the канго classification is collection-local and no longer asserts Chinese origin; 固める has its reading. The 飾り and 高等 optional items are **resolved** by adoption. No regression: 高層 keeps the building/atmosphere distinction, 高級 keeps broad high quality beside luxury, the 飽くまで and 挿す lessons survive the removal of the English glosses, and 刺す keeps sewing distinct from stinging. Spelling evidence: public JMdict XML entries 1306470 and 1535790 still mark 螫す and 餠 search-only; the learner-facing rarity wording is supported by the JMdictIssues #126 tag explanation and Daijisen. Validator 0 errors. Correctness and scoped coverage are **CLEAN**. |
| Consistency | Snapshot `199a694` with a clean tree. The diff touches only the 14 word cards, `manifest.json` and the intake; no navigation file changed. The three new entries are well-formed, their targets exist, there are no duplicates and no reverse YAML; 挙げる has 11 entries and 高層 4; the RU-added total is 7, and all EN exclusions are retained. H1 equals the title on all 14 changed cards. The title-pool screen finds no unguarded exact overlap among the changed titles (騒がしい/騒々しい with うるさい, 驚かす with おどかす, 飾り with アクセサリー/飾る, 高層 with 高度, 挙げる with 立てる/上がる all guarded). Links are unchanged; navigation stays 5 files and 8 links, and the only RU-only link is still 強化→固まる. The intake's 35 hashes equal the manifest and the committed files. The 激増 «резк-» optional item is **closed** and the 刺す line-44 wording **resolved**. Consistency, quiz safety and scoped coverage are **CLEAN**. |
| Comprehensibility | The reviewer read the changed passages. C1–C9 are **resolved**, accepting the alternative wordings for C3, C4 and C7 and no longer maintaining «крикливый»: «шумный; беспокойный (об обстановке)» is the card's own wording and covers nonhuman noise, and the shared lead with うるさい is excluded. Q1 is **withdrawn** (agreed). The 騒がしい, 裁縫, 刺す:32 and 高層:21 optional items are resolved by adoption; the 一流 suggestion is not maintained; 馴れる and «атэдзи» remain optional, not elevated. No regression, including 挙げる's other taught senses, 驚かす's distinction from おどかす, the канго rewrite, 裁縫's cutting step, 刺す's sewing sentence and 強化's reading. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 騒がしい «шумливый» and 騒々しい «галдящий» narrow general noisiness (minor) | **Resolved** | `騒がしい.md:4,12`, `騒々しい.md:4,12`; Kuznetsov шумливый, галдеть; JMdict 1403000 and 1596440; Digital Daijisen 騒騒しい. |
| Correctness C2: 挙げる and 驚かす titles omit "raise" and "frighten" (minor, coverage) | **Resolved** | `挙げる.md:4,12`, `驚かす.md:4,12`; JMdict 2864818 senses 9 and 1; 1238650 sense 1. |
| Correctness C3: 裁縫 «рукоделие» too broad (minor) | **Resolved** (alternative wording) | `裁縫.md:4,12,16`; Daijisen 裁縫; JMdict 1296200; Kuznetsov рукоделие. |
| Correctness C4: 騒々しい канго defined by Chinese origin (minor) | **Resolved** (adapted wording) | `騒々しい.md:32,34`; Seisenban on Kotobank. |
| Correctness C5: 強化 lacks the reading of 固める (minor, coverage) | **Resolved** | `強化.md:35`; JMdict 1266570. |
| Correctness optional: 飾り «орнамент»; 高等 «высокого порядка» | **Optional, adopted** | Through comprehensibility C2 and C4; `飾り.md:4,12,16`, `高等.md:4,12`. |
| Consistency optional: 激増 «резк-» against the previous batch | **No action needed**; closed by the reviewer at recheck | The only «резк-» titles are きつい, ぎらぎら, 屑, 急に, 急激 and 激増; 激増→急激 is guarded. |
| Consistency optional: 刺す:44 reads awkwardly | **Optional, adopted** | `刺す.md:44`; frozen EN "not merely another way to say that an insect bites it". |
| Comprehensibility C1: 高層 «многоэтажный» (moderate) | **Resolved** | `高層.md:4,12,17`; Digital Daijisen 高層; guard 高層→高度. |
| Comprehensibility C2: 飾り «орнамент» (moderate) | **Resolved** | `飾り.md:4,12,16`; Gramota орнамент. |
| Comprehensibility C3: 騒々しい «галдящий» (moderate) | **Resolved** (alternative wording; «крикливый» not maintained) | `騒々しい.md:4,12`; Digital Daijisen 騒騒しい; うるさい guarded on both cards. |
| Comprehensibility C4: 高等 «высокого порядка» (minor) | **Resolved** (alternative wording) | `高等.md:4,12,16`. |
| Comprehensibility C5: 高級 «элитный» (minor) | **Resolved** | `高級.md:4,12,16`; MAS элитный. |
| Comprehensibility C6: 飽くまで English "after all" (minor) | **Resolved** | `飽くまで.md:41–42`. |
| Comprehensibility C7: 飽くまで «из исходного списка» (minor) | **Resolved** (alternative wording) | `飽くまで.md:23`. |
| Comprehensibility C8: 挿す English "graft" (minor) | **Resolved** | `挿す.md:23`; JMdict 1399830 sense 2. |
| Comprehensibility C9: 餅 project jargon (minor) | **Resolved** | `餅.md:29`; JMdict 1535790 (search-only 餠); JMdictIssues #126. |
| Comprehensibility Q1: a reverse ビル–高層 exclusion | **Withdrawn** by the reviewer at recheck | 高層 declares ビル, and Android applies declarations in both directions; after C1 the titles share no stem. |
| Comprehensibility optional: 騒がしい, 裁縫, 刺す:32, 高層:21 | **Optional, adopted** | Through correctness C1 and C3; `刺す.md:32` (JMdict 1306470; JMdictIssues #126); `高層.md:21`. |
| Comprehensibility optional: 一流 «один из лучших» | **Optional, not adopted**; not maintained at recheck | «ведущий» would collide exactly with アナウンサー «диктор; ведущий»; the nuance section rejects race placement, not membership among the best; the correctness reviewer established no defect. |
| Comprehensibility optional: 馴れる «приручаться», «атэдзи» unglossed | **Optional, not adopted**; kept optional at recheck | 馴れる's second gloss «становиться ручным» and the body make the animal the subject (Kuznetsov приручиться sense 1); «атэдзи» is the deck's established term. |
| Consistency limit: raw-byte hash mismatch on 118 `strokes/*.json` manifest entries | **Withdrawn** as a defect; pre-existing and outside the batch | `tools/build_manifest.py` hashes text files after CRLF→LF normalization. All 718 `strokes/` entries at `199a694` match the normalized hash; exactly those 118 files contain CRLF, and they are byte copies of EN blobs kept by `.gitattributes` (`strokes/*.json -text`). The batch touches no `strokes/` file. |
| Exclusion classification | **Author's and reviewer's classification agree** | All four candidate entries are conservative (table in review 001). The fix entries 挙げる→上がる, 挙げる→立てる and 高層→高度 are conservative, as the dispositions and the fix commit have them; the reviewer confirmed them and the total of 7 at recheck but did not restate a required/conservative split. |

Cross-batch note: links to absent targets stay plain. Seven EN link targets in this batch's new cards are absent from RU:
the kanji cards 層 (from 高層), 片 (from 片付く) and 香 (from 香水), and the word cards 揚げる (from 挙げる), 増減 (from
増大), 生け花 (from 挿す) and 刺さる (from 刺す). Kanji 刺's three EN links to 刺さる also stay plain. EN has kanji cards for
層, 片 and 香; the other 18 written kanji without an RU kanji card have none in EN either.

## Final exclusion set

All 157 EN exclusion entries (28 lists) are retained in EN order. Seven direct, one-sided entries are added on six new
cards (no new list):

- Required (0).
- Conservative (7): 激増→急激, 驚かす→驚く, 飢饉→飢える, 高める→上がる and, added in fix 1, 挙げる→上がる and 立てる and
  高層→高度.

On 挙げる and 高める, 上がる is inserted after EN's first entry 上げる; nothing is removed or reordered. Android applies
each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after the fix (騒がしい, 騒々しい, 裁縫); both optional items adopted.
- Scoped coverage: **CLEAN** after the fix (挙げる, 驚かす, 強化).
- Comprehensibility: **CLEAN** after the fix (高層, 飾り, 騒々しい, 高等, 高級, 飽くまで, 挿す, 餅); 馴れる and «атэдзи» remain
  optional.
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN**, including the three fix-1 entries. This covers the reviewed batch and the directly adjudicated
  pairs. Exclusions are direct pairs, not transitive groups.

## Limits

- The rechecks reread only the changed passages and the lines needed to judge them. The unchanged cards rest on review
  001, in which all three reviewers read all 30 cards in full against EN.
- The comprehensibility reviewer did not re-fetch dictionaries or run the validator at recheck. The consistency
  reviewer's recheck manifest comparison covered the 35 intake paths; its full `kanji/`, `words/` and `articles/` match
  was at `bebdf80`.
- The consistency reviewer's dictionary senses came from the cards' citations and general JMdict knowledge, not fresh
  lookups; its necessity classes are judgements, not measurements.
- The live JMdictDB entry 1518320 was password-gated for the comprehensibility reviewer; C6 did not depend on it.
- Online dictionaries were current observations, not pinned archives. The app's quiz selection was not inspected.
- No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.

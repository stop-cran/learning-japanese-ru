# Batch 257 / word batch 96 — consistency review

## Snapshot

READ-ONLY RU candidate `bd3cb7293fa63d0b8ad59692524d561e2df91678`, tree `8b50554614afa6e0e4d5f91895425ced03b43387`, parent `8ddfa6793f162d6e896a91417d81b77c511df39e`; frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

RU root: `C:\Users\romanko\repos\copilot-worktrees\learning-japanese-ru\romanko-microsoft-sturdy-doodle`; EN root: `C:\Users\romanko\repos\learning-japanese-en-frozen`. Comparisons used exact Git objects. Inventory SHA-256 matched `d6a27d79c3a7ff1a5a6a1bc17375b575372701628f42734d7f3ac24b52d1078d`. No edits; final working-tree status clean. Runtime model identity unavailable.

## Scope and actual reads

**30 new translations + existing 汗 correction**, not 31 new cards. Every paired card was read completely, including examples, explanations, comparisons and citations. Each number below is the inclusive endpoint of a read starting at line 1, **RU/EN**, under `words/`:

有料 41/46; 月給 40/40; 下旬 39/39; 月末 40/40; 書道 42/48; 書籍 45/58; 更ける 42/52; 曲線 37/33; 捩る 48/54; 工夫 36/37; 捻る 46/54; 曲げる 38/40; 曖昧 37/41; 普及 43/52; 昼寝 43/52; 映す 41/44; 写る 44/46; 映る 47/48; 明け方 40/42; 早口 41/49; 日陰 41/46; 日課 40/47; 日時 43/48; 日程 44/51; 日用品 41/45; 光線 40/46; 日差し 44/54; 日当たり 41/50; 日帰り 44/49; 日の出 42/46; 汗 34/34.

Read all five complete navigation diffs: `kanji/方.md`, `kanji/明.md`, `words/カーブ.md`, `words/写す.md`, `words/直線.md` — six link insertions. Separately read the complete 汗 before/after diff.

Evidence coverage:

- All 31 dictionary packets and all 31 metadata/related-title packets; complete 4363-word metadata pool; all 417 heuristic-screen lines, supplemented by independent semantic searches.
- All three neutral supplemental locator files; all 17 cited secondary dictionary families: 上旬, 中旬, 習字, 字, 筆, 本, 書物, 図書, 冊子, 出版, 刊行, 発行, 工夫こうふ, 居眠り, 写す, 映る, 光. All 30 primary N2 families were compared with frozen EN JSON objects: no differences. Frozen vocabulary rows confirmed 30 N2 mappings and 汗 N3:22.
- Complete additional RU comparisons: 絞る 1–52; 帰り 1–53; 仕方 1–53; 物 1–41; 品物 1–50; 芸術 1–46; ぺらぺら 1–39; 夢 1–46; うとうと 1–33; 向ける 1–56; 案 1–43. Complete frozen EN 夢, 仕方, 掻く and 拭く articles also read.
- Original Agency for Cultural Affairs PDF entry 025 and full footnote; PDF hash matched the locator. Relevant original dictionary definition blocks read for 書道, 習字, 更ける, 昼寝, 早口, 日陰, 日程, 日差し, 日当たり, 日帰り, 日の出, 普及, 有料, 捻る, 工夫, 仕方, 夢, 明け方, 汗をかく and 拭く. These were definition-section reads, not entire-site reads.

No paired-card read was truncated. Oversized policy/comparison outputs and an encoding failure were recovered with bounded reads/UTF-8 execution; failed HTML extraction was recovered with the standard-library parser. Only relevant sections of the broader content-structure instruction were read. No author rationale, other reviewer report or execution log was consulted.

## Verdicts

- **Consistency / quiz integration: NEEDS FIX.** Two direct ambiguity gaps below survive the declared pool checks.
- **Correctness within this facet:** no confirmed Japanese identity/reading defect; the 汗 correction and 写る/映る/映す distinction are supported. Quiz-answer correctness is not cleared.
- **Assigned coverage / dependencies: PASS structurally.** All assigned cards and navigation changes covered; no missing required target found. Not semantic clearance of every repository article.
- **Russian comprehensibility within this facet: NEEDS FIX for answer labels.** Finding 1 concerns Russian polysemy; finding 2 an inadequately excluded valid sense. No general prose-comprehensibility clearance is claimed.

Actual checks:

- C1-confirmed `python -X utf8 -B tools\validate.py`: exit 0, **0 error(s)**. Structural evidence only.
- Read-only Git/Python comparisons: all 62 paired sides matched frozen blobs; all 4363 pool records matched candidate metadata; 4363 distinct IDs; no exact-title collision involving assigned cards.
- Identity fields, community JLPT mappings, types, written kanji and source tags retained. No missing written character was concealed by an unavailable kanji article.
- 142 relative Markdown links resolved; 136 unique related-word records matched pool metadata. All required exclusion IDs existed; no source exclusions/distractors removed. Assigned cards declare 125 exclusion entries and no curated distractors.
- Three added direct guards retained: 捻る–思い付く, 日の出–昇る, 明け方–夜明け. No transitive closure assumed.
- Manifest entry hashes and recomputed contentVersion `8280df1bcb5f9963` matched; generator not run.
- Navigation targets/readings matched, including the actual linked 明け方 example under `## Чтения` at `kanji/方.md:36`.

## Findings

### 1. Medium — Russian “сон” remains an admissible distractor for 昼寝

**Locations:** `words/昼寝.md:4,9,16`; `words/夢.md:4,9,15–16`.

The new card displays **«дневной сон; сиеста»**. Existing 夢 displays **«сон; мечта»**, with no exclusions; 昼寝 excludes 居眠り/寝る/眠る/睡眠 but not 夢. Russian «сон» can denote sleeping, so the 夢 label is not unambiguously wrong for a bare 昼寝 meaning question. The answer-side explanation that 夢 means a dream cannot disambiguate the choice beforehand.

**Consequence:** the unrestricted metadata pool permits a misleading answer set despite different exact titles. This is a RU-specific interaction with an existing ambiguous label, not a claim that Japanese 昼寝 and 夢 are synonyms; frozen EN 夢 says “dream”.

**Correction:** add only the direct 昼寝–夢 exclusion, preferably on the in-scope 昼寝 card. Alternatively, separately authorize changing the existing 夢 title to «сновидение; мечта» and recheck it. Do not expand a sleep-word clique.

**Evidence:** archived JMdict 1426370 defines daytime sleep; frozen EN 夢 cites 1529410, senses 1–2. Independently, [Daijisen 昼寝](https://www.weblio.jp/content/昼寝) defines sleeping during daytime; [Daijisen 夢](https://www.weblio.jp/content/夢), ゆめ senses 1–2, defines dream imagery and aspiration. Candidate labels and both exclusion endpoints checked directly. **Confidence: high.**

### 2. Medium — 工夫’s resulting-method sense is not guarded against 仕方

**Locations:** `words/工夫.md:4,9,16–19`; `words/仕方.md:4,9,16`.

工夫 includes devising a useful way and its practical result. Existing 仕方 displays **«способ; приём»**. Neither endpoint excludes the other. For bare 工夫, that alternative label can describe a supported noun sense; the narrower official title **«изобретательность; придумывание способа»** does not remove other valid meanings from the Japanese prompt.

**Consequence:** an allowed distractor need not be wrong. The missing pair is inherited from source declarations but remains material in this candidate. This is not a demand to add a new teaching sense.

**Correction:** add only the direct 工夫–仕方 guard on 工夫. Do not infer further guards through 方法, 手段, 方 or other neighbors.

**Evidence:** primary JMdict 1278220 and the card’s own result explanation; frozen EN 仕方 cites 1594110 sense 1. Crucially, [Daijisen 工夫](https://www.weblio.jp/content/工夫), くふう sense 1, explicitly includes the resulting method/means; [Daijisen 仕方](https://www.weblio.jp/content/仕方), sense 1, defines a way of doing something. Direct sense evidence, not transitive reasoning. **Confidence: high.**

Read-only data witnesses:

- 工夫 / 仕方 / 有料 / 日陰
- 昼寝 / 夢 / 有料 / 曲線

Each quartet has four distinct actual Russian labels and zero forbidden direct pairs. These demonstrate admissibility under supplied metadata rules, **not observed runtime sampling or grading**. Reverse-direction labels were also considered; one ambiguous direction already warrants a symmetric direct guard.

## Optional

- `words/明け方.md:4,12` uses «предрассветное время», whereas navigation says «рассвет» / «время около рассвета». Harmonizing toward «время около рассвета» would reduce friction, but the dictionary supports approaching dawn; not a confirmed mistranslation.
- Missing optional kanji articles: 及, 捩, 捻, 旬, 昧, 普, 曖, 汗, 籍, 線, 課, 陰. Unavailable ねじ and 日の入り links became plain text. No requirement to add these out-of-scope articles was found.
- 光線 retains the inherited 桁 exclusion although Russian labels no longer share the English “beam” ambiguity. Conservative overrestriction, not grounds to remove a source guard or weaken the pool.

## Limits

No full unit/smoke suite, client quiz playback, device/media/voice or activation test ran. Actual randomized option counts and level-filter behavior remain **UNVERIFIED** without consuming-client/mode execution. No scene/media change was assigned; unchanged assets received no new semantic approval.

All assigned learner-facing bodies were read. The full word pool received metadata checks and targeted article comparisons, not an independent semantic rereview of every body; globally exhaustive semantic exclusion coverage is not claimed. The N3 汗 row proves noun mapping only; the corrected sweating/wiping distinction was checked separately against verb evidence. Structural success does not override the findings.

Original review complete; no changes made. Available for a bounded recheck.
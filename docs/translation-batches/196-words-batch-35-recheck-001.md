# Batch 196 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `dd399249fe65eeba0cef005a3655cc3bc1ab874f` | `2585cf658a0f2479ce3fae46abb0b9c5ba55ea23` | Initial review snapshot: the signed candidate, pushed before review. |
| `14a5f4c68156d202d3d5fd0b624a43d7e169ca3d` | `95bfdd1691a605b88557e4f63a2634ab5124b74d` | Final candidate: review fixes (`2cad28d`) plus the intake refresh. |

The final candidate changes eight word files:
- `綿`: line 19 restores the frozen EN reading gloss （このしゃつはめんでできています。）. A new unlinked contrast says 木綿（もめん）
  «хлопок (материал)» is another word for cotton as a material with its own reading, and that 綿 in the examples is read めん or わた.
- `老人`: `quiz_exclusions: [おじいさん, おばあさん]` is added. A new unlinked paragraph says おじいさん «дедушка; пожилой мужчина» and
  おばあさん «бабушка; пожилая женщина» specify sex and can denote kinship, while 老人 names an age group with neither.
- `能`: the title, heading, body, example and synonym line use «театр Но», and the body adds «здесь «Но» — название театра».
  A new sentence points to 音楽の才能がある from the 才能 card for talent in a field, rather than substituting 能 mechanically.
- `能力`: the 才能 contrast says «подчёркивает талант, одарённость» instead of «природную одарённость», matching frozen EN
  "talent or aptitude".
- `考慮`: a new unlinked sentence separates 尊重（そんちょう）, respect for an opinion or right（意見を尊重する）, from weighing a factor
  such as cost or weather（費用を考慮する）.
- `絶対`: a new unlinked sentence gives ぜひ's typical role of strengthening a request, invitation or desire（ぜひ来てください）
  and says the shared «обязательно» does not make the two words interchangeable.
- `羽`: «ханэцуки» becomes «для игры в ханэцуки» in the example translation and the note. The source-row, compiler-intention
  and N3 sentences become a learner-facing note: some word lists wrongly pair はね with a counter gloss; the card follows the
  verified «перо; крыло»; the counter is a comparison only.
- `皮`: the note no longer refers to an unseen source list. It says some word lists also give «выделанная кожа» and that the
  dictionary separates processed leather into 革.
- The manifest and intake are regenerated. `contentVersion` is `d8d220dd00cf6fed`, and only the eight changed word hashes differ.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks used the same model variants and facets as review 001, run as fresh agents rather than the original agent sessions:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

Rechecks ran serially.
Each reviewer received only:
- its facet's original blind report;
- the coordinator's dispositions of its findings;
- the revised snapshot;
- the actual diff `dd39924..14a5f4c`.

The coordinator's recheck prompts misstated the number of changed word files as nine. The actual diff changes eight word files,
the manifest and the intake. All three reviewers worked from the actual diff; correctness and comprehensibility noted the mismatch,
and consistency recomputed hashes for the eight changed files. No ninth file was changed or omitted from review.

HEAD and the working tree were unchanged after every recheck.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | `14a5f4c` | F1 resolved: `綿.md:19` exactly restores frozen EN's kana reading. The reviewer checked every changed passage against frozen EN and the existing RU 才能, 尊重 and ぜひ cards. It inspected Jisho/JMdict entries for 木綿, おじいさん, おばあさん, 是非, 尊重, 羽, 皮 and 革, デジタル大辞泉 是非 adverb senses 1–2 on kotobank, and the Polivanov table (ханэцуки). «Типичная роль» qualifies ぜひ without excluding commitments such as ぜひ伺います; 老人's «без родства» describes what the word encodes rather than banning its use of a relative. No EN sense or restriction was lost. Correctness and scoped coverage are **CLEAN**. |
| Consistency | `14a5f4c` | F1 resolved: `老人.md:9` declares both guards; both target cards exist. The reviewer ran the validator (0 errors), recomputed the eight changed manifest hashes and found no RU-only relative link in added lines (the only link touched is EN's existing 才能 link in 能力). The 能 title change is capitalisation only and collides with no other title. The optional items are withdrawn or unchanged; 考え→考える remains a harmless conservative pair. Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | `14a5f4c` | C1–C9 resolved. 能力 no longer teaches that 才能 is innate, and 能 points to a concrete 才能 construction. «Но» no longer reads as the conjunction. The 木綿, 尊重, ぜひ and おじいさん/おばあさん contrasts are self-contained without links. The 羽 and 皮 notes now state a learner operation instead of exposing author provenance, and line 25's 羽根つき（はねつき） makes «ханэцуки» identifiable. Optional items unchanged. No regression. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1: 綿 changed EN's kana reading gloss | **Resolved** | `綿.md:19`. A source-preservation fix; the pronunciation was never wrong. |
| Consistency F1: 老人 overlaps おじいさん/おばあさん | **Resolved with guards and a contrast** | `老人.md:9,32–33`. Two direct, one-sided pairs, applied symmetrically by the app. The author had declined this pair before review; RU-added exclusions now total 15. |
| Consistency optional: 考え vs 計画/案 | **Optional, withdrawn on recheck** | The titles do not collide. |
| Consistency optional: 絶対 vs 決して | **Optional, unchanged** | No guard added; the new ぜひ contrast is plain text. |
| Consistency optional: 肌 vs 革 | **Optional, no guard needed** | The displayed qualifiers «(тела)» and «выделанная» disambiguate; 肌 guards 皮 through EN and 皮 guards 革. |
| Consistency classification: 考え→考える unjustified but harmless | **Kept as conservative** | Noun→verb precedent (B192 読書→読む). Not actionable for either side; see the independent-review table. |
| Comprehensibility C1: 才能 described as innate; 能/才能 circular | **Resolved** | `能力.md:34`, `能.md:37–38`. Worded by fidelity to frozen EN "talent or aptitude" and agreement with `才能.md`, which does not settle innate versus practised ability. The correctness reviewer's dictionary evidence for 生まれつき glosses is preserved in its report; the card makes no claim either way. |
| Comprehensibility C2: «театр но» reads as a conjunction | **Resolved** | `能.md` title, heading, body, example and synonym line. Capitalised as a name, with a clarifying clause. |
| Comprehensibility C3: 綿 lacks a 木綿 contrast | **Resolved, unlinked** | `綿.md:40–41`. EN 綿 has no 木綿 link, so RU adds none. |
| Comprehensibility C4: 考慮 lacks a 尊重 contrast | **Resolved, unlinked** | `考慮.md:36–37`. |
| Comprehensibility C5: 絶対 and ぜひ share «обязательно» | **Resolved, unlinked** | `絶対.md:39–40`. Qualified as ぜひ's typical role; no claim that ぜひ cannot accompany a commitment. |
| Comprehensibility C6: 老人 lacks an おじいさん/おばあさん contrast | **Resolved** | Same change as consistency F1. No register or rudeness claim was added. |
| Comprehensibility C7: 羽 keeps author-facing notes | **Resolved by rewording** | `羽.md:47–49`. The EN substance (incompatible counter gloss, verified meaning, comparison-only counter) is kept in learner wording. |
| Comprehensibility C8: bare «ханэцуки» | **Resolved** | `羽.md:28,51`. Polivanov form kept and given context. |
| Comprehensibility C9: 皮 refers to an unseen source list | **Resolved by rewording** | `皮.md:40–41`. The EN statement that leather belongs to 革 is kept. |
| Comprehensibility optional items (保存/維持, 結ぶ/繋ぐ, 繰り返す/復習, 給料, 考え/意思, 缶, 能く) | **Optional, unchanged** | Confirmed as polish on recheck. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN** after fixes.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** after fixes, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.

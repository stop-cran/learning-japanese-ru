# Batch 191 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `20834c891a290fd011cbc3ce5b4940d5d1f5f5be` | `09404a2d88294118352e760242feb2a6ff59de3e` | Initial review snapshot: a local unsigned commit that was never pushed. |
| `3109d3d20ad14c3bd1453458a5e20133a3172b87` | `09404a2d88294118352e760242feb2a6ff59de3e` | The same tree, committed signed with the same parent once signing recovered. It is the first batch commit in the published history. |
| `fde4dcd5608340551ccfae98374454979a0e5b37` | `7faab8ecc2e13c9035fc2e55ca1d16a63626a7bc` | Final candidate. |

The final candidate makes these changes:
- `越す`: the English "go over" remark is deleted, and 過ぎる is guarded.
- `販売`: the «распродажа» warning is restated without English.
- `貢献`: the English "services" aside is deleted.
- `負け`: the first gloss is non-past, and the unsourced 敗北 register claim is removed.
- `働き`: an unlinked 労働 contrast is added.
- `貴重`: 高価 is guarded.
- The manifest and intake are regenerated.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks used the same assigned model variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

Rechecks ran serially, and each reviewer verified that `20834c8` and `3109d3d` have the same tree.
Each reviewer received only:
- its own original findings;
- the coordinator's dispositions of them;
- the revised snapshot;
- the actual diff `3109d3d..fde4dcd`.

HEAD and the working tree were unchanged after every recheck.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | `fde4dcd` | C191-1 resolved. The new 労働（ろうどう）«труд» and 労働時間（ろうどうじかん）«рабочее время» glosses were checked against freshly read Jisho/JMdict entries. No changed passage lost an EN teaching point, and there was no regression. Correctness and scoped coverage are **CLEAN**. |
| Consistency | `fde4dcd` | F1 and F2 resolved. Optional 渡す and おかげ items withdrawn. The new guards are one-sided. 働き–労働 was already guarded, and link parity holds with 労働 unlinked. The six changed manifest hashes match, and the validator reports 0 errors. Consistency, quiz safety and cross-file integration are **CLEAN**. |
| Comprehensibility | `fde4dcd` | C1–C5 resolved. The optional items remain optional. No changed passage regressed. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C191-1: 敗北 «звучит книжнее» | **Resolved** | `負け.md:34–35` now says only that 敗北（はいぼく）also means «поражение» and keeps 試合で敗北した, matching frozen EN. |
| Consistency F1: 越す lacks 過ぎる | **Resolved** | `越す.md:9` is `[越える, 渡る, 過ぎる, 引っ越す, 移る]`. |
| Consistency F2: 貴重 lacks 高価 | **Resolved** | `貴重.md:9` is `[大切, 大事, 高価]`. Nothing in the body equates value with price. |
| Comprehensibility C1: 越す English "go over" remark | **Resolved** | The three sentences are deleted. «年を越す означает переход в новый год…» remains. |
| Comprehensibility C2: 販売 English "sale" | **Resolved with modification** | `販売.md:40–42`: «Не принимайте 販売 за «распродажу»: 販売 в магазине может идти по обычной цене…». The marketing distinction is kept. |
| Comprehensibility C3: 貢献 English "services" | **Resolved** | The sentence is deleted. The «вклад» explanation and the participation contrast remain. |
| Comprehensibility C4: 負け past-tense gloss | **Resolved** | `負け.md:20`: «На этот раз это мой проигрыш.», which agrees with the noun-versus-verb note. |
| Comprehensibility C5: no 働き–労働 contrast | **Resolved with modification** | `働き.md:35–37` contrasts 労働 «труд» (労働時間 «рабочее время») with the person's or organ's work shown in this card's examples. The proposed «часто условия и время труда» claim was not adopted because it was unsourced. 労働 stays unlinked for EN link parity. |
| Consistency optional: 渡す guards on 与える/贈る | **Withdrawn** | No shared title word, and necessity was not established. |
| Consistency optional: 恩–おかげ | **Withdrawn** | Loose stem overlap only. |
| Comprehensibility optional: 資本:41 and 与える:17 wording | **Optional, declined** | Faithful renderings of frozen EN `資本.md:38–40` and `与える.md:17`. |
| Comprehensibility optional: 賢い→利口 back-pointer; 質 «характер вещи» | **Optional, declined** | The examples already disambiguate. 利口 already contrasts お利口, and 質–性格 is guarded. |
| Comprehensibility optional: 係 «ведение» → «поручение» | **Optional, declined** | «поручение» is an exact title segment of 依頼 «просьба; поручение» and 用事 «дело; поручение». Adopting it would create a new quiz overlap, so the author retitled away from it. «ведение» is attested in Warodai and Jardic for かかり. |
| Comprehensibility optional: 越す honorific sense 6 | **Optional, declined** | Frozen EN stops at senses 1–5, so this would be expansion. |
| Comprehensibility limit: 役→係 and 働き→労働 are declared on one side only | **No finding** | Exclusions are one-sided direct declarations, and Android applies each one symmetrically. Reverse declarations are not added on baseline cards. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN**.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.

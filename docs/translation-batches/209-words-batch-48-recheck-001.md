# Batch 209 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `5f015601f1ff714f7c63b0edfa85215c8f99f071` | `b7775854199e6bd437d9ef17989cc2a7a45ae79a` | Initial review snapshot: the signed candidate, pushed before review. |
| `5c78e529f27e1e7072051b1fad195ab853a05496` | `bf2044299cda216d6693dc85bbabca937d9ebdf8` | Fix 1 (final candidate): one review finding and two adopted optional notes plus the intake refresh, committed signed and pushed before the rechecks. |

Fix 1 changed three word files and regenerated `manifest.json` (`contentVersion` `a305b1c19c4c1d26`, 4,384 entries) and the
intake:
- `得意` (line 19): 得意な科目は数学です is rendered «Предмет, который мне хорошо даётся, — математика.» instead of «Лучше
  всего мне даётся математика.» (comprehensibility C1).
- `引っ張る` (line 18): ロープを強く引っ張ってください is rendered «Пожалуйста, сильно тяните верёвку.» instead of «Пожалуйста,
  тяните верёвку сильнее.» (comprehensibility optional note; EN "Please pull the rope hard.").
- `年齢` (line 19): この講座は年齢に関係なく参加できます is rendered «В этом курсе можно участвовать независимо от возраста.»
  instead of «На этот курс можно записаться независимо от возраста.» (comprehensibility optional note; EN "You can join
  this course regardless of age.").

Net change from the candidate: three learner glosses. No title, Japanese example, reading, internal link or quiz exclusion
changed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer reread its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially. Each reviewer appended to its own report file, which stayed in its session context, and each
recheck message gave it only:
- the revised snapshot, its parent and the read-only rules;
- the actual content diff (`git diff 5f01560 5c78e52 -- words`);
- the coordinator's evidence for each change (no superlative in the Japanese and EN "My strong subject is mathematics."; 強く
  as an adverb, not a comparative; 参加できます as participation);
- a summary of its own findings and optional notes, with the coordinator's disposition of each, without the other reviewers'
  reports.

The shared opening of the messages said that the edits came from the comprehensibility reviewer's findings. One came from
its finding and two from its optional notes, and the comprehensibility reviewer's own message referred to its report in the
third person. Each message showed the full diff and the evidence for every change, so the scope of the rechecks was
unaffected.

The recheck prompts forbade running `tools/build_manifest.py` or any other generator; all three recheck sections state that
none was run. The correctness and consistency reviewers ran `tools/validate.py` (0 errors); the comprehensibility reviewer
does not report running it. After every recheck the coordinator confirmed that HEAD was unchanged and that
`git status --porcelain --ignored` was empty.

### Round 1 (`5c78e52`)

| Facet | Scope and result |
|---|---|
| Correctness | The reviewer inspected the complete words diff and both-language lines 14–23 of the three changed cards. 得意 no longer has an unsupported superlative; 引っ張る renders 強く without adding a comparative; 年齢 keeps 参加できます as possible participation rather than registration. Experiencer, polarity, register and the polite request are preserved, and all Japanese sentences and kana lines are unchanged. The reviewer noted that its original CLEAN verdict missed these three localized fidelity issues and accepted the fixes on their Japanese and EN evidence. `tools/validate.py` reported 0 errors. Correctness and scoped coverage are **CLEAN**. |
| Consistency | The reviewer confirmed that the fix touches five files (three cards, the manifest and the intake) and that no title, link or exclusion changed, so there is no new title overlap. All 4,384 manifest entries match the sha256 of the file text after CRLF→LF normalization, which confirmed the coordinator's explanation; the reviewer withdrew its 118-strokes limit as a raw-hash artifact. Every changed path and hash is present among the intake's 50 payload paths, checked by substring match rather than field by field. It kept the declined optional guards optional and accepted the decline. `tools/validate.py` reported 0 errors. Consistency, quiz safety and scoped coverage are **CLEAN**. |
| Comprehensibility | C1 is resolved: the gloss matches the card's own «хорошо получается» and JMdict 1454510 sense 2 (forte, not best). The adopted 引っ張る and 年齢 notes are resolved; «участвовать в курсе» has the right government. The declined notes on 役割, 幼い and 従う stay optional, and the reviewer accepted the declines without new evidence; 床 stays adequate. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Comprehensibility C1: 得意 example adds a superlative | **Resolved** | `得意.md:19`; frozen EN `得意.md:20`; JMdict 1454510 sense 2. |
| Comprehensibility optional: 引っ張る «сильнее» is comparative | **Resolved** (adopted) | `引っ張る.md:18`; frozen EN `引っ張る.md:20`. |
| Comprehensibility optional: 年齢 «записаться» narrows participation to registration | **Resolved** (adopted) | `年齢.md:19`; frozen EN `年齢.md:19`. |
| Comprehensibility optional: 役割 adds «насоса» | **Optional, not adopted** | «выполняет роль насоса, перекачивающего кровь» keeps 役割を果たす «выполнять роль» with the same meaning; the suggested nominalisation is heavier. Reviewer accepted the decline. |
| Comprehensibility optional: 幼い title «малолетний» | **Optional, not adopted** | Kuznetsov «малолетний» gives the neutral childhood sense, verified by the correctness reviewer; the body renders each example naturally; a bare «маленький» would overlap 小さい/小さな. Reviewer accepted the decline. |
| Comprehensibility optional: 従う slash list mixes cases | **Optional, not adopted** | Each alternative is grammatical with «следовать»; «подчиняться» would drop the following sense taught by the card. Reviewer accepted the decline. |
| Comprehensibility observation: 床 separates floor from sex and storey | **No action** | Not a defect; 床→性 is guarded. |
| Consistency optional guards 引退↔辞める, 徹底↔丁寧, 心理↔精神, 得意↔自慢 and the weaker pairs | **Optional, not adopted** | EN declares none; the current titles share no exact segment, and the app deduplicates exact titles only. Reviewer accepted the decline. |
| Consistency limit: 118 strokes hash mismatches | **Withdrawn** by the reviewer | `tools/build_manifest.py` hashes text after CRLF→LF normalization; 118 of 718 strokes blobs contain CRLF. All 4,384 entries match. |
| Exclusion classification (author, coordinator and consistency reviewer) | **Agreed** | 得意→武器, 影響→左右, 床→性 required; 効果→有効, 影響→毒 conservative. |

## Final bounded verdicts

- Correctness: **CLEAN** throughout; the reviewer accepted the three fidelity fixes raised by the comprehensibility facet.
- Scoped coverage: **CLEAN** throughout.
- Comprehensibility: **CLEAN** after fixes (得意, with the adopted 引っ張る and 年齢 notes).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** throughout, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs,
  not transitive groups.

Limits: the rechecks reread only the changed passages and the cards needed to judge them; unchanged cards rest on review
001's full reading. No reviewer fetched new dictionary pages in the recheck; the consistency reviewer's JMdict senses for
the exclusion pairs remain from its own knowledge. No native-speaker, learner, app-import, device, media, activation or
release acceptance is claimed.

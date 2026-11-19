# Batch 195 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `4a2fd76f6380d7478317c486f1042215190a5934` | `02afdeec8bfbf21e076e959600ab7ed18980f642` | Initial review snapshot: the signed candidate, pushed before review. |
| `b44f566b00ec2c6b618fa98194e2cf33405f0d0b` | `bea0ec09ceee353b850896295fc1ef0cabdfa20c` | Final candidate. |

The final candidate makes these changes:
- `衣服`: the example translation is «Я сменил мокрую одежду.» instead of «Я переоделся из мокрой одежды.».
- `衣服`: a new sentence restores the Japanese number rule: «Даже когда речь идёт о многих вещах, 衣服 не требует японского окончания
  множественного числа.» The English-translation comparison is not reproduced.
- `虫歯`: `quiz_exclusions: [歯]` is added.
- `自慢`: a new unlinked paragraph in «Синонимы и антонимы» contrasts 誇り. It quotes the existing 誇り card's example
  このチームは町の誇りです «Эта команда — гордость города», says both words can name a source of pride, and qualifies that
  自慢 can name boasting to others while 誇り can concern an unspoken sense of dignity.
- The manifest and intake are regenerated. `contentVersion` is `eaaf5e0f833670c9`, and only the three changed word hashes differ.

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
- the actual diff `4a2fd76..b44f566`.

HEAD and the working tree were unchanged after every recheck.

| Facet | Snapshot | Scope and result |
|---|---|---|
| Correctness | `b44f566` | C1 resolved: the new 衣服 sentence preserves EN's rule that a plural translation needs no Japanese plural ending, without importing the English comparison or claiming Japanese has no plural expressions. «Я сменил мокрую одежду» conveys changing out of wet clothes (JMdict-backed 着替える). The 自慢/誇り paragraph is qualified by «могут»/«может», not a strict split, and matches the JMdict-backed 自慢 and 誇り senses (誇り also lists "boast") and the existing 誇り card. The quoted example matches that card apart from sentence-final punctuation. No EN sense, note or exclusion was lost, no RU-only link was added, and the three hashes match the manifest. Correctness and scoped coverage are **CLEAN**. |
| Consistency | `b44f566` | F1 resolved: `quiz_exclusions: [歯]` is valid front matter after `tags`; 歯's own `[年]` is unchanged and no reverse declaration was added. The declined 舌→言語 and 脇/隣 optional items and the kept 作家 plain-text pointer were accepted. The 自慢 paragraph has no link, quiz-behaviour statement or frequency wording. The reviewer recomputed the three manifest hashes and confirmed that only the three word files, the manifest and the intake changed. Consistency, quiz safety and scoped cross-file integration are **CLEAN**. |
| Comprehensibility | `b44f566` | C1 withdrawn: the 作家 pointer is a see-also, the rule is already on the card, and plain-text pointers to untranslated articles are the published restoration pattern; severity reassessed from minor to not actionable. C2 resolved: a beginner can now separate the shared «гордость» frame from 自慢's boasting behaviour without a strict split. The 衣服 optional item is resolved. «Пример с садом выше» and «пример с машиной» point to the card's only garden and car examples. No regression. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 衣服 dropped the plural-ending rule | **Resolved** | `衣服.md:48`. Worded as a standalone Japanese rule rather than the reviewer's «В этом употреблении…»; the reviewer accepted it on recheck. |
| Consistency F1: 虫歯 «кариозный зуб» overlaps 歯 «зуб; зубы» | **Resolved as a conservative guard** | `虫歯.md:9` is `[歯]`, the reviewer's first remedy. It follows this batch's hypernym guards 菓子→ケーキ/飴 and 衣服→洋服. The author had declined this pair before review. |
| Comprehensibility C1: 作家 points to an absent article | **Declined; withdrawn on recheck** | The pointer stays plain text so the link can be restored at the EN-linked position later, as in published 政治家, 武士, 研究員, いかがわしい, 奇しい, 妖しい and 疑わしい. Importing the article's examples would add content that EN's card lacks. The 作者/作家 rule is at `作家.md:36,43–47`. |
| Comprehensibility C2: 自慢 and 誇り share «гордость» without a distinction | **Accepted with a variant remedy; resolved** | `自慢.md:40–44`. The proposed [誇り] link was not added because EN 自慢 has none and RU must not add RU-only links. The frequency word «чаще» was dropped because the cited dictionaries do not establish it. The contrast example is the existing 誇り card's own. |
| Comprehensibility optional: 衣服 example calques "changed out of" | **Optional, accepted** | `衣服.md:22`: «Я сменил мокрую одежду.» (ぬれた = «мокрый»; the reviewer's «промокшую» was also acceptable). |
| Consistency optional: guard 舌–言語 | **Optional, declined** | The displayed parentheticals «язык (орган)» / «язык (как система)» disambiguate; EN has no such pair. The reviewer accepted this on recheck. |
| Consistency optional: 脇–隣 | **Optional, declined** | No guard needed; EN has none. The reviewer accepted this on recheck. |
| Consistency optional: 作家 plain-text pointer | **Optional, unchanged** | Same convention as comprehensibility C1; revisit when the article is translated. |
| Author/reviewer required-versus-conservative classification | **Preserved disagreement** | See the table in the independent-review record. Classification does not change runtime behaviour. |

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN** after fixes.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** after fixes, for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

No native-speaker, learner, app-import, device, media, activation or release acceptance is claimed.

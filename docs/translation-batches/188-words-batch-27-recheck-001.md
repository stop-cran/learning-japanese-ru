# Batch 188 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `c721e1cb63f33938081927e236dc7f9674f073b6` | `b355d4c7005159e48aa02d1ed71aec0b60529078` | Initial review snapshot. |
| `b8eaf4401c15156eca26dbdd113bc82973790524` | `916fa39d1d135795fc03de8319610b432699fa74` | Text fixes; `連続`→`次々` and `進歩`→`発展` guards; reverse entries on `次々` and `発展`. |
| `35ddea44130f54d4789ff42c55b0842f7318e007` | `b71665ba00f6a9a9ac1a60a8245a5573a41d30ea` | Reverse entry `幸せ`→`幸い`. |
| `d9c6b4f0224f67cc005369373d47b27a75824947` | `5a39dd36d3da0f4107ff472bda20e9603a3a0d35` | Removed the three reverse entries on baseline cards; intake back to 39 payloads. |
| `e1a7600f347424fa0ae13a97aeee7eb99eb53b41` | `7ed82c8d6d35aeed3ce92fe5a5d91215066ee713` | Final candidate: `幸い`→`幸福` and `進歩`→`発達` guards. |

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks used the same assigned model variants and facets as review 001: `gpt-6.1-sol` correctness, `claude-sonnet-5.5` consistency/quiz safety, `grok-4.7` comprehensibility. Model assignments are recorded from the task-runner runtime listing; reviewer prose did not expose separate serving IDs.

| Facet | Recheck | Snapshot | Scope and result |
|---|---|---|---|
| Correctness | 1 | `b8eaf44` | Bounded F1 recheck: resolved; correctness and coverage CLEAN for that scope. |
| Correctness | 2 | `d9c6b4f` | Full re-read of all 30 RU and EN cards: two missing direct guards, `幸い`–`幸福` and `進歩`–`発達`; coverage CLEAN. |
| Correctness | 2, follow-up | `e1a7600` | Both findings resolved; no regression; **CLEAN**. |
| Consistency | 1 | `b8eaf44` | Reconciled M1–M8 (below). |
| Consistency | 2 | `35ddea4` | `幸い`–`幸せ` judged justified; pass for the bounded scope. |
| Consistency | Reciprocal audit | `35ddea4` | Reviewed 32 listed one-way edges and two two-sided pairs; recommended reverse YAML for the 31 still one-way. That premise was withdrawn (below); its per-pair "retain" judgements stand. |
| Consistency | 3 | `d9c6b4f` | Confirmed `進歩`–`発達` (minor); called `幸い`–`幸福` supported but advisory (low); advisory-only pairs listed. |
| Consistency | 3, follow-up | `e1a7600` | Both resolved; no overguards, missing targets or hash mismatches; **CLEAN**. |
| Comprehensibility | Post-fix | `e1a7600` | All five original findings resolved; no regression in changed passages; comprehensibility and scoped coverage **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness F1, 毎週 «раз в неделю» | **Resolved** | `週間.md` now says «повторение каждую неделю». Both correctness rechecks verified this against JMdict ("every week") and Daijisen 「1週間ごと。週がかわるたび。」. |
| M1 / comprehensibility 1, identical `運`/`幸運` glosses | **Resolved** | `運` title and H1 are now «судьба; удача», matching the body's neutral 運が悪い use; `幸運` stays «удача; везение». The existing `幸運`→`運` and `運`→`幸い` guards remain. |
| M1, `運`–`幸せ` and `幸運`–`幸せ` | **Withdrawn / optional** | Consistency recheck 1 judged `運`–`幸せ` unsupported («судьба; удача» vs «счастье; счастливый»), and `幸運`–`幸せ` optional. Not added. |
| M1, `幸い`–`幸福` | **Resolved** after a preserved disagreement (below) | `幸い.md:9` declares `幸福` (`e1a7600`). |
| M2, `違いない`–`確か` | **Withdrawn** by the original reviewer | 確か is a な-adjective for reliable facts or a memory hedge, not the 〜に違いない construction; `違いない`→`きっと` and `確か`→`多分` cover the adverb overlap. |
| M3, `遅刻`–`遅れる` | **Withdrawn** by the original reviewer | The noun «опоздание» and the broader verb, which also covers train delays, differ; the card explains the distinction. |
| M4, `連想` vs `関連`/`関係`/`連絡` | **Withdrawn** by the original reviewer | Only the generic «связь» overlaps; the three other words already exclude one another. |
| M5, `連続`–`次々` | **Resolved** | `連続.md:9` declares `次々`, matching the body's «подряд» sense. |
| M5, `連続`–`連休` | **Withdrawn** | 連休 is the specific "several days off in a row". |
| M6, `進歩`–`発展` | **Resolved** | `進歩.md:9` declares `発展`. |
| M6, `伸びる` edges to `改善`/`進歩`/`上達` | **Optional, declined** | Improvement is a secondary title sense of 伸びる; no direct collision was established. |
| Late correctness finding, `進歩`–`発達` | **Resolved** | `進歩.md:9` declares `発達` (`e1a7600`). JMdict 発達 sense 2 is "progress; development; advancement". The examples overlap: 進歩 describes medicine advancing and a skill improving; 発達 describes a child's speech and a transport system developing. |
| M7 / comprehensibility 2, `進める` title/H1 mismatch | **Resolved** | H1 matches the title «продвигать; вести дело вперёд»; «продолжать» stays with 続ける. |
| Comprehensibility 3, circular `進める` ban | **Resolved** | The sentence was deleted; the を/が contrast and collocation advice remain. |
| Comprehensibility 4, `通過`/`合格` «проверки» overlap | **Resolved** | `通過.md` now ties the figurative use to passing a selection stage and adds a linked `合格` comparison, 試験に合格する: «прохождение этапа» vs «соответствие критерию». |
| Comprehensibility 5, English «way» in `道路` | **Resolved** | The warning is now worded entirely in Russian. |
| M8, no progress/tracking record | **Resolved by the record commit** | The batch records, ledger and progress updates are committed with this file. |
| L1, weaker label overlaps | **Optional, declined** | Consistency recheck 3 judged 過去–昔, 通信–伝える/放送 and the cross-part-of-speech pairs advisory only. Shared tokens such as «экзамен», «вперёд» or «период» do not establish a direct answer collision. |
| L2, seven cards without a word-type tag | **Declined** | Inherited unchanged from frozen EN; metadata parity is kept and no repository rule requires the tag. |
| L3, five kanji without RU cards (善, 徳, 改, 逮, 遂) | **Out of scope** | Kanji metadata is correct; the validator exempts kanji without cards; the EN `../kanji/改` link stays plain text. |
| Optional navigation (`週.md:34`→`週間`; plain new words on 15 kanji cards) | **Optional, declined** | Link parity on `週.md` and the 15 kanji cards found no EN link to a B188 word missing in RU; return links are not required for every mention. Links dropped because their RU targets are absent remain listed for restoration, including CW086 `勧める`–`進める`. |
| Comprehensibility optional notes | **Optional, declined** | English-homonym warnings carried over from EN, godan/ichidan labels and the カイゼン note were not defects. |

### Withdrawn reciprocal requirement

The initial consistency report and the reciprocal audit assumed that each excluded pair must be declared on both cards.
That premise was withdrawn. The frozen EN contract (`docs/content-format.md:162–165`, `docs/confusable-words.md:311–312`)
and the Android reader at `87c34fb` (`Words.kt:177–180`; `WordsTest.kt:182–200, 250–273`) apply each declaration in both
directions, and not transitively. The reverse entries added to the baseline cards `次々`, `発展` (`b8eaf44`) and `幸せ` (`35ddea4`)
were removed in `d9c6b4f`. B188 therefore changes exclusions only on its 30 new cards; the nine navigation files change only links.
The audit's per-pair semantic dispositions ("retain" for every listed edge) were accepted. No transitive pair was inferred.

### Preserved disagreement: `幸い`–`幸福`

- Consistency recheck 1 (`b8eaf44`) called it **unsupported**: «удача; к счастью» and «счастье; благополучие» differ enough.
- Correctness recheck 2 (`d9c6b4f`) reported it as a **medium, high-confidence** quiz ambiguity. Daijisen defines the noun sense of 幸い as 「しあわせ。幸福」, and JMdict gives "happiness; blessedness".
- Consistency recheck 3 (`d9c6b4f`) called it **supported but advisory (low)**: the adverbial «к счастью» sense is not 幸福, but the noun sense overlaps, and `幸い` already excludes `幸せ`, which in turn excludes `幸福`.

Resolution: the direct guard was added on evidence. The dictionaries show the noun sense of 幸い overlapping 幸福, and a learner
could defend either title. An exclusion only removes one foil; it does not claim the words are interchangeable. Both reviewers
who had raised the pair verified the fix at `e1a7600`. The earlier "unsupported" judgement was based on titles alone and is
superseded by the dictionary evidence, not by a vote.

### Process deviations

- During the `d9c6b4f` round, correctness, consistency and comprehensibility rechecks were started concurrently, contrary to the
  one-reviewer-at-a-time workflow. The coordinator kept the correctness recheck and stopped the other two.
  - The comprehensibility recheck produced no report.
  - The consistency recheck had already returned a complete report (CLEAN, "no missing pairs required"). It is recorded as an
    **unaccepted draft**, not as review evidence; its "no missing pairs" conclusion conflicts with the accepted correctness and
    consistency rechecks. Its out-of-scope note on the baseline card `カーブ` («кервбол») was not assessed in B188.
  - The consistency recheck was then repeated serially at the same tree and is the accepted record above.
- The original comprehensibility reviewer could not receive a follow-up message in this runtime. A new reviewer with the same
  assigned model (`grok-4.7`) received the original five findings, the final snapshot and the actual card diff `c721e1c..e1a7600`.
- An untracked early final-validation draft seen by consistency rechecks 1 and 2 was not committed and is not evidence; the
  validation receipt is generated after these records are committed.

## Final bounded verdicts

- Correctness: **CLEAN**.
- Scoped coverage: **CLEAN**.
- Comprehensibility: **CLEAN** after fixes.
- Cross-file consistency: **CLEAN**.
- Quiz safety: **CLEAN** for the reviewed batch and the directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

The correctness recheck at `d9c6b4f` re-read the complete 30-card common sample; the final follow-ups were bounded to the
`d9c6b4f..e1a7600` diff. The comprehensibility recheck covered the changed passages and the cross-card targets `幸運` and `合格`.
No reviewer re-audited the complete Russian word pool or executed the quiz UI.

## Final validation

On the final candidate `e1a7600f347424fa0ae13a97aeee7eb99eb53b41`:

- `tools/build_manifest.py`: 3,759 files; content version `b0eb8ea82765424a`; rebuild idempotent.
- `tools/validate.py`: 0 errors.
- `python -X utf8 -B -m unittest discover -s tools -p 'test_*.py'`: 124 tests passed.
- `tools/check_content_budget.py`: 3,767 archive files; 3,776 entries; 10,534,709 inflated bytes; 5,292,992 local ZIP bytes.
- 30-card source checker: 0 bad, covering example sentence/reading pairs, encoding and Latin text.
- Frozen Japanese sentence scan: 124 strings, 0 missing.
- Link parity across the 39 Markdown payloads: the only difference from EN is the intentional `通過`→`合格` link added by the comprehensibility fix.
- `git diff --check`: clean. Intake hashes match all 39 payloads.

## Limits

No native-speaker, device, learner, voice, drawing, runtime import, activation or ordinary-release acceptance is claimed.
Quiz-safety judgements rest on displayed titles, article text and dictionary senses, not a quiz-engine simulation. Advisory pairs
remain advisory. The exact model variants above are the assigned models recorded by the task runner; no serving-build identifiers
were available.

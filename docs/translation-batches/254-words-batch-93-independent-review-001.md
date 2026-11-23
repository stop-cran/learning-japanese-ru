# B254 — independent review of word batch 93

**Blind candidate:** `559309ba0d24b9a8cd90fe1a59776a34a86a66e8`, tree `a2bcc0443c45b810984ecb22edec77e7b21d4e81`. **Frozen EN:** `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. **Published RU input:** `9ea35cf017da9e6ec4d458e8fb614420813b41e0`. The candidate's parent `7ba5db72ca85c0d5a92fb6f79d7ab902b09a472d` adds only B253 records above that input. The authoring snapshot `272665c192e3f9492a88822d2564f424f4ef5a72` (parent `074c0bbd6d50b31cf5c4eaeb0572617718380edf`) supplied 40 preflighted content blobs, not a manifest or a merge parent.

The [intake](254-words-batch-93-intake.json) fixes the 30 new words and ten existing navigation files by path and raw EN/RU hash. The requested word set equals its closure; no additional or held word and no deferred guard. Relative to its parent the signed candidate changes those 40 files, the rebuilt manifest and the intake only. Tracking and generated progress still describe B253 at this stage.

### Common sample and independent returns

Each reviewer had the same 30 complete EN/RU pairs verified against the intake, the 30 attributed dictionary packets, the frozen EN repository, existing RU labels and secondary senses, all ten navigation diffs and the signed candidate/base diff. The common mechanical input named existing exclusions and links, not a judgement of their necessity. Initial reviewers were not given the author's adjudication, other reviewers' findings, or the coordinator's subsequent reconciliation supplement. The signed candidate did not change between assignments.

| Assignment and original report | Runtime model and reviewer ID | Initial run, UTC on 2026-11-23 | Original report: bytes / raw SHA-256 |
|---|---|---|---|
| [Correctness and source coverage](254-words-batch-93-review-correctness-001.md) | `gpt-6.2-sol` · `e068a9e0-56ea-4f50-a09c-e5f151de29cc` | 21:06:37.893–21:18:51.300 | 10,821 · `5eab33ff263aed312282220e5ad107fe54e1433899257152b5b984682f342ce9` |
| [Consistency, quiz safety and integration](254-words-batch-93-review-consistency-001.md) | `claude-opus-5.5` · `d6fa97fa-35a2-416f-8e84-0f260d96c459` | 21:19:37.975–21:27:41.925 | 7,680 · `92969b9291ca8f976f04c864ee3ed092dfe9eaa1a7656868b1f90c64f6fe9baa` |
| [Russian comprehensibility and scoped coverage](254-words-batch-93-review-comprehensibility-001.md) | `grok-4.7` · `a4fb99dc-af7c-4824-b3fc-bb51193fa085` | 21:28:10.528–21:41:11.477 | 6,243 · `133a812896b0aa9c5b0b5d6958ad9661723a8d3a919e24b2b7df000ee3bc58f2` |

Each initial `subagent.completed` preceded the next `subagent.started`. The completed-agent metadata identified the three distinct serving families. All three reviewers reported reading the 30 pairs and ten navigation diffs in full. Separately, the execution records contain each complete numbered pair and each navigation file's complete diff, not merely commands requesting those reads. In each run the public report also appears in returned tool output (comparison after normalizing line endings and ignoring trailing newline/edge whitespace). The hashes above identify the saved original report files, **not** the stdout wrapper, network bytes or the Git files with their provenance prefixes. Completeness of the returned text is not proof of comprehension.

### Initial results and coordination decisions

The tables preserve each reviewer's assignment, including overlaps and unverified claims. “Accepted” here means implemented at signed fix `dfdfeebcc0c54972451bc3d028ccc918ccc99ab7`; the [separate recheck record](254-words-batch-93-recheck-001.md) reports what the original reviewers found on those bytes.

| Correctness finding | Decision and source-specific reason |
|---|---|
| F01 冷める, medium | Accepted. JMdict 1556750 §2 includes feelings subsiding. A person can «охладеть к поездке», but anger itself subsides: «гнев утихает». |
| F02 消極的, medium | Accepted; also comprehension C2. JMdict 1350220 §1 and the two complete JP sentences support reluctance about the plan and **opinions** showing reluctance to act, not polite delivery by many speakers. Retained the distinct 遠慮 comparison. |
| F03 流行る, medium | Accepted. 1552310 §2 supports prevalence/spread without severity. Replaced «свирепствовать» in title, heading, definition and flu example. Fashion and a flourishing establishment remain separate uses. |
| F04 流域, medium | Accepted; also comprehension C1. Water flows **from the land into the river**. Removed the additional unsupported frequency claim about «бассейн» without removing its other Russian meaning. |
| F05 活字, medium | Accepted. 1208300 §1 concerns movable type. The text, not the typeface, is what the printer sets from individual pieces of type. |
| F06 活力, medium | Accepted. 1208480 §1 concerns vitality and energy to act, not mere viability. Retitled «жизненная сила; энергия». |
| F07 治す, medium | Accepted. 2856318 §1 and contrast with 治る: «вылечить; залечить (рану)». The completed medicine example reports recovery; the ために example reports a goal. |
| F08 海水浴, low | Accepted. 1201520 §1 and frozen EN describe bathing/swimming as the activity. The journey belongs to に行く; not every beach visit qualifies. Daijisen also includes sunbathing, so the old absolute exclusion was not retained. |
| F09 消防署, low | Accepted. [Daijisen, 消防署](https://www.weblio.jp/content/消防署) situates the institution in municipalities and special wards. Kept organization/building and corrected the public-service gloss, including the 署 explanation. |
| F10 洋品店, medium | Accepted; also a comprehension optional. Title names the Western style, not the goods' country of origin. Primary 1794470 §1 and separate 洋品 1662200 §1, not an invented sense of the first entry. |
| F11 法則, medium | Accepted; also a comprehension optional. 1517380 §1 and [Daijisen §1–2](https://www.weblio.jp/content/法則) support an obligatory rule as well as a scientific regularity. «Закономерность; научный закон; правило» agrees with the body and the existing 則 navigation. |
| F12 洒落, low | Accepted. The frozen row selects 1568640 §1; the style sense (§2) does not receive a separate N2 classification. The learner-facing qualifier is restored; the word's `jlpt` is unchanged. |
| F13 example format, low | Accepted as a **literal formatting** correction, not a corrupted reading. Restored the source separator and parentheses for 59 pairs across 29 cards: 53 space-plus-parenthesis and six newline/indent-plus-parenthesis. Both 冷める pairs were already exact. All 61 sentence–reading blocks, including internal punctuation, match frozen EN in order. |
| F14 おしゃれ, low | Accepted. 出かける does not say the speaker takes a walk. «Сегодня перед выходом я наряжусь» preserves getting dressed to go out. The coordinator had separately recorded the same concern against the authoring snapshot, checked it on the signed candidate and the existing 出かける card, and **did not give it to the initial reviewers**. |

Correctness and scoped coverage were **NEEDS FIX**; comprehensibility was not assigned. The ten navigation diffs were clean within the changed lines. The initial reviewer's unresolved «обычно» observation on 流域 is separately addressed under F04.

The consistency reviewer reported **NEEDS FIX** on quiz safety (one medium C1); format, links and source preservation **CLEAN**. C1 proposed a one-sided ショップ→売り場 guard. The reviewer marked the remembered English wording “point of sale” **unverified**. Coordinator verification found `1588550` §1 in frozen EN `docs/n2-vocabulary-batch-sources/batch-68.json`, `reviewEvidence/comparisonEntryFamilies`: selling area, counter, section, department, sales floor, **not that literal quote**. [Daijisen 売り場 §1](https://www.weblio.jp/content/売り場) includes a place where goods or tickets are sold. With the actual labels «торговая точка» and «место продажи; торговый отдел», one direct guard avoids a defensible answer; it does not mean that every shop is a department. The original report also paraphrases the EN title: the actual frozen `words/売り場.md` title is **sales area**.

| Candidate-only direct entry or proposal | Disposition at fix; not empirical necessity |
|---|---|
| 商店→店; ショップ→店 | Kept separately. 1347180 and 1062820 each give the shop sense; 店 1582120 §1 includes precisely a store/shop. «Магазин» fits both, independent of any third pair. |
| 油断→のんき | Kept. Frozen batch-66 `entryFamilies/1600560` §1 includes careless/thoughtless as well as carefree; 1538690 includes carelessness. Current RU cards teach both the actual lapse and a careless attitude. A shared stem alone would not establish this. |
| 涼む→休む | Kept conservatively for the actual RU label «отдыхать в прохладе» vs «отдыхать». 1554380 is enjoying the cool air, not “to rest” in general; ordinary-quiz necessity is unverified. |
| 泊める→泊まる (optional O2) | Removed. The host provides lodging (1474860 §1); the guest stays (1474850 §1). «Дать ночлег» and «ночевать» distinguish those roles. No inherited pair was removed; the comparison and the causative explanation remain. |
| ショップ→売り場 (C1/O3) | Added on ショップ; evidence above. The existing 売り場 file is unchanged. |
| 洋品店→商店 (optional O1) | Added as a separate conservative direct pair. A shop for Western-style apparel/accessories (1794470; 1662200) is a retail shop, the actual 商店 label. The presence of a more specific option does not invalidate the broader one. Not inferred via 店; no claim about all shops or guaranteed generated options. |

The comprehension reviewer reported **NEEDS FIX** for Russian, **CLEAN** for scoped coverage. Both findings (C1, C2) overlap F04/F02. Other optional observations: chose «пропустил» in 油断 and a glossed causative in 泊める; accepted the qualifier/title and outing changes above. Kept «налейте» for putting liquid into a bottle, the EN example's plural shops in 活力 (number is not specified in Japanese), «торговая точка» with the guard, and practical explanations after «атэдзи». These are not additional mandatory findings. No cross-facet model ranking or learner test.

### Integration and limits

All 15 links in the ten existing cards are wrapper-only and remain at the same bytes in the signed fix: `kanji/則` → 法則 (2), `kanji/商` → 商店 (3), `kanji/域` → 流域 (1), `kanji/巻` → 寝間着 (3); `words/せっけん` → 洗剤, `断水` → 淡水, `気体` → 液体, `活躍` → 活力, `焦点` → 商店, `血液` → 液体. 断水→停電 is an existing RU-only link, not a sixteenth new link. The old 「規則」 link in the 則 reading row and the existing 活動/努力 links alongside 活力 are not new links either.

In the 30 new cards, five in-batch href occurrences are retained. Twelve EN href occurrences have eleven absent RU targets: ten kanji paths (極 毒 油 泊 浴 液 涼 署 衣 防; 浴 twice) and the word 冷ます. The set of **written kanji without an RU card** is larger (淡 涼 液 防 署 耗 毒 極 的 浴 衣 剤 洒 泊 油); missing a kanji card is not identical to losing an EN href. The fix retains all EN relative href occurrences to available targets. The 122 EN exclusion entries include seven in-batch entries; the candidate appended five entries, the fix appends six (128 total), always after the inherited ordered prefix. No transitive closure.

For reconciliation, a separate supplement resolved references already available in frozen EN: seven source rows with additional senses (冷める, くたびれる, 消化, 流行る, 洒落, 洋品店, 注す) and the two 寝間着/寝巻 source surfaces for ねまき. In particular the original common per-card JSON did not separately expand the 洋品 family. Source access is not evidence that each initial reviewer actually read a particular family; the original packets and returns were not replaced.

Qualified source-content evidence only. A validator, title screen, successful recheck or manifest membership does not certify every fallback choice, voice or drawing prompt, device, learner outcome, ordinary activation or release.

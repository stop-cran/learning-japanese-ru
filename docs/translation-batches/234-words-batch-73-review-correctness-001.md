# B234 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `1e7c04d20795a3f0efac996855d00f233ebe566b` (tree `02023ebe35e7f52010e453f8711aa47bf99c56ae`),
> the signed candidate pushed before review.
> Later reconciliation is in `234-words-batch-73-recheck-001.md`.

Snapshot: RU 1e7c04d20795a3f0efac996855d00f233ebe566b, branch full-ru-234-words-73, compared with parent 931612db628dde1a2b447b910eaa7d476980eed2. Frozen EN: 6af98cb717755690a9ca793e5454a96ebd7a8f9f. RU HEAD matched the candidate at both checks; initial and final working tree and index were clean. No repository edits, generators, commits, pushes or issues.

Scope: Blind correctness and scoped-coverage review. I read each of these RU files IN FULL against its complete frozen EN original:

- words\お先に.md; words\さようなら.md; words\送別.md; words\送り仮名.md; words\ずれる.md.
- words\退く.md; words\退ける.md; words\埋める.md; words\補う.md; words\追加.md.
- words\追い越す.md; words\追い掛ける.md; words\迷信.md; words\述語.md; words\宴会.md.
- words\応対.md; words\応接.md; words\接する.md; words\接近.md; words\催促.md.
- words\迫る.md; words\近寄る.md; words\近付ける.md; words\近々.md; words\農薬.md.
- words\農産物.md; words\農村.md; words\船便.md; words\交通機関.md; words\輸送.md.

Also checked the runtime link additions in kanji\埋.md and words\パーティー.md, 追う.md, 隙間.md, 面接.md, relevant existing RU comparison cards, stable front matter, retained citations, Japanese example/reading text, and available-target link parity. Prohibited author/reviewer materials were not consulted. One reviewer; no subagents. Actual model identity is not independently verifiable.

Verdicts:
- Correctness: NEEDS FIX. Exceptions: 近々 and 補う, below. The other 28 new cards are CLEAN within this scope.
- Scoped coverage: NEEDS FIX for 補う's lost explicit qualification. 近々 and the other 28 cards are CLEAN: the broader temporal sense remains in 近々's body despite its narrowed title/example. No other actionable omission of an EN sense, teaching note, example, citation or available-target link was established.
- Comprehensibility and quiz safety were not separately assigned or certified.

Findings:

F1; Minor; correctness; words\近々.md:4,12,19.
Claim and impact: The title and first translation say «в ближайшие дни», whereas EN says “in the near future.” That introduces a days-based horizon absent from the Japanese sentence and turns a context-dependent possibility into the general displayed gloss. Line 16 correctly retains «скоро, в ближайшее время», limiting the defect; the spatial sense and its reading restriction are also retained.
Remedy: At lines 4 and 12 replace «в ближайшие дни (о предстоящем)» with «в ближайшее время (о предстоящем)»; at line 19 use «В ближайшее время я собираюсь переехать.» Preserve the spatial gloss.
Evidence: Actual JMdict entry 1578110, sense 1: “soon; before long; shortly; in the near future,” without a days restriction. Actual Digital Daijisen ちかぢか sense 1 defines temporal proximity as ごく近いうちに; its きんきん entry says 近い将来 / 近いうちに. Neither supplies the narrower unit. https://www.weblio.jp/content/近々 . Compared directly with the complete frozen EN card.
Confidence: High that the displayed general gloss narrows the source; this is a localized translation-precision defect, not proof that a days-based rendering is never appropriate in context.

F2; Minor; correctness/scoped coverage; words\補う.md:42–43.
Claim and impact: EN qualifies the contrast: “does not automatically mean paying legal damages.” RU says «補う не означает выплату возмещения по закону», without preserving “automatically.” As teaching guidance, this can read as excluding the legal-payment interpretation instead of saying that the verb does not itself establish it. The useful comparison with 補償する should remain, but not as a categorical semantic boundary.
Remedy: Replace these two lines with «補う само по себе не указывает на юридическое возмещение ущерба; для этого значения полезно сравнить 補償する（ほしょうする）.»
Evidence: Actual JMdict 1514460, sense 1 includes “compensate for” and “cover (a shortage, loss, etc.)”; 1514650 gives “compensation; reparation.” Digital Daijisen 補う sense 2 explicitly covers making up for damage/loss; 補償 sense 1 describes compensating losses, especially monetary damages. These support the comparison, not an unrestricted exclusion. https://www.weblio.jp/content/補う ; https://www.weblio.jp/content/補償 . The decisive translation evidence is the missing qualification in the frozen EN/RU comparison.
Confidence: High about the lost explicit qualification; moderate about readers construing the Russian wording categorically. No claim that these entries establish interchangeability in every legal collocation.

Optional: None within the assigned facets.

Limits:
- CLEAN is bounded, not exhaustive linguistic certification or native-speaker approval.
- Existing validator ran directly on the candidate: 0 errors. No manifest generator ran. Original exclusions and external citations were retained; stable metadata differences were additive quiz exclusions. Structural checks supplement, not replace, the full bilingual reading.
- Inspected the actual JMdict XML entries for all 30 primary IDs and all additional IDs cited by these cards. This also verified search-only/rare/irregular/obsolete flags and reading-local restrictions omitted by Jisho's API. Distribution: http://ftp.edrdg.org/pub/Nihongo/JMdict_e.gz, linked by the official project page https://www.edrdg.org/wiki/JMdict-EDICT_Dictionary_Project.html . Retrieved XML SHA-256: a2049d4702b3bacb806f129281992a9bec604ac71f8f7492e313f6538ea699cf. It is a live distribution, not a claim to have reproduced the author's historical dictionary snapshot.
- Supplementary actual dictionary sections included Kotobank 送り仮名, 応対 and 応接; Digital Daijisen entries for the consequential lexical contrasts; Jisho kanji-reading sections; Russian lexical entries and usage. Gramota and some Jisho requests failed; incomplete aggregator snippets were not treated as verified dictionary articles.
- Russian-only expansions were checked against their actual Japanese senses and relevant Russian usage. Agricultural produce includes livestock products in Daijisen; growth regulators fall within «пестициды» in the inspected Russian statutory definition. These are scoped meaning checks, not frequency claims. No unsupported consequential Russian-only claim remained established beyond the findings above.
- Only this report file was written. Final RU status and staged/unstaged diff checks confirmed the repository and index remained unchanged.

Final verdicts: correctness NEEDS FIX; scoped coverage NEEDS FIX.
F1: 近々's title and moving example narrow “near future” to “the next few days.”
F2: 補う's legal-compensation contrast drops EN's explicit “not automatically” qualification.

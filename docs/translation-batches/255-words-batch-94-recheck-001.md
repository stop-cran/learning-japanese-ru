# B255 — scoped rechecks at the signed content fixes

| Input | Revision |
|---|---|
| Frozen EN | `6af98cb717755690a9ca793e5454a96ebd7a8f9f` |
| Signed blind candidate / parent of first fix | `8f4707c36e5d79d004c808e633c03c2cfaa4ae11` |
| First signed fix / parent of second fix | `46f7089e8d6257686cd4af522595ec7455c107ed`, tree `973ca257d8082965aa82b68a01f56016f9cb473e` |
| Second signed fix, final rechecks | `c4d64291556bb0cc4ee7457febb567dea37df433`, tree `d3da7587f2e91bbf74d80e9400d92e9e086ea62c` |

The [independent-review record](255-words-batch-94-independent-review-001.md) separates initial reviewer findings, coordinator checks and the decision on each item. The first fix changes 18 of the 30 new word files and the generated manifest; the second changes 汁 and 正味 and the manifest again. Neither changes the intake, the nine navigation files or the other twelve new cards (水素, 水平, 気圧, いってらっしゃい, 気を付ける, 公衆, 毛皮, 比較的, 殻, 段階, いちいち, 死体), which keep their candidate bytes. No Japanese sentence, reading or kana string was rewritten: the changes are Russian titles, glosses, explanations and quiz exclusion lists, and the Japanese-script characters of every changed body line are identical between candidate and second fix.

### What each recheck covered

Unlike B254, the original reviewer sessions could not take a follow-up message. Each facet was therefore rechecked by a fresh instance requested on the original reviewer's model, given the original brief, the original report, the coordinator's dispositions as claims to verify and the cumulative diff. Each rechecker states in its report that it did not write the original review. They ran strictly in sequence, each after the previous one's final reply; the correctness rechecker's second round was a follow-up message to the same instance after the second fix. Rechecks covered the changes, not a second blind read of the batch.

| Facet | Runtime model and rechecker ID | UTC | Bounded result and actual scope |
|---|---|---|---|
| Correctness and source coverage | `gpt-6.2-sol` · `0b689367-2de0-45a9-87bf-29d2b6eb77fe` | Round 1 on `46f7089e`: 2026-11-23 23:44:33.855–23:51:17.269. Round 2 on `c4d64291` (follow-up message to end of reply): 23:55:29.232–23:56:51.696 | Round 1: F01–F09 resolved, two new findings — R01 汁 «похлёбка» is narrower than Daijisen しる③ (吸い物, 味噌汁); R02 正味 «без наценки» excludes ordinary markup, whereas 掛け値 is a price padded for bargaining — so **NEEDS FIX / NEEDS FIX**. Both were applied in the second fix. Round 2: R01 and R02 resolved, no new finding, **CLEAN / CLEAN**. Returned in round 1: every changed line of all 18 changed files. Round 2: every changed line and all 33 nonempty lines of 汁 and 正味 at `c4d64291`; スープ only partly, and it was not reported as a full read. |
| Consistency, quiz safety, integration | `claude-opus-5.5` · `4d5572e2-27ba-4669-8eae-42b04dfbacdd` | 2026-11-23 23:57:59.865 – 2026-11-24 00:08:28.502 | At `c4d64291`: quiz safety, format/links/navigation/manifest and integration coverage **CLEAN**. F1 and F2 resolved; the four removals are justified on the whole labels; the optionals are correctly left optional and 水筒 «В» is resolved. EN 121 entries retained in order, RU 131; the 12 unchanged cards and nine navigation files are byte-identical; validator 0 errors. Returned: the complete cumulative word diff in `--word-diff=plain` form (all 217 nonempty lines in one result), the manifest diff, the brief, original report and dispositions, and nine cards in full (ステージ, 演説, スピーチ, 水平線, 歯車, 欧米, 比較的, 元気でね, いってらっしゃい). Its zero-context diff was filtered to title and exclusion lines, so whole changed body lines of 14 files appear only in inline-marked word-diff form. |
| Russian comprehensibility and scoped coverage | `grok-4.7` · `f1d023ab-411a-4c1e-8d43-3de1ba60c997` | 2026-11-24 00:11:01.727–00:18:24.765 | At `c4d64291`: Russian comprehensibility of the changed learner text **CLEAN** (the original candidate NEEDS FIX, as reported). F1–F4 resolved; O3, the 汁 plant/fruit narrowing, resolved, and the broader 汁 title and the 正味:35 price gloss were read without a new defect; O1 垂直 «ровный» and O2 正門 «не прямой» remain optional; no new optional. Returned in full: the brief, original report and dispositions, and 汁, 毎度, 正味, おだいじに, 残らず, 正門 at `c4d64291`; every changed line of all 18 changed files. Range reads: 民謡 1–40, 歌謡 1–30, 公共 25–45, 民間 25–42, 元気でね 1–28, 水分 1–30, 歯磨き 1–28, 水筒 28–42, 垂直 15–35, and ステージ, 水平線, 歯車, 欧米 1–15. The other 12 new cards and the navigation files other than 垂直 were not reread; no validator was run. |

The coordinator matched every nonempty line of each read that the rechecks call full or give as a range against the tool output each rechecker actually received; none was missing. The comprehension report notes that its prompt listed 正味:9; the cumulative diff does not change that line (tags), and the coordinator's prompt was in error. That rechecker's one `rename_session` call was refused as a no-op; its only file write was its report. The [initial review record](255-words-batch-94-independent-review-001.md) documents the complete blind reads; each recheck verdict applies only to the material it actually returned.

### Changed titles and evidence limits

| Word | Blind label → signed fix |
|---|---|
| 汁 | «сок растений и плодов; бульон; похлёбка» → first fix «выжатый или выделившийся сок; бульон; похлёбка» → second fix «выжатый или выделившийся сок; бульон; суп» |
| 毎度 | «каждый раз; благодарим за покупку (постоянному клиенту)» → «каждый раз; спасибо, что снова выбираете нас (клиенту)» |

At the second fix the complete 30-word title screen against the RU pool returned 234 lexical lines: 35 already guarded and 199 unguarded (at the candidate: 258 lines, no unguarded exact segment). It removes parentheticals and splits labels on `;` and `,`. Four exact segment matches remain. 汁–スープ («суп»), 毎度–ありがとう and 毎度–どうも («спасибо») are guarded by inherited EN pairs. 毎度–すまない («спасибо») is unguarded and comes from splitting the connected label «спасибо, что снова выбираете нас»: thanks for repeat patronage and «извини, виноват; спасибо, прости за хлопоты» are not answers to each other's prompts, as the coordinator and the consistency rechecker judged separately on the whole labels. Neither this screen nor the guard decisions establish that all Russian meanings are distinct or that every theoretical overlap will be drawn.

All 121 EN exclusion entries of the 30 cards remain in source order; ten RU-only entries follow them (131). Five were judged required for the displayed labels (いってらっしゃい→さようなら, 元気でね→さようなら, 公衆→観客, 正味→中身, ステージ→演説), five conservative without established necessity (水平線→横, 元気でね→元気, 民間→私立, 比較的→比較, ステージ→スピーチ). Four candidate-stage RU additions were removed (水平線–地平線, 歯車–車輪, 欧米–欧州, 欧米–ヨーロッパ): each article teaches the contrast, and neither whole label answers the other. The consistency rechecker agreed with each classification and corrected one reason: 健康 «здоровье; здоровый» does contain a «здоровый» segment; it is not paired with 元気でね because a farewell formula and a state do not answer each other. Its two new optionals are not adopted in this batch: 正味–値 (正味 guards 価格 and 値段 for its body-taught secondary price sense; 値 «цена (товара)» is unguarded in frozen EN too) and a conservative 毎度–再三. Both are inherited EN gaps, not effects of the fixes; necessity is not established, and adding them would need its own check. Nothing here certifies option counts, tag/random fallback, voice, drawing, device rendering, ordinary RU activation or release.

The second fix tree regenerated manifest `57ea12fc9026d94d` (5,764 files, three images, two scene catalogs); the validator reported zero errors, 124 unit tests passed, and the post-generation local archive-budget estimate was 8,377,540 bytes (5,786 entries). These checks used the content-fix tree; final validation of the later committed records is a separate [receipt](255-words-batch-94-final-validation-001.json), not a public archive or release verification.

## Original recheck reports

The reports below are reproduced in run order, normalized to LF. Section headings, runtime metadata and hashes are not part of the reports. A hash denotes the original report file, not its stdout wrapper or the network return.

### correctness, round 1 — gpt-6.2-sol

Agent 0b689367-2de0-45a9-87bf-29d2b6eb77fe, input 46f7089e8d6257686cd4af522595ec7455c107ed, completed 2026-11-23T23:51:17.269Z; original report file SHA-256 f0e3e43b9189905a07533e3e8c5c57621ad0c0ded8cc0ca3cb0ee49328013ebd.

Snapshot: B255 `255-words-batch-94`, RU fix `46f7089e8d6257686cd4af522595ec7455c107ed` (tree `973ca257d8082965aa82b68a01f56016f9cb473e`, local Git signature status `G`), parent/candidate `8f4707c36e5d79d004c808e633c03c2cfaa4ae11`. `rev-parse HEAD` matched the fix and `status --porcelain` emitted nothing at start and finish. No uncommitted changes. EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`, Git objects only.

Scope: Correctness and scoped coverage, read-only recheck. The initial blind review of these facets at the signed candidate was written by an earlier instance of the same model, gpt-6.2-sol. That instance cannot receive follow-up; I am its replacement, not the author. Model for this recheck: gpt-6.2-sol per assignment; no independent runtime model identifier verified. Read `briefs/b255-brief-correctness.md`, `originals/b255-review-correctness.md` and `dispositions-correctness.txt` in full. Read all old/new hunks with context from the authoritative commit-to-commit `-- words` diff. Supplementary human reading below: `words/<ID>.md`, fix RU / frozen EN, inclusive lines.

- 汁 1–45 / 1–47; 残らず 1–42 / 1–35; 毎度 1–43 / 1–39; 公共 1–47 / 1–51; 民間 1–45 / 1–50; 正味 1–45 / 1–36 (all six pairs in full).
- ステージ 1–44 / 1–46; 水平線 1–41 / 1–35; 歯車 1–43 / 1–46; 欧米 1–45 / 1–52 (all four pairs in full).
- 元気でね, 水分, 歌謡, 正門, 歯磨き, おだいじに: 14–25 / 14–25 each; 民謡 26–42 / 1–44; 水筒 26–39 / 26–33.
- RU quiz context only: 地平線 1–25,34; 車輪 1–25,46; 欧州 1–25,42; ヨーロッパ 1–25,43; 演説 1–25,56; スピーチ 1–25,58. Rules: RU `.github/copilot-instructions.md` 166–255, `.github/instructions/content-structure.instructions.md` 121–181, `docs/content-format-reference.md` 44–112, `docs/translation-methodology.md` 152–203; EN `docs/content-format.md` 136–174 and `docs/confusable-words.md` 10–49,67–77 and quiz-rule search hits.
- Sources actually consulted: B255 paired-sample `dictionary/{汁,毎度,正味,水分,ステージ}.json` in full (JMdict 2026-10-21 entries 1335520, 1524710, 1377980, 1372010, 1070320, respectively). Named online entries/sections: Digital Daijisen しる 1–3 and 味噌汁, 残る 2 and 残らず (plus Weblio conjugation entry), 毎度 1–2, 公立 and 私立 1, 正味 4 and 掛け値 1–2, 歌謡曲 1, 工事, 付ける 1㋐ and 歯磨き, 民間 1–2, 水筒, 水平線 1–2, 地平線 1–2, and 欧米 (also Seisenban NKD’s 欧米); Weblio 実用日本語表現辞典 お大事に; Gramota’s Kuznetsov and Babenko entries for «похлёбка» and «наценка»; MAS «сок» sense 1 as reproduced by Gufo; Tofugu volitional conjugation and proposing/inviting; Japan Environment Ministry prevention page and Apple Music RU *Atelier* genre label. Checked the actual relevant entries/sections rather than relying on search summaries.
- Mechanical checks on the full 18 changed word objects: 36 Japanese example sentences and readings match old RU, fixed RU and EN (punctuation, kana spacing and sentence–reading layout; LF/CRLF not compared to EN). Stable `word/reading/jlpt/type/kanji/tags` match EN; all inherited exclusion entries retained in order; H1/title agree; link labels and targets did not change and fixed relative targets exist. The exclusion change targets have valid word IDs. Only these 18 cards and `manifest.json` differ between the commits.
- Blob IDs and modes match between both RU commits for all 12 unchanged word cards: 水素, 水平, 気圧, いってらっしゃい, 気を付ける, 公衆, 毛皮, 比較的, 殻, 段階, いちいち, 死体. Also match for all nine navigation files: `kanji/圧.md`, `words/{お帰り,地平線,垂直,毛糸,羊毛,血圧,西洋,門}.md`. This confirms raw byte identity, not a fresh review of those files.

Verdicts:
- Frozen initial report at `8f4707c`: correctness **NEEDS FIX** (F01–F09); scoped coverage **NEEDS FIX** (汁/F01; all nine navigation diffs CLEAN); Russian comprehensibility **not assigned**.
- Recheck at `46f7089`: correctness **NEEDS FIX** and scoped coverage **NEEDS FIX**, limited to R01–R02 below; other changed areas CLEAN within assigned scope. Russian comprehensibility **not assigned**.

Findings — disposition of the initial findings (high confidence):
- **F01 — resolved** for the reported juice/sap restriction. `words/汁.md:4,12,16,42` no longer limits the source to plants/fruit; :42 was already generic «сок», so no edit there was needed for that defect. MAS «сок» 1 includes animal tissues; Daijisen [しる](https://kotobank.jp/word/汁-526204) 1 and archived JMdict 1335520 support the new first gloss. JMdict’s spelling and つゆ-only dipping-sauce restrictions at :39–44 are intact, as are both EN guards. See R01 for the distinct soup gloss issue.
- **F02 — resolved.** `words/残らず.md:27` explicitly ties the negative to intransitive 残る, «так, что ничего не остаётся»; :34,39–40 retain the contrast with 残す and clause polarity. [残る](https://www.weblio.jp/content/残る) 2 and [残らず](https://www.weblio.jp/content/残らず) confirm the distinction.
- **F03 — resolved.** `words/毎度.md:4,12,20` now thank for repeated patronage without inserting a sale or a face-to-face greeting. JMdict 1524710 s2 and [毎度](https://www.weblio.jp/content/毎度) 2 support the formula; :22–23 still teach the distinct shortened greeting, and :28 preserves the frequency sense.
- **F04 — resolved.** `words/公共.md:36` distinguishes typical local administration from the wider category that can include 国立 when contrasted with private institutions; `words/民間.md:34` includes both private individuals and organizations, with establishment and maintenance. Daijisen [公立](https://www.weblio.jp/content/公立) and [私立](https://www.weblio.jp/content/私立) 1 directly support the distinctions.
- **F05 — resolved** for the earlier «себестоимость» error in `words/正味.md:35`: «закупочная цена» denotes the purchase price, as in 仕入れの値段 (Daijisen 正味 4; JMdict 1377980 s3). See R02 for the replacement of the *other* price gloss on that line.
- **F06 — resolved.** `words/元気でね.md:19` expresses an invitation («Давай ещё встретимся»), not a prediction; matches EN and [Tofugu’s volitional](https://www.tofugu.com/japanese-grammar/verb-volitional-form-you/) 会う → 会おう, proposing/inviting.
- **F07 — resolved.** `words/水分.md:22` describes taking in fluids without implying an existing deficit or requiring plain water; matches EN, JMdict 1372010 s1 and [the Environment Ministry's usage](https://www.wbgt.env.go.jp/heatillness_three_points.php) in prevention.
- **F08 — resolved.** `words/歌謡.md:22` gives the attested Russian genre label «каёкёку», with original かようきょく intact. [Daijisen 歌謡曲](https://www.weblio.jp/content/歌謡曲) 1 and [Apple Music RU](https://music.apple.com/ru/album/atelier/1593595502) support the Japanese and Russian forms, respectively.
- **F09 — resolved.** `words/正門.md:20` retains the negative potential during construction, without assuming repair. `words/歯磨き.md:20` retains apply-to-brush action without specifying a tube/squeezing. EN examples and Daijisen [工事](https://www.weblio.jp/content/工事), [付ける](https://www.weblio.jp/content/付ける) 1㋐ and [歯磨き](https://www.weblio.jp/content/歯磨き) support the fixes.

Findings — additional issues confirmed at the fix:
- **R01 — low; correctness and coverage; `words/汁.md:4,12,16` (also carried through :20,42); unresolved.** The reissued label and definition still offer «похлёбка» as the general soup sense. This is narrower than the teaching source: Daijisen [しる](https://kotobank.jp/word/汁-526204) 3 includes [味噌汁](https://www.weblio.jp/content/味噌汁) (e.g. miso with tofu or seaweed in dashi); JMdict 1335520 s2 and EN :4,16 distinguish soup from broth. [Gramota, «похлёбка»](https://gramota.ru/poisk?query=похлёбка&mode=slovari), Kuznetsov and Babenko, give a subtype of soup dressed with flour, grain or potato; Kuznetsov’s other sense is colloquial and disparaging. The body’s :23,33 do mention «суп», but the tested label and primary definition can teach an unwarranted restriction. Keep the new juice gloss and «бульон», use «суп» instead of «похлёбка» in the glosses, and «Суп горячий, будьте осторожны» in the unspecified example. No change to either guard. High confidence.
- **R02 — low; correctness and coverage; `words/正味.md:35`; unresolved.** «Цена без наценки» implies absence of a normal markup, not just absence of an inflated asking price. [Daijisen 正味](https://www.weblio.jp/content/正味) 4 distinguishes 掛け値のない値段 from 仕入れの値段; [掛け値](https://www.weblio.jp/content/掛け値) 1 is an asking price padded above the actual selling price in anticipation of bargaining. [Gramota, «наценка»](https://gramota.ru/meta/natsenka) (Kuznetsov, Babenko) includes ordinary additions to the price. A learner could wrongly infer that the first meaning requires selling at cost, narrowing it to the second. Use «фактическая цена продажи (без завышения в расчёте на торг); закупочная цена». High confidence.

Other patch checks: `おだいじに:16` keeps both contextual wishes and the illness/injury setting; `民謡:33` still distinguishes the ordinary-people association from the meaning “song”; `水筒:36` only changes the preposition form. Exclusions: ステージ adds exact IDs 演説 and スピーチ for the Russian «выступление» overlap, without asserting Japanese synonymy. The removed RU-only pairs do not drop a rule: 水平線 and 地平線 have explicit water/land labels (Daijisen 1 on each); 歯車 is toothed, while 車輪’s label specifies a vehicle wheel; 欧米 includes both regions and neither Europe-only label covers both (Daijisen and Seisenban NKD). Body comparisons and navigation are still present. No additional finding on these edits.

Optional: **ステージ «эстрада» — optional (declined).** RU :16 explains the platform and the second label segment covers the performance. No semantic change or loss of the frozen EN platform/performance distinction.

Limits: Recheck of changed hunks, relevant context and initial findings only; not a new audit of all card prose or the full quiz pool. No manifest contents, validator/build, app/device/media testing, frequency study or independent Russian comprehensibility assessment. No repository files changed by this review.

### correctness, round 2 — gpt-6.2-sol

Agent 0b689367-2de0-45a9-87bf-29d2b6eb77fe, input c4d64291556bb0cc4ee7457febb567dea37df433, follow-up reply ended 2026-11-23T23:56:51.696Z; original report file SHA-256 f6de0de36680fefc507d3253e9d5f96057e414fa5fe78c7e1bfa5190e2d44aee.

Snapshot: B255 `255-words-batch-94`, RU fix `c4d64291556bb0cc4ee7457febb567dea37df433`, tree `d3da7587f2e91bbf74d80e9400d92e9e086ea62c`, parent `46f7089e8d6257686cd4af522595ec7455c107ed`. Local Git signature status `G`. `git rev-parse HEAD` matched and `git status --porcelain` emitted nothing at start and finish. No uncommitted changes reviewed. EN source `6af98cb717755690a9ca793e5454a96ebd7a8f9f`, Git objects only.

Scope: Read-only follow-up on correctness and scoped coverage. Read the entire `git diff 46f7089e c4d64291 -- words`: `words/汁.md` hunks 1–7, 9–23, 39–45 and `words/正味.md` hunk 32–38 (same old and new ranges). At the fix, read both files in full, `words/汁.md:1–45` and `words/正味.md:1–45`, and `words/スープ.md:1–12` for the label. Compared the four Japanese example sentences and their readings with the parent and frozen EN; they match, including punctuation, spacing and layout. The `quiz_exclusions` lines did not change; for 汁 the exact `[ジュース, スープ]` also matches EN. Reapplied the earlier recheck’s source evidence: archived JMdict 2026-10-21 entries 1335520 s1–3 and 1377980 s3; Digital Daijisen しる 1–3, 味噌汁, 正味 4, and 掛け値 1; Kuznetsov and Babenko on «похлёбка» and «наценка». Follow-up reviewer model: gpt-6.2-sol per assignment, not independently verified. The initial blind candidate review was by an earlier instance of the same model, not this reviewer.

Scope — byte identity: Compared Git blob IDs and modes at parent and fix for all 4,303 `words/` objects and `kanji/圧.md`. Only `words/汁.md` and `words/正味.md` have different blobs; all 4,301 other word objects match byte for byte, including the eight word navigation files `words/{お帰り,地平線,垂直,毛糸,羊毛,血圧,西洋,門}.md`. `kanji/圧.md` also matches, so all nine navigation files are unchanged. `manifest.json` was the only other path reported changed.

Verdicts: Prior recheck at `46f7089`: correctness **NEEDS FIX**, scoped coverage **NEEDS FIX** (R01–R02). Follow-up at `c4d64291`: correctness **CLEAN**, scoped coverage **CLEAN** for these two changes and their verified dependencies. Russian comprehensibility **not assigned**. F01–F09 remain resolved as previously reported; not re-audited here.

Findings:
- **R01 — resolved; correctness and coverage; `words/汁.md:4,12,16,20,42`; high confidence.** «Суп» restores the generic dish sense, without the narrower preparation connotations of «похлёбка». Archived JMdict 1335520 s2 gives both soup and broth; Digital Daijisen [しる](https://kotobank.jp/word/汁-526204) distinguishes seasoned cooking liquid (2) from dishes such as [味噌汁](https://www.weblio.jp/content/味噌汁) (3). The juice and broth glosses and JMdict’s つゆ-only dipping-sauce note are preserved. Neither spelling of «похлёбка» remains. «Суп горячий, будьте осторожны» has correct masculine agreement and conveys the hot-soup warning without adding a particular dish; 汁が熱いので、気をつけてください。 and its reading are unchanged. The new exact «суп» segment matches `words/スープ.md:4`; the unchanged direct exclusion at `words/汁.md:9` covers that pair under the same quiz contract.
- **R02 — resolved; correctness and coverage; `words/正味.md:35`; high confidence.** «Фактическая цена продажи без завышения в расчёте на торг; закупочная цена» preserves two distinct readings. Digital Daijisen [正味](https://www.weblio.jp/content/正味) 4 gives a price without 掛け値 and the purchase price (仕入れの値段); [掛け値](https://www.weblio.jp/content/掛け値) 1 specifically means inflating the asking price above the actual selling price in anticipation of bargaining. The new gloss no longer rules out an ordinary trade markup, keeps the acquisition-price meaning, and agrees with archived JMdict 1377980 s3 (net price, cost price). The related 価格/値段 links and the warning against generalizing the price sense remain intact.
- **New findings: none.** No new regression in the changed lines or affected labels within scope.

Optional: None in this follow-up. Prior optional ステージ wording remains declined and was not revisited.

Limits: No new corpus, full quiz-pool, or navigation-content audit; unchanged paths were checked by blob identity only, except for the noted スープ label. No manifest contents, validator/build, or app/device/media testing. No remote re-verification or repository writes.

### consistency — claude-opus-5.5

Agent 4d5572e2-27ba-4669-8eae-42b04dfbacdd, input c4d64291556bb0cc4ee7457febb567dea37df433, completed 2026-11-24T00:08:28.502Z; original report file SHA-256 864fd89fc9d4da84a809c392cf56a275987f1ebe6eb600d967bf5b489851292d.

# B255 recheck — consistency, quiz safety and integration

Reviewer: replacement rechecker (claude-opus-5.5 family). I did NOT write the original blind consistency review (agent 8231b23d…, unavailable for follow-up); I verified its findings and the coordinator's dispositions as claims.

Snapshot: W HEAD c4d64291556bb0cc4ee7457febb567dea37df433, tree d3da7587f2e91bbf74d80e9400d92e9e086ea62c, `git status --porcelain` empty at start and before saving this report. EN read only via Git objects at 6af98cb717755690a9ca793e5454a96ebd7a8f9f. Target: cumulative `diff 8f4707c3 c4d64291 -- words` + manifest.json.

Scope:
- Read in full: R\briefs\b255-brief-consistency.md L1–43; R\originals\b255-review-consistency.md L1–67; R\dispositions-consistency.txt L1–11; the whole cumulative words diff (word-diff and -U0) and the manifest diff.
- Rules: EN docs/content-format.md L136–174 (esp. 162–173) and EN docs/confusable-words.md L300–320 (no B255 words) @6af98cb; RU content-structure.instructions.md L145–185; RU docs/content-format-reference.md L85–110; RU copilot-instructions (quiz-pair rules).
- Cards read in full at c4d64291: ステージ, 演説, スピーチ, 水平線, 歯車, 欧米, 比較的, 元気でね, いってらっしゃい. Partial: 汁, 毎度 (title/exclusions/body lines in diff), 正味 L9/L35/L41, 水筒 L36, 歌謡 L22 (diff). Title/exclusion lines of all partner words named below (RU), and EN title/exclusions of ステージ, コンサート, 正味, 値, 舞台, 公演 plus all 30 EN cards' exclusions.
- Tools: `tools\validate.py` (PYTHONDONTWRITEBYTECODE=1) → "0 error(s)", exit 0, `status --porcelain --ignored` empty afterwards; `word_title_screen.py 汁 毎度` (exit 0); read-only stdin Python: regex title screens over all 4303 RU titles for 汁, 毎度, ステージ, 水平線, 歯車, 欧米, 正味, 元気でね; blob, link-sequence, manifest-hash, exclusion-prefix and H1=title checks.

Verdicts:
- Original candidate 8f4707c3 (as reported, confirmed): quiz safety NEEDS FIX (F1 missing pair; F2 over-guarding); format/links/navigation/manifest CLEAN; integration coverage CLEAN.
- At c4d64291: quiz safety CLEAN; format/links/navigation/manifest CLEAN; integration coverage CLEAN.

Findings:

A. Original findings and optionals
- F1 ステージ–演説/スピーチ — resolved. words/ステージ.md:9 = [舞台, 公演, 演技, 演奏, 芝居, 水準, 演説, スピーチ] (EN six-item prefix kept). ステージ «эстрада; выступление на сцене»; body L16/L20 teaches the performance sense. 演説 «публичная речь; выступление» contains a bare «выступление» that a learner can defend for ステージ → required. スピーチ «выступление перед слушателями» vs «выступление на сцене» → conservative-to-required, harmless. Consistent with 公演 [芝居, 演説, スピーチ]. Confidence medium-high.
- F2a 水平線–地平線 — resolved (removal justified). «линия горизонта (над водой); горизонтальная линия» vs «горизонт (над сушей)»: both whole labels carry the taught water/land qualifier, and 水平線 L31–33 teaches exactly this contrast; neither label is a correct answer to the other prompt. EN has no pair; EN prefix [線, 水平] kept, 横 appended. Residual note: L32 says Russian «горизонт» can name both, so a learner ignoring the brackets might hesitate; the labels still differ by taught content. Medium.
- F2b 歯車–車輪 — resolved. «шестерня; зубчатое колесо» vs «колесо (поезда, автомобиля, велосипеда)»: the vehicle qualifier excludes a gear; 歯車 L32 contrasts 車輪. EN has no pair; 歯車 now has no quiz_exclusions line (as EN). Medium-high.
- F2c 欧米–欧州/ヨーロッパ — resolved. «Европа» is only part of the connected «Европа и Америка; западные страны»; neither whole label answers the other. Body (L36 area) explains the composition. Now consistent with アメリカ «Америка; США», never guarded. 欧米:9 = [西洋] (EN). Medium-high.
- O1 欧米–西 — optional, not adopted; agree. 西 «запад» is a direction, not «западные страны».
- O2 元気でね–健康 — optional, not adopted; agree: «здоровье; здоровый» vs «всего хорошего; будь здоров (при прощании)» — neither is a defensible answer to the other. The disposition's reason ("«здоров», which 健康 lacks") is imprecise: 健康 has «здоровый»; the real difference is farewell formula vs state/noun. 元気でね–元気 kept (shared base お元気で/元気で).
- O3 割と/割合に — optional/deferred; no RU word files exist (only 割合 «доля; соотношение»). Nothing to check now.
- O4 水筒 «Во»→«В» — resolved: 水筒.md:36 «В 水筒 наливают воду, чай и другие напитки.»
- O5 水平線 «горизонтальная линия» basis — optional, recorded: body L16/L37 and footer cite Digital Daijisen. Sense correctness is outside my facet.

B. RU-added pairs and EN retention — verified.
- Counts: EN 121 entries for the 30 cards; RU 133 at 8f4707c3, 131 at c4d64291. Every EN list is retained as an ordered prefix; RU additions only appended; no duplicates; every target is an existing RU word file (4303).
- Required, agree: いってらっしゃい–さようなら («счастливо (провожая уходящего)» is an ordinary farewell a learner can accept for «до свидания; прощайте», despite L39's usage limit); 元気でね–さようなら («всего хорошего … при прощании»); 公衆–観客 (shared «публика»); 正味–中身 («содержимое» vs the contents sense, body L35 area; parallels EN 内容); ステージ–演説 (F1).
- Conservative, agree: 水平線–横 («по горизонтали»); 元気でね–元気; 民間–私立 (shared «частн-» sense); ステージ–スピーチ; 比較的–比較 — weakest: shared morpheme only («сравнительно» vs «сравнение» are not mutual answers); harmless, it only narrows distractors.
- Removed, agree: 水平線–地平線, 歯車–車輪, 欧米–欧州, 欧米–ヨーロッパ. All four were RU-added (no EN exclusion removed), and per A none is needed for a whole-label answer overlap. The screens found no other unguarded partner whose whole label answers these prompts (e.g. 外国, 直線, 境界 are not defensible).

C. Changed titles
- 汁 «выжатый или выделившийся сок; бульон; суп» (was «сок растений и плодов; бульон; похлёбка») — CLEAN. スープ «суп» equals one segment of 汁 but not the whole title, and is covered by the EN-inherited direct pair (汁:9 = [ジュース, スープ]). ジュース «сок; …» guarded. 液体 «жидкость» is a hypernym, not a defensible answer either way, unchanged EN parity. No new unguarded overlap; dropping «похлёбка» leaves nothing dangling.
- 毎度 «каждый раз; спасибо, что снова выбираете нас (клиенту)» (was «…; благодарим за покупку (постоянному клиенту)»); exclusions unchanged (EN list of 10) — CLEAN. 毎度 vs すまない «извини, виноват; спасибо, прости за хлопоты»: agree no pair, both ways. The shared «спасибо» sits in different whole clauses: thanks to a customer for repeat custom (no apology) vs an apology/apologetic thanks for trouble. Neither label is a defensible answer to the other prompt; EN has no pair. Medium-high. ありがとう, どうも, 御礼, 礼 are guarded; 感謝 «признательность; чувство благодарности» is unchanged EN parity; other leads (客, 毎日, 繰り返す, また…) are not defensible.

D. Integrity
- Blob comparison 8f4707c3→c4d64291: changed = manifest.json + 18 cards (汁, 水筒, 水平線, 水分, 元気でね, おだいじに, 公共, 民間, 歌謡, 民謡, 毎度, ステージ, 残らず, 歯車, 歯磨き, 正門, 正味, 欧米). 46f7089e→c4d64291 changed only manifest, 正味, 汁.
- The 12 unchanged new cards (水素, 水平, 気圧, いってらっしゃい, 気を付ける, 公衆, 毛皮, 比較的, 殻, 段階, いちいち, 死体) and 9 navigation files (kanji/圧; words/お帰り, 地平線, 垂直, 毛糸, 羊毛, 血圧, 西洋, 門) have identical blob IDs.
- In all 18 changed cards the ordered (label, target, image-flag) link sequence is identical; no link was added, removed or broken. Line counts are unchanged except 歯車 44→43 (deleted exclusions line).
- Manifest: key set unchanged; exactly 18 file hashes + contentVersion (d0a4ace9c128fa69→57ea12fc9026d94d) changed; all 18 equal raw SHA-256 of the c4d64291 blobs (no CR).
- validate.py: 0 errors. H1 = title for all 30 cards.

E. New defects introduced by either fix: none found in scope.

Optional:
- 正味–値 (pre-existing, EN parity, not introduced by the fixes): 正味:9 guards 価格 «цена; стоимость» and 値段 «цена», and L35 names that price overlap; 値 «цена (товара)» has the same basis but is unguarded (EN also lacks it). Appending 値 to 正味:9 would make the price guard set consistent. Low.
- 毎度–再三 (pre-existing, EN parity): «каждый раз» vs «снова и снова; раз за разом»; EN guards 毎度–たびたび/しばしば/よく for the "often" sense. A conservative append of 再三 is possible; necessity unproven. Low.
- ステージ–コンサート «концерт»: screened; a hyponym of «выступление на сцене», no EN pair; no action recommended.
- 比較的–比較: weak basis noted in B; keep or drop at the owner's discretion.

Limits:
- No web or dictionary re-fetch; dictionary-sense statements rely on card bodies, the original review and the dispositions.
- Title screens are heuristic (stem/regex). Whole-label judgments are mine. No app quiz run.
- Of the 30 cards, only the 9 listed were read in full. Others were checked via the cumulative diff and title/exclusion lines. Unchanged content relies on the original blind review.
- Did not check whether other RU cards transliterate 歌謡曲 like 歌謡:22 («каёкёку»).
- Correctness and Russian comprehensibility facets were not re-reviewed.
- No scratch files; R\scratch-consistency\ not used. Only this report was created (converted to LF after saving).

### comprehensibility — grok-4.7

Agent f1d023ab-411a-4c1e-8d43-3de1ba60c997, input c4d64291556bb0cc4ee7457febb567dea37df433, completed 2026-11-24T00:18:24.765Z; original report file SHA-256 19a3c9f195b3df580b780ff85beb9189c799d25fbbf1632e37bd544e33748469.

Snapshot: RU HEAD c4d64291556bb0cc4ee7457febb567dea37df433, tree d3da7587f2e91bbf74d80e9400d92e9e086ea62c; `git status --porcelain` empty at start and at finish. Frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f, read only via `git show`. This rechecker replaces the original comprehensibility reviewer (grok-4.7, agent 2d1a19ce…); it is not that report's author. Own model id not independently verifiable.

Scope: Russian comprehensibility of the cumulative learner-text change `git diff -U3 8f4707c36e5d79d004c808e633c03c2cfaa4ae11 c4d64291 -- words` (18 cards), not a new full-batch review. Read in full: `briefs/b255-brief-comprehensibility.md`; `originals/b255-review-comprehensibility.md`; `dispositions-comprehensibility.txt`; `words/汁.md`; `words/毎度.md`; `words/正味.md`; `words/おだいじに.md`; `words/残らず.md`; `words/正門.md`. Changed line plus surrounding learner context: `民謡.md` 1–40; `歌謡.md` 1–30; `公共.md` 25–45; `民間.md` 25–42; `元気でね.md` 1–28; `水分.md` 1–30; `歯磨き.md` 1–28; `水筒.md` 28–42; `垂直.md` 15–35 (optional, unchanged). Exclusion-only front matter: `ステージ.md` 1–15; `水平線.md` 1–15; `歯車.md` 1–15; `欧米.md` 1–15. Rules actually read: `.github/copilot-instructions.md` learner-language opening; `content-structure.instructions.md` word title/H2 section (about lines 123–175); `docs/translation-methodology.md` glossary and cross-language boundaries (lines 130–165). Sources treated as data: JMdict captures `正味.json` 1377980 and `汁.json` 1335520; EN `words/正味.md` and `words/毎度.md` at 6af98cb; Weblio Digital Daijisen 正味 sense 4, 汁 しる senses 1 and 3, 掛け値 sense 1. No validator. No native-speaker or learner test.

Verdicts: Russian comprehensibility of the original candidate, as reported by the earlier reviewer: NEEDS FIX. At c4d64291, within this recheck scope: CLEAN.

Findings:
F1; resolved; was medium; `words/おだいじに.md:16`; «а также скорее поправиться» adds the recovery wish and no longer withdraws «беречь себя». Title/H1 stay «берегите себя; поправляйтесь». The example «Берегите себя» is one contextual reply, not a clash with a corrective definition. Evidence: card lines 4, 13, 16, 20. Confidence: high.
F2; resolved; was low; `words/民謡.md:33`; «тоже связано…, но само не означает песню» removes the «разделяет связь» inversion. Neuter «связано» agrees with «само». Evidence: line 33 and the preceding 歌謡 bullet. Confidence: high.
F3; resolved; was low; `words/歌謡.md:22`; «кайёкёку» is now «каёкёку», the prescribed aid (か, not かい). Kana かようきょく remains in the same sentence; line 26 still says to keep long よう. Confidence: high.
F4; resolved; was low; `words/毎度.md:28`; «в каждом случае» is grammatical prepositional. The shorter gloss is the accepted form; the title already has «каждый раз». Evidence: lines 4, 13, 28. Confidence: high.
O1; optional; n/a; `words/垂直.md:29`; «горизонтальный, ровный» unchanged and absent from the cumulative words diff. Still non-blocking. Confidence: high.
O2; optional; n/a; `words/正門.md:27`; «не прямой» not added. Line 27 still blocks «правильными» and says which gate is meant. Confidence: high.
O3; resolved; was optional; `words/汁.md:4,16`; the plant/fruit narrowing is gone. The replacement was reviewed below and is not a new defect. Confidence: high.

Changed learner lines at c4d64291; no new defect:
- 汁 title/H1 «выжатый или выделившийся сок; бульон; суп» match. As a bare label the participles modify only «сок»; «бульон; суп» are separate senses. Body :16 restates that without a plant limit. :20 «Суп горячий…» is a situational gloss of 汁が熱い; the next sentence says 汁 itself does not mean «горячий». :42 «сок» and «бульон, суп» agrees with the title heads. Daijisen しる① (liquid made to seep out or squeezed out) and ③ (味噌汁 and similar 汁物) support the broader label; «суп» correctly replaces narrower «похлёбка». «выделившийся» is a fair learner compression of しみ出させ, not a false Russian sense.
- 毎度 title/H1 «каждый раз; спасибо, что снова выбираете нас (клиенту)» match and work as bare labels. The first segment is the frequency sense; the parenthesis marks the shop-to-client formula. :20 uses the same Russian for 毎度ありがとうございます, a natural equivalent of continued custom, not an English calque. :18 still explains repeated purchases and visits.
- 残らず:27 «непереходного… буквально «так, что ничего не остаётся»» is clear. «оставаться» and the later 残す contrast carry the point; «непереходный» is ordinary school terminology. Examples still say «без остатка» / «без исключения».
- 公共:36 keeps the hedges «обычно» and «иногда». «создано и содержится местными властями» is a readable parallel; elliptical «частным» is recoverable as private institutions.
- 民間:34 is clear: private persons or non-state organizations create and maintain the institution; it is not a general word for any civic or folk practice.
- 正味:35 «фактическая цена продажи без завышения в расчёте на торг; закупочная цена» matches Daijisen 正味④ (掛け値のない値段; 仕入れの値段) and 掛け値① (a price set above the real selling price in anticipation of haggling). «без завышения» blocks an inverted reading. Dense, but this is a recognition note, not the quiz title («вес нетто; чистое количество», unchanged). The prompt listed :9; the cumulative diff does not change line 9 (tags).
- 元気でね:19 «Давай ещё встретимся» matches inclusive また会おう and the friendly register of the title.
- 水分:22 «пить жидкость; речь не обязательно о простой воде» matches the preceding «пейте достаточно жидкости» and does not collapse the sense to plain water.
- 正門:20 «Пока идут строительные работы…» is a natural contextual gloss of 工事中; «главными воротами» matches the title.
- 歯磨き:20 «нанёс… на щётку» matches つけました without the extra «выдавил»; next to «зубную пасту» the brush is unambiguous on this card.
- 水筒:36 «В 水筒» is the ordinary preposition; the sentence is clear.
- Exclusion lines in ステージ, 水平線, 歯車 and 欧米 are YAML id lists or a removed key only. No learner prose.

Optional: none new. O1 and O2 remain optional and were not applied.

Limits: Japanese correctness and quiz-exclusion consistency were not re-reviewed; no clear out-of-facet defect noticed. The other 12 new cards and the nine navigation files were not reread, except `垂直.md` 15–35. The Polivanov table was not re-fetched; F3 was judged against the prescribed string, the kana in the same sentence, and standard Polivanov values (か ка, よう ё, きょ кё, く ку). No audio, validator, native-speaker, or learning-effectiveness claim. Dispositions were checked against the files, not taken as facts. No scratch files written.

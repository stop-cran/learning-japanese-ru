## Independent read-only review

**Snapshot:** HEAD `043bc0c704cc92e19d65426f84e27e454e788ccd` plus the current worktree changes; source `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. I made no edits, staging, commits, messages, or publication actions.

### C1 — Japanese correctness and source fidelity
**Verdict:** Fidelity to the frozen source is verified; independent factual confirmation is **partial / UNVERIFIED**. No Japanese-content defect was substantiated.

I read all 10 complete Russian kanji lessons and all 10 complete frozen-source English lessons: `熱`, `疲`, `痛`, `眠`, `状`, `点`, `然`, `破`, `犯`, `石`. The Russian `kanji`, `jlpt`, `tags`, stroke count, radical/number, on/kun readings, and distractor IDs match the source across all 10. I compared the Japanese text and checked all **11 example sentences** against the source; they are unchanged.

I read the supplied KANJIDIC2 capture’s **5 complete records**: `石`, `然`, `点`, `破`, `犯`. Their recorded strokes, grade, classical radical, readings, and legacy JLPT value match the candidate/source metadata. The other five characters (`熱`, `疲`, `痛`, `眠`, `状`) are not in that capture; their fields were compared with the frozen source, not independently confirmed against a raw KANJIDIC2 record. Candidate N3 labels are explicitly identified as the community list, so the capture’s legacy JLPT `2` is not treated as a contradiction.

I read the JMdict capture’s **15 complete entries and exact matched queries**: 点/てん, 百点/ひゃくてん, 偶然/ぐうぜん, 自然/しぜん, 当然/とうぜん, 破る/やぶる, 破れる/やぶれる, 破壊/はかい, 犯人/はんにん, 犯罪/はんざい, 犯す/おかす, 容疑者/ようぎしゃ, 石/いし, 石油/せきゆ, 宝石/ほうせき. The matched readings and senses support the cited lesson uses (e.g. 点’s mark/score/aspect senses, 破る’s “tear/rip,” 犯す’s commit/violate senses, and 石’s stone/rock sense). I noted alternate forms `遇然` (marked `sK`) and `当前` (marked ateji/`rK`); neither is used in the candidate. The records do not cover the JMdict citations for `熱`, `疲`, `痛`, `眠`, or `状`, so those claims remain source-matched rather than independently capture-confirmed.

All ten stroke assets were compared against the frozen-source Git blob IDs; **10/10 matched**.

### C2 — Scope, closure, links, quiz semantics
**Verdict:** File/link structure checked; ordinary quiz semantics remain **UNVERIFIED**.

The 13 modified word pages were reviewed by their complete changed hunks and surrounding context. Each change only wraps an existing kanji mention in a link to its new card; no other page text changes appear. The 13 targets exist. All **46 relative Markdown links** in the new kanji lessons resolve, and all **30 distractor IDs** point to existing kanji cards.

The five source-linked example word pages `状態`, `偶然`, `破る`, `破れる`, and `犯人` are absent from this RU tree. Their Japanese terms remain in the lessons without dangling RU links; this is a partial word-page closure, not a confirmed defect in the stated batch scope.

I did **not** resolve the 30 direct distractor directions; card existence or differing titles is not evidence that an option is semantically unsafe/safe. The unresolved pairs are:

- 熱 → 点, 黒, 然; 疲 → 痛, 病, 破; 痛 → 通, 用, 同
- 眠 → 目, 銀, 服; 状 → 犬, 大, 犯; 点 → 店, 黒, 熱
- 然 → 熱, 点, 犬; 破 → 疲, 研, 石; 犯 → 犬, 状, 兄
- 石 → 右, 口, 古

The manifest diff records `contentVersion: d8a791473ae509d9` and the new card/stroke entries. I did not rerun its generator or treat manifest data as semantic evidence.

### C3 — Russian comprehensibility
**Verdict:** No specific comprehension defect was substantiated in the complete lesson bodies read. This is a text-level reviewer assessment only—not native-speaker certification or a learning-outcome claim.

### Findings, optional items, and limits
**Supported findings:** None; therefore no severity, correction, or confidence entry applies.  
**Optional / unresolved scope:** The five absent source-linked word pages above; adding them would be separate scope.  
**Limits:** Quiz semantics for all 30 directions; independent KANJIDIC2 confirmation for five characters; cited JMdict claims outside the supplied capture. No app/device/media/release review or full-translation assessment was performed. No validator or tests were run.

### Exact read coverage
- Complete RU lessons: `kanji/熱.md`, `疲.md`, `痛.md`, `眠.md`, `状.md`, `点.md`, `然.md`, `破.md`, `犯.md`, `石.md`.
- Complete frozen-source lessons at the cited SHA: `kanji/熱.md`, `疲.md`, `痛.md`, `眠.md`, `状.md`, `点.md`, `然.md`, `破.md`, `犯.md`, `石.md`.
- Changed hunks plus surrounding context for: `words/交差点.md`, `全然.md`, `句読点.md`, `点.md`, `然る.md`, `熱.md`, `熱い.md`, `疲れる.md`, `症状.md`, `痛い.md`, `眠い.md`, `眠る.md`, `石.md`.
- Both supplied capture files: `ru-131-dependency-kanjidic2-capture-001.json` and `ru-131-dependency-jmdict-capture-001.json`.
- Review rules read: `.github/copilot-instructions.md` (source/evidence, report and quiz-review sections); `.github/instructions/content-structure.instructions.md` (kanji, links, distractors and word sections); `docs/translation-methodology.md` (workflow/invariants); `docs/content-format-reference.md`; and all three specified reviewer-agent instructions.
- The worktree also contains untracked `tools/__pycache__/` files, outside the stated runtime candidate; they were not modified or reviewed.

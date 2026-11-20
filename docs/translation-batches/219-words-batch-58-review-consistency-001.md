# B219 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `f72537721d86b0d72485aecb4a758b10ef241a20` (tree `ea1be965b31c1cc36dc04bbe0cacaaacc3b3e6b5`),
> the signed candidate pushed before review.
> Later reconciliation is in `219-words-batch-58-recheck-001.md`.

Snapshot: f72537721d86b0d72485aecb4a758b10ef241a20 (RU checkout; `git status --porcelain` empty, no uncommitted changes). EN comparison base: learning-japanese-en-frozen 6af98cb.
Scope: Consistency and quiz-safety facet of batch 219 (219-words-batch-58). Read in full: the 30 new words/*.md cards and the diffs of the 18 navigation files (kanji 互/仏/務; words 以来, 元, 噂, 大使, 天然, 延期, 強調, 暮らし, 現実, 生命, 神, 見送り, 計算, 説, 過去). Also checked: manifest.json (hashes), the intake JSON (paths only), `tools\validate.py` (0 errors). Coordinator tools (title screen, link parity) used only as leads. Reviewer model identity cannot be verified from inside this session. No repository files were modified.
Verdicts:
- Consistency: CLEAN
- Scoped coverage (link/manifest/intake integration): CLEAN
- Quiz safety: CLEAN
- Comprehensibility: not assigned (not reviewed)
Findings: None.
- Front matter (word, reading, type, kanji, jlpt, tags) is identical to EN for all 30 cards.
- All EN `quiz_exclusions` are retained; RU lists are supersets.
- Body links equal EN except six RU-only links, each introduced or compared substantively, with existing targets: 代理→本人, 今回→最近, 今にも→今に, 事務→事務所, 予報→天気予報, 主に→だけ.
- EN-only links stay plain text because the RU targets do not exist: 交際→デート, 世間→世の中, 予算→kanji 算, 予測→kanji 測. Absence was confirmed.
- All 18 nav files are prose-identical to their parents once links are stripped. Path forms are correct (`../words/X.md` in kanji, `X.md` in words). Link counts for every batch word match EN across all existing RU files (0 mismatches). Nav lines: 互 21/34/43, 仏 32/36, 務 21/33/43.
- The 以来→今後 link, held in the previous batch, is now restored and is the only change to that card.
- manifest.json: contentVersion changed 9bd4efcc… → bc7ef195…; changed and new file hashes match.
- Intake JSON: 48 payload paths (30 + 18) equal the commit's content diff exactly; held = 0; no learner content. The commit has 50 files, with no generated or unrelated files.
- No exact title-segment duplicates among answer titles beyond 中学 vs 中学校, which is guarded.
Quiz-safety guard classification (RU additions beyond EN; pairs are direct and not transitive; reverse declarations not required). No unjustified guard and no missing required guard found.
- Required, with a basis in the dictionary or the visible Russian titles:
  - 以前→先, 以前→過去
  - 今にも→もうすぐ
  - 代表→典型
  - 代理→代わり
  - 付き合い→関係, 付き合い→仲
  - 人生→生命
  - 今回→度, 今回→場合
  - 人込み→混雑
  - 主張→見解
  - 主に→大半, 主に→大部分
  - 事務→仕事
- Conservative (real basis, necessity unestablished, harmless):
  - 以前→元, 以前→まず
  - 今後→将来, 今後→先
  - 今にも→今に
  - 人生→生, 人生→生活
  - 交際→恋, 交際→連絡
  - 主要→要点
  - 主義→思想
  - 主張→要求
  - 主に→主要
  - 中止→止める, 中止→止む
  - 交際→関係, 交際→仲
  - 予測→予期, 予測→読み, 予測→天気予報
  - 予報→予測, 予報→予想, 予報→天気予報
  - 乗せる→置く (EN)
Optional (nonblocking, weak; none established as defects):
- 主に vs たいてい («обычно; большинство»): 大半 and 大部分 declare たいてい, but 主に does not.
- 以前 vs 昔.
- 主要 vs 中心.
- 世間 vs 人.
- 今後 vs 未来.
Limits:
- 110 strokes/*.json files showed hash mismatches in a working-tree check. This commit does not touch them, and the cause is likely a line-ending artifact, but the `git show HEAD:` re-check did not complete, so it is unconfirmed.
- Dictionary evidence came from jisho's rendering of JMdict, not entry-by-entry source reading.
- Comparison with EN body text was by links, front matter and structure only. Prose accuracy and comprehension belong to the other facets.
- No Cyrillic transcription convention was found in the RU instructions; the cards use kana readings only.
- Whether 混雑's body mentions 人込み was not checked.

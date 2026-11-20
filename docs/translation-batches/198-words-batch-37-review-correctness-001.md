# B198 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `c82e94b30d2c72c36fb56406ba2aaaf1f54e0002`, staged in a scratch worktree at detached
> HEAD `5dd9a78` while commit signing was unavailable. No commit of this tree exists.
> Later reconciliation is in `198-words-batch-37-recheck-001.md`.

Snapshot: RU candidate TREE c82e94b30d against reviewed base TREE ea3a478, in C:\Users\romanko\repos\learning-japanese-ru-b198; detached HEAD 5dd9a78f4e6d2f806be09953326bf77cb8e77c47. Candidate is staged, not committed. Initial and final git diff-index --cached --quiet c82e94b30d and git diff --quiet all exited 0; initial/final untracked listings were empty. Frozen EN HEAD verified as 6af98cb717755690a9ca793e5454a96ebd7a8f9f.

Scope: Independent blind, read-only CORRECTNESS and SCOPED COVERAGE review. Actual model identity/version is not independently verifiable from the available execution context; no model-specific claim is made.

Read all 30 new cards completely against their complete frozen EN originals:
words/{笛,章,立ち上がる,空き,穴,積極的,積む,積もる,穀物,稼ぐ,根,種,税金,税,移動,動かす,移す,秒,科目,禁煙,禁止,祭,神経,神,祝う,祝い,礼儀,感謝,礼,確認}.md.

Read every baseline-card change in the candidate diff: kanji/{明,積}.md and words/{人間,制限,実,恩,瞬間,芽,苗,行儀,記念,許可,道徳}.md. These changes add navigation links without changing the existing teaching text.

For comparison, read complete current RU cards お祭り, お祝い, 御礼, 恩, 行儀, 動く, 移る, 写す, 原因, 実, 証明, チェック, 調べる, 確か, 暇, 立つ, 起きる, 上がる, 働く, 料金, 代金, 費用, 米, 稲, 食料. Inspected titles/readings, not complete bodies, for the remaining adjacent comparison words listed in the assignment. Read the three binding RU instruction/format files in full. Did not read the prohibited batch records, tracking file, author material or other reviewers' reports.

Verdicts:
- CORRECTNESS: CLEAN for all 30 new cards and the reviewed baseline changes.
- SCOPED COVERAGE: CLEAN for all 30 new cards and the reviewed baseline changes.

Findings: none. No actionable defect established within these two facets.

Evidence and checks:
- Compared every example and its Russian translation, and the explanatory constructions, including polarity, event stage, transitivity and participant roles. All 60 Japanese example sentences remain present verbatim; checked their readings against the source in the complete paired reads. Delimiters/layout are localized to the established RU full-width-parenthesis convention; this does not change Japanese wording or kana.
- Source word/readings, JLPT, type, kanji and tags are unchanged; every original direct quiz exclusion is retained. Additional exclusions are outside this review's quiz-safety assignment.
- All source-taught senses, example material and Japanese teaching distinctions remain represented. Removed English-only ambiguity discussions (such as ordinal “second,” “have the nerve,” and English “corn”) do not remove a Japanese rule needed by these Russian explanations.
- Checked removed source links individually: all point to cards absent from this RU tree; their Japanese labels/meaningful comparisons remain as plain text, with readings where needed. No removed source link to an available RU target was found. All original dictionary citations and cited sense selections remain.
- Independently retrieved and read exact Jisho/JMdict lexical entries, including forms/readings, sense-local tags/restrictions and parts of speech, for every one of the 30 new words; ignored Wikipedia-definition objects and unrelated homonyms. Also inspected the separate entries 神経を使う and 礼儀正しい. In particular: 積もる's taught accumulation sense is intransitive godan; 移動 permits both transitive/intransitive する; 移す's illness sense carries the kana-usual tag; 空き lists 明き without a sense restriction across the taught uses; 種's たね entry separates seed, cause/source and conversational material from the distinct しゅ entry.
- Actual inspected entry endpoints include:
  https://jisho.org/api/v1/search/words?keyword=祭
  https://jisho.org/api/v1/search/words?keyword=祝い
  https://jisho.org/api/v1/search/words?keyword=礼
  https://jisho.org/api/v1/search/words?keyword=移す
  https://jisho.org/api/v1/search/words?keyword=積もる
  https://jisho.org/api/v1/search/words?keyword=空き
  https://jisho.org/api/v1/search/words?keyword=種
  Other entries were retrieved through the same endpoint using each exact headword above. These live API inspections corroborate meanings; they do not establish frequency or independently authenticate the frozen source's numeric JMdict IDs.
- For 穀物, additionally inspected the actual 改訂新版 世界大百科事典 and 日本大百科全書 entries by 星川清親 at https://kotobank.jp/word/穀物-64302: the category includes crops and their edible seeds. An earlier attempted URL redirected to an unrelated 国際放送 entry and was rejected as evidence.
- Ran python -X utf8 -B tools\validate.py directly in the candidate worktree: exit 0, “0 error(s).” Independently compared LF-normalized SHA-256 values for all 43 changed content files with their manifest entries: all matched. Manifest language envelope remains schema 2, ru → ja. Did not run a writing generator.

Optional: words/穀物.md:38 could stay closer to EN's non-exclusive phrasing: “穀物 называет зерно или зерновые культуры; само слово не обозначает именно готовые хлопья к завтраку.” This avoids leaning on “как сырьё” as a definition of every use. The current surrounding explanation already includes crops, and no consequential wrong example or scope loss was established; this is nonblocking precision, not a finding.

Limits: CLEAN means no established actionable defect in the assigned scope, not exhaustive linguistic certification. Comprehensibility, complete quiz-pool safety and broader consistency were not assigned and receive no verdict here. No full-body review is claimed for comparison cards inspected only by title/reading. Did not independently reconstruct kanji etymology, verify modern usage frequency, or authenticate every cited numeric dictionary ID; retained Japanese facts were checked against the reviewed frozen EN source and the actual lexical entries noted above. No native-speaker, app/device, archive-delivery or learning-effectiveness testing. Repository HEAD/index/worktree remained unchanged; only this report was written.

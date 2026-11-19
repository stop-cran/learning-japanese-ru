# Batch 187 — blind correctness and scoped-coverage review

## Snapshot

- Reviewed 2026-11-19.
- RU repository: `C:\Users\romanko\repos\learning-japanese-ru`.
- Branch: `full-ru-187-words-26`.
- HEAD/base: `cc6b8f13ebceb4be3a1b13194f53efa9e27e0bc9` (`cc6b8f1`).
- Staged tree: `1597f0853220fbaeb521bab731c807b81e62373e`, confirmed by `git write-tree` before and after review.
- Frozen EN: `C:\Users\romanko\repos\learning-japanese-en-frozen`, HEAD `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. Intake source hashes were checked against Git blobs at this exact commit.
- Actual serving model identifier is unavailable to this reviewer. Requested identity was GPT / `gpt-6.1-sol`; that request is not independent verification of the serving model.
- Blindness: no author report, author prompt, or other reviewers' reports were read. Intake was inspected as scope/hash evidence, not as an author correctness argument. No delegation.

## Scope

All **30/30** new articles were read completely in RU and compared with their exact frozen EN counterparts, including front matter, constructions, Japanese examples and kana, Russian translations, comparisons, qualifications and dictionary citations:

`words/離す.md`, `words/雇う.md`, `words/集団.md`, `words/集中.md`, `words/会.md`, `words/会合.md`, `words/集まり.md`, `words/隠れる.md`, `words/隠す.md`, `words/障害.md`, `words/回.md`, `words/度.md`, `words/際.md`, `words/陰.md`, `words/限界.md`, `words/守る.md`, `words/防ぐ.md`, `words/関連.md`, `words/関心.md`, `words/関する.md`, `words/誤り.md`, `words/間違い.md`, `words/始まり.md`, `words/開始.md`, `words/閉じる.md`, `words/長期.md`, `words/鎖.md`, `words/鍋.md`, `words/鋭い.md`, `words/鋏.md`.

All **17/17** navigation-only changed Markdown files were read, and every patch inspected for correct destination and preservation of surrounding meaning:

`kanji/団.md`, `kanji/守.md`; `words/ぼんやり.md`, `words/仕舞い.md`, `words/利口.md`, `words/団体.md`, `words/対する.md`, `words/感心.md`, `words/永久.md`, `words/破る.md`, `words/約束.md`, `words/紐.md`, `words/組織.md`, `words/表す.md`, `words/達する.md`, `words/違い.md`, `words/離れる.md`.

Also reviewed `manifest.json` and `docs/translation-batches/187-words-batch-26-intake.json`: **49 changed paths total**.

Applied RU `.github/copilot-instructions.md`, `.github/instructions/content-structure.instructions.md`, README approach and `docs/content-format-reference.md`; the requested RU `docs/content-format.md` does not exist. Used the referenced exact frozen EN `docs/content-format.md`, particularly repository language, kanji/quiz and word contracts, plus `docs/jlpt-levels.md` vocabulary policy.

### Source verification and scoped checks

- Inspected actual exact-word Jisho dictionary API entries for all 30 words, including forms, lexical senses, parts of speech, restrictions and usage information. Endpoint: `https://jisho.org/api/v1/search/words?keyword=<word>` with the Japanese word URL-encoded. Six initially rate-limited requests succeeded on subsequent retrieval. Homographs, name entries and “Wikipedia definition” blocks were not treated as lexical evidence.
- Matched the frozen `docs/n3-vocabulary-sources.tsv`: 31 N3 source rows map to these 30 articles, including separate たび/ど entries for 度. All 30 `jlpt: 3` labels retain their sourced article-level classification; none was inferred from kanji levels.
- Checked unchanged 団/守 metadata against actual [団 API](https://kanjiapi.dev/v1/kanji/%E5%9B%A3) and [守 API](https://kanjiapi.dev/v1/kanji/%E5%AE%88) responses. Jisho kanji entries confirm their radicals; the radical tables [31](https://en.wikipedia.org/wiki/Radical_31) and [40](https://en.wikipedia.org/wiki/Radical_40) confirm 囗/宀 numbering. Mnemonics were not treated as historical evidence.
- All 47 intake payload paths exactly match the changed Markdown set; all candidate raw, source raw and source LF-normalized SHA-256 values match. The intake's earlier baseline `acef99457c635222a5a38da49b9724da98d58cf8` is an ancestor of the supplied review base, not an unexplained replacement snapshot.
- All scoped relative Markdown links and declared quiz-reference targets exist. All 30 direct frozen-source quiz-reference edges are retained. The mechanically traversed RU quiz-reference closure contains 723 cards / 1,940 directed declarations, with no missing target. This is reference integrity, not a semantic review of those 723 cards.
- Manifest equals an in-memory call to the existing `build_manifest` function: content version `157cf612e0e30e3d`; 30 added and 17 changed `files` entries; no removals; image/scene maps unchanged. The generator's writing entry point was not run.
- Actual command `python -X utf8 -B <RU>\tools\validate.py` completed, exit 0: `0 error(s)`.

## Verdicts

| Facet | Verdict | Boundary |
|---|---|---|
| Correctness | **NEEDS FIX** | Two confirmed instructional errors below. |
| Scoped coverage / prerequisites | **CLEAN** | All requested cards, navigation changes and intake/manifest entries included; no required reference or source-row omission established. This does not certify the whole curriculum. |
| Russian comprehensibility | **UNVERIFIED** | Not assigned as a full facet; translations were examined for correctness, not comprehensibility acceptance. |
| Quiz safety | **UNVERIFIED** | Reference integrity and preservation checked; no exhaustive semantic answer-pool or fallback review. |

## Findings

### F1 — P2 / medium; correctness; `words/集中.md:26–27`

**Claim:** In the transitive example 注意を一点に集中する, “を обозначает то, на чём сосредотачиваются”.

**Defect / learning impact:** This assigns を the role of the target of concentration. Here 注意 is the attention being directed; 一点 is the target, marked に. The Russian phrase “то, на чём сосредотачиваются” describes the latter role and contradicts both the example's correct translation and the following explanation of に. Learners can consequently select the wrong particle for the focus.

**Remedy:** Say, for example, “を обозначает то, что сосредоточивают (здесь — внимание), а に — то, на чём его сосредоточивают / цель сосредоточения.”

**Concrete evidence:** The frozen EN `words/集中.md:20` distinguishes “what is focused” from “where”. The inspected [JMdict/Jisho entry](https://jisho.org/api/v1/search/words?keyword=%E9%9B%86%E4%B8%AD) recognizes transitive and intransitive uses. More directly, Shogakukan's Digital Daijisen entry [焦点を絞る](https://kotobank.jp/word/%E7%84%A6%E7%82%B9%E3%82%92%E7%B5%9E%E3%82%8B-532619) defines it as “注意や関心を、一点に集中させる”: attention/interest is directed to one point. Actual entry text was read.

**Confidence:** High. **Status:** unresolved; no edit made.

### F2 — P2 / medium; correctness; `words/際.md:46–49`

**Claim:** 来た際に “относится к случаю уже совершённого прихода”, contrasted with 来る際に introducing an upcoming visit.

**Defect / learning impact:** This presents the た-form as establishing an already accomplished visit without qualifying the reference time. A visit expressed by 来た際 can still be prospective relative to speaking: the arrival is viewed as completed at the relevant occasion. The current past-versus-upcoming contrast can make learners reject valid instructions about a future visit. The frozen EN wording merely says “a visit expressed with 来た”; it does not add the Russian assertion of an already accomplished arrival.

**Remedy:** Explain that the form helps locate the event relative to the relevant occasion, but た際 does not by itself mean “before now”. Allow a future-context example and let the whole sentence establish actual timing.

**Concrete evidence:** The inspected teaching entry [「際」「際に」の例文・文法解説](https://japanese-language-education.com/for-overseas-learners/sai/) explicitly gives “京都に来た際は、ぜひ清水寺に行ってください” and translates it “When you come to Kyoto, be sure to visit Kiyomizu Temple.” It lists both Vる and Vた attachments. A second inspected teacher reference, [N1et: 際(に/は)](https://jn1et.com/saini/), gives prospective “台風が来た際には、避難勧告に従って安全な場所に避難してください.” These are instructions for the relevant possible occasion, not assertions that the arrival already occurred before speaking.

**Confidence:** High. **Status:** unresolved; no edit made.

## Optional

None raised within the assigned facets. No finding is based solely on editorial taste or an alternative acceptable translation.

## Limits

- No native-speaker consultation, app import, device testing, learner testing or corpus-frequency study was performed. Dictionary evidence does not independently attest every full example sentence; sentence-level grammatical/translation judgments also use reviewer analysis.
- Navigation patches are link-only; this is not a new acceptance review of every inherited, unmodified baseline claim.
- The new words retain all 33 distinct written kanji in metadata. Ten do not yet have RU kanji cards: 鋏・鋭・鍋・鎖・防・陰・障・隠・雇・離. The word contract permits this; absent optional kanji/comparison articles were not invented as mandatory prerequisites.
- Full quiz safety, including all Russian-label overlaps, new exclusions' semantic necessity and automatically selected fallback options, remains UNVERIFIED.
- Failed/irrelevant source retrievals were discarded, not used as evidence. In particular, an initial Kotobank numeric URL resolved to 充当 rather than 集中; only the subsequently located and read relevant entries support the analysis.
- Both repositories were left unchanged. Initial and final RU porcelain status match exactly: 49 staged changes plus pre-existing untracked `tools/__pycache__/`. No cleanup was attempted. Final branch, HEAD, frozen EN HEAD and staged tree match the snapshot above. Only this requested external report was created.

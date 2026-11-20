# B201 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `6e8f38856e4b35ab1e3322e0c66d6e16c5c39c43`, staged in a scratch worktree at detached
> HEAD `5dd9a78` on top of the reviewed Batch 200 tree `00107e1` while commit signing was unavailable.
> No commit of this tree exists. Later reconciliation is in `201-words-batch-40-recheck-001.md`.

Snapshot: RU scratch worktree C:\Users\romanko\repos\learning-japanese-ru-b198, candidate tree 6e8f38856e4b35ab1e3322e0c66d6e16c5c39c43 vs base 00107e1. `git diff-index --cached --quiet` = 0, `git diff --quiet` = 0, `git ls-files --others --exclude-standard` empty: index and worktree equal the candidate. No uncommitted changes beyond the staged tree. Frozen EN 6af98cb.

Scope: All 30 new word cards read in full against their frozen-EN front matter/structure; 14 navigation-only restorations (diff -U0); manifest.json diff. Facets: consistency, quiz safety, cross-file integration. Tools run: `tools/validate.py` (0 errors), `tools/build_manifest.py --check` (exit 0, 4149 files), `link_parity.py` on the 30 cards (no issues), plus an ad-hoc EN-vs-RU link-count comparison for every link to a new word in all EN kanji/words/articles files (no discrepancies, no RU-only links). RU titles of every word card were screened by Russian-word overlap. Reviewer model not verifiable from inside this session. Dictionary evidence for added guards was checked against jisho.org's JMdict mirror for 嫌 and 無し only; the rest rests on card text and the RU/EN titles.

Verdicts:
- Consistency: CLEAN. Front matter matches EN (tags, kanji, jlpt, type); all EN quiz_exclusions retained; the 14 restorations change only link brackets/hrefs at EN link positions; manifest hashes fresh; no generated files.
- Quiz safety: NEEDS FIX (two missing direct guards, F1 and F2; both Minor). No EN exclusion lost.
- Scoped coverage of cross-file integration: CLEAN (every EN link to a new word has an RU counterpart; no Russian-only links).

Findings:
- F1; Minor; quiz safety; words/現状.md:9; missing guard 現状↔様子. 様子 «положение дел; облик» (an existing card that every sibling situation card already guards) is a defensible answer for 現状 «нынешнее положение; статус-кво», and the 現状 body itself glosses it «нынешнее положение дел». Not an EN pair, but created by the Russian titles. Remedy: `quiz_exclusions: [状態, 状況, 事態, 様子]`. Evidence: RU 様子 title and the RU 状態/状況/事態 lists all include 様子. Confidence: medium.
- F2; Minor; quiz safety; words/無.md:9 (or words/ノー.md:10); missing guard 無↔ノー. Titles «не-, без- (приставка); небытие» and «нет; без (в составе слов)» both teach prefix «без», and both bodies show prefix use (ノーネクタイ vs 無作法, 無事). Not an EN pair. Remedy: `quiz_exclusions: [無し, ノー]` on 無 (one side suffices). Evidence: the two titles and bodies. Confidence: medium.
- F3; Minor (optional cleanup, not blocking); quiz safety; words/無し.md:9; guards 無し→いいえ, いえ, 否 are unjustified. The 無し title is «без; отсутствие» and jisho/JMdict 無し senses are "without" / colloquial "unacceptable" / archaic "nonexistent"; no sense of "no". The Russian «нет» is discussed only in the body. Remedy: either `quiz_exclusions: [ノー]` (EN) or keep the extras as harmless distractor-pool loss. If a guard for the colloquial それはなし sense is wanted, だめ («не годится; нельзя») is the better target. Confidence: medium-high that these three pairs are unnecessary; low that anything breaks.

Classification of every exclusion beyond EN (EN-retained: 現状×3, 現場, 王→王様, 率, 独身, 犯罪→罪, 物語→話, 父親, 無事→安全, いえ, 否×3, ノー×3, 無し→ノー: all present):
- 物語→歴史: real basis (Russian «история» also means "story", taught in the body; JMdict 物語 "tale; story"); conservative/near-required.
- 物語→語る: «повествование» vs «повествовать» share stem; conservative.
- 物質→布: required (JMdict 布 "cloth"; RU 布 «ткань; материя» and 物質 «физическая материя» share a Russian word).
- 物事→こと, 物: required (title «дела и вещи» spells out both neighbours' glosses «дело», «вещь»).
- 燃える→焼ける: required (гореть/сгорать; JMdict 燃える "to burn", 焼ける "to burn; to be roasted").
- 熱中→ねっしん: required (shared стем «увлечённ-»; noun vs adjective of the same root 熱).
- 無事→大丈夫: required («цел и невредим» vs «в порядке»; JMdict both include "safe/all right"; 安全→大丈夫 already guarded).
- 無事→幸福: required (shared «благополуч-»).
- 否→嫌: conservative (JMdict 嫌 has the interjection sense "no!/quit it!" with the same reading いや; the RU 嫌 title has no «нет», so necessity unestablished).
- 無し→いいえ, いえ, 否: unjustified (F3).
- 無→無し: required (shared «без», same kanji; body explains).

Checked and judged no guard required (no defensible shared answer): 現場 vs 場所/所/場/会場/事件 (title is the specific «место происшествия; рабочая площадка», 場面 guarded), 王子 vs 息子, 独立 vs 一人/自由/支配, 犯人 vs 泥棒/罪/犯罪, 物価 vs 値段/価格/値/料金/費用, 物理 vs 科学/生物/数学/地理, 爆発 vs 火事/火, 煙 vs 霧/禁煙/たばこ («дымка» vs «дым» differ), 無視 vs 尊重/重視 (contrasts), 無料 vs 料金/安い/自由, 寧ろ vs より/いえ/ノー/反対, 父親 vs 親/祖父/主人, 熱中 vs 集中, 熱帯 vs 熱/暑い/熱い, 現状 vs 現在/現実.

Optional:
- 父親 vs 親 share the gloss «родитель»; the title «отец (как родитель)» is explicit about «отец», so no guard is required. Left to the author.

Limits: No native review of the Japanese; linguistic correctness and comprehensibility are other reviewers' facets. Dictionary senses for guards other than 嫌/無し come from the cards' own JMdict citations and EN/RU titles, not fresh entry inspection. Batch records and the ledger were out of scope. `__pycache__` was not created in the worktree.

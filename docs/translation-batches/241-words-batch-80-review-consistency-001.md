# B241 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `5e43b26c27b09f0e00c766db801c20954a827654` (tree `81db4ea431574bf2d6d8de974150fd4ffa35bdf0`),
> the signed candidate pushed before review.
> Later reconciliation is in `241-words-batch-80-recheck-001.md`.

Snapshot: RU repo `C:\Users\romanko\repos\learning-japanese-ru`, `git rev-parse HEAD` = `5e43b26c27b09f0e00c766db801c20954a827654` (as specified). `git status --porcelain` was empty at start. Running `tools/validate.py` created an untracked `tools/__pycache__/`; I deleted it, and status is empty again. No tracked file was changed, and I did not run `build_manifest.py` as a writer. Frozen EN `6af98cb` was used as the source. No uncommitted changes remain.

Scope: Facets CONSISTENCY and QUIZ SAFETY plus cross-file integration. Model: not verifiable from inside the session.
Read in full (front matter and body, RU) and compared with EN front matter and links by script:
- All 30 new cards `words/`: いきなり あわただしい さっさと 至急 自衛 稽古 自習 自然科学 自治 格別 特殊 でたらめ 甚だしい 傑作 ばからしい うんと 大層 なんとも めちゃくちゃ やたら 一段 着替え 予備 いよいよ 余計 臨時 臍 展開 宣伝 広める.
- All four navigation diffs: `kanji/着.md`, `words/あわてる.md`, `words/広告.md`, `words/早速.md`. Each diff is exactly one changed line and only adds the link brackets/href.
- `manifest.json`: rebuilt in memory via `build_manifest.build_manifest()`, equal to the committed file (contentVersion 6b287c38009cd16d). Every new or changed file's hash matches.
- The intake JSON: checked only the path list and hashes. It adds no learner content.
- `python tools/validate.py` → 0 errors.
- Quiz screening: every new title against all 3883 RU word titles and their `quiz_exclusions`. Method: Russian title-segment and stem overlap, the prompt's clusters, and my own sense-based candidate lists.
- Blind rule respected. A directory-wide text search listed the file names under `docs/translation-batches/` and `docs/translation-drafts/` as matches for a transliteration term. I did not open them.

Verdicts:
- Consistency (format, front matter, links, manifest, generated files): CLEAN.
- Navigation-only restorations (4 files): CLEAN.
- Quiz safety (EN exclusions retained, no missing required guard established): CLEAN. There are five low-confidence optional leads (see Optional).
- Intake record: CLEAN (path set equals the content diff: 34 payload paths = 30 new + 4 restored; no learner content).

Findings: none actionable.

Evidence per check:

1. EN-parity of front matter and links.
   - A script compared EN and RU `word, reading, jlpt, type, kanji, tags` for all 30 cards: no differences.
   - Every EN `quiz_exclusions` entry is retained in RU on all 30 cards.
   - No excluded entry is missing as a RU word file, duplicated, or the card itself.
   - Every `.md` link in each RU card resolves.
   - EN links absent in RU are all to targets with no RU file, so they stay plain text per convention: 大層 → `../kanji/層.md`; なんとも → `なんとなく.md`; 着替え → `../kanji/替.md`; 広める → `広げる.md`.
   - One RU-only link: 一段 → `段.md` (see Optional).
   - Repo-wide EN→RU link-count parity for the 30 targets found no dropped link and no RU-only link in any existing file.
   - Absent kanji cards are explicit coverage gaps, not link errors: 至 衛 稽 殊 甚 傑 層 替 臨 臍 展 宣. Each card names its kanji and explains the kanji, and 特殊 states that 殊 has no card here. Existing kanji cards are all linked; none are left unlinked.

2. Title uniqueness: no new word title duplicates any RU word title, and no new `;`-separated title segment equals a segment of another word title. Kanji cards were not touched.

3. Restorations. All four are single-line, link-only changes (checked with `git diff`) and match EN positions.
   - kanji/着.md:53 → `../words/着替え.md` (EN line 45, same path form). The mention occurs only on that line.
   - words/あわてる.md:39 → `あわただしい.md` (EN line 39).
   - words/広告.md:28 → `宣伝.md` (EN line 33). That is the only mention.
   - words/早速.md:31 → `さっさと.md` (EN line 28). That is the only mention.
   - Glosses beside the new titles do not mislead.
     - 着: «смена одежды; одежда на смену» next to the 着替え title «переодевание; сменная одежда» is a body gloss that covers both senses, as in EN (EN gloss vs EN title differ the same way). The difference is harmless.
     - あわてる: «суматошные обстоятельства или деятельность» is compatible with «суматошный; торопливый».
     - 広告: «продвижение, раскрутку» is compatible with the 宣伝 title.
     - 早速: «бойкую или равнодушную манеру» is compatible with «не мешкая; без колебаний», and the さっさと card teaches the cold manner at lines 21–22.

4. Manifest: rebuilt in memory and equal to the committed file; no stale hash. Intake `candidateRawSha256` equals the git blob hash. CRLF-normalised hash equals the manifest entry. No CR, tab, BOM or trailing whitespace in new cards. No generated or unrelated file is in the commit (36 files: 30 new + 4 modified + manifest + intake).

5. Reading/term consistency: no conflicting readings of the 30 words elsewhere in RU content. The two hits, 宣伝 しょうひんのせんでん and 自治 ちほうじち, are compounds, not conflicts. Terminology (итидан, атэдзи, «Digital Daijisen через Weblio», Дайдзисэн) matches existing cards.

Quiz-exclusion classification of every entry beyond the EN file (dictionary basis: JMdict sense or RU title; necessity in an ordinary quiz):

| Card → entry | Basis | Class |
|---|---|---|
| あわただしい → 騒ぎ | 騒ぎ «переполох; суматоха» vs あわただしい «суматошный». Shared Russian root and sense (uproar/commotion vs hectic); POS differs. | conservative |
| 自然科学 → 自然 | 自然 «природа; естественный» vs «естественные науки». Title root «естествен-», and the word is a component of 自然科学. | conservative |
| 自治 → 管理 | 管理 (management, administration, control) vs 自治 (self-government). «управление» appears in both titles («самоуправление» vs «управление»). The article teaches the contrast. | conservative (a real title trap; harmless) |
| うんと → もっと | もっと «больше; ещё» (more) vs うんと in comparison «намного». Both mark degree in comparisons. | conservative |
| うんと → 一層, 更に | «ещё сильнее/ещё больше» vs «в большом количестве; намного». Weak: even-more vs much-more. | conservative-weak (harmless) |
| なんとも → 別に | 別に «не особо (с отрицанием)» vs なんとも negative sense «вовсе не». Same negative-polarity slot. | conservative |
| なんとも → あんまり | あんまり «не очень-то (с отрицанием); чересчур» vs «вовсе не». Same slot. | conservative |
| やたら → 余る | 余る «оставаться лишним; быть сверх нужного» vs やたら «сверх меры». Shared «сверх». | conservative-weak |
| 一段 → 段 | 段 (step, stair) vs 一段 (one step); 一段 title «одна ступень» ≈ 段 «ступенька». | required (EN-link only; this direct pair is needed) |
| 一段 → だいぶ | だいぶ «значительно; заметно» vs «ещё заметнее». Shared «заметн-» and degree sense. | conservative |
| 予備 → 余裕 | 余裕 «запас (времени, денег, сил)» vs 予備 «резерв (запасные вещи, силы)». «запас» = «резерв» in Russian, and the parentheticals overlap («силы»). | required |
| 展開 → 流れ | 流れ «течение; ход (событий)» vs 展開 «поворот событий». Both sense «course of events». | conservative |
| 宣伝 → 進める | 進める «продвигать; вести дело вперёд» vs 宣伝 «продвижение». Same Russian root, different sense. | conservative (Russian-title trap, not a dictionary synonym) |
| 広める → 発展, 流行 | 発展 «развитие; расширение» vs «расширять». 流行 «массовое распространение» vs «распространять». Root overlap with the 広める title. | conservative |

No entry is unjustified: each has a real dictionary or Russian-title basis and an ordinary-quiz risk. None needs removal. A reader who prefers the narrowest lists could drop うんと → 一層/更な and やたら → 余る as weakest.

Dense-cluster check: every pair in the prompt's clusters has a direct exclusion on at least one side. Intra-batch pairs are also covered: 大層, なんとも, うんと and めちゃくちゃ guard one another on at least one side; likewise 余計, 一段, いよいよ and やたら; 至急 and さっさと; 自習 and 稽古; 宣伝, 広める and 展開; 傑作 and ばからしい; 特殊, 格別 and 臨時. I did not infer transitive pairs.

Optional:
- O1 (low confidence): 格別 → 別に. 格別's article teaches the negative use 格別問題はありません «особых проблем нет», and 別に is «не особо (с отрицанием)». 別に already guards 特に and あまり. Only 別に's own `quiz_exclusions` would need the pair (別に: `[あまり, 特に, 別]`). The title 格別 «особенный; в особенности» is not a defensible match for a negation-only 別に title, so this is not required. If wanted: 格別 `quiz_exclusions: [特別, 特に, 別に]`. This would also be a new RU-only guard beyond EN.
- O2 (low): いきなり vs 意外 «неожиданный». The いきなり body teaches «неожиданный вопрос» (いきなりの質問). ばったり and ひょいと, titled «неожиданно», are guarded. 意外 has no exclusions. If wanted: いきなり gets `意外` added. The title «без предупреждения; с ходу» does not itself match 意外.
- O3 (low): でたらめ «чепуха; как попало» vs くだらない «вздорный». Different parts of speech and nuance (pointless vs unfounded). No EN guard. Not required.
- O4 (low): 余計 «сверх необходимого; ненужный» vs 贅沢 «роскошь; излишество». 贅沢 (luxury) is not a dictionary synonym of 余計 (excess). Not required.
- O5 (low): 臨時 body teaches «дополнительный поезд», and 追加's title includes «дополнительный». The 臨時 title is «временный; внеплановый», so the pair is not a defensible quiz match.
- O6 (nonblocking): words/一段.md adds prose not in EN. The sentence «Отдельное слово 段（だん）«ступенька; ярус» называет саму ступень; 一段 считает одну такую единицу или служит наречием степени» and the link `段.md` are not in EN. It is accurate and useful, and it supports the required 一段 → 段 guard. Judge it under the fidelity facet. RU keeps EN's `../kanji/段.md` link.
- O7 (nonblocking): words/展開.md keeps a long unwrapped paragraph and uses inline code for `a(b + c) = ab + ac`. Inline code is already used in 35 other word cards, so this is acceptable.

Limits:
- I did not run `rutools/link_parity.py` or `word_title_screen.py`. I used my own EN-vs-RU scripts for link, front matter and title checks instead. Lexical-overlap screening is a lead generator, not a verdict. The semantic judgments (required, conservative, optional) rest on my reading of the Russian titles and JMdict-style senses. I did not query JMdict itself, so the dictionary senses cited are from my knowledge of its entries.
- The manifest rebuild was done in memory by importing `build_manifest`. The file on disk was not written. This confirms the content hash only, not any later coordinator regeneration.
- Prose accuracy, Russian style and translation fidelity (the other reviewers' facets) were read for consistency only and were not audited in depth.
- The tag vocabulary of some cards, e.g. さっさと `[adverb, action, manner]` and でたらめ `[noun, na-adjective, unreliability]` without `wago`, equals EN's tags exactly. I judged it as EN parity and did not review it further. The validator accepts it.

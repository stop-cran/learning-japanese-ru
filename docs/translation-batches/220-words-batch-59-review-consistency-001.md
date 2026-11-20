# B220 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `19bcfe00f202ae1368ffc4422b38d9b1da172c2e` (tree `6c90c32e275e1f0b28692443c41fdd228aad6c76`),
> the signed candidate pushed before review.
> Later reconciliation is in `220-words-batch-59-recheck-001.md`.

Snapshot: RU branch full-ru-220-words-59, commit 19bcfe00f202ae1368ffc4422b38d9b1da172c2e. `git rev-parse HEAD` matches and `git status --porcelain` is empty, so there are no uncommitted changes. The review was read-only; no generator was run (only `tools/validate.py`, which reported 0 errors). Frozen EN source: learning-japanese-en-frozen @6af98cb.

Scope: Facets reviewed: consistency, quiz safety, and scoped coverage of cross-file integration.
- All 30 new cards `words/<word>.md` were read in full (front matter and body). Their front matter (`word`, `reading`, `jlpt`, `type`, `kanji`, `tags`) and H2 count were compared with EN by script, and their link sets and `quiz_exclusions` were compared with EN by script. The EN bodies were not re-read line by line.
- All eighteen navigation files were inspected in full as diffs (19 link occurrences). Their link counts and path forms were compared with EN.
- `manifest.json`: every one of the 4714 entries was rehash-checked. Markdown matches on the raw bytes; the `strokes/*.json` files are tracked CRLF and match only after LF normalisation, which is the repository convention and not part of this diff (none of the strokes lines changed).
- The intake record `docs/translation-batches/220-words-batch-59-intake.json` was checked, but only for its path list, candidate SHA-256 values and the absence of learner content, as the prompt permits.
- RU `.github\instructions\content-structure.instructions.md` was read for the quiz and link rules. I did not read any author report, title-screen output or batch record. I ran `word_title_screen.py` myself.
- Model: not verifiable from inside the session.

Verdicts:
- Consistency: CLEAN. The 18 files differ from the previous commit only by the restored link brackets. All 19 occurrences match EN-position parity and EN's path form. 48 payloads match the 48 content paths in the diff, and no unrelated or generated file is committed.
- Quiz safety: NEEDS FIX (two minor findings, F1 and F2). All EN exclusions are retained, and every RU-introduced guard has a real basis (classified below). The dense-cluster screen found no missing guard apart from two generic-versus-specific pairs.
- Scoped coverage of cross-file integration: CLEAN. Every EN link in the 30 cards is restored to an existing RU target. The only EN links not carried over are those to absent files: kanji 層 and 般, and ウイスキー and ビール. Plain mentions that EN leaves unlinked and whose RU file is absent are plain text.
- Per-article exceptions: ワイン (F1) and ラケット (F2).

Findings:

F1; minor; quiz safety; words/ワイン.md:7-8 (front matter, no `quiz_exclusions`); claim and impact: ワイン «вино» is a kind of 酒 «алкогольный напиток; сакэ», so in a "ワイン → meaning" question the option «алкогольный напиток; сакэ» is a defensible correct answer.
- The RU content-structure rule says a generic label inside a title needs a direct pair, as with 車/電車 (line ~157). The repository already guards the same hypernym relation: 酒 excludes [アルコール, お酒, 飲み物] and テニス excludes [スポーツ].
- The card itself links 酒 and says 酒 is broader.
- Remedy: add the line `quiz_exclusions: [酒]` after `tags:` in words/ワイン.md, then regenerate the manifest.
- Evidence: JMdict ワイン "wine"; 酒 "alcohol; sake", and the RU 酒 title begins «алкогольный напиток». EN has no guard here, so this is an RU-title-driven pair.
- Confidence: medium.

F2; minor; quiz safety; words/ラケット.md:7-8 (front matter, no `quiz_exclusions`); claim and impact: 道具 «инструмент; приспособление; средство» is a generic label that fits a racket as sports equipment. In a "ラケット → meaning" question, «приспособление» is arguably a correct answer.
- The card links 道具 and calls it "более широкая категория".
- Remedy: add `quiz_exclusions: [道具]` to words/ラケット.md (the manifest must be regenerated). If the owner does not accept hypernym pairs without a title clash, record it as a conservative-optional pair and do not block on it.
- Evidence: JMdict 道具 "tool; implement; equipment". 道具 already carries a long guard list including 物, 方, 道, 技術 and ギター. I found no existing guard on ラケット.
- Confidence: low to medium.

Classification of every `quiz_exclusions` entry beyond the EN file. "Required" means the pair is defensible in an ordinary quiz; "conservative" means there is a real basis but necessity is unestablished. Over-guarding is harmless (it only shrinks the distractor pool), but I report it as asked.
- 不足→欠ける: RU-introduced. JMdict 欠ける sense 2 "to be lacking; to be missing". The 欠ける title «недоставать» overlaps 不足 «нехватка». Required.
- 不自由→制限: JMdict 制限 "restriction; limit". The shared stem «огран-» (ограниченность and ограничение) is the basis. Conservative; titles partly separate (state versus imposed limit).
- 不安→緊張: JMdict 緊張 "tension; nervousness". The title «нервное волнение» is near «тревога». Conservative to required; 緊張 already guards 心配.
- 不安→はらはら: JMdict はらはら sense 2 "feeling anxious (suspense)". Both titles contain «тревог». Conservative to required; はらはら already guards 心配 and 緊張.
- 不可→禁止: JMdict 禁止 "prohibition". The 不可 title «не разрешено» is near «запрет». Required.
- 下り→下りる: JMdict 下りる sense 1 "to descend". The shared root gives «спуск» and «спускаться». Required, borderline.
- 下り→降りる: JMdict 降りる "to descend; to disembark". Its title shares «спускаться». Conservative.
- 下り→坂: JMdict 坂 "slope"; the 下り坂 compound is taught in the body. Conservative; the titles «спуск» and «склон» differ.
- 下り→方向: the 下り title contains the exact word «направление», which is the 方向 title. Required.
- 上京→東京: the 上京 title contains «Токио», which is the whole 東京 title. Required.
- 一言→要するに: JMdict 要するに "in short". The title of 要するに, «словом; если коротко», shares only «корот» with 一言 «пара слов; короткое высказывание», and the parts of speech differ. Conservative at best, arguably over-guarding (see Optional).
- 一致→合う: JMdict 合う "to match; to agree". Title «совпадать» against «совпадение». Required.
- 一致→偶然: the 偶然 title contains «совпадение», the whole 一致 title segment. Required.
- 一生→命: JMdict 命 sense 2 "lifespan; lifetime"; the 命 title carries «срок жизни». Conservative to required.
- 一方→方: JMdict 方 "side (of comparison)"; the title has «сторона сравнения» next to 一方 «одна из сторон». Conservative.
- 一度に→同時: JMdict 一度に "all at once; at the same time". Conservative.
- 一体→全体: identical title segment «целое». Required.
- 一人一人→個人: «отдельный человек» against «каждый человек; каждый по отдельности». JMdict 個人 "individual". Conservative to required.
- ヨーロッパ→欧州: the titles are identical, «Европа». Required.
- メンバー→委員: JMdict 委員 "committee member". A narrow subtype of «член». Conservative.
- メンバー→参加: 参加 «участие» against «участник» is only a stem relation and a different part of speech. Unjustified, mild over-guarding: the titles already separate the cards.
- メモ→記録: JMdict 記録 "record; document". Title «запись (сведений)» against «записать для памяти». Conservative.
- メモ→手紙: JMdict 手紙 "letter; note". The 手紙 title carries «записка», and the メモ body gives «записка» as its main sense. Required.
- メモ→栞: JMdict 栞 "bookmark; guide". Its «памятка» is close to «для памяти». Conservative.

The three guards the author calls required (上京→東京, 一致→偶然, ヨーロッパ→欧州) are confirmed required. The retained EN guards are intact, and the 世の中→世間 guard resolves against the revised 世間 card.

The eleven RU-only links:
- All eleven targets exist in RU. EN does not link any of them. For 不足→欠ける, 不安→緊張, 下り→下りる, 一致→合う, 一生→命, 一体→全体, 一人一人→個人, メンバー→委員 and メモ→手紙, EN does not mention the target at all; the RU card adds a comparison sentence and links it. These are substantive comparisons, so a link is appropriate under the RU content-structure rule, and each addition is covered by a guard.
- 上京→東京 and ヨーロッパ→欧州: EN mentions the target unlinked (上京.md lines 23 and 34, ヨーロッパ lines 32). The RU card introduces the target substantively and links it. Acceptable.
- The accuracy of the added prose belongs to the correctness reviewers, not this facet.

The title-collision screen found no unguarded exact title or segment duplicate (checked with the dense-cluster list in the prompt):
- 世紀 (guarded against 時代 and 年代).
- 世の中 (guarded against 社会, 世界 and 世間).
- 一生 («жизнь»; guarded against 人生 and 命).
- ますます and 一層 (both guarded against もっと and 更に).
- 一体 («целое»), メンバー («член») and ヨーロッパ.
- ロケット «ракета» against ラケット «ракетка»: distinct.

Optional:
- Over-guarding (harmless): メンバー→参加 and 一言→要するに could be dropped. Their titles already separate the cards. Dropping them is not required.
- 一瞬 against ちょっと «ненадолго» is an EN-linked pair with no guard on either side. The meaning overlap is weak; I do not claim a defect.

Limits:
- No dictionary was re-fetched. The JMdict entries and senses cited above are from memory and are the basis for the classifications, not for a verdict.
- Correctness and comprehension of the Russian prose are other reviewers' facets. I did not evaluate the accuracy of the RU-added comparison paragraphs.
- Pre-existing, outside this batch: `kanji/杯.md` links `[不](不.md)` where the frozen EN does not. That link was already present at the parent commit ff8310d.
- The manifest was re-hashed, not regenerated. After any fix (F1 or F2), the coordinator must regenerate the manifest and intake record.

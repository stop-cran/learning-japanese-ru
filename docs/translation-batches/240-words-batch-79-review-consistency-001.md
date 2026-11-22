# B240 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `d0d977cad025983c702361e0408d9c9be4b8b085` (tree `401f953909d959a255de1b8abeeb08406c7d4054`),
> the signed candidate pushed before review.
> Later reconciliation is in `240-words-batch-79-recheck-001.md`.

Snapshot: RU primary checkout, HEAD = d0d977cad025983c702361e0408d9c9be4b8b085 (confirmed by `git rev-parse HEAD`); `git status --porcelain` printed nothing (no uncommitted changes). Parent e67e771 -> candidate diff = 36 files (30 new word cards, 4 navigation files, manifest.json, intake JSON). `python tools/validate.py` -> 0 error(s). I did not run build_manifest.py or any generator.

Scope: Read in full (front matter + body): all 30 new cards (蒸発 気体 蒸す 蒸気 湿度 湿気 蒸し暑い 散らかる 散らかす 散る 散らす 撒く 蒔く 葬式 著す 落第 落とし物 下駄 草履 茂る 英文 英和 若々しい 教養 芸能 花火 花嫁 芯 艶 早速), compared programmatically with frozen EN (front matter fields, quiz_exclusions, link-target sets, URL/JMdict-ID footers, H2 count) and by reading. All four navigation diffs read in full (kanji/花.md, words/忘れ物.md, words/花.md, words/足袋.md) with the EN link positions. manifest.json: all 34 changed words/kanji hashes recomputed from the files = manifest values (0 mismatches), no missing file entries. Intake JSON: path list (34 payloads) = the content diff paths exactly (30 new + 4 navigation); I checked only that. Also read the RU cards はらはら, 跳ねる, さわやか, 棒, 忘れ物 for guard analysis and ran word_title_screen.py (output used only as a lead) plus my own scan of all RU word titles for stems. Model: not verifiable from inside the session (unknown).

Verdicts:
- Consistency: CLEAN
- Quiz safety: CLEAN (optional notes only; all EN exclusions retained, 3 RU additions classified below)
- Scoped coverage / cross-file integration (links, kanji links, nav restorations, manifest, intake): CLEAN

Findings: none (no actionable defect established).

Evidence summary
1. Front matter vs EN: word, reading, jlpt, type, kanji, tags identical to EN for all 30 cards. quiz_exclusions: every EN entry retained in EN order (0 missing, 0 reorder); the only additions are 散る +[はらはら, 跳ねる] and 若々しい +[さわやか]. Validator and kanji-link checks pass; all relative `.md` links resolve (0 broken).
2. Links vs EN: link sets equal EN except these EN-only links, all legitimate: kanji/蒸, kanji/湿, kanji/著, kanji/芸 (no RU kanji file); 液体 (気体), 乾燥 (湿気), 巻く (撒く, 蒔く), 枯れる (茂る), さっさと (早速) – all targets absent from RU (confirmed), rendered as plain text with glosses that read naturally (枯れる «засыхать, увядать»; 乾燥 «сухость, высыхание»; 液体 «жидкость»; 巻く «наматывать, сворачивать»; さっさと with its nuance sentence), nothing dropped. The one EN-only link whose target exists is 蒸す→べたべた (EN:48), inside the EN paragraph about the English labels 'sticky'/'close' that RU deliberately drops; no RU sentence remains for it to sit in, so I do not count it a defect (see Optional 1). RU has no link without an EN counterpart. In-batch links (蒸発→蒸気 etc.) all present as in EN.
3. Mentions left plain that have RU cards but EN leaves plain (遊ぶ, 試験, 交番, 着物, 種, 鉛筆, 野菜, 桜, サラダ, 庭, 返事, 番組, 単語, 親戚, 部屋): they are examples/glosses only; no substantive introduction -> no link required. Mentions with no RU file (沸騰 固体 蒸らす 湿る 通夜 留年 退学 中退 和英 新婦 花婿 艶消し 火花 線香花火 蒔絵 繁る 芸能界 無教養 落し物 浴衣 葬儀 蒸汽) confirmed absent -> plain text correct. No EN card that links a batch word has an RU counterpart (ゆでる, 広げる, 水分, 水蒸気, 湯気, 湿る, 直後, 至急, 執筆, 文芸, 生長, 漢和, 和英 all absent in RU), so no inbound links are owed. Pre-existing plain mentions of 花火 (kanji/火 l.28, words/見物 l.18) and 落とし物 (words/すり l.36) are plain in EN too -> no parity gap.
4. Navigation files: diffs are bracket/href only, nothing else changed. kanji/花 l.40 and l.52 -> `../words/花火.md` (EN l.30, l.35; prose l.22 stays plain as EN l.22); words/忘れ物 l.36 -> `落とし物.md` (EN l.26 first mention; later mention l.38 plain as in EN); words/花 l.28 -> `花火.md` (EN l.19); words/足袋 l.35 -> `草履.md` and `下駄.md` (EN l.39). Path forms match EN. Glosses beside the new titles: 花火 «фейерверк» = title; 落とし物 «оброненная или потерянная вещь» vs title «потерянная или обронённая вещь» – same two senses, order/ё only, a prose gloss not a quiz label, harmless; 足袋 «традиционная японская обувь» beside 草履/下駄 – accurate generic category, no conflict with the dzori/geta titles.
5. Footers: JMdict entry IDs identical to EN for every card; Weblio/Kotobank/KANJIDIC2 URLs identical to EN. The only URL difference is that the two AHD (English-only 'sticky'/'close') links in 蒸す and 蒸し暑い are dropped together with the English-label paragraph (sound for a Russian adaptation). 花火 has no dictionary footer, mirroring EN's older format (see Limits).
6. Manifest: contentVersion changed, 34 file hashes updated/added and equal to the raw SHA-256 of the working-tree files; no unrelated files in the diff (only the intake JSON besides content + manifest).
7. 葬式 vs 儀式/式: «похороны» and «более общие слова для церемонии» (l.35, EN:36) stay consistent with 儀式 «церемония; обряд, ритуал» and 式 «церемония; формула»; 葬式→式/儀式/勤め/サービス guards kept.
8. 花嫁–嫁: the only exact shared title segment found by the screen («невеста»), guarded by EN's 花嫁→嫁 (declared on the 花嫁 card; 妻 also kept).

Quiz-safety analysis
- Retained EN guards (all present): verified programmatically per card; none dropped. One-sided declarations suffice (app applies pairs symmetrically); I did not demand reverse entries.
- RU-introduced guards (dictionary basis / necessity):
  a) 散る→はらはら – basis: JMdict はらはら (adv) "(of leaves, tears) falling lightly/fluttering" vs 散る sense 1 "(of blossoms, leaves) to fall". Titles «плавно опадать» vs «опадать (о цветах, листьях)» are near-identical -> REQUIRED (agree with author).
  b) 散る→跳ねる – basis: 跳ねる sense "(of liquid) to splash/spatter" vs 散る sense 2 "to scatter, fly apart"; titles share «разлетаться». Real basis, necessity unestablished -> CONSERVATIVE (harmless; a learner could defend «разлетаться брызгами» for glass/liquid scattering).
  c) 若々しい→さわやか – basis: 爽やか "refreshing; fresh; (of voice/manner) clear, pleasant" vs 若々しい "youthful"; titles share the qualifier «(о голосе, манере/манерах)» and the stem «свеж». Real basis, necessity unestablished -> CONSERVATIVE. Not unjustified: it guards a qualifier overlap, not an antonym the article teaches. No over-guarding found.
- Unguarded in-batch pairs (蒸発–蒸す/蒸気/蒸し暑い, 気体–湿気, 蒸気–湿気/蒸し暑い, 散らかる–散らす, 落第–落とし物, 英文–英和, 花火–花嫁): titles separate them (different parts of speech or senses; no shared correct-answer segment) -> no guard needed.
- Declined pairs judged OK: 湿度–空気/大気/しっとり, 蒸す–天気/料理, 撒く–逃げる/去る, 著す–作家, 落第–合格 (antonym), 落とし物–迷子, 茂る–覆う, 英文–英語, 若々しい–新鮮, 芯–心臓, 艶–表面, 早速–延期, 蒸発–人間, 下駄–台. 気体–物質 and 落とし物–物/品物 only share a hypernym word («вещество», «вещь»); see Optional 3.
- My own scan of all RU word titles for stems beyond the screen (исчез/пропа, потер, экзамен/провал, сочинение, стержень, середина, сразу/скоро, брызг, сажать, сеять, блеск, пышный, пар) found no further defensible correct-answer pair. Checked specifically: 芯 vs 棒 «палка; стержень; шест» (棒 is a rod, not the inner core/lead; not defensible), 著す vs 作文 «сочинение» (noun school composition vs authoring verb), 蒔く vs 挿す «сажать черенок» (different act), 早速 vs 直/もうすぐ/ぺろり (different senses).
- Title fit: 蒸発 (qualifier «(человека)» is accurate, body explains), 気体 (covers 'gas' as state of matter; ガス guarded), 蒸す (register «прогревать паром» acceptable), 蒸気 («пар» + body note on non-water vapour), 湿度 (qualifier correct), 散らす («раскидывать» acceptable colloquial register), 撒く, 著す, 落第, 下駄 («на подставках» understandable and explained in body), 草履, 英和, 若々しい («моложавый» fits 'youthful, young-looking'), 教養, 芸能 (second segment readable), 花火, 花嫁 («новобрачная» acceptable), 芯, 艶 – no misleading title found.

Optional:
1. 蒸す and 蒸し暑い keep six guards (べたべた, 密, 近い, 親しい, 閉じる, 閉まる) whose only EN rationale (English labels 'sticky'/'close') was dropped; in Russian titles none of these overlap (Russian «липкий», «близкий», «закрывать» do not describe sultry weather) so the guards are harmless dead weight with no in-card explanation. They must stay (all EN exclusions are to be retained); no action needed. If a later pass wants a comment, one Russian sentence could explain that they protect similar-looking words, and 蒸す→べたべた could be re-linked there.
2. 撒く title «уходить от погони» reads intransitive while the verb is transitive (追っ手をまく); body l.20 line clarifies. A tighter label such as «отрываться от погони» is a wording preference only, not required.
3. If the project wants extra caution, 気体→物質 and 落とし物→物 could be added as conservative guards (hypernym overlap); not required by the contract.

Limits:
- Dictionary senses (JMdict/Daijisen) are cited from memory of those entries, not re-fetched; guard classifications b) and c) are judgment calls.
- 花火 has no quiz_exclusions list and no dictionary footer, mirroring EN's older card format; acceptable parity, worth recording as a limit rather than a defect.
- Manifest hashes were verified for all changed files and fully for file existence, but I did not regenerate the manifest (not allowed); contentVersion consistency rests on the per-file hashes matching.
- Pre-existing differences from EN in the four navigation files (e.g. kanji/花 → 花見 RU-only link) were left unreviewed as out of batch.

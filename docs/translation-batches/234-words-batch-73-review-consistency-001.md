# B234 consistency and quiz-safety review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `1e7c04d20795a3f0efac996855d00f233ebe566b` (tree `02023ebe35e7f52010e453f8711aa47bf99c56ae`),
> the signed candidate pushed before review.
> Later reconciliation is in `234-words-batch-73-recheck-001.md`.

Snapshot: 1e7c04d20795a3f0efac996855d00f233ebe566b (learning-japanese-ru); `git status --porcelain` empty, no uncommitted changes. 37 files: 30 new words, 5 nav-only edits (kanji/埋, パーティー, 追う, 隙間, 面接), manifest.json, intake JSON.
Scope: Consistency and quiz-safety plus cross-file integration of batch 234. All 30 RU cards and all 5 nav diffs read in full. Only お先に, さようなら, 送別 and the start of 送り仮名 were read in full in the EN-frozen originals; the rest were compared programmatically (front matter, quiz_exclusions, link targets and occurrence counts, footers). Ran validate.py (0 errors) and re-hashed the manifest. Author reports, batch records and drafts were not read. Reviewer model not verifiable by me.
Verdicts:
- Consistency: CLEAN
- Quiz safety: CLEAN (no required guard is missing and none is unjustified; several RU-added guards are conservative, and four optional under-guard candidates are listed)
- Scoped coverage (nav/link integration): CLEAN
- Comprehensibility: not assigned to this review.

Mechanical results
- validate.py: 0 errors. All 5134 manifest hashes match the files (CRLF-normalised sha256), and no content file is missing from the manifest. The manifest diff changes only contentVersion, the 埋 hash and the new entries.
- Intake: its 35 payload paths equal the content diff exactly, and it adds no learner content. The held list is empty.
- Front matter: identical to EN for all 30 cards, except that 近付ける carries RU-only quiz_exclusions.
- EN guards: every EN quiz_exclusions list is kept as a prefix of the RU list, in the same order. 送り仮名, 迷信 and 述語 have no key in EN or RU.
- Links: parity with EN by target and by occurrence count. The only dropped EN links point to targets with no RU file: 仮名, ずらす, 主語 and kanji 補, 述, 接, 農, 村, 輸. They remain plain text and read naturally. No broken links.
- RU-only link: 追い掛ける «Оттенки значения» links «догнать» to 追い付く.md. This is a substantive contrast and the target exists.
- Nav files: only link brackets and hrefs changed; RU wording is unchanged and positions match EN.
  - kanji/埋 wraps 埋める at lines 29 and 38; the うずめる row and the prose stay plain, as in EN.
  - パーティー→宴会, 追う→追い掛ける, 隙間→埋める, 面接→接近.
- EN links from existing RU cards to the new words: all restored. The remaining non-links point to words with no RU file.
- Footers: 応接 (Digital Daijisen, kotobank), 応対 (Seisenban, kotobank) and 交通機関 (Daijisen on Weblio) mirror EN's shape and source names.

Findings: none that require a fix.

Classification of the 19 RU-introduced quiz_exclusions entries (direct pairs; the app applies them symmetrically and not transitively). The dictionary basis is the JMdict/Daijisen entries cited in each card (退ける 2850084/1595080, 送別 1402850, 応対 1179980, 催促 1292200, 迫る 1475720, 近付ける 1242520) together with the RU titles. I did not perform fresh web lookups.
- 退ける→しまう: REQUIRED. Both titles contain the identical segment «убирать».
- 退ける→収める: REQUIRED. Same identical «убирать» segment.
- 農産物→製品: REQUIRED or near-required. The titles share the word «продукция» («сельскохозяйственная продукция» vs «изделие; продукция»).
- 迫る→収める: conservative. The basis is the real overlap in the closing sense, but the titles differ.
- 近付ける→近寄る, 接近, 寄る, 近い: conservative. They are real near-synonym families with EN links, but the titles separate them. They add no harm because 近付ける has few other candidates.
- 船便→郵送, 船便→速達: conservative. The basis is shipping and mail sense overlap; the titles are distinct.
- 交通機関→車: conservative. 車 «автомобиль; транспортное средство» is the closest competitor to 交通機関 «транспорт».
- 農村→地域: conservative, with a real basis in an area/region sense.
- お先に→譲る, 送別→送る, 追い掛ける→走る, 応対→付き合い, 応対→返事, 応対→答, 催促→急ぐ: conservative and weakest. They have a plausible semantic basis; 送る «отправлять; провожать» is close to 送別 «проводы». The titles already separate them, so necessity is unestablished. None is unjustified, and over-guarding costs only a slightly smaller distractor pool.
- Unjustified: none.
- Dropped EN guards: none.

Optional (nonblocking; no required guard established; necessity UNVERIFIED)
- ずれる «смещаться; не совпадать (по времени, сути)» vs 相違 «расхождение; несовпадение» and vs 逸れる «отклоняться в сторону…; уходить от темы». Neither pair is guarded.
- 応対 «…» vs 答える «отвечать» and 応じる «откликаться; соглашаться (на просьбу)». The sibling pairs 答 and 返事 are guarded, but these two are not.
- 近付ける «приближать (что-либо к чему-либо)…» vs くっつける «приклеивать; придвигать вплотную».
- Optional remedy if the owner wants more conservatism: append `ずれる`: [相違, 逸れる]; `応対`: [答える, 応じる]; `近付ける`: [くっつける]. Not required.
- 休み is a plain example in 送り仮名 (EN also leaves it unlinked), even though an RU card exists. Optional.

Pairs judged, no guard needed (separated by title)
- Declined by the author: 催促–返事, 迫る–返事, 接する–境界. The related titles 境界 «граница», 国境, 関係, 交際, 合う «подходить; совпадать», 農業, 食品, 診察, 一致, 関する, 対する and 知る are separated by title.
- In-batch unguarded pairs: お先に–送別, 追い越す–追い掛ける (linked to each other, titles differ), 埋める–追加, 応対–宴会, 接する–近寄る/迫る/近付ける, 催促–応対, 近々–接近, the 農薬/農産物/農村 pairs and 船便–交通機関.
- One-way declarations (接する→接近, 近寄る↔近付ける, 追い越す↔追い掛ける) are valid under the symmetric direct-pair contract.
- Title screen: only three exact shared segments exist, and all three are guarded (送別–見送り «проводы», 退ける–しまう, 退ける–収める). The stem hit «прохо» between 通路 «проход…» and お先に/退ける is unrelated in meaning, so no guard is needed.
- Title fit of the phrase-like titles (お先に, 応対, 催促, 近々, 農薬, 農村) matches EN and the cards' explanations.
- Pre-existing prose beside the new links (埋, パーティー, 追う, 隙間, 面接) is consistent with the new card titles.

Limits
- No web or dictionary lookups were done. Dictionary bases come from the entries the cards cite, so the necessity of the conservative guards is UNVERIFIED.
- EN originals were fully read for only three cards and compared programmatically for the rest.
- Naturalness of the plain renderings (仮名, ずらす, 主語) was read but is not a linguistic-correctness verdict.
- Not covered: Japanese accuracy, translation quality and comprehensibility; no device or app test.

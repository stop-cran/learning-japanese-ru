> Original blind consistency report on `559309ba0d24b9a8cd90fe1a59776a34a86a66e8` (tree `a2bcc0443c45b810984ecb22edec77e7b21d4e81`).
> Completed runtime: `claude-opus-5.5`, agent `d6fa97fa-35a2-416f-8e84-0f260d96c459`. The report body below is unchanged apart from LF line endings.
> [Coordinator reconciliation](254-words-batch-93-independent-review-001.md) and [scoped rechecks](254-words-batch-93-recheck-001.md).

# B254 consistency / quiz-safety review (blind, read-only)

## Snapshot
- Candidate 559309ba0d24b9a8cd90fe1a59776a34a86a66e8; parent 7ba5db72ca85c0d5a92fb6f79d7ab902b09a472d; frozen EN 6af98cb717755690a9ca793e5454a96ebd7a8f9f.
- HEAD verified = candidate; `git status --porcelain` empty before and after review.
- Diff parent..candidate: 42 files = 30 new words/*.md, 10 navigation files, manifest.json, docs/translation-batches/254-words-batch-93-intake.json. Nothing unrelated is committed.

## Scope (actually done)
- Brief, mechanical facts and full navigation diff read completely.
- All 30 paired RU/EN cards read in full: 淡水 冷める 涼む 液体 消防署 くたびれる 消耗 消毒 消極的 消化 海洋 海水浴 寝間着 浴衣 流行る 流域 活字 活力 洗剤 おしゃれ 洒落 商店 ショップ 洋品店 注す 原理 法則 泊める 治す 油断.
- Dictionary JSON read for 油断, 涼む, 泊める, 商店, ショップ; titles/exclusions of RU neighbours checked (店, 売り場, 書店, 休む, 休み, 休憩, 泊まる, 宿, のんき, 八百屋).
- Commands run: `python -X utf8 -B tools\validate.py` (PYTHONDONTWRITEBYTECODE=1) -> "0 error(s)", exit 0, no bytecode left. link_parity on the 40 files: only `words/断水.md EXTRA words/停電.md`, which predates B254 (not a defect). word_title_screen on 30 words: 191 stem-only `!!` (seg=[]), 19 OK; manual triage below. EN<->RU front matter, key order and heading comparison done for all 30.
- Not done: no web verification of dictionary senses beyond the archived JSON; the model/author identity is not verifiable.

## Verdicts
- Correctness / consistency: NEEDS FIX (one medium, missing quiz guard; no format or link defects).
- Coverage / EN preservation: CLEAN.
- Russian comprehensibility: not assigned to this reviewer.

## Findings
**C1 — medium, confidence medium — missing direct guard ショップ <-> 売り場.**
- File: words/ショップ.md:9, `quiz_exclusions: [商店, 店]`.
- RU title ショップ «торговая точка» (line 4) and RU 売り場 «место продажи; торговый отдел» (words/売り場.md:4, no exclusions) overlap in Russian. «Торговая точка» is the normal Russian for a point of sale / retail outlet, and JMdict 売り場 is "place where things are sold; point of sale; sales floor; counter". That gloss is from my own knowledge; it is not in the archived packet, so this is unverified here.
- In the RU-title -> JP-options direction («торговая точка» -> {ショップ, 売り場}), both options are defensible.
- The collision exists because of the RU title. EN "shop" vs "sales floor; counter" was distinct, so EN needed no guard. Neither card excludes the other.
- Remedy (one-sided direct pair is sufficient): words/ショップ.md:9 -> `quiz_exclusions: [商店, 店, 売り場]`. The alternative is retitling ショップ (e.g. «магазин; бутик»), but that needs 店/商店 re-checked.

No other findings. Checked and clean:
- **Format.** Each card has flat front matter in EN key order. The extra `quiz_exclusions` in 商店/泊める is in the last position. Each has exactly the 4 headings `## Значение / ## Как сочетаются кандзи / ## Синонимы и антонимы / ## Оттенки значения`, plus footers labelled «Словарь:» / «Употребление:».
- **Japanese data.** Word, reading, jlpt, type, kanji and tags are identical to EN on all 30. Japanese examples are kept verbatim.
- **Links.**
  - Every EN link whose RU target exists is kept.
  - Links to absent RU kanji cards are plain text, correctly: 淡 涼 液 防 署 耗 毒 極 浴 衣 剤 洒 油 泊.
  - 冷ます is absent in RU and is also plain text.
  - No dangling RU links (validator clean).
- **Navigation (10 files).** Only link brackets/hrefs are added, and line counts are unchanged. All 15 restored links are at EN-parity positions. EN 則 also links 不規則, which has no RU file, so plain text there is correct.
- **Link debt.** For each batch word, every existing RU file whose EN counterpart links it now links it too. No debt remains.
- **Manifest.** Validator passes, so no stale hash or missing entry was detected. Intake JSON is mechanical.

## quiz_exclusions: EN preservation and RU-only additions
- **EN preservation.** All EN exclusions are retained on all 30 cards; none dropped or reordered.
- **Existing cards.** No existing RU card names a batch word in its exclusions. EN cards that do (ふざける, カロリー, スマート, プリント, モダン, 冷ます, 冷やす, 刷る, 和服, 売店, 店屋, 張り切る, 普及, 水分) have no RU file, so there is no reverse debt.
- **RU-only additions.** All are one-sided, which is valid under the direct, non-transitive contract.

| Pair (file:9) | Class | Evidence |
|---|---|---|
| 商店 -> 店 | required | 店 «магазин» vs 商店 «...розничный магазин»: the hypernym title is a defensible answer. JMdict 1347180 "shop; store; firm"; 店 1582120 "store; shop". |
| ショップ -> 店 | required | «торговая точка» vs «магазин»; JMdict 1062820 "shop". (EN had 商店 only.) |
| 油断 -> のんき | required | «беспечность» vs のんき «беззаботный; беспечный» share the stem беспеч-. JMdict 1538690 "negligence; carelessness"; 呑気 includes "careless". |
| 涼む -> 休む | conservative | RU title «...отдыхать в прохладе» overlaps 休む «отдыхать; отсутствовать». JMdict 1554380 has no rest sense ("to cool oneself; enjoy the cool air"), so this is RU-title-driven. Acceptable. |
| 泊める -> 泊まる | conservative (not strictly needed) | Titles «приютить на ночь; дать ночлег» vs «ночевать; ...» are distinct. The card teaches the transitive/intransitive contrast (lines 32-34), and the guard removes a useful distractor. It follows the in-repo precedent 治す -> 治る (EN) and 宿 -> 泊まる; harmless. |

## Title-collision triage (no guard required)
- 寝間着/浴衣 vs 服 (hypernym; precise title present).
- 洋品店 vs 商店/書店/八百屋 (distinct qualifiers).
- 注す vs ぽたぽた (adverb vs verb, distinct).
- 流行る vs 成功.
- 消防署 vs 火事.
- 涼む vs さっぱり/すっきり/さわやか.
- 治す: no RU 治療 card.
- 原理/法則: EN one-sided guard 法則 -> 原理 is kept, which is sufficient as a direct pair; 原理 has 主義/説/基本/基礎.
- 洒落 vs おしゃれ: guarded as in EN.
- Stem-only `!!` lines are all seg=[] with no shared gloss.

## Optional (non-blocking)
- O1: 洋品店 could also exclude 商店 («розничный магазин» is a hypernym). Not required, because 洋品店's specific title is always among the options. Conservative only.
- O2: 泊める -> 泊まる could be dropped to keep a pedagogically useful distractor. Keeping it is also consistent with precedent.
- O3: 売り場 is outside B254. If C1 is instead fixed on 売り場 (adding ショップ), that touches a non-batch card. Putting the guard on ショップ keeps the fix inside the batch.

## Limits
- Dictionary evidence comes from the archived JMdict JSON packets. The 売り場/呑気 glosses are not in the packet and are unverified here.
- English or Japanese glosses do not verify Russian naturalness.
- Quiz-runtime behaviour (option count, direction) was inferred from the format reference, not executed.
- No generators or tests beyond the validator, link_parity and the title screen were run.
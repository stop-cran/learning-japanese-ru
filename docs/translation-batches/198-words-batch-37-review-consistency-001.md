# B198 review — consistency and quiz safety

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `claude-sonnet-5.5`
> (Claude family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: tree `c82e94b30d2c72c36fb56406ba2aaaf1f54e0002`, staged in a scratch worktree at detached
> HEAD `5dd9a78` while commit signing was unavailable. No commit of this tree exists.
> Later reconciliation is in `198-words-batch-37-recheck-001.md`.

Snapshot: staged tree `c82e94b30d` (base reviewed tree `ea3a478`). `git diff-index --cached --quiet c82e94b30d` = 0, `git diff --quiet` = 0, no untracked files; no uncommitted difference from the candidate. Detached HEAD `5dd9a78`, nothing was changed.

Scope: all 30 new `words/*.md` cards read in full against their frozen-EN originals (6af98cb); the 13 navigation-only files (diff read line by line); `manifest.json`. Facets: consistency, quiz safety, cross-file integration. Evidence gathered by read-only scripts (front-matter/link diff against EN, SHA-256 recomputation against the manifest, all-card EN→RU link parity), `tools/validate.py` (0 errors) and `word_title_screen.py` with `RU_ROOT` (leads only). Model: not independently verifiable. Dictionary senses were not re-fetched (see Limits).

Verdicts:
- Consistency: CLEAN. Front matter fields word/reading/jlpt/type/kanji/tags equal EN for all 30; every EN link either exists in RU or its RU target is absent (章/極/根/税/移/秒/禁/祭/祝 kanji, 重ねる, 収入, 煙, 仏, 悲しむ, おめでとう, ありがとう, お辞儀, 確かめる all missing in RU) and is plain text; no Russian-only link in the 30 cards. Across all RU words/kanji/articles, EN links to the 30 new targets match RU (the one hit, `kanji/紙.md` → `神.md`, is a pre-existing link to the existing kanji card, outside the diff). The 13 navigation files change only link brackets/hrefs (kanji/明 now `[明き](../words/空き.md)` as in EN). Manifest: all 4054 entries match recomputed hashes (CRLF-normalised), nothing unlisted, no generated/unrelated files in the diff.
- Quiz safety: NEEDS FIX (one missing direct guard, minor; F1). All EN exclusions are retained. Exclusions beyond EN are classified below.
- Scoped coverage of integration: CLEAN.

Findings:
- F1; Minor; quiz safety; `words/移動.md:6` (and `words/動かす.md:6`). 移動 teaches the action sense する («передвинул стол», `この机を窓のそばに移動しました`) and 動かす «сдвигать; приводить в движение» is taught with the near-identical `椅子を…動かしてください` («Сдвиньте стул»). The card itself says 動かす “сосредоточено на…” 移動. 移動 guards 移す and 移る, 移す guards 動かす, but the pair 移動–動かす has no direct exclusion on either side (EN also has none), so “передвинуть/сдвинуть” is defensible for both. Remedy: in `words/移動.md` set `quiz_exclusions: [移す, 移る, 動かす]` (or add `quiz_exclusions: [移動]` to 動かす), then regenerate the manifest. Evidence: JMdict 移動 (する-noun: “to move; to shift”) and 動かす 1 “to move; to shift”. Confidence: medium (title wording is noun vs verb; necessity from the action sense).

Exclusions beyond EN (basis; necessity):
- 立ち上がる→上がる: 上がる 1 “to rise; to go up”; 立ち上がる 1 “to stand up; to rise”. RU titles do not overlap. Conservative.
- 空き→席: 席 “seat; place”; 空き 1 “vacant seat/room”. Shared “место”. Conservative (the card contrasts 満席).
- 積む→折る: 折る “to fold” overlaps the Russian segment «складывать». Titles differ («складывать в стопку» vs «складывать»). Conservative (weak).
- 穀物→米: 米 “uncooked rice; rice grain”, title «рис (зерно)» shares «зерно». Conservative; the article teaches 米 as a kind of 穀物, not an antonym.
- 稼ぐ→働く: 働く 1 “to work”; 稼ぐ “to earn by working”. Titles differ. Conservative (the card teaches the contrast).
- 根→原因: 根 “root; (fig.) source/cause”; 原因 “cause”. Conservative (the card calls 原因 the direct term).
- 種→話題: 種 “(topic) material, 話の種”; 話題 “topic of conversation”; RU titles «повод для разговора» vs «тема разговора». Required.
- 移動→移す, 移動→移る: 移動する “to move”; 移す 1 “to move; to transfer”, 移る 1 “to move; to shift”; title stem «перем-». Required for 移す (title overlap); 移る conservative.
- 禁煙→禁止: 禁止 “prohibition; ban”; 禁煙 “ban on smoking”. Title stem «запрет». Required.
- 祭→お祭り: identical title «фестиваль» (dedupes in the app); harmless, conservative.
- 祭→お祝い, 祭→祝い: 祭り “festival; feast”; 祝い “celebration”. Titles do not overlap. Conservative (weak: topical relation).
- 祝う→お祝い, 祝う→祝い: 祝う “to celebrate; to congratulate”; お祝い «поздравление; празднование». Required (title overlap «поздравл-/празднов-»).
- 祝い→お祝い: identical segment «празднование». Required.
- 祝い→プレゼント, 祝い→贈り物: 祝い 2 “congratulatory gift”; titles «подарок». Required (segment containment).
- 祝い→お土産: 土産 “souvenir; present”. Conservative (weak; a visit gift is another kind of gift).
- 祝い→記念: 記念 “commemoration”; «ознаменование» ~ «празднование». Conservative.
- 祝い→お祭り: topical relation only; the article itself teaches that 祝い does not replace the festival name. Unjustified, nonblocking.
- 感謝→恩, 礼→恩: 恩 “favour; debt of gratitude”, title «долг благодарности» shares «благодарность». Conservative.
- 確認→チェック: チェック “check; verify”, title «проверка». Required (same segment).
- 確認→テスト: テスト “test; check”, same segment «проверка». Required (identical segment).
- 確認→調べる: 調べる 1 “to examine; to check”, «проверять». Required.

Pairs screened with no further guard needed: 税金–料金/代金/費用 (distinct titles), 神経–精神/心/気, 秒–瞬間/時間, 科目–授業/科学/課, 章–文章/部分/題, 笛–吹く/鳴る/音楽, 穴–口/窓, 動かす–動く/運転, 禁止–制限/許可/規則/違反, 礼儀–行儀 (EN pair retained)/道徳, 稼ぐ–給料, 積む/積もる–集まる/増える, 立ち上がる–起きる/立つ (retained), 空き–暇 (retained)/空く/余裕, 根/種–実/芽/苗/材料/種類/一種. Not inferred transitively.

Optional:
- 祝い→お祭り (and, if the owner prefers fewer guards, 祭→お祝い/祝い and 祝い→お土産) could be dropped; they add distractor suppression without a demonstrated defensible answer.
- 動かす–動く could be revisited only if a quiz shows «работать» ambiguity; not required now.

Limits: JMdict senses are cited from the card records and my own knowledge of the entries, not re-fetched during this review. The title screen reported lexical overlap only; judgments of defensibility are mine. Pronunciation, correctness and comprehension were not reviewed (other facets). The batch intake record, ledger and tracking files were out of scope.

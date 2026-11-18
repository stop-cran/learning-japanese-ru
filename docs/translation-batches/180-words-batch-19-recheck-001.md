Snapshot: learning-japanese-ru, branch full-ru-180-words-19. The recheck covers fix commit 87bb8aa (parent c2967ea, the candidate from the first review). No uncommitted changes are included.
Scope: I read the full diff `git diff c2967ea 87bb8aa`. It changes six files: manifest.json and the words あっさり, せっせと, もりもり, 備える and 破る. I reread each changed line in context. The rest of the batch was reviewed in b180-review.md and is unchanged by this commit. Reviewer: blind read-only reviewer subagent (model not exposed).
Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety CLEAN

Findings:
F1 (破る.md:39), resolved.
- The absolute claim «Но «сломать» сюда не входит» is gone. The line now reads «Но это не значит, что 破る подходит к любой поломке: для сломанной машины подходит 壊す（こわす）, и подставлять вместо него 破る автоматически не нужно.»
- This matches JMdict 1471200: sense 1 is "to tear; to rip; to break; to destroy" (https://jisho.org/search/%E7%A0%B4%E3%82%8B). It also matches the EN point that 壊す, not 破る, suits a broken machine.
- No regression: the list of Russian verbs and the 破れる/破る sentence are unchanged, and the grammar reads naturally.

F2 (備える.md:9), resolved.
- quiz_exclusions now ends with 予習, giving a direct guard against 予習 «подготовка к уроку».
- This matches the existing 準備, 用意 and 支度 precedent. The YAML list is well formed, and no other entries changed.

Optional items:
- あっさり.md:26, resolved. The gloss is now «отказать сразу, не раздумывая», which no longer reuses the きっぱり word «наотрез». It fits JMdict あっさり sense 2 ("readily; without fuss") and the "readily" sense taught on this card. The sentence remains grammatical.
- せっせと.md:18, resolved. «выпалывает сорняки» is the standard collocation (Ožegov: выполоть — удалить при прополке). The translation still matches 草を抜いている, and the Japanese and kana are unchanged.
- もりもり.md:8, resolved. 一生懸命 has been added, consistent with the ばりばり and せっせと guards. The YAML is well formed.
- Declined extra guards (少しも/全く→とても/何; 全く→皆/実に), accepted. These were optional and harmless, and nothing in the files changed for them.

Manifest: the diff is limited to `contentVersion` (fb508efd89f901e4 → e38eba5ccd0be877) and the five edited files' hashes. Each new hash equals the SHA-256 of the file blob at 87bb8aa (checked for all five). No other manifest entries changed.

Optional: none.
Limits:
- I did not rerun word_title_screen.py or link_parity.py on 87bb8aa. No titles or links changed, only exclusions and body text, so their earlier results still apply.
- The contentVersion derivation algorithm was not independently recomputed.

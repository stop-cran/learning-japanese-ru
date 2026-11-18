Snapshot: learning-japanese-ru `2ed9172` (parent `4abbf09`, the commit of review 001); working tree clean. EN source unchanged: learning-japanese-en-frozen `6af98cb`.
Scope: the full diff `4abbf09..2ed9172`, 6 files: words/トップ, 支える, 暮れ, 栗, 豊か and manifest.json. Each changed passage was reread in context. Checks run:
- rutools/word_title_screen.py on the 5 changed words against the whole RU pool;
- rutools/link_parity.py on the same 5 files (all 5 checked, no losses);
- a recompute of the SHA-256 of all 5 changed files against manifest.json (all match).
The guard targets 賛成, 端 and いちばん all exist as cards. Reviewer: the same blind reviewer as in 001; the model is not recorded.
Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety CLEAN.

Findings reconciliation:
F1 (支える–賛成): resolved. words/支える.md:9 is now `[持つ, 助ける, 賛成]`, and the screen reports the pair as "OK … 賛成 «одобрение; поддержка»". Side effects: the screen also flags 支える against サイン and 署名. That is a false positive from the shared stem «подпи» (подпирать / подпись) and existed before this fix, so no new risk.
F2 (暮れ–端): resolved. words/暮れ.md:9 is now `[夕方, 暮れる, 終わり, 最後, 仕舞い, 端]`, and every «конец» title pairs as OK. Side effects: 週末 «выходные; конец недели» still shows as "!!". That is acceptable: «конец года» and «конец недели» are different periods, and EN distinguishes year-end from weekend. This was not part of F2 and needs no guard.
F3 (トップ–いちばん): resolved. words/トップ.md:9 is now `[頂上, 上, いちばん]`. The exclusion is narrow, so it cannot hide any other plausible confusion.
F4 (栗, конский каштан): resolved. Lines 43-44 now read «…конский каштан — другое растение (по-японски トチノキ; европейский вид называют マロニエ). Его сырые семена ядовиты. 栗 — это съедобный каштан.» This is factually correct:
- The genus *Aesculus* is トチノキ属, and Japanese *A. turbinata* is トチノキ.
- The European *A. hippocastanum* is マロニエ / セイヨウトチノキ.
- The raw seeds are toxic, and toxic-when-raw does not contradict the leached 栃餅 use.
The grammar is sound: «Его» clearly refers to «конский каштан». Evidence: ja.wikipedia トチノキ ("有毒"; "マロニエ … セイヨウトチノキ").
F5 (豊か wording): resolved. Lines 40-41 now say that Russian «богатый» can also be a noun («богатые»), that 豊か is only a な-adjective, and that the noun for a person with money is 金持ち. This no longer contradicts JMdict sense 2 "rich; wealthy; well-off" or the title «зажиточный». It agrees with JMdict's part of speech (adj-na only), and the Russian grammar and punctuation are correct. The paragraph still flows, because the preceding sentence ends at «разные утверждения.». Evidence: https://jisho.org/word/豊か .

Optional (status):
- 冊子 «на ресепшене»: optional, declined by owner. The owner's reason holds: RU 受付 is titled «приём; стойка регистрации», and keeping that term is consistent across cards.
- 豊富–多い, 暮れ–晩: optional; no guard, as concluded in 001.
- The screen shows 豊か against 富 «богатство» and 財産 «…богатство» as "!!". This is unchanged from 4abbf09 and not new: an adjective title against noun titles is not a defensible same answer, and EN has the same split (rich vs wealth/property). No action needed.

Limits:
- Only the fix diff and the passages it touches were rechecked. The other 25 articles and 6 navigation pages were covered by review 001 at 4abbf09 and are unchanged by 2ed9172 (diff stat confirms).
- contentVersion was not recomputed (its algorithm was not inspected); the per-file hashes were verified.
- No validator, generator or budget commands were run.
- Russian wording was judged by the reviewer, not by a native speaker.

Snapshot: RU `C:\Users\romanko\repos\learning-japanese-ru`, fix commit 2c33c06 (parent af53715, which was the reviewed candidate); working tree clean. Frozen EN 6af98cb7. The fix diff touches 11 files: manifest.json (hashes plus contentVersion) and words/ケース プラン 典型 出来事 提案 残り 知恵 腹 自宅 計. No generated files (__pycache__, .pyc, .log, .tmp) were committed. `tools/validate.py` (-X utf8 -B): 0 errors.

Scope: Recheck 001 of batch 173. I read the full `git -c core.quotepath=off diff af53715 2c33c06` and reconciled the original findings F1-F6 and the accepted optional items. Re-ran word_title_screen on the retitled words 自宅 腹 提案 出来事 and the newly guarded 残り ケース プラン 典型 計. Searched kanji/, words/ and articles/ for leftover old title wording («брюхо», «инициатива», «собственное жильё», 出来事 — «происшествие»). Owner-declined items were taken as decided and not reopened. The author report and earlier reviews were not read.

Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety CLEAN.

Reconciliation:
- F1 (残り–続き): resolved. 残り.md:9 now reads `[後, 跡, ほか, 続き]`, and the screen shows OK. The remaining unguarded 残る «оставаться» (verb vs noun) was declined by the owner; it is not a defensible answer for a noun prompt.
- F2 (典型–型): resolved. 典型.md:9 adds `quiz_exclusions: [型]`. The new screen hits (≈«примерно», «представление») match only on the stem and are not defensible answers.
- F3 (プラン–料金): resolved. プラン.md:9 adds 料金, and the screen shows OK.
- F4 (ケース–出来事): resolved. ケース.md:9 adds 出来事. After the 出来事 retitle the overlap is also smaller. The other «случай» hits (в таком случае, на всякий случай, несчастный случай = 事故) are set phrases or a narrower meaning, not a correct answer for ケース; 事件 was already guarded.
- F5 (自宅): resolved. Lines 4, 11 and 15 now read «свой дом; своё жильё», consistent with the body (lines 15-16, 38) and kanji/宅.md. The new screen hit 引っ越す «переезжать (менять жильё)» is a verb about moving house, so not a correct answer.
- F6 (腹): resolved. Lines 4 and 12 now read «живот; брюшная область»; おなか stays guarded. The screen hits on «живот-» (動物, 家畜, 鳴く, いる) come from the root of «животное» and are false positives.
- Optional 計–器具: resolved. 計.md:9 adds 器具, and the screen shows OK.
- Optional 提案 title: resolved. Now «предложение (на рассмотрение)», which matches the body (line 15); 案 stays guarded. The owner declined to guard 意見; I agree it is not a defensible answer.
- Optional 提案:20: resolved. «провести выступление на следующей неделе» no longer adds the rescheduling sense.
- Optional 知恵:20: resolved. «обратиться к бабушкиной мудрости (спросить у неё совета)» keeps 知恵 and the idiom; consistent with lines 17 and 22.
- Optional 出来事 title and line 23: resolved. Title and H1 now read «событие; случившееся». Line 23 now reads «сообщает, что что-то произошло». こと stays guarded. words/事件.md:34 still describes 出来事 as «более широкое слово для происшествия или события»: this is a fair comparison in the prose, not a stale copy of the title, so no change is needed.

Findings: none. No regressions found in the changed passages or new titles: grammar and register are sound, and the Japanese and front matter outside the changed fields are unchanged.

Optional: none new.

Limits: Russian naturalness is the reviewer's judgment, not native-speaker validation. word_title_screen matches stems and segments, so semantic overlap with different wording could escape it. Not rechecked: the quiz-generation code, app rendering, and the intake JSON.

Snapshot: learning-japanese-ru `full-ru-169-words-08` @ a9b65b6 (parent 27ba8c1); working tree clean. EN source: learning-japanese-en-frozen @ 6af98cb.
Scope: Recheck of round-1 findings in b169-review.md against `git diff 27ba8c1 a9b65b6`. The diff touches 13 word files and manifest.json, with no kanji pages or new files. Every changed hunk was read in full. Manifest SHA-256 values for all 13 changed files match the files at a9b65b6. Every new quiz_exclusions target exists in words/: 出会う, 少ない, 気持ち, 時間, 具合, 場合, 思わず. word_title_screen.py was rerun on ざっと, もやもや, 様子, 一時, 少々, ばったり and うっかり. The author's "Fix round 1" notes were not read; the diff alone was used as evidence.
Verdicts: correctness CLEAN; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety CLEAN.

Findings: none open. Reconciliation of the round-1 findings:
- Q1: resolved. words/ばったり.md:9 now has `[突然, 急に, 出会う]`.
- Q2: resolved. words/少々.md:9 now has `[少し, ちょっと, 多少, 少ない, 気持ち]`.
- Q3: resolved by retitling, as the owner decided. words/ざっと.md:4 and H1 :12 now read «навскидку; бегло (просмотреть)». The screen still matches the stem «бегло» against ぺらぺら «бегло говорить…». The parentheticals now separate the senses: "skim through" for ざっと and "speak fluently" for ぺらぺら. Neither title is a defensible answer for the other word's prompt.
- Q4: resolved. words/様子.md:9 adds `quiz_exclusions: [具合, 場合]`, a new key placed after tags as the schema requires.
- Q5: resolved. words/一時.md:9 now has `[しばらく, 時間]`.
- Q6: resolved. words/うっかり.md:9 now has `[ぼんやり, ぼうっと, ふと, 思わず]`.
- Q7: resolved by retitling, as the owner decided. words/もやもや.md:4 and its H1 read «туманный; смутно на душе». Line 19 now ends «…и у меня до сих пор неприятный осадок», which matches the JMdict sense "feeling of dissatisfaction; uneasy feeling". The new title describes vagueness, not worry, so it no longer overlaps 心配 «беспокойство; тревога». The screen hits on the stem «смутн» against ぼんやり and ぼうっと are already guarded: もやもや excludes ぼんやり, and ぼうっと excludes もやもや.
- C1: resolved. words/加減.md:42 now reads «некоторая усталость», which matches the next clause about a slight degree and the EN "rather tired".
- R1: resolved. words/ばったり.md:35 now reads «Русские «с размаху», «плашмя» или «с глухим стуком» хорошо передают действие.» The English-only remark about the gloss "plump" is gone. The dropped content was EN-gloss metadata, not a sense or an example, so coverage is not affected.
- R2: resolved. words/急に.md:40 reads «…; значения взяты из словаря.» and words/ふと.md:29 reads «В исходном списке слов стояло 不図…». No «общественный словник» calque remains.

Regression check:
- Every changed sentence is grammatical Russian and keeps the EN meaning.
- One sentence was removed from 約: words/約.md:35 drops the remark about "about" being mistranslated as «о». It applied only to readers working through English. The rule about bounds and stacking stays verbatim, so no EN teaching point is lost for a Russian learner.
- The polish edits are accepted as applied: 一時:25 «час (1:00) на часах», 永遠:41 «вечной названа именно любовь», and でこぼこ:21 «заметно несхожая парочка».
- No Japanese text changed.
- The other new stem hits are pre-existing noise in a different part of speech: 一時 vs time nouns, 少々 vs 半, ばったり vs 会う and 迎える, and うっかり vs 欠点 and 長短. They are outside this fix round.

Optional:
- The screen matches ざっと «бегло (просмотреть)» and 拝見 «просмотр (скромная форма)» on the stem «просм». ざっと is an adverb meaning "cursorily", while 拝見 is a humble noun or verb meaning "viewing", so neither title fits the other word's prompt. No exclusion is needed, but adding one would be harmless.
- The owner declined retitling ぼうっと. That decision is reasonable, because «в полусне; рассеянно» would collide with ぼんやり «смутно; рассеянно».

Limits: Quiz safety was screened by title against the current RU pool; the distractor or fallback algorithm was not run. Only the changed hunks were re-read; unchanged passages rely on the round-1 review. Validator output and the intake JSON were not reviewed. Russian naturalness was judged by the reviewer, not by a native-speaker panel.

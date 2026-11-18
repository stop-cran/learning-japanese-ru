Snapshot: learning-japanese-ru, branch full-ru-180-words-19, candidate c2967ea (parent 1bb1f44). No uncommitted changes are included. Compared with frozen EN 6af98cb. The commit contains no generated files (`__pycache__`/`.pyc`).
Scope: I read all 30 new word articles in full against their EN originals: 少しも 全く 明確 明らか はあ さっぱり すっきり ほっと あっさり きっぱり はきはき きびきび せっせと 破る がちがち かちかち ばりばり 活気 ぴんぴん もりもり ぺろり ぺろぺろ ぱくぱく むしゃむしゃ もぐもぐ ぽつぽつ ぐつぐつ 備える こしらえる 家事.
I checked the 17 navigation-only edits by word diff: kanji/備.md, kanji/破.md, and words かたかた ぐずぐず ぐったり ぐにゃぐにゃ ことこと しっかり ばきばき ぱちぱち びくびく ぶくぶく へとへと ぼそぼそ むかむか もやもや 約束. Each edit only wraps an existing token in a link at the EN link position, and no other text changed. link_parity.py reports 47 files OK. Its one EXTRA, the 準備 link in kanji/備.md, already existed at 1bb1f44 and is not part of this commit.
I ran word_title_screen.py over all 30 batch titles and read the titles and exclusions of about 100 neighbouring RU cards.
I did not read the author report or the intake rationale. Reviewer: blind read-only reviewer subagent (model not exposed).
Verdicts: correctness NEEDS FIX; scoped coverage CLEAN; comprehensibility CLEAN; quiz safety NEEDS FIX (minor)

Findings:
F1; Minor; correctness; words/破る.md:39. The line says «Но «сломать» сюда не входит».
- Problem: this is an absolute claim, and it is false. JMdict sense 1 of 破る is "to tear; to rip; to break; to destroy", and sense 2 is "break through; breach" (for example, ドアを破る and 窓を破って入る). The EN source makes a narrower point. It says only that the gloss "break" is broader than the paper-tearing use, and that 壊す, not 破る, suits a broken machine.
- Impact: the RU line teaches learners that 破る never covers breaking.
- Remedy: replace the second sentence of line 39 with: «Но это не значит, что 破る подходит к любой поломке: для сломанной машины подходит 壊す（こわす）, и подставлять вместо него 破る автоматически не нужно.» Keep the first sentence (the list of Russian verbs) and the 破れる sentence.
- Evidence: https://jisho.org/search/%E7%A0%B4%E3%82%8B (JMdict 1471200, senses 1–2).
- Confidence: high.

F2; Minor; quiz safety; words/備える.md:9.
- Problem: there is no direct guard against 予習. The 予習 title is «подготовка к уроку», and as a する-noun it also has the action sense «готовиться к уроку» (RU rule on the action sense of する-nouns). The 備える title «оснащать; готовиться (к чему-либо)» is therefore a defensible answer for a bare 予習 prompt.
- Precedent: the existing «подготовка» cards 準備, 用意 and 支度 all guard 予習 directly. 備える guards those three but not 予習.
- Remedy: change line 9 to `quiz_exclusions: [持つ, ある, 準備, 用意, 支度, 設備, できる, 予習]`.
- Evidence: titles and exclusions of words/予習.md, 準備.md, 用意.md and 支度.md in the RU tree.
- Confidence: medium.

Optional:
- あっさり.md:26 glosses あっさり断る as «отказать наотрез». That is the same Russian word as the きっぱり title «решительно; наотрез» and its example «наотрез отказался». Ožegov defines наотрез as «решительно, категорически», which is closer to きっぱり than to あっさり ("readily, without fuss"). Suggested replacement: «может значить «отказать сразу, не раздумывая»». The two words are already guarded against each other in the quiz, so this only affects explanation clarity.
- せっせと.md:18: «пропалывает сорняки» is a mild collocation slip, because пропалывать takes the bed as its object (пропалывать грядку). Suggested replacement: «Мама усердно выпалывает сорняки в саду.»
- もりもり «с аппетитом; с приливом сил» and 一生懸命 «изо всех сил» share «сил». The batch already guards the parallel ばりばり–一生懸命 and せっせと–一生懸命 pairs, so adding 一生懸命 to もりもり would be consistent. It is not strictly required.
- Some new guards look harmless but unnecessary: 少しも/全く→とても, 何; 全く→皆, 実に. They copy the ちっとも/全然 precedent and do not damage any quiz.

Limits:
- Links to targets with no RU page were dropped, consistent with RU policy. These are 全て, 完全, こってり, ずけずけ, ぶるぶる, 守る, びりびり, ぱらぱら, しとしと, ざあざあ, じゅうじゅう and the onomatopoeia articles.
- `image:` fields were dropped, which matches the existing RU onomatopoeia cards.
- I checked JMdict sense ranges only for 破る. For the other articles I accepted the citations carried over unchanged from EN.
- The quiz-title screen covered the stems that word_title_screen.py flags plus a manual check of the clusters named in the prompt. It was not an exhaustive semantic pass over all RU titles.
- Polivanov transcriptions in the batch (итидан, годан, бэнто, онигири) follow the standard system. I did not cite an external source for them.

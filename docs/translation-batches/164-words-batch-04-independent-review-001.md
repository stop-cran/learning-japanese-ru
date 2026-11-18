Snapshot: 0501fab (branch full-ru-164-words-04; working tree clean, no uncommitted changes). EN frozen source 6af98cb.
Scope: Fully read, RU next to EN: all 30 new words/*.md (生物 生き物 牛 家畜 熊 猪 馬鹿 猿 酔う 酔っ払い 虎 のんびり 回り くるくる ふらふら うろうろ ぶらぶら ころころ ごろごろ のろのろ 怠ける だらだら 句 文句 不満 不平 ぐずぐず ぐっしょり びしょびしょ ぐしゃぐしゃ), plus the words/しっかり.md diff. Scripted checks: every EN example line is present verbatim in RU; for each link, EN vs RU link sets and target existence; no image/image_scene fields; the titles and quiz_exclusions of all 1603 RU words screened by Russian stem overlap and by a targeted semantic list. validate.py: 0 error(s); no __pycache__ was left behind. Sources: Jisho/JMdict API for まわり, 文句 and 句; Digital Daijisen (weblio) for まわり. Reviewer: Claude (independent reviewer agent). The repo was not modified.
Verdicts: correctness CLEAN; scoped coverage CLEAN; Russian comprehensibility NEEDS FIX (C1, minor); quiz safety NEEDS FIX (Q1).

Findings:
Q1; moderate; quiz safety; words/文句.md:9 (with words/反対.md:5).
  The RU title of 反対 is «возражение; противоположность». 文句 has the JMdict sense "complaint; grumbling; objection" (1505260 s.1). The new card itself teaches this at lines 17 and 19 («жалоба или возражение», 文句がある — «есть возражения»).
  Impact: when 文句 is the prompt, the distractor «возражение; противоположность» is a correct answer by the card's own teaching. Neither side has an exclusion: 文句 has [句, 表現, 言葉] and 反対 has none.
  This risk is new in RU: the EN 反対 title is "opposition; opposite".
  Remedy: words/文句.md:9 -> quiz_exclusions: [句, 表現, 言葉, 反対]
  Evidence: https://jisho.org/api/v1/search/words?keyword=もんく and the repo titles. Confidence: high.
C1; minor; comprehensibility (Russian prose accuracy); words/句.md:17-18.
  Claim: «В лингвистике это «фраза», то есть группа слов». In Russian, «фраза» is not the linguistic term for the English "phrase". The usual meaning is «законченный оборот речи, высказывание, предложение» (Ожегов), which is exactly the reading the card warns against at lines 20-21.
  Impact: a Russian learner reads the title and body «фраза» as "sentence".
  Remedy (replace lines 17-18): «В лингвистике 句 — группа слов, меньшая, чем предложение\n(в русской грамматике ей примерно соответствует словосочетание; ср. «именная группа» в примере ниже).\nРусское «фраза» в подписи понимайте в этом узком смысле, а не как целое предложение.»
  Evidence: Ожегов s.v. «фраза» (from the reviewer's knowledge; not fetched). JMdict 1243940 lists "phrase" separately from "sentence; passage". Confidence: medium-high.

Russian-specific claims checked and accepted:
- 牛 «корова» = female.
- 猪 «кабан» also means a male domestic pig (Ожегов s.v. «кабан», sense 2).
- 酔っ払い «пьяница» = habitual drinker.
- 酔う «меня укачало»: impersonal, the person is not the grammatical subject.
- 家畜: «домашние животные» is commonly understood as pets.
- 句: mora example にほん = 3 morae.
- 馬鹿: register/insult warnings kept. «никого не оскорбляет» for ばかにならない is slightly stronger than EN "need not be" but true.

Added exclusions checked:
- 回り+周り: JMdict 2800530 has no "surroundings" sense, and 1604290 does not list a 回り spelling. Digital Daijisen, however, has one まわり【回り／廻り／周り】 entry, whose surroundings sense is marked «ふつう「周り」と書く». Verdict: justified as a conservative guard, not a defect.
- 回り+回る, 回り+広がる, ころころ+変わる, くるくる+回る, のんびり+休む/静か, 家畜+動物, ぐっしょり/びしょびしょ+ぬれる, and the coordinator's 生物/生き物+動物: each is a defensible direct pair.
- All EN quiz_exclusions are kept.

Optional:
O1 words/くるくる.md:36: «Неподвижный предмет может вращаться на месте» is self-contradictory in Russian. Suggest «Предмет может вращаться на одном месте, никуда не перемещаясь,».
O2 words/ころころ.md:20: «Он то и дело меняет свои слова» is unnatural. Suggest «Он то и дело говорит то одно, то другое.»
O3 words/だらだら.md: the title «литься ручьём» implies more volume than the body's «непрерывной струйкой» (line 15). Either align the body («течёт не переставая, струйками или ручьями») or leave as is, since 汗がだらだら = «пот лил ручьями» is natural.
O4 Weak, EN-parity pairs that are not RU-specific: ぶらぶら–散歩 «прогулка»; のんびり–休み «отдых»; 怠ける vs ごろごろ «валяться без дела» and ぶらぶら «бродить без дела»; 回り vs 辺/近く/近所 «окрестности». This last one would be needed only if the 周り rationale is applied fully. Consider these at the coordinator's discretion.
O5 words/ぐずぐず.md: the title dropped EN "unsettled"; the sense is kept in the body. Acceptable as concise.

Limits:
- Russian dictionary judgments (Ожегов on «фраза» and «кабан») come from reviewer knowledge, not fetched pages.
- The quiz screen covers stem overlap plus a targeted semantic list. It is not an exhaustive semantic comparison of all 1603 titles.
- The JMdict sense numbers cited in cards were spot-checked only for 回り, 周り, 文句 and 句. Other entry IDs were checked as unchanged from EN, not re-fetched.
- No native-speaker or learning-effectiveness claims.

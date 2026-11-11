# Batch 155 semantic review

Read-only review of candidate `19f33adb89ee28a85a4ed47393759cc5e3ed994c`
(parent `f5fb4bcc961cd16d6d6f4f07c4da70d28072e85c`) against frozen English
source `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. The reviewed scope was
the 15 new lessons, their frozen stroke assets, ten navigation-only word
backlinks, and the two counter-gate documentation corrections.

**Disposition: qualified pass; no supported Japanese-content blocker.**
Each card received separate judgments for Japanese factual accuracy,
source-scope fidelity, and Russian clarity. This is not a blanket CLEAN
verdict, fresh record-level dictionary adjudication, or native-speaker
certification.

| Card | Japanese factual accuracy | Source-scope fidelity | Russian clarity |
| --- | --- | --- | --- |
| `印` | **PASS.** Readings, 印刷/印象, voiced じるし, and the 記す caveat are consistent (20, 30–47). | **PASS.** Readings, examples, and cautions are retained (26–47). | **PASS.** Distinctions are clear (20, 45–47). |
| `卵` | **PASS.** 卵子, food usage, 玉子, and the absence of a strict raw/cooked spelling rule are accurately described (20, 30–43). | **PASS.** Source readings, examples, and food/counter caveats are retained (26–43). | **PASS.** Clear and natural distinctions (20, 41–43). |
| `厚` | **PASS.** 厚い/厚意, source-only あか, and 暑い/熱い contrasts are handled correctly (20, 28–32, 42–44). | **PASS.** Source readings and qualifications are retained (24–44). | **QUALIFIED PASS.** The title gloss `доброжелательный` was less exact than the body's `доброта; любезность` (3, 14, 20, 28); refined in the hash-bound follow-up. |
| `双` | **PASS.** 双子, 双方, rare 双ぶ, and lookup-only readings are appropriately qualified (20, 28–34, 43–46). | **PASS.** Source readings, indexed-form warning, and twin caveat are retained (24–46). | **PASS.** The title `два вместе` was slightly literal but clarified in the body (3, 14, 20, 29, 43); refined in the hash-bound follow-up. |
| `叫` | **PASS.** Shouting is distinguished from crying; conjugation and readings are accurate (20, 28–39). | **PASS.** Source readings, verb forms, and 泣く distinction are retained (24–39). | **PASS.** Clear; the title's `восклицать` was less forceful than the body (3, 14, 20); refined in the hash-bound follow-up. |
| `召` | **PASS.** Summons and context-dependent respectful meanings are distinguished; the honorific direction of 召し上がる is correct (20, 28–40). | **PASS.** Source reading, examples, and context qualifications are retained (24–40). | **QUALIFIED PASS.** The title phrase `почтительные действия` was stiff Russian (3, 14); refined in the hash-bound follow-up. |
| `史` | **PASS.** 史学 is correctly limited to history and no kun-reading is invented (20, 30, 39–40). | **PASS.** Source readings, examples, and no-kun warning are retained (26–40). | **PASS.** Concise and clear (20, 39–40). |
| `各` | **PASS.** 各地/各々 readings and distribution nuance are accurate (20, 28–41). | **PASS.** Readings, examples, and 毎 distinction are retained (24–41). | **PASS.** Clear Russian explanation and examples (20, 39–41). |
| `含` | **PASS.** Oral and abstract senses are distinguished; both verbs are correctly identified as transitive (20, 28–42). | **PASS.** Source readings/examples, transitivity, and component qualification are retained (24–42). | **PASS.** Clear, including the distinction between holding liquid and swallowing (40–42). |
| `周` | **PASS.** 口 radical, 周り as a noun, and distinction from 囲 are correct (20, 24, 30–44). | **PASS.** Source readings, vocabulary, and radical contrast are retained (26–44). | **PASS.** Clear and consistent terminology (20, 42–44). |
| `咲` | **PASS.** 咲く is intransitive; 早咲き, 巧咲/巧笑 qualification, and inflection are accurately distinguished (20, 28–42). | **PASS.** Source readings, unusual dictionary example, and grammar notes are retained (24–42). | **PASS.** Detailed but clear; distinctions are well signposted (20, 39–42). |
| `喫` | **PASS.** Food/drink/smoking senses, 喫茶店 sound change, and 喫む restriction are handled correctly (20, 28–40). | **PASS.** Source readings/examples and cautions are retained (24–40). | **PASS.** Clear; vocabulary context limits the broad gloss (20, 38–40). |
| `営` | **PASS.** 営業/経営 distinction, 営む extension, and verb/noun distinction are accurate (20, 30–44). | **PASS.** Readings, examples, and source caveats are retained (26–44). | **PASS.** Clear and appropriate for instructional prose (20, 42–44). |
| `団` | **PASS.** 団体/布団 readings, ateji qualification, and reference-only kun readings are appropriately separated (20, 30–49). | **PASS.** Source readings, vocabulary, and warnings are retained (26–49). | **PASS.** Clear; it appropriately warns against literal 布団 translation (20, 47–49). |
| `囲` | **PASS.** 囲む/囲う transitivity, 囲い noun, and abstract 範囲 are correctly distinguished (20, 30–45). | **PASS.** Source readings, examples, and usage qualifications are retained (26–45). | **PASS.** Clear, with physical and abstract uses distinguished (20, 43–45). |

## Navigation and documentation

The ten word-page diffs add only contextual links to their corresponding
kanji cards: `印` (30), `卵` (24), `厚い` (27), `召し上がる` (27), `周り`
(27), `咲く` (27), `喫茶店` (24), `団体` (28–29), `布団` (36), and `歴史`
(30). No unrelated word-page wording changed.

`docs/PILOT-B.md` (205–210) correctly separates runtime
`CounterGate.typeOpen` availability—Choose in Review with at least two
repetitions and estimated stability of at least 2.0 days, **or** Type already
started (`phase != New`)—from the second distinct real `CounterChoose` day
needed for native acceptance. It states that only one real day is recorded,
the requirement remains unpassed, and the clock/state must not be manipulated.
`docs/translation-methodology.md` (119–126) states the same distinction and
correctly says this is not a two-calendar-day gate.

## Mechanical evidence and qualifications

The reviewer confirmed all 15 stroke JSON blobs have the same Git blob IDs as
the frozen source, parse as schema version 1, use sequential stroke IDs, and
have counts matching the card metadata. All 42 changed paths are within the
requested scope; no runtime or learner-state paths changed. The pre-existing
untracked `tools/__pycache__/` was left untouched. The reviewer ran no tests or
builds, consistent with the read-only request.

Minor non-blocking wording observations remain documented: a `券` example
could use a more precise phrase for a time-limited pass (30, 38); one `刺`
construction is awkward (20); `則` has a slightly stiff particle description;
`劇` repeats the sense of “theatre” in one phrase; `効` uses the less idiomatic
`результативность` for 効果; and `卒` uses unexplained Jōyō-list jargon (34).
No supported Japanese-content blocker was found.

All 45 direct distractor directions remain **UNVERIFIED**; no transitive
closure or quiz-safety conclusion is inferred. No fresh record-level JMdict
adjudication, native-speaker certification, runtime/device/media release,
ordinary activation, checkpoint authority, or full-translation completion is
claimed. Protected `空` remains outside scope and C2 **UNVERIFIED**.

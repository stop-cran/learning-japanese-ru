# B248 correctness-facet review

> Provenance: recorded verbatim from the blind reviewer's returned report. The task runner assigned `gpt-6.1-sol`
> (GPT family), as shown in the runtime agent listing; the reviewer could not see its own execution metadata.
> Reviewed snapshot: `14cc61a3526acddf05f23db55318f168a6d55b44` (tree `6813010a904c7b243be5fd05a86333b6e79affa8`),
> the signed candidate pushed before review.
> Later reconciliation is in `248-words-batch-87-recheck-001.md`.

Snapshot: RU 14cc61a3526acddf05f23db55318f168a6d55b44, parent 848abada5653f7cdee1a8510e02c863be094f19d; HEAD matches; status --porcelain empty at initial and final checks. Frozen EN source: 6af98cb. No repository edits, staging, commits, pushes or branch changes.

Scope: blind, read-only correctness and scoped coverage review of batch 248 (248-words-batch-87). Model identity not verifiable. Each path below was read IN FULL, including front matter, every example, explanation, comparison, note and footer, against its frozen EN counterpart read IN FULL:
- words/派手.md — RU full / EN full
- words/目立つ.md — RU full / EN full
- words/中身.md — RU full / EN full
- words/目次.md — RU full / EN full
- words/狙う.md — RU full / EN full
- words/狙い.md — RU full / EN full
- words/目指す.md — RU full / EN full
- words/あたりまえ.md — RU full / EN full
- words/標準.md — RU full / EN full
- words/思い込む.md — RU full / EN full
- words/仮定.md — RU full / EN full
- words/推定.md — RU full / EN full
- words/目安.md — RU full / EN full
- words/目上.md — RU full / EN full
- words/盛る.md — RU full / EN full
- words/盗難.md — RU full / EN full
- words/盆地.md — RU full / EN full
- words/盆.md — RU full / EN full
- words/皮膚.md — RU full / EN full
- words/案外.md — RU full / EN full
- words/思いがけない.md — RU full / EN full
- words/皮肉.md — RU full / EN full
- words/的確.md — RU full / EN full
- words/百科事典.md — RU full / EN full
- words/白髪.md — RU full / EN full
- words/登場.md — RU full / EN full
- words/発電.md — RU full / EN full
- words/発揮.md — RU full / EN full
- words/発想.md — RU full / EN full
- words/発射.md — RU full / EN full

Also inspected permitted runtime diff, manifest changes and link-only patches in kanji/外.md and words/目下.md, words/課程.md, words/過程.md. Link targets and contextual glosses were checked in the current RU tree. No author reports, other reviewer reports, translation-batch/draft records or tracking file were read.

Verdicts:
- Correctness: NEEDS FIX — words/目次.md (F1), words/目立つ.md (F2). Other 28 cards: CLEAN within the checked scope, meaning no actionable defect established, not exhaustive correctness.
- Scoped coverage: CLEAN for all 30 cards. Original word/reading/jlpt/type/kanji/tags and exclusions are retained; added exclusions do not replace originals. Japanese example sentences and kana payloads match EN; localized surrounding parentheses/separators are not content loss. No required sense, note, example, citation or teaching contrast was established as missing. English-dependent contrasts may be adapted rather than reproduced literally.
- Russian comprehensibility and corpus-wide quiz quality: outside assigned facets; no verdict.

Findings:

F1; severity: medium; facet: correctness; words/目次.md:18; confidence: high; status: unresolved.
Claim: 探しました is translated as «Я нашёл в оглавлении главу, которую хотел прочитать.» EN says “I looked for…”. 探す describes searching, not successful finding. The Russian perfective result asserts an outcome absent from the Japanese and teaches a wrong search/finding equivalence.
Remedy: replace the Russian translation only with «Я искал в оглавлении главу, которую хотел прочитать.»
Evidence: https://www.weblio.jp/content/探す — actual Digital Daijisen entry さがす【捜す／探す】, definition “見つけ出そうとして…”: looking, walking around or asking in an attempt to find. This does not assert discovery. RU/EN example comparison confirms the changed outcome.

F2; severity: low; facet: correctness; words/目立つ.md:19; confidence: high; status: unresolved.
Claim: 彼は背が高いので、よく目立ちます。 becomes «Он высокий, поэтому всегда на виду.» よく qualifies conspicuousness here; it does not establish “always”. The added absolute frequency changes the example and risks teaching よく as всегда.
Remedy: replace the Russian translation only with «Он высокий, поэтому хорошо заметен.»
Evidence: https://www.weblio.jp/content/よく — actual Digital Daijisen adverb entry よく【善く／良く／好く／能く／克く】, sense 2 (high degree: 非常に、たいそう) and sense 6 (frequently: しばしば、たびたび). Neither means invariably/always. The unchanged Japanese and EN “stands out easily” support the degree reading.

Evidence/checks supporting the remaining verdicts:
- Actual Jisho/JMdict entries were inspected for all 30 principal words, not merely search snippets or footer reachability; all principal cited entry IDs match. Actual Digital Daijisen entries cited in the cards were inspected, distinguishing the named dictionary from other aggregator blocks.
- Spelling-specific annotations checked in full Jisho entries: 中味 is marked ateji (1599430); 思い掛けない is marked rarely-used kanji form (1610630); 的確/適確 and てきかく/てっかく occur in 1437290; 白髪 includes はくはつ alongside しらが (1583050); 案外 has the cited na-adjective sense (1154820). No mismatch established.
- Component on/kun readings independently checked through https://kanjiapi.dev/v1/kanji/<character> for all 43 distinct characters: 派手目立中身次狙指思込標準仮定推安上盛盗難盆地皮膚案外肉的確百科事典白髪登場発電揮想射. Direct shell requests failed with 403; web_fetch subsequently returned the actual KANJIDIC-based JSON. This resolves the earlier access limitation. Reading data support reading claims, not historical etymology or phonetic roles. 派手 explicitly retains the project's mixed/on-first classification, not an all-on assertion.
- Russian «метить» checked in https://ru.wiktionary.org/wiki/метить (homonym II, senses 1–2; present мечу), and https://gramota.ru/meta/metit (Kuznetsov homonym 2, aiming sense 1 and colloquial aspiration sense 3). The constructions «метить в чемпионы» and «мечу в победители» fit aspiration toward a role/status. A dictionary need not list each productive substitution verbatim; no defect established.
- Festival naming: https://ru.wikipedia.org/wiki/Обон_%28праздник%29 explicitly states «Обон … или Бон». This is actual established Russian usage supporting the added note, not proof of normative spelling-dictionary coverage. Gramota searches did not yield a festival entry; its unrelated «бон» entry is not counterevidence.
- Technical terminology: https://ru.wikipedia.org/wiki/Кандзи, sections “Чтение кандзи”, “Онъёми” and “Кунъёми”, actually uses «онное чтение» and «исконно японских слов»; https://ru.wiktionary.org/wiki/исконный records the native/original meaning. No factual terminology defect established; these terms' beginner accessibility is a different facet.
- All 30 N2 labels match the frozen EN policy and pinned vocabulary source rows in docs/n2-vocabulary-sources.tsv; aliases 中味, 適確 and 思い掛けない are retained in teaching notes. Word levels were not inferred from component-kanji levels or missing API JLPT values.
- No broken RU links or lost EN links to available RU targets established. Plain text for unavailable 準, 皮/膚, 地味 and 平野 targets is justified. 狙う's added 目指す link targets an existing card. Added exclusion targets have existing cards and plausible overlapping senses.
- Permitted RU read-only validator completed: 0 error(s). This supports structural validation only.

Optional:
- Outside facets; words/発射.md:30 still uses English “catapult” in a learner-facing explanation. The action-versus-apparatus point is retained, so this is not a coverage omission or false Japanese claim. Russian-only replacement: «発射 называет действие запуска, а не пусковое устройство.»
- Outside facets; English “robbery” in 盗難 and “exhibition” in 発揮 have Russian parenthetical glosses; source-list references in 盛る, 百科事典 and 白髪 may be less useful to learners without the English source. These are accessibility observations, not additional correctness findings.

Limits:
No article was left partially read. Dictionary and RU/EN comparison evidence do not constitute a native-speaker corpus study of every example or historical research into every component association. Festival-name usage was verified, but normative Russian spelling-dictionary attestation remains unverified; no exclusive spelling or normative-status claim is made by the card. No consequential unresolved claim beyond F1/F2 was established.
This review does not certify global semantic uniqueness of automatically selected quiz answers. Optional word distractors can leave fallback selection active; retained exclusions and existing targets alone do not prove every generated pool unambiguous. No app/device acceptance, media/package publication, manifest regeneration or whole-repository approval is claimed.

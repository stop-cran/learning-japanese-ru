## Независимое read-only ревью

**Снимки:** кандидат `1619774212fecce63acf398f5591e114c597acc4`, ветка `full-ru-132-skill-search-collection-disposal-kanji`; frozen EN `6af98cb717755690a9ca793e5454a96ebd7a8f9f`. Изменения не выполнялись.

### Покрытие

Успешно прочитаны:

- `.github/copilot-instructions.md`, `instructions/content-structure.instructions.md`;
- все три rubric-файла reviewers;
- `docs/content-format-reference.md`;
- intake, source/semantic freeze, navigation amendment и navigation-scope correction batch 132;
- candidate lessons `kanji/拾.md`, `kanji/捜.md`, `kanji/捨.md`;
- frozen EN counterparts;
- пять изменённых word pages полностью: `words/拾う.md`, `探す.md`, `捨てる.md`, `塵.md`, `落す.md`;
- `words/投げる.md` и correction record, подтверждающие отсутствие допустимой prose-навигации;
- полный KANJIDIC2 capture как JSON-артефакт и записи 拾/捜/捨;
- targeted JMdict capture entries for 拾う, 捜す/探す, 捜査, 捜索, 捨てる, 取捨, 取捨選択, 四捨五入, 投げる и заявленный search-result summary;
- candidate stroke files and frozen-source stroke references;
- exact navigation diff: пять разрешённых ссылок, `投げる.md` не изменён;
- direct distractor metadata и declared nine directions.

Не выполнялись и не заявляются: native-speaker certification, glyph-pixel inspection, app/device/release acceptance, grading approval, actual quiz execution, complete answer-pool/sense-operation proof.

---

## C1 — Japanese/source fidelity и factual correctness

**Вердикт: ACCEPTABLE WITH EVIDENCE LIMITS; конкретной фактической ошибки в проверенном scope не установлено.** Это не полная внешняя языковая сертификация.

Проверенные совпадения:

- `kanji/拾.md:2-11,30-32`: strokes 9, radical 64, readings `シュウ/ジュウ/ひろ.う`, JLPT metadata и distractors соответствуют frozen metadata и KANJIDIC2.
- `kanji/捜.md:2-11,30-35`: strokes 10, radical 64, `ソウ/シュ/シュウ/さが.す`; квалификация `シュ/シュウ` как character-dictionary readings согласуется с заявленным capture summary.
- `kanji/捨.md:2-11,30-31`: strokes 11, radical 64, `シャ/す.てる`; соответствуют KANJIDIC2 и freeze.
- `kanji/捜.md:20,39-47`: distinction `探す/捜す` ограничена как тенденция, а не строгое правило; это соответствует inspected JMdict evidence.
- `kanji/拾.md:41-43`, `kanji/捨.md:42-44`: morphology и semantic contrast не выданы за этимологические факты.

**Evidence boundary:** raw KANJIDIC2 capture был прочитан; JMdict был проверен по заявленным batch entries и targeted matches, но не построчно перечитан как целиком отображённый 24-KB файл. Поэтому verdict не распространяется на все остальные JMdict entries или весь внешний словарь.

**Stroke identity:** stroke files присутствуют в candidate и заявлены как byte-identical frozen-source assets. В локальном RU baseline commit `f6f67d33…` эти новые paths отсутствуют, поэтому сравнение с этим baseline Git tree невозможно; это не следует трактовать как mismatch. Git blob IDs и raw-byte SHA256 не смешивались.

---

## C2 — Scope/navigation/dependency consistency

**Вердикт: CONSISTENT WITH THE SIGNED SCOPE.**

Проверено:

- ровно три новых kanji lessons и три stroke assets;
- пять фактически изменённых word pages соответствуют correction record;
- `words/投げる.md` не изменён, поскольку его единственное `捨` находится в `quiz_exclusions`, а не в learner-facing navigation;
- prose, Japanese text, readings, metadata, examples и quiz arrays в word pages не изменены; изменения — только ссылки:
  - `words/拾う.md:32`
  - `words/探す.md:54`
  - `words/捨てる.md:34`
  - `words/塵.md:21`
  - `words/落す.md:41`
- links resolve to existing `kanji/拾.md`, `kanji/捜.md`, `kanji/捨.md`;
- optional absent Russian pages `words/捜す.md` и `words/四捨五入.md` не были ошибочно созданы;
- direct distractor declarations прочитаны:
  - 拾 → 捨, 指, 押
  - 捜 → 押, 捨, 招
  - 捨 → 拾, 持, 招

### Ordinary quiz negative/fallback safety

**Все девять направлений остаются `UNVERIFIED`:**

1. 拾 → 捨 — `UNVERIFIED`
2. 拾 → 指 — `UNVERIFIED`
3. 拾 → 押 — `UNVERIFIED`
4. 捜 → 押 — `UNVERIFIED`
5. 捜 → 捨 — `UNVERIFIED`
6. 捜 → 招 — `UNVERIFIED`
7. 捨 → 拾 — `UNVERIFIED`
8. 捨 → 持 — `UNVERIFIED`
9. 捨 → 招 — `UNVERIFIED`

Причина: metadata retention и наличие distractor arrays не доказывают answer operation, actual candidate pool или sense constraints. Quiz execution, accepted-answer paths и fallback behavior отдельно не устанавливались. Green validation, если имеется в records, также не заменяет эту проверку.

---

## C3 — Russian novice clarity/comprehensibility

**Вердикт: NO CONFIRMED NOVICE-CLARITY DEFECT IN THE READ SCOPE; NATIVE-SPEAKER CERTIFICATION NOT PROVIDED.**

Положительные проверки:

- learner-facing headings и body на русском;
- основные значения видны в title и первых explanatory lines;
- readings сопровождаются русскими пояснениями и примерами;
- `捜` явно предупреждает, что `シュ/シュウ` не являются рекомендацией обычного написания;
- `探す/捜す` объясняется как tendency, не как абсолютное правило;
- ссылки добавлены в существующий русский текст без изменения его смысла;
- `投げる.md` не получил искусственную ссылку на кандзи.

Ограничение: это проверка структуры и понятности по rubric, не подтверждение естественности каждой русской формулировки носителем языка и не гарантия результата обучения.

### Findings

Подтверждённых consequential findings с узкой обязательной коррекцией не установлено.

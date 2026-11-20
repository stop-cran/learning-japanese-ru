# Batch 214 — independent recheck 001

## Snapshots

| Commit | Tree | Change |
|---|---|---|
| `a371c734a15f44e674e87a3a9ea0c9f147961d90` | `6712ca2c3fe82adc1a20a1e86be3a7a58861d70a` | Initial review snapshot: the signed candidate, pushed before review. |
| `49b86e1aa755384a9310169428754186b5c1045a` | `13be7b43d497aa7dad04ffe403f3f044dfb834f0` | Fix 1: the correctness finding, the accepted correctness optional, the eight comprehensibility findings and the accepted comprehensibility optional notes, with the intake refresh; committed signed and pushed before the rechecks. |
| `32e1a261a4a3fa1db31493fa7a2fd03f78245678` | `80ab6888b522b14d22b9029845103f91b06f0597` | Fix 2 (final candidate): two navigation links in 周囲, raised in the correctness recheck; committed signed and pushed before the remaining rechecks. |

Fix 1 changed eleven word files and regenerated `manifest.json` (`contentVersion` `b951e3a45e9181cc`, 4,534 entries) and the
intake:
- `地区` (lines 4, 9, 12): title and H1 «район; выделенная зона» instead of «округ; выделенная зона» (correctness C1).
  Daijisen 地区 sense 1 («ある限られた範囲内の土地。地域。») and JMdict/Jisho 地区 (district; area; zone; quarter; section;
  region) give an ordinary area; Kuznetsov «район» sense 1 covers it, while «округ» names a formal subdivision. The new
  exact segment «район» is shared with 町 «городок; район» and 辺 «окрестности; район», so both are added as required
  guards; 近所 «окрестности; район поблизости» shares only the stem and is added as a conservative guard. The list is now
  `[地域, 地方, 町, 辺, 近所]`. The coordinator's title screen after the edit found only the pre-existing false friend
  革 «кожа (выделанная)», which the old title already shared.
- `土産` (lines 43–44): a two-sentence note that the title word «гостинец» is a conversational Russian word for such a
  gift, a translation rather than a style label on the Japanese word (correctness optional; Kuznetsov «гостинец»).
- `図` (lines 16, 18, 21): the definition opens «схема, чертёж или другое наглядное изображение»; the first example reads
  «на следующую схему»; the caption sentence keeps the Russian convention after the meaning: «…обозначает
  пронумерованную иллюстрацию, а не количество; в русских текстах такой подписи соответствует «рис. 1» или «схема 1».»
  (comprehensibility 1, modified). «Рис. 1» is the standard Russian figure caption, so it is presented as a caption
  equivalent, not a gloss.
- `国語` (lines 18, 19, 21): «Первый урок — японский как школьный предмет.»; «На школьном уроке японского мы писали
  сочинение.»; 国語の教科書 «учебник по этому предмету» (comprehensibility 2, modified second example, because the
  reviewer's «На уроке этого предмета» does not stand alone in an example).
- `囲む` (line 19): «Мы всей семьёй собрались вокруг стола и поужинали.» (comprehensibility 3, modified). «Вокруг стола»
  restores what テーブルを marks; «всей семьёй» is kept because the following note explains 家族で that way.
- `品` (line 32): «В заголовке этой карточки основное чтение — しな, но так читается не каждое появление знака 品.»
  (comprehensibility 4). EN's metadata wording is not carried over.
- `味方` (line 28): «Словарь помечает 味方 как атэдзи — написание, в котором кандзи подобраны ради звучания.»
  (comprehensibility 5). The participle is repaired and the dictionary name stays in the footer, as in コーヒー.
  Jisho/JMdict 1527070 confirms the ateji note.
- `呼吸` (lines 16, 29): «呼吸 — дыхание как процесс: вдох и выдох.», dropping «респирация» (also the reviewer's optional
  note); and «[息](息.md)（いき）— само дыхание, вдыхаемый и выдыхаемый воздух…», dropping «дух» (comprehensibility 6,
  modified). Jisho/JMdict 息 1404320 gives breath and breathing, concord and steam, with no "spirit" sense; the gloss now
  follows the 息 card. The proposed 一息 sentence is not adopted (see the table below).
- `周囲` (lines 34–38): EN's single sentence that 回り also refers to the space around is replaced by a qualified
  three-way contrast: 周り names the space around or a circumference; 回り, with the same reading, chiefly names rotation,
  a circuit or spreading, and the surroundings are usually written 周り; 環境 is «окружающая среда», conditions of life or
  work, not a place in a circle or a perimeter length (comprehensibility 7, modified). This is a recorded RU deviation
  from EN content, justified by the deck's own 回り card and Jisho/JMdict 周り 1604290 and 回り 2800530. «Прежде всего»
  and «обычно» avoid an absolute denial. In fix 1 the 周り and 環境 mentions stayed plain text, mirroring EN, which links
  only 回り here; the 回り link is kept.
- `国境` (lines 29–30): the opaque «JMdict ограничивает…» sentence is replaced instead of deleted, so the EN information
  survives in usable form: «Ту же запись 国境 можно прочитать и くにざかい (у этого чтения есть ещё написание 国界); в
  этой карточке изучается чтение こっきょう.» (comprehensibility 8, modified). The Jisho entry for 国境 lists
  国境【こっきょう】, 国境【くにざかい】 and 国界【くにざかい】.
- `哲学` (line 20): «форма на 的な делает из него определение «философский».» (comprehensibility optional).
- The intake note now names the fixed cards, and the eleven candidate hashes were refreshed.

Fix 2 wraps the first mentions of 周り and 環境 in `周囲` as `[周り](周り.md)` and `[環境](環境.md)`, with no wording change,
and regenerates `manifest.json` (`contentVersion` `cf2d40b45bfe5d4d`, 4,534 entries) and the intake (note and 周囲 hash).
The correctness recheck observed, outside its facet, that the RU-introduced comparison names two existing cards without
links. `.github/instructions/content-structure.instructions.md:42` asks for links to existing cards at a substantive
introduction or comparison, and EN link parity is not a repository rule. `link_parity.py` reports the two links as EXTRA
by design. 周辺 stays plain because it has no RU card.

Net change from the candidate: one retitle with three added exclusions (地区), one added register note (土産), two added
links (周囲) and reworded prose in nine cards. No Japanese example, reading or EN exclusion changed.

Frozen EN source: `6af98cb717755690a9ca793e5454a96ebd7a8f9f`.

Rechecks reused the original reviewer agent sessions, so each reviewer retained its own blind report. They kept the same model
variants and facets as review 001:
- `gpt-6.1-sol` for correctness;
- `claude-sonnet-5.5` for consistency/quiz safety;
- `grok-4.7` for comprehensibility.

Model assignments are recorded from the task-runner runtime listing. Reviewer prose did not expose separate serving IDs.

The rechecks ran serially. Each reviewer appended to its own report file, which stayed in its session context, and each
recheck message gave it:
- the revised snapshot, its parent and the read-only rules;
- the actual content diff from `a371c73` inline: `49b86e1` for correctness, `32e1a26` for consistency and
  comprehensibility;
- the coordinator's evidence for every change, and the declined items from all three facets with their reasons, without
  the other reviewers' reports;
- the coordinator's disposition of each of its own findings and optional notes.

The correctness recheck came first, on `49b86e1`; fix 2 followed from its navigation observation. Consistency and then
comprehensibility rechecked `32e1a26`. Finally the correctness reviewer received a short fix 2 brief, inspected the
complete `49b86e1..32e1a26` diff and appended a confirmation. The recheck prompts forbade running `tools/build_manifest.py`
or any other generator; all recheck sections state that none was run. The correctness reviewer (at `49b86e1`) and the
consistency reviewer (at `32e1a26`) ran `tools/validate.py` (0 errors); the comprehensibility reviewer and the fix 2
confirmation ran no validator. After every recheck the coordinator confirmed that HEAD was unchanged and that
`git status --porcelain --ignored` was empty.

### Round 1 (`49b86e1`, then `32e1a26`)

| Facet | Scope and result |
|---|---|
| Correctness | At `49b86e1` the reviewer read the actual word diff and surrounding text of all eleven changed cards and the current 周り, 回り, 環境 and 息 cards. It re-inspected Jisho/JMdict entries for 周り, 回り, 環境, 息, 国境 and 図, Daijisen 地区 senses 1–2 (Weblio) and 環境 senses 1–3 (Kotobank). C1 is resolved: the title now includes the ordinary «район», consistent with Daijisen and the examples, and the earlier guards remain. The 土産 note accurately labels the Russian translation, not Japanese register. 国境's three spelling–reading pairs match the dictionary; 周囲 distinguishes the principal 周り/回り senses without banning a variant spelling, as a practical modern-sense contrast; 環境 describes conditions, not a measured perimeter; 呼吸/息 keep breathing and breathed air without inventing exclusive meanings; 図 keeps general visual representation and treats «рис. 1» as a caption equivalent; 国語, 囲む, 品, 味方 and 哲学 preserve their readings and rules. It raised, outside its facet, the unlinked 周り/環境 comparison in 周囲 (fixed in `32e1a26`). Its fix 2 confirmation verified that only two link wrappers changed, with no Japanese or Russian wording change, and that both targets exist and identify 周り（まわり） and 環境（かんきょう）. Correctness and scoped coverage are **CLEAN** for all eleven changed cards. |
| Consistency | At `32e1a26` the reviewer confirmed that the diff from `a371c73` touches eleven cards, the manifest and the intake. Scanning every `words/*.md` title, it found that the exact segment «район» in 地区's new title is shared only with 町, 辺 and 近所; the added guards 町 and 辺 (required) and 近所 (conservative) cover them, 地域/地方 are kept and no other title hit arises. The two 周囲 links are justified under content-structure:42; the 周り, 回り and 環境 cards agree with the new text, and their existing exclusions are untouched. The other ten cards change prose only, with no link, title, kanji or exclusion change; 図 no longer repeats 絵's «рисунок» except as the caption note; 国語 no longer glosses 国語 with 日本語's «японский язык»; 呼吸/息 agrees with the 息 card. The SHA-256 of all batch files matches the tree, all manifest paths exist and the intake diff touches only metadata. O1 and O2 remain optional, and declining them is acceptable. `tools/validate.py` reported 0 errors. Consistency, quiz safety and scoped coverage are **CLEAN**, with no regressions. |
| Comprehensibility | At `32e1a26` the reviewer reread the eleven changed passages and the contrast cards 息, 周り, 回り, 環境, 絵 and 日本語. Findings 1–8 are resolved: 図 no longer uses 絵's title word, and «рис. 1» is a caption equivalent beside «схема 1»; 国語's glosses stay within the school-subject frame; 囲む's «вокруг стола» shows what を marks and «всей семьёй» matches the 家族で note; 品's wording is learner-facing; 味方's ateji sentence parses; 呼吸 drops «респирация» and «дух», separating the process from 息's breathed air; 周囲's three-way contrast matches the linked cards, with «прежде всего»/«обычно» avoiding an absolute denial; 国境 names くにざかい/国界 and scopes the card to こっきょう. It judged the declined 一息 sentence unnecessary because 一呼吸置く already shows a breath used as a pause. The 哲学 line is clear enough, and the 土産 note correctly labels the Russian title. No regressions: 地区's «район» matches its body. Comprehensibility and scoped coverage are **CLEAN**. |

## Reconciliation

| Original finding or recommendation | Status | Evidence |
|---|---|---|
| Correctness C1: 地区 title «округ» narrows the ordinary district sense | **Resolved** | `地区.md:4,9,12`; Daijisen 地区 senses 1–2; JMdict/Jisho 地区; Kuznetsov «округ», «район». Severity unchanged (minor). |
| Correctness optional: 土産 «гостинец» register note | **Resolved** | `土産.md:43–44`; Kuznetsov «гостинец». Reviewer accepted the wording. |
| Correctness optional: 吐く title «рвать (о рвоте)» | **Optional, not adopted** | The current title is correct and matches EN "vomit; utter"; «рвать» is homonymous with "tear", and the body already glosses «меня вырвало». The reviewer kept it optional. |
| Correctness recheck: 周囲 introduces 周り/環境 without links | **Resolved** | Fix 2; content-structure:42; consistency and comprehensibility rechecks and the fix 2 confirmation. |
| Consistency | **No findings** | Review 001 reported none; the recheck found no regression. |
| Consistency optional O1 吸収→吸う, O2 味方/相手 | **Optional, not adopted** | No shared title segment or stem; same rule as the B209–B213 declined optional guards. Reviewer accepted the decline. |
| Consistency limit: RU `kanji/地.md` has an extra 地図 link and leaves 土地 unlinked | **No action** | Pre-existing and outside this batch's diff. |
| Comprehensibility 1: 図 glosses repeat 絵's «рисунок» | **Resolved** (modified wording) | `図.md:16,18,21`; RU 絵 title; «рис. 1» kept as a caption equivalent. |
| Comprehensibility 2: 国語 examples gloss «японский язык» | **Resolved** (modified wording) | `国語.md:18,19,21`; RU 日本語 title. |
| Comprehensibility 3: 囲む «за столом» | **Resolved** (modified wording) | `囲む.md:19`. |
| Comprehensibility 4: 品 author-facing metadata wording | **Resolved** | `品.md:32`. |
| Comprehensibility 5: 味方 ungrammatical ateji sentence naming JMdict | **Resolved** | `味方.md:28`; Jisho/JMdict 1527070. |
| Comprehensibility 6: 呼吸 «дыхание, дух» | **Resolved** (modified) | `呼吸.md:16,29`; Jisho/JMdict 息 1404320. The proposed 一息 one-breath sentence was not adopted: it was the medium-confidence part, beyond EN's scope, and the revised lines already separate the process from the breathed air. Reviewer agreed. |
| Comprehensibility 7: 周囲 says 回り denotes the space around; 環境 missing | **Resolved** (modified wording; moderate) | `周囲.md:34–38`; Jisho/JMdict 周り 1604290, 回り 2800530; RU 回り and 環境 cards. Links completed in fix 2. Recorded RU deviation from EN content. |
| Comprehensibility 8: 国境 opaque JMdict sentence | **Resolved** (modified: replaced, not deleted) | `国境.md:29–30`; Jisho 国境 other forms. |
| Comprehensibility optional: 哲学 的な wording | **Resolved** | `哲学.md:20`. |
| Comprehensibility optional: «респирация» in 呼吸 | **Resolved** | Removed under finding 6. |
| Comprehensibility optional: 商売 contrast with 営業/貿易 | **Optional, not adopted** | EN contrasts neither in the body, and the 商売→貿易 exclusion covers the quiz risk. Reviewer agreed. |
| Comprehensibility optional: 含む contrasts 入れる, not 加える; title-screen false friends | **No action** | As in EN; the reviewer did not require reopening, and the stem hits are false friends. |
| Exclusion classification | **Reviewer differs from author on 3 entries** | The author called 商売→貿易 and 国語→科目 required and 土産→祝い conservative; the consistency reviewer rated 商売→貿易 likely required, 土産→祝い conservative or likely required, and 国語→科目 conservative. The reviewer's classification is recorded as final, with 土産→祝い under likely required. |

Cross-batch note: no link is held for a later batch.

## Final exclusion set

All 28 EN exclusion entries (19 lists) are retained. Ten direct, one-sided entries are added on eight new cards:

- Required (3): 土曜→土曜日, 地区→町, 地区→辺.
- Likely required (2): 土産→祝い, 商売→貿易.
- Conservative (5): 地区→近所, 商人→店員, 国語→科目, 善→道徳, 吸収→夢中.

Android applies each declaration symmetrically, so no reverse declarations were added to baseline cards.

## Final bounded verdicts

- Correctness: **CLEAN** after fixes (地区).
- Scoped coverage: **CLEAN** after fixes (周囲; 呼吸 for the 息 contrast).
- Comprehensibility: **CLEAN** after fixes (図, 国語, 囲む, 品, 味方, 呼吸, 周囲, 国境).
- Cross-file consistency: **CLEAN** throughout.
- Quiz safety: **CLEAN** throughout, including the three 地区 guards added with C1, for the reviewed batch and the
  directly adjudicated pairs. Exclusions are direct pairs, not transitive groups.

Limits: the rechecks reread only the changed passages and the cards needed to judge them; unchanged cards rest on review
001's full reading. The correctness recheck preceded fix 2; its confirmation covered the link markup and targets only,
without a renewed linguistic or manifest audit, and ran no validator. The consistency reviewer did not re-fetch dictionaries,
rerun `link_parity.py` or recompute `contentVersion`. The comprehensibility reviewer did not re-judge quiz-pair safety,
re-read raw JMdict XML restrictions, rerun the title screen or run `tools/validate.py`. The 1947 Diet date in 国会 was not
re-checked against a statute. No native-speaker, learner, app-import, device, media, activation or release acceptance is
claimed.

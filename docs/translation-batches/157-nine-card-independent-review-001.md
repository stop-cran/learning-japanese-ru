> Publication note: machine-local paths in the preserved reviewer-authored report are replaced with descriptive labels. The verbatim original is retained outside this repository; its raw SHA-256 is `ce75ce2009dae927c64a81f9ec69a7900a3c7751e7f94ebd92309d3ea85148cb`.

## Review result

**Qualified review complete.** I found no new substantive content discrepancy in the nine active cards. This is not a semantic CLEAN or a release decision.

### Verification

At packet root `the bound private nine-card candidate packet`:

- `package-manifest.json` matches SHA-256 `4da05222932a381798150b57305c7f234f31c3633cebcbd817c943141b0cd5aa`. All **287** listed files match their recorded byte counts and SHA-256 values.
- `binding-manifest.json` pins source commit `6af98cb717755690a9ca793e5454a96ebd7a8f9f` and predecessor `c9fa34ca61c057d60f4be789917437c3d3bd4197`. I verified all nine active source files and the held 岩 source against their recorded raw hashes and Git blob IDs, plus all **50** predecessor published-file bindings.
- The eight unchanged active articles—孫/宇/宝/寺/専/尊/導/岸—byte-match their original-freeze candidates. The prior report at `the earlier ten-card review report` matches its stated SHA-256 `345b2d0c5c635db77d6876f5e5e5d4fff7c382a10e50fa997f83db6d73a61a16`.
- The derivative records original packet manifest SHA-256 `e39e12c6dcd93741f03b6c77ad0363c6dbb8fe5bde2fb1ac4631d25fc8d2fd92`; that original manifest itself is not separately included here, so I verified it as a recorded provenance binding, not by recomputing the original packet.
- The rebind receipt, closure evidence, and all three backlink diffs are included in the hash-verified packet. The backlinks are limited to one target-link insertion each: words/寺.md → 寺, words/将来.md → 将, and words/海岸.md → 岸.

### Per-card findings and direct distractors

The 27 listed directions match the active cards and structural closure evidence. “Qualified” below refers to the bounded content/source review—not visual recognizability or learner performance.

| Card | Direct distractors | Status and qualification |
|---|---|---|
| 孫 | 係 / 乳 / 好 | **Qualified, unchanged.** The text properly distinguishes standalone まご from the broader 子孫. The foil list is verified; actual visual-confusion risk is untested. |
| 宇 | 守 / 字 / 安 | **Qualified, unchanged.** The article warns against treating 宇 as an ordinary standalone word for space and notes the shared 宀 with 字/守. **Reading coverage is non-exhaustive:** Kanjipedia lists supplemental のき and いえ, absent from the article. |
| 宝 | 字 / 王 / 守 | **Qualified, unchanged.** Although the title could suggest a gemstone, the body clarifies 宝 means treasure and that treasure need not be a gemstone; it also distinguishes 宝 from 王. |
| 寺 | 時 / 待 / 持 | **Qualified, unchanged.** The article identifies the differing left-side components and distinguishes temples from shrines. The 寺 backlink remains attached to standalone てら. |
| 専 | 申 / 東 / 事 | **Qualified, unchanged.** The article cautions about the lower strokes and distinguishes specialization from autocratic rule. **Reading coverage is non-exhaustive:** Kanjipedia lists supplemental ほしいまま, absent from the article. |
| 将 | 状 / 待 / 付 | **Qualified after correction.** The corrected text keeps Kanjipedia’s 外 qualification, separates it from the JMdict limitation, and does not present ひきいる as everyday spelling. The listed foils and backlink are retained; visual-confusion risk is untested. |
| 尊 | 専 / 導 / 首 | **Qualified, unchanged.** The article compares the 専/導 relations and avoids assigning exclusive meanings to pronunciation variants. **Reading coverage is non-exhaustive:** Kanjipedia also lists supplemental みこと. |
| 導 | 尊 / 首 / 待 | **Qualified, unchanged.** The article compares 導 with 尊 and bounds the “draw a conclusion” sense. **Reading/sense coverage is non-exhaustive:** Kanjipedia lists しるべ and conductive heat/electricity senses not covered here. |
| 岸 | 厚 / 午 / 山 | **Qualified, unchanged.** The article distinguishes 岸 from 厚 and explains the 山 radical; 海岸 appropriately narrows the compound to a seacoast. **Reading coverage is non-exhaustive:** Kanjipedia also lists supplemental かどだつ. |

The only active internal distractor relations are 尊→専, 尊→導, and 導→尊. Closure records no active dependency on held cards and no active incoming candidate link or retained published backlink to 岩. The closure evidence is structural only; it does not establish semantic or drawing safety.

### Corrected 将 and scope boundaries

The corrected article SHA-256 is `9845fa88968bcdda62b2f1afc2fe48a2f4a64f94bf864107ae96562657702642`; its source-evidence file `evidence/kanjipedia-sho-001.json` matches `098b670312498d463b7d797a9ad2df610de9a0f4b6d9bb0e9be6fa8783bf12ec`. The live Kanjipedia entry at [将](https://www.kanjipedia.jp/kanji/0003375200) displays 外 before the reading list containing ひきいる and gives sense ① as “ひきいる。また、軍をひきいる人.” The article accurately preserves that qualification. Separately, it says no suitable example was located in the **inspected JMdict snapshot**; Kanjipedia does not establish that such a JMdict example was found. Other supplemental readings remain explicitly non-exhaustive.

Held cards were not reviewed as active content. The prior ten-card report and its synthetic runtime context do not clear this nine-card scope. No pool/voice/ASR, handwriting/drawing, device/IME, acceptance, hold, release, or publication clearance is claimed. No files or checkouts were modified; no JVM, Gradle, or AVD was run.

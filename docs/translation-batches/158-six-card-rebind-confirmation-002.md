<!-- Publication copy: local artifact prefixes sanitized; the original report is preserved separately. Original raw SHA-256: dd68ebda9700c904bb124b73bdb08ac41c77bdfe32ef8dcc5c7f630a49856253. -->

# B158 six-card current-main rebind confirmation

**Verdict: REBIND CONFIRMED against the exact frozen published-main target below, with no checked-file mismatch.** This is a bounded, read-only rebind and direct-metadata neighbor check—not B158 semantic CLEAN, acceptance, hold, adoption, or publication authorization.

## Bound scope and packet integrity

- Exact packet: `review-confirmation-001` (the frozen packet under the coordinator's B158 evidence directory).
- `package-manifest.json` SHA-256: `17bf9c223334187ea89b9fc9c38d48e2e41fa47edd2aec7265937465758c5f85`. All 155 listed payloads were independently checked against recorded sizes and SHA-256 values; zero mismatches.
- `rebind.json` SHA-256: `dc32efd52cb4a83767c1fbab774d3712dca1267a4fc676db60f56e1ea5d56737`.
- `b157-baseline-delta.json` SHA-256: `ce94eb7c572e80ca3417a3064d579baee940686fb4734ae73364d2ce7e2a45fe`.
- Prior six-card review SHA-256: `05763e6d9a5a5f31487bb102033de4e7b51b6414d552ca97e0b84e77e63315bc`. This remains a separate qualified semantic review; it is not replaced or upgraded here.

Only `州`, `巻`, `帯`, `帽`, `幅`, and `幼` are active. Their six card and stroke payloads match the rebind-bound candidate bytes:

| Candidate | Article SHA-256 | Stroke SHA-256 |
|---|---|---|
| 州 | `de3ab7fda7efdf8d2cdf3ae965ed7b457289ba39f238a9e26e34324d9aecb6b8` | `de052131817f358b30fdda7855bd42da9d29ee75724b8d612e62c05f74f3485a` |
| 巻 | `b219ef04894d0943611ecd29a105bdea990d5f447e4d2572efb1245ce00a4d86` | `06235ac3a4796279dae6a8667c097b327bc4263c1751128e00aa478baedfac08` |
| 帯 | `d8122dd57389f7c96166977f1a77035b0ddf1ac8acf3aaa11fda06bbbddb2f2e` | `901b1a6f4d3da2b22601f486983a0981b8962b38f8fc0df227cbe53c37795de0` |
| 帽 | `3319b376653c48f266b3c6dfb3ce7cad7d0134681525d0e4ce50c2c86009b89c` | `34946d810767e502431b2ed4ea8a5f834f14d53c36732cb891cd62ecd71e6eec` |
| 幅 | `1b1dd4167bfed65ba91404b32eadee79fdf17f841f5a6931bcf5950724366ff2` | `0d7c008cbcef470e639140d3d10814c43390c852e7ff2cbc2b18480550defefd` |
| 幼 | `d9b0258c0c76fced746e6233cd0f76540eb42614be352469fcf207b837acc164` | `78bb99597126d74dd21f84e4d19b2dad265f3ed794c0b9675649966cf20dd074` |

`巨` remains held context, not an active card and not a hold decision. The other held-context candidates also remain non-active. No assessment or clearance of their content is made.

## Frozen source and published-main binding

The frozen English source is commit `6af98cb717755690a9ca793e5454a96ebd7a8f9f`, `docs/n2-batch-sources/batch-07.json` (77,030 bytes; SHA-256 `032527291ab28ffe8777b5c5a9a9ab39b5390c7eda6509dbff53ffb47e6577a72`). The 19 externally bound predecessor targets—including direct-foil targets, other held/context targets, and `words/帽子.md`—were matched to the published-main objects and verified unchanged from c9fa. No target-byte mismatch was found.

The published-main target is commit `2b83105f8fc08236a667bf721011c882cdea53d0`, tree `462e27c74e3e58b79048581926d240edc68151e6`, content version `6eb5aadef3ed81b1`; its `manifest.json` SHA-256 is `303c547c1473643a9c90596e01ae5ff4e86239fa56932a6da7e14de711fb7ab7` (2,901 registrations). In the provided checkout, `HEAD` and the cached `origin/main` ref both resolve to that commit, and the worktree is clean. The checkout's branch label is `full-ru-157-nine-card-publish`, not literally `main`; this confirms the requested commit/ref identity in the frozen checkout, not a later live-remote fetch.

The complete frozen c9fa→2b83105 patch was independently reproduced byte-for-byte (`core.quotePath=false`, binary/full-index form): SHA-256 `404d933e597fc5c0127ea1590bd804ea6e22320936c8ab2329b9a85153b6ab43`. Its 34 paths match the baseline-delta inventory; reverse-apply check against the clean target passed. This includes nine B157 card/stroke pairs and the three changed word pages `寺.md`, `将来.md`, and `海岸.md`; the packet snapshots for these additions and pages match the target commit. This patch check establishes delta identity, not semantic or runtime acceptance.

## Backlink and progress checks

`words/帽子.md` has exactly one proposed `[帽](../kanji/帽.md)` wrapper. Removing that wrapper and normalizing line endings yields the published-base page; no other content delta was found. The old caption-segment screen remains bound to c9fa and 15 B158 candidates; it is an unreviewed lexical lead screen, not a current-main six-card pool result. It was not reused as a six-card current-main verdict.

Published-main `docs/translation-progress.json` and its frozen snapshot agree: 2,906 reviewed-current, 8 runtime-blocked, and 5,364 pending (8,278 inventory total). These are already-published B157-era progress values; they are not B158 acceptance evidence.

## Direct distractor metadata and cross-set edges

I compared the `distractors` metadata on the six B158 candidates with the nine B157 additions. Exact listed sets:

| B158 candidate | Direct distractors |
|---|---|
| 州 | 川, 形, 卵 |
| 巻 | 券, 卵, 差 |
| 帯 | 常, 帰, 帽 |
| 帽 | 幅, 席, 晴 |
| 幅 | 福, 富, 帽 |
| 幼 | 力, 約, 切 |

| B157 addition | Direct distractors |
|---|---|
| 孫 | 係, 乳, 好 |
| 宇 | 守, 字, 安 |
| 宝 | 字, 王, 守 |
| 寺 | 時, 待, 持 |
| 専 | 申, 東, 事 |
| 将 | 状, 待, 付 |
| 尊 | 専, 導, 首 |
| 導 | 尊, 首, 待 |
| 岸 | 厚, 午, 山 |

Exact direct cross-set metadata edges: **B157→B158: none; B158→B157: none.** This is only a comparison of explicit direct metadata. It does not imply transitive negative relations, safety of any fallback, co-display/pool behavior, voice behavior, visual/drawing distinction, or learner confusion.

## Qualified findings and non-clearances

The earlier six-card content report remains the source for content/caption findings; its scope and qualifications are preserved, not re-adjudicated by this byte-and-delta confirmation. That report found no confirmed translation or misleading-caption defect in its bounded review. Reading and sense coverage remains non-exhaustive. The secondary “hanging scroll” coverage and frequency question for 幅 remains unresolved. Direct-negative/fallback behavior and visual/drawing confusion remain unverified/untested. The c9fa lexical screen is not elevated to current-main pool evidence.

No semantic CLEAN, acceptance, hold, adoption, release, or publication decision is made. No JVM, Gradle, emulator, or device work was run. No repository, packet, or frozen-source file was changed.
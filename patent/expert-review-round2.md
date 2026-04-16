# Expert Review Round 2 — Compiled Results

**Generated:** Round 2 post-fix review of patent application
**Agents reviewed:** 37 of 37 (all completed)

---

## 1. SCORECARD: CLEAN vs NEW ISSUES

| # | Agent ID | Verdict | New Issues? | Fix Problems? |
|---|----------|---------|-------------|---------------|
| 1 | r2-patent-law-critical | NOT CLEAN | Yes (B1 fwd ref, B2 dup claim, B3 §16 contradiction) | Yes (A1 terminology schism, A2 powered-roller inconsistency) |
| 2 | r2-patent-law-curious | MOSTLY CLEAN | Opportunities only | Minor (§16 parenthetical, wheel-load inconsistency) |
| 3 | r2-mech-eng-critical | NOT CLEAN | Yes (N1-N5 incl. drawings mismatch, terrace transit gap) | Yes (B1 drawings list, B2 terrace transit undefined for 3-part) |
| 4 | r2-mech-eng-curious | NOT CLEAN | Yes (fire hydraulics, 3mm tolerance, retention clips) | None noted |
| 5 | r2-civil-critical | NOT CLEAN | Yes (B1-B4 incl. fig contradictions, elevator reconciliation) | Yes (fig/caption inconsistencies) |
| 6 | r2-civil-curious | NOT CLEAN | Yes (drawings mismatch, §16 contradiction, power path conflict) | None noted |
| 7 | r2-hort-critical | NOT CLEAN | Yes (B1-B4 hort blockers, H1-H6 species/substrate) | Yes (fig depth contradiction) |
| 8 | r2-hort-curious | NOT CLEAN | Yes (drawings mismatch, claim 55/78 conflict, §16 contradiction) | None noted |
| 9 | r2-hosp-critical | NOT CLEAN | Yes (drawings mismatch, §16 contradiction, claim antecedent) | None noted |
| 10 | r2-hosp-curious | NOT CLEAN | Yes (drawings mismatch, §16 contradiction, §15 embodiment conflict) | None noted |
| 11 | r2-mfg-critical | NOT CLEAN | Yes (drawings mismatch, §16 contradiction, elevator dual-def) | None noted |
| 12 | r2-mfg-curious | MOSTLY CLEAN | Minor (cross-ref bugs, orphan number) | None noted |
| 13 | r2-elec-critical | NOT CLEAN | Yes (P1-P11 power engineering gaps) | None noted |
| 14 | r2-elec-curious | NOT CLEAN | Yes (drawings mismatch, §16 contradiction, Fig 8 stale) | None noted |
| 15 | r2-sw-critical | NOT CLEAN | Yes (claim 41 written-desc gap, fire hydraulics, SIL2 gap) | Yes (claim 39 antecedent, sequencing restriction) |
| 16 | r2-sw-curious | NOT CLEAN | Yes (drawings mismatch, §16 contradiction, wheel rating) | None noted |
| 17 | r2-lit-critical | NOT CLEAN | Yes (claim 39/41 antecedent basis, fwd ref, MPF risk) | Yes (hardware-tying broke 112(b)) |
| 18 | r2-lit-curious | NOT CLEAN | Yes (claim 1 IPR-dead, fire disclaimer self-defeating) | Yes (admitted prior art weakens claim 1) |
| 19 | r2-ptab-critical | MOSTLY CLEAN | No new blockers | Claims 43, 39, 41 improved; others unchanged |
| 20 | r2-ptab-curious | NOT CLEAN | Yes (drawings mismatch, claim redundancy) | None noted |
| 21 | r2-landscape-critical | NOT CLEAN | Yes (broken cross-refs, orphan figure, term mismatch) | None noted |
| 22 | r2-landscape-curious | NOT CLEAN | Yes (drawings mismatch, Fig 2 contradiction, §16 contradiction) | None noted |
| 23 | r2-fire-critical | NOT CLEAN | Yes (claim 71 unhedged, pump sizing, drainage conflict) | None noted |
| 24 | r2-fire-curious | NOT CLEAN | Yes (hydraulically impossible pipeline, gas manifold undefined) | None noted |
| 25 | r2-ada-critical | MOSTLY CLEAN | Moderate gaps (accessibility modalities, service animals) | None noted |
| 26 | r2-ada-curious | NOT CLEAN | Yes (drawings mismatch, egress not code-compliant, ADA gaps) | Yes (Fig 2 contradiction) |
| 27 | r2-vc-critical | NOT CLEAN | Yes (claim 39 antecedent, claim 45 orphaned, §19.8 self-wound) | None noted |
| 28 | r2-vc-curious | NOT CLEAN | Yes (drawings mismatch, claim 55/78 conflict, cost model) | None noted |
| 29 | r2-product-critical | NOT CLEAN | Yes (§16 contradiction, interlock non-enabled, drainage gap) | Yes (pan-to-pan interlock species) |
| 30 | r2-product-curious | NOT CLEAN | Yes (drawings mismatch, cross-refs, underground comms gap) | None noted |
| 31 | r2-env-critical | NOT CLEAN | Yes (§16 contradiction, drainage gaps, fertigation cross-contamination) | None noted |
| 32 | r2-env-curious | NOT CLEAN | Yes (dual preferred embodiments, §16 contradiction, Fig 2) | None noted |
| 33 | r2-acoustics-critical | NOT CLEAN | Yes (Fig 2 contradiction, claim 78 "flat bottom", §16/Fig 11) | None noted |
| 34 | r2-acoustics-curious | NOT CLEAN | Yes (§16 contradiction, reference numeral conflicts, Fig 14 gaps) | None noted |
| 35 | r2-network-critical | NOT CLEAN | Yes (802.1s wrong, WiFi 6E constraints, AP mobility, security) | None noted |
| 36 | r2-network-curious | NOT CLEAN | Yes (drawings mismatch, claim 78/55 contradiction, fire claims) | None noted |
| 37 | r2-risk-critical | NOT CLEAN | Yes (egress not passive, fire claim language, AED mobility) | None noted |
| — | r2-risk-curious | NOT CLEAN | Yes (drawings mismatch, emergency egress, fire suppression) | None noted |
| — | r2-illust-critical | NOT CLEAN | Yes (drawings list mismatch, 5 minor figure fixes) | None noted |

### Summary Counts

- **CLEAN (no issues):** 0 agents
- **MOSTLY CLEAN (minor/opportunities only):** 4 agents (patent-law-curious, mfg-curious, ptab-critical, ada-critical)
- **NOT CLEAN (new issues found):** 33 agents

---

## 2. ALL NEW CRITICAL FINDINGS (Not in Round 1)

### TIER 1: UNIVERSAL CONSENSUS BLOCKERS (cited by 20+ agents)

**C1. DRAWINGS LIST MISMATCH (lines 1004-1005)**
Figs 13/14 listed as "Inter-tile manifold" and "Pop-up utility" but actual PNGs are three-part architecture. Result: independent claims 58 and 61 have NO figure; claims 78-89 have figures but are unlisted.
*Cited by:* Nearly every agent. **FIX BEFORE FILING.**

**C2. SECTION 16 INTERNAL CONTRADICTION (line 466)**
States "trough channels do not carry irrigation water (all utilities route through inter-tile manifolds)" immediately before §16.1-16.3 describe sub-channel water delivery. Threatens claims 25, 26, 51.
*Cited by:* 20+ agents. **FIX BEFORE FILING.**

### TIER 2: HIGH-SEVERITY NEW ISSUES (cited by 5+ agents)

**C3. CLAIM 55/78 ANTECEDENT CONFLICT**
Claim 55 requires autonomous self-propelled repositioning; dependent claim 78 says pan has "no integrated drive mechanism." Logical contradiction.
*Cited by:* hort-curious, vc-curious, network-curious, ada-curious, product-curious

**C4. CLAIM 39/41 ANTECEDENT BASIS (§112(b))**
"Roller chassis," "elevator boxes," "tile mesh network," "chassis load cells," "elevator limit switches" used with definite articles but never introduced. Hardware-tying fix created new indefiniteness.
*Cited by:* lit-critical, sw-critical, vc-critical, hosp-critical, mfg-curious, sw-curious

**C5. CLAIM 30 FORWARD REFERENCE + TERMINOLOGY MISMATCH**
References "claim 43" (higher-numbered) and says "horizontal-slide" while claim 43 says "horizontal-transfer."
*Cited by:* patent-law-critical, civil-curious, ptab-curious, landscape-critical, sw-curious, lit-critical

**C6. FIRE-SUPPRESSION HYDRAULICS IMPOSSIBLE (Claims 71, 76)**
2 GPM / 60 PSI micro-pumps in series cannot deliver NFPA sprinkler flows. "Pressure-boosted pipeline" is physically unachievable as described.
*Cited by:* mech-eng-curious, sw-critical, fire-critical, fire-curious, vc-critical, network-curious, risk-critical

**C7. FIG 2 CONTRADICTS §2.3**
Fig 2B shows trough-floor elevator at ~12" travel; §2.3 describes container-integrated lift at 3-6". Fundamentally different mechanisms.
*Cited by:* landscape-critical, landscape-curious, env-curious, acoustics-critical, acoustics-curious, ada-curious

**C8. CLAIM 78/82 "FLAT FEATURELESS BOTTOM" vs ACTUAL PAN CONTENTS**
Pan carries micro-pump, 3-way valve, MCU, manifold connectors, power buffer per spec, but claim says "flat featureless bottom."
*Cited by:* civil-curious, sw-critical, acoustics-critical, risk-curious

### TIER 3: SIGNIFICANT NEW ISSUES (cited by 2-4 agents)

**C9.** Claim 43/48 near-duplicate (both recite 2mm settle) — patent-law-critical, hort-curious, hosp-curious, product-curious
**C10.** "needfor" typo line 39 — 15+ agents (cosmetic but universal)
**C11.** Orphan "682 tiles" in §26.21 — landscape-critical, mfg-curious, product-curious
**C12.** Dangling cross-ref §24.3 "Section 46" — landscape-critical, mfg-curious, product-curious
**C13.** Cross-ref §20.2(l) "Section 18" should be §14.2 — landscape-critical, mfg-curious
**C14.** §15.1 missing space after bold — hort-curious, sw-curious
**C15.** Placeholder text still in lines 6, 9 — lit-curious, vc-curious, risk-curious, acoustics-critical
**C16.** Two incompatible elevator definitions (§15 vs §20B) — mfg-critical, hosp-curious, civil-critical
**C17.** 3mm engagement tolerance insufficient for outdoor conditions — mech-eng-curious, product-critical
**C18.** Pan-to-trough retention force contradiction (wind vs chassis release) — mech-eng-curious, product-critical, risk-critical
**C19.** Sub-surface chassis/elevator communication gap — product-curious, env-curious
**C20.** Emergency egress depends on motion (not passive) — risk-critical, risk-curious, ada-curious
**C21.** Gas fire-feature tiles mechanically undefined for repositioning — fire-curious, risk-critical
**C22.** Weight-reduction percentages inconsistent (35-45% vs 40-60%) — vc-critical
**C23.** Abstract exceeds 150-word limit (~850-1400 words) — 8+ agents
**C24.** Fig 8 system architecture is stale (no three-part, no mesh) — elec-curious, network-critical
**C25.** Claim 1 anticipated by admitted prior art (Harvest/Kiva) — lit-curious, vc-critical, network-curious, ptab-curious

---

## 3. CROSS-DOMAIN CONFLICTS BETWEEN FIXES

| Conflict | Domains | Description |
|----------|---------|-------------|
| **§16 Dry vs Wet** | Civil + Hort + Product + Env | Drainage fix (dry troughs) contradicts hydroponic sub-channel claims 25/26/51. Fig 11 "All channels DRY" vs §16.1-16.3 wet sub-channels. |
| **Claim 39 Alice fix vs §112(b)** | Patent-Law + Litigation + SW | Hardware-tying fix for Alice/§101 introduced antecedent-basis indefiniteness. Net-neutral or worse per lit-critical. |
| **Fire "supplement" disclaimer vs Claims 71/76** | Fire + Risk + Litigation | Spec §26.12 disclaims independent fire suppression, but claims 71/76 positively recite "fire suppression system" without caveat. |
| **§2.3 preferred embodiment vs §20B preferred embodiment** | Env + Civil + Acoustics | Two contradictory architectures both labeled "preferred." Container-integrated lift vs passive pan with separate chassis. |
| **Claim 78 "flat bottom" vs §20B.1 pan contents** | SW + Civil + Acoustics | Claim language contradicts spec description of pump/valve/MCU on pan bottom. |
| **Claim 55 "autonomous" vs Claim 78 "no drive"** | Hort + VC + Network | Parent claim requires self-propulsion; dependent claim removes all drive. |
| **Powered roller on sending only (Claim 43) vs both sides (Claim 48/spec)** | Patent-Law | Claim 43 rewrite recites roller on sending side only; spec and Claim 48 require both sides. |

---

## 4. FIXES VERIFIED AS HOLDING (Round 1 items confirmed resolved)

- ✅ Flexible egress timing (§7) — site-specific, no numeric trap
- ✅ §13.4 power architecture — trough-primary and manifold-primary coexist
- ✅ Cost disclaimer §20B.4 — "illustrative estimates" language present
- ✅ §21.4 weatherproofing cross-ref to §14.11 drain-before-energize
- ✅ Claim 43 rewrite tracks spec (powered roller conveyor)
- ✅ Claims 39/41 Alice §101 hardware-tying (conceptually improved, execution has §112 issue)
- ✅ Fire suppression "supplements" language in §26.12
- ✅ ASCE 7 parametric wind loading
- ✅ Formwork alternatives in §20B.6
- ✅ Figs 15/16 removal (stale references cleaned)

---

## 5. FINAL RECOMMENDATION

### GO / NO-GO: **CONDITIONAL GO for Provisional Filing**

**Rationale:** A provisional patent application has a low formal bar. None of the issues found are fatal for a provisional, which is not examined. However, several issues directly weaken the priority date for key claims and should be fixed in the filing window.

### MUST-FIX BEFORE FILING (4 items, ~1-2 hours)

1. **Fix drawings list (lines 1004-1005)** — Update to describe the three-part architecture figures actually present. Note manifold/pop-up figures are missing. (30 min)
2. **Fix §16 line 466 contradiction** — Scope "do not carry water" to the manifold-only embodiment. One sentence edit. (10 min)
3. **Fix "needfor" typo line 39** and placeholder text lines 6, 9. (5 min)
4. **Fix claim 30 forward-reference** — Either renumber or inline the limitation. Also align "slide" vs "transfer" terminology. (15 min)

### SHOULD-FIX BEFORE FILING (5 items, ~1-2 hours)

5. Fix claim 55/78 conflict (make 78 independent or loosen 55)
6. Fix claim 39/41 antecedent basis (introduce chassis/elevator in preamble)
7. Fix claim 78/82 "flat featureless bottom" to "bottom lacking integrated locomotion hardware"
8. Harmonize fire claims 71/76 with §26.12 "supplement" disclaimer
9. Fix dangling cross-refs (§24.3 "Section 46", §20.2(l) "Section 18")

### FIX IN NON-PROVISIONAL CONVERSION (12-month window)

- Add manifold + pop-up utility figures
- Redraw Fig 2 for consistency with §2.3 or §20B
- Update Fig 8 system architecture
- Add flowchart figure for software method claims
- Trim abstract to 150 words
- Reconcile weight-reduction percentages
- Add sub-surface comms disclosure for chassis/elevator
- Address fire-suppression hydraulics (reframe as misting/cooling)
- Add continuous-egress invariant claim
- Numerous enablement-strengthening paragraphs identified by domain experts

### CROWN JEWEL CLAIMS (strongest after R2 fixes)

1. **Claim 82** — Three-part architecture (pan/chassis/elevator with shared fleet). Strongest novelty.
2. **Claim 43** — Terrace transit (planter never traverses slope). Unique outdoor capability.
3. **Claim 58** — Inter-tile connectivity manifold. Strong standalone licensing vehicle.
4. **Claim 86** — Software-defined landscape zones. Highest commercial value.
5. **Claim 66** — Automated event orchestration with signed readiness report.
6. **Claim 50** — Surface grid + sub-surface tunnel + depot (operational security).
7. **Claim 55** — Universal tile family. Broadest platform claim.

---

*Report compiled from 37 Round 2 expert review agents across 18 domains.*

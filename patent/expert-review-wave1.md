# Expert Review Wave 1: Collated Findings

**Date:** 2025-07-17
**Patent:** Universal Modular Landscape Infrastructure Platform (Provisional)
**Agents:** 20 expert reviewers across 10 domains

---

## Summary Counts

| Agent | Domain | CRITICAL | IMPORTANT | MINOR |
|---|---|:---:|:---:|:---:|
| patent-law-critical | Patent Law | 8 | 12 | 4 |
| patent-law-curious | Patent Law | 3 | 5 | 5 |
| mech-eng-critical | Mechanical Eng | 4 | 6 | 5 |
| mech-eng-curious | Mechanical Eng | 4 | 5 | 4 |
| civil-critical | Civil Eng | 4 | 5 | 4 |
| civil-curious | Civil Eng | 5 | 6 | 6 |
| hort-critical | Horticulture | 5 | 5 | 2 |
| hort-curious | Horticulture/AgTech | 5 | 6 | 3 |
| hosp-critical | Hospitality Ops | 5 | 5 | 4 |
| hosp-curious | Hospitality Ops | 4 | 6 | 3 |
| mfg-critical | Manufacturing | 6 | 6 | 3 |
| mfg-curious | Manufacturing | 3 | 4 | 3 |
| elec-curious | Electrical/Smart Grid | 5 | 7 | 5 |
| sw-critical | Controls/Safety Eng | 6 | 5 | 3 |
| sw-curious | Software/AI | 5 | 8 | 5 |
| lit-curious | IP Litigation | 6 | 3 | 1 |
| ptab-critical | PTAB/IPR | 3 | 3 | 5 |
| ptab-curious | PTAB/IPR | 6 | 8 | 5 |
| landscape-critical | Landscape Architecture | 4 | 4 | 4 |
| vc-critical | Venture Capital | 7 | 5 | 2 |
| **TOTALS** | | **96** | **114** | **80** |

---

## All CRITICAL Findings by Agent

### 1. patent-law-critical (Patent Law, 8 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Claim 1 anticipated by applicant-admitted prior art (Harvest Automation, Iron Ox, Kiva all do "containers + autonomous repositioning + central control") | Rewrite Claim 1 to include trough/flush-seat/lift-slide features from dependent claims 11-12 |
| C2 | Claim 21 ("reconfigurable living barrier") independently anticipated; "operable as" list is non-limiting intended use | Cancel or rewrite to recite trough/manifold/elevator structure |
| C3 | Figs 15-16 listed in spec drawings section but do not exist (only 14 PNGs present) | Produce the missing figures or remove references from spec |
| C4 | Figs 1-2 contradict spec on core mechanism geometry; Fig 2 labeled as §2.3 but illustrates §15 trough-bay elevator; no reference-numeral glossary | Relabel Fig 2; fix cross-references; add ref-numeral index |
| C5 | Abstract is ~1,100 words; USPTO limit is 150 words | Replace with ≤150-word abstract before non-provisional |
| C6 | Claim 43 "low-friction bearing interface" contradicts spec's powered-roller replacement in §14.6.1(c) and Fig 9 | Rewrite Claim 43 to recite powered conveyor as described |
| C7 | Claims 39/41 (method + CRM) fail Alice §101 without inventive-concept tie to hardware | Amend to recite trough-bay elevator + seated-position sensor verification |
| C8 | Power math: §26.20 claims 24 tiles at 100W = 50A = 100% of rated capacity, contradicts §26.19's 80% rule | Replace "24" with "19" or explicitly allow 50A peak with metering/shedding |

### 2. patent-law-curious (Patent Law, 3 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Drawings list out of sync: Figs 13/14 descriptions swapped vs actual files; Figs 15-16 missing | Correct figure numbering/descriptions; produce missing figures |
| C2 | Claim 1 too narrow for three-part embodiment: passive pan cannot "self-propel" but Claim 1 requires it; many dependents (2,11,13,14,16,18,19,20) hang off Claim 1 and are unavailable for three-part architecture | Rewrite Claim 1 to cover both self-propelled and passive-pan-with-cooperating-chassis embodiments |
| C3 | Prior-art collision with Amazon/Kiva (drive unit lifts pod, transports) needs sharper differentiation for three-part architecture | Add explicit Background disclaimer distinguishing warehouse-flat-floor from nested-trough-depth outdoor architecture |

### 3. mech-eng-critical (Mechanical Engineering, 4 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | 3mm chassis lift is geometrically incoherent: ACI 117 slab tolerance is ±6mm; 3mm engagement consumed before first contact; elastic sag under 4,300 lb exceeds stroke | Spec chassis lift ≥15-25mm (screw-jack or cam); publish tolerance stack-up with ≥3x margin; delete "3mm" from claims |
| C2 | Pan floor structure unspecified: 3" concrete floor spanning 3-4 ft open trough at 125 psf is at cracking strength without serious rebar; chassis engages center (max deflection point) | Add floor spec: min 4-5" thick, two-way #4 rebar at 6" OC, or structural steel sub-pan; alternatively use 4-corner bearing with steel box-frame underside |
| C3 | Brake holding force (3,200 lbf) decoupled from tire friction: polyurethane on wet concrete μ=0.3 gives only 1,290 lbf vs 1,113 lbf needed (SF 1.16, not 2.9); slides in freezing rain | Restrict autonomous operation to ≤5° slopes; add mechanical trough-engagement pins as primary holding; or spec tire compound for μ≥0.5 wet |
| C4 | Terrace 2mm settling gap mis-models physics: sum of sending+receiving deflections = 5-15mm; HDG after machining loses ±0.5mm flatness (contradictory spec) | Bridge transfer gap with positively actuated flipper plate; use stainless/nickel-plated bearing pads instead of galvanized A36; restate tolerance as 5-10mm |

### 4. mech-eng-curious (Mechanical Engineering, 4 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Dual-embodiment confusion: §2.3 (container-borne) and §15/§20B (three-part passive pan) are mechanically incompatible but both presented as "preferred" | Rewrite §2 to make three-part the preferred embodiment; relegate container-borne to §18 alternatives |
| C2 | Wicking contradicts dry trough: §16.1-16.3 describes sub-channel wicking water; Fig 11 says "all channels DRY" | Delete sub-channel wicking; make pan self-contained with internal reservoir refilled via inter-tile manifold |
| C3 | Cover-tile delivery mechanism undefined: Fig 14D shows cover tile appearing with no explanation of how it gets there | Add §14.2-a describing chassis-carried or adjacent-pocket-stored cover tile choreography with figure panel |
| C4 | 3mm bearing preload across outdoor freeze-thaw unrealistic: frost heave routinely 3-10mm on 40-ft run | Replace hard preload with compliant tapered self-centering cones (3mm nominal, ±8mm compliance) |

### 5. civil-critical (Civil/Structural Engineering, 4 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Stepped U-channel (Fig 11) not pourable as single monolithic element: re-entrant shelves trap inner formwork; no strip direction for single plug former | Redraw as two-piece precast assembly (U-base + drop-in ledge cap) or three-stack; drop "single concrete form" claim |
| C2 | Ledge bearing capacity unquantified: 3" cantilever ledge in 3" wall has no room for code-cover rebar; 10^4-10^5 fatigue cycles will spall the re-entrant corner | Spec cast-in continuous steel angle at every ledge (composite corbel); increase wall thickness to 5" outer, 4" middle |
| C3 | Thermal expansion over whole-property grids has no joint strategy: 100-ft section moves 0.92" seasonally; frost heave adds 0.25-1.5"; ±0.5mm docking tolerance swamped | Specify isolation expansion joints every 40-60 ft; per-bay local datums; found below frost depth or on gravel capillary break with insulation |
| C4 | "All channels DRY" not physically achievable outdoors: rain enters during reconfig, groundwater infiltrates, condensation; freeze-thaw of trapped water jams chassis | Slope center channel at 0.5% min to sumps; add weep holes at step ledges; specify air-entrained C666/C672 concrete with w/c ≤ 0.40 |

### 6. civil-curious (Civil Engineering, 5 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Hydrostatic uplift/flotation: 3,000+ ft² contiguous slab with air-filled channels in saturated soil is buoyant; troughs will float | Under-slab drainage blanket, relief valves in center channel floor, or ballasted/piled design in hydric soils |
| C2 | Differential settlement (1-5mm) vs ±0.5mm bearing flatness: system not survivable on real subgrade without continuous re-leveling | Add mandatory adjustable shims with automatic compensation, or pile-support every slab section |
| C3 | Freeze-thaw in channels: wet from rain/debris/condensation, ice blocks jam chassis and elevator Nov-Mar in northern climates | Show drainage plan with continuous positive slope (min 1%) to sump locations with powered pumps |
| C4 | Vehicular load rating undefined: §17 claims vehicular-scale but no AASHTO HS-20/HL-93 analysis; fire truck on cover tile = punching shear failure | Provide explicit ratings: pedestrian / H-5 / H-10 / HS-20 variants with commensurate slab thickness |
| C5 | ADA gap at pan/cover transitions: worst-case asymmetric settlement produces 4-5mm vertical offset; no explicit edge geometry detail | Add explicit pan rim chamfer and cover tile edge geometry detail; show compliance under worst-case settlement |

### 7. hort-critical (Horticulture, 5 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Species list unsafe for recirculating hydroponics: Fagus (mycorrhizae-obligate, hates wet feet), Taxus (Phytophthora death sentence), Buxus (boxwood blight vector in shared loop) | Cut list to Nellie Stevens Holly and Thuja 'Green Giant'; relegate others to isolated-loop embodiments |
| C2 | Container volume/root binding: 2.5-3ft depth caps at ~10-12ft hedges, not 15ft; visible decline by year 3-4; reserve ratio needs 15-25% of fleet, not "one spare rack" | Deepen pan to 3.5-4.0ft or cap specified height at 10-12ft; quantify reserve-stock ratio |
| C3 | Wicking physics unsound: LECA 8-16mm has capillary rise of only 1-2 inches, not 12-18in; system is actually drip-fed hydroponic with stagnant sump, not "wicking" | Redesign with 1-2% floor slope to strainer sump; add cleanable false bottom; characterize honestly as drip-fed with reservoir; specify DO targets >5 mg/L |
| C4 | Recirculating water is pathogen superhighway: one infected planter + shared recirc = fleet infection in days; UV/ozone insufficient; §16.4/§16.5 (sterilize vs. inoculate) contradictory | Default to per-planter closed sumps with shared supply only (one-way with backflow prevention + inline UV at supply point) |
| C5 | Wind overturning: 90 mph on 13ft hedge = 12,000-16,000 ft-lb overturning vs 8,600 ft-lb restoring; unit tips at design wind; rootball rotates in loose LECA | Specify tension tie-down from pan to trough; minimum base width ≥ 1/3 hedge height; explicit overturning-moment specs |

### 8. hort-curious (Horticulture/AgTech, 5 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Species list horticulturally unsafe: Taxus extremely Phytophthora-susceptible; Buxus carries blight in recirc; Fagus hates wet feet | Remove Taxus/Buxus; add Podocarpus, Ligustrum, Viburnum; specify compatibility standard rather than species list |
| C2 | Wicking height (12-18in claimed) vs planter depth (30-36in) mismatch: supplementary drip is actually primary, not optional | Rewrite §16.2 to characterize drip as primary irrigation method; wicking as supplementary bottom moisture |
| C3 | Edge-manifold quick-connects are pathogen freeway: every nightly reconfig commingles dozens of root zones | Add per-port check valve + first-flush purge in the manifold engagement sequence (§21.3) |
| C4 | No salinity-bleed/blowdown strategy: closed loop on municipal water becomes phytotoxic within months | Add EC-triggered blowdown to waste; acknowledge water-efficiency tradeoff (70-75%, not 90%+) |
| C5 | LECA + 4-8hr pump failure = system-wide fine-root death: LECA has ~zero water-holding buffer | Spec moisture-reserve horizon (rockwool slab, hydrogel layer, or capillary reservoir) between wicking mat and medium |

### 9. hosp-critical (Hospitality Operations, 5 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Trip hazard from cover tile edge differential: soil/frost heave, debris under covers, wear on lift interface produce gaps exceeding ADA 1/4" limit | Mechanical redundancy: spring-loaded seating indicator + load cell + perimeter contact sensor; physical lockout until flush verified |
| C2 | Medical extraction timing indefensible: cardiac arrest has 4-min window; clearing 30+ pans at 0.5 ft/s = 5-10+ minutes; NFPA 101 requires continuously available egress | Maintain permanent always-open egress corridors regardless of maze configuration |
| C3 | Mid-transit failure + child trapped: 4,300 lb unit stranded above grade with gaps large enough for child's limb; no stated MTBF, response time, or staffing model | Document sub-60-second response with on-property staffed recovery capability |
| C4 | ADA: detectable warnings (truncated domes) cannot be installed on routes that change nightly; blind guests cannot use attraction with changing landmarks | Maintain permanent static accessible configuration; dedicated ADA compliance section with consultant review |
| C5 | Storm/wind response: sequencing 60+ units at 0.5 ft/s takes hours; microbursts arrive in 15 min; ground pins must be passive/always-engaged, not storm-triggered | Make trough ground-pin engagement passive and automatic whenever pan is seated |

### 10. hosp-curious (Hospitality Operations, 4 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Plant stress under repeated repositioning unproven: no empirical basis; mature hedges likely show root disturbance, transplant shock, canopy asymmetry over 3-5 years | Require 24-month horticultural pilot with 8-10 units on named species before full build |
| C2 | Wind loading on 15ft hedge with ~20 sq ft sail area severe: 4,300 lb with high CG marginal in 60+ mph gust without trough engagement | Lock down structural engineering before marketing commitments |
| C3 | Guest safety envelope vs "24/7 magic garden" marketing: if tiles only move when guests absent, "watch it transform" experience requires controlled demo zones | Separate marketing claims for hidden-reconfig vs live-transformation |
| C4 | ADA compliance aspirational: §13.11 says "may be configured to maintain" which is not a commitment; every generated configuration must pass automated accessibility check | Make automated ADA validation a hard constraint, not optional feature |

### 11. mfg-critical (Manufacturing, 6 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | "Single-pour, simple formwork" not manufacturable: three nested cavities with re-entrant corners have no strip direction for rigid forms | Redraw Fig 11 as two-piece composite (lower U-channel + upper frame section) with draft angles ≥1:12 |
| C2 | Junction cross-channels destroy pan-bearing ledge: perpendicular openings cut through the shelf pans rest on | Either prohibit pan placement at junctions (~10-15% grid loss) or add retractable ledge inserts |
| C3 | Cost model off by 3x-10x: pans realistic $2,800-4,500 (not $400-800); chassis $15,000-30,000 (not $2-4k); elevator $20,000-50,000; cover $600-1,200 (not $100-200) | Delete specific dollar figures from patent; replace with qualitative relative-cost statement |
| C4 | Precast tolerance stack-up exceeds manifold self-alignment: cumulative lateral misalignment across 5 slabs (20ft) exceeds 1 inch vs ±0.5" envelope | Reduce to same-slab-only manifold mating; or add floating outer-ledge steel frame surveyed to datum; or widen self-centering to ±1.5" |
| C5 | Embedded A36 bearing plates cannot achieve coplanar precision: standard cast-in tolerance ±1/4" vs needed ±1/32"; plates rotate during vibration/shrinkage | Cast pockets with threaded leveling anchors; set plates post-cast on leveling screws; shim and grout |
| C6 | Outdoor cast-in 48V/50A DC contacts in drainage-channel environment will fail within one season: debris, standing water, corrosion, salt | Move primary power to inter-tile manifold; keep trough contacts only as low-current maintenance injection behind wiper seals |

### 12. mfg-curious (Manufacturing, 3 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | SKU proliferation: 7 sizes x 2 depths = 10-14 SKUs; each needs own tooling, chassis engagement, manifold spacing, covers, spares | Collapse to 3 hero sizes (M, L, SQ) covering ~85% of use cases; express XL as two coupled L pans |
| C2 | Tolerance stackup on manifold mating unvalidated: concrete shrinkage + thermal expansion + freeze-thaw heave across 40ft can exceed 1 inch vs ±0.5" spec | Build 4-pan mockup on representative substrate; measure worst-case misalignment across thermal cycle; likely need ±1.5" float with gimbaled mount |
| C3 | Pan cost estimate optimistic by 2-3x: realistic BOM at 1,000-5,000 units is $1,500-2,500/pan, not $400-800 | Redo BOM with vendor quotes or caveat cost claims more strongly |

### 13. elec-curious (Electrical/Smart Grid Engineering, 5 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | 48V DC at 50A link undersized: §23.6 says 10kW peak/tile (=208A at 48V, 4x link rating); DC fast charging at 48V is impossible (3,125A) | Define dual-bus architecture: 48V SELV for ELV loads + 380V DC backbone for high-power tiles; limit 48V to 2.4kW/link |
| C2 | Arc-fault and hot-unmate safety handwaved: 48V DC at 50A into inductive loads produces destructive arc if contacts part under load; pan lifted while power live | Mandatory de-energization handshake before mechanical separation; mechanical interlock preventing lift while current exceeds threshold; add AFCI per link |
| C3 | Ground-fault detection unspecified for wet DC mesh: centralized GFDI cannot work on a mesh topology; NEC 690/712 thresholds not addressed | Specify per-tile isolation monitor (IMD) architecture with inter-tile fault-localization via differential current measurement |
| C4 | Water + 48V DC in same manifold cavity: dripless disconnects fail after hundreds of cycles; capillary wicking across connectors; DC corrodes faster than AC | Physically separate wet and electrical halves into different cavities with labyrinth seal; add moisture detection per cavity with interlock |
| C5 | Coordinated protection/selectivity on DC mesh not addressed: single fault fed from multiple sources; eFuses don't automatically coordinate | Claim automated protection-coordination service that computes per-eFuse trip curves based on current topology, re-converging after each reconfig |

### 14. sw-critical (Controls/Safety Engineering, 6 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Safety integrity claim malformed: SIL 2 / Cat 3 PL d conflates IEC 61508 and ISO 13849; PL determination for public-access 10,000 lb machine near children likely requires PL e | Drop specific SIL/PL from independent claim; reference ANSI/RIA R15.08 and ISO 3691-4 as applicable standards |
| C2 | Hard-wired E-stop chain over dynamically-mated manifold connectors not safety-rated: connectors cycle tens of thousands of times; topology transiently broken during reconfig | Replace with independent wireless safety protocol (PROFIsafe over WiFi/LoRa) with on-tile safety PLCs |
| C3 | Sensor occlusion by carried hedge defeats collision avoidance: ground-level LIDAR blocked by adjacent 8-15ft opaque hedge walls; child crouched beyond neighboring wall invisible | Add independent safety sensor layer: fixed overhead/perimeter sensors + pressure mats on transit corridors |
| C4 | Live reconfiguration with guests present (§24.5) is different safety case than nightly; falls under ANSI/RIA R15.08 for mobile robots in public spaces | Separate claims into "unattended reconfiguration" (cleared zones) and "attended micro-reconfiguration" (speed-restricted, trained spotter) |
| C5 | Emergency egress "within 5 minutes" not defensible: MAPF for 60 agents on dense grid is NP-hard; cannot pre-cache for 10^23 configurations; one faulted unit blocks the plan | Claim egress as configuration invariant (always-open corridor from every point), not emergency reconfiguration action |
| C6 | Fire suppression via water mesh doesn't meet NFPA 13: 2 GPM per-tile pump vs NFPA's 0.10-0.15 gpm/ft² requirement; serial manifold pressure losses enormous | Recast as auxiliary cooling/misting system; remove "satisfy code-required fire protection" language |

### 15. sw-curious (Software/AI Architecture, 5 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Swarm coordination hand-waved: §18.13 and §24.3 are a single sentence each; NP-hard multi-resource scheduling for 600 pans / 30 chassis / 15 elevators is unproven | Build discrete-event simulator (SimPy/AnyLogic); validate 30-chassis-per-night claim before hardware; publish formulation as companion claim |
| C2 | Digital twin is load-bearing for every safety claim but underspecified: no physics engine named, no fidelity budget, no sim-to-real gap discussion, no calibration | Specify minimum fidelity; state calibration cadence from live sensors; cryptographically bind sim-validated config to twin state |
| C3 | Edge-AI collision avoidance conflicts with fail-safe determinism: ML making motion-permissive decisions is not acceptable under SIL 2 / PL d | Make ML strictly advisory/perception-only; motion authorization from deterministic rule-based envelope checks (LIDAR geometry to safety PLC) |
| C4 | Guest app position tracking has privacy/security gap: live position + dwell-time + cameras = GDPR/CCPA-regulated surveillance platform by default | Specify on-device processing, ephemeral beacon IDs, k-anonymity thresholds, differential privacy, explicit consent UX |
| C5 | ML configuration-generation (§4.1) has no defined reward signal; optimizing "visitor experience" via RL risks dark-pattern layouts (dead-ends near concessions) | Define multi-criteria constrained optimization with hard constraint layer (egress + accessibility + novelty + horticulture stress) |

### 16. lit-curious (IP Litigation, 6 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | §20B.4 cost figures ($400-800/pan, $360k for 600 pans) cap damages testimony by anchoring royalty base | Remove specific cost table from non-provisional |
| C2 | §19.8 dedication sentence threatens to dedicate un-prosecuted subject matter to public; infringers' counsel will cite it | Delete or soften to standard CIP/continuation boilerplate without dedication language |
| C3 | Express prior-art distinguishing statements in Background and §18 create prosecution-history estoppel under Festo on five specific features | Rewrite to describe prior art neutrally; let examiner find distinctions |
| C4 | Functional claiming without algorithmic disclosure (§112(f) vulnerability): "configured to" recitations for control methods lack pseudocode or flowcharts | Add pseudocode or explicit step lists for reservation arbitration, manifold handshake state machine, orchestration solver |
| C5 | Claims tied to "hedge/maze/living plant" lose coverage of modular event flooring, smart-city tiles, etc.; Claim 55 wisely avoids this but others don't | Generalize key claims; add "including but not limited to" definitions; preserve Claim 82's non-plant-requiring scope |
| C6 | Single monster patent filing invites restriction requirement and concentrated IPR attack | Pursue continuation family: separate tile-platform claims (55-77) from maze claims (1-54) |

### 17. ptab-critical (PTAB/IPR Judge, 3 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Claim 1 FALLS: pure §103 combination of Harvest Automation + US 6,855,062 anticipates full scope; every element maps directly | Rewrite Claim 1 with trough-flush-concealment limitation (claims 11-12) |
| C2 | Claim 52 LIKELY FALLS: reads as applied Kiva-style multi-agent coordination; "emergency egress override" is trivial priority rule | Add "within recessed trough grid with inter-terrace vertical-lift transfers" or similar infrastructure hooks |
| C3 | Claim 86 LIKELY FALLS: "software-defined configurable landscape" = Kiva zones applied to landscape tiles; §101 scrutiny in parallel | Cancel or substantially rewrite; add tile-family + physical-repositioning requirement |

*Note: PTAB also rated Claims 29, 55, 61 as TOSS-UP; Claims 42, 50, 51, 54, 58, 66, 82 as LIKELY SURVIVES; Claim 82 as strongest (SURVIVES). Real defensive moat = Claims 50, 51, 58, 82.*

### 18. ptab-curious (PTAB/IPR Judge, 6 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | 18 independent claims: too many broad independents (1, 21, 29, 55, 86) are nearly pure combinations of known elements | Narrow independents; push breadth into dependents; cut or dependent-ize Claims 21, 29, 86, 42 |
| C2 | "Living plants" as claim limitation carries no structural weight under §103 | Move trough-elevator concealment, three-part decomposition, manifold, terrace-transit into independents |
| C3 | Claim 1 reads directly on Harvest Automation; Background (ln 37) names the prior art that anticipates it | Pull up trough-flush-concealment (11-12) and transit-concealment into Claim 1 |
| C4 | Claim 21 should be DROPPED or radically narrowed: structurally identical to Harvest/Iron Ox deployment | Delete or convert to dependent of amended Claim 1 |
| C5 | Claim 86 ("software-defined landscape") overlaps with 55 and invites §101 + §103 attack | Drop or add tile-family limitation + physical-repositioning requirement |
| C6 | Claims 39/41/42 have enablement exposure: generic constraint-satisfaction planning; functional language at point of novelty | Tie methods to physical system (elevator lift, roller transit, trough seating); add explicit structure |

*Crown jewels to prioritize in prosecution: Claim 82 > 52 (with egress-preservation) > 58 > 50 > amended Claim 1 > Claim 43 family (planter never traverses slope).*

### 19. landscape-critical (Landscape Architecture, 4 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Canopy seam between pans always visible: §2.9 mandates canopy separation, but a row of discrete 3-4ft pans reads as "topiary in pots," not a continuous hedge | Allow controlled canopy interlock in upper 18-24" ("handshake zone") with pruning discipline; accept adjacent pans travel together |
| C2 | 2.5-3ft root depth horticulturally implausible for 8-15ft hedges over aesthetic lifespan: chronic stress browning, reduced density (15-25% thinner), uniform decline cycle at year 12 | Deepen pan or explicitly cap height at 6-8ft; plan for visible swap-outs as younger specimens among older ones |
| C3 | LECA/hydroponic media visually wrong: machined pan edge where foliage meets ground; unnaturally crisp, straight ground-to-foliage junction | Specify 3-4" organic topdressing + deliberately irregular "skirt planting" (Hedera, Vinca) cantilevered over pan rim |
| C4 | Cover tile seam is not "seamless": thermal cycling opens 1/8-1/4" gaps; surface weathering differential between covered and walked areas visible under raking light | Specify cover tile material/surface treatment/weathering matching protocols; or accept visible outlines and design around them |

*Additional recommendation: soften "indistinguishable from traditional planted hedge" to "evokes the aesthetic of a traditional hedge maze."*

### 20. vc-critical (Venture Capital, 7 CRITICAL)

| # | Finding | Fix |
|---|---|---|
| C1 | Claim 1 reads on cited prior art (Iron Ox, Harvest, Kiva); examiner will reject under 102/103 in first office action | Narrow Claim 1 per patent-law recommendations |
| C2 | 89 claims / 7+ independent inventions: restriction requirement imminent; prosecution costs explode to $150-300k | Ruthlessly focus on 3 claim families: three-part transport, terrace lift-and-slide, convertible cover/trough grid |
| C3 | Real SAM is tiny: ~200-500 qualified properties globally; 3-8 installs/year at maturity; ~$75M/year revenue at peak = not venture-scale | Narrow vertical focus; get paid-pilot LOIs |
| C4 | No repeatable GTM: every sale is bespoke multi-year custom engineering (18-36 month sales cycle); defense-contractor business model | Build one installation to prove repeatable process before pitching platform |
| C5 | Moat beyond patent is weak: publication in 18 months enables Chinese/Japanese knockoffs of three-part architecture | Invest in horticultural know-how (tacit moat), reference-customer halo, and regulatory precedent |
| C6 | Horticultural viability unproven: no data on whether mature hedges survive repeated transit; plant death in 2 years kills the company | Fund 24-month horticultural study on 3-5 candidate species under realistic transit cycles before priced round |
| C7 | Pop-up 120V GFCI outlet (Claim 61) has commercial prior art: retractable pool-deck and lawn outlets from Hubbell/Lew Electric are existing products | Narrow claim to include sod-plug/turf-continuous + tile-base repositioning elements |

---

## Deduplicated CRITICAL Findings (Unique Issues)

Below are the unique CRITICAL issues consolidated across all 20 agents, with the number of agents that independently flagged each.

### Patent Drafting / Claims

| # | Issue | Agents Flagging |
|---|---|:---:|
| 1 | **Claim 1 anticipated by prior art** (Harvest/Kiva/Iron Ox); must add trough/concealment/flush-grade limitations | 5 (pat-crit, pat-cur, ptab-crit, ptab-cur, vc) |
| 2 | **Claim 21 independently anticipated**; intended-use phrasing adds no structure | 3 (pat-crit, ptab-crit, ptab-cur) |
| 3 | **Claim 86 "software-defined landscape" too abstract**; §101/§103 vulnerable | 3 (ptab-crit, ptab-cur, vc) |
| 4 | **Figs 15-16 missing**; Figs 13-14 descriptions swapped vs actual files | 2 (pat-crit, pat-cur) |
| 5 | **Figs 1-2 contradict spec** on core mechanism geometry | 1 (pat-crit) |
| 6 | **Abstract ~1,100 words** (150-word USPTO limit) | 1 (pat-crit) |
| 7 | **Claim 43 "low-friction bearing"** contradicts spec's powered-roller replacement | 1 (pat-crit) |
| 8 | **Claims 39/41 fail Alice §101** without hardware tie | 2 (pat-crit, ptab-cur) |
| 9 | **Power math inconsistency** (§26.20 vs §26.19 80% rule) | 1 (pat-crit) |
| 10 | **Dual-embodiment confusion** (self-propelled vs three-part passive pan both "preferred") | 3 (pat-cur, mech-cur, mech-crit indirectly) |
| 11 | **Cost figures in spec** cap damages testimony / are 3-10x too low | 3 (lit-cur, mfg-crit, mfg-cur) |
| 12 | **Prosecution-history estoppel** from express prior-art disclaimers in Background/§18 | 1 (lit-cur) |
| 13 | **§19.8 dedication sentence** threatens to dedicate un-prosecuted matter to public | 1 (lit-cur) |
| 14 | **Functional claiming without algorithmic disclosure** (§112(f) vulnerability) | 2 (lit-cur, ptab-cur) |
| 15 | **Too many broad independents** (18 independents invite IPR) | 2 (ptab-cur, vc) |
| 16 | **Pop-up outlet (Claim 61)** has commercial prior art | 1 (vc) |

### Mechanical / Structural

| # | Issue | Agents Flagging |
|---|---|:---:|
| 17 | **3mm chassis lift / bearing preload inadequate** for outdoor tolerances, frost heave | 3 (mech-crit, mech-cur, mfg-crit) |
| 18 | **Pan floor structure unspecified**; likely inadequate as unsupported concrete slab | 1 (mech-crit) |
| 19 | **Brake holding vs tire friction** decoupled on slopes; slides in wet/icy conditions | 1 (mech-crit) |
| 20 | **Terrace 2mm settling gap** mis-models physics (real deflection 5-15mm); HDG-after-machining contradictory | 1 (mech-crit) |
| 21 | **"Single-pour, simple formwork"** not manufacturable; re-entrant corners trap formwork | 3 (civil-crit, mfg-crit, mech-cur) |
| 22 | **Ledge bearing capacity** unquantified; fatigue cracking from 10^4-10^5 load cycles | 1 (civil-crit) |
| 23 | **Thermal expansion** no joint strategy; 0.92" movement over 100ft swamps ±0.5mm tolerance | 2 (civil-crit, mfg-crit) |
| 24 | **"All channels DRY"** not achievable outdoors; contradicts drainage/wicking elsewhere | 4 (civil-crit, civil-cur, mech-cur, mfg-crit) |
| 25 | **Hydrostatic uplift** of empty troughs in saturated soil; no buoyancy analysis | 1 (civil-cur) |
| 26 | **Differential settlement vs sub-mm tolerance** incompatible on real subgrade | 1 (civil-cur) |
| 27 | **Vehicular load rating** undefined despite §17 claims | 1 (civil-cur) |
| 28 | **ADA gap at pan/cover transitions** under worst-case settlement | 2 (civil-cur, hosp-crit) |
| 29 | **Junction cross-channels** destroy pan-bearing ledge continuity | 1 (mfg-crit) |
| 30 | **Cover-tile delivery mechanism** undefined | 1 (mech-cur) |
| 31 | **Precast tolerance stack-up** exceeds manifold self-alignment envelope | 2 (mfg-crit, mfg-cur) |
| 32 | **Embedded A36 bearing plates** cannot achieve needed coplanar precision when cast-in | 1 (mfg-crit) |
| 33 | **Wind overturning moment** exceeds restoring moment at design wind speed | 3 (hort-crit, hosp-crit, hosp-cur) |

### Electrical / Controls / Safety

| # | Issue | Agents Flagging |
|---|---|:---:|
| 34 | **48V/50A link undersized** for stated loads (10kW peak, DC fast charge impossible) | 1 (elec-cur) |
| 35 | **Arc-fault / hot-unmate safety** on 48V DC contactors handwaved | 2 (elec-cur, sw-crit) |
| 36 | **Ground-fault detection** unspecified for wet buried DC mesh | 1 (elec-cur) |
| 37 | **Water + 48V DC in same manifold cavity** = corrosion and tracking failure mode | 1 (elec-cur) |
| 38 | **DC mesh protection coordination** not addressed; cascading trips likely | 1 (elec-cur) |
| 39 | **Outdoor cast-in 48V/50A DC contacts** will fail within one season | 1 (mfg-crit) |
| 40 | **Safety integrity claim malformed** (SIL/PL conflated; likely needs PL e, not PL d) | 1 (sw-crit) |
| 41 | **E-stop chain over dynamically-mated connectors** not safety-rated | 1 (sw-crit) |
| 42 | **Sensor occlusion** by carried hedge defeats collision avoidance LIDAR | 1 (sw-crit) |
| 43 | **Live reconfiguration with guests** = different (unaddressed) safety case | 1 (sw-crit) |
| 44 | **Emergency egress "within 5 minutes"** not defensible (NP-hard MAPF; faulted units block) | 3 (sw-crit, sw-cur, hosp-crit) |
| 45 | **Fire suppression via water mesh** doesn't meet NFPA 13 density by ~10x | 2 (sw-crit, hort-cur) |

### Horticulture / Botany

| # | Issue | Agents Flagging |
|---|---|:---:|
| 46 | **Species list unsafe** for recirculating hydroponics (Fagus, Taxus, Buxus will fail/die) | 2 (hort-crit, hort-cur) |
| 47 | **Container volume / root depth** inadequate for 13-15ft hedges (2.5ft depth insufficient) | 3 (hort-crit, landscape-crit, hosp-cur) |
| 48 | **Wicking physics unsound**: LECA capillary rise only 1-2in, not 12-18in; system is really drip-fed | 2 (hort-crit, hort-cur) |
| 49 | **Recirculating water = pathogen vector**: one infected planter contaminates fleet in days | 2 (hort-crit, hort-cur) |
| 50 | **Salinity bleed/blowdown** absent; closed loop becomes phytotoxic in months | 1 (hort-cur) |
| 51 | **LECA pump failure** = system-wide fine-root death (zero water buffer) | 1 (hort-cur) |
| 52 | **Plant stress under repeated repositioning** unproven; no empirical data | 2 (hosp-cur, vc) |

### Operations / Hospitality / Business

| # | Issue | Agents Flagging |
|---|---|:---:|
| 53 | **Medical extraction timing** indefensible (4-min cardiac window vs minutes-long reconfig) | 1 (hosp-crit) |
| 54 | **Mid-transit child entrapment** scenario unaddressed | 1 (hosp-crit) |
| 55 | **ADA detectable warnings** invalidated by nightly route changes; blind guest access | 2 (hosp-crit, hosp-cur) |
| 56 | **Canopy seam between pans** always visible; reads as "topiary in pots" not continuous hedge | 1 (landscape-crit) |
| 57 | **Cover tile weathering** differential visible; "seamless" claim unsupportable | 1 (landscape-crit) |
| 58 | **LECA/hydroponic media visually wrong** for formal hedge aesthetic | 1 (landscape-crit) |

### Software / AI

| # | Issue | Agents Flagging |
|---|---|:---:|
| 59 | **Swarm coordination** hand-waved; NP-hard scheduling unproven at scale | 1 (sw-cur) |
| 60 | **Digital twin** underspecified but load-bearing for all safety claims | 1 (sw-cur) |
| 61 | **Edge-AI vs fail-safe determinism** conflict; ML cannot make motion-permissive decisions under SIL/PL | 1 (sw-cur) |
| 62 | **Guest position tracking** GDPR/CCPA gap (surveillance platform by default) | 1 (sw-cur) |
| 63 | **ML configuration reward signal** undefined; risk of dark-pattern physical layouts | 1 (sw-cur) |

### Business / Market

| # | Issue | Agents Flagging |
|---|---|:---:|
| 64 | **Real SAM tiny**: 3-8 installs/year; not venture-scale | 1 (vc) |
| 65 | **No repeatable GTM**: bespoke multi-year sales; defense-contractor model | 1 (vc) |
| 66 | **Competitive moat weak** beyond patent; Chinese/Japanese knockoffs feasible after publication | 1 (vc) |
| 67 | **Horticultural viability unproven**: plant death in 2 years kills company | 2 (vc, hosp-cur) |
| 68 | **SKU proliferation**: 10-14 SKUs fragment production runs and undermine scale economics | 1 (mfg-cur) |

---

## Grand Totals

| Severity | Count |
|---|:---:|
| **CRITICAL** | **96** |
| **IMPORTANT** | **114** |
| **MINOR** | **80** |
| **Total findings** | **290** |

**Unique deduplicated CRITICAL issues: 68**

### Top Issues by Cross-Agent Agreement (flagged by 3+ agents independently)

| Issue | Agents |
|---|:---:|
| Claim 1 anticipated by prior art | 5 |
| "All channels DRY" not achievable outdoors | 4 |
| Wind overturning moment exceeds restoring moment | 3 |
| "Single-pour" formwork not manufacturable | 3 |
| 3mm bearing preload inadequate for outdoor conditions | 3 |
| Emergency egress "within 5 minutes" not defensible | 3 |
| Claim 21 anticipated | 3 |
| Claim 86 too abstract / vulnerable | 3 |
| Dual-embodiment confusion (self-propelled vs three-part) | 3 |
| Cost figures in spec are 3-10x too low and cap damages | 3 |
| Container depth inadequate for claimed hedge heights | 3 |

---

*Generated from 20 expert review agents (Wave 1). Each agent ran independently with no access to other agents' findings. Cross-agent agreement on findings indicates high confidence in those issues.*

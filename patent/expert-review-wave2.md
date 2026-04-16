# Expert Review Wave 2: Collated Results

Generated from 28 expert review agents across 14 domains.

---

## Agent Summary Table

| # | Agent | Domain | CRITICAL | IMPORTANT | MINOR |
|---|-------|--------|----------|-----------|-------|
| 1 | elec-critical | Electrical Engineering | 3 | 8 | 4 |
| 2 | sw-critical | Controls Engineering | 6 | 5 | 3 |
| 3 | sw-curious | Software/AI Architecture | 5 | 8 | 5 |
| 4 | lit-critical | IP Litigation (Defense) | 8 | 10 | 4 |
| 5 | lit-curious | IP Litigation (Plaintiff) | 6 | 5 | 2 |
| 6 | ptab-critical | PTAB Judge (Invalidity) | 3 FALLS + 3 TOSS-UP | 5 SURVIVES | 1 SURVIVES |
| 7 | ptab-curious | PTAB Judge (Hardening) | 6 rewrites | 5 keeps | 5 cuts |
| 8 | landscape-curious | Landscape (Theme Park) | 3 | 5 | 4 |
| 9 | fire-critical | Fire Protection | 3 | 4 | 5 |
| 10 | fire-curious | Fire Safety | 5 | 5 | 3 |
| 11 | ada-critical | ADA Accessibility | 4 | 5 | 3 |
| 12 | ada-curious | Universal Design | 3 | 7 | 5 |
| 13 | vc-curious | VC / PropTech | 6 | 5 | 5 |
| 14 | env-critical | Environmental Engineering | 4 | 5 | 3 |
| 15 | env-curious | Sustainability | 4 | 6 | 4 |
| 16 | acoustics-critical | Acoustics | 3 | 6 | 3 |
| 17 | acoustics-curious | Audio Systems | 3 | 7 | 5 |
| 18 | network-critical | Network Engineering | 4 | 5 | 3 |
| 19 | network-curious | Network/IoT | 5 | 7 | 5 |
| 20 | risk-critical | Insurance Underwriting | 4 | 8 | 6 |
| 21 | risk-curious | Risk Management | 3 | 6 | 4 |
| 22 | product-critical | Industrial Design | 5 | 6 | 4 |
| 23 | product-curious | Product Architecture | 3 | 5 | 5 |
| 24 | illust-critical | Patent Illustrations | 2 | 0 | 12 |
| 25 | illust-curious | Technical Visualization | 3 | 0 | 0 |
| 26 | landscape-critical | Landscape Aesthetics | 4 | 4 | 4 |
| 27 | mfg-critical | Manufacturing | 6 | 6 | 3 |
| 28 | mfg-curious | Manufacturing Strategy | 3 | 4 | 3 |
| | **TOTALS** | | **~113** | **~155** | **~111** |

---

## All CRITICAL Findings by Agent

### 1. elec-critical (Electrical Engineering)

**C1. 120V inverter capacity exceeds 48V manifold capacity.**
DC draw of 15-20A inverter at 120V AC saturates/exceeds the 50A @ 48V manifold with zero headroom. 10 kW/tile claim in S23.6 is internally inconsistent.
> Fix: Downrate pop-up outlets to 120V/10A/1.2kW continuous, or require two manifold links with load-sharing, or raise manifold to 80A.

**C2. DC arc hazard at 48V/50A under hot-unmate is understated.**
48V DC >14V will not self-extinguish across opening contact gap. Foreseeable hot-separation events not prevented. Prospective short-circuit current likely >1,000A with distributed batteries.
> Fix: Add electromechanical interlock between pan-lift and contactor; specify DC-rated contactors; add shunt-trip/pyrofuse; include arc-flash calculation; address NEC Article 706.

**C3. GFCI on 48V-derived inverter only works if grounding strategy is specified, and it isn't.**
Neutral bonding undefined (floating neutral GFCI won't trip on line-to-ground fault). 48V DC bus grounding configuration never stated.
> Fix: Require bonded-neutral inverters per NEC 250.34; declare DC bus grounding config; add insulation-resistance monitor per IEC 61557-8.

### 2. sw-critical (Controls Engineering)

**C1. Safety integrity claim (S26.5, Claim 65) is malformed and under-rated.**
Conflates SIL (IEC 61508) with Cat/PL (ISO 13849). PL determination for this hazard class lands on PL e, not PL d. No HAZOP, SRS, fault-reaction times, or PFH budget.
> Fix: Drop specific SIL/PL claim from independent claim; reference ANSI/RIA R15.08 and ISO 3691-4.

**C2. Hard-wired E-stop chain over dynamically-mated manifold connectors is not safety-rated.**
Connectors mate/unmate thousands of times, defeating safety-function reliability. During reconfiguration the E-stop topology is transiently broken.
> Fix: Use independent wireless safety protocol (PROFIsafe over WiFi/LoRa) with on-tile safety PLCs.

**C3. Edge-AI collision avoidance: sensor occlusion by the hedge the tile carries.**
Ground-level LIDAR blocked by adjacent hedge tiles. Cannot see a child crouched beyond neighboring hedge wall.
> Fix: Add independent safety sensor layer (fixed infrastructure sensors + pressure mats on transit paths).

**C4. Live reconfiguration with guests present is a different safety case than nightly reconfiguration.**
Moving 2,000-10,000 lb machines near seated guests has no stop category, minimum separation distance, or verified method for confirming no guest in motion envelope.
> Fix: Separate claims into "unattended reconfiguration" and "attended micro-reconfiguration" with different safety cases.

**C5. Emergency egress "within 5 minutes" is not defensible.**
MAPF is NP-hard; emergency case is worst case. One faulted unit blocks plan. 10^23 configurations cannot all have pre-cached egress sequences.
> Fix: Guarantee every valid configuration already has at least one open emergency corridor from every point (treat egress as configuration invariant, not emergency action).

**C6. Fire suppression via water mesh does not meet NFPA 13 density by ~10x.**
Per-tile micro-pump: 2 GPM at 60 psi. NFPA 13 light-hazard: 150+ gpm total. Pressure losses across serial quick-connects are enormous.
> Fix: Recast as auxiliary cooling/misting system; remove "satisfy code" language.

### 3. sw-curious (Software/AI Architecture)

**C1. Swarm coordination is hand-waved; no algorithm, no bounds, no simulation evidence.**
600 pans, 30 chassis, 15 elevators = NP-hard multi-resource scheduling. "30 chassis relocate 600 pans per night" is unsupported.
> Fix: Build discrete-event simulator (SimPy/AnyLogic) and validate throughput claim.

**C2. Digital twin claim is load-bearing for every safety claim but underspecified.**
No physics engine named, no fidelity budget, no sim-to-real gap discussion, no calibration methodology.
> Fix: Specify minimum fidelity, calibration cadence, version configurations with cryptographic binding.

**C3. Edge AI collision avoidance (S26.13) conflicts with fail-safe determinism (S11.2).**
Neural inference for collision prediction is a SIL-relevant decision. ML making motion-permissive decisions is not acceptable under ISO 13849 PL d.
> Fix: Make ML strictly advisory/perception-only; motion authorization from deterministic rule-based envelope checks.

**C4. Guest app position tracking has privacy/security model gap.**
Live guest position + dwell-time + movement patterns is GDPR/CCPA-regulated PII. Combined with cameras and position-aware audio, this is a surveillance platform by default.
> Fix: Specify on-device processing, ephemeral beacon IDs, k-anonymity thresholds, differential privacy, explicit consent UX.

**C5. ML configuration-generation claim has no reward signal defined.**
Optimizing "visitor experience" via RL tends to produce manipulative layouts (dark patterns in physical space).
> Fix: Define as multi-criteria constrained optimization with hard constraint layer, not blended reward.

### 4. lit-critical (IP Litigation, Defense)

**A1. Background para admits Harvest Automation HV-100 does exactly what Claim 1 recites.**
Binding admission that autonomous container-transport robots existed. Preempts Claim 1 as written.
> Fix: Narrow Claim 1 to include trough-flush-concealment and elevator mechanism.

**A2. S14.13 admits terrace transfer tolerance is "consistent with industry practice for AGV pallet transfer."**
Destroys Claims 44 and 48 (2mm settling) for obviousness.
> Fix: Remove or rephrase the admission.

**I1. Claim 12 "visually indistinguishable" is indefinite.**
Purely subjective aesthetic. No objective reference point. Classic Datamize/Nautilus indefiniteness.
> Fix: Replace with objective measurable criteria.

**I2. Claim 4 "progressive-reveal map" is indefinite.**
Undefined threshold for "immediate vicinity." No metric.
> Fix: Define the reveal distance or mechanism.

**E1. Claim 15 severe-weather mode is non-enabled.**
No bracing geometry, no computed wind-load capacity. Wheel brake rating dangerously close to design failure.
> Fix: Provide actual wind-load analysis and bracing geometry.

**E2. Claim 8 anti-aerial-observation is non-enabled.**
No method of creating path visible from above but ground-discontinuous that adversarial drone cannot detect.
> Fix: Provide specific method or remove claim.

**E3. Claims 39/52/66 software claims have no algorithm disclosed.**
Configuration engine, swarm coordinator, event template solver, digital twin all black-box. Fails S112(f) and S112(a).
> Fix: Add pseudocode or explicit step lists for each.

**101-1. Claim 39 is abstract idea under Alice.**
"Plan, validate, then execute" on generic hardware. Only physical tie is generic "commanding physical repositioning."
> Fix: Add hardware-coupled physical verification steps.

### 5. lit-curious (IP Litigation, Plaintiff)

**C-Claims 50, 55+58, 82 are strongest enforcement targets.** (Strategic, not defects)

**C-Remove cost figures from non-provisional.** S20B.4 cost table ($400-800/pan, $360k for 600 pans) caps damages testimony.
> Fix: Delete specific cost table from non-provisional.

**C-Delete dedication sentence in S19.8.** Gratuitous self-harm that infringers' counsel will cite.
> Fix: Replace with standard CIP/continuation boilerplate.

**C-Soften prior-art distinguishing statements.** Background contains express disclaimers that become prosecution-history estoppel under Festo.
> Fix: Rewrite to describe prior art neutrally.

**C-Add algorithmic disclosure for control methods.** Without pseudocode, software claims fall to S112(f).
> Fix: Add pseudocode or flowcharts for each "configured to" function.

**C-Add S101 Alice inoculation for software claims.** Hardware transformations in method claims.
> Fix: Add "wherein said computing results in the physical engagement of a mechanical coupling."

### 6. ptab-critical (PTAB Judge, Invalidity Assessment)

**Claims 1, 52, 86 FALL.** Claim 1 anticipated by Harvest + US 6,855,062. Claim 52 obvious over Kiva. Claim 86 obvious (software-defined Kiva zones).
> Fix: Rewrite Claim 1 with trough-flush-concealment. Narrow Claim 52 with physical infrastructure hooks. Cancel or rewrite Claim 86.

**Claims 29, 55, 61 TOSS-UP.** Depend on art petitioner can surface.
> Fix: Strengthen with specific structural limitations.

### 7. ptab-curious (PTAB Judge, Hardening)

**Claim 1 must be rewritten** with trough-flush-concealment pulled up from Claims 11-12.
> Fix: Add receiving troughs, seated state, and unoccupied-trough-as-landscape-feature limitations.

**Claim 21 should be dropped or folded into dependents.** Reads on any movable-planter + crowd-control stanchion.
> Fix: Delete or convert to dependent of amended Claim 1.

**Claims 29, 42, 86 overlap heavily.** Consider merging/cancelling to reduce attack surface.
> Fix: Cut to dependents. Make Claim 82 the lead claim.

**Software claims 39, 52, 66 need physical anchors.** Alice S101 exposure.
> Fix: Tie to measured physical state (flow, voltage, link-layer handshake measurements).

**Split into two applications.** Tile platform (Claims 55-77) separate from maze (Claims 1-54).
> Fix: File continuation focused purely on tile platform.

### 8. landscape-curious (Landscape, Theme Park)

**C1. Species list is climate-narrow (temperate only).**
Thuja and Taxus will FAIL in Zone 9b (Florida/California). Patent claims "universal" but species only work in cool-temperate.
> Fix: Add Podocarpus, Ligustrum, Viburnum, Ficus, Pittosporum to S2.2.

**C2. Container root volume too small for 15-ft hedges.**
2.5-3 ft depth for 8-15 ft Taxus/Thuja needs 36+ inch deep root ball. Plants will be chronically stressed.
> Fix: Increase standard depth to 4 ft for L/XL, or cap hedge height at 10 ft in 2.5 ft pans.

**C3. Wind load on 15-ft sail above 4,300 lb pan.**
Safety factor under 1.2 (needs 2.0). Trough anchor pins should be mandatory, not "may include."
> Fix: Move anchor pins from "may include" to "shall include" for ASCE 7 zones >120 mph.

### 9. fire-critical (Fire Protection)

**C1. Water mesh cannot satisfy NFPA 13.**
2 GPM/60 PSI per micro-pump is irrigation, not suppression. NFPA 13 requires 150+ gpm. Moving pop-up heads void hydraulic calculations.
> Fix: Delete/qualify S26.12; remove "satisfies or supplements code-required fire protection" language.

**C2. Egress during active fire with moving walls is a life-safety hazard.**
NFPA 101 requires continuously maintained egress, not "assembled on demand." Moving planters in egress corridors are crushing/tripping hazards.
> Fix: Require every configuration to provide code-compliant egress at rest; fail-safe locks all units on alarm.

**C3. Hedge + facade + trellis = unquantified fuel load with no flame-spread spec.**
No flame-spread, smoke-developed, or combustibility ratings for any surface material. Gas fire-feature tiles adjacent to combustible hedges.
> Fix: Specify ASTM E84 Class A for facades, NFPA 701 for fabrics; enforce separation distance for fire-feature tiles.

### 10. fire-curious (Fire Safety)

**C1. Suppression flow rate is 10x too low.**
2 GPM per pump vs 15-30+ GPM per head for NFPA. AHJs will reject.
> Fix: Reclassify as exposure-protection/pre-wetting system, not "fire suppression."

**C2. Freeze drain-down and fire suppression are mutually exclusive.**
Water mesh fully drained ahead of freezing, exactly when dry hedges create highest ignition risk.
> Fix: Disclose dry-pipe/pre-action embodiment with antifreeze loops.

**C3. Firebreak by retracting combustible payloads is too slow.**
0.5 ft/s = 20-40s to open gap. Radiant ignition of adjacent dry conifers occurs in single-digit seconds. Lowering pan doesn't remove fuel.
> Fix: Clarify firebreak uses horizontal transit to safe bay, not lowering-in-place.

**C4. Thuja/arborvitae as preferred species is a wildfire-safety red flag.**
CAL FIRE, IBHS, NFPA Firewise call these "little green gasoline cans."
> Fix: Add fire-resilient species variant with live fuel moisture monitoring.

**C5. Gas fire-feature tiles adjacent to combustible hedges with no mandated separation.**
No minimum separation, gas shutoff interlock, LEL sensing in trough manifolds where gas can pool.
> Fix: Controller-enforced minimum separation rule; LEL sensor coverage with auto-purge.

### 11. ada-critical (ADA Accessibility)

**C1. Trough seam gap tolerance is aspirational, not engineered.**
"Maximum 1/2 inch" claimed but no mechanism ensures this through thermal cycling, settlement, and swap cycles.
> Fix: Add sensor-verified gap-width interlock; orientation constraints in configuration engine.

**C2. Emergency egress for mobility-impaired guests is not credibly addressed.**
5-minute reconfiguration is disqualifying for fire egress. IBC requires continuously available egress paths. No areas of refuge disclosed.
> Fix: Disclose baseline accessible egress spine never closed by reconfiguration; add areas of refuge.

**C3. Detectable warnings at grade changes and trough edges are unaddressed.**
Terrace risers of 6-24 inches have no disclosed mechanism for wheelchair traversal. No specified visual contrast.
> Fix: Add accessible guest routes between terraces (ramps at <=1:12 or integrated lifts).

**C4. Reconfiguration during operating hours breaks accessible route mid-visit.**
No protection against stranding a wheelchair user on a route fragment disconnected from an exit.
> Fix: Add invariant: accessibility route remains physically valid until guest's exit is confirmed.

### 12. ada-curious (Universal Design)

**C1. Per-visitor adaptive width and turning radius is not claimed.**
Real leverage is moving hedges to widen corridors on demand for specific guests. Not claimed.
> Fix: Add dependent claims for dynamic corridor widening triggered by mobility profile.

**C2. On-demand ramp/level-transition deployment is absent.**
Elevator bays could stage wheelchair-rated transfer platform. No "ramp tile" or "guest elevator tile" in tile family.
> Fix: Add ramp tile member to tile family (Claim 55) and method claim for dispatching to guest route.

**C3. Emergency egress claim does not account for mobility-impaired guests.**
Claim 5 assumes self-evacuation. Egress geometry not generated to satisfy slowest registered guest's parameters.
> Fix: Add "wherein emergency egress configurations satisfy the most restrictive accessibility profile of any guest currently within the maze."

### 13. vc-curious (VC / PropTech)

**C1. No customer, no revenue, no validated willingness-to-pay.**
Zero evidence of signed LOI, pilot site, or hospitality brand partnership.
> Fix: Land one named flagship customer with paid pilot.

**C2. Capex per installation is unfundable at venture scale.**
$20M-$80M construction project per site. VCs do not fund construction.
> Fix: Reframe as software + retrofit-kit licensing business to landscape contractors.

**C3. Combinatorial math argument is a tell.**
Guest doesn't care about 10^27 configurations. Technologist-led project looking for a market.
> Fix: Lead with named anchor experience and specific ROI case.

**C4. Licensing model is completely undefined.**
No royalty structure, certification program, or reference design.
> Fix: Publish reference spec, royalty schedule, and certification program before A round.

**C5. Patent is dangerously broad and will face enablement/obviousness attacks.**
54-89 claims across 10+ inventive categories in a provisional is overreach.
> Fix: File 4-5 focused continuations.

**C6. Horticulture risk is hand-waved.**
Mature hedges in shallow containers being autonomously relocated is a brutal biological problem. Plant mortality could destroy unit economics.
> Fix: Budget 18-24 months of horticultural pilot data before scaling.

### 14. env-critical (Environmental Engineering)

**C1. Nutrient discharge pathway explicitly created; silent on NPDES compliance.**
Dual-use sub-channel is hydraulic short-circuit between fertigation loop and stormwater. Textbook illicit discharge under 40 CFR 122.26.
> Fix: Physical isolation between fertigation and stormwater via air-gapped sump with fail-closed diverter valve.

**C2. Impervious coverage ratio likely non-compliant.**
Near-100% impervious installation. Most municipalities cap new-construction DCIA at 25-50%.
> Fix: Disclose permeable cover tiles, sub-base infiltration gallery, bioretention equivalency calculation.

**C3. Recirculating hydroponic loop = pathogen and pesticide amplifier.**
One contaminated planter can defoliate entire hedge fleet. Recirculated biocides concentrate via evapotranspiration.
> Fix: Elevate S16.4 from "may" to mandatory; add quarantine return line; mandate treatment before discharge.

**C4. Heat island effect from whole-property concrete grid contradicts "environmental buffering."**
Concrete SRI ~0.20-0.25 weathered. Will fail LEED/SITES credits any hospitality buyer will pursue.
> Fix: Require high-albedo concrete (SRI >= 29) or mandate living-cover tiles for unoccupied troughs.

### 15. env-curious (Sustainability)

**C1. Plant palette is ecologically poor and partly invasive.**
All listed species non-native to North America. Prunus laurocerasus is regulated invasive in PNW. Monoculture creates catastrophic disease risk.
> Fix: Require regionally native species, species diversity minimums, climate-regional selection embodiment.

**C2. Closed-loop water claims unquantified; water source unspecified.**
"90%+ efficiency" claim unsupported. No makeup water source, blowdown cycle, transpiration loss accounting.
> Fix: Add rainwater/condensate capture embodiment; disclose blowdown management; provide water-budget methodology.

**C3. Embodied carbon of infrastructure is enormous and undisclosed.**
Thousands of cubic yards of concrete. No low-carbon cement, recycled aggregate, or end-of-life disassembly disclosure.
> Fix: Add low-carbon concrete mixes, recycled reinforcement, EPD/HPD requirement, disassembly/reuse claim.

**C4. Hedges in shallow containers are weak carbon sinks; patent overstates living-system benefits.**
Root volume constrained to 2.5-3 ft in inert medium limits biomass accumulation. Net lifecycle carbon plausibly negative.
> Fix: Do not claim sequestration without LCA. Reframe benefits around evapotranspirative cooling and biophilic value.

### 16. acoustics-critical (Acoustics)

**C1. S26.11 noise budget is per-tile, but reconfiguration is swarm-scale.**
45 dBA per tile x 30 simultaneous tiles = ~60 dBA. Violates WHO 40 dBA Lnight guideline and luxury resort standards.
> Fix: Rewrite as aggregate property-line/guest-facade limit (Lnight < 40 dBA at any occupied room facade).

**C2. Pan-seating impact noise is unbudgeted and probably dominant.**
300-700 lb pan lowering onto concrete trough rim generates broadband thump at 60-90 Hz that carries through hardscape.
> Fix: Require terminal hydraulic damping (last 1/2 inch at <5 mm/s), compliant elastomer seat ring, vibration-isolation break.

**C3. Wheels on concrete at trough-edge crossings generate impulse noise.**
Each wheel-over-edge event is broadband transient 10-20 dB above rolling floor, carries 200+ ft at night.
> Fix: Specify lip geometry (chamfer radius, max gap), or route quiet-hours transit through sub-surface tunnels exclusively.

### 17. acoustics-curious (Audio Systems)

**C1. Auto-delay calibration based on position alone is insufficient outdoors.**
Speed of sound varies ~0.6 m/s per degree C. Wind refraction changes delay by tens of ms. Position-only cal is prior art (Meyer/d&b/L-Acoustics).
> Fix: Add on-tile reference microphones, ambient sensors, closed-loop auto-EQ from distributed mic array.

**C2. "Line-array speakers" is wrong transducer class for hedge maze.**
Line arrays designed for 30-150m throws; in 12-16 ft corridors will exceed safe SPL within 2-3m.
> Fix: Broaden to "point-source, coaxial, column, beam-steered, or line-array speakers."

**C3. Mesh-network latency claim of "acceptable for audio synchronization" is wrong without PTP.**
AES67/Dante/Ravenna require IEEE-1588 PTPv2 with <1 us sync. 20 ms path latency differential produces audible comb filtering.
> Fix: Claim PTP-over-mesh with boundary clocks. Name AES67/Dante/Ravenna as embodiments.

### 18. network-critical (Network Engineering)

**C1. Sub-second reconvergence is inconsistent with cited L2 protocols and movement model.**
MSTP: 1-6s best case. SPB: 500ms-seconds. 682 nodes far exceeds vendor limits (50-100 bridges). Claim 63 is not enabled.
> Fix: Add BFD, TI-LFA, SDN-computed precomputed failover paths; pre-stage FDB entries before transit.

**C2. Tile transit creates 6-40 second network outage per tile, contradicts "sub-second" claim.**
Moving tile has no wired fabric during transit. Distinction between mesh-reconvergence and tile-reattachment not made.
> Fix: Distinguish remainder-of-mesh reconvergence from moving tile's re-attachment latency.

**C3. WiFi channel planning for 682 co-located APs not addressed; 6 GHz outdoor has regulatory gates.**
2.4 GHz: 227 APs per channel (unusable). 6 GHz outdoor requires AFC; LPI prohibited outdoors in US.
> Fix: Add AFC coordination, disable 2.4 GHz on most tiles, centrally-computed channel/power plan.

**C4. Fiber connector cycle life and outdoor contamination.**
Standard LC/SC APC rated ~500-1000 cycles. Daily relocation = 2-3 years to EOL. 70-85% of fiber failures are endface contamination.
> Fix: Add expanded-beam connectors (ARINC 801, MIL-DTL-38999) rated 2000-10000 cycles; automated endface cleaning.

### 19. network-curious (Network/IoT)

**C1. Mobile tiles break claimed Layer-2 mesh.**
Every tile pickup is link flap on up to 6 edges. STP/MSTP/SPB reconverge in 1-30+ seconds at this scale.
> Fix: Claim SDN/controller-based approach with centralized forwarding tables updated on planned transits.

**C2. Security posture is nearly absent.**
No device attestation, mutual TLS, PKI, firmware signing, network segmentation. 24V handshake is trivial impersonation vector. RFID/1-Wire identity is trivially cloneable.
> Fix: Add cryptographic payload attestation, signed OTA, safety-bus authentication, tenant isolation.

**C3. Fire suppression via water mesh is code/liability landmine.**
NFPA 13/24/IBC do not permit ad-hoc reconfigurable plumbing as primary suppression.
> Fix: Reframe as supplementary cooling/misting. Remove "satisfy code-required" language.

**C4. Guest positioning is not feasible.**
GPS blocked by canopy (3-10m error). BLE RSSI outdoors 3-5m (larger than path width). No AR infrastructure claimed.
> Fix: Add UWB anchor claims, visual fiducials, sensor-fusion claim.

**C5. Data/privacy architecture is missing entirely.**
Cameras, LPR, crowd-density CV, BLE tracking with no GDPR/CCPA/BIPA compliance. No data minimization or retention policy.
> Fix: Claim edge-only inference; differential privacy; structured retention and tenant model.

### 20. risk-critical (Insurance Underwriting)

**C1. Gas-fed mobile tiles in publicly accessible reconfiguring grid: UNINSURABLE.**
Automated re-mating of fuel-gas couplings in public space. Leak-at-separation plus ignition source plus fuel (hedges).
> Fix: Remove gas entirely, or make gas tiles permanently plumbed, non-mobile, behind guest-inaccessible fence.

**C2. Vehicular-scale reconfigurable driving maze: UNINSURABLE.**
No applicable safety standard (not FMVSS, not ASTM F24, not AASHTO).
> Fix: Sever from commercial filing or limit to closed professional use.

**C3. Cyber-physical single point of failure on life safety.**
Same controller governs movement, egress, fire suppression, gas shutoffs, and guest app. Ransomware could produce mass-casualty scenario.
> Fix: Independent certified safety PLC for egress; air-gapped from scheduling/guest-app; mechanical fail-open egress.

**C4. Emergency egress time of "preferably under 5 minutes."**
5-minute reconfiguration exceeds realistic RSET during fast-moving hedge fire. Indefensible to fire marshal or plaintiff's expert.
> Fix: Permanent, never-blocked code-compliant egress that does not rely on reconfiguration.

### 21. risk-curious (Risk Management)

**C1. Egress validation has no independent safety-rated channel.**
Egress path continuity asserted by same control system that commands motion. No redundant verification.
> Fix: Redundant egress-integrity verification with independent sensors feeding separate safety PLC. Hard rule: no guest access during reconfiguration.

**C2. Pinch/crush/entrapment exposure during transit is under-specified.**
Static crushing force unbounded. Safety bumpers are "may include," not mandatory. Max approach-closure force not specified.
> Fix: Mandatory safety-rated bumpers (PL d); max 150 N dynamic per ISO/TS 15066; no-public-motion policy.

**C3. Terrace transit elevator is a fall hazard with guest-accessible edges.**
8,000 lb planter on raised platform over 24-inch drop with child in proximity.
> Fix: Declare terrace transits as guest-excluded operations with hard physical barriers during motion.

### 22. product-critical (Industrial Design)

**C1. Pan-to-pan interlock is not consistent with single-pan pickup.**
Interlocks on both edges bind when pan lifts with any tilt. Asymmetric hedge CG shifts CG off-center.
> Fix: Require powered retraction of interlock pins, commanded before lift, with sensor confirmation.

**C2. "Single-pour, simple formwork" claim is wrong.**
Three-level cast concrete labyrinth with continuous stepped ledges across entire property. Not tile-by-tile single pour.
> Fix: Describe expansion/contraction joints, drainage sumps, sectioning strategy; remove "simple formwork" claim.

**C3. Channels specified as DRY but physically open to weather.**
Rain, snowmelt, leaves, grit fall into middle and center channels. No sump, drainage, or filter. A36 bearing plates will rust.
> Fix: Add powered shutter when pan seated, or accept wet channels and add drainage, stainless plates, IP67 chassis.

**C4. Pan-to-trough retention has contradictory stiffness requirements.**
Must hold 4,300 lb pan against wind uplift yet release when chassis applies 3mm lift force. Spring detents wear in 1-2 years.
> Fix: Replace with commanded solenoid-actuated latches, independently retracted before lift.

**C5. Wind overturning on solo-seated pan not covered.**
12-ft hedge on 4x4 pan: overturning moment ~90,000 ft-lb vs tile deck capacity 2,500 ft-lb. No rule prevents isolated tall-sail configurations.
> Fix: Controller constraint: tall-payload pans never seated without N adjacent interlocked neighbors.

### 23. product-curious (Product Architecture)

**C1. Two contradictory "preferred embodiments" for transit mechanism.**
S2.3 (integrated elevator/wheels) vs S20B (three-part, no wheels on pan). Figures 2 and 10 contradict each other.
> Fix: Pick three-part as canonical; demote S2.3 to alternative/legacy embodiment.

**C2. Trough slot geometry is under-specified.**
How is slot sealed when cover tile occupies position? Debris falls into chassis channel. Pan bridges slot on narrow ledges.
> Fix: Specify retractable/hinged floor panels, gasket/seal detail, debris gutter with drain, ledge reinforcement.

**C3. "Consumer simple" claim undermined by 20+ interconnected subsystems.**
No integrator tile, starter kit, or minimum-viable-installation definition. LEGO promise, refinery reality.
> Fix: Define product tiers (Tier 1: Pan+Chassis+Outer Trough only; Tier 2: adds manifold; Tier 3: adds tunnels/depot).

### 24. illust-critical (Patent Illustrations)

**MAJOR REWORK: Fig. 13 and Fig. 14 spec mismatch.**
Spec lists Fig. 13 as "Inter-tile connectivity manifold" and Fig. 14 as "Pop-up utility access point." Actual files show three-part architecture. Either update spec figure list or produce missing drawings.
> Fix: Reconcile spec figure list with actual files; add reference numerals to all figures.

**MAJOR REWORK: Missing reference numerals on Figs. 4, 5, 6, 7, 9, 11, 12, 13, 14.**
Claims 58, 78, 81, 82, 85 depend on features needing on-drawing call-outs.
> Fix: Add numerals keyed to spec for every figure.

### 25. illust-curious (Technical Visualization)

**Fig. 2 lift-height contradiction.** Fig. 2B shows ~12" but S2.3 specifies 3-6 inches. Creates prosecution risk.
> Fix: Change figure to ~5" or amend spec.

**Fig. 7 false-path panel inverts the claim.** Drawing shows opposite of what S9 describes.
> Fix: Redraw panel B to match specification.

**Drawing list does not match actual files.** Fig. 13, 14, 15, 16 mismatch. Two figures missing entirely.
> Fix: Reconcile or produce 4 additional figures (manifold, pop-up utility, event orchestration, mesh topology).

### 26. landscape-critical (Landscape Aesthetics)

**C1. Canopy seam between pans will always be visible.**
S2.9 mandates canopy separation. Row of discrete pans reads as "topiary in pots lined up in a row," not a hedge.
> Fix: Allow controlled canopy interlock in upper 18-24 inches; accept pans must travel together in most configurations.

**C2. 2.5-3.0 ft root depth for 8-15 ft hedge is horticulturally implausible.**
Chronic stress browning, reduced density, uniform decline. Root zone temperatures >105F in summer.
> Fix: Increase minimum root volume or cap height at 6-8 ft for 2.5 ft pans.

**C3. LECA/hydroponic media visually wrong for formal hedge aesthetic.**
Unnaturally crisp, machined pan top edge. Flat, straight ground-to-foliage junction across 6-12 ft.
> Fix: Specify 3-4 inch organic topdressing, skirt planting cantilevered over pan rim, naturalistic mulch band.

**C4. Cover tile seam is not "seamless."**
Thermal cycling opens 1/8-1/4 inch gaps. Surface texture/color/weathering differential visible under raking light.
> Fix: Match cover weathering to surrounding path; accept or design around visible tile outlines.

### 27. mfg-critical (Manufacturing)

**C1. "Single-pour, simple formwork" claim is not manufacturable as drawn.**
Three nested rectangular cavities with 90-degree re-entrant corners and no draft. Cannot strip rigid internal form.
> Fix: Redraw as two-piece composite (lower U-channel + upper frame), document draft angles (min 1:12).

**C2. Junction cross-channels destroy pan-bearing ledge.**
At junctions, outer-to-middle step ledge is cut through in two directions. Pan at junction has no continuous ledge.
> Fix: Prohibit pan placement at junctions, or add retractable ledge inserts.

**C3. Cost model is off by 3x to 10x.**
Pans: $2,800-4,500 realistic (not $400-800). Chassis: $15,000-30,000 (not $2,000-4,000). Elevator: $20,000-50,000 (not $1,500-3,000).
> Fix: Delete specific dollar figures from patent; replace with qualitative relative-cost statement.

**C4. Precast tolerance stack-up exceeds manifold self-alignment envelope.**
Cumulative lateral misalignment across 5 slabs easily exceeds 1 inch. S21.2 claims +/-0.5 inch self-alignment.
> Fix: Reduce to pan-to-neighbor-only manifolds, add floating outer-ledge frame, or widen manifold envelope to +/-1.5 inch.

**C5. Embedded A36 bearing plates cannot be cast-in with chassis-required coplanar precision.**
Standard cast-in tolerance +/-1/4 inch; chassis needs +/-1/32 inch coplanar.
> Fix: Cast pockets with threaded leveling anchors; shim and grout post-cast per crane-rail practice.

**C6. Outdoor cast-in 48V/50A DC contacts in drainage-channel environment will fail.**
Gold-flash contacts in below-grade cavity with standing water, leaf decomposition, fertilizer salts. Contact resistance climbs after one season.
> Fix: Move primary power to inter-tile manifold; keep trough-floor contacts as low-current maintenance injection only.

### 28. mfg-curious (Manufacturing Strategy)

**C1. SKU proliferation in standardized planter family.**
7 sizes x 2 depth variants = 10-14 SKUs. Fragments production runs; undermines economies of scale.
> Fix: Collapse to THREE hero sizes (M, L, SQ); express XL as two coupled L pans.

**C2. Tolerance stackup on manifold mating is unvalidated.**
Concrete shrinkage, thermal expansion, freeze-thaw heave can exceed 1 inch. Likely biggest technical risk.
> Fix: Build four-pan mockup on representative substrate; measure worst-case misalignment across thermal cycle.

**C3. Pan cost estimate is optimistic by 2-3x.**
Realistic BOM at 1,000-5,000 units: $1,500-2,500 per pan, not $400-800.
> Fix: Redo BOM with vendor quotes, or caveat cost claims more strongly.

---

## Grand Summary

| Metric | Count |
|--------|-------|
| **Total CRITICAL findings** | **~113** |
| **Total IMPORTANT findings** | **~155** |
| **Total MINOR findings** | **~111** |
| **Total agents** | **28** |
| **Total domains** | **14** |

### Top 10 Most-Repeated CRITICAL Themes (cross-domain)

1. **Fire suppression water mesh does not meet NFPA 13** (fire-critical, fire-curious, sw-critical, network-curious, risk-critical, mfg-critical) -- 6 agents
2. **Emergency egress "within 5 minutes" is indefensible** (sw-critical, fire-critical, ada-critical, risk-critical, risk-curious) -- 5 agents
3. **Cost model is off by 3-10x** (mfg-critical, mfg-curious, vc-curious, product-curious) -- 4 agents
4. **Manifold tolerance stack-up exceeds self-alignment envelope** (mfg-critical, mfg-curious, product-curious, product-critical) -- 4 agents
5. **Claim 1 is anticipated/obvious** (lit-critical, ptab-critical, ptab-curious) -- 3 agents
6. **Safety integrity claim (SIL/PL) is malformed and under-rated** (sw-critical, risk-critical, risk-curious) -- 3 agents
7. **Root volume too small for 15-ft hedges** (landscape-curious, landscape-critical, vc-curious) -- 3 agents
8. **Species list is climate-narrow / ecologically poor** (landscape-curious, env-curious, fire-curious) -- 3 agents
9. **No privacy/security architecture for guest data** (sw-curious, network-curious, env-curious) -- 3 agents
10. **Software claims lack algorithmic disclosure, vulnerable to S112/S101** (lit-critical, lit-curious, ptab-curious, sw-curious) -- 4 agents

### Priority Fix List (ordered by cross-domain consensus)

1. **Reframe water mesh as supplemental cooling/misting; remove all "satisfies code-required fire protection" language**
2. **Make egress a configuration invariant (always-open corridors), not a reconfiguration action**
3. **Delete cost figures from patent; replace with qualitative relative-cost statements**
4. **Rewrite Claim 1 with trough-flush-concealment pulled up from Claims 11-12**
5. **Add algorithmic disclosure (pseudocode/flowcharts) for all software claims**
6. **Reconcile Fig. 13/14 spec list with actual drawings; produce missing figures**
7. **Add privacy/security architecture section (GDPR/CCPA/IEC 62443)**
8. **Broaden species list to include warm-climate and native species**
9. **Increase pan root depth for large hedge embodiments or cap specified height**
10. **Replace "single-pour simple formwork" with two-piece composite trough disclosure**

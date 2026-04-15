#!/usr/bin/env python3
"""Assemble The Compound presentation HTML with embedded images and SVG."""
import os, sys, json

BASE = r"F:\home\exploded-hexagon-home\presentation"
B64 = os.path.join(BASE, "b64")
OUT = os.path.join(BASE, "the-compound.html")
SVG_PATH = r"F:\home\exploded-hexagon-home\out\plan_s23_d7.svg"

def b64(name):
    with open(os.path.join(B64, name + ".b64"), "r") as f:
        return f.read()

def svg():
    with open(SVG_PATH, "r") as f:
        content = f.read()
    # Strip XML declaration and make it inline-friendly
    content = content.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
    return content

ADMIN_PW = "minotaur"

# Budget data (percentages for public, actuals for admin)
BUDGET_PHASES = [
    {"phase": "Phase 1: Foundation", "years": "0-2", "pct": "48-53%", 
     "actual_low": "$3.8M", "actual_high": "$5.6M",
     "items": "Land acquisition, perimeter wall, mass excavation, unified slab, tunnel network, main house (livable shell), entry drive"},
    {"phase": "Phase 2: Completion", "years": "2-4", "pct": "22-24%",
     "actual_low": "$1.5M", "actual_high": "$2.5M",
     "items": "Finish main house interiors, construct guesthouse, pools & hot tubs, water features around homes"},
    {"phase": "Phase 3: Grounds", "years": "4-6", "pct": "22-24%",
     "actual_low": "$1.5M", "actual_high": "$2.5M",
     "items": "Engineered stream, koi pond, full hedge/labyrinth system, garden development, forest manicuring, exterior paths"},
]

BUDGET_LINES = [
    ("Land Acquisition", "$600k-875k", "8-9%"),
    ("Perimeter Wall", "$500k-800k", "7-8%"),
    ("Underground Infrastructure", "$480k-820k", "7-8%"),
    ("Main House Construction", "$2.2M-3.1M", "29-32%"),
    ("Guesthouse Construction", "$700k-1.0M", "9-10%"),
    ("Pools & Water Features", "$300k-530k", "4-5%"),
    ("Engineered Water System", "$350k-500k", "4-5%"),
    ("Hedge & Labyrinth System", "$200k-350k", "3-4%"),
    ("Gardens, Paths & Forest", "$1.0M-1.5M", "13-15%"),
    ("A&E Fees (10-15%)", "$450k-750k", "6-7%"),
    ("Contingency (15%)", "$600k-900k", "8-9%"),
]

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Compound — Estate Design Vision</title>
<style>
/* ═══════════════ RESET & BASE ═══════════════ */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --concrete: #3a3a38;
  --concrete-light: #5a5a56;
  --warm-cream: #f5f0e8;
  --sage: #6b7c5e;
  --sage-dark: #4a5a3e;
  --sage-light: #8fa07a;
  --copper: #b87333;
  --copper-light: #d4956a;
  --earth: #8b7355;
  --deep-green: #2d4a2d;
  --water: #5a8a9a;
  --white: #fefefe;
  --text: #2a2a28;
  --text-light: #6a6a66;
  --section-gap: 0;
}}

html {{ scroll-behavior: smooth; }}
body {{
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  color: var(--text);
  background: var(--warm-cream);
  line-height: 1.7;
  overflow-x: hidden;
}}

/* ═══════════════ TYPOGRAPHY ═══════════════ */
h1, h2, h3, h4 {{
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 400;
  letter-spacing: 0.02em;
}}
h1 {{ font-size: clamp(2.5rem, 5vw, 4.5rem); line-height: 1.1; }}
h2 {{ font-size: clamp(1.8rem, 3vw, 2.8rem); line-height: 1.2; margin-bottom: 1.5rem; }}
h3 {{ font-size: clamp(1.3rem, 2vw, 1.8rem); color: var(--concrete-light); margin-bottom: 1rem; }}
h4 {{ font-size: 1.1rem; color: var(--sage-dark); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.8rem; }}

p {{ max-width: 70ch; margin-bottom: 1.2em; }}
.lead {{ font-size: 1.15em; color: var(--concrete-light); }}

/* ═══════════════ NAV ═══════════════ */
nav {{
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  background: rgba(58,58,56,0.95); backdrop-filter: blur(10px);
  padding: 0.6rem 2rem;
  display: flex; align-items: center; gap: 2rem;
  font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.12em;
  border-bottom: 2px solid var(--copper);
  overflow-x: auto; white-space: nowrap;
}}
nav a {{
  color: var(--warm-cream); text-decoration: none; opacity: 0.7;
  transition: opacity 0.3s;
}}
nav a:hover, nav a.active {{ opacity: 1; color: var(--copper-light); }}
nav .brand {{ font-family: Georgia, serif; font-size: 1rem; letter-spacing: 0.2em; opacity: 1; color: var(--copper-light); }}

/* ═══════════════ SECTIONS ═══════════════ */
section {{
  padding: 6rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}}
section:first-of-type {{ padding-top: 0; margin-top: 0; max-width: none; }}

.full-bleed {{
  max-width: none;
  padding: 0;
}}

/* ═══════════════ HERO ═══════════════ */
.hero {{
  min-height: 100vh;
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  text-align: center;
  position: relative;
  background: var(--concrete);
  color: var(--warm-cream);
  overflow: hidden;
}}
.hero::before {{
  content: '';
  position: absolute; inset: 0;
  background: url('data:image/png;base64,{b64("01_exterior_hill")}') center/cover;
  opacity: 0.35;
}}
.hero-content {{
  position: relative; z-index: 1;
  padding: 2rem;
}}
.hero h1 {{
  margin-bottom: 1rem;
  text-shadow: 0 2px 40px rgba(0,0,0,0.5);
}}
.hero .subtitle {{
  font-size: clamp(1rem, 2vw, 1.4rem);
  font-family: Georgia, serif;
  font-style: italic;
  color: var(--copper-light);
  margin-bottom: 2rem;
  max-width: 50ch;
}}
.hero .tagline {{
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.25em;
  color: var(--sage-light);
}}
.scroll-hint {{
  position: absolute; bottom: 3rem;
  color: var(--copper-light); opacity: 0.6;
  animation: bob 2s ease-in-out infinite;
  font-size: 1.5rem;
}}
@keyframes bob {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(10px); }} }}

/* ═══════════════ IMAGE SECTIONS ═══════════════ */
.img-full {{
  width: 100%; max-height: 70vh; object-fit: cover;
  border-radius: 4px;
  margin: 2rem 0;
  box-shadow: 0 8px 40px rgba(0,0,0,0.15);
}}
.img-half {{
  width: 100%; max-height: 50vh; object-fit: cover;
  border-radius: 4px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}}
.img-caption {{
  font-size: 0.85rem; color: var(--text-light);
  font-style: italic; margin-top: 0.5rem; text-align: center;
}}

.two-col {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin: 2rem 0;
}}
.three-col {{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1.5rem;
  margin: 2rem 0;
}}
@media (max-width: 768px) {{
  .two-col, .three-col {{ grid-template-columns: 1fr; }}
}}

/* ═══════════════ FEATURE CARDS ═══════════════ */
.card {{
  background: var(--white);
  border-radius: 6px;
  padding: 2rem;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  border-left: 4px solid var(--copper);
}}
.card h4 {{ color: var(--copper); }}
.card.sage {{ border-left-color: var(--sage); }}
.card.sage h4 {{ color: var(--sage-dark); }}
.card.water {{ border-left-color: var(--water); }}
.card.water h4 {{ color: var(--water); }}

/* ═══════════════ DIVIDERS ═══════════════ */
.divider {{
  text-align: center;
  padding: 4rem 2rem;
  position: relative;
  color: var(--concrete);
  max-width: none;
  background: linear-gradient(135deg, var(--warm-cream) 0%, #e8e2d8 100%);
}}
.divider::before {{
  content: '';
  display: block;
  width: 60px; height: 2px;
  background: var(--copper);
  margin: 0 auto 1.5rem;
}}
.divider h2 {{ font-style: italic; }}

/* ═══════════════ DATA TABLES ═══════════════ */
table {{
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
  font-size: 0.95rem;
}}
th {{
  background: var(--concrete);
  color: var(--warm-cream);
  padding: 0.8rem 1rem;
  text-align: left;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.8rem;
}}
td {{
  padding: 0.7rem 1rem;
  border-bottom: 1px solid #ddd;
}}
tr:nth-child(even) {{ background: rgba(0,0,0,0.02); }}
tr:last-child td {{ border-bottom: 2px solid var(--copper); }}
.total-row {{ font-weight: 700; background: var(--warm-cream) !important; }}

/* ═══════════════ SVG CONTAINER ═══════════════ */
.svg-plan {{
  background: white;
  padding: 1.5rem;
  border-radius: 6px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  overflow-x: auto;
  margin: 2rem 0;
  text-align: center;
}}
.svg-plan svg {{
  max-width: 100%;
  height: auto;
}}

/* ═══════════════ SPEC GRID ═══════════════ */
.spec-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
}}
.spec {{
  text-align: center;
  padding: 1.5rem;
  background: var(--white);
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}}
.spec .num {{
  font-size: 2rem;
  font-family: Georgia, serif;
  color: var(--copper);
  display: block;
}}
.spec .label {{
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-light);
}}

/* ═══════════════ PHASE TIMELINE ═══════════════ */
.timeline {{
  position: relative;
  padding-left: 3rem;
  margin: 2rem 0;
}}
.timeline::before {{
  content: '';
  position: absolute;
  left: 1rem; top: 0; bottom: 0;
  width: 3px;
  background: linear-gradient(to bottom, var(--copper), var(--sage), var(--water));
  border-radius: 2px;
}}
.timeline-item {{
  position: relative;
  margin-bottom: 3rem;
  padding: 1.5rem;
  background: var(--white);
  border-radius: 6px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}}
.timeline-item::before {{
  content: '';
  position: absolute;
  left: -2.35rem; top: 1.8rem;
  width: 14px; height: 14px;
  background: var(--copper);
  border-radius: 50%;
  border: 3px solid var(--warm-cream);
}}
.timeline-item:nth-child(2)::before {{ background: var(--sage); }}
.timeline-item:nth-child(3)::before {{ background: var(--water); }}
.timeline-label {{
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--copper);
  margin-bottom: 0.3rem;
}}

/* ═══════════════ ADMIN SECTION ═══════════════ */
.admin-section {{
  display: none;
  background: #1a1a18;
  color: var(--warm-cream);
  padding: 4rem 2rem;
  max-width: none;
  margin: 0;
}}
.admin-section.visible {{ display: block; }}
.admin-section h2 {{ color: var(--copper-light); }}
.admin-section table {{ background: #2a2a28; }}
.admin-section th {{ background: #333; }}
.admin-section td {{ border-bottom-color: #444; color: #ccc; }}
.admin-section tr:nth-child(even) {{ background: rgba(255,255,255,0.03); }}
.admin-section .warning {{
  background: rgba(184,115,51,0.15);
  border: 1px solid var(--copper);
  padding: 1rem 1.5rem;
  border-radius: 6px;
  margin-bottom: 2rem;
  font-size: 0.9rem;
}}

/* ═══════════════ GARDEN REGIONS ═══════════════ */
.garden-section {{
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  margin: 2rem 0;
}}
.garden-section .garden-bg {{
  width: 100%; height: 400px;
  object-fit: cover;
  display: block;
}}
.garden-section .garden-overlay {{
  position: absolute;
  bottom: 0; left: 0; right: 0;
  padding: 2rem;
  background: linear-gradient(transparent, rgba(0,0,0,0.75));
  color: white;
}}
.garden-section .garden-overlay h3 {{ color: var(--copper-light); margin-bottom: 0.5rem; }}

/* ═══════════════ PRINCIPLES ═══════════════ */
.principles {{
  counter-reset: principle;
  margin: 2rem 0;
}}
.principle {{
  counter-increment: principle;
  padding: 1.2rem 1.5rem 1.2rem 4rem;
  position: relative;
  border-bottom: 1px solid rgba(0,0,0,0.06);
}}
.principle::before {{
  content: counter(principle);
  position: absolute;
  left: 0; top: 1.2rem;
  width: 2.5rem; height: 2.5rem;
  background: var(--concrete);
  color: var(--copper-light);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: Georgia, serif;
  font-size: 1.1rem;
}}

/* ═══════════════ FOOTER ═══════════════ */
footer {{
  background: var(--concrete);
  color: var(--warm-cream);
  text-align: center;
  padding: 3rem 2rem;
  font-size: 0.85rem;
  opacity: 0.8;
}}

/* ═══════════════ VIDEO PLACEHOLDER ═══════════════ */
.video-placeholder {{
  background: #1a1a18;
  border: 2px dashed var(--concrete-light);
  border-radius: 8px;
  padding: 4rem 2rem;
  text-align: center;
  color: var(--text-light);
  margin: 2rem 0;
}}
.video-placeholder .icon {{ font-size: 3rem; margin-bottom: 1rem; }}

/* ═══════════════ PRINT ═══════════════ */
@media print {{
  nav {{ display: none; }}
  .hero {{ min-height: auto; padding: 4rem 2rem; break-after: page; }}
  section {{ break-inside: avoid; padding: 2rem; }}
  .admin-section {{ display: none !important; }}
}}
</style>
</head>
<body>

<!-- ═══════════════ NAVIGATION ═══════════════ -->
<nav>
  <span class="brand">The Compound</span>
  <a href="#vision">Vision</a>
  <a href="#site">Site</a>
  <a href="#layout">Layout</a>
  <a href="#perimeter">Perimeter</a>
  <a href="#arrival">Arrival</a>
  <a href="#house">House</a>
  <a href="#guesthouse">Guesthouse</a>
  <a href="#labyrinth">Labyrinth</a>
  <a href="#water">Water</a>
  <a href="#tunnels">Tunnels</a>
  <a href="#grounds">Grounds</a>
  <a href="#phasing">Phasing</a>
  <a href="#budget">Budget</a>
  <a href="#media">Media</a>
</nav>

<!-- ═══════════════ HERO ═══════════════ -->
<section class="hero full-bleed" id="hero">
  <div class="hero-content">
    <p class="tagline">A Private Estate Vision</p>
    <h1>The Compound</h1>
    <p class="subtitle">A haven of rest for weary travelers, and a foundation for a new garden of eden. Like a portal between many worlds.</p>
    <p style="font-size:0.8rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--sage-light); margin-top:3rem;">Browns Summit, North Carolina &middot; 59.82 Acres</p>
  </div>
  <div class="scroll-hint">&darr;</div>
</section>

<!-- ═══════════════ THE VISION ═══════════════ -->
<section id="vision">
  <h4>Chapter I</h4>
  <h2>The Vision</h2>
  <p class="lead">Cast concrete, embedded in the earth, seeming to extrude into and out from the ground itself. A wondrous cave of light within a multiplicity of hidden worlds, each accessible steps from the others, with many hidden surprises and delights.</p>
  
  <p>The Compound is not a house. It is an entire world, enclosed within forest and stone, threaded by water and woven through with living green walls that create mystery at every turn. The home emerges from an artificial hilltop as if it has always been there, its angular concrete and glass planes catching light while the lower levels disappear into the landscape.</p>
  
  <p>Surrounding it: a labyrinth of hedged corridors connecting secret gardens, each with its own character and mood. Below: a network of tunnels linking house to guesthouse to garden to the world beyond the wall. Above: open sky, rolling Piedmont hills, and the distant blue ridges of the North Carolina mountains.</p>

  <p>It is fortress-like in its security and absolute in its privacy, yet warm and welcoming within. A place where intimate gatherings happen in hidden garden rooms, where a stream winds through as if nature placed it there, where art and sculpture punctuate formal lawns, and where the boundary between architecture and landscape dissolves entirely.</p>

  <h3 style="margin-top:3rem;">Design Principles</h3>
  <div class="principles">
    <div class="principle"><strong>The house emerges from the landscape</strong>, not imposed upon it. From the approach, only one modest level is visible. The rest is embedded in the earth.</div>
    <div class="principle"><strong>Privacy is absolute</strong> within the perimeter wall. Ecological control is total. No venomous snakes, no invasive plants, no unwanted intrusion.</div>
    <div class="principle"><strong>No single contractor</strong> sees the full tunnel and security layout. Two separate systems, two separate builders.</div>
    <div class="principle"><strong>The guesthouse reads as an independent estate</strong> from every exterior view. Only from within do you discover the connection.</div>
    <div class="principle"><strong>Water unifies the entire compound</strong> as a continuous landscape spine, from hidden spring to stream to pond to waterfall to rill.</div>
    <div class="principle"><strong>The labyrinth creates mystery and discovery</strong> at every scale, from intimate garden rooms to the full perimeter corridor.</div>
    <div class="principle"><strong>Materials are real.</strong> Concrete, stone, glass, living plants. Nothing faux, nothing fake, nothing that pretends to be what it is not.</div>
    <div class="principle"><strong>The arrival sequence is cinematic.</strong> Reveal, descent, tunnel, emergence into the sunken motorcourt. Every guest earns the view.</div>
    <div class="principle"><strong>Phased construction</strong> allows immediate occupancy while the vision builds over six or more years.</div>
  </div>
</section>

<!-- ═══════════════ THE SITE ═══════════════ -->
<div class="divider"><h2>The Land</h2></div>
<section id="site">
  <h4>Chapter II</h4>
  <h2>The Site</h2>
  
  <div class="spec-grid">
    <div class="spec"><span class="num">59.82</span><span class="label">Acres</span></div>
    <div class="spec"><span class="num">~800'</span><span class="label">Elevation</span></div>
    <div class="spec"><span class="num">2</span><span class="label">Parcels</span></div>
    <div class="spec"><span class="num">AG</span><span class="label">Zoning</span></div>
  </div>
  
  <p class="lead">8220 Southerland Drive, Browns Summit, North Carolina 27214. Two parcels (230483, 128207) at the end of a high-end neighborhood, backed by a working horse farm that will never be subdivided.</p>
  
  <p>The property sits northwest of Greensboro, approximately six miles from Piedmont Triad International Airport. Rolling topography with mature second-growth deciduous forest, existing internal trails, and no natural water crossing, which is by design: engineered water systems provide full ecological control within the perimeter.</p>
  
  <p>The terrain is Piedmont clay (Cecil and Appling series soils), favorable for excavation and engineered earthwork. The elevation is modest but sufficient; gentle rolls will be enhanced by artificial grading to create the dramatic hill-and-valley experience the design requires.</p>
  
  <div class="two-col">
    <div class="card">
      <h4>South ~30 Acres</h4>
      <p>The walled compound. Circular precast concrete perimeter wall encloses approximately 5.6 acres of program space within manicured forest. All structures, gardens, labyrinth, and water features contained within.</p>
    </div>
    <div class="card sage">
      <h4>North ~30 Acres</h4>
      <p>Horse farm, designated for Lisa. Architecturally consistent with the compound's design language: high-end North Carolina horse country aesthetic with modern details that clearly belong to the same property.</p>
    </div>
  </div>
</section>

<!-- ═══════════════ THE LAYOUT ═══════════════ -->
<section id="layout">
  <h4>Chapter III</h4>
  <h2>Estate Layout</h2>
  
  <img src="data:image/png;base64,{b64("04_aerial_compound")}" alt="Aerial view of compound" class="img-full">
  <p class="img-caption">Conceptual aerial view: the compound clearing within the forest, with hedge-lined corridors radiating outward</p>
  
  <p>The south 30 acres contain a roughly circular walled enclosure of approximately 5.6 acres. Within it:</p>
  
  <div class="spec-grid">
    <div class="spec"><span class="num">1 ac</span><span class="label">Circular Lawn</span></div>
    <div class="spec"><span class="num">0.5 ac</span><span class="label">Hedge Labyrinth</span></div>
    <div class="spec"><span class="num">0.5 ac</span><span class="label">Structures & Gardens</span></div>
    <div class="spec"><span class="num">~3.6 ac</span><span class="label">Manicured Forest</span></div>
  </div>
  
  <p>External forest buffers the perimeter wall from property boundaries by approximately 150 feet on all sides. This existing tree canopy and understory makes the 12-foot wall effectively invisible from the road on day one, before any landscaping work begins.</p>
</section>

<!-- ═══════════════ THE PERIMETER ═══════════════ -->
<div class="divider"><h2>The Wall</h2></div>
<section id="perimeter">
  <h4>Chapter IV</h4>
  <h2>The Perimeter</h2>
  
  <p class="lead">The wall is not meant to be seen. It is meant to be felt only in its absence, in the absolute serenity of what lies within.</p>
  
  <p>Approximately 1,750 linear feet of precast concrete panels form a roughly circular perimeter. Standard height is 12 feet; at the rose garden ridgeline section where the artificial hill meets the wall, it rises to 24 feet. The wall has an inward cant for anti-climb resistance, with thorny climbing plants trained on the exterior face and a concealed sensor cable embedded in the cap.</p>
  
  <div class="two-col">
    <div class="card">
      <h4>Exterior Face</h4>
      <p>Board-formed or stacked stone finish. Thorny climbing plants (hawthorn, firethorn, climbing roses) trained densely. From outside, it reads as an impenetrable natural thicket. Beautiful but unwelcoming to approach.</p>
    </div>
    <div class="card sage">
      <h4>Interior Face</h4>
      <p>Hidden behind a double layer of tall formal hedges. From inside the compound, the wall is invisible. Walking the perimeter corridor feels like being in a living hedge labyrinth, not alongside a concrete barrier.</p>
    </div>
  </div>
  
  <p>No gate columns, no gatehouse visible from the road. Entry points use flush cattle grids that blend with the ground plane. The wall does not announce itself. It simply ensures that everything within is protected.</p>
</section>

<!-- ═══════════════ THE ARRIVAL ═══════════════ -->
<div class="divider"><h2>The Approach</h2></div>
<section id="arrival">
  <h4>Chapter V</h4>
  <h2>The Arrival Sequence</h2>
  
  <img src="data:image/png;base64,{b64("10_arrival_sequence")}" alt="Arrival sequence" class="img-full">
  <p class="img-caption">The hedgerow lane: guests pass through a living green corridor before the first reveal</p>
  
  <p class="lead">Three completely separate entrances serve different functions. Each is a journey, not just a driveway.</p>
  
  <h3>Main Guest Entrance</h3>
  <p>The guest arrival is designed as a cinematic sequence of compression and revelation:</p>
  <ol style="margin:1rem 0 2rem 1.5rem; max-width:70ch;">
    <li style="margin-bottom:0.6rem;"><strong>The Gate</strong> — A flush cattle grid, invisible in the road surface. No columns, no signage. You cross it without realizing.</li>
    <li style="margin-bottom:0.6rem;"><strong>50' Naturalistic Buffer</strong> — Dense native planting screens the transition from public road to private world.</li>
    <li style="margin-bottom:0.6rem;"><strong>200' Hedgerow Lane</strong> — 16 feet wide, two-car width. Tall formal hedges rise on both sides, creating a living green tunnel. Compression builds anticipation.</li>
    <li style="margin-bottom:0.6rem;"><strong>Circular Turnabout</strong> — 70-80 feet in diameter. Flanking stone fountains. Overflow parking. The hedges part and for the first time, through a gap, the house is visible on the hilltop ahead.</li>
    <li style="margin-bottom:0.6rem;"><strong>The Descent</strong> — As the land rises around the drive, the road effectively descends. The house grows above you.</li>
    <li style="margin-bottom:0.6rem;"><strong>Lawn Berm Tunnel</strong> — A precast box culvert (10-12 feet clear) passes under the lawn. The world goes quiet for a moment.</li>
    <li style="margin-bottom:0.6rem;"><strong>Motorcourt Emergence</strong> — You emerge into a sunken courtyard, 12 feet below the lawn grade. Open sky above. Water sheeting gently down battered stone walls. Light, air, and the sound of water.</li>
  </ol>
  
  <img src="data:image/png;base64,{b64("02_motorcourt")}" alt="Sunken motorcourt" class="img-full">
  <p class="img-caption">The motorcourt: sunken 12 feet below the lawn, water cascading down stone walls, open sky above</p>
  
  <div class="two-col">
    <div class="card">
      <h4>Service / Guesthouse Entrance</h4>
      <p>Separate gate positioned ~60° around the perimeter. Tall functional hedges. A brief glimpse of the guesthouse lawn during approach. 14-foot clear tunnel accommodates delivery trucks. Functional, secure, and beautiful in its own right.</p>
    </div>
    <div class="card sage">
      <h4>Owner's Entrance</h4>
      <p>An abrupt hillside tunnel entrance. No ceremony, no reveal sequence. Direct route to the private below-grade garage. Every day is efficient. The theater is for guests.</p>
    </div>
  </div>
</section>

<!-- ═══════════════ THE MAIN HOUSE ═══════════════ -->
<div class="divider"><h2>The Architecture</h2></div>
<section id="house">
  <h4>Chapter VI</h4>
  <h2>The Main House</h2>
  
  <img src="data:image/png;base64,{b64("01_exterior_hill")}" alt="Main house exterior" class="img-full">
  <p class="img-caption">The main house emerging from the hilltop: only the upper triangle level is visible from the lawn approach</p>
  
  <p class="lead">The Exploded Hexagon: a parametric design built from pure geometry. Hexagonal plan, 23-foot edges, three wings radiating from a central atrium, crowned by a rotated scalene triangle containing the owner's private quarters.</p>
  
  <h3>Floor Plan</h3>
  <div class="svg-plan">
    {svg()}
  </div>
  <p class="img-caption">Plan view: hexagonal atrium (center), three wings (A, B, C), and the rotated upper triangle with three rooms</p>
  
  <div class="spec-grid">
    <div class="spec"><span class="num">7,201</span><span class="label">Total Plan SF</span></div>
    <div class="spec"><span class="num">1,374</span><span class="label">Atrium SF</span></div>
    <div class="spec"><span class="num">3</span><span class="label">Levels</span></div>
    <div class="spec"><span class="num">45'</span><span class="label">Atrium Height</span></div>
    <div class="spec"><span class="num">23'</span><span class="label">Hex Edge</span></div>
    <div class="spec"><span class="num">2</span><span class="label">Elevators</span></div>
  </div>
  
  <h3>Three Levels</h3>
  <table>
    <tr><th>Level</th><th>Program</th><th>Relationship to Grade</th></tr>
    <tr><td><strong>Upper (Triangle)</strong></td><td>Owner's private quarters: bedroom (~826 sf), office (~826 sf), bathroom (~740 sf)</td><td>Only level visible from lawn. Appears modest, floating.</td></tr>
    <tr><td><strong>Middle (Wings A+B)</strong></td><td>Guest suites (687 sf each)</td><td>Embedded in artificial hill. Exits to private rear courtyards facing downhill toward creek.</td></tr>
    <tr><td><strong>Lower (Wing C)</strong></td><td>Shared living, dining, kitchen</td><td>Opens fully to rear grade at pool terrace. Below-grade garage adjacent.</td></tr>
  </table>
  
  <h3>The Atrium</h3>
  <img src="data:image/png;base64,{b64("03_atrium_interior")}" alt="Atrium interior" class="img-full">
  <p class="img-caption">The atrium: a 45-foot void of light, water, and tropical garden, the heart of the home</p>
  
  <p>The atrium floor sits 2 feet below entry grade. The roof peaks at 49 feet, creating a ~45-foot vertical void. It is the heart of the home: a tropical garden with palms, ferns, a central banyan tree, a stone fountain, and a dramatic architectural waterfall cascading down one concrete wall. This is not a fake-natural feature. It is intentionally, beautifully artificial: water, concrete, and light working together.</p>
  
  <p>Glass walls face the atrium from all levels, so the garden is the first and last thing guests see. From the motorcourt entrance, the lush green interior is visible through the glass as you approach, drawing you forward and downward into the space.</p>
  
  <h3>Materials</h3>
  <div class="three-col">
    <div class="card">
      <h4>Concrete</h4>
      <p>Board-formed exposed concrete on all exterior walls. Smooth, warm, real. The defining material of the compound.</p>
    </div>
    <div class="card sage">
      <h4>Glass</h4>
      <p>Floor-to-ceiling glazing on atrium walls and rear elevations. Impact-rated. Variable opacity technology when available.</p>
    </div>
    <div class="card water">
      <h4>Stone & Marble</h4>
      <p>Polished marble in the atrium. Natural stone in water features. Real materials throughout; nothing that pretends.</p>
    </div>
  </div>
  
  <h3>Vertical Circulation</h3>
  <p><strong>Public elevator:</strong> Glass and steel, architectural, with elegant exposed workings. Maglev drive when the technology becomes available. It is a feature, not a utility.</p>
  <p><strong>Private elevator:</strong> Beautiful interior, hidden behind a concealed door system. Serves all three levels plus garage. Wheelchair accessible.</p>
</section>

<!-- ═══════════════ THE GUESTHOUSE ═══════════════ -->
<section id="guesthouse">
  <h4>Chapter VII</h4>
  <h2>The Guesthouse</h2>
  
  <p class="lead">A hexagonal plan without an atrium. Two levels, approximately 2,748 square feet total. From every exterior view, it appears to be an entirely independent estate.</p>
  
  <div class="two-col">
    <div class="card">
      <h4>Upper Level (~1,374 sf)</h4>
      <p>Master bedroom suite, bunkroom / second bedroom, open living area with kitchen and dining. Views toward the private guest pool, hot tub, and cold plunge on the far side, overlooking its own lawn and the approach tunnel.</p>
    </div>
    <div class="card sage">
      <h4>Lower Level (~1,374 sf)</h4>
      <p>Game room, recreation area, bar, and party space, all facing the shared pool terrace. A connector garage volume abuts the main house garage behind an ivy-covered retaining wall, hiding the connection.</p>
    </div>
  </div>
  
  <img src="data:image/png;base64,{b64("09_pool_terrace")}" alt="Pool terrace" class="img-full">
  <p class="img-caption">The shared pool terrace between main house and guesthouse, with the ivy retaining wall hiding the connector below</p>
  
  <p>The unified structural slab extends from the main house to the guesthouse footprint during Phase 1, even though the guesthouse superstructure waits for Phase 2. A secret tunnel also connects the two houses below grade. The connector garage provides a large shared space that can serve as storage, workshop, or additional parking.</p>
</section>

<!-- ═══════════════ THE LABYRINTH ═══════════════ -->
<div class="divider"><h2>The Labyrinth</h2></div>
<section id="labyrinth">
  <h4>Chapter VIII</h4>
  <h2>The Labyrinth</h2>
  
  <img src="data:image/png;base64,{b64("08_labyrinth_corridor")}" alt="Labyrinth corridor" class="img-full">
  <p class="img-caption">A corridor within the labyrinth: tall hedges, dappled light, the turn ahead concealing what lies beyond</p>
  
  <p class="lead">Approximately 12,900 linear feet of formal hedge across the full property. Not merely a maze, but a labyrinth: a system of corridors, garden rooms, and perimeter walks that connects every element of the compound into a single, mysterious, walkable world.</p>
  
  <div class="spec-grid">
    <div class="spec"><span class="num">12,900</span><span class="label">Linear Feet of Hedge</span></div>
    <div class="spec"><span class="num">~4,500'</span><span class="label">Perimeter Corridors</span></div>
    <div class="spec"><span class="num">3</span><span class="label">Garden Regions</span></div>
    <div class="spec"><span class="num">0.5 ac</span><span class="label">Dense Maze Area</span></div>
  </div>
  
  <h3>The Perimeter Labyrinth</h3>
  <p>The perimeter wall is embedded within a double-hedge system. An inner corridor runs between the wall and a hedge on the compound side; an outer corridor runs between the wall and a hedge on the forest side. The wall itself disappears between the two layers. Walking either corridor, you feel you are in a living hedge labyrinth, the concrete invisible.</p>
  <p>Phased installation: outer hedges first (~4,000 LF), the wall visible but the walk pleasant. Later, inner hedges added (~4,000 LF), and the wall vanishes entirely. The same path transforms from a perimeter walk into a pure labyrinth experience.</p>
  
  <h3>The Three Regions</h3>
  <p>Long hedge hallways connect three distinct garden regions, creating the illusion of an enormous unified maze. Each region has its own character, its own mood, its own world.</p>
  
  <!-- ROSE GARDEN -->
  <div class="garden-section">
    <img src="data:image/png;base64,{b64("05_rose_garden")}" alt="Rose Garden" class="garden-bg">
    <div class="garden-overlay">
      <h3>Region I: The Rose Garden</h3>
      <p>Formal, elevated on the ridgeline, the most intimate of the three. A secret inner garden accessed via a hedge portico and tunnel. Climbing roses in deep reds, pinks, and whites on stone trellises. Two exits lead deeper into the maze. Stone water rills thread through the beds. This is the region where the wall rises to 24 feet, hidden entirely by the hedge and the artificial ridgeline.</p>
    </div>
  </div>
  
  <!-- CULTURE GARDEN -->
  <div class="garden-section">
    <img src="data:image/png;base64,{b64("07_culture_garden")}" alt="Culture Garden" class="garden-bg">
    <div class="garden-overlay">
      <h3>Region II: The Culture Garden</h3>
      <p>Formal lawn with modern abstract sculpture on low stone plinths. Architectural hedge walls create outdoor rooms. This is the largest of the three regions, integrated into the main lawn area. Not overly modern, but sophisticated: art and landscape woven together, the sculptures punctuating views and creating focal points along curving paths.</p>
    </div>
  </div>
  
  <!-- NATURE GARDEN -->
  <div class="garden-section">
    <img src="data:image/png;base64,{b64("06_nature_garden")}" alt="Nature Garden" class="garden-bg">
    <div class="garden-overlay">
      <h3>Region III: The Nature Garden</h3>
      <p>English wild style: foxglove, lavender, echinacea, and ornamental grasses spilling over stone borders. Species selected to attract butterflies and repel pests naturally. A rustic round open pavilion with a copper roof sits on a steep bank overlooking the naturalistic stream below. This is the romantic corner of the compound, alive with pollinators and gentle chaos.</p>
    </div>
  </div>
  
  <h3>Secret Access</h3>
  <p>Hidden tunnel exits emerge in each of the three regions via hinged living hedge sections that swing open on concealed hardware. An additional emergency egress tunnel exits beyond the exterior wall. The labyrinth is not just beautiful; it is the above-ground expression of the tunnel network below.</p>
</section>

<!-- ═══════════════ THE WATER ═══════════════ -->
<div class="divider"><h2>The Water</h2></div>
<section id="water">
  <h4>Chapter IX</h4>
  <h2>The Water System</h2>
  
  <p class="lead">An engineered naturalistic stream threads the entire compound as a unifying landscape spine. Its origin is concealed inside an artificial berm, appearing as a natural hillside spring. You never see where it begins. You never see where it ends. It simply flows.</p>
  
  <p>The stream crosses the entry drive via a stone bridge, is visible from both guest wing rear courtyards, passes the Wing C living area, flows alongside the pool terrace between the houses, and is visible from the guesthouse upper level. It feeds a naturalistic koi pond at the circular lawn edge.</p>
  
  <p>Formal stone water rills thread through the rose garden and hedge maze sections. The motorcourt features water sheeting down battered stone walls. The atrium waterfall is the one intentionally architectural water element: dramatic, vertical, and honest about what it is.</p>
  
  <div class="card water" style="margin:2rem 0;">
    <h4>Ecological Control</h4>
    <p>No natural water flows through the property. This is by design: the engineered water system provides full control of what lives within the perimeter wall. Venomous snakes (copperheads, water moccasins) are fully eradicated and prevented via habitat control and engineered water management. The stream is recirculating; all pump systems are hidden.</p>
  </div>
</section>

<!-- ═══════════════ THE TUNNELS ═══════════════ -->
<section id="tunnels">
  <h4>Chapter X</h4>
  <h2>The Tunnel Network</h2>
  
  <p class="lead">Two completely separate tunnel systems, commissioned from different contractors. No single builder sees the full layout.</p>
  
  <h3>Primary System</h3>
  <p>Known to intimates. Connects: house to guesthouse, house to rose garden, house to wall exit point.</p>
  
  <h3>Secondary System</h3>
  <p>Private egress. Connects: house to beyond the exterior wall. Known only to the owner and the most trusted.</p>
  
  <h3>Entry Drive Tunnels</h3>
  <p>Under the lawn berm (guest arrival), under the service approach (guesthouse/delivery), and the owner's direct hillside entrance.</p>
  
  <table>
    <tr><th>Type</th><th>Construction</th><th>Clearance</th><th>Notes</th></tr>
    <tr><td>Vehicle (residential)</td><td>Rectangular precast box culvert</td><td>10-12 ft</td><td>Guest and owner entries</td></tr>
    <tr><td>Vehicle (service)</td><td>Rectangular precast box culvert</td><td>14 ft</td><td>Delivery truck rated</td></tr>
    <tr><td>Pedestrian</td><td>6 ft diameter round precast</td><td>6 ft</td><td>Inter-structure connections</td></tr>
  </table>
  
  <p>All tunnels are wheelchair accessible with a maximum grade of 1:10. Total pedestrian network: approximately 300-400 linear feet. All constructed on the unified structural slab.</p>
</section>

<!-- ═══════════════ THE GROUNDS ═══════════════ -->
<section id="grounds">
  <h4>Chapter XI</h4>
  <h2>The Grounds</h2>
  
  <p class="lead">The forest floor within the compound will be fully manicured: ivy ground cover, ferns, soft moss, and native understory plants. Every harmful species eradicated. Every path a pleasure to walk.</p>
  
  <p>Internal forest paths use railroad ties and spongy running surface or soft wood chips. No heavy brambles, no briars, no impassable sections except as one approaches the perimeter wall from outside. The external forest will also receive path development: lovely trails throughout the full 60 acres, connecting to the internal trail system via controlled exit points in the wall.</p>
  
  <div class="two-col">
    <div class="card sage">
      <h4>Internal Forest (~3.6 ac)</h4>
      <p>Manicured floor: native ferns, ivy, moss. All poison ivy, briars, and invasive species removed. Beautiful ground cover throughout. The forest screens the perimeter wall from every internal vantage point.</p>
    </div>
    <div class="card">
      <h4>External Forest (~24 ac)</h4>
      <p>Existing mature second-growth Piedmont forest. Paths with soft surfaces connect throughout. Poison ivy and harmful plants eradicated even outside the wall. Dense, natural screening maintained along the perimeter.</p>
    </div>
  </div>
</section>

<!-- ═══════════════ PHASING ═══════════════ -->
<div class="divider"><h2>The Timeline</h2></div>
<section id="phasing">
  <h4>Chapter XII</h4>
  <h2>Phasing & Timeline</h2>
  
  <p class="lead">Three phases over six years, designed so that the owner occupies the property from Year 2 onward, establishing primary residence while the vision continues to build around him.</p>
  
  <div class="timeline">
    <div class="timeline-item">
      <div class="timeline-label">Phase 1 &middot; Years 0-2 &middot; Foundation</div>
      <h3>Breaking Ground</h3>
      <p>Land acquisition. Full perimeter wall installation. Mass excavation of compound interior. Unified structural slab covering both house footprints, guesthouse, all tunnels, and garages. Entry drive tunnel construction. Main house constructed to livable but unfinished state.</p>
      <p><strong>Milestone:</strong> Owner takes residence to establish North Carolina primary residency and begin mortgage interest deduction. Existing forest provides immediate screening of the wall.</p>
    </div>
    <div class="timeline-item">
      <div class="timeline-label" style="color:var(--sage);">Phase 2 &middot; Years 2-4 &middot; Completion</div>
      <h3>Building the World</h3>
      <p>Fully finish main house interiors. Construct guesthouse superstructure on the Phase 1 slab. Build shared pool, private guest pool, hot tubs, cold plunge. Commission water features around both houses. Owner travels extensively during noisy construction periods.</p>
      <p><strong>Milestone:</strong> Both houses complete and occupied. Pool terrace and immediate landscape operational.</p>
    </div>
    <div class="timeline-item">
      <div class="timeline-label" style="color:var(--water);">Phase 3 &middot; Years 4-6 &middot; The Landscape</div>
      <h3>Growing the Dream</h3>
      <p>Full forest floor clearing and replanting. Engineered naturalistic stream. Koi pond. Full hedge and labyrinth system installation. Rose garden, culture garden, and nature garden development. Formal maze regions. Exterior paths with soft surfaces throughout the full 60 acres.</p>
      <p><strong>Milestone:</strong> The compound vision is complete. The labyrinth is walkable. The stream flows. The worlds within worlds are alive.</p>
    </div>
  </div>
</section>

<!-- ═══════════════ BUDGET ═══════════════ -->
<section id="budget">
  <h4>Chapter XIII</h4>
  <h2>Budget Overview</h2>
  
  <p class="lead">The project is budgeted across three phases, with contingency reserves and architectural fees accounted for. All figures below are shown as percentages of the total project budget.</p>
  
  <table>
    <tr><th>Category</th><th>% of Total</th><th>Phase</th></tr>
    <tr><td>Land Acquisition</td><td>8-9%</td><td>1</td></tr>
    <tr><td>Perimeter Wall</td><td>7-8%</td><td>1</td></tr>
    <tr><td>Underground Infrastructure (slab, excavation, tunnels)</td><td>7-8%</td><td>1</td></tr>
    <tr><td>Main House Construction</td><td>29-32%</td><td>1-2</td></tr>
    <tr><td>Guesthouse Construction</td><td>9-10%</td><td>2</td></tr>
    <tr><td>Pools & Water Features</td><td>4-5%</td><td>2</td></tr>
    <tr><td>Engineered Water System</td><td>4-5%</td><td>3</td></tr>
    <tr><td>Hedge & Labyrinth System</td><td>3-4%</td><td>3</td></tr>
    <tr><td>Gardens, Paths & Forest Management</td><td>13-15%</td><td>3</td></tr>
    <tr><td>Architectural & Engineering Fees</td><td>6-7%</td><td>All</td></tr>
    <tr class="total-row"><td>Contingency Reserve</td><td>8-9%</td><td>All</td></tr>
  </table>
  
  <div class="card" style="margin-top:2rem;">
    <h4>Phase Distribution</h4>
    <table>
      <tr><th>Phase</th><th>Timeline</th><th>% of Budget</th></tr>
      <tr><td>Phase 1: Foundation</td><td>Years 0-2</td><td>48-53%</td></tr>
      <tr><td>Phase 2: Completion</td><td>Years 2-4</td><td>22-24%</td></tr>
      <tr><td>Phase 3: Grounds</td><td>Years 4-6</td><td>22-24%</td></tr>
    </table>
  </div>
  
  <p style="margin-top:2rem; font-size:0.9rem; color:var(--text-light);">Annual maintenance at full completion is estimated at approximately 1.5-2% of total project cost per year, covering landscape maintenance, forest management, water system upkeep, and property management.</p>
</section>

<!-- ═══════════════ MEDIA ═══════════════ -->
<div class="divider"><h2>Gallery</h2></div>
<section id="media">
  <h4>Chapter XIV</h4>
  <h2>Media & Renderings</h2>
  
  <div class="video-placeholder">
    <div class="icon">&#9654;</div>
    <h3>Full Site Flyover Video</h3>
    <p>Coming soon: A complete aerial walkthrough of the compound, generated from the updated 3D model including terrain, wall, driveways, hedge maze, and all structures. To be produced using the architecture-3d Blender workflow.</p>
  </div>
  
  <h3>Concept Gallery</h3>
  <div class="two-col">
    <div>
      <img src="data:image/png;base64,{b64("01_exterior_hill")}" class="img-half" alt="Exterior">
      <p class="img-caption">Main house emerging from the hilltop</p>
    </div>
    <div>
      <img src="data:image/png;base64,{b64("02_motorcourt")}" class="img-half" alt="Motorcourt">
      <p class="img-caption">Sunken motorcourt with water walls</p>
    </div>
  </div>
  <div class="two-col">
    <div>
      <img src="data:image/png;base64,{b64("03_atrium_interior")}" class="img-half" alt="Atrium">
      <p class="img-caption">The 45-foot atrium void</p>
    </div>
    <div>
      <img src="data:image/png;base64,{b64("09_pool_terrace")}" class="img-half" alt="Pool">
      <p class="img-caption">Pool terrace between houses</p>
    </div>
  </div>
  <div class="three-col">
    <div>
      <img src="data:image/png;base64,{b64("05_rose_garden")}" class="img-half" alt="Rose Garden">
      <p class="img-caption">Rose Garden</p>
    </div>
    <div>
      <img src="data:image/png;base64,{b64("07_culture_garden")}" class="img-half" alt="Culture Garden">
      <p class="img-caption">Culture Garden</p>
    </div>
    <div>
      <img src="data:image/png;base64,{b64("06_nature_garden")}" class="img-half" alt="Nature Garden">
      <p class="img-caption">Nature Garden</p>
    </div>
  </div>
</section>

<!-- ═══════════════ APPENDIX ═══════════════ -->
<section id="specs">
  <h4>Appendix</h4>
  <h2>Technical Specifications</h2>
  
  <h3>Main House Dimensions</h3>
  <table>
    <tr><th>Element</th><th>Value</th></tr>
    <tr><td>Hexagon edge length</td><td>23.0 ft</td></tr>
    <tr><td>Atrium area</td><td>1,374 sf</td></tr>
    <tr><td>Wing A (guest suite)</td><td>687 sf</td></tr>
    <tr><td>Wing B (guest suite)</td><td>687 sf</td></tr>
    <tr><td>Wing C (living/dining)</td><td>687 sf</td></tr>
    <tr><td>Triangle Room A (bedroom)</td><td>826 sf</td></tr>
    <tr><td>Triangle Room B (office)</td><td>825 sf</td></tr>
    <tr><td>Triangle Room C (bathroom)</td><td>740 sf</td></tr>
    <tr><td>Total plan area</td><td>7,201 sf</td></tr>
    <tr><td>Ceiling height</td><td>12.0 ft</td></tr>
    <tr><td>Slab thickness</td><td>1.0 ft</td></tr>
    <tr><td>Atrium floor</td><td>-2.0 ft (below entry grade)</td></tr>
    <tr><td>Atrium roof range</td><td>43.0 to 49.0 ft</td></tr>
    <tr><td>Upper ground (wing A/B slab)</td><td>13.0 ft</td></tr>
    <tr><td>Triangle level base</td><td>25.0 ft</td></tr>
  </table>
  
  <h3>Guesthouse</h3>
  <table>
    <tr><th>Element</th><th>Value</th></tr>
    <tr><td>Plan type</td><td>Hexagonal (no atrium)</td></tr>
    <tr><td>Area per level</td><td>~1,374 sf</td></tr>
    <tr><td>Total area</td><td>~2,748 sf</td></tr>
    <tr><td>Levels</td><td>2</td></tr>
  </table>
  
  <h3>Infrastructure</h3>
  <table>
    <tr><th>Element</th><th>Value</th></tr>
    <tr><td>Perimeter wall length</td><td>~1,750 LF</td></tr>
    <tr><td>Wall height (standard)</td><td>12 ft</td></tr>
    <tr><td>Wall height (rose garden section)</td><td>24 ft</td></tr>
    <tr><td>Total hedge</td><td>~12,900 LF</td></tr>
    <tr><td>Perimeter corridors</td><td>~4,500 LF (inner + outer)</td></tr>
    <tr><td>Pedestrian tunnels</td><td>~300-400 LF</td></tr>
    <tr><td>Vehicle tunnel clearance</td><td>10-14 ft</td></tr>
    <tr><td>Driveway ramp</td><td>67.5 ft + 50 ft flat + 50 ft curve</td></tr>
    <tr><td>Motorcourt</td><td>Hexagonal, sunken 12 ft below lawn</td></tr>
    <tr><td>Walled compound area</td><td>~5.6 acres</td></tr>
    <tr><td>Total property</td><td>59.82 acres</td></tr>
  </table>
</section>

<!-- ═══════════════ ADMIN SECTION ═══════════════ -->
<section class="admin-section" id="admin">
  <div style="max-width:1000px; margin:0 auto;">
    <div class="warning">&#9888; This section contains private financial information. It is visible only with the correct access key.</div>
    
    <h2>Financial Detail</h2>
    
    <h3>Current Position (April 2026)</h3>
    <table>
      <tr><th>Metric</th><th>Value</th></tr>
      <tr><td>Current portfolio</td><td>~$3.192M</td></tr>
      <tr><td>Historical annualized return (2010-present)</td><td>~18%+</td></tr>
      <tr><td>Retirement target (6-8 years)</td><td>$8M-$12M+</td></tr>
      <tr><td>Minimum trigger for compound</td><td>$8M portfolio</td></tr>
      <tr><td>Fallback plan</td><td>$3M country club home in Piedmont Triad</td></tr>
      <tr><td>Current monthly housing cost</td><td>~$5,900 (mortgage + HOA + tax + insurance)</td></tr>
      <tr><td>Current home equity</td><td>~$800K-$1M</td></tr>
      <tr><td>Expected annual maintenance at completion</td><td>~$150-200K/yr</td></tr>
    </table>
    
    <h3>Detailed Budget by Line Item</h3>
    <table>
      <tr><th>Category</th><th>Low Estimate</th><th>High Estimate</th><th>% of Total</th></tr>
'''

for name, actual, pct in BUDGET_LINES:
    low, high = actual.replace("$","").split("-")
    html += f'      <tr><td>{name}</td><td>${low}</td><td>${high}</td><td>{pct}</td></tr>\n'

html += '''      <tr class="total-row"><td><strong>GRAND TOTAL</strong></td><td><strong>$6.4M</strong></td><td><strong>$10.1M</strong></td><td><strong>100%</strong></td></tr>
    </table>
    
    <h3>Phase Budget Detail</h3>
    <table>
      <tr><th>Phase</th><th>Years</th><th>Low</th><th>High</th><th>% of Total</th></tr>
'''

for p in BUDGET_PHASES:
    html += f'      <tr><td>{p["phase"]}</td><td>{p["years"]}</td><td>{p["actual_low"]}</td><td>{p["actual_high"]}</td><td>{p["pct"]}</td></tr>\n'

html += f'''    </table>
    
    <h3>Funding Strategy</h3>
    <table>
      <tr><th>Source</th><th>Notes</th></tr>
      <tr><td>Miami condo sale proceeds</td><td>Expected ~$800K-1M+ after payoff and fees</td></tr>
      <tr><td>Retirement account withdrawals</td><td>Strategic pre-tax to Roth conversions to minimize lifetime tax</td></tr>
      <tr><td>Mortgage / construction loan</td><td>NC residency in Phase 1 enables mortgage interest deduction</td></tr>
      <tr><td>Portfolio growth</td><td>18%+ historical returns; AI semiconductor thesis (NVDA, TSMC, MU)</td></tr>
    </table>
    
    <h3 style="margin-top:2rem; color:var(--copper-light);">Budget Audit Notes (April 2026)</h3>
    <div class="warning">
      <p><strong>Perimeter wall:</strong> Original estimate $180-440K is likely low. 2026 market research shows $350-700/LF for 12ft precast. Revised to $500-800K. Mitigating: rural NC, long runs, economies of scale.</p>
      <p style="margin-top:0.5rem;"><strong>Structure costs:</strong> Were not itemized in original planning. Main house $2.2-3.1M and guesthouse $700K-1M are new additions to the budget based on $300-400/sf high-end concrete construction in NC Piedmont.</p>
      <p style="margin-top:0.5rem;"><strong>Risk:</strong> Phase 1 is front-loaded at 48-53% of total budget. Delays or cost overruns here compress Phases 2-3 or require timeline extension. Phased approach provides flexibility to adjust.</p>
    </div>
  </div>
</section>

<!-- ═══════════════ FOOTER ═══════════════ -->
<footer>
  <p>The Compound &middot; A Design Vision by Jon Burchel</p>
  <p>Architect: Toby Witte / Wittehaus</p>
  <p style="margin-top:1rem; font-size:0.75rem;">This document is confidential. April 2026.</p>
</footer>

<!-- ═══════════════ SCRIPTS ═══════════════ -->
<script>
// Admin section visibility
(function() {{
  const params = new URLSearchParams(window.location.search);
  const key = params.get('admin');
  if (key === '{ADMIN_PW}') {{
    document.getElementById('admin').classList.add('visible');
    // Add admin link to nav
    const nav = document.querySelector('nav');
    const link = document.createElement('a');
    link.href = '#admin';
    link.textContent = 'Financials';
    link.style.color = '#e8a87c';
    nav.appendChild(link);
  }}
}})();

// Smooth scroll for nav links
document.querySelectorAll('nav a').forEach(a => {{
  a.addEventListener('click', e => {{
    const href = a.getAttribute('href');
    if (href && href.startsWith('#')) {{
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {{
        target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}
    }}
  }});
}});

// Active nav highlighting on scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav a[href^="#"]');
window.addEventListener('scroll', () => {{
  let current = '';
  sections.forEach(section => {{
    const top = section.offsetTop - 100;
    if (window.scrollY >= top) current = section.getAttribute('id');
  }});
  navLinks.forEach(link => {{
    link.classList.toggle('active', link.getAttribute('href') === '#' + current);
  }});
}});
</script>
</body>
</html>'''

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

size_mb = os.path.getsize(OUT) / (1024*1024)
print(f"Written: {{OUT}}")
print(f"Size: {{size_mb:.1f}} MB")

# Provisional Patent Application

## AUTONOMOUSLY RECONFIGURABLE LIVING LANDSCAPE MAZE SYSTEM AND METHOD

### Inventor
[Jon Burchel - to be completed on filing]

### Filing Date
[To be filed at USPTO.gov]

---

## TITLE OF THE INVENTION

Autonomously Reconfigurable Living Landscape Maze System and Method

---

## CROSS-REFERENCE TO RELATED APPLICATIONS

None.

---

## FIELD OF THE INVENTION

The present invention relates to outdoor landscape maze and labyrinth systems, and more particularly to a system and method for creating a continuously reconfigurable outdoor maze using living plant containers mounted on motorized platforms that autonomously reposition according to programmable schedules.

---

## BACKGROUND OF THE INVENTION

Traditional hedge mazes and labyrinths, such as those found at Hampton Court Palace, the Chateau de Versailles, and various botanical gardens, are static structures. Once planted and grown, their paths and walls remain fixed. Visitors who solve the maze once have no reason to return, as the experience is identical on subsequent visits. Modifications to traditional hedge mazes require years of plant growth and significant horticultural labor.

Prior art in reconfigurable mazes has focused on indoor amusement applications using artificial walls, including hydraulically lifted columns (U.S. Pat. No. 6,855,062), pivoting wall panels (U.S. Pat. No. 6,675,538), and water-jet walls (U.S. Pub. No. 2015/0024856). These systems are limited to indoor or controlled environments, use artificial materials rather than living plants, operate at small scales, and do not integrate with guest navigation or scheduling systems.

There exists a need for a large-scale outdoor maze system that uses living plants to maintain the aesthetic and experiential qualities of a traditional hedge maze while providing continuous reconfigurability, autonomous operation, and integration with digital guest experience systems.

---

## SUMMARY OF THE INVENTION

The present invention provides a system and method for creating a continuously reconfigurable outdoor labyrinth comprising a plurality of living plant containers mounted on motorized transport platforms. Each platform operates within a bounded positioning zone on a prepared surface, repositioning autonomously according to algorithmic scheduling to create new maze configurations. The system integrates with a guest navigation application and emergency management systems.

The invention achieves a maze that is visually and experientially indistinguishable from a traditional planted hedge maze, while being capable of producing a functionally infinite number of unique configurations through the combinatorial repositioning of its movable sections.

---

## DETAILED DESCRIPTION OF THE INVENTION

### 1. System Overview

The reconfigurable living landscape maze system comprises the following primary components:

a) A plurality of **mobile hedge units**, each comprising a living plant container mounted on a motorized transport platform;

b) A network of **prepared positioning surfaces** (positioning zones) distributed throughout the maze footprint;

c) A **central control system** that commands the positioning of mobile hedge units according to programmable schedules;

d) An optional **guest navigation system** that provides wayfinding information adapted to the current maze configuration;

e) An optional **emergency access system** that can simultaneously reposition all mobile hedge units to create clear egress paths.

### 2. Mobile Hedge Units

Each mobile hedge unit comprises:

**2.1 Plant Container.** A durable container (preferably precast concrete, composite, or heavy-gauge metal) of sufficient size to support a mature hedge specimen. Typical dimensions are 6-12 feet in length, 3-6 feet in width, and 3-5 feet in depth, sized to support hedge plants of 8-15 feet in height. The container includes integrated irrigation connections, drainage, and soil volume sufficient for multi-year plant health without transplanting.

**2.2 Plant Material.** Living hedge plants of species suitable for the regional climate and capable of tolerating periodic repositioning. Suitable species include but are not limited to: Thuja standishii x plicata (Green Giant Arborvitae), Ilex x 'Nellie R. Stevens' (Nellie Stevens Holly), Fagus sylvatica (European Beech), Taxus baccata (English Yew), Buxus sempervirens (Common Boxwood), and Prunus laurocerasus (Cherry Laurel). Plants are maintained at heights of 8-15 feet to create opaque visual barriers when viewed from ground level.

**2.3 Trough-and-Elevator Mechanism (Preferred Embodiment).** In the preferred embodiment, each mobile hedge unit operates using a trough-and-elevator system:

- **Receiving trough:** A concrete channel (trough) is set into the path surface at each position where a mobile hedge unit may rest. The trough is sized to receive the base of the plant container such that when the container is lowered into the trough, the bottom edge of the hedge plant meets the surrounding ground level seamlessly. When the trough is unoccupied, it presents as a drainage channel or expansion joint in the paving, indistinguishable from normal landscape infrastructure.

- **Elevator mechanism:** Each mobile hedge unit includes an integrated vertical lift mechanism (scissor jack, pneumatic cylinder, cam mechanism, or similar) capable of raising the plant container approximately 3-6 inches (preferably 5 inches) above the trough rim. This lift height is sufficient to expose a roller or wheel assembly beneath the container base, clearing the trough walls and allowing horizontal movement along the path surface.

- **Roller/wheel assembly:** Concealed beneath the plant container base, exposed only when the elevator mechanism is in the raised position. Comprises powered wheels (electric drive motors) capable of self-propelled movement along the prepared path surface between trough positions. Wheels are rubber or polyurethane for smooth, quiet operation on concrete or paved surfaces.

- **Operating sequence:**
  1. CLOSED (wall): Container rests in trough, hedge at ground level, mechanism invisible. Visually indistinguishable from a permanently planted hedge.
  2. RAISING: Elevator lifts container approximately 5 inches, exposing roller assembly above trough walls.
  3. TRANSIT: Container rolls out of trough onto flush path surface, traverses to destination trough under powered drive or autonomous guidance.
  4. POSITIONING: Container rolls onto destination trough while in raised position, aligns with trough.
  5. LOWERING: Elevator lowers container into destination trough. Hedge base meets ground level. Mechanism concealed.
  6. OPEN (path clear): Vacated trough remains in path surface, appearing as drainage channel or expansion joint. Pedestrians walk over it without obstruction.

- **Locking mechanisms:** Mechanical pins, electromagnetic brakes, or detent systems engage when the container is lowered into a trough, securing it against wind loads, accidental contact, or unauthorized movement.

**2.4 Alternative Transport Mechanism.** In alternative embodiments, the plant container may be mounted on a continuously wheeled or tracked platform as described: The plant container is mounted on a powered wheeled or tracked platform capable of self-propelled movement along the prepared positioning surface. The platform includes:

- Electric drive motors (one or more) powered by onboard rechargeable batteries or wired connection to embedded power supply in the positioning surface;
- Steerable wheels, omnidirectional wheels (mecanum or holonomic), or tracked drive systems;
- Locking mechanisms (mechanical pins, electromagnetic brakes, or wheel locks) that secure the platform in a discrete position;
- Position sensors (GPS, RFID, optical encoders, or combinations thereof) that report the unit's current position to the central control system;
- Wireless communication module (WiFi, LoRa, Zigbee, cellular, or similar) for receiving positioning commands from the central control system;
- Onboard rechargeable power supply with provisions for autonomous or manual recharging;
- Obstruction detection sensors (LIDAR, ultrasonic, infrared, or camera-based) to prevent collisions during repositioning.

**2.5 Self-Leveling Suspension System.** Because outdoor path surfaces may exhibit minor irregularities (settling, frost heave, root intrusion, natural grade variations), each mobile hedge unit includes a self-leveling suspension system:

- Each wheel or wheel cluster is mounted on an independent suspension assembly (spring, pneumatic, or hydraulic) capable of vertical travel of at least 1 inch above and below the nominal ride height (2-inch total range of compensation).
- Omnidirectional pivot capability on each wheel allows the platform to traverse paths that are not perfectly straight or that include gentle curves, without requiring the entire unit to rotate.
- An onboard level sensor (accelerometer, inclinometer, or gyroscopic) continuously monitors the platform attitude and commands individual suspension adjustments to maintain the plant container in a level orientation during transit, preventing soil shifting, root disturbance, or water spillage.
- The self-leveling system also compensates for minor misalignment between the transit surface and the receiving trough, ensuring smooth entry into the trough during the positioning phase.
- In the stationary (closed) position, the suspension is locked to prevent any rocking or movement from wind loads on the hedge plant.

**2.6 Irrigation Integration.** Each mobile hedge unit includes flexible or quick-connect irrigation fittings that allow the unit to connect to water supply at any of its discrete positions within its positioning zone. In the trough-and-elevator embodiment, irrigation supply connections may be integrated into the trough base, automatically engaging when the container is lowered into position. Alternatively, the unit carries an onboard water reservoir sufficient for operation between scheduled irrigation connections.

### 3. Prepared Positioning Surfaces (Positioning Zones)

Each mobile hedge unit operates within a bounded positioning zone comprising:

**3.1 Surface.** A load-bearing prepared surface (reinforced concrete slab, compacted aggregate with paving, precast concrete panels, permeable pavers, stabilized gravel, or similar) capable of supporting the fully loaded weight of the mobile hedge unit (estimated 2,000-10,000 lbs depending on container size and plant maturity). The surface between trough positions should be generally level but need not be perfectly smooth; the self-leveling suspension system (Section 2.5) compensates for surface irregularities of up to 1 inch in any direction. This allows the use of natural-looking outdoor path surfaces (flagstone, brick, textured concrete, compacted gravel) rather than requiring polished indoor-grade flooring, preserving the aesthetic of an outdoor garden environment.

**3.2 Trough Positions (Preferred Embodiment).** Concrete troughs are set into the path surface at each position where a mobile hedge unit may rest. Each trough is:

- Sized to receive the specific container base dimensions with close tolerance;
- Set at a depth such that the lowered container positions the hedge plant base flush with surrounding grade;
- Constructed with smooth interior walls to guide container descent during lowering;
- Optionally fitted with irrigation supply connections at the base;
- Optionally fitted with electrical connections for charging onboard systems;
- Designed to appear as a drainage channel or expansion joint when unoccupied.

**3.3 Guidance Infrastructure.** One or more of the following embedded in or on the positioning surface to guide units between trough positions:

- Flush rail channels or tracks (recessed below surface grade to be invisible to pedestrians);
- RFID markers or magnetic strips at discrete positions;
- Optical guide lines or painted markers (visible or UV-fluorescent);
- GPS reference points with differential correction for centimeter-level accuracy;
- Physical edge guides or shallow channels connecting trough positions.

**3.4 Discrete Positions.** Each positioning zone provides a plurality of discrete trough positions (preferably 4-12 positions) at which the mobile hedge unit may be secured. Positions are arranged in a grid, radial, linear, or custom pattern suited to the local maze geometry. The spacing between positions is sufficient to create meaningfully different path configurations when the unit is repositioned (typically 3-20 feet between adjacent positions).

**3.5 Flush Integration.** The positioning surface, including all troughs and guidance infrastructure, is designed to be flush with surrounding pedestrian path surfaces. Unoccupied troughs and guidance channels are not readily identifiable as maze infrastructure by casual observation, appearing instead as standard landscape drainage or paving features.

### 4. Central Control System

A computerized central control system manages the configuration of the maze by commanding the positions of all mobile hedge units. The control system comprises:

**4.1 Configuration Engine.** Software that generates, stores, and schedules maze configurations. Configurations may be generated by:

- Manual design by an operator;
- Algorithmic generation subject to constraints (e.g., all paths must connect to at least one exit; minimum/maximum difficulty ratings; compliance with accessibility requirements);
- Randomized selection from a library of pre-validated configurations;
- Machine learning or AI-based generation optimized for visitor experience metrics.

**4.2 Scheduling System.** Configurations are applied according to a programmable schedule (e.g., daily, weekly, event-triggered, seasonal). The system supports:

- Timed transitions (e.g., reconfigure at 2:00 AM when no visitors are present);
- Event-triggered transitions (e.g., open a specific path configuration for a scheduled event);
- Emergency transitions (see Section 7);
- Gradual transitions (reconfigure a subset of units per cycle to create progressive change).

**4.3 Safety Validation.** Before executing any configuration change, the control system validates that:

- All pedestrian paths connect to at least one exit;
- No mobile hedge unit movement path is obstructed;
- No visitors are present in active repositioning zones (verified by occupancy sensors, camera systems, or scheduled closure periods);
- The resulting configuration complies with applicable fire egress and accessibility requirements.

**4.4 Position Monitoring.** The control system continuously monitors the reported position of each mobile hedge unit and alerts operators to any discrepancy between commanded and actual positions.

### 5. Guest Navigation System

An optional guest-facing navigation application provides wayfinding adapted to the current maze configuration:

**5.1 Real-Time Map.** The application receives the current maze configuration from the central control system and generates a navigable map. The map may be presented to the guest in various modes:

- **Full map mode:** Shows all open paths and destinations (suitable for accessibility needs);
- **Progressive reveal mode:** Shows only the immediate vicinity of the guest's current position, with paths fading at the edges of revealed area, requiring physical exploration to reveal more;
- **Destination guidance mode:** Shows a path to a guest-selected destination without revealing the overall maze structure;
- **Minimal mode:** Shows only the direction to the nearest exit.

**5.2 Artistic Presentation.** The map is presented in a hand-drawn, illustrated, or stylized aesthetic rather than a technical schematic, maintaining the experiential quality of the maze.

**5.3 Position Tracking.** Guest position within the maze is determined by smartphone GPS, Bluetooth beacons distributed throughout the maze, or similar indoor/outdoor positioning technology.

### 6. Section Closure and Rotation System

The system supports designating subsets of the maze as "closed" to visitors while remaining physically in place:

**6.1 Open/Closed Designation.** Each maze section (which may comprise one or more mobile hedge units and fixed hedge elements) can be designated as open or closed in the central control system. Closed sections are:

- Excluded from the guest navigation application;
- Optionally blocked by positioning mobile hedge units to seal entry paths;
- Available for maintenance, replanting, re-theming, or new construction.

**6.2 Rotation Scheduling.** The control system supports scheduling the opening and closing of sections on independent cycles (e.g., weekly, biweekly, seasonal) to create a continuously changing visitor experience.

### 7. Emergency Access System

In an emergency (fire, medical, severe weather, security), the control system can execute a pre-programmed emergency configuration that:

- Simultaneously commands all mobile hedge units to positions that create clear, direct egress paths from all points in the maze to designated exits;
- Activates visual guidance (projected arrows, illuminated path markings, or similar) on hedge surfaces or path surfaces to direct visitors to exits;
- Communicates the emergency configuration to the guest navigation application, which switches to exit-guidance mode;
- Completes reconfiguration within a predetermined time (preferably under 5 minutes).

### 8. Projected Guidance System

Projectors mounted on poles, structures, or embedded in the ground project visual indicators onto hedge surfaces or path surfaces:

- Directional arrows pointing toward exits during closing time or emergencies;
- Wayfinding indicators for special events;
- Decorative or atmospheric lighting effects during normal operation.

### 9. Anti-Aerial-Observation Features

The system optionally incorporates features to prevent the maze configuration from being solved by aerial observation (drone, satellite, or elevated vantage point):

- Pergolas, arbors, or trained canopy growth over selected path sections to obscure paths from above;
- Mobile hedge units positioned to create the visual appearance of path openings that are physically inaccessible from ground level (false paths);
- Integration with underground passage sections (tunnels) that connect non-adjacent maze sections without visible surface paths;
- Multi-level path crossings (bridges and underpasses) that create vertical path complexity invisible from directly above.

### 10. Variations and Alternative Embodiments

The invention encompasses the following variations:

**10.1 Scale.** The system may be implemented at any scale from a small garden (4-10 mobile units) to a landscape-scale installation (50-200+ mobile units covering multiple acres).

**10.2 Plant Types.** While hedge plants are the preferred embodiment, the mobile containers may support any living plant material including ornamental grasses, bamboo, flowering shrubs, espaliered trees, climbing plants on integrated trellis structures, or combinations thereof.

**10.3 Container Shapes.** Containers may be rectangular, curved, L-shaped, or custom-shaped to create varied wall geometries.

**10.4 Movement Mechanisms.** In addition to wheeled platforms, mobile hedge units may be transported by:

- Air-cushion (hovercraft) systems;
- Magnetic levitation on embedded rail systems;
- Robotic transport vehicles (autonomous mobile robots that dock with and transport containers);
- Hydraulic slide systems;
- Cable-drawn systems.

**10.5 Power Sources.** Platforms may be powered by onboard batteries, embedded inductive charging in the positioning surface, solar panels integrated into the container or platform, wired connections, or combinations thereof.

**10.6 Fixed and Mobile Hybrid.** The maze may comprise a combination of permanently planted (fixed) hedge sections and mobile hedge units, where the fixed sections provide the primary maze structure and the mobile units alter specific junctions, openings, or connections.

**10.7 Integration with Hospitality or Entertainment Operations.** The system may be integrated with hospitality management systems (hotel booking, event scheduling, guest management) to automatically configure the maze for specific events, guest groups, or operational requirements.

**10.8 Data Collection and Optimization.** The system may collect anonymized data on visitor movement patterns, section popularity, average time in maze, and other metrics, and use this data to optimize configuration scheduling, section placement, and guest experience.

---

## CLAIMS (INFORMAL - FOR PROVISIONAL ONLY)

The following informal claims outline the scope of the invention. Formal claims will be prepared for the non-provisional application.

1. A reconfigurable outdoor maze system comprising a plurality of containers holding living plants, each container mounted on a motorized platform capable of autonomous repositioning within a bounded zone on a prepared surface, wherein the positions of the plurality of containers are coordinated by a central control system to create variable maze configurations.

2. The system of claim 1, wherein each motorized platform includes position sensors, wireless communication, locking mechanisms, and obstruction detection.

3. The system of claim 1, further comprising a guest navigation application that adapts its displayed map to the current maze configuration.

4. The system of claim 3, wherein the guest navigation application displays a progressive-reveal map that shows only the guest's immediate vicinity, requiring physical exploration to reveal additional paths.

5. The system of claim 1, further comprising an emergency access mode wherein all mobile containers simultaneously reposition to create direct egress paths.

6. The system of claim 1, wherein the central control system generates configurations algorithmically subject to constraints including path connectivity, accessibility compliance, and difficulty parameters.

7. The system of claim 1, further comprising projected visual guidance on plant or path surfaces for wayfinding during closing periods or emergencies.

8. The system of claim 1, further comprising anti-aerial-observation features including overhead canopy structures, false paths visible only from above, and integration with underground passages.

9. A method of operating a reconfigurable outdoor maze comprising: providing a plurality of living plant containers on motorized platforms; defining a schedule of maze configurations; autonomously repositioning the containers according to the schedule during periods when no visitors are present in repositioning zones; and providing visitors with a navigation application adapted to the current configuration.

10. The method of claim 9, further comprising designating subsets of the maze as open or closed on independent rotation schedules to create a continuously changing visitor experience.

---

## ABSTRACT

A reconfigurable outdoor landscape maze system uses living plants in mobile containers mounted on motorized platforms. Each platform operates within a bounded positioning zone on a prepared level surface, autonomously repositioning to discrete locations under command of a central control system. The system creates a continuously variable outdoor labyrinth that maintains the aesthetic of a traditional hedge maze while producing a functionally unlimited number of unique configurations. The system integrates with a guest navigation application providing progressive-reveal wayfinding, an emergency access mode for rapid egress path creation, a section rotation system for operational flexibility, and anti-aerial-observation features. The invention addresses the fundamental limitation of traditional static hedge mazes by enabling a living landscape that reconfigures itself according to programmable schedules.

---

## DRAWINGS

[To be prepared before filing. Recommended drawings:]

1. Fig. 1 - System overview showing maze footprint with mobile and fixed hedge sections
2. Fig. 2 - Detail of a single mobile hedge unit (side view, showing container, plant, platform, wheels, locking mechanism)
3. Fig. 3 - Detail of positioning zone (top view, showing discrete positions, flush rail channels, guidance infrastructure)
4. Fig. 4 - Two different maze configurations using the same set of mobile hedge units
5. Fig. 5 - Guest navigation application screens (full map, progressive reveal, destination guidance, exit mode)
6. Fig. 6 - Emergency configuration showing direct egress paths
7. Fig. 7 - Anti-aerial-observation features (cross-section showing false path, overhead canopy, tunnel integration)
8. Fig. 8 - System architecture diagram (mobile units, central control, guest app, emergency system)

[Hand-drawn sketches are acceptable for provisional filing.]

---

## FILING INSTRUCTIONS

### To file this provisional patent application:

1. Go to https://www.uspto.gov/patents/apply
2. Create a USPTO.gov account if you don't have one
3. Select "File Online" via "Patent Center"
4. Choose "Provisional Application for Patent"
5. Upload this document as the specification
6. Prepare and upload simple drawings (hand-drawn is fine)
7. Complete the cover sheet (form SB/16) with inventor information
8. Pay the filing fee: $320 (small entity) or $160 (micro entity*)
9. Save your confirmation number and filing date

*Micro entity status: You may qualify if your gross income is less than 3x the median household income (~$225,000 in 2026) and you haven't been named as inventor on more than 4 prior applications.

### After Filing
- You have 12 months to convert to a full (non-provisional) utility patent application
- During this period, you may mark the invention as "Patent Pending"
- You may file a new provisional before the 12 months expires to extend priority
- Consult a patent attorney before the 12-month deadline to prepare formal claims

---

*This document is a draft provisional patent application. Review all details for accuracy before filing. This is not legal advice. Consider consulting a registered patent attorney or agent for review before filing.*

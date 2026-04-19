---
title: "SpaceX Software Engineering AMA — Falcon, Dragon, Starlink Deep Dive"
date: "2026-04-19"
category: "software-engineering"
subcategory: "architecture"
tags: [spacex, aerospace, embedded, real-time, c-plus-plus, linux, fault-tolerance, redundancy, starlink, dragon, falcon9, rva-tech-talks]
author: "Ford Prior"
status: "final"
confidence: "high"
sources_verified: true
---

# SpaceX Software Engineering AMA — Falcon, Dragon, Starlink Deep Dive

## TL;DR

SpaceX's flight software is built on custom Linux (with PREEMPT_RT), C++ at the application layer, and a multi-computer redundant architecture with hardware-in-the-loop testing as the gold standard. Their Crew Dragon displays are a web stack (Chromium/HTML/JS/CSS) with an in-house reactive library — a first-principles choice that paid off. Dragon and Falcon use zero AI/ML.

## Context

This is a summary and transcript recreation of a Reddit AMA conducted by SpaceX's software team around June 2020, shortly after the Demo-2 crewed launch of Crew Dragon with astronauts Bob Behnken and Doug Hurley. The AMA was reconstructed and presented as an episode of the RVA Tech Talks podcast by Ford Prior and his sister Morgan. Contributors included:

- **Jeff Dexter** — Flight software & cybersecurity
- **Josh Sulkin** — Software design lead, Crew Dragon
- **Wendy Shimada** — Dragon software team manager, fault tolerance & safety
- **John Dietrich** — Lead software dev, Demo-2
- **Sofian (last name unclear)** — Lead, crew displays software, Demo-2
- **Matt Monson** — Starlink software lead (former Dragon)

## Key Findings

### Career Advice from SpaceX Engineers

**Getting a job at SpaceX (Jeff Dexter):**
- Get a CS degree or equivalent
- Engineers who do well are meticulous about understanding how everything works: code, network, Linux, hardware
- Get real-world experience: hobby projects or internships
- Focus on algorithms & data structures and understanding computers at the lowest levels — even if you never touch device drivers or assembly, understanding the stack enables you to solve any problem
- Crossover from video game development is particularly good — math-heavy and performance-centric problems overlap significantly
- SpaceX software engineers are primarily in Seattle and Hawthorne (CA); some work in Texas

### Technology Stack

**Flight software (Falcon 9, Dragon):**
- Language: **C++** for all application-level autonomous software
- Paradigm: Object-oriented, but kept as simple as possible
- Open source used: DAS, U-boot, buildroot, musl (outside of the OS and crew display software, very little outside software)
- Policy: Use only extremely high-quality open source libraries; often develop own libraries to control code quality

**Crew displays (Dragon):**
- Stack: **HTML, JavaScript, CSS** rendered by Chromium
- Reactive programming: custom in-house reactive library
- Web Components used extensively
- No LESS; uses plain CSS
- Hardware: dedicated quad-core processor similar in power to a 5-year-old phone (at time of AMA, ~2015-era mobile SoC)
- Not Tesla hardware
- Started as a simulator prototype to show NASA a design vision; then found it worked well on flight hardware with modifications; committed to the stack from there

**OS:**
- **Linux** with the **PREEMPT_RT patch** for real-time performance
- No off-the-shelf distro — SpaceX maintains their own kernel
- Small custom modifications + custom hardware drivers
- Supports multiple hardware architectures (not specified)

**Testing:**
- **Python** for testing

**Editors:**
- Team members use different editors; Sofian prefers VS Code

### Architecture

**Modular, hierarchical design:**
- Multiple small modules organized in a hierarchy: low-level component → subsystem → entire vehicle
- Different subsystems are isolated from each other, sometimes on the same computer, sometimes across computers
- Narrow interfaces between subsystems

**Real-time control loop:**
> "Almost everything can be expressed as a real-time control loop. You read some sensors, you make a decision (a combination of your sensors and the past state), then issue the outputs of that decision back to the hardware. This happens many times per second." — John Dietrich

**Many distributed computers** running in time-synchronized lockstep, overseen by a flight computer.

**Software configuration (not code) changes per mission:** Same Falcon source for every mission, but configs provided by other engineering groups change each mission — state machines, fault tolerance thresholds, day-of-launch winds, etc.

### Redundancy & Fault Tolerance

**Falcon 9:**
- Triplicates almost everything (flight computers, sensors, actuators)
- Can tolerate loss of **any one** flight computer, sensor, or actuator
- Algorithm-level compensation for engine/thruster loss

**Dragon:**
- **Two-fault tolerant**: Must be capable of safely retreating from ISS and returning home even after any two failures (NASA requirement)
- Multiple computers, sensors, actuators
- Software fault responses coordinated across subsystems
- Autonomous state machine: can switch from "approach" mode to "breakout" if failures detected
- Interesting edge case: computer reboots in flight are completely expected and designed for (due to radiation)

**Starlink:**
- System-level fault tolerance: multiple satellites in view simultaneously, so individual failures are absorbed
- Satellites designed to passively de-orbit via atmospheric drag in case of failure; SpaceX fights hard to actively de-orbit when possible
- High drag state triggered if satellite hasn't heard from ground in a long time (predictable deorbit)

**Error detection:**
- Radiation-induced errors: multiple redundant computers with voting on outputs
- Sensor errors: multiple different sensors
- Data transmission errors: error-detecting/correcting codes on each payload

### Autonomous Flight Termination System (AFSS)

- Runs on independent microcontrollers, completely separate from the flight computer
- Receives sensor inputs directly (IMU measurements) and some computed inputs from flight computer
- Mission data load configures which conditions trigger termination (off-course, loss of acceleration, etc.)

### Testing & Release

**Testing approaches (in order of rigor):**
1. Unit tests
2. Containerized integration tests (runnable on personal machine with full physics simulation)
3. Full hardware-in-the-loop (HITL) on real flight hardware with physics simulation

"Mating the flight software against the simulator is the most powerful tool we have for testing, especially when run on the real hardware. We can simulate an entire mission and even many detailed fault scenarios with the vehicle hardware just sitting on a table in the lab." — Dietrich

**Continuous integration:** Code is always being tested; if any key performance indicator is violated, the test case "fails" and an engineer investigates.

**Dragon release cycle:**
- Periodic releases cut for integration/testing
- Full suite of tests run against specific code revision
- For Demo-2: code aggressively stabilized starting January 2020, locked down for several months before May launch
- Weather-scrub attempt on May 27 was used as a full-up test up to T-minus zero — learned a lot, ultimately changed nothing

**Software freeze before flight:** "Several months" — no changes after that point

### Starlink Specifics

**Scale:**
- Each batch of 60 satellites: >4,000 Linux computers
- Constellation (at time of AMA): >30,000 Linux nodes, >6,000 microcontrollers in space
- Shares Linux platform and infrastructure with Falcon and Dragon → benefits from >180 vehicle-years of on-orbit test time

**Update cadence:**
- Satellite software updated ~**once per week**
- Smaller test deployments more frequently
- Ground services deployed **several times per week or more**
- By launch day, new satellites are already on an older build than the rest of the constellation

**Canary deployments:** Test build deployed to small subset of satellites, compare performance vs. fleet; if it doesn't perform, tweak and retry; if problem found during rollout, pause, roll back, try again.

**Data:** Generating >5 terabytes of telemetry per day; actively reducing per-device data; analysis of problems on-board to reduce what needs to be sent back

**Custom ASICs:** Yes, SpaceX does custom ASIC development for Starlink

**Security:** End-to-end encryption for user data; all hardware only runs software signed by SpaceX (no permanent foothold even if compromised); defense-in-depth within data centers

### AI/ML Policy

**Dragon and Falcon: zero AI/ML.** ("Dragon does not use any AI." — Dietrich)

Exception: Dragon uses computer vision for navigation only. Possibility of AI/ML in SpaceX's future, but not in flight-critical systems at time of AMA.

### Tech Debt

Managed actively, especially on frequently-flown vehicles. Small team means inefficiency is visible. Balance between new features and burning down debt each flight cycle. Similar to most software organizations — tech debt is always a conversation.

### Crew Display UI/UX Process

**Design principles:** Human-centered design; "minimum crew interaction as success criteria" — don't require the crew to press a button if you can avoid it. Clarity, simplicity, removing clutter.

**Glove testing:** Tested for vibration and visibility conditions; crew did many suited simulations interacting with displays while wearing gloves.

**Crew feedback:** Bob Behnken and Doug Hurley worked closely with the SpaceX team since the start of the program, spent extensive time in Hawthorne providing feedback on displays, button panels, audio system, and backup capabilities. Their work ethic was described as "truly inspirational."

**Physical backup buttons:** Hardware buttons below the displays as a failsafe for critical actions (e.g., responding to cabin fire) in case the displays are unusable.

**Ground displays:** The same code that runs on the crew displays can run on the ground, fed by live telemetry. Limitation: not all cockpit telemetry available on the ground due to RF budget constraints.

**Cross-pollination:** The map and alerts from crew displays formed the basis of the Starlink UI; Starship ground software uses the crew displays tech stack.

**Docking simulator:** Developed by the crew displays team as a "fun project" (Shane Milkey and Mike Westenhaver); finished and published to the web before Demo-2.

### Starlink Future

- Still evolving rapidly (at time of AMA)
- Customer self-service interface using crew display tech stack heritage

## Analysis

SpaceX's software approach is a study in disciplined minimalism under extreme constraints:

1. **Proven over novel.** They default to what they understand. Custom Linux build rather than a distro they can't fully control. In-house libraries rather than open source they can't vet. C++ they know rather than Rust they don't (at time of AMA). They only deviate from this rule when the deviation has high upside (e.g., the web stack for displays — accessible to a large talent pool, proven in industry, and prototyped successfully before commitment).

2. **Test everything multiple ways.** The layered testing approach (unit → integration → HITL → actual flight) isn't bureaucratic — each layer catches different failure modes. Hardware-in-the-loop is particularly powerful because it surfaces real-time behavior that software-only simulation cannot.

3. **Redundancy is systemic, not incidental.** Fault tolerance is designed in at the hardware, software, algorithm, and system levels simultaneously. No single layer is expected to carry the full burden.

4. **Starlink as a different paradigm.** Starlink operates more like a web service fleet than a spacecraft — canary deployments, weekly software updates, system-level fault tolerance rather than per-satellite hardening. This is a profound shift in how space vehicles are thought about.

5. **Small teams, high visibility.** A team small enough that every inefficiency is visible forces good engineering discipline. Tech debt can't hide.

## Implications

- The "web stack for mission-critical displays" precedent matters: if you have the right testing discipline and performance rigor, familiar stacks can be used in unfamiliar domains
- PREEMPT_RT Linux as a real-time OS substrate is well-validated at this scale — not exotic
- System-level fault tolerance (redundant nodes) can substitute for per-unit hardening in large constellations
- The gap between SpaceX's code-freeze discipline and typical software shops is enormous — months of stability before a flight
- Canary deployments in space are real and working

## Open Questions

- [ ] Has SpaceX introduced AI/ML into flight-critical systems since 2020?
- [ ] What is the PREEMPT_RT patch adoption story — upstream integration status?
- [ ] How does Dragon's display tech stack evolve for Starship crewed flights?
- [ ] What does SpaceX's bug bounty program look like today?

## Sources

1. SpaceX Software Team Reddit AMA, r/spacex, ~June 2020
2. RVA Tech Talks podcast episode — "SpaceX AMA" hosted by Ford Prior, recreated with Morgan Prior
3. SpaceX Crew Dragon docking simulator: [https://iss-sim.spacex.com](https://iss-sim.spacex.com)

## Appendix

### Q&A Highlights (verbatim reconstructions)

**On the craziest thing Elon asked for:**
> "I recall for F9-14, I was in Elon's cube telling him there was no way we could get all of the new S1 landing code done in time for the upcoming launch in two weeks. After some thought, he looked over to Lars Blackmore and asked: if we could implement the code, what was our probability of landing? Lars said around 90%. Elon looked at us and basically said, 'Can you give me 50%?' I said, in two weeks, we can definitely get right enough of the logic to get you 50% probability of landing. We didn't land F9-14 — you can see it on our blooper reel — but we learned a lot from it, and it was instrumental in eventually landing F9-21. A critical part of our success is our willingness to fail in ways that won't compromise the mission." — Jeff Dexter

**On the coolest thing Dragon can do:**
> "Dragon can manage a complicated, delicate, zero-G rendezvous with ISS, and it can also fly all by itself to safety in a supersonic mini-G orbit in the thickest parts of the atmosphere." — Dietrich

> "Although we hope it's never used with the crew on board, I think the launch escape system is one of the coolest parts of Dragon. I watched the Pad Abort test live in Cape Canaveral — I was shocked by how fast the vehicle leapt off the pad. Dragon separated smoothly from F9 opening up a large separation distance while F9 exploded underneath. It looked like a sci-fi movie, except it was real." — Josh Sulkin

**On the Chromium choice:**
> "The use of Chromium and JavaScript in mission-critical environments is a popular question. Chromium in this context is used as a UI rendering engine only — the flight software interaction layer with the displays and the fault-tolerant [system] is well-defined and resides outside the displays boundary. We follow the same development process for all vehicle code regardless of the technology stack. We cross-train our developers to write vehicle code in C++ and then carry the same mentality towards writing reliable software. We also liked having access to the talent that is already trained in that stack. We are not afraid of doing things slightly differently here at SpaceX — we like taking a first-principles approach to problem solving." — Sofian

**On Linux:**
> "Yes, we run Linux with the PREEMPT_RT patch applied in order to get better real-time performance. We don't use any third-party distro, but maintain our own copy of the kernel and associated tools. We've made small changes to the kernel over the years, although it's mostly unmodified — the only exception is the addition of several custom drivers to interface with our hardware." — Dietrich

**On Starlink's novel approach:**
> "We need to think of our satellites more like servers in a data center than like a special one-of-a-kind vehicle... we can deploy a test build to a small subset of our vehicles and then compare how it performs against the rest of the fleet. If it doesn't do what we want, we can tweak it and try again before merging it. If we see a problem when rolling out, we can pause, roll back, and try again. This is a hugely powerful change in how we think about space vehicles, and absolutely critical to being able to iterate quickly." — Jeff

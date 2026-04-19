---
title: "Ford Prior — Tech Career Story"
date: "2026-04-19"
category: "personal"
subcategory: "career"
tags: [ford-prior, tech-career, amazon, capital-one, snagajob, qe-automation, aws, python, ruby, richmond, rva-tech-talks, meetups, geico, flying-pig-labs]
author: "Ford Prior"
status: "final"
confidence: "high"
sources_verified: false
source: "Otter.ai transcript (approx. 2023–2024) + deep research (April 2026, parallel.ai)"
---

# Ford Prior — Tech Career Story

## TL;DR

Ford Prior graduated from JMU with English and Spanish degrees in 2011, spent years struggling to find meaningful work, and talked his way into tech without a CS background. Over roughly a decade he went from ~$44k as a QA analyst to ~$324k total compensation as a Senior Software Engineer at Amazon — building skills one layer at a time (manual QA → test automation → cloud → Python → TypeScript → AI/ML adjacent work). Nearly every job came through networking, not applications. He also built the RVA Tech Talks podcast and Richmond tech meetups as a parallel career-building strategy.

## Context

This is a personal narrative recording by Ford Prior telling the story of his career in technology. He describes it as "a little haphazard" and acknowledges he "could use help coming up with a more interesting narrative." The recording appears to be a solo voice memo, speaking into a recorder with some background context dropped in. No interviewer. Estimated date: 2023–2024.

---

## Career Timeline

### Pre-Tech: 2011–2014 — The Lost Years

**Education:** James Madison University (JMU), Harrisonburg, VA
- Degrees: **English** and **Spanish**
- Graduated ~2011 into a very difficult job market

**Original ambition:** Ford originally wanted to be a **cattle farmer** — a small-scale agriculturalist in rural Virginia. He'd fallen in love with Bridget and, when he started thinking about starting a family, realized he needed "a trade — something that people valued."

**What drew him to tech:**
> "What really drew me to technology was just the feeling of importance — like, I have a skill that people want. I had spent long enough feeling like I had no skills that people wanted, and it made me feel powerless. It made me feel emasculated even. And at the end of the day, I just wanted to feel like I was important."

**Jobs during this period:**
- **Blue Sky Fund**: Teaching environmental science, 7am–2pm daily
- **Brown Greer law firm**: Deepwater Horizon oil spill claims administration, 4:30pm–midnight
  - Used a GIS tool to locate **sustenance losses** — mapping how much game and fish existed in Gulf coast areas at certain times, then validating those against claims from people living off the land who lost their livelihoods
  - Data came in weekly from state agencies, NOAA, land management bureaus, Coastal Resource/Wildlife Refuge groups, federal hydrological data
  - Found this work fascinating; first exposure to data tools being used to serve real human problems
- Simultaneously: audited/paid for classes at **VCU** — GIS and Environmental Policy (~$2,000–3,000; billed after the fact, pissed him off)
  - GIS class: he was too tired at night to do well, but it planted a seed
  - Environmental Policy: motivated by thinking he might become a lawyer (he worked at a law firm, was dating Bill Prior's daughter, found law fascinating — "a weird world where words held covenants")
  - Read *Don't Become a Lawyer*: convinced him not to, after seeing paralegals with law degrees and huge debt working miserable jobs

**Daily schedule during this period:**
- 6am: arrive at Blue Sky Fund office, take an hour jog before shift
- 7am: teach environmental science
- 2pm: end shift, drive home
- Nap
- 4:30pm: arrive at law office
- Midnight: end shift
- Repeat

"My life was great — really fucking great, just goddamn Charmed."

---

### VCU IT Management Master's Program — ~2013–2015

- Convinced **Maureen Carley**, director of admissions for VCU's master's in IT management, to let him in with **zero IT experience** using the "buy low, sell high" pitch: "I'm a low-priced asset right now that's only going up."
- His father **Bill Prior** joined the same program (Bill needed a master's degree to teach at the next level at University of Richmond)
- Format: **every Saturday all day, plus most of Sunday** — roughly 1.5 years, summers and winters off
- "My dad and I were kind of like the people everyone was amused that we were in the class"
- Ford asked relentless questions — didn't care if they sounded stupid — and got positive feedback for it
- **Key takeaway**: IT management is just management; he knew he didn't want to do management — he wanted to solve problems and build things
- Also received feedback that he should be in a job where he talks a lot — advice he mostly ignored at the time

---

### Acuity (Legal Billing Software) — ~2014–2015

**Placement by:** Staffing agency recruiter Cami Little  
**How he got the meeting:** Bruce Slough (family friend) connected him to Debbie Mills at Magellan Health; she was hiring QA people; but it was Cami Little at a staffing agency who eventually placed him at Acuity

**Acuity Legal Enterprise Management Systems** — a ~25-person legal billing software company in **Manchester, Richmond**
- CEO: Kelly Johnston; CTO: Troy; Tech Director: Daryl
- Engineering team of ~7 total (including CTO and director)
- Stack: **Pearl (Perl)** for the application, **MySQL** database
- Small "pod" team: Jurgen (little German lead engineer, very nice), Jim (tattooed, heavily bearded Burning Man type, drove a van with a skull, did blacksmithing — "total goofball"), Mark (Ron Cartwright — senior engineer, grumpy; later likely laid off; had chickens, wife had cancer, struggled with depression; Ford had long conversations with him about his life)
- Culture: small and tight, "shouty matches" over bug priority between QA and Dev; PM would weigh in when they couldn't break ties

**What Ford did:**
- Manual QA: clicking through legal billing applications to verify requirements
- Deployments: manual deployments of slightly modified application copies for different customers
- Tools learned: **Microsoft Access** (basic relational tables and queries), **Selenium IDE** (record-and-playback UI testing)
- Side project: Rachel Sharma's husband suggested Selenium; they used it to record and replay user flows in a test deployment environment
- Started learning basic **Ruby** in evenings ("Hello World, basic Ruby setup") to eventually level up to automation

**Pay:** ~$44–48k starting

**Note on working style (self-reflection):**
> "I've been fucking around at my desk at jobs my whole career — which is kind of depressing to think about. But when I say fucking around, I don't mean playing video games. I mean doing little side projects no one asked me to do."

He was also managed by **Michelle Lowe** (a contractor manager) with whom he had ongoing friction: she tracked hours closely; he would walk around too much, occasionally not show up without calling in. "I wouldn't say she was my favorite, but no hard feelings."

---

### Magellan Health (QA) — ~2015

**Placement by:** Staffing agency (may have been Cami Little again)  
**Role:** QA, data migration project  

- Larger company; working on a migration of huge relational data sets from one system to another (tech stack not recalled)
- Worked in a **war room with an agile process**
- Manager: effervescent woman who "brought life to the office" and led the team  
- Teammates were "really fun women in tech who loved their jobs"
- Put onto a more boring **health claims QA** track after the migration; knew it was temporary

**Skills gained:**
- Agile process exposure (war room format)
- More Selenium practice
- Started learning Ruby automation more seriously

---

### SnagaJob (QA Engineer, then Sr. QA Engineer) — ~2015–2018

**Placement by:** Cami Little (or Kate Flannery) connected him to **Chris Monger** at SnagaJob, who was building out their QA org

**SnagaJob** — one of Richmond's landmark tech companies; online hourly job marketplace
- Engineering org: ~100 engineers; total company ~350
- Got the job despite barely knowing Ruby — the interviewers didn't know Ruby either; only one engineer on the team did
- Starting comp: ~$75,000
- At time of joining: top of their investment bubble — had received a **Series F, $75 million**; heavy investment in tech, acquired products; very exciting
- By 2018: investment climate shifted; things didn't sell as well; two huge layoffs occurred
- Ford survived both layoffs; then got a better offer from Capital One and left

**What Ford built:**
- A full **Ruby test automation system** — large library of scripts testing product flows
- Put the whole automation system in **the cloud** (first real cloud experience — AWS)
- Learned ton of Ruby; learned ton of AWS

**Culture:**
- First "real" engineering org — legitimate, legit engineers, respected Richmond company
- Fridays at 3pm: tech talks for everyone; "I fucking loved that"
- Lunch as a team; org events; "young people who all appreciated me"
- "All in" — worked evenings adding code, making a good impression, meeting people, very well liked

**Promotions & negotiation:**
- Got promoted once or twice
- Got a competing offer from **CapTech** (~1.5 years in); used it to negotiate salary from $75k → **$98k** ("I was a ballsy motherfucker")
- Promised his boss to stay a year after the negotiation; boss got laid off 6 months later; Ford left for Capital One

---

### Capital One (QA/Cloud Engineer) — ~2018–2021

**How:** SnagaJob experience + AWS skills got him through a 3-round on-site interview (whiteboarding, no phones, engineers walking the campus)  
**Starting comp:** ~$105–110k

**Capital One campus** (McLean, VA / remote): "Such a cool period of life... all these engineers at the campus — distinguished engineers, huge tech culture"

**First assignment — Fraud Detection (East/West Failover):**
- Writing a **Jenkins script** to automate failover from East to West AWS regions
- Context: in financial industry, need to be able to "turn East black" and route traffic to West (nuclear attack planning / financial continuity requirement)
- Working next to **fraud investigators** — "grizzled, tattooed guys, former Marines who were like detectives tracking down fraud"
- Worked with a **COBOL transaction warehouse** — had a colleague Stanley ("an Indian guy with a little shrine to some random guru guy next to his desk") who peacefully wrote COBOL all day
- The rule management system: a Python notebook-based tool that let fraud investigators tune rules without engaging engineering; saving **$50–75 million a year in fraud prevention**; this system's success led to funding which led to a rewrite (which went badly — "horrifying Python application")
- **Key skill gained: Python** — learned it comprehensively for the first time on this job
  - Built a **James River water gauge Alexa skill** (Python) on the side
  - Started writing Python scripts, building side apps
  - "I did Python all day, all night. That was my thing at Capital One."

**Promoted — moved to "Share Tech" (Developer Experience):**
- Was the worst person on the team by far (except for "Al")
- Building enterprise pipelines used by teams like the fraud team he'd come from
- Stack: **TypeScript/JavaScript, Java/Groovy** — he didn't love it, was stubborn about TypeScript, didn't do that well
- Had 4 different managers in <1 year due to restructuring / pandemic disruption
- COVID hit right as he joined — never met his team in person
- Went to **Costa Rica** without telling Capital One; worked remotely; came back; was put on a **performance improvement plan (PIP)** within weeks of returning
- Quit within a couple weeks of the PIP, with two job offers already in hand

**Parallel work during Capital One:**
- Significant **Ansible + Python** work on "bogey gears" — shared code modules (inner-sourced) that did things like deploy standard S3 buckets with all Capital One permissions baked in; published some blog posts about this ("my first DevRel muscle")
- "I was in cloud administration — managing CloudFormation templates, load balancers, network gateways, deployed resources, blue-green deployments, pipeline management"

---

### CarMax (Cloud Engineer) — ~2021–2022

**How:** Two job offers when leaving Capital One — CarMax ($150k) and SingleStone ($150k); chose CarMax  
**Manager:** Craig; also Chuks  
**Stack:** **Azure** (no prior Azure experience; they trusted him to learn on the job)

**What Ford did:**
- All cloud work in **Azure**
- Python with Azure SDKs
- Cloud governance scripting: tagging strategies, data generation for auditing
- **Saved ~$500,000** on reserved instances they weren't using; identified new reserved instances for ML workloads that saved significant money
- Cloud administration: right-sizing, governance, audit

**Honest assessment:**
> "I was bored. Carmax just bored the hell out of me, honestly. And I was kind of still depressed about COVID."

- Stayed ~1.5 years
- Interviewed at **Amazon Web Services (AWS) for the 5th time** while at CarMax — had tried four times before; finally got through

---

### Amazon Web Services (Sr. Software Development Engineer, Code Examples) — ~2022–Present

**How:** 5th AWS interview attempt; interviewed for the **Code Examples team**  
**Starting total comp:** ~$250,000 (includes stock; paycheck ~same as CarMax $150k base, with rest in stock)  
**Current total comp (after title change to Software Engineer):** ~**$324,000**

**What the team does (at time of joining):**
- Handwriting code examples demonstrating how to use AWS SDK features
- Small, somewhat "sleepy" team

**What Ford helped transform it into:**
- An **AI/prompt-engineering-enabled** team
- Deploying code snippets from distributed repos into a unified doc system
- Using Gen AI extensively to automate example generation and validation
- "Kind of proud of what we've done"

**Languages used:** Python (primary), Ruby (again), TypeScript (had to learn), more cloud work (obviously, working for AWS)

**Interview process:** "Hard as fuck. Three or four rounds, raising the bar all the time. Barely keeping up."

**Current challenge (at time of recording):**
- Gen AI is making code example writers' jobs less necessary — the work is "being worked out of jobs"
- Ford's team title changed to Software Engineer; may survive better than pure writers
- Waiting on stock vesting in May; uncertainty about layoffs

---

## Networking as Career Strategy

> "Almost every job I've ever gotten, I have not applied for. I've known someone there, and I've talked to them, gotten coffee with someone, made an email impression. I've gotten all my jobs through networking."

**The RVA Tech Talks podcast:**
- Started at Acuity during lunch breaks, at his desk with his podcast setup
- Did interviews over Skype and in person with an iPhone
- Primary motivation: "An excuse to email people I want to learn from and want to be like — and get a chance to talk to them and impress them"
- Pitched the RVA (Richmond tech association) on it; they ghosted him
- New executive director later reached out: they paid him ~$150/episode and provided a real studio
- Did episodes in a legit studio for a while; then interest faded; "I don't know why I don't get back in the habit of doing that — that was good for me"

**Richmond tech meetups:**
- Started a **QA meetup** while doing QA work
- As he moved into cloud/programming, created a **Cloud meetup**
  - Grew to **1,000+ members**
  - Regular meetups of 30–50 people
  - COVID ended the in-person culture; never fully recovered
- Meetups served multiple purposes: community visibility, excuse to stay current (he had to present sometimes), reason to meet potential employers and colleagues
- "Hustling — talking people into liking me — has been a huge part of my tech career progressing."

---

### GEICO (Senior Staff Engineer & Tech Evangelist) — 2025–Present

**How:** Left Amazon; joined GEICO to run an innovation lab  
**Title:** Senior Staff Engineer & Tech Evangelist  
**Context:** A new chapter focused on AI-driven innovation rather than pure engineering execution

**What Ford does:**
- Runs GEICO's **innovation lab** — using AI to generate "truly novel and feasible ideas" (documented in his article "The Ideation Engine")
- Builds **knowledge management systems** — e.g., turned 147 unread meeting notes into a living knowledge base in 30 days
- Continues the evangelist work: speaking, writing, representing the company externally

**Published work from this role:**
- "The Ideation Engine: How I Used AI to Generate Truly Novel & Feasible Ideas at GEICO" — LinkedIn, Nov 19, 2025
- "From 147 Unread Meeting Notes to a Living Knowledge Base in 30 Days" — LinkedIn, Nov 14, 2025
- "Learning Open Source AI Models On My Morning Commute in Richmond, VA" — LinkedIn, Nov 3, 2025
- "Augment, Don't Automate: How to Stay Valuable While Using AI" — LinkedIn, Oct 27, 2025

**June 2025 public talk:** "Hacking the Future - Notes from the Front Lines of GenAI @ AWS" — AWS User Group Richmond, at Ippon Technology HQ, described as "former engineer at AWS"

**Flying Pig Labs:** Ford's personal consultancy/venture. Listed as a sponsor for his June 2025 AWS User Group talk. The GitHub org `Flying-Pig-Labs` hosts the `rvaopenclaw` repo.

---

## Compensation History

| Company | Approx. Pay |
|---|---|
| Brown Greer (law firm) | ~$25/hour |
| Acuity | $44–48k |
| Magellan | ~similar |
| SnagaJob (start) | $75k |
| SnagaJob (negotiated) | $98k |
| Capital One | $105–110k start; promoted to ~$125k |
| CarMax | $150k |
| Amazon (total comp, start) | ~$250k |
| Amazon (total comp, final) | ~$324k |
| GEICO | not disclosed |

**~10x salary growth over ~10 years.** From ~$44k (2014) to ~$324k total comp at Amazon peak (~2024), then to GEICO.

---

## Community Building & Public Presence

*(Not covered in the voice recording — sourced from deep research, April 2026)*

### RVA Tech Talks Podcast
- Started at Acuity during lunch breaks with a basic setup; did early interviews via Skype and iPhone
- Primary motivation: an excuse to email people he wanted to learn from and impress
- Pitched to rvatech; got ghosted; new exec director later came back and paid ~$150/episode with a real studio
- Role evolved to host, co-host, and moderator of formal episodes (e.g., moderated "2022 Data Summit Live" and "Roundtable Talk On All Things Data" while at CarMax)
- Still active in some form as of 2022

### Richmond Cloud Wranglers (AWS/GCP/Azure User Group)
- Started as a QA meetup; evolved into a cloud meetup as his career did
- **1,000+ members**
- **32 events organized**; personally presented original content at **12+ events**
- Pre-COVID: 30–50 people per event regularly
- COVID ended in-person momentum; never fully recovered

### rvatech/ Code & Cloud Conference
- **Co-chair** of the annual Richmond tech conference
- Mentioned in his LinkedIn "About" section; confirmed by the 2025 conference event page

### Sidekick RVA
- **Volunteer job coach and mentor** for people entering the Richmond tech community

### Richmond Folk Festival
- **Volunteer music logger for the Library of Congress** — long-running; mentioned in his professional volunteering section

### Flying Pig Labs
- Personal consultancy and venture label
- GitHub org `Flying-Pig-Labs` (hosts `rvaopenclaw` — his personal OpenClaw AI assistant on AWS)
- Sponsors his own tech community events

---

## Published Writing

| Title | Platform | Date |
|---|---|---|
| The Ideation Engine: How I Used AI to Generate Truly Novel & Feasible Ideas at GEICO | LinkedIn | Nov 19, 2025 |
| From 147 Unread Meeting Notes to a Living Knowledge Base in 30 Days | LinkedIn | Nov 14, 2025 |
| Learning Open Source AI Models On My Morning Commute in Richmond, VA | LinkedIn | Nov 3, 2025 |
| Augment, Don't Automate: How to Stay Valuable While Using AI | LinkedIn | Oct 27, 2025 |
| Streamlining AWS Deployments with Python & Ansible Part I | Capital One Tech Blog | Apr 27, 2021 |
| How We Built A Self-Service API Testing Platform in AWS | Medium (@priorww) | Jan 2018 |
| ACG Cliff Notes: AWS History & 10,000 Foot Overview | Medium (@priorww) | Aug 18, 2018 |

---

## Public Speaking Highlights

| Talk | Venue | Date |
|---|---|---|
| Hacking the Future - Notes from the Front Lines of GenAI @ AWS | AWS User Group Richmond (Ippon HQ) | June 23, 2025 |
| AWS End-to-End Setup & Deep-Dive: Deploying a Website | SlideShare | Oct 2019 |
| Building Killer Tech Teams: Insights from an Engineer | SlideShare | Oct 2019 |
| Agile QA: Redefining Quality in the Wild West | SlideShare | Jan 2018 |
| 12+ original talks | Richmond Cloud Wranglers meetups | Various |

---

## GitHub Projects of Note

- **order-anything-button** — AWS IoT button that triggers ordering from any website
- **qualityCodeDeploy** — QA-friendly CI pipeline demo: GitHub + CircleCI + AWS
- GitHub username: `fordprior` (https://github.com/fordprior)

---

## Analysis

Ford's career is a case study in **social capital as technical leverage**. He didn't have a CS degree, couldn't pass a rigorous technical screen, and didn't follow a traditional path. What he had:

1. **Shameless self-advocacy**: He told the VCU admissions director he was a "buy low" asset. He asked relentless questions in class. He cold-called a family friend for a connection. At SnagaJob, he barely knew the language they were hiring for — and got hired anyway because the team didn't know it either.

2. **Parallel investment in skills**: Every evening during his worst-paying periods, he was learning something. Ruby. AWS. Python. He was always building one layer ahead of where he was.

3. **Community as infrastructure**: The podcast and meetups weren't hobbies — they were deliberate relationship-building at scale. He had 1,000+ members in his cloud meetup. Those were all potential hiring managers, references, or connectors.

4. **Side projects as proof of work**: The Alexa water gauge skill. Blog posts about inner-sourced Ansible modules. Small things that said "I build stuff" to people who needed to believe that about him.

5. **Willingness to be the worst in the room**: He joined "Share Tech" at Capital One knowing he'd be terrible. He bombed for 8 months. He learned a lot. He moved on. He doesn't apologize for it.

The one arc that runs through everything: wanting to feel important. He named it directly at the start — working three part-time jobs simultaneously and still feeling powerless was unbearable. Tech was never about passion for code; it was about having skills that mattered to people who'd pay for them. That motivational clarity probably kept him going when the work was tedious.

---

## Open Questions

- [ ] What did Ford's cloud meetup become? Is it still active in some form post-COVID?
- [ ] What happened to the RVA Tech Talks podcast — is there a permanent archive?
- [ ] What is the current AI strategy at Ford's Amazon team — what tools/models are in use?
- [ ] Does Ford still want to return to Capital One as he mused in the recording?
- [ ] What does Ford want to do after Amazon — another big co, startup, or something different?

## Sources

1. Otter.ai transcript — Ford Prior narrating his tech career (voice recording)

## Appendix

### Key People Named

| Name | Role / Context |
|---|---|
| Bridget Prior | Ford's wife; catalyst for career decision (wanting to start a family) |
| Bill Prior | Ford's father; did VCU IT Management master's program together with Ford |
| Bruce Slough | Family friend; provided connection to Debbie Mills at Magellan |
| Debbie Mills | Magellan Health; connection that led to early QA work |
| Cami Little | Staffing agency recruiter; placed Ford at Acuity and SnagaJob |
| Kate Flannery | Staffing agency recruiter; may have placed Ford at SnagaJob |
| Maureen Carley | VCU IT Management master's program director; admitted Ford without IT background |
| Michelle Lowe | Manager at Acuity; conflict over hours/behavior |
| Rachel Sharma | Magellan teammate; suggested Selenium automation |
| Chris Monger | SnagaJob; hired Ford for their QA org build-out |
| Ron Cartwright (Mark) | Acuity; senior engineer; personal conversations about depression and difficult life |
| Craig / Chuks | CarMax managers who trusted Ford to learn Azure on the job |
| Stanley | Capital One; COBOL developer with desk shrine; peaceful coder |

### Direct Quotes

On why tech:
> "What really drew me to technology was just the feeling of importance... I had spent long enough feeling like I had no skills that people wanted, and it made me feel powerless. It made me feel emasculated even."

On his early work ethic:
> "I would get up at 6am, take an hour-long jog before my Blue Sky Fund shift. Do that 7am to 2pm. Drive home. Nap. At 4:30, due at the law office. Work there until midnight. God damn Charmed is what it was."

On talking his way into VCU:
> "I basically said the same thing I'd said to the grad school admissions person: 'I'm the fucking shit, and you should buy low, and you're about to see me rock it up.' And I asked so many questions, and I didn't give a fuck. I was so goddamn confident, at least, I felt like I was."

On the meetup strategy:
> "Hustling — talking people into liking me — has been a huge part of my tech career progressing."

On current anxiety about Gen AI and job security:
> "Gen AI is taking over and making people like us — code example writers — kind of working us out of jobs. So it's a weird job title. Gen AI writes really good code examples. And so. But now my total comp, because they bumped us up and made us actual software engineers... We are making $324k. That's my story of going from $48 grand to basically almost 10x my salary in like 10 years."

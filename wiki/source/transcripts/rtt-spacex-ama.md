---
page_type: source
source_kind: otter_ai_transcript
title: "Transcript - RTT SpaceX AMA"
ingest_timestamp: "2026-04-29T10:37:35Z"
last_updated: "2026-04-29T10:37:35Z"
source_platform: otter_ai
recorded_date: ""
word_count: 0
domain: ""
subdomain: ""
tags:
  - transcript
  - otter-ai
related_entities: []
related_concepts: []
related_pages: []
---

## Summary

_Awaiting integration. See raw transcript below._

## Raw Transcript
Speaker 1  0:07  
What's up party, people. This is Ford. And welcome back to another episode of RVA tech talks, the podcast where I sit down with the gurus of Richmond tech scene and talk to them about whatever they're interested in. This is kind of a special episode. I'm not actually sitting down with anybody. Well, actually, technically I am. It's my little sister Morgan, and we are reenacting a SpaceX. Ask me anything that happened on Reddit a couple months ago, and basically the SpaceX software team specifically got together, and there's like four, I guess, like maybe six or seven of them actually, and they answered questions from the world about what SpaceX does in terms of software. And their names are as follows. Jeff Dexter is the flight and software cybersecurity dude at SpaceX. Josh Sulkin is the software design lead for the Crew Dragon, which is the space capsule that the people actually were in that was launched a couple months ago. Wendy shimata, which is who is the person who manages the Dragon software team and works out fault tolerance and safety on Dragon. John Dietrich is the lead software development person for demo two. Sophia, Sophia on night, day, I think that's it. Is the lead for the crew displays software for demo two, and Matt Monson, who actually used to work on Dragon, but now leads the Starlink software. And anyway, these folks got together, answered a bunch and bunch of questions, and I reenact those questions, because honestly, this SpaceX, like the Reddit format for asking me anything kind of sucks, and it's really hard to follow. And so I thought, What wouldn't it be great people could just drive in their cars and actually enjoy the Ask me anything without having to actually read through the thread anyway. Without further ado, I give you Morgan prior and Ford Pryor. Morgan's my little sister, like I said, I went to her house and said, Please, can you be like the other person to talk? And she helped me out so you can thank Morgan for that, and Owen and their dog, who all kind of sat there and listened to me talk forever in their living room without further ado, I give you the SpaceX. Ama, all right, let's

Speaker 2  2:19  
go. You just me to be close to the microphone.

Speaker 1  2:24  
Honestly, you can just do it and just pass it me. Just think that's perfect. You want me to go ahead.

Speaker 3  2:31  
I'm in high school. What can I do if I want to get a software job at SpaceX sometime in the future?

Speaker 1  2:38  
The answer comes from Jeff, who says, Get your CS degree or something similar. Spend time to really make sure you know how things work. Engineers who do well at SpaceX are meticulous in their understanding of how their code works, how the network works, how Linux works, how the hardware works, etc. Get real world experience building things and solving hard problems, either through hobby projects or in internships like at SpaceX.

Speaker 3  3:03  
I live nowhere near Hawthorne. Does SpaceX have jobs based on the East Coast? And if not, will SpaceX consider doing so in the future?

Speaker 1  3:11  
And Jeff, once again, says, well, our software engineers are mainly located in Seattle Hawthorne. There's some work from our Texas sites. If you're seriously interested in joining SpaceX, we're always looking for great engineers to reach out. Never hurts to chat and see if we can make it work. And once again, that's Jeff saying that

Speaker 3  3:30  
what is the single craziest, slash most impossible thing management, aka Elon, has asked you to do.

Speaker 1  3:39  
Jeff answers this one once again, and he says, I recall, for the f9 14, I was in Elon's cube playing, telling him the news that there was no way we could get all of the new s1 landing code done in time for the upcoming launch in two weeks. After some thought, he looked over to Lars Blackmore, who was there with us, and asked if we could implement the code, what was our probability of landing? So sorry, and asked if we could implement that code, what was our probability of landing? Lars said around 90% paraphrasing. Elon looked at us and basically said, quote, can you give me 50% end quote. I said, in two weeks, we can definitely get right enough of the logic to get you 50% probability of landing. Exclamation point. We didn't land the f9 14. You can see it on our blooper reel, but we learned a lot from it, and it was instrumental in eventually landing the f9 21 a critical a critical part of our success is our willingness to fail in ways that won't compromise the mission. As long as we are constantly learning from our failures.

Speaker 3  4:42  
You could you possibly tell us about the previous jobs, projects, skills that you've worked on that have helped you get the job at SpaceX, and anything you think is important to work on when landing your first job at a tech company? I.

Speaker 1  5:02  
Uh, Dietrich answers this one, and he says, our team hails from all backgrounds. Seriously, exclamation point. We have noticed particularly good crossover between video game development and what we do. There are a lot of similar math heavy and performance centric problems in the two spaces, but that's by no means a requirement. I've never professionally built games, for example, for getting your first or really any software engineering job. Two big things to focus are on are a, your algorithms and data structures, and B, understanding how a computer works at the lowest levels, even if you're not regularly mucking around in device drivers, the network stack or assembly and understanding how it all fits together will enable you to pick apart. Doing that will enable you to pick apart any problem you come across.

Speaker 3  5:52  
Please name a few open source software used for Falcon slash Dragon, other than Linux kernel and chrominum, chromium.

Speaker 1  6:03  
And the answer comes from Dietrich, who says, das, u boot, build root, M, U, S, l, muscle, and just those three outside of the OS and the crew display software. We don't really use much outside, as much outside software as you might think. We try to keep our programs simple, slim and based on the code we understand throughout

Speaker 3  6:25  
what is the most used programming language for developing the f9 and Dragon software? Is it C or C plus plus?

Speaker 1  6:34  
All of the application level autonomous software is written in C plus plus. And I don't actually know who answered that one, but that was

Speaker 3  6:41  
the answer. What programming paradigm are you using to develop the software for f9 and Dragon, procedural, object oriented, functional or a combination?

Speaker 1  6:50  
And again, I don't know who answered this one, but the answer is, we generally use object oriented programming techniques from C Plus Plus, although we like to keep things as simple as possible.

Speaker 3  7:04  
Are you using any open source software? I'm mostly referring to libraries. If the answer is yes, which one is used the most, or is the most important or relevant? If the answer is no, do you at least think the standard library provided by the language C Plus Plus STL, or is everything implemented in house?

Speaker 1  7:28  
And the answer is, I don't know who's answered this one, once again, I didn't put the answers on all these. But anyway, the answer to this question about open source software and which ones are used, is, we do use open source libraries, primarily the standard C library, plus some others. However, we limit our use of open source libraries to only extremely high quality ones, and often will opt to develop our own libraries when it's feasible, so that we can control the code, control the code quality ourselves.

Speaker 3  7:56  
Is the software composed of small, sometimes independent modules, or is everything integrated in one big module? For example, how tight is the integration of the Crew Dragon GNC module with the module that handles the Crew Dragon environment, pressure, oxygen, level, temperature, etc?

Speaker 1  8:14  
The answer is, the software is definitely composed of multiple small modules, the design of which was one of the main things I worked on. I don't know who answered this one. So sorry. The and the answer goes on. There is a hierarchy to the design, from the low level component to the subsystem to the entire vehicle. Different subsystems, or subsystems are generally isolated from each other, sometimes in the same computer, sometimes across different computers with narrow interfaces between them.

Unknown Speaker  8:45  
Hey, Owen Morgan's helping me with the podcast thing.

Speaker 1  8:50  
She's pretty awesome. Testing, testing, Okay, we're good, right? Which one

Speaker 3  8:57  
did you fit? I think we're here. If you were to delete the entire code base. How much time do you estimate it would take to re implement everything from scratch, having the current team and the accumulated know how? One year, five years, 10 years, do you think the result would be better than the current implementation? And what do you what would you do differently from what you are currently doing?

Speaker 1  9:22  
John, Josh answers this one, and he says, Not sure how long would take for us to rewrite the code base from scratch. We don't plan on deleting it anytime soon.

Speaker 3  9:33  
How do you address technical debt within your organization? Does the constant pressure to deliver that Elon companies are famous for, prevent you from going back and revisiting past designs.

Speaker 1  9:49  
Wendy answers this one, and she says, we're mindful of the outstanding tech debt, and because we're a small team of and because we're a small team, any kind of inefficiency is very prominent. It flight over flight. For many of our vehicles that we fly often, we strive to invest in an operational team to ensure that we can burn down this tech debt and make each subsequent flight as painless as possible. There's always a lot going on, though. So with any decision of how we spend our time, we need to think about the right balance between moving the needle forward in terms of features, and burning down in terms of features and burning down existing debt. So account sounds kind of similar to pretty much everywhere else.

Speaker 3  10:29  
What are your tech stacks? Are they mostly open source or in house frameworks?

Speaker 1  10:35  
And this one was kind of answered elsewhere, but it was I included them all here, and this answer is, we use and sophon answers this one. He says, we use C, C plus plus, and that's for the flight software. And then we use HTML, JavaScript and CSS for displays. And then we use Python for testing, which is interesting.

Speaker 3  10:55  
Do you use rest for any systems? Or have you thought about it?

Speaker 1  10:59  
Wendy answers this one, and she says, Well, we do not currently, though it comes out once in a while in our internal chat rooms.

Unknown Speaker  11:07  
What code editors do you use?

Speaker 1  11:10  
So Fion says, different team members use different editors. I prefer VS code, but I might be just a little biased. It's my face.

Speaker 3  11:20  
What is the longest method name you have in your code base?

Speaker 1  11:25  
Sofian says, I will have to get back to you on that. But overall, code is our craft here, and we make sure it's clean and tidy. I wouldn't expect something too outrageous. Fair warning, we have linters on everything.

Speaker 3  11:39  
Where can I find the code, slash pseudo code for the G fold algorithm, which is falcons, Falcon nine's landing algorithm. I've tried going through Lars, Blackmores, original paper, but as a computer science major student, some terminologies just went over my head,

Speaker 1  11:59  
and the answer, or rather non answer, comes from Josh, who says, unfortunately, I can't go into much detail on the f9 landing algorithms. Linux is only used to run our applications and interface with hardware. All default management and computer redundancy is handled at the application layer and custom software that we've developed ourselves. Time synchronization uses a combination of hardware and software features, some industry standard and some built in house.

Speaker 3  12:26  
What open source libraries does SpaceX team use, if any?

Speaker 1  12:31  
And this was kind of answered elsewhere, but this answer actually is different from the ones answered previously about open source, because so Fion says we use Web Components extensively.

Speaker 3  12:44  
At what level and which web technologies do you use, other than ones mentioned above?

Speaker 1  12:52  
Sofian says we use reactive programming. Sorry, we use a reactive programming library that we developed in house.

Speaker 3  13:01  
What's your software release cycle look like?

Speaker 1  13:07  
And the answer is from Wendy, who says, on Dragon, we cut releases periodically for use when the vehicle is being integrated and tested and run that release through a series of tests and data review. Similarly, we cut a release when we're ready for flight and run the full suite of cases, test cases against specific revisions of our code.

Speaker 3  13:31  
How different is the development experience and the rate of change on production software between the rarely flown dragon and NASA scrutinized, which is assuming Dragon v2 less true of v1 and the BI monthly launched and purely internal Starlink batches.

Speaker 1  13:54  
What does that question mean? I don't know. It sounds like it's saying. What's the difference between the rarely flown. Dragon software and the in the BI monthly launched and purely internal. I have no idea what that question means, but it got an answer, and the answer is as follows, the tools and concepts are the same. Many of the engineers on the team have worked on both projects that being Starlink and Dragon myself included, but being our own customer on Starlink allows us to do things a bit differently. The Starlink software is quite flexible. It takes a ton of software to make it work, and small improvements in the software can have huge impact on the quality of the service we provide and the number of people we can serve, which confuses me, because it just said Starlink didn't have any customers. I might just delete that question.

Speaker 3  14:42  
How often do you work? Nope. How often do you remotely upgrade already flying SATs software

Speaker 1  14:53  
and SATs is satellites there on this kind of project. Pace of innovation is everything we spend a bunch of time making it easier. Safer and faster to update our constellation, we tend to update the software running on all the Starlink satellites about once a week, with a bunch of smaller test deployments happening as well. By the time we launch a batch of satellites, they're usually on a build that all is already older than what's on the rest of the constellation. That's interesting. Our ground services are a big part of the story as well, and they're a huge part of making the system work, and we tend to deploy them a couple times a week or more.

Speaker 3  15:30  
How do you perform error detection and correction during flight?

Speaker 1  15:35  
The answer comes, sorry, the answer is, in terms of error handling, there is a lot of different facets to that radiation induced errors in computers are handled by having multiple redundant computers and voting on their outputs. Errors, errors and sensors can be handled by having multiple different sensors. And errors in data transmission are handled by using error detecting or error correcting codes attached to each payload.

Speaker 3  15:59  
This question is for Jeff Dexter, can you go into some detail into contingency plans during flight, for example, engine failure during ascent, something going wrong during the landing, etc? And the

Speaker 1  16:13  
answer comes from Jeff, and he says, contingency comes in many forms. In our software, as noted, we triplicate almost everything, so that we can tolerate loss of any kind, for example, of a flight computer or sensor or an actuator on Falcon and and any two on Dragon. So they can tolerate a loss of any two of these things on Dragon, and I think, a loss of one on Falcon. So Dragon is better than Falcon Anyway, anyway. At a system level, Falcon and Dragon are designed so that loss of things like engines and thrusters can be tolerated and our algorithms can compensate. We can also add certain contingencies to our state machines. For example, the dragon state machine is designed to autonomously switch from approach to a breakout if certain failures are observed.

Speaker 3  16:59  
I'm sure there are tons of redundant redundancy strategies you guys are implementing. Can you share some

Speaker 1  17:08  
Wendy says? Wendy says, Sure. On Dragon, we have a lot of redundancy on the hardware side, multiple computers, sensors, actuators, etc, but also employ software to handle responses to faults. NASA requirements are such that our vehicle must be too fault tolerant from which means capable of being safely retreating, of being safely retreating from Space Station and or returning home safely for crew vehicles. So we can do both analysis and testing to ensure we meet this fault tolerance. And then another answer from Matt for the same question, says on Starlink. And because, I guess Matt speaks for Starlink, we've designed the system so that satellites will quickly, passively de orbit due to atmospheric drag. In the case of failure, that we fight actively hard. We fight hard to actively de orbit them, if possible, we still have some redundancy inside the vehicle where it's easy and makes sense, but we primarily trust in having system level fault tolerance multiple satellites in view that can serve a user. Launching more satellites is our core competencies. So we generally use that kind of fault tolerance whenever we can, and it allows us to provide even better service most of the time when there aren't problems.

Speaker 3  18:25  
Please give a very high level overview of the control program of Falcon nine and Dragon what kind of communication links used in between Falcon and Dragon nine. I mean dragon and Falcon nine

Speaker 1  18:40  
at a very high level, we have many computers in the vehicle, each built and configured to best suit the task it's assigned. They all run in time secret synchronization with each other, and the flight computer oversees all actions. Almost everything can be expressed as a real time control loop. You read some sensors, you make a decision combination, which is basically a combination of your sensors and the past state, and then issue the outputs of that decision back to the hardware. This time, this happens many times per second, and that answer came from Dietrich.

Speaker 3  19:10  
In your opinion, what's the coolest thing dragon can do with the software inside of it?

Speaker 1  19:16  
This answer comes from Dietrich, and Josh, the first one from Dietrich, though he says, Dragon can dragging. Can do many cool things. It's hard to pick just one, but I think our last two flights have really demonstrated how versatile the vehicle is. It can manage a complicated, delicate, zero G rendezvous with ISS, and it can also fly all by itself to safety in a supersonic Mini G orbit in the thickest parts of the atmosphere. And then Josh says quote, although we hope it's never used with the crew on board. I think the launch escape, escape system is one of the coolest parts of Dragon. I remember when I watched the Pad Abort test live in Cape Canaveral, I was shocked by how fast the vehicle leapt off the pad. And there's YouTube link there. I'm. Um, it was equally amazing to see in the in flight Abort test. Dragon separated smoothly from f9 opening up a large separation distance while f9 exploded underneath. It looked like a sci fi movie, except it was real. And then he adds another, another link there, which I'll definitely be checking out later. Okay, I think we

Speaker 3  20:21  
skipped one. You're right. Does the control software running on Falcon nine, a custom build made for mission Leo, satellite launch, ISS resupply, etc, or is it the same base software with different with a different set of parameters, goals and scripts.

Speaker 1  20:47  
And answer comes from Jeff, who says, we run the same source on Falcon for every mission, though we're still updating that software pretty regularly and usually have new code on each mission. We also have configs for the software that we that are provided from from the other engineering groups that typically change every mission. So conflict changes every mission. These make changes to things like state machines, fault tolerance thresholds, day of launch, wins, etc, so that the software leverages to fly the vehicle

Unknown Speaker  21:16  
that software leverages.

Speaker 3  21:18  
How does a F, T, S, software work,

Speaker 1  21:23  
and that stands for autonomous flight safety system. A F S, S is all about safety, and the software runs on a set of microcontrollers independent from the flight computer. It receives, it receives sensor inputs directly, for example, i am, i, m, u measurements, as well as some computed inputs from the flight computer a mission data load configures the afss for which conditions might require termination of the flight, such as the rocket going way off course, or losing all acceleration, etc. Jeff says that

Speaker 3  21:54  
this question is for Wendy Shimada, how do you calculate LOM, which stands for loss of mission and lo, C, V, loss of crew or vehicle. How do you calculate those numbers for Dragon?

Speaker 1  22:11  
Wendy says, I don't actually know. We have a distinct team in flight reliability whose main job is to calculate these numbers and ensure it's kept up to date given various hardware and CONOPS changes.

Speaker 3  22:26  
How do you make the video streams pretty much real time, without lag?

Speaker 1  22:33  
Dietrich says on the vehicle for Bob and Doug's displays, this is pretty easy for getting it to the ground, like when people like you and I are watching launches, we have some great view great communication links and ground side networking that allows us to get a lot of the data back from the vehicle very quickly. That's not an answer at all. Thanks.

Speaker 3  22:51  
Dietrich, what kind of CPUs does Crew Dragon run in comparison to regular desktop CPUs? I know that there are multiple CPUs for redundancy, but how would one of those units compare to, let's say, a desktop I 990, 900k

Speaker 1  23:15  
Sofian says we use a dedicated quad core processor, similar in power to a five year old phone.

Speaker 3  23:24  
I'm curious about computing hardware. SpaceX is famous for building components in house with Starlink eyeing 10s of 1000s of satellites in Earth orbit. Are there any areas where custom as ICS would be cheaper than c o, t, s solutions. Are there instances of components that are over engineered to the Starlink with under a 10 year lifespan, perhaps for radiation tolerance that could be rebuilt for a significant cost savings.

Speaker 1  24:04  
It's a deep question, over engineered just to Starlink with a roughly less than 10 year lifespan, perhaps of radiation tolerance. I don't It's a complicated question, but the answer is super simple. Matt says. Matt just says, Yes, we do a lot of custom ASIC development work on the starlight project.

Speaker 3  24:27  
Is the rocket landing automated without human control?

Speaker 1  24:30  
Dietrich says, yes, the rocket landing is completely automated.

Speaker 3  24:35  
Do software engineering teams of Falcon slash dragon play any role on the actual launch day.

Speaker 1  24:42  
Dietrich says absolutely, though nominally in it's a support slash double check capacity. We spend a lot of time pouring over data from the live, the live, the live vehicle, before the mission gets started, and we have software folks in mission control throughout all the important phases of flight, just in case something comes. Up, we have a great mission training team that pits our Mission Control Operators against a variety of scenarios and simulations before the flight, and our hope is that the real launch day is a lot more like boring, lot more boring than those simulations. I'm happy to say that for demo two so far, that has been the case you

Speaker 3  25:24  
So how was the software critiqued between the day the weather prevented the launch, which was the 27th and the day of the launch, which was the 30th? Did you do or consider any new deployments? How many days typically before launch? Is your production code considered frozen?

Speaker 1  25:42  
The answer comes from Dietrich, who says the launch that was to be on the 27th on the 27th was a great opportunity for another full up test of everything until nearly t minus zero. So they took it all the way to T minus zero and then stopped. They got test everything up to that point, we'd done a similar thing the previous weekend, but it's always good to have more data. We spent the intervening few days checking and rechecking everything that we learned from that almost launch on the 27th but we ultimately didn't change anything. We started aggressively stabilizing the code around the beginning of the year, so like six months ago, and it's been more or less locked down for the past several months.

Speaker 3  26:25  
Dietrich, does SpaceX use AI in any of its software?

Speaker 1  26:31  
Dragon does not use any AI. Says, Dietrich, do you

Unknown Speaker  26:35  
use any machine learning techniques?

Speaker 1  26:37  
Dragon and Falcon do not use any machine learning tech. But that's not to say things like this aren't not in space X's future. And Dietrich answered that as well.

Speaker 3  26:47  
How important is latency for various software components in Dragon? Does every action have to be instantaneous? Or is there some wiggle room?

Speaker 1  26:57  
Wendy says, great question. This is very important, and maintaining a fault tolerant computing system relies on ensuring correct timing between all the flight computers for slower responding subsystems like life support or thermal control, the response timing has a little more slack on the order of seconds, depending on what fault we take.

Unknown Speaker  27:16  
What is your Linux distro?

Speaker 1  27:20  
Distro we don't use any off the shelf distro. We'd have our own. Says Dietrich,

Speaker 3  27:27  
as far as we know now, your rockets run on Linux. Which but which mainstream distribution is closest to your kernel?

Speaker 1  27:40  
He says, Yes, we run Linux with the preempt RT patch applied in order to get better real time performance. We don't use any third party distro, but maintain our own copy of the kernel and associated tools. We've made small changes to the kernel over the years, although it's mostly unmodified, the only exception to that is the addition of several custom drivers to the interface within our software, within our hardware. Sorry, we use a variety of hardware architectures, and I can't go into much detail other than that to say it's a distributed system made up of many individual computers.

Speaker 3  28:15  
I know. SpaceX mostly uses standard, off the shelf CPUs for its flight systems with modified Linux distro is the redundant computing managed by the Linux kernel itself or by the C Plus Plus application running in the Linux environment, if possible. Can you explain the practices involved in implementing hardware level lockstep computing.

Speaker 1  28:46  
There is no answer to that question. Sorry if you get you really excited.

Speaker 3  28:51  
And most importantly, do you play KSP?

Speaker 1  28:56  
KSP stands for Kerberos, Space Program or something, and which is like a flight simulator. And Sofian says, of course, we play KSP. Smiley face.

Speaker 3  29:07  
Did you ever consider adding some games to Dragon?

Speaker 1  29:11  
And Sofian says, we don't have any yet, but I can see this happening in the future. Vote for your favorite game. Exclamation point.

Speaker 3  29:18  
What level of rigor is being put into Starlink security. How can we as normal citizens become comfortable with the idea of a private company find 1000s of internet satellites in a way that's safe enough for them not to be remote controlled by a bad actor? This has potential multi generation impacts if your team gets this wrong. So it would be awesome if you could speak publicly about the strategy.

Speaker 1  29:48  
And the answer comes from Matt who says, in general, with security, there are many layers to this. For starters, we designed the system to use end to end encryption for our users data to make breaking into. A satellite or gateway less useful to an attacker who wants to intercept communications. Every piece of hardware, hardware in our system, like satellites, gateways, user terminals, is designed to only run software signed by us, so that even if an actor breaks in, they won't be able to gain a permanent foothold. And then we harden the insides of the system, including services in our data centers, to make it harder for an exploitive vulnerability in one area to be leveraged somewhere else. We're continuing to work hard to ensure our overall system is properly hardened and still have a lot of work ahead of us where we are hiring. Exclamation point, but it's something that we take very seriously.

Speaker 3  30:40  
Is this question for Jeff? This question is for Jeff. What does cybersecurity look like for you guys? I imagine you're constantly under attack from state, nation, slash, apts, et cetera, to steal confidential IP. Do you have to follow any regulations relating to ITAR in this regard, or is that more high level than what you deem proportionate?

Speaker 1  31:12  
Answer comes from Jeff who says, We have a lot of traditional cyber a lot of the traditional cyber security you'd expect, protecting our corporate networks, monitoring for threats inside and outside the networks, phishing campaigns, etc. We also need to analyze potential attacks against our vehicles, especially around the command paths within the pedigree of the code that ends up in the vehicles. We have a dedicated team that identifies how our vehicles and satellites could possibly be hacked so that we can eliminate or pro prohibit these sorts of threats. When we're building our vehicles, we also take full advantage of the static and dynamic analysis of our code. ITAR mostly limits what we can share. Sorry, ahead of time, if we can't answer all your questions, we're looking forward to get a bug bounty system up shortly.

Speaker 3  32:01  
What does the development cycle for flight simulators look like for the Falcon system say? How frequently are they updated based on telemetry? What's the hardest part of the launch cycle to model

Unknown Speaker  32:18  
this answer comes from

Speaker 1  32:21  
probably Jeff, but it doesn't say for Starlink, we we need to think of our satellites more like servers in a data center than like a special one of a kind vehicle. They are awesome things that we need to be absolutely sure of, like commanding, software update, power, hardware safety, and therefore deserve to have specific test cases around. But there's also a lot of things that we can be a little more flexible about. For example, sorry for these things. We can take an approach that's more similar to the way that, like a web service is deployed. We can deploy a test build to a small subset of our vehicles and then compare how it performs against the rest of the fleet. So kind of like a carried Canary deployment, if it doesn't do what we want, we can tweak it and try again before merging it. If we see a problem when rolling out, we can pause, roll back, and try again. This is a hugely powerful change in how we think about space vehicles, and absolutely critical to being able to iterate quickly on our systems.

Speaker 3  33:19  
Was the docking simulator developed by the crew displays software team itself, or was it a separate project?

Speaker 1  33:27  
Jeff says the docking simulator is completely separate code from what's actually in the crew displays though. It was developed by our crew displays team. It started out as a fun project from Shane milkey and Mike westenhaver Before we decided to finish it up and put it on the web before demo two.

Speaker 3  33:49  
SpaceX is known for its hardware in the loop testing what fraction of SWE person hours go into developing these systems

Speaker 1  34:02  
when making changes, we expect our engineers to think critically and question each other about functional testing, like, for example, how do I know that my change works? And regression testing, which is like, how do I know if I broke something else, or if this breaks in the future? Building test cases we can run on the ground is a great way to answer these questions, and we do a lot of that, but it's not the only way, and that's where he leaves it.

Speaker 3  34:26  
With a few 100 Starlink satellites in orbit. Are there parts of individual or constellation operation that you've come to realize are not well covered in testing?

Speaker 1  34:36  
We've definitely found places in our code where test cases had holes, having hundreds of satellites in space, 24/7 will find edge cases in every system, and will mean that you see the crazy edges of the bell curve. The important thing is to be confident about the core that keeps the hardware safe tells you about the problem and gives you time to recover. We've had many instances where a satellite on. Orbit had a failure we'd never, ever conceived of before, but was able to keep itself safe long enough for us to debug it, figure out a fix or a workaround and push the software to that satellite for an update.

Speaker 2  35:13  
You do this one, skip it. This one, there's no answer.

Speaker 3  35:20  
Okay. Do you track performance of your code? I'd imagine it's a critical design parameter for an ebbed software system with critical timing constraints like yours. So I'm wondering how your approach compares to something like the video game industry, where such a practice is common, but likely not as rigorous as what would be required for space flight.

Speaker 1  35:44  
And Wendy says, Yeah, we do have performance tracking of our code. We use a continuous integration system such that our code is always being tested, but we also analyze this data real time to ensure our performance metrics are within expected bounds. The cases are set up such that if we violate any key performance indicators, the case quote, unquote, fails, and an engineer takes a look,

Unknown Speaker  36:07  
how do you test your software?

Speaker 1  36:09  
Dietrich says every way we can think of unit test, containerized integration tests, you can run these on your own machine with a full physics simulation and full up H, I, T, L or hardware in the loop, tests on real flight hardware, again with full simulation. Mating the flight software up against the simulator is the most powerful tool that we have for testing, especially when it's run on the real hardware, we can simulate an entire mission and even many detailed fault scenarios with the vehicle hardware just sitting on a table in the lab.

Speaker 3  36:44  
How do you test your code before deploying it in deploying it to flight hardware?

Speaker 1  36:51  
Wendy says, for each vehicle, we have hardware in the loop simulator, all flight critical hardware, plus simulated physics and sensing. That's the whole that's the term hardware in the loop. It's like a full simulator with hardware physics sensing. Anyway. So Wendy says that for each vehicle, we have that simulator that we run a huge suite of tests on before ever deploying it to a production vehicle or in flight. We anytime that we take a new software change, which happens frequently for development vehicles, we ensure we run through both unit tests for the code functional tests to ensure the software works as intended and system level testing for mission phases, for both nominal and off nominal cases,

Speaker 3  37:36  
what are the strangest bugs that you ran into while developing and testing the software for Crew Dragon

Speaker 1  37:45  
answer here comes from Dietrich, who says, I can't go into much detail on specific problems, but kernel bugs are definitely the most quote, unquote, fun and memorable. Most of our software, our control software, is single threaded to avoid the non determinism that synchronization issues can introduce. But there are a lot of there are, of course, a lot of things that happen on the OS at any given time. We've gone to a lot of effort to turn Linux into a dependable platform for real time control that has as much a high that has a much higher degree of determinism than you'd see on your desktop OS, as mentioned elsewhere, we use the config, preempt, RT patch, which is a huge help. But even still, in earlier development, we sometimes catch the system not performing as real time as we'd like to, and digging into those problems is always an adventure.

Speaker 3  38:35  
What are some of the most interesting edge cases that you've had to take into account when writing the software for Crew Dragon.

Speaker 1  38:42  
This one's hard to answer without going into too much detail, but anything having to do with rebooting one of our computers in flight is definitely interesting. Reboots are completely expected and supported due to radiation concerns, and they're one of the most insert, one of the more interesting scenarios that we have to design for the Dietrich says that, but Wendy also answers as follows, some of the more interesting systems cases, some of the most some of the more interesting system cases, too, are faults or failures that require responses in multiple subsystems, spanning computing, RF, comms, life support and propulsion. A great example of this is handling a launch escape or a cabin fire, the vehicle goes through a lot of reconfiguration really quickly, which requires many of our code components to coordinate with each other.

Speaker 3  39:30  
How does the UI or what does the UI development process look like, and how is the UI tested?

Speaker 1  39:37  
Sofian says we follow Agile processes and have a high bar for unit testing coverage and also high bar for integration tests that run with and without flight hardware. We also take a lot of pride in manually verifying and documenting our new features to make sure they work as intended and that we have no regression.

Speaker 3  39:57  
It's known that Crew Dragon displays are. Name chromium and JS, are you using a reactive library? And if so, is that developed in house, or is an existing library slash framework?

Speaker 1  40:13  
Sofian says, Yes, we use chromium and we do use a reactive library, but we develop that reactive library in house.

Speaker 3  40:21  
In some shots of Mission Control, I noticed UI very similar to this, to the displays in Crew Dragon. Can the exact same crew display software be served from a server on the ground, feeding off of live telemetry from Dragon while in flight. If so can or will this software be used to monitor cargo dragon as well on future flights.

Speaker 1  40:48  
Jeff says we can and do run the exact same code that's on the crew displays on the ground. The only limitation is that we don't necessarily get all the same telemetry that we have in the cockpit on the ground. Due to the limitations in our RF budget. We could also, or sorry, we could, we could, but we generalize, generalize prioritizing. We generalize, prioritize getting other critical telemetry instead. Yeah, generally prioritize getting other critical telemetry instead. And Jeff says that,

Speaker 3  41:22  
is there any chance of getting high resolution screenshots off the crew displays? It's hands down the prettiest UI I have ever seen in aerospace.

Speaker 1  41:31  
I don't know about that. We definitely want to share some high res screenshots of the crew displays. We'll see if we can get this approved so we can show you what Bob and Doug were able to see up close. That's from Jeff.

Speaker 3  41:43  
One question regarding Starlink, how did creating the crew display software affect the development of the Starlink interface for the Space X operations like map views and data visualizations,

Speaker 1  41:59  
the tech from the crew displays, especially the map and the alerts, formed the basis of our UI for the first couple Starlink satellites, 1010, it's grown a lot since then, but it was awesome to see Bob and Doug using something that somehow felt familiar to us to also Matt says that

Speaker 3  42:17  
this Question is for Josh Sulkin, did the software design team take feedback from Bob and Doug during training?

Speaker 1  42:25  
And Josh says yes, the entire software team took feedback from Bob and Doug on all aspects of the software while they were primarily focused on the displays, button panels, audio system. Bob and Doug were also very interested, interested in how the software as a whole worked, especially like back, things like backup capabilities that might be necessary in emergencies, their feedback was invaluable in making the system better.

Unknown Speaker  42:50  
What type of display technology does dragon use?

Speaker 1  42:55  
Dragon uses some computer vision, though, just for navigation.

Speaker 3  43:01  
When do you expect laser links to be a thing on Starlink satellites?

Speaker 1  43:09  
I think actually one of the answers to the previous questions about display technology. So Fiona answered that as well, and said, LCD. When do you expect better laser links to be a thing on Starlink? I don't know. I That one got kind of garbled, but we're still in the same area of UI, so we're just going to next, okay,

Speaker 3  43:29  
could you talk about how Crew Dragon touch screens, Oh, could you talk about how Crew Dragon touch screens used chromium, and what challenges that created, what fault tolerant measures were taken when such a large underlying code base powers it, and what efforts went into rad hardening? Was this a good choice in hindsight, and will the same web based approach go into starship in the future, what was the user experience process like with design and user testing?

Unknown Speaker  44:09  
And the answer is, the use

Speaker 1  44:12  
of chromium and JavaScript in mission critical environments is a popular question. In order for me to answer the question, clearly, we have to understand that chromium in this context is used as a UI rendering engine only the flight software interaction layer with the displays and the fault tolerant. And the fault tolerant is well defined and resides outside of the system displays boundary. That said, we follow the same development process for all Vehicle Code, regardless of the technology stack. We cross train our developers to write vehicle code in C plus plus and then carry the same mentality towards writing reliable software. We take reliability and performance very, very seriously, and just like other vehicle software, we test extensively under different conditions to understand all failure modes, we have alerts and procedures in place to act on those failures in case we encounter them. And all of that added to hundreds and hundreds of hours of simulations that we run on flight hardware to train the crew.

Speaker 3  45:15  
I'm a front end web developer slash UX designer slash graphics programmer slash 3d artist slash graphic designer, straddling the design and engineering disciplines, and it's been my dream to work for SpaceX when I graduate this August crew designs user interface has been right down my alley. Although current SpaceX job listings are mostly for embedded systems, how can I find the right graphical software project to apply to. I've had some contacts at SpaceX, but are there any fitting teams or projects I could ask and send my resume to them, in particular, graphical simulations for starship something customer facing with Starlink? The answer is,

Speaker 1  46:09  
while we, while we face many challenges in law along the way, we are very, very happy with our displays. And most importantly, our two customers are happy as well. Starship ground software is already using the crew displays tech stack, and it won't be too long before we start designing human interfaces for starship for Mars. We sure be sure to apply exclamation point. You'll notice a certain you'll notice you'll also notice in certain images too, that we are still that there still exists some hardware buttons in the capsule right below the displays. This is also to ensure that, in case the displays are unusable for whatever reason, the astronauts can still use the hardware buttons to initiate critical actions, such as responding to a fire in the cabin.

Speaker 3  46:56  
Are you using Tesla hardware slash touchscreens on the Crew Dragon. No, our hardware

Unknown Speaker  47:03  
is not the same one that Tesla has.

Speaker 3  47:05  
There were rumors about crude dragon UI running on Chromium wrapped in Qt. Is that true? If so, why did you go with Rev web tech instead of straight up native slash Qt UI,

Speaker 1  47:23  
that's correct. We do use chromium as the rendering engine for the displays UI. This project started as a simulator prototype to showcase the design vision to NASA. We then attempted to run it on a flight hardware with flight on flight hardware, the hardware with modifications. And it actually worked pretty well. We gained more confidence in that stack as we developed the prototype, and then we designed the flight software around it. With that in mind, we liked all the modern features that come with that comes in, with browsers, browsers out of the box. We also liked having access to the talent that is already trained in that stack. Perhaps we are not afraid of doing things slightly differently here at SpaceX, we like taking first principles approach to problem solving, as opposed to just relying on industry standards, and that was from Sofian.

Speaker 3  48:09  
What's your front in tech stack for the display,

Speaker 1  48:12  
HTML, JavaScript, CSS, and we also use Web Components heavily.

Speaker 3  48:17  
How are Doug and Bob to work with? Did they ever make any particular suggestion which spiraled into a major change in Crew Dragon over time?

Speaker 1  48:27  
And this one answer comes from Sofian, who says Bob and Doug have been working closely with the SpaceX team since the start of the program. They have spent a lot of time in Hawthorne with the teams designing the vehicle. They bought a broader wealth of experience that spans multiple shuttle flights, and they were generous in sharing that experience that said, and to their credit, they came in with a clean slate and with the will to accept that many things are done differently in this vehicle. We all see them now in their fancy spacesuits or doing space flips, doing flips in space, but those guys put a ton of hours flying in and out of Hawthorne, spending spending time away from their family, training while providing feedback, all with a smile and without a complaint. Their work ethic is truly inspirational, and that's what makes them do the things that they do.

Speaker 1  49:21  
Oh, then Sophia continues. We cannot wait to debrief them in Hawthorne when they get back from their trip, sure they will have plenty of feedback for us, especially Bob, he always does.

Speaker 3  49:37  
How was the UI designed? Did you follow any specific design principles. How did you take into account the specific conditions of space flight, like vibration, helmet, limiting visibility, etc?

Speaker 1  49:50  
The answer is, we followed a human centered design process, starting by defining the main guiding principles that closely follow the vision of Dragon being a. 21st Century fully autonomous spacecraft. One example is identifying minimum crew interaction as a success criteria, like, for example, don't press the button. Paradigm, we believe that presenting information well means minimizing the required interaction it takes to monitor and control the vehicle. Overall, we based the design around a detailed understanding of crew tasks, capabilities, situational awareness, needs and environmental conditions throughout the flight, which allowed us to focus on clarity, simplicity and removing clutter our developer, developer, developer, slash pilot. Mike Westen haver developed a tool that allowed us to allowed us to map crew tasks to display features and functions, allowing us to fully track requirements and how they are implemented in our software.

Speaker 3  50:50  
How did you test the UI and specifically touch interaction with gloves as

Speaker 1  50:56  
part of our testing and qualification, we do test for vibration and visibility conditions under different seat configurations, different seat configurations. The crew did many suited simulations, interacting with displays while wearing gloves.

Unknown Speaker  51:13  
What are some cases of JavaScript

Speaker 1  51:16  
and less the crew displays on board dragon runs Chromium with HTML, JavaScript and CSS. We actually don't use less at all. Says Sofian.

Speaker 3  51:27  
What's the amount of telemetry in gigabytes that you usually get from Falcon dragon? Starlink. Do you run some machine learning slash data analysis tools on it.

Speaker 1  51:45  
The answer is for Dragon, the telemetry data is in the hundreds of gigabytes for a typical mission, and we do a fair amount of data review after every flight to ensure we understand if the system behaved as we intended. That answer came from Wendy, and then Matt says, For Starlink, we are currently generating more than five terabytes a day of data. We're actively reducing the amount of each the amount each device sends, but we're also rapidly scaling up the number of satellites and users in the system. So as far as analysis goes, doing, the detection of problems on board is one of the best ways to reduce the amount of telemetry we need to send back to and store like, for example, analyze it and only send back stuff that's interesting. The alerting system we use for this is shared between dragon and Starlink.

Unknown Speaker  52:34  
That answer came from Matt.

Speaker 3  52:36  
Are there any fancy changes you made that you could actually tell us about

Speaker 1  52:42  
for some level of scope on Starlink, each launch of 60 satellites contains more than 4000 Linux computers. The constellation has more than 30,000 Linux nodes and more than 6000 microcontrollers in space right now. And because we share a lot of our Linux platform and infrastructure with Falcon and Dragon, they get the benefit of more than 180 vehicle years of on orbit test time.

Unknown Speaker  53:07  
Our Starlink stat

Speaker 3  53:10  
are Starlink sets programmed to de orbit themselves, in case they aren't able to communicate back for a given amount of time,

Unknown Speaker  53:21  
like antenna damage on an otherwise healthy set.

Unknown Speaker  53:29  
And the answer is a little

Speaker 1  53:33  
confusing, but as follows and about and about de orbit, the satellites are programmed to go into a high drag state if they haven't heard from the ground in a long time, this lets atmospheric Drag pull them down in a very predictable way. You Thank.

Transcribed by https://otter.ai

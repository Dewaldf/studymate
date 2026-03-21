# BUSINESS PLAN
## StudyMate AI
### The personal AI tutor for every secondary school student
**United Kingdom · South Africa**
*Understand · Build · Progress · Belong*

---

| £2B+ | 600K | 900K | Daily |
|---|---|---|---|
| UK Tutoring Market — Annual spend | GCSE Students / year — England alone | SA Matric Cohort — Largest in history (2025) | Engagement Model — Check-in after every school day |

---

## 1. Executive Summary

StudyMate AI is a personal AI tutor for GCSE students in England and Wales, and Matric students in South Africa. The product is built around a fundamental inequality: in a classroom of thirty students, a teacher can only explain a concept one way, at one speed, at one level. Students who do not understand in that moment are left behind. Private tutors — at £40 per hour — are the only solution available, and they are unaffordable for most families.

StudyMate AI closes that gap. It is the personal tutor that every student deserves: one that meets each learner where they are, explains concepts from first principles if needed, adapts its teaching to how that individual understands, and then scaffolds them step by step up to the level expected by their exam board. The daily check-in and five-question quiz are the entry point — they diagnose where the student is. What follows is the real product: an adaptive tutoring loop that ensures genuine understanding before moving on.

The MVP is delivered as a **native Android mobile application**, built with Flutter. The MVP covers text and image-based explanations. Audio and video follow in later phases.

The founder has direct personal insight into the problem through a daughter currently sitting GCSEs, technical capability to build the product in Flutter, C#, and .NET Core, and existing personal connections in South Africa that provide a faster adoption pathway there than any competitor could replicate.

**The core product insight**

Every student in the world understands things differently. Some need an analogy. Some need a diagram. Some need to be taken back to first principles before the current topic makes sense. A human tutor adapts instinctively to this — they notice the blank look, they try a different explanation, they check understanding before moving on. No classroom teacher with thirty students can do this. StudyMate AI can. It does not stop until the student genuinely understands, and it remembers how each student learns so it gets better at teaching them over time.

---

## 2. The Problem

### 2.1 The understanding gap

GCSE and Matric students sit high-stakes examinations that shape their academic futures. The period between each lesson and the eventual exam is largely unsupported. Students attend class, go home, and have no reliable way to know whether they have truly understood what was taught — and no one to ask if they have not.

The most common evening revision methods — re-reading notes, watching YouTube, or skimming a revision guide — are passive. They feel productive without creating lasting understanding. Small misunderstandings compound over weeks and months into genuine gaps, which only become visible when it is too late to address them effectively.

The root cause is structural: the average UK secondary school classroom has 30 students and one teacher. When a student does not understand something, the lesson moves on anyway. The teacher cannot stop the class of 30 to re-explain a concept to one student using a different approach. The student who needed a simpler analogy, a diagram, or to revisit a prerequisite concept is left behind — not because they cannot learn, but because the teaching model cannot adapt to them.

- **Growing need:** 29% of secondary school students in England have had private tutoring, rising to 45% in London — proof that the gap is real and families are willing to pay to close it
- **Cost barrier:** Human tutors cost an average of £40 per hour — effective, personalised support is unaffordable for most families at daily frequency
- **AI gap:** Existing AI tools require students to self-direct the interaction — a skill that struggling students do not have and motivated students do not need reminding to use
- **The missing product:** No current product diagnoses where a student's understanding breaks down, then teaches the concept from the right starting point for that individual student, in a way that student can actually follow

### 2.2 The parent visibility problem

Parents who care about their child's education have almost no timely signal on whether their child is keeping up. School reports arrive twice a year. Parents' evenings last ten minutes per teacher. Parents are investing worry, time, and often money into GCSE preparation with no feedback loop shorter than a school term.

StudyMate gives parents a clear, regular picture of where their child genuinely understands the curriculum and where gaps are forming — not just quiz scores, but the progression story: where the student started and how far they have come.

### 2.3 The teacher's blind spot

Teachers who want to support individual students have no scalable way to know which students in a class of 30 have understood today's lesson and which have not. StudyMate's future teacher module addresses this — giving teachers class-level visibility so they can focus their limited time where it is most needed. This is Phase 2, but the data architecture is designed for it from the start.

---

## 3. Product

### 3.1 The daily check-in loop — the entry point

The daily after-school check-in is where the product begins. It takes five to eight minutes and establishes the habit that makes everything else possible.

| Stage | What happens |
|---|---|
| Step 1 | **Student opens the app** — Each evening after school, triggered by a native push notification at a time the student sets during onboarding. |
| Step 2 | **Reports today's subjects** — Student taps which subjects they had today. Pre-populated from their uploaded timetable if available, or entered manually in under ten seconds. |
| Step 3 | **Specifies what was covered** — For each subject, the agent asks: "What did you cover in Maths today?" The student responds in their own words — a sentence is enough. |
| Step 4 | **Diagnostic quiz** — The agent generates five targeted questions based on what the student reported was taught, calibrated to their current mastery level on that topic. |
| Step 5 | **The tutoring loop begins** — Quiz results reveal where the student's understanding breaks down. The real product starts here. |

### 3.2 The adaptive tutoring loop — the core product

The five-question quiz is a diagnostic tool, not the destination. Its job is to reveal the shape of the student's understanding: what they have grasped, what they have partially grasped, and where their understanding breaks down entirely. Once the quiz reveals a gap, the adaptive tutoring loop begins.

**Step 1: Socratic diagnosis**

The AI does not immediately launch into an explanation. Instead, it asks the student to explain their reasoning — Socratic method, not multiple choice. "You got that question wrong — can you tell me how you were thinking about it?" This serves two purposes: it gives the AI a precise picture of where the student's mental model is incorrect (not just that it is incorrect), and it requires the student to articulate their thinking, which is itself a powerful learning mechanism.

The diagnosis is conversational. The AI asks follow-up questions until it understands exactly where the student's understanding breaks down — which concept is missing, which prerequisite has not been internalised, which step in the reasoning chain fails.

**Step 2: Explain at the right starting level**

Once the gap is located, the AI begins explaining from a level below where the student's understanding currently sits. If a student cannot explain why a quadratic equation has two solutions, the AI does not start with the quadratic formula — it starts with what a function is, what roots mean graphically, and builds from there.

The language and framing of the explanation is calibrated to be simple first — "explain like I'm 5" — and then progressively more rigorous as the student demonstrates understanding. The AI uses text and images (MVP), and later audio and video (Phase 2+), to find the framing that works for this particular student.

**Step 3: Check understanding, adjust, repeat**

After each explanatory step, the AI checks whether the student has understood before moving on. This is not another formal quiz — it is a natural conversational check: "Does that make sense? Can you give me an example of that in your own words?" If the student cannot, the AI tries a different explanation — a different analogy, a different diagram, a different angle. It does not repeat the same explanation louder.

**Step 4: Scaffold up to curriculum level**

Once the foundational concept is genuinely understood, the AI progressively builds the explanation up toward the level expected by the student's exam board. It is explicit about this progression — "You've got the basic idea. Now let's look at how your GCSE syllabus expects you to apply this." The gap between "understanding the concept simply" and "answering an exam question correctly" is itself a teaching goal.

**Step 5: Confirm and record**

When the student can correctly answer an exam-style question on the topic — with reasoning, not just the right answer — the session is complete. The mastery map updates. The progression is recorded and surfaced to the student in an encouraging way.

**Disengagement fallback**

The Socratic loop assumes a willing participant — but the typical user is a tired 15-year-old after a full school day. If the student gives two consecutive low-effort responses ("idk", single words, or clearly random input), the AI gracefully shortens the session: it provides a clear, simple explanation and one follow-up check instead of the full Socratic cycle. The session is logged as "incomplete understanding" in the mastery map — the student still gets streak credit for showing up, but the topic is flagged for revisiting in a future session. This protects the daily habit from being killed by an overly demanding tutoring loop on days when the student is not fully engaged.

**"Flag this explanation" button**

Every AI explanation includes a simple "Flag this explanation" button. Students or parents can tap it to report content they believe is incorrect, confusing, or unhelpful. Flagged explanations are logged for review and feed into the content quality monitoring pipeline. At seed phase, flags are reviewed manually by the founder. At scale, an automated review workflow prioritises flags by frequency and topic. This is a low-cost MVP feature that provides structured feedback on content accuracy from day one.

**Why Socratic questioning, not blunt correction**

Telling a student they are wrong and giving them the right answer is the least effective form of feedback for long-term retention. It produces the correct answer in the moment and nothing else. Socratic questioning — prompting the student to articulate their reasoning, identify where it fails, and reconstruct the correct understanding — produces durable learning. It is also kinder: students who feel like they arrived at understanding themselves, rather than having it handed to them, build genuine confidence.

### 3.3 The silent learner profile

StudyMate learns how each student learns best, but it does not ask them. Self-reported learning style preferences (e.g. "I'm a visual learner") are not reliably predictive of learning outcomes — the research on this is clear. Instead, the AI observes behaviour and outcomes over time:

- Which types of explanation correlate with faster understanding for this student?
- Does this student respond better to analogies or to step-by-step logical derivations?
- Does visual scaffolding (diagrams, worked examples) help, or does it distract?
- Which subjects require more foundational re-grounding, and which can the student meet at curriculum level directly?

This profile is built silently in the background and is never exposed to the student as a label. It simply makes the tutoring better over time — the AI gets faster at finding the right starting point and the right framing for this individual.

**Parent notes (optional, non-MVP)**

Parents who know something meaningful about how their child learns — a diagnosed learning difference, a known anxiety around a particular subject, a preferred explanation style from a previous tutor — can add optional notes to the student profile. These notes inform the AI's initial approach before enough behavioural data has accumulated. This is a post-MVP feature, but the data model accommodates it from the start.

### 3.4 Curriculum alignment — knowing the expected level

The tutoring loop's goal is to bring the student to the level expected by their exam board. This requires the app to know what that level is.

**Exam board selection**

During onboarding, students or parents select their exam board. For UK students: AQA, Edexcel, or OCR. For South African students: DBE or IEB. This determines the curriculum framework against which all explanations and assessment are calibrated.

**Students who don't know their exam board**

If a student does not know their exam board during onboarding, the app prompts them to ask their teacher or parent. The exam board can be updated at any time in settings. School-name-to-exam-board inference is a potential future feature once sufficient user data has been accumulated to crowdsource reliable mappings — but at MVP, a simple prompt is more reliable than an inference that could silently teach to the wrong specification.

**Curriculum depth**

The AI has knowledge of what each exam board expects students to be able to do on each topic — not just the fact list, but the level of reasoning, the style of question, and the common misconceptions examiners report. The tutoring loop's endpoint is not "student understands the concept" in the abstract — it is "student can handle what the exam board will actually ask."

### 3.5 Progression visibility — encouraging, explicit, shared

When a student completes a tutoring session having genuinely understood something they did not understand before, the app makes that progression visible and celebrates it. This is not a score — it is a story: "You started today not being sure what a covalent bond was. You now understand it well enough to explain it and apply it to an unfamiliar example. That is real progress."

**Why explicit progression matters**

The research on self-efficacy — a student's belief in their own ability to succeed — shows it is one of the strongest predictors of academic persistence. Students who feel competent engage more deeply and do not give up when the material gets hard. Making the journey from confusion to understanding explicit and visible is one of the most important things an educational tool can do. It is the difference between a student thinking "I'm bad at Chemistry" and thinking "I didn't understand this thing, and now I do."

**Parent visibility**

Parents can see their child's progression in the parent dashboard — not just quiz scores, but the arc: where the student started on each topic, where they are now, and the direction of travel. The weekly digest frames this in plain, encouraging language. Parents do not need to understand the curriculum to find this useful.

**Teacher visibility (Phase 2)**

Once the teacher module is built, class-level progression data is available to teachers — aggregated and anonymised at class level by default, with individual student data available to the student's own teachers. A teacher who can see that 60% of their Year 10 class did not grasp last Tuesday's lesson on covalent bonding can plan Thursday's lesson accordingly. This creates a virtuous loop: StudyMate supports students, and the data from that support helps teachers focus their classroom time more effectively.

### 3.6 Multimodal content — phased delivery

The tutoring loop can use multiple modalities to explain concepts. The MVP prioritises the modalities that are buildable at high quality immediately:

| Modality | Phase | Rationale |
|---|---|---|
| Text | MVP | Highest quality AI generation. Socratic dialogue, explanations, examples, and analogies are all text-native. |
| Images | MVP | Diagrams, worked examples, and visual scaffolding significantly improve comprehension for many students. Static images can be generated or curated for common topics. |
| Audio narration | Phase 2 | Text-to-speech narration of explanations. Valuable for auditory learners and students who are tired of reading. TTS quality via leading providers is now production-grade. |
| Explanatory video | Phase 3+ | Short generated videos explaining concepts simply. Significant cost and complexity — the value is real, but this is not an MVP or Phase 2 decision. |

### 3.7 Timetable upload

During onboarding, students can upload their school timetable — a photo, a PDF, or simple text entry. The app parses this to know which subjects occur on which days. The check-in experience then requires zero effort to start: the app already knows it is a Tuesday and that means Maths, English, and Biology.

For students who do not upload a timetable, manual subject selection takes under ten seconds.

### 3.8 Gamification — badges, streaks, and confidence

Gamification is built into the core loop from day one. Badges and streaks reinforce the habit and make progress visible in a way that feels earned.

**Subject mastery badges**

Each subject has a badge progression with five tiers: Beginner, Developing, Confident, Strong, and Expert. Badge tier is determined by the student's rolling accuracy score on that subject across both quiz performance and tutoring session outcomes. Topic badges within each subject allow granular visibility — a student can be Expert in Algebra and Beginner in Probability within the same Maths subject.

**Streaks**

A daily streak counter tracks consecutive days with completed check-ins. Streak milestones (7 days, 30 days, 100 days) trigger parent notifications and in-app celebrations. On paid plans, one missed day per month is forgiven — the streak mechanic motivates without punishing.

**No public failure states**

The gamification layer is designed to build confidence, not create anxiety. There are no public leaderboards in the MVP. Badges are earned, not taken away. The app does not surface a student's lowest scores prominently. The progression narrative is always framed as forward movement, even when a session reveals a significant gap.

**Leaderboards and friend challenges (Phase 2)**

Once a sufficient user base exists, optional friend connections and quiz battles become available. The mastery data architecture supports this from day one.

### 3.9 AI agent architecture

Each student's session is handled by an AI agent built on the Anthropic Claude API. The agent assembles a personalised context at the start of every session:

- **Profile:** Year group, exam board, subject selections, target grades, and the silently accumulated learner profile (which explanation approaches have worked for this student, which modalities they engage with, which topics have required foundational re-grounding)
- **Mastery map:** Accuracy score and understanding depth per topic, updated after every session
- **Today's lesson:** What the student reported was covered in class — used to generate topically relevant quiz questions and to frame the tutoring loop
- **Session history:** A summary of recent sessions on this topic — avoids repetition, targets recently weak areas, and tracks the progression arc

The Socratic diagnostic phase and the tutoring loop are handled by Claude Sonnet (claude-sonnet-4-6) — the model's reasoning capability is essential for following a student's line of thinking, identifying precisely where it breaks down, and generating explanations calibrated to both the student's current level and the curriculum endpoint. Content moderation runs in parallel via Claude Haiku.

**AI cross-validation agent**

A separate AI model (e.g. GPT-4o) validates the teaching agent's output before it is presented to the student. The validation agent checks factual accuracy, curriculum alignment, and mark scheme consistency against the reference material anchored to the student's exam board. Using a different model family for validation ensures that model-specific hallucination patterns are caught — the same model checking its own output is likely to agree with its own mistakes. This adds a small latency and cost overhead per tutoring turn, but is essential for a product where incorrect content directly harms the user.

**Curated reference material — the accuracy anchor**

The AI does not teach from its general training data alone. Each tutoring session is anchored with authoritative, freely available reference material specific to the student's exam board:

- **Exam board syllabus specifications** — the full AQA, Edexcel, OCR, DBE, and IEB specs define exactly what students must know and at what depth
- **Mark schemes** — published by exam boards after each sitting, these show the exact language and reasoning examiners expect
- **Examiner reports** — published after each exam series, these document the most common student misconceptions — directly informing the Socratic diagnosis phase
- **Siyavula (South Africa)** — open-licensed (Creative Commons) Maths and Science textbooks for Grades 10-12, directly aligned to CAPS curriculum
- **Open Educational Resources (OER)** — OpenStax and CK-12 provide peer-reviewed, commercially licensable content for foundational concepts

This reference material is loaded into the system prompt context for each session, giving the AI precise, exam-board-specific anchoring rather than relying on general knowledge. Publisher-licensed textbook content (Hodder, Pearson, CGP) is a future enhancement once revenue justifies the licensing cost.

### 3.10 Parent dashboard

The parent creates the account and invites the child. This is both a legal requirement (parental consent for processing child data) and a product decision — parents who are paying subscribers deserve visibility.

- **Weekly digest (Sundays):** Topics covered this week, understanding progression per topic, subjects where the student is building confidence, topics flagged as needing more work, streak status
- **Progression narrative:** Not just scores but the arc — where the student was struggling, how the tutoring addressed it, and the direction of travel. Framed encouragingly.
- **Optional parent notes (post-MVP):** Parents can add contextual notes about their child — learning differences, known anxieties, preferences — that inform the AI's initial approach
- **Safeguarding alerts:** Immediate notification if the content monitoring agent flags anything concerning
- **Streak milestone notifications:** Parent receives a message at 7, 30, and 100-day streaks

### 3.11 What is not in the MVP

| Feature | Rationale for deferral |
|---|---|
| Teacher module | Class-level progression visibility for teachers. Data architecture supports it. Built in Phase 2. |
| Parent notes | Optional parent context about their child's learning profile. Post-MVP. |
| School-name-to-exam-board inference | Requires crowdsourced school-board mapping data. Simplified to manual selection at MVP — students prompted to ask teacher/parent if unsure. |
| School system integration | Connecting to SIMS, MIS, or Google Classroom. Not required when the student self-reports. |
| Friend quiz battles | Social competitive layer. Phase 2 once user base is established. |
| iOS support | Flutter makes iOS build straightforward — a sequencing decision, not a technical barrier. |
| Audio narration | TTS narration of explanations. Phase 2. |
| Explanatory video | Generated video explanations. Phase 3+. |
| Early secondary (Years 7–9) | Phase 2 once the GCSE/Matric habit model is proven. |
| Afrikaans language support | Meaningful Phase 2 localisation for Western Cape schools in South Africa. |
| Web frontend | Backend API and parent digest emails serve any web-based needs at MVP. |

---

## 4. Market Opportunity

### 4.1 The addressable market

StudyMate AI enters the market at the highest-pressure point in secondary education — the GCSE and Matric years — where student and parent motivation to invest in academic support is at its peak. This is not the largest possible addressable market, but it is the most motivated cohort and the most commercially accessible entry point.

| Segment | Total students | Fee-paying addressable | Price per month |
|---|---|---|---|
| UK GCSE (Years 10–11) | ~720,000 / year | ~180,000 | £15–18 |
| SA FET & Matric (Grades 10–12) | ~2.1 million enrolled | ~270,000 | R249 (~£10) |
| Combined MVP addressable | — | ~450,000 | — |

The 450,000 figure represents the fee-paying subset — those from households that currently spend on private tutoring or academic resources. It is deliberately conservative. The full secondary school expansion (Years 7–9 and Grades 8–9) represents a further 500,000 addressable students planned for Phase 2.

### 4.2 Market context

The UK private tutoring market is worth approximately £2 billion per year. The global AI tutoring market was valued at $1.63 billion in 2024 and is projected to reach $7.99 billion by 2030, growing at 30.5% annually. The South African EdTech market was valued at $1.1 billion in 2024, with the K-12 AI segment projected to grow at 35.4% annually through to 2033. In January 2026, the UK government announced plans to pilot AI tutoring tools in state schools, validating the concept at a policy level.

Mobile is the dominant access channel in both markets. In South Africa, 90%+ of secondary students access the internet primarily via smartphone. In the UK, smartphone usage among 12–17 year olds exceeds 95%.

### 4.3 Revenue projections

| Milestone | Students | Estimated ARR |
|---|---|---|
| UK MVP launch (Month 4) | 20–30 paying students | ~£4,800–5,940 |
| UK Month 6 | 100 paying students | ~£19,800 |
| UK break-even (solo founder) | ~300 paying students | ~£59,400 |
| SA seed launch (Month 12) | 50 paying SA students | ~£6,000 equivalent |
| UK Year 1 target | 300–500 paying students | ~£59,400–99,000 |
| Combined Year 2 target | 2,000 paying students | ~£360,000 |
| Combined Year 3 — 1% addressable | 4,500 paying students | ~£850,000 ARR |
| Phase 2 — add Years 7–9 / Gr 8–9 | +5,000 students | Additional ~£900,000 ARR |

**Note on projections:** the Month 4 and Month 6 figures are deliberately conservative. As a solo founder launching a new product with no existing brand, the first paying customers will come from personal network and word-of-mouth referrals. Organic growth via Play Store, SEO, and social channels takes 3–6 months to build momentum. The projections above reflect this reality.

---

## 5. Competitive Landscape

### 5.1 Existing products

| Competitor | Positioning | Gap |
|---|---|---|
| Medly AI | GCSE/A-Level AI tutor. £1.2M seed (Oct 2024). 10,000 students. | Exam revision tool — not a daily habit product. No adaptive tutoring loop from first principles. No Socratic diagnosis of student understanding. No parent reporting. |
| Cognito | Adaptive quizzing. Free. UK exam board aligned. | Student must choose to start a session. Adaptive difficulty on quizzes, but no tutoring loop that finds the student's baseline and scaffolds up. No parent reporting. |
| Duolingo | Daily habit gamification — the clear benchmark for daily engagement in EdTech. | Covers languages only. Fixed content — cannot adapt the explanation, only the difficulty of the question. |
| Quizlet | Student-generated flashcard decks. Large user base among GCSE students. | Entirely self-directed and passive. No AI tutoring. No understanding scaffold. No parent layer. |
| ChatGPT / Claude | Used informally by students for homework help. | No structure, no habit loop, no gamification, no curriculum alignment, no parent layer. Student must entirely drive the interaction — a skill struggling students do not have. |
| Human tutors | £35–50 per hour. Best outcomes. | Cost-prohibitive for daily reinforcement. Not available at 9pm after school. No parent reporting. No ability to remember every prior session. |

### 5.2 StudyMate AI's differentiated position

The specific combination that no existing product delivers:

1. **Adaptive tutoring from first principles** — the AI locates where a student's understanding breaks down and teaches from there, using Socratic questioning to diagnose and then progressive scaffolding to build up to curriculum level
2. **Silent learner profile** — the app learns how each student understands things best and gets better at teaching them over time, without requiring self-reporting
3. **Daily check-in habit** — native push notification at the student's chosen time, student-driven without any teacher dependency
4. **Curriculum-anchored endpoint** — the tutoring loop does not stop at "roughly understands" — it stops when the student can handle what their specific exam board will ask
5. **AI cross-validation** — a separate AI model validates every teaching output for factual accuracy and curriculum alignment before it reaches the student
6. **Curated reference anchoring** — the AI teaches from authoritative exam board specifications, mark schemes, and examiner reports, not from general training data alone
7. **Explicit progression visibility** — the student and parent can see the arc from confusion to competence, not just a score
8. **Parent visibility layer** — weekly digest and progression narrative, with the parent owning the account
9. **Dual-market from launch** — UK GCSE and South African Matric, with personal network enabling faster SA adoption
10. **Native Android application** — the right form factor for a product whose core interaction happens on the way home from school

**The private tutor benchmark**

The best private tutors do not test and tell. They ask. They notice confusion. They try a different explanation. They go back to first principles when needed. They remember what worked last time. They build the student's confidence by making understanding feel achievable. StudyMate AI is not trying to be better than a Duolingo habit — it is trying to be the private tutor that 95% of students cannot afford.

---

## 6. Monetisation

### 6.1 Subscription tiers

| Tier | Price | Includes |
|---|---|---|
| Free | £0 / R0 per month | 3 subjects, 5 check-ins per month. No parent dashboard. No badge leaderboard. Full quiz and tutoring experience — acquisition and habit-seeding layer. |
| Student Plus | £15–18 / R249 per month | All subjects, unlimited daily check-ins, full adaptive tutoring loop, full parent dashboard with weekly digest and progression narrative, complete badge collection, streak protection (one missed day per month forgiven). |
| Family | £22 / R320 per month | Up to 3 children. Single parent login sees all children's progress. Targets households with siblings in GCSE years. |
| School Licence (Phase 2) | £3–5 / R50–80 per pupil/year | Full year-group access. Teacher dashboard with class-level progression data. School-branded badge set. Compatible with LEA and provincial procurement. |

### 6.2 Unit economics

| Metric | Estimate |
|---|---|
| Monthly subscription (blended UK) | £16 |
| AI API cost per student per month (estimated) | ~£2.00–4.00 |
| AI cross-validation overhead | ~20–30% of tutoring API cost |
| Hosting and infrastructure (1,000 students) | ~£80/month total |
| Gross margin at scale (at £16 price) | ~75–87% |
| Gross margin at scale (at £20–22 price) | ~82–90% |
| Estimated LTV (GCSE joiner — 2 years) | ~£384–528 |
| Target CAC (organic and referral) | < £20 |
| LTV:CAC ratio | ~19–26:1 |

**API cost note — requires validation:** the adaptive tutoring loop is conversational — it involves 10-15 Sonnet calls and 10-15 Haiku calls per session, with growing context windows as the conversation progresses. The cross-validation agent (a separate model checking each teaching output) adds approximately 20-30% to the tutoring API cost. At an estimated 30 sessions per month, the monthly API cost per student is approximately £2.00–4.00. This estimate must be validated against real token usage from a sample tutoring session before finalising the subscription price. If real costs are at the upper end, the subscription price may need to increase from £16 to £20–22 to protect margins. Prompt caching on stable system prompt prefixes reduces cost as the student's profile matures — this is the primary cost efficiency mechanism.

---

## 7. Safeguarding and Legal Compliance

### 7.1 Parent-owned account model

The parent creates the account, pays the subscription, and invites the child as a sub-profile. This is the lawful basis for processing child data under both UK GDPR (Article 8) and South Africa's POPIA. The parent can view, export, or delete all data at any time. On account closure, child data is deleted within 30 days.

- Only session summaries and learner profile signals are stored — never full conversation transcripts
- No geolocation, no commercial behavioural profiling, no data sharing with third parties
- All 15 standards of the UK Age Appropriate Design Code (Children's Code) formally audited before launch
- Data Processing Agreement signed with Anthropic before any student data passes through the API

### 7.2 Content monitoring

A secondary AI agent — Claude Haiku — reviews every student message and every AI response before it is stored or displayed. On flagging anything concerning, the parent receives an immediate notification and the session pauses. The Terms of Service clearly state the monitoring agent's limitations and that it is not a substitute for professional safeguarding services.

### 7.3 Required legal steps before launch

- Engage a UK data protection solicitor for a two-hour review — budget £500–1,000. Complete before any production code touches real child data.
- Complete a Data Protection Impact Assessment (DPIA) under UK GDPR
- Draft two privacy notices: one legal document for parents, one in plain language for the child
- Confirm Supabase instance hosted in UK or EEA before storing any student data
- Engage a South African data protection attorney (budget R5,000–10,000) before SA launch — POPIA compliance and cross-border transfer documentation

---

## 8. Technical Architecture

### 8.1 Stack

| Layer | Technology |
|---|---|
| **Mobile app (primary)** | Flutter (Dart). Android-first MVP, targeting Android 8.0+. iOS build follows in Phase 1b using the same Flutter codebase — no rewrite required. Published to Google Play Store at launch. |
| **API layer** | ASP.NET Core 8 Minimal API. C#. Thin HTTP boundary. Dispatches to Application layer via MediatR. No business logic in endpoint handlers. |
| **Architecture** | Domain-Driven Design with strict four-layer separation. Domain layer has zero external framework dependencies. Bounded contexts: Learning, Identity, Curriculum, Reporting, Safeguarding. |
| **AI — tutoring and quiz** | Anthropic claude-sonnet-4-6. Handles the Socratic diagnostic phase, the adaptive tutoring loop, and quiz generation. Called multiple times per session in the tutoring loop — conversation is stateful within a session. |
| **AI — moderation** | Anthropic claude-haiku-4-5. Runs in parallel on every student message and every AI response. Fast and cost-effective for content safety. |
| **Database** | PostgreSQL via Supabase. UK/EEA hosted. EF Core ORM. Row-level security for multi-tenant isolation. Session data stored as JSONB. Learner profile signals stored per student per topic. |
| **Authentication** | Supabase Auth. JWT tokens. Parent / Student role claims. Child as sub-profile under parent account. |
| **Background jobs** | Hangfire. Weekly parent digest cron (Sundays 8am). Badge and mastery recalculation. Postgres-backed job storage. |
| **Email** | SendGrid. Weekly parent digests and safeguarding alerts. |
| **Payments** | Stripe. GBP (UK) and ZAR (SA) subscription plans. Family plan. Webhook handler for subscription lifecycle events. |
| **Hosting** | Azure Container Apps. Autoscales on load. Secrets via Azure Key Vault. |

### 8.2 The tutoring session — how the AI calls work

A tutoring session is conversational and stateful. It involves multiple AI calls within a single session, not one call returning a fixed output.

| Phase | AI call | Purpose |
|---|---|---|
| Quiz generation | Claude Sonnet (single call) | Generates 5 diagnostic questions based on today's reported topic and the student's mastery map. Returns structured JSON. |
| Socratic diagnosis | Claude Sonnet (conversational) | Asks the student to explain their reasoning on wrong answers. Follows the student's line of thinking. Identifies exactly where the mental model breaks down. |
| Explanation — initial | Claude Sonnet | Generates a first-principles explanation calibrated to the diagnosed starting level. Includes text; may include image prompts for diagram generation. |
| Understanding check | Claude Sonnet (conversational) | Checks whether the student has understood before scaffolding up. Tries a different framing if needed. |
| Scaffolding — curriculum level | Claude Sonnet | Progressively builds the explanation toward the exam board's expected level. Anchors to syllabus. |
| Final confirmation | Claude Sonnet | Presents an exam-style question. Evaluates the student's response for reasoning quality, not just correctness. |
| Cross-validation | Separate model (e.g. GPT-4o) | Validates the teaching agent's output for factual accuracy, curriculum alignment, and mark scheme consistency before presenting to the student. Catches model-specific hallucination patterns. |
| Moderation | Claude Haiku (parallel, every message) | Reviews every student message and every AI response. Flags safeguarding concerns immediately. |

**Prompt caching:** The student's profile and mastery map form a stable system prompt prefix that is cached by the API. As the student's profile matures, the cached prefix grows richer without increasing marginal cost. This is the primary cost efficiency mechanism for the tutoring loop.

### 8.3 Learner profile data model

The learner profile is built silently over time from session behaviour. Key signals stored per student:

- Which explanation approaches correlated with successful understanding checks (analogy, logical derivation, worked example, diagram)
- Which topics required foundational re-grounding vs. curriculum-level teaching from the start
- Typical session length before understanding is confirmed — a proxy for cognitive load on different topics
- Which question types (calculation, explanation, application, comparison) the student handles well vs. poorly

This profile is stored in PostgreSQL as a structured JSONB document per student, versioned so degrading signals can be rolled back if data quality issues are detected.

### 8.4 Badge and mastery data model

The badge system is driven by the mastery map — a table of accuracy scores and understanding depth ratings per student per topic, updated after every session. Badge tier thresholds: Beginner (0–39%), Developing (40–54%), Confident (55–69%), Strong (70–84%), Expert (85%+). Understanding depth (confirmed through tutoring sessions, not just quiz accuracy) is a secondary signal that can accelerate badge progression for students who demonstrate deep comprehension.

---

## 9. Go-to-Market Strategy

### 9.1 UK — seed (Months 1–3)

The product validation starts with one student: the founder's daughter, currently in GCSE year. Her unprompted daily usage — or absence of it — is the most meaningful product-market fit signal available. If she opens the app after school without being reminded, the habit loop works.

- Expand to her peer group and their parents — 10–20 families via personal introduction
- UK parent communities: Facebook groups (GCSE Parents Support, Secondary School UK Mums), Mumsnet secondary education boards
- Student communities: r/GCSE (95K+ members)
- Offer 3 months free to the first 50 families in exchange for structured feedback — specifically on the tutoring loop quality, explanation clarity, and whether students feel they have genuinely understood
- Measure three metrics in this phase: (1) daily check-in completion rate — target 60% of users completing a check-in on any given school day; (2) tutoring loop completion rate — do students stay through the Socratic diagnosis and scaffolding, or drop off?; (3) disengagement fallback trigger rate — how often does the shortened session activate, and does the student re-engage on subsequent days?

### 9.2 UK — growth (Months 3–12)

- Freemium tier live at Month 3: free users share the product with friends. The badge display and progression story are designed for word-of-mouth.
- Google Play Store listing optimised for search: 'GCSE revision app', 'GCSE tutor app', 'GCSE quiz app'
- SEO content from Month 3: blog posts targeting 'GCSE revision tips', 'how to study for GCSEs', 'GCSE Maths revision'
- TikTok and Instagram Reels showing a student going from a wrong quiz answer through the tutoring loop to a correct exam-style answer — the transformation story is the product's best marketing asset
- Referral programme: students get one free month for each friend who converts to a paid plan
- Target: 300–500 paying UK students by Month 12

### 9.3 South Africa — seed and launch (Months 12–18)

- Month 12: founder's personal SA network — 10–20 families with Matric-year students. Free access in exchange for structured feedback on CAPS curriculum quality and Android performance on SA devices.
- Month 15: SA MVP launch at R249/month. South African CAPS curriculum for both DBE and IEB. Android app validated on mid-range Android hardware.
- SA social channels: Instagram and TikTok perform strongly with South African Matric students, particularly around exam season.
- Android is the dominant platform in South Africa — the choice of Android-first perfectly matches this market.
- Target: 200 paying SA students by Month 18

### 9.4 iOS launch (Month 6–9)

- Once the Android habit loop is validated, the Flutter codebase is compiled for iOS and submitted to the Apple App Store.
- The iOS build requires no rewrite — only platform-specific configuration (provisioning, App Store guidelines compliance, StoreKit in-app purchase integration).
- Target: iOS available by Month 9

### 9.5 Phase 2 expansion (Month 18+)

- **Teacher module:** class-level progression data surfaced to teachers whose students are already using the product. Free to teachers initially — creates bottom-up institutional adoption without formal procurement.
- **Audio narration:** TTS narration of AI explanations, expanding the tutoring loop's modality options.
- **Friend quiz battles:** once 1,000+ students are active, the social graph has enough density for battles to work.
- **Parent notes:** optional parent-added context about their child's learning profile.
- **Early secondary expansion:** Years 7–9 in the UK and Grades 8–9 in South Africa.
- **UK government AI tutoring pilot (DfE, 2027):** register as a potential partner — daily usage data, parent reporting, and progression narratives make the product a strong candidate.

---

## 10. Risk Assessment

| Risk | Status | Mitigation |
|---|---|---|
| Daily habit does not form | Primary risk | Native push notifications at the student's chosen time, streak mechanics, parent digest that makes engagement visible. Validated in seed phase before scaling spend. |
| Tutoring loop quality is not good enough | High importance | If the Socratic diagnosis feels robotic or the explanations miss the student's actual confusion, students will not stay through the loop. Mitigation: extensive seed-phase testing with real students, qualitative feedback on whether they felt genuinely understood. The tutoring loop is the product — it must be excellent before scaling. |
| Loop is too long — students drop off | High importance | The tutoring loop is conversational and could feel long if not well-paced. Mitigation: session design targets a maximum of 12–15 minutes including quiz and full tutoring. Progress indicators in-app. Students can save and resume a session. |
| AI content accuracy | High importance | The AI may teach concepts incorrectly or with subtle inaccuracies. For a product used by children sitting high-stakes exams, incorrect content causes direct harm. Mitigation: AI cross-validation agent (separate model family) checks every teaching output against curated reference material. "Flag this explanation" button provides structured user feedback. Exam board specs, mark schemes, and examiner reports anchor all content to authoritative sources. At seed phase, flagged content reviewed manually. |
| Student disengagement during tutoring loop | High importance | Tired students after school may give minimal responses ("idk"), making the Socratic loop ineffective. Mitigation: disengagement fallback shortens the session after two low-effort responses, logs topic as "incomplete understanding" for revisiting, preserves streak credit. Protects the daily habit from being killed by an overly demanding session. |
| AI cost higher than projected | Medium | The conversational tutoring loop uses more tokens than a quiz-only model, and the cross-validation agent adds ~20-30% overhead. Mitigation: prompt caching on stable prefixes, Haiku for moderation, session length caps to prevent unbounded conversations. Monitor cost per session from day one. Subscription pricing may need to increase to £20-22 if costs are at the upper end. |
| Big tech competition | Ongoing | Google, Microsoft, and OpenAI all building education tools. Mitigation: daily check-in habit mechanic, Socratic tutoring loop, silent learner profile, and dual-market specificity (UK exam boards + SA CAPS) are not priorities for large platforms serving the whole curriculum globally. |
| Student self-reporting accuracy | Medium | Students may report topics vaguely or incorrectly. Mitigation: the agent asks a follow-up question if the initial report is too vague. The mastery map compensates over time. |
| GDPR / Children's Code (UK) | Action required | Parent account model and data minimisation address core risks. DPIA and solicitor review required before UK launch. |
| POPIA compliance (SA) | Action required | SA data protection attorney review required before SA launch. |
| Solo founder execution | Elevated | MVP scope is deliberately narrow, with an extended build timeline to protect tutoring loop quality. SA launch is 12 months after UK — never simultaneous. iOS follows Android — never parallel. |
| Gamification backfire | Low | Badges and streaks could create anxiety in some students. Mitigation: streak recovery mechanic, no public leaderboard in MVP, badges earned not taken away, progression framed as encouraging narrative. |

---

## 11. Build Plan

### 11.1 Milestone roadmap

| When | Stage | Deliverables |
|---|---|---|
| Weeks 1–2 | Legal groundwork | UK data protection solicitor review. DPIA begun. Supabase UK/EEA hosting confirmed. Parent and child-friendly privacy notices drafted. Anthropic Data Processing Agreement signed. |
| Weeks 3–6 | Core tutoring loop | Focus exclusively on the tutoring loop quality: Socratic diagnosis, explanation scaffolding, understanding checks, disengagement fallback. One subject (Maths) only. Text only. Curated reference material (AQA Maths spec, mark schemes, examiner reports) loaded and tested. AI cross-validation agent integrated. No UI polish, no auth, no payments. Tested with founder's daughter. |
| Weeks 7–10 | Android prototype | Flutter app: daily check-in flow, diagnostic quiz, tutoring loop with disengagement fallback, "flag this explanation" button, streak counter. Timetable upload. Three GCSE subjects. Cross-validation agent live on all tutoring output. Tested with founder's daughter and 5 peers on Android devices. |
| Month 3–4 | UK private beta | Full subject suite (8 subjects). Curated reference material for all subjects. Parent account model with child invite. Weekly digest email with progression narrative. Stripe payments live. Basic badge system. Freemium tier active. 20–50 families. Android only. |
| Month 4 | UK MVP launch | Push notifications live (Android). Timetable upload polished. Badge collection screen. Exam board selection (manual, with prompt to ask teacher/parent if unsure). Safeguarding content monitoring. UK GDPR compliance confirmed. Google Play Store listing live. Public launch. |
| Month 6 | UK growth — 100 paying students | SEO content live. Referral programme. Streak milestone parent notifications. Badge sharing to social media. |
| Month 7–10 | iOS launch | Flutter iOS build compiled and submitted to Apple App Store. StoreKit in-app purchase integration. iOS-specific UI polish. |
| Month 10–12 | SA preparation | CAPS subject taxonomy and topic structure. Siyavula OER content integrated for Maths and Science. DBE and IEB exam board configuration. R249/month ZAR pricing in Stripe. SA POPIA legal review complete. Android app tested on mid-range SA devices. |
| Month 12 | SA seed launch | 10–20 SA families on free Android access. Structured feedback on curriculum quality and mobile experience. |
| Month 15 | SA MVP launch | R249/month live. Full SA curriculum. SA parent digest. |
| Month 18 | Phase 2 planning | Teacher module design. Audio narration. Friend quiz battles. Parent notes feature. Early secondary curriculum scoping. Seed round assessment. Automated content flag review workflow. School-name-to-exam-board inference (crowdsourced from user data). |

**Timeline philosophy:** the build timeline is extended compared to an aggressive 8-week MVP because the tutoring loop is the product. If the Socratic diagnosis, explanation quality, and content accuracy are not excellent, nothing else matters. The first 6 weeks are dedicated to getting the tutoring loop right with one subject before expanding scope.

### 11.2 Cash cost to SA MVP launch

- UK data protection solicitor: £500–1,000
- SA data protection attorney: £200–400
- Supabase hosting (UK/EEA): £25/month
- Azure Container Apps: £30–60/month
- Anthropic API (prototype through early paying): £50–100/month (higher than quiz-only model due to tutoring loop)
- SendGrid, Stripe, Apple Developer Programme (£99/year), Google Play Console (£21 one-time), domain, miscellaneous: ~£60/month
- **Total cash cost to SA MVP launch at Month 15: under £5,000**

---

## 12. Summary

StudyMate AI is not a quiz app. It is a personal AI tutor — the tutor that 95% of students have never had access to. The daily check-in and five-question quiz are how students build the habit and how the system diagnoses where each student's understanding sits. What follows is the real product: an adaptive tutoring loop that locates the precise point where understanding breaks down, explains from first principles in a way that works for this particular student, and scaffolds them step by step up to the level their exam board expects.

The product is built on a simple and well-evidenced observation: everyone in the world understands things differently. When a classroom has thirty students and one teacher, some students are inevitably left behind — not because they cannot learn, but because the teaching model cannot adapt to them. StudyMate AI adapts. It learns each student over time. It gets better at teaching them specifically. And it makes that progression visible to the student and their parent in a way that builds genuine confidence.

The MVP launches as a **native Android mobile application built with Flutter**, with text and image explanations, Socratic tutoring, and parent progression visibility. Audio comes in Phase 2. Video in Phase 3. The teacher module follows once the student and parent product is proven.

The technical foundation is solid: ASP.NET Core 8 with Domain-Driven Design, Flutter for Android (and soon iOS), the Anthropic API providing the tutoring intelligence and content moderation, and a separate AI model cross-validating every teaching output for accuracy. All tutoring content is anchored to authoritative exam board specifications, mark schemes, and examiner reports — not generated from general training data alone. The legal groundwork is defined and costed. The go-to-market starts with one student in the founder's household and builds outward.

**Immediate next steps:**

1. Engage a UK data protection solicitor this month — before any code touches real child data
2. Build the tutoring loop first — Socratic diagnosis, explanation scaffolding, disengagement fallback, and AI cross-validation — for Maths only. Anchor with AQA Maths spec, mark schemes, and examiner reports. Get this right before building anything else.
3. Measure three metrics in prototype phase: (1) does she open it without being asked? (2) does she stay through the tutoring loop when she gets something wrong? (3) how often does the disengagement fallback trigger?
4. Run 5 parent interviews — does the progression narrative tell them what they actually want to know?
5. Identify 3–5 South African families now — brief them so they are ready for Month 12
6. Implement native Android push notifications from week one — the daily habit depends on the prompt

**The first milestone that matters**

If the founder's daughter completes a daily check-in for 14 consecutive days without being reminded, and stays through the tutoring loop when she gets a question wrong, the core product works. Everything else — the parent dashboard, the badges, the iOS launch, the South Africa expansion, the school licensing, the friend battles — is built on that foundation.

---

*End of Document*

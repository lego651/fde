# CTO Feasibility & Build-Cost Assessment

**Scope:** Technical/cost feasibility of four SMB AI product candidates, for a solo engineer, Claude-assisted, 90 days full-time, ~$1,000 cash budget. Companion to the CMO's market-angle research on the same candidate list (parent: FDE-1).

**Basis for estimates:** general knowledge of the relevant tech stacks, APIs, and typical integration effort for a solo engineer working with AI-assisted coding tools. No code has been written or prototyped for this assessment, and no outside vendors were contacted — all cost and time figures below are estimates, not measurements, and should be treated as planning inputs rather than commitments. Where a number is a guess rather than a published price, it's marked "assumed."

---

## 1. Physio-clinic-style AI ops tool

**What it is:** voice intake → fills patient forms + saves profile; automated post-visit follow-up messaging; AI-drafted review text for patient approval (before send, not auto-posted).

### Complexity & timeline
Already built once for one clinic (single-tenant), per the issue brief — this materially changes the estimate from a greenfield build. Productizing into a thin multi-tenant layer (per-clinic config, auth, data isolation) on top of existing single-tenant logic is realistically **2-4 weeks** for a solo engineer. Widening to other verticals (dental, chiro, salons) is mostly intake-form schema changes and prompt tuning, not new architecture — **roughly 1 week per adjacent vertical** once the multi-tenant core exists, assuming the voice-intake and messaging pipeline generalizes without redesign.

Greenfield (if the "already built" claim doesn't hold up on inspection, or the existing build is throwaway/prototype code not worth carrying forward) would be **6-10 weeks**: voice capture + transcription + structured field extraction is the hard part; follow-up messaging and review-draft generation are comparatively simple LLM-prompt-and-send flows.

### Build vs. buy
- Voice-to-text: buy (Whisper API / Deepgram / AssemblyAI) — building this from scratch is not worth it at this scale.
- Form-filling / structured extraction from transcript: build (thin LLM prompt layer over the transcription), this is the core IP.
- Messaging (SMS/email follow-up): buy — Twilio, or email via Postmark/Resend. Not worth building.
- No viable no-code assembly for the voice-intake piece specifically; the review-draft and follow-up pieces could be partially assembled from no-code tools (Zapier/Make + an LLM step) but would be flimsy for anything patient-facing.

### Ongoing costs (5-10 pilot clinics, assumed moderate usage — ~50-100 patient visits/month per clinic)
- Hosting (small app, e.g. Fly.io/Render/Railway): **$20-50/mo** (assumed).
- Transcription API: assumed ~$0.25-0.65/hour of audio (Whisper-API-class pricing); at ~10 min/intake × 500-1000 intakes/mo across pilots ≈ **$20-60/mo** (assumed).
- LLM API (form extraction + follow-up drafting + review drafting): light usage per visit, likely **$20-50/mo** total across pilots (assumed).
- SMS/email for follow-up: Twilio SMS is typically low-cents per message; at 500-1000 messages/mo, **$10-40/mo** (assumed).
- **Total assumed: ~$70-200/mo** for 5-10 pilot clinics. This is a rough planning estimate, not a vendor quote — validate against actual Twilio/Whisper/LLM pricing before committing a client to a price.

### Services-first viable?
**Yes, and arguably the strongest candidate for this.** Since one clinic's version already exists, the founder could manually onboard 2-3 more clinics using the existing single-tenant build (copy/configure per client) before investing in multi-tenancy — i.e., a white-glove/templated rollout rather than real SaaS. This defers the productization cost until there's repeat demand signal.

### Key technical risks
- **Voice intake accuracy**: medical/dental terminology, accents, and noisy clinic environments can degrade transcription accuracy; misfilled patient forms are a trust-breaking failure mode, not a minor bug. Needs a human-review step before data is finalized, at least initially.
- **PHI / privacy**: patient intake data is likely to qualify as personal health information depending on jurisdiction (Canada: PIPEDA + possibly provincial health-privacy statutes like Alberta's HIA if clinics are in Alberta). This is a legal/compliance question, not purely technical, but it has real technical consequences: need encryption at rest/in transit, data residency consideration (Canadian hosting may be required or strongly preferred for health data), access controls, and a clear data-retention/deletion policy. **Recommend explicit legal review before any multi-clinic PHI handling** — flagging this to the CEO/board rather than deciding it unilaterally.
- **AI-drafted review text**: kept as a human-approved draft (per the issue's framing) avoids the compliance risk flagged for candidate 2 below, but the same "don't auto-post AI-written reviews" caution applies if this ever gets automated further.

---

## 2. Local SMB review/visibility growth tool (compliant version)

**What it is:** automated review-request reminders + easy review links (e.g., direct Google review deep links) + simple dashboard tracking requests/reviews. Explicitly **not** AI-authored review text — customer writes their own review.

### Complexity & timeline
This is the simplest candidate on the list. Core loop: trigger (e.g., after a POS/booking event, or manual CSV upload) → send SMS/email with a review link → track clicks/completions on a dashboard. **Realistic MVP: 1.5-3 weeks** solo, Claude-assisted. Most of the complexity is in the dashboard polish and reliable link-tracking, not novel tech.

### Build vs. buy
This category has a notable **buy-side risk**: there are many existing no-code/low-code reputation-management tools (Podium, NiceJob, Birdeye, etc.) already doing exactly this. A no-code assembly (Zapier/Make + Twilio/SendGrid + a Google Sheet or Airtable dashboard) could realistically hit a working MVP **in days, not weeks**, and may be worth prototyping before building custom — the differentiation has to come from price, local-market fit, or bundling with another service, not from technical novelty. Building custom is justified mainly if bundling this into a broader local-SMB offering (e.g., alongside candidate 1).

### Ongoing costs (5-10 pilot businesses)
- Hosting: **$10-20/mo** (assumed) — this is a lightweight CRUD app.
- SMS/email sending: **$10-30/mo** (assumed) depending on volume (assume 50-200 review requests/mo per business).
- No significant LLM cost (no AI-authored content in the compliant version) — maybe trivial usage if an LLM is used to personalize the reminder copy template, effectively **$0-5/mo**.
- **Total assumed: ~$20-55/mo** for 5-10 pilots. Lowest ongoing cost of the four candidates.

### Services-first viable?
**Yes, and easiest of the four.** Could be delivered almost entirely as a manual/templated service in week one (manually sending review-link texts via existing tools) while a lightweight dashboard is built behind it. Low technical risk means the main question is market demand/willingness to pay, which is the CMO's research angle.

### Key technical risks
- Low technical risk overall. Main risk is **platform policy compliance** — review-link/reminder automation must stay within Google's review policies (no incentivized reviews, no review-gating by sentiment) to avoid the business's Google listing being penalized. This is a known industry gray area; worth a short explicit policy check before pitching, since a client's Google profile being penalized would be a severe trust failure. Flagging as a research/legal item, not deciding it here.
- Attribution/tracking accuracy (did the review actually come from this reminder?) is inherently fuzzy since Google doesn't expose a clean referral signal — dashboards in this space generally approximate (click-through rates, timing correlation) rather than prove causation. Set client expectations accordingly.

---

## 3. Realtor portfolio/lead-gen websites

**What it is:** marketing/portfolio sites for individual realtors with lead capture.

### Complexity & timeline
A single realtor site (template-based, with a contact/lead form and maybe a blog) is **genuinely fast — 3-5 days** per site using an existing template system. But the issue brief is right to flag incumbent risk: this space has entrenched, well-funded competitors (IDX-integrated site builders like Real Geeks, BoomTown, Sierra Interactive, Placester) that offer MLS/IDX listing integration, which is usually the actual value driver for a realtor's site, not the design. **A differentiated MVP that includes real IDX/MLS integration is a different, much larger problem**: MLS data access requires board-level data licensing agreements (e.g., through a regional real estate board), which involves business/legal process, not just engineering — likely **4-8+ weeks of calendar time dominated by licensing/approval delay**, not coding effort, plus ongoing data-license fees that are typically **not** covered by the $1k budget.

A non-IDX MVP (portfolio + lead form + maybe a simple AI-assisted "describe your dream home" lead-qualifier chatbot) is buildable in **1-2 weeks**, but is a weaker product precisely because it lacks what competitors already offer, and differentiation would have to come from something other than core features (e.g., aggressive pricing, superior copy/design for a specific local niche).

### Build vs. buy
Template-based site builders (Webflow, or a lightweight Next.js template reused per client) make the build side cheap. No credible no-code path to IDX integration — that's a data-licensing problem, not a tooling one.

### Ongoing costs (5-10 realtor clients)
- Hosting for 5-10 static/light sites: **$10-25/mo total** (assumed) on something like Vercel/Netlify free-to-cheap tiers.
- If an AI lead-qualifier chatbot is included: light LLM usage, **$5-20/mo** (assumed) across clients.
- IDX data licensing, if pursued: **assumed $20-50+/month per client** paid to an IDX provider/board, separate from the founder's own costs — this would typically be passed through to the client, not absorbed.
- **Total assumed (non-IDX version): ~$15-45/mo** for 5-10 clients.

### Services-first viable?
Yes for the simple version — effectively a web-design service with a modest recurring hosting/maintenance fee, deliverable without any product build. Not really a SaaS product unless templatized into a self-serve builder, which is a bigger investment than the $1k/90-day budget supports if IDX is in scope.

### Key technical risks
- Low technical risk for the non-IDX version.
- **Primary risk is competitive, not technical**: without IDX, this is a commodity web-design offering competing against (a) established IDX-integrated platforms and (b) general-purpose freelance web designers. Worth flagging clearly to CMO/CEO — the technical assessment here supports deprioritizing this candidate unless local market research finds realtors specifically underserved by current options at a price point the founder can hit profitably.

---

## 4. Airbnb host direct-booking websites

**What it is:** direct-booking site per host, bypassing Airbnb/VRBO fees — needs calendar sync, availability, and payments.

### Complexity & timeline
This is the **most technically involved candidate** of the four. Minimum viable scope: single-property (or small multi-property) booking site with real-time availability, calendar sync to avoid double-booking against Airbnb/VRBO, and a payment flow. Realistic MVP: **4-6 weeks** solo, assuming use of existing payment infra (Stripe) and calendar-sync via iCal feeds (Airbnb/VRBO both expose iCal export/import, which is the low-effort sync path — true two-way API sync requires Airbnb's partner API, which has approval gatekeeping and is not reliably accessible to an independent solo developer within 90 days).

### Build vs. buy
- Payments: buy — Stripe (Stripe Checkout/Payment Links can shortcut a lot of custom payment UI work).
- Calendar sync: **iCal-based one-way/near-real-time sync is the pragmatic buy-ish approach** (poll external iCal feeds periodically); true bidirectional real-time sync needs platform API partnership status that's a business-development/approval problem, not something solvable by engineering effort alone within the timeline.
- There are existing no-code direct-booking tools (Lodgify, Hostaway, OwnerRez, Smartbnb/Hospitable) already serving this niche — similar buy-side risk to candidate 3. A custom build is justified mainly if targeting a price point or local-host segment these tools don't serve well.

### Ongoing costs (5-10 pilot hosts)
- Hosting: **$15-30/mo** (assumed).
- Stripe fees: transaction-based (~2.9%+30¢ typical), not a fixed monthly cost but scales with booking volume — not a "hosting cost" but worth flagging to hosts as pass-through.
- Calendar sync (iCal polling): negligible compute cost, **~$0-5/mo**.
- No significant LLM usage needed unless adding an AI concierge/FAQ feature — if added, **$5-20/mo** (assumed).
- **Total assumed: ~$20-55/mo** (excluding Stripe transaction fees, which are volume-based and typically pass through to the host).

### Services-first viable?
Partially. The site-build-and-launch part can be delivered as a one-time templated service; but a booking site is useless without working calendar sync and payments from day one — unlike candidates 1 and 2, there's no meaningful "manual version" of this to sell before the product works, because the whole point is that bookings happen automatically. So this is closer to **"requires real product from day one"** than services-first.

### Key technical risks
- **Double-booking risk is the critical failure mode**: if calendar sync lags or fails silently, a host gets two guests booked for the same dates — a severe trust-breaking bug for a hospitality business, worse than a typical software bug because it has real-world, hard-to-undo consequences (a guest shows up to a booked room). Needs conservative design (sync frequency, explicit "last synced" indicators, manual-override safeguards) from day one, not added later.
- **Payment/refund/cancellation-policy handling** adds real complexity (partial refunds, cancellation windows) that's easy to underscope initially.
- Platform API access risk: if the long-term vision depends on real-time two-way Airbnb API integration, that's gated by Airbnb's partner program and not guaranteed to be obtainable solo — scope commitments to hosts accordingly (don't promise real-time two-way sync until partner access is confirmed).

---

## Comparison summary

| Candidate | Weeks to MVP (solo) | Services-first? | Monthly cost @ 5-10 pilots (assumed) | Primary risk |
|---|---|---|---|---|
| 1. Physio/clinic AI ops | 2-4 (productize existing build) | Yes — strongest fit | $70-200 | PHI/privacy compliance; voice accuracy |
| 2. Review/visibility (compliant) | 1.5-3 | Yes — easiest | $20-55 | Buy-side competition; Google policy compliance |
| 3. Realtor sites (non-IDX) | 1-2 | Yes, but weak differentiation | $15-45 | Competitive commodity risk, not technical |
| 4. Airbnb direct-booking | 4-6 | No — needs working product | $20-55 (+ Stripe fees) | Double-booking failure mode; no real-time platform API access |

---

## Recommendation

**Most buildable within $1k/90 days: Candidates 1 and 2.**

- **Candidate 1 (clinic AI ops)** has the best economics specifically because it isn't greenfield — one clinic's version already exists, so the 90-day budget goes toward productization and vertical-widening rather than invention. It also has the clearest services-first on-ramp (manually extend the existing build to 2-3 more clinics before building multi-tenancy) and the highest willingness-to-pay potential per customer (patient-facing ops tooling is higher-value than a review-reminder tool). The PHI/privacy question needs an explicit legal check early — this should be resolved (or at least formally flagged to the board) before pitching beyond the clinics already comfortable with the existing single-tenant arrangement.
- **Candidate 2 (compliant review/visibility tool)** is the lowest-risk, fastest-to-revenue option and a reasonable complement to #1 — it could be sold as an add-on to the same local-service-business customer base (clinics, salons, etc. all want more Google reviews), reusing the same go-to-market motion. Its main risk is competitive crowding, which is a market question for the CMO's research, not a technical blocker.
- **Candidates 3 and 4 are not recommended as the primary bet** for this budget/timeline: #3's technical ceiling is capped by IDX licensing it can't realistically clear in 90 days, and the non-IDX version is a commodity service facing stiff incumbent competition; #4 demands a working product (not a services-first ramp) with a severe failure mode (double bookings) and no real path to the real-time platform integration that would differentiate it, within this budget.

**Proposed minimal first SaaS product after services-first validation:**
A multi-tenant "AI front-desk" product for local service businesses (starting with physio/dental/chiro/salons), combining candidate 1's voice-intake-and-follow-up core with candidate 2's review-request flow as a bundled feature — i.e., don't build two separate products; build one local-service-business ops tool where "ask for a review after a good visit" is a natural extension of the same patient/client-communication pipeline already needed for follow-up messaging. This also diversifies the vertical risk: if clinics specifically stall on PHI/privacy concerns, the same core product (minus patient-form-filling) still has a market in salons/other appointment-based local businesses with no PHI complication.

This recommendation is a technical/cost-feasibility view only — final vertical choice should weight the CMO's market-research findings (demand signal, willingness to pay, competitive density) alongside this assessment before the board commits.

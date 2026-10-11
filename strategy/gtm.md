# FDE Go-to-Market Strategy

**Status:** draft for board confirmation (issue FDE-1). Do not build or sell beyond the existing physio-clinic arrangement until approved.
**Founder constraints:** solo software engineer, Calgary AB, ~40 hrs/week for 90 days, ~$1,000 cash budget, no existing SMB contacts beyond one reference customer (a Calgary physio clinic).
**Inputs:** CMO market/competitive/compliance research ([research/gtm-research.md](../research/gtm-research.md), FDE-2) and CTO feasibility/cost research ([research/cto-feasibility.md](../research/cto-feasibility.md), FDE-3). Both are desk research — no businesses or people were contacted.

---

## 1. Target Segments

**Ranked candidates** (full detail in CMO research §1–2):

1. **AI front-desk ops for local, repeat-visit service businesses** — voice intake that fills patient/client forms, automated post-visit follow-up, and a *compliant* review-request flow. Anchored on the existing physio-clinic build; widenable to dental, chiropractic, massage/wellness, med spa, veterinary.
2. **Review/visibility growth for local SMBs generally** — not a separate bet. Same product, buyer, and price band as #1; treat as a positioning widener once #1 is proven, not a parallel motion.
3. **Airbnb host direct-booking sites** — weak third. Legitimate local host community, but core software is commoditized ($15–100+/mo, 6+ funded national players) and Calgary's April 2025 short-term-rental licensing bylaw caps growth in the non-primary-residence host segment most likely to pay.
4. **Realtor portfolio/lead-gen sites** — not recommended now. CREB's IDX/MLS data-licensing terms are an unresolved, uncosted barrier; the category is the most saturated and highest-CAC of the four; AI features are already being commoditized by incumbents.

**Why #1 wins:** it's the only candidate where the founder already has a working product, a live reference customer, and a provable warm-referral path. The CTO assessment independently confirms it's also the best use of the $1k/90-day budget — the build already exists, so the budget goes to productization and widening, not invention (CTO research §1, §"Recommendation").

### Ideal Customer Profile (segment #1)

- Calgary-based, owner-operated local service business: physiotherapy, chiropractic, dental, massage/wellness, med spa, or veterinary clinic. 1–5 locations, 2–15 staff.
- High-frequency repeat-visit model (one-time-transaction businesses get little value from a follow-up cadence).
- Manual/error-prone intake today (paper forms, phone tag, no-shows) and inconsistent Google review velocity vs. visible local competitors.
- Owner or office manager handles marketing/ops personally — the buyer is reachable directly and can decide fast, with no procurement layer.
- Comfortable with some booking/EMR software already, but hasn't adopted AI tooling.
- Values time saved and client experience over lowest price. Realistic budget: $100–300/mo per location (supported directly by comps: NiceJob $75–125, EmbedMyReviews $99, Weave $199–599+, Birdeye $299–449 — CMO research §1.1).

Calgary alone has 200+ listed physiotherapy clinics plus many more adjacent wellness businesses (Medimap/Cortico directories) — a large local prospect pool before even widening to other verticals.

---

## 2. Problems & Offer

**Clearest-ROI AI use cases for this segment:**
- Voice-based patient/client intake that auto-fills forms and saves a profile — removes paperwork and front-desk time.
- Automated, personalized post-visit follow-up messaging (SMS/email).
- A **compliant** review-growth flow: timely, uniform review-link reminders; the customer writes their own review in their own words (see §5 on why this changed from the original "AI drafts, customer approves" design).

**Offer ladder:**
1. **Pilot/setup service (services-first)** — manually onboard 2–3 more clinics using the existing single-tenant build, configured per client, before investing in multi-tenancy. One-time setup fee + first month, e.g. $300–500 setup + $150–250/mo. Validates demand before any further build spend (CTO research §1, "Services-first viable?").
2. **Recurring SaaS (post-validation)** — once 2–3 pilots are running and demand is confirmed, invest 2–4 weeks productizing into a thin multi-tenant "AI front-desk" product (per-clinic config, auth, data isolation). Target $100–300/mo per location, bundling intake + follow-up + compliant review requests as one pipeline rather than separate products (CTO research, "Proposed minimal first SaaS product").
3. **Vertical widening** — once the core product is multi-tenant, each adjacent vertical (dental, chiro, salons) is roughly 1 week of intake-schema and prompt changes, not a new build.

**Pricing hypotheses** (to validate, not committed):
- $100–300/mo per location, informed by direct competitor comps spanning $75–600/mo/location.
- One-time setup/onboarding fee ($300–500) for white-glove pilots, waived or reduced once self-serve onboarding exists.
- Add-on pricing for the standalone review/visibility flow if sold to businesses that don't need intake automation (e.g., salons, retail) — lower price band, ~$50–150/mo, given it's the simplest and lowest-cost-to-run candidate (CTO research §2).

---

## 3. Competition & Positioning

- **No direct Calgary competitor** runs this exact bundle (voice intake + follow-up + compliant review growth) for local clinics today. One vendor's "Calgary" SEO pages cite the wrong province's privacy law — a sign of generic programmatic marketing, not real local presence (CMO research §1.1).
- **National incumbents** (Podium, Birdeye, NiceJob, Weave, Tebra/PatientPop) sell review/communication tooling broadly into clinics at $75–600/mo/location, but their "AI" features draft the *business's reply* to a review, not the review itself — not the same product.
- **Jane App** (Canadian physio practice management) covers booking/intake but has no review-automation or AI-draft features — complementary, not competitive.
- **Why FDE wins locally:** a live, working reference customer and case study (rare for a brand-new entrant); a founder who can sell, configure, and support in person in Calgary; a narrower, cheaper, more personal offer than the $300–600/mo enterprise-flavored incumbents; and the flexibility to bundle intake + follow-up + review-growth as one pipeline instead of three separate purchases.
- **Positioning:** "The AI front desk for Calgary's independent clinics — built by the person who runs it, proven at [reference clinic]." Not competing on feature breadth with Podium/Birdeye; competing on being local, personal, and anchored to a real result.

---

## 4. Channels & Sales Motion

First-10-customers motion (CMO research §3, concrete and Calgary-specific):

1. **Warm referral chain from the reference physio clinic** (highest priority). Ask the clinic owner for 3–5 introductions to other clinic owners they know personally.
2. **Attend 2–3 local events/month** to meet owner-operators and collect names for warm outreach (not to pitch cold): Calgary Chamber of Commerce "Business After Hours," Exmerce Business Owner Mastermind Networking (500+ local businesses), Calgary Entrepreneurs Network, Calgary Business Network.
3. **Seed inbound interest** by posting the physio case study (with the clinic's permission) in the "Calgary Business Group" and "Linking Calgary" LinkedIn groups.
4. **AI Tinkerers Calgary** (Platform Calgary) — not a direct customer channel, but useful for credibility and collaborator/referral discovery.
5. **Prioritized prospect list** from Medimap/Cortico directories (200+ Calgary physio clinics, plus adjacent multidisciplinary clinics) — for referral-anchored outreach only, once a few live customers can vouch. Never cold-blast.

Draft outreach scripts (cold email, cold DM, warm-referral in-person pitch) are in [research/gtm-research.md §4](../research/gtm-research.md#4-draft-outreach-scripts-drafts-only--do-not-send-board-reviews-and-sends-manually). **These are drafts only — the board reviews and sends/says them manually. No agent contacts any business or person.** All three scripts already reflect the compliant review-request framing from §5 below (private follow-up + link, customer writes their own review — not "AI writes your reviews").

---

## 5. Compliance: AI-Drafted Reviews Must Change Before Further Sales

The board flagged this explicitly, and the CMO research (§5) confirms it's a real, avoidable risk — not a false alarm:

- **Google policy:** bans "fake engagement" and "attempting to influence... the contents of the review." The current physio-clinic flow (AI drafts review text, patient approves and posts) sits in tension with that — approval is not the same as authorship, and Google's clearest AI-specific rule (in Merchant Center) bans reviews "primarily generated by an automated program or artificial intelligence application."
- **Canadian Competition Act:** anyone who writes or *permits the writing of* a misleading review can be liable; a misleading general impression is enough. Risk is lower here than outright employee ghostwriting (the patient is real, the visit is real), but rises if the AI invents specifics the patient didn't say.
- **Verdict:** gray zone, moderate and avoidable risk — not a clean violation, but not safe to scale or use as the core sales pitch as-is.

**Required change before this is sold to any new customer:** move AI from *review author* to *review facilitator*:
1. AI drafts a **private** post-visit follow-up message (not public review text), sent to **every** patient uniformly — no sentiment-based gating.
2. The patient writes their **own** review in their own words. AI never supplies draft text to approve-and-post.
3. No incentives tied to leaving a review; no requests to edit/remove negative reviews.

**Action item:** update the reference clinic's existing workflow to this model, and verify today whether the current flow solicits all patients uniformly or only likely-happy ones (selective solicitation/"review gating" is a separate, explicit Google violation that wasn't confirmed either way in desk research). Do this before using the review feature as a sales point with any new customer.

---

## 6. CTO Input: Minimal Product, Build-vs-Buy, Cost

(Full detail: [research/cto-feasibility.md](../research/cto-feasibility.md), FDE-3)

- **Not greenfield.** A single-tenant version already exists for one clinic. Productizing into multi-tenant (per-clinic config, auth, data isolation) is **2–4 weeks** solo; each additional vertical (dental, chiro, salons) is **~1 week** once the core exists.
- **Build vs. buy:** buy voice-to-text (Whisper API/Deepgram/AssemblyAI) and messaging (Twilio/Postmark/Resend); build the thin LLM layer that extracts structured form data and drafts follow-ups — that's the actual IP.
- **Ongoing cost at 5–10 pilot clinics: ~$70–200/mo total** (hosting, transcription, LLM, SMS/email — all estimates, not quotes).
- **Services-first is viable and recommended**: manually extend the existing single-tenant build to 2–3 more clinics before paying the multi-tenancy cost. Defers productization spend until there's repeat demand signal.
- **Key technical risk — PHI/privacy:** patient intake data likely qualifies as personal health information (PIPEDA, possibly Alberta's Health Information Act). Needs encryption, access controls, a retention/deletion policy, and likely Canadian data residency. **The CTO recommends explicit legal review before handling PHI across multiple clinics** — flagged to the board, not decided unilaterally. This gates widening beyond clinics already comfortable with the current single-tenant arrangement.
- **Minimal first SaaS product (post-validation):** one bundled "AI front-desk" tool — voice intake + follow-up + compliant review requests as a single pipeline — not three separate products. This also diversifies risk: if clinics stall on PHI concerns, the same core product (minus patient-form-filling) still serves salons and other appointment-based businesses with no PHI complication.

---

## 7. Validation Plan (Next 30 Days)

Cheap experiments, in order, each gated on the prior one producing a positive signal:

1. **Fix the compliance gap (week 1, before anything else is sold).** Update the reference clinic's review flow to the compliant model in §5. Confirm whether current solicitation is uniform or sentiment-gated. *Success: workflow updated and confirmed compliant; no new customer is pitched the old "AI-drafted review" framing.*
2. **3–5 warm introductions from the reference clinic (week 1–2).** Ask the clinic owner directly. *Success: at least 3 intro conversations booked.*
3. **5–10 discovery conversations with introduced clinic owners (week 2–3).** Validate the ICP assumptions in §1: manual intake pain, review-velocity gap, willingness to pay $100–300/mo. Not a pitch — a listening interview. *Success criteria: at least 3 of 5–10 confirm the pain and would consider paying within the stated range.*
4. **1–2 paid pilot clinics signed on the services-first offer (week 3–4).** White-glove setup using the existing single-tenant build, per §2 offer #1. *Success: 1–2 signed pilots with a setup fee or first month paid — real money changing hands, not a free trial.*
5. **Attend 2 local networking events** (Business After Hours, Exmerce, or Calgary Entrepreneurs Network) to build the warm-referral pipeline beyond the first clinic. *Success: 5+ new owner-operator contacts collected for future warm outreach.*
6. **PHI/privacy legal check (parallel, week 1–2).** Get a basic read (even informal) on PIPEDA/Alberta HIA obligations before pilot #2 or #3 touches patient data at a new clinic. *Success: a documented answer, even if "proceed with caution and X safeguard," not silence.*

**Do not build the multi-tenant product until at least 2 paid pilots confirm demand** (step 4) — per the issue's explicit instruction not to build product before plan approval, and the CTO's recommendation to defer productization cost until repeat demand is signaled.

---

## 8. Targets & Metrics

| Milestone | Target | Timeframe |
|---|---|---|
| Compliance fix shipped on reference clinic | Done, confirmed uniform solicitation | Week 1 |
| Warm introductions from reference clinic | 3–5 | Week 1–2 |
| Discovery interviews with clinic owners | 5–10 | Week 2–3 |
| Interviews confirming pain + willingness to pay | ≥3 of 5–10 | Week 3 |
| Paid services-first pilots signed | 1–2 | Week 3–4 |
| New warm contacts from networking events | 5+ | Week 4 |
| PHI/privacy legal read obtained | 1 (documented) | Week 2 |
| **90-day target** | 3–5 paying clinics on services-first or early SaaS pricing; multi-tenant build started only if ≥2 pilots confirm demand | Day 90 |
| **MRR goal (90 days)** | $500–1,200 MRR (3–5 clinics × $150–300/mo-equivalent, mix of setup fees and recurring) | Day 90 |

Tracking: a simple spreadsheet (or the `research/` directory) logging interview outcomes, pilot status, and MRR — no new tooling needed at this stage.

---

## 9. Board Actions Needed

1. **Approve or amend this plan** (segment choice, offer, validation plan, targets) via the plan confirmation request on this issue.
2. **Confirm the compliance fix (§5)** before any new customer is pitched the review feature — this can proceed immediately, it doesn't need to wait on the full plan approval.
3. **Decide who asks the reference clinic for introductions** — founder (board) does this personally; no agent contacts the clinic.
4. **Get an informal PHI/privacy read** (§6, §7 step 6) — likely the founder's own research or a short paid consult; flag if budget is needed beyond the $1k already allocated.
5. **Review and personally send/say the draft outreach scripts** ([research/gtm-research.md §4](../research/gtm-research.md#4-draft-outreach-scripts-drafts-only--do-not-send-board-reviews-and-sends-manually)) — no agent sends these.
6. **Approve moving to the multi-tenant SaaS build** only after ≥2 paid pilots confirm demand (§7, §6) — flagged back to the board at that point, not decided by agents.

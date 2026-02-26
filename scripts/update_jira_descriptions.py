import csv
import re

# ─── EVENT TYPE MAP ────────────────────────────────────────────────────────────
EVENT_TYPES = {
    "Dunham Summit":                       "conf_speaking",
    "Pastors Retreat (1)":                 "retreat",
    "NRB Convention":                      "conf_speaking_booth",
    "April Event (TBD)":                   "sports_vip",
    "America Reads the Bible":             "conf_attendance",
    "MegaMetro":                           "conf_attendance",
    "Outcomes Conference":                 "conf_speaking_booth_premier",
    "May Event (TBD)":                     "sports_vip",
    "America Prays National Mall":         "faith",
    "June Event (TBD)":                    "sports_vip",
    "SBC VIP Event":                       "sports_vip_hosted",
    "BCI Conference":                      "conf_sponsor",
    "Pastors Retreat (2)":                 "retreat",
    "Q3 Sporting Event July (TBD)":        "sports_vip",
    "Q3 Sporting Event September (TBD)":   "sports_vip",
    "Family Reunion":                      "conf_attendance",
    "November Sporting Event (TBD)":       "sports_vip",
}

EVENT_LOCATIONS = {
    "Dunham Summit":                       "Lake Buena Vista, FL",
    "Pastors Retreat (1)":                 "San Diego, CA",
    "NRB Convention":                      "Nashville, TN",
    "April Event (TBD)":                   "Dallas, TX",
    "America Reads the Bible":             "Washington, D.C.",
    "MegaMetro":                           "Boston, MA",
    "Outcomes Conference":                 "Dallas, TX — Hyatt Regency DFW International Airport",
    "May Event (TBD)":                     "Houston, TX",
    "America Prays National Mall":         "Philadelphia, PA",
    "June Event (TBD)":                    "Dallas, TX",
    "SBC VIP Event":                       "Orlando, FL",
    "BCI Conference":                      "Atlanta, GA",
    "Pastors Retreat (2)":                 "TBD",
    "Q3 Sporting Event July (TBD)":        "TBD",
    "Q3 Sporting Event September (TBD)":   "TBD",
    "Family Reunion":                      "TBD",
    "November Sporting Event (TBD)":       "Dallas, TX",
}

PHASE_NAMES = {
    1: "Phase 1: Mission & Strategy",
    2: "Phase 2: Theme & Audience",
    3: "Phase 3: Systems & Planning",
    4: "Phase 4: Final Prep",
    5: "Phase 5: Execution",
    6: "Phase 6: Follow-up",
    7: "Phase 7: ROI Analysis",
}

# ─── CHECKLISTS BY EVENT TYPE AND PHASE ───────────────────────────────────────
CHECKLISTS = {

    # ── CONFERENCE: SPEAKING ONLY (Dunham Summit) ───────────────────────────
    "conf_speaking": {
        1: [
            "Define primary objective for the conference (leads, awareness, or partnerships)",
            "Set target MQLs, SQLs, and post-session meetings",
            "Define speaking session CTA and desired audience action",
            "Confirm budget allocation and minimum ROI threshold",
            "Get faith alignment sign-off from leadership",
            "Assign event owner and primary speaking lead",
        ],
        2: [
            "Align session messaging with the Dunham Summit audience profile",
            "Identify ICP personas most likely to be in the room",
            "Draft full presentation outline and key talking points",
            "Design handouts, leave-behinds, or post-session digital resources",
            "Build a targeted pre-conference outreach list for expected attendees",
            "Get content and messaging sign-off from leadership",
        ],
        3: [
            "Configure HubSpot to capture leads from the speaking session",
            "Build the run-of-show and timeline for the speaking slot",
            "Coordinate all session logistics with the Dunham Summit organizer",
            "Test and finalize slide deck, A/V setup, and contingency plan",
            "Confirm travel and accommodation for the speaking team",
        ],
        4: [
            "Complete final run-through and rehearsal of the full presentation",
            "Confirm all session logistics with the organizer (time, room, A/V)",
            "Assign an on-site support owner to handle logistics day-of",
            "Prepare post-session follow-up links and resource delivery mechanism",
            "Get final creative and content sign-off",
        ],
        5: [
            "Arrive early — confirm A/V, clicker, and stage setup are working",
            "Deliver the speaking session as prepared",
            "Facilitate Q&A and engage with the audience",
            "Collect contact info and leads from session attendees",
            "Flag the top 5 hottest prospects for same-day follow-up",
        ],
        6: [
            "Upload all session leads to HubSpot within 48 hours",
            "Send personalized follow-up emails referencing the session content",
            "Activate the post-event nurture sequence in HubSpot",
            "Brief the sales team on high-priority prospects to contact",
            "Share the session recording or deck with attendees if available",
        ],
        7: [
            "Pull the 30-day MQL and pipeline report tied to Dunham Summit leads",
            "Calculate speaking ROI vs. the event investment",
            "Document session performance: attendance, leads, and conversions",
            "Deliver the 60-day and 90-day funnel updates to leadership",
            "Use data to evaluate Dunham Summit for future year investment",
        ],
    },

    # ── CONFERENCE: BOOTH + SPEAKING (NRB Convention) ───────────────────────
    "conf_speaking_booth": {
        1: [
            "Define primary objectives: lead generation, meetings booked, brand visibility",
            "Set MQL, SQL, and deal targets for the event",
            "Define booth CTA and speaking session CTA",
            "Confirm booth/sponsorship budget and minimum ROI threshold",
            "Get faith alignment sign-off from leadership",
            "Assign booth owner, speaking lead, and full team roster",
        ],
        2: [
            "Develop booth messaging, tagline, and visual concept",
            "Align speaking presentation messaging with booth theme",
            "Define ICP personas attending the conference",
            "Build the pre-conference outreach and meeting-booking target list",
            "Get approval on booth graphics, slide decks, demos, and handouts",
            "Launch the pre-event email sequence and meeting-booking campaign",
        ],
        3: [
            "Integrate HubSpot with badge scanner for seamless lead capture",
            "Set up event tracking with UTM parameters for all links",
            "Build detailed run-of-show covering booth hours and speaking sessions",
            "Test the full lead capture workflow from badge scan to CRM entry",
            "Confirm the meeting booking system is live and linked to team calendars",
            "Finalize booth shipping logistics and confirm setup window",
        ],
        4: [
            "Brief and train all booth staff on messaging, goals, and lead qualification",
            "Activate meeting booking links and confirm the full on-site schedule",
            "Confirm all booth materials, demos, and giveaways have shipped",
            "Assign on-site owner and designate a backup in case of emergency",
            "Walk through the run-of-show one final time with the full team",
            "Get creative, strategic, and operations sign-off on all assets",
        ],
        5: [
            "Set up booth on arrival — confirm all materials are present and functional",
            "Run morning check-ins each day to hit daily lead and meeting targets",
            "Capture all leads via badge scanner and ensure CRM sync is working",
            "Deliver all scheduled speaking sessions",
            "Flag hot prospects in real time and brief the team each evening",
            "Nightly team debrief: recap leads, hot prospects, and next-day priorities",
        ],
        6: [
            "Upload all event leads to HubSpot within 48 hours of event close",
            "Send personalized follow-up emails to hot leads within 72 hours",
            "Activate the full post-event nurture sequence in HubSpot",
            "Share the event debrief and top prospect list with the sales team",
            "Flag SQL-ready leads for immediate SDR outreach",
        ],
        7: [
            "Pull the 30-day MQL, SQL, and pipeline report from event leads",
            "Calculate total event ROI vs. all-in budget",
            "Deliver 60-day and 90-day funnel updates to leadership",
            "Document booth performance, session outcomes, and lessons learned",
            "Share the final ROI report and evaluate conference for next year",
        ],
    },

    # ── CONFERENCE: BOOTH + SPEAKING — PREMIER (Outcomes Conference) ────────
    "conf_speaking_booth_premier": {
        1: [
            "Define primary objectives: lead gen, meetings booked, ministry brand elevation",
            "Set MQL, SQL, and deal targets for the Outcomes Conference",
            "Define speaking CTAs for Max Bard (AI content) and Ryan Beck (AI ministry)",
            "Confirm Premier sponsorship at $34,850 and minimum ROI threshold",
            "Get faith alignment sign-off from leadership",
            "Assign Grand Foyer booth owner, speaking leads, and team roster",
        ],
        2: [
            "Develop Grand Foyer booth messaging, theme, and visual concept (conference theme: 'Multiply')",
            "Finalize Max Bard session: 'AI Secrets for Creating Cinematic Content' (Marketing & Communications track)",
            "Finalize Ryan Beck session: 'AI for Ministry Leaders' (Internet & Technology track)",
            "Define ICP personas: nonprofit execs, ministry leaders, church administrators",
            "Import CLA attendee list into HubSpot and build pre-event outreach sequence",
            "Approve booth graphics, session slide decks, and handout materials",
            "Launch pre-conference email and meeting-booking campaign",
            "ACTION REQUIRED: Blog post deadline was Jan 30 — contact Donna Bostick to confirm status",
            "ACTION REQUIRED: Program ad artwork deadline was Feb 20 — contact Donna Bostick to confirm status",
        ],
        3: [
            "Integrate HubSpot with badge scanner for Grand Foyer booth lead capture",
            "Configure event tracking and UTM parameters for all pre-event links",
            "Build run-of-show: booth hours, speaking sessions, and Grand Opening Reception",
            "Test full lead capture workflow from badge scan to CRM entry",
            "Confirm meeting booking system is live for Apr 28–30",
            "Finalize and ship all booth materials to Hyatt Regency DFW International Airport",
            "Confirm all 4 full-conference registrations are reserved and active",
        ],
        4: [
            "Brief and train all 4 booth personnel on messaging and lead qualification goals",
            "DEADLINE: Register all booth personnel by April 1",
            "Confirm Grand Opening Reception attendance (Apr 28, 5:30–7 PM)",
            "Activate meeting booking links and finalize the full Apr 28–30 schedule",
            "Confirm all booth materials and giveaways have arrived at Hyatt DFW",
            "Assign on-site booth owner and designate a backup",
            "Get creative, strategic, and operations sign-off on all assets",
        ],
        5: [
            "Booth load-in: Apr 28, 8 AM–4 PM at Grand Foyer, Hyatt Regency DFW",
            "Attend Grand Opening Reception: Apr 28, 5:30–7 PM — prioritize key prospect conversations",
            "Max Bard: Deliver 'AI Secrets for Creating Cinematic Content' — Tue Apr 28, 2:00–3:30 PM",
            "Ryan Beck: Deliver 'AI for Ministry Leaders' — Wed Apr 29, 10:30 AM–12:00 PM",
            "Staff Grand Foyer booth: Wed Apr 29 (10 AM–5:30 PM), Thu Apr 30 (10 AM–2 PM)",
            "Capture all leads via badge scanner — confirm CRM sync daily",
            "Flag hot prospects in real time and share priority list with team nightly",
            "Begin booth teardown: Thu Apr 30, 2–6 PM",
        ],
        6: [
            "Upload all booth and session leads to HubSpot within 48 hours",
            "Send personalized follow-up emails to hot leads within 72 hours",
            "Activate post-event nurture sequence in HubSpot",
            "Contact Donna Bostick (Donna.Bostick@ChristianLeadershipAlliance.org) to confirm post-conference attendee list",
            "Share post-event debrief and speaking session highlights with the sales team",
            "Flag SQL-ready leads for immediate SDR outreach",
        ],
        7: [
            "Pull 30-day MQL, SQL, and pipeline report from Outcomes Conference leads",
            "Calculate Premier sponsorship ROI vs. $34,850 investment",
            "Deliver 60-day and 90-day funnel updates to leadership",
            "Document Grand Foyer booth traffic, session attendance, and lead quality",
            "Share the final ROI report with leadership",
            "Evaluate Premier sponsorship renewal for TOC 2027",
        ],
    },

    # ── CONFERENCE: ATTENDANCE / TBD PARTICIPATION ──────────────────────────
    # (America Reads the Bible, MegaMetro, Family Reunion)
    "conf_attendance": {
        1: [
            "Define conference objective: leads, awareness, or relationship building",
            "Confirm participation format (attending, co-sponsoring, or speaking)",
            "Set success targets: MQLs, meetings booked, and key contacts made",
            "Confirm budget and get leadership approval",
            "Get faith alignment sign-off",
            "Assign event owner and attending team",
        ],
        2: [
            "Align PRAY.COM messaging with the specific conference audience",
            "Define ICP profile and lead qualification criteria for this event",
            "Prepare conference-appropriate materials, handouts, and collateral",
            "Build a pre-conference outreach list of expected attendees",
            "Get all messaging and materials reviewed and approved",
        ],
        3: [
            "Configure HubSpot to capture leads and track interactions at the event",
            "Finalize travel, hotel, and on-site logistics for the attending team",
            "Confirm any sponsorship deliverables or session commitments due to organizer",
            "Build a daily schedule and run-of-show for the attending team",
        ],
        4: [
            "Confirm final staffing and designate the on-site owner",
            "Pack or ship all materials, handouts, and branded items",
            "Brief the attending team on messaging, goals, and lead qualification criteria",
            "Confirm any pre-scheduled meetings or booking slots",
        ],
        5: [
            "Attend all relevant sessions and actively represent PRAY.COM",
            "Capture qualified leads and hold meaningful conversations with ICP contacts",
            "Log key contact notes in real time or immediately after each session",
            "Flag top prospects for immediate post-event follow-up",
        ],
        6: [
            "Upload all leads and contacts to HubSpot within 48 hours",
            "Activate the post-event nurture sequence",
            "Send personalized follow-up messages to every key contact",
            "Share the conference debrief and top contact list with the sales team",
        ],
        7: [
            "Pull 30-day report on leads, meetings booked, and pipeline created",
            "Calculate event ROI vs. total conference investment",
            "Document key insights, standout contacts, and recommendations",
            "Deliver the final event performance summary to leadership",
        ],
    },

    # ── CONFERENCE: SPONSOR ONLY (BCI Conference) ────────────────────────────
    "conf_sponsor": {
        1: [
            "Define sponsorship objective: brand reach, relationship building, or leads",
            "Confirm BCI Conference sponsorship tier and full list of deliverables",
            "Set measurable success metrics: impressions, leads, or key relationships",
            "Confirm $15,000 sponsorship budget and get leadership approval",
            "Get faith alignment sign-off from leadership",
            "Assign sponsorship owner and attending team member(s)",
            "NOTE: BCI Conference (Jun 19–20, Atlanta) conflicts with June Event (Jun 19–21, Dallas) — plan team split now",
        ],
        2: [
            "Adapt PRAY.COM brand messaging to fit the BCI Conference audience and tone",
            "Confirm expected audience size, key attendee profiles, and reach",
            "Prepare or adapt all brand assets for sponsor placements",
            "Identify target attendees for direct relationship building",
        ],
        3: [
            "Deliver all required sponsorship assets to the BCI organizer by their deadline",
            "Define PRAY.COM's CTA or lead capture mechanism at the event",
            "Secure any pre-event or post-event touchpoints with BCI organizers",
            "Confirm travel and logistics for attending team members",
            "Coordinate with June Event team on the split-team logistics plan",
        ],
        4: [
            "Confirm all sponsorship assets are correctly placed and live",
            "Set up attribution tracking for any PRAY.COM CTAs or links at the event",
            "Brief attending team on relationship targets, goals, and messaging",
            "Finalize the June Event / BCI split-team assignments",
        ],
        5: [
            "Attend the BCI Conference and represent the PRAY.COM sponsorship presence",
            "Engage with key attendees and nonprofit or ministry leaders",
            "Capture and log contact notes for any new relationships",
            "Confirm sponsor deliverables (signage, digital mentions, stage mentions) are fulfilled",
        ],
        6: [
            "Follow up with every key contact from BCI Conference within 48 hours",
            "Upload all new contacts to HubSpot",
            "Activate a targeted post-event follow-up sequence for warm relationships",
        ],
        7: [
            "Measure brand reach, audience impressions, and sponsor deliverable fulfillment",
            "Calculate sponsorship ROI vs. $15,000 investment",
            "Evaluate relationship outcomes against the original objectives",
            "Deliver the post-event sponsorship summary to leadership",
        ],
    },

    # ── PASTORS RETREATS (1 & 2) ─────────────────────────────────────────────
    "retreat": {
        1: [
            "Define retreat purpose and spiritual/relationship objectives",
            "Set attendance target and guest qualification criteria",
            "Confirm $80,000 budget and get the ROI framework approved",
            "Document faith guardrails and hospitality standards for the experience",
            "Assign retreat owner and planning team",
            "Begin venue research and create a shortlist of 2–3 options",
        ],
        2: [
            "Finalize retreat theme, visual identity, and invitation tone",
            "Build the finalized ICP guest list of qualified pastors and ministry leaders",
            "Develop a personalized invitation strategy and outreach plan",
            "Finalize messaging, copy, and design for all invitation materials",
            "Send invitations and track RSVPs in HubSpot",
        ],
        3: [
            "Configure HubSpot for full guest tracking and RSVP management",
            "Build a detailed run-of-show and session schedule for the retreat",
            "Execute venue contract and lock the room block",
            "Confirm all vendors: A/V, catering, activities, and transportation",
            "Finalize critical path and risk register",
            "Coordinate travel, ground transportation, and room assignments for all guests",
        ],
        4: [
            "Finalize the complete on-site experience flow: sessions, meals, and activities",
            "Lock the staffing plan and assign each team member their role",
            "Confirm all guest travel and accommodation details are set",
            "Prepare and ship all on-site materials, gifts, and branded collateral",
            "Send the final retreat confirmation and detailed itinerary to every attendee",
            "Get strategic, creative, and operations sign-off",
        ],
        5: [
            "Personally welcome and onboard each attendee upon arrival",
            "Execute all sessions and activities per the run-of-show",
            "Capture detailed conversation notes for every attendee throughout the retreat",
            "Identify high-priority relationship moments to highlight in follow-up",
            "Team debrief each evening — review the day and adjust the next-day plan",
        ],
        6: [
            "Send personalized, tailored thank-you notes to every attendee within 48 hours",
            "Activate the 90-day post-retreat nurture sequence in HubSpot",
            "Upload all attendees with detailed context and conversation notes to CRM",
            "Identify the top retreat-to-pipeline opportunities",
            "Schedule follow-up discovery or check-in calls with warm prospects",
        ],
        7: [
            "Pull the 30/60/90-day pipeline and revenue report tied to retreat attendees",
            "Calculate cost per qualified relationship built",
            "Document retreat outcomes, attendee feedback, and key highlights",
            "Deliver the full ROI and relationship impact report to leadership",
        ],
    },

    # ── SPORTS / VIP EVENTS ──────────────────────────────────────────────────
    # (April, May, June Events, Q3 July, Q3 Sep, November)
    "sports_vip": {
        1: [
            "Define event purpose and VIP relationship objectives",
            "Confirm or select the specific sporting event, venue, and date",
            "Set attendance target (~18–23 VIP guests) and guest list criteria",
            "Confirm $30,000 budget and get leadership approval",
            "Document faith guardrails and hospitality standards",
            "Assign event owner and host team",
        ],
        2: [
            "Build the finalized VIP guest list in HubSpot with priority tiers",
            "Draft personalized invitation messaging for each guest or segment",
            "Confirm invite format: digital, physical, or hybrid",
            "Align branded visuals and experience theme for the event",
            "Send invitations and track all RSVPs in HubSpot",
        ],
        3: [
            "Purchase or confirm ticket block, suite, or VIP access",
            "Finalize all logistics: transportation, parking, catering, and hospitality setup",
            "Configure HubSpot for guest tracking and post-event follow-up",
            "Define specific conversation goals or a natural CTA for each key guest",
            "Build a detailed run-of-show for the event evening",
        ],
        4: [
            "Confirm final headcount and lock the VIP guest list",
            "Prepare branded guest experience materials and personalized gifts",
            "Assign a primary event host and on-site support staff",
            "Brief every team member on individual conversation goals for each guest",
            "Get final approval on all logistics, gifts, and the overall experience plan",
        ],
        5: [
            "Welcome each VIP guest personally upon arrival",
            "Execute hospitality and the guest experience per the run-of-show",
            "Capture key conversation notes for every guest in real time",
            "Identify pipeline opportunities and follow-up priorities on the spot",
            "Communicate PRAY.COM's mission and value naturally throughout the evening",
        ],
        6: [
            "Send personalized thank-you messages to every guest within 24 hours",
            "Activate the 90-day post-event nurture sequence in HubSpot",
            "Upload all guests with full conversation notes to CRM",
            "Flag guests ready for SDR or direct sales outreach",
            "Share the event debrief with the sales team within 48 hours",
        ],
        7: [
            "Pull the 30/60/90-day pipeline report tied to VIP event guests",
            "Calculate ROI vs. $30,000 event budget",
            "Document relationships built, pipeline created, and opportunities identified",
            "Share the final performance report with leadership",
        ],
    },

    # ── SBC VIP EVENT (Hosted — slightly unique) ─────────────────────────────
    "sports_vip_hosted": {
        1: [
            "Define the SBC VIP event purpose and relationship objectives",
            "Confirm SBC Annual Convention context: Jun 6–8, 2026, Orlando, FL",
            "Set attendance target (~23 VIP guests) and guest qualification criteria",
            "Confirm $32,200 budget and get leadership approval",
            "Document faith guardrails and hospitality standards",
            "Assign event owner and host team",
        ],
        2: [
            "Build the finalized VIP guest list targeting SBC church and ministry leaders",
            "Draft personalized invitation messaging tailored to the SBC leader audience",
            "Confirm invite format: digital, physical, or hybrid",
            "Align PRAY.COM visuals and experience theme for the SBC context",
            "Send invitations and track RSVPs in HubSpot",
        ],
        3: [
            "Finalize VIP venue: dinner, private experience, or hospitality event in Orlando",
            "Confirm all logistics: transportation, catering, parking, and hospitality setup",
            "Configure HubSpot for SBC VIP guest tracking and post-event follow-up",
            "Define specific conversation goals and a natural CTA for each target guest",
            "Build a detailed run-of-show for the SBC VIP event",
        ],
        4: [
            "Confirm final headcount and lock the VIP guest list",
            "Prepare branded guest experience materials and personalized gifts",
            "Assign primary event host and on-site support staff",
            "Brief every team member on individual conversation goals per SBC leader",
            "Get final approval on all logistics, gifts, and the event plan",
        ],
        5: [
            "Welcome each SBC VIP guest personally upon arrival",
            "Execute hospitality and the guest experience per the run-of-show",
            "Capture detailed conversation notes for every guest in real time",
            "Identify ministry connection moments and pipeline opportunities",
            "Communicate PRAY.COM's mission and value naturally throughout",
        ],
        6: [
            "Send personalized thank-you messages to every guest within 24 hours",
            "Activate the 90-day post-event nurture sequence in HubSpot",
            "Upload all SBC VIP guests with full conversation notes to HubSpot",
            "Flag warm leads ready for SDR or direct sales outreach",
            "Share the SBC event debrief with the sales team within 48 hours",
        ],
        7: [
            "Pull the 30/60/90-day pipeline report tied to SBC VIP guests",
            "Calculate ROI vs. $32,200 event budget",
            "Document ministry relationships built and church leader opportunities identified",
            "Deliver the final performance report to leadership",
        ],
    },

    # ── FAITH EVENT (America Prays National Mall) ────────────────────────────
    "faith": {
        1: [
            "Define PRAY.COM's awareness and ministry objectives for America Prays",
            "Confirm PRAY.COM's participation role, visibility level, and deliverables",
            "Set success metrics: reach, brand impressions, ministry alignment, and app downloads",
            "Confirm $50,000 budget and get leadership approval",
            "Document faith guardrails and brand standards for the event",
            "Assign event owner and attending team",
        ],
        2: [
            "Align PRAY.COM's messaging with the event's spiritual theme",
            "Identify key partner organizations and relationship-building opportunities",
            "Develop the full PRAY.COM presence strategy: stage, signage, digital, and app",
            "Finalize all creative assets for every event placement",
            "Get content and creative sign-off from leadership",
        ],
        3: [
            "Confirm all on-site logistics and PRAY.COM setup requirements with organizers",
            "Coordinate with event organizers on visibility placement and promotional opportunities",
            "Set up any digital engagement tools or PRAY.COM app push campaigns for attendees",
            "Build a detailed run-of-show for PRAY.COM's full on-site presence",
            "Finalize travel, logistics, and accommodation for the attending team",
        ],
        4: [
            "Confirm staffing and full on-site coverage plan for the event",
            "Finalize and ship all signage, collateral, and branded assets",
            "Confirm all partnership, visibility, and sponsorship deliverables are in order",
            "Brief the attending team on spiritual objectives and brand guidelines",
        ],
        5: [
            "Execute PRAY.COM's full presence and representation at the event",
            "Engage authentically with attendees, speakers, and ministry partners",
            "Capture photo and video content for post-event social and media use",
            "Document key relationships, spiritual moments, and ministry connections made",
        ],
        6: [
            "Share an event impact summary internally within 48 hours",
            "Follow up personally with every key ministry leader and partner",
            "Upload all new contacts to HubSpot",
            "Post a compelling event recap across PRAY.COM social and digital channels",
            "Send thank-you notes to event organizers and ministry partners",
        ],
        7: [
            "Document total brand reach, impressions, and media exposure from the event",
            "Assess alignment with PRAY.COM's ministry mission and spiritual values",
            "Report on key relationships and ministry moments from America Prays",
            "Deliver the post-event summary and brand impact report to leadership",
        ],
    },
}


# ─── HELPERS ──────────────────────────────────────────────────────────────────
def extract_event_and_phase(summary):
    match = re.match(r'^\[(.+?)\] Phase (\d):', summary)
    if match:
        return match.group(1), int(match.group(2))
    return None, None


def build_description(event_name, location, event_type, phase_num):
    phase_name = PHASE_NAMES[phase_num]
    items = CHECKLISTS[event_type][phase_num]
    checklist = "\n".join(f"[ ] {item}" for item in items)
    return f"Event: {event_name}\nLocation: {location}\n{phase_name}\n\nTo-Do:\n{checklist}"


# ─── MAIN ─────────────────────────────────────────────────────────────────────
CSV_PATH = "/Users/nayluchetti/Documents/GitHub/mktsaasevents/events/jira-import-2026-events.csv"

rows = []
with open(CSV_PATH, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        rows.append(row)

updated = 0
skipped = []
new_rows = []

for row in rows:
    summary = row[0]
    event_name, phase_num = extract_event_and_phase(summary)

    if event_name and phase_num:
        event_type = EVENT_TYPES.get(event_name)
        location   = EVENT_LOCATIONS.get(event_name, "TBD")

        if event_type and phase_num in CHECKLISTS.get(event_type, {}):
            new_desc = build_description(event_name, location, event_type, phase_num)
            new_rows.append([summary, new_desc, row[2], row[3], row[4], row[5]])
            updated += 1
        else:
            skipped.append(summary)
            new_rows.append(row)
    else:
        skipped.append(summary)
        new_rows.append(row)

with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    writer.writerows(new_rows)

print(f"Updated : {updated} rows")
print(f"Skipped : {len(skipped)}")
if skipped:
    for s in skipped:
        print(f"  - {s}")

---
name: propose-trade
description: This skill should be used when the user asks to "send the trade", "submit the trade offer", "propose the trade on Yahoo", "send him the offer", "make the trade official", "put the offer in", or wants an agreed trade actually transmitted on their fantasy platform. Drives the user's own logged-in browser session to build and send the offer - Yahoo first, with ESPN and Sleeper variants. Always pauses for explicit confirmation before sending. Not for judging whether the trade is good (trade-evaluation), finding a partner (trade-finder), or the negotiation itself (trade-negotiation).
---

# Propose Trade (Browser Playbook)

Transmit a finalized trade offer through the user's own logged-in browser session. One hard gate: **never click Send/Propose without explicit user confirmation.** Sending a trade is outward-facing — the other manager sees it immediately — so the gate here is absolute even if the user seemed sure earlier in the conversation.

## Ground rules (all roster-ops skills)

- **The user's session is the auth.** Never ask for, read, store, or type usernames, passwords, or 2FA codes. On a login page: stop, ask the user to log in themselves, resume after.
- **Navigate by goals and landmarks**, not memorized selectors — find controls by visible text ("Propose Trade", "Continue", "Send") and structure, and read the page when unsure.
- **Confirmation gate** before the send click. Building the offer on-screen is fair game.
- If no browser tooling is available in the session, say so and walk the user through the clicks.

## Phase 1: Confirm the terms

Before the browser: restate the full trade — every player (and pick, if the league trades picks) on both sides, and which team gets what. If the terms came out of a negotiation thread, quote the final agreed version. If the trade hasn't been pressure-tested, offer (don't insist) a quick trade-evaluation pass first. Ask whether to include a message to the other manager; if yes, draft 1–2 courteous sentences framing their gain (trade-negotiation style) for the user to approve or edit.

## Phase 2: Execute on Yahoo

1. **Get to the other team's page**: `fantasysports.yahoo.com` → the correct league (verify by league-name landmark) → find the opposing team via the League/standings or teams list → open their team page. Landmark: their team name in the header with their roster below.
2. **Open the trade flow**: find the **Propose Trade** control on their team page (button or under a "…"/actions menu). Landmark: a two-roster view — their players and yours — with checkboxes or select controls.
3. **Build the offer**: select the exact players from **their** roster the user is to receive, then the players from the **user's** roster to send. Cross-check every selection against Phase 1 — similar names and multiple same-position players make this the highest-risk step. Paste the approved note into the message box if there is one.
4. **Review screen**: Yahoo summarizes the offer (you give / you get, expiry date) before sending.
5. **⛔ CONFIRMATION GATE**: read the summary back verbatim — "You send Errol Fontaine and Dewey Sandoval to Turf Burns; you receive Oren Vasquez; offer expires in 14 days; note attached." Wait for an explicit yes. Only then click Send/Propose.
6. **Verify**: check the pending trades area (Yahoo shows outgoing offers on My Team/Transactions). Confirm the offer is listed with the right pieces; report it, plus how the user can cancel it later if needed.

## Platform variants

- **ESPN** (`fantasy.espn.com`): opposing team page → **Propose Trade** opens a checkbox list of both rosters → review step ends on **Send Trade Offer** — the gated click. Pending offers live under Transactions with a cancel option.
- **Sleeper** (`sleeper.com`): open the other team's roster → trade icon/**Propose Trade** → tap players on both sides → optional message → **Send Offer** is the gated click. Sleeper shows the pending trade in the league's trades view; note Sleeper leagues often have voting/review windows — set that expectation.

## Failure handling

- Can't find a Propose Trade control: the league's trade deadline may have passed or trading may be disabled — check for a deadline notice, report it, stop.
- A selected player is locked or ineligible (recently claimed, in another pending deal): the platform will block or warn — surface the message to the user verbatim rather than working around it.
- The review screen shows anything different from Phase 1 (extra player, wrong direction, unexpected expiry): stop and surface it — never send a variant the user hasn't approved word for word.
- The user hesitates at the gate: park the built offer unsent and summarize where things stand. An unsent trade costs nothing; a wrong one costs league trust.

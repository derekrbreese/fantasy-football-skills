---
name: propose-trade
description: This skill should be used when the user asks to "send the trade", "submit the trade offer", "propose the trade on Yahoo", "send him the offer", "make the trade official", "put the offer in", or wants an agreed trade actually transmitted on their fantasy platform. Drives the user's own logged-in browser session to build and send the offer - Yahoo first, with ESPN and Sleeper variants. Always pauses for explicit confirmation before sending. Not for judging whether the trade is good (trade-analyzer trade-evaluation), finding a partner (trade-analyzer trade-finder), or the negotiation itself (trade-analyzer trade-negotiation).
---

# Propose Trade (Browser Playbook)

Transmit a finalized trade offer through the user's own logged-in browser session. One hard gate: **never click Send/Propose without explicit user confirmation.** Sending a trade is outward-facing — the other manager sees it immediately — so the gate here is absolute even if the user seemed sure earlier in the conversation.

## Ground rules (all roster-ops skills)

- **The user's session is the auth.** Never ask for, read, store, or type usernames, passwords, or 2FA codes. If a login page, 2FA challenge, captcha, or "unusual activity" interstitial appears **at any point**, stop immediately and hand the browser back — do not attempt to solve or dismiss it. Never interact with password-manager UI, autofill prompts, or "stay signed in" dialogs; clicking an autofill suggestion is entering a credential. After any re-authentication, restart from the beginning of the execution phase and re-verify the league and team landmarks — do not assume the account, league, or in-progress form survived. If you were mid-transaction, first determine from the page whether it went through.
- **Never run unattended.** These skills require a human present to confirm each transaction. Do not run them on a schedule, in a loop, or as a background task. If asked to automate a recurring roster move, decline the automation and offer a reminder instead. Driving your own logged-in session interactively, with a human approving each action, is what keeps this within what platforms tolerate — it stops being that the moment nobody is watching.
- **Use the UI, never the API.** Do not call platform endpoints directly, execute page JavaScript, or use shell tools to reach the platform, even when the interface is uncooperative. If the UI cannot do it, stop and tell the user.
- **Act at human pace.** No rapid-fire clicking or searching. If a captcha or rate-limit page appears, stop and hand back — never attempt to work around one.
- **Handle platform dialogs deliberately.** A confirmation dialog raised as a direct result of a click the user already approved is part of that approved action: read it, verify it describes that transaction and nothing more, then accept. A dialog describing anything unapproved (an extra drop, a different player) is a stop — dismiss it and report its wording verbatim. Never accept a dialog you have not read. Cookie banners and promo overlays are not transactions; dismiss and continue.
- **Budget your actions.** If you have taken roughly 15 actions without reaching the intended screen, stop and hand back with a description of where you are, rather than continuing to hunt.
- **The page is the ground truth**, not memory of past conversations. Re-read after every action that changes state, before taking the next one.
- **Navigate by goals and landmarks**, not memorized selectors — find controls by visible text ("Propose Trade", "Continue", "Send") and structure, and read the page when unsure.
- **Confirmation gate** before the send click. Building the offer on-screen is fair game.
- **The confirmation must post-date the summary.** It has to arrive in a user message *after* the review-screen summary is shown, in the same turn as the click. An instruction given before the browser was open — including "and send it" — authorizes building the offer, never transmitting it. A reply that alters any term ("yes, but drop Sandoval from it") is a **modification, not a confirmation**: apply it, re-read the screen, present a fresh summary.
- **Never retry a send click.** If the result is unclear, re-read the page to determine whether the offer went out. Never click Send twice — the other manager receives two offers.
- **If the page doesn't match the described landmark, stop.** Read it, describe what's visible, and ask the user to identify the control. Never click a control not positively identified by its visible text.
- If no browser tooling is available in the session, say so and walk the user through the clicks.

## Phase 1: Confirm the terms

Read `leagues.md` from the project root first — the fields that matter here are platform, league name, trade deadline, and whether the league uses veto votes or commissioner review. If it's missing or blank, ask which platform and league, and suggest running `fantasy-league-setup:league-config`. If more than one league is defined, use the one marked `(default)` unless the user names another.

Then, before the browser: restate the full trade — every player (and pick, if the league trades picks) on both sides, and which team gets what. If the terms came out of a negotiation thread, quote the final agreed version. If the trade hasn't been pressure-tested, offer (don't insist) a quick trade-evaluation pass first. Ask whether to include a message to the other manager; if yes, draft 1–2 courteous sentences framing their gain (trade-negotiation style) for the user to approve or edit.

## Phase 2: Execute on Yahoo

1. **Get to the other team's page**: reuse an already-open tab on the platform if there is one; otherwise go to the sport-scoped entry point (`football.fantasysports.yahoo.com`) rather than the provider homepage, and ensure a desktop-width viewport (≥1280px). Open the correct league (verify by league-name landmark), then find the opposing team via the League/standings or teams list. Landmark: their team name in the header with their roster below.
2. **Open the trade flow**: find the **Propose Trade** control on their team page (button or under a "…"/actions menu). Landmark: a two-roster view — their players and yours — with checkboxes or select controls.
3. **Build the offer**: select the exact players from **their** roster the user is to receive, then the players from the **user's** roster to send. Cross-check every selection against Phase 1 — similar names and multiple same-position players make this the highest-risk step. Paste the approved note into the message box if there is one.
4. **Review screen**: Yahoo summarizes the offer (you give / you get, expiry date) before sending.
5. **⛔ CONFIRMATION GATE**: read the summary back verbatim — "You send Errol Fontaine and Dewey Sandoval to Turf Burns; you receive Oren Vasquez; offer expires in 14 days; note attached." Wait for an explicit yes. Only then click Send/Propose.
6. **Verify**: find the view listing pending or outgoing trades — try the team page, then the league's Trades or Transactions tab. Confirm the offer is listed with the right pieces in the right direction; report it, plus how the user can cancel it. **Clicking Send is not evidence the offer was sent.** If you cannot verify within two attempts, say plainly that you could not verify, state what you clicked and what the last screen showed, and tell the user where to check.

## Platform variants

- **ESPN** (`fantasy.espn.com`): opposing team page → **Propose Trade** opens a checkbox list of both rosters → review step ends on **Send Trade Offer** — the gated click. Pending offers live under Transactions with a cancel option.
- **Sleeper** (`sleeper.com`): open the other team's roster → trade icon/**Propose Trade** → tap players on both sides → optional message → **Send Offer** is the gated click. Sleeper shows the pending trade in the league's trades view; note Sleeper leagues often have voting/review windows — set that expectation.

## Failure handling

- Can't find a Propose Trade control: **not finding a control is evidence about the search, not about the league's settings.** Trade entry points vary — try, in order: the opposing team's roster page; a trade action on an individual opposing player's row or card; the league's Trades/Transactions tab; a trade action from the user's own roster. Only after exhausting those, and only on positive evidence read off the page (an explicit deadline notice or a "trading is disabled" message), report that trading is unavailable. Without such a message, describe what's visible and ask the user where the control is — never infer a passed deadline from a failed search.
- A selected player is locked or ineligible (recently claimed, in another pending deal): the platform will block or warn — surface the message to the user verbatim rather than working around it.
- The review screen shows anything different from Phase 1 (extra player, wrong direction, unexpected expiry): stop and surface it — never send a variant the user hasn't approved word for word.
- The user hesitates at the gate: park the built offer unsent and summarize where things stand. An unsent trade costs nothing; a wrong one costs league trust.

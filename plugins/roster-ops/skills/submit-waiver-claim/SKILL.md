---
name: submit-waiver-claim
description: This skill should be used when the user asks to "put in the claim", "submit my waiver claim", "claim him off waivers", "add him and drop X", "file the waiver for me", "place that bid on Yahoo", or wants a specific add/drop transaction executed on their fantasy platform. Drives the user's own logged-in browser session to file the claim - Yahoo first, with ESPN and Sleeper variants. Always pauses for explicit confirmation before submitting. Not for deciding who to target (waiver-scan), the bid amount (faab-bidding), or who to cut (drop-candidates).
---

# Submit Waiver Claim (Browser Playbook)

File a specific waiver claim or free-agent add in the user's own logged-in browser session. One hard gate: **never click the final submit without explicit user confirmation.**

## Ground rules (all roster-ops skills)

- **The user's session is the auth.** Never ask for, read, store, or type usernames, passwords, or 2FA codes. On a login page: stop, ask the user to log in themselves, resume after.
- **Navigate by goals and landmarks**, not memorized selectors — find controls by visible text ("Add", "Claim", "Continue") and page structure, and read the page when unsure.
- **Confirmation gate** before the click that files the transaction. Navigation, search, and opening the claim form are fair game.
- If no browser tooling is available in the session, say so and walk the user through the clicks instead.

## Phase 1: Assemble the claim

Collect before touching the browser — ask for whatever is missing:

1. **Player to add** (exact name; get team/position too — platforms list multiple players with similar names).
2. **Player to drop**, if the roster is full. Unsure → suggest running drop-candidates first.
3. **Bid amount**, if `leagues.md` says FAAB. Unsure → suggest running faab-bidding first.
4. Read `leagues.md` for platform, league, budget; note whether the player is likely on **waivers** (claim processes later, on the league's waiver day) vs. a **free agent** (add is immediate). Set that expectation with the user now — an "immediate" add that's actually a Wednesday claim surprises people.

## Phase 2: Execute on Yahoo

1. **Get to the league's player pool**: `fantasysports.yahoo.com` → the team for this league → **Players** in the team navigation. Landmark: a searchable player table with status/availability columns.
2. **Find the player**: use the search box with the exact name. Verify identity by name **and** NFL team/position before proceeding. Landmark: the player row shows an availability marker — "FA" (free agent) or "W" with a date (on waivers until then).
3. **Open the claim**: click the add/claim control (a "+" or "Add" on the player row). Yahoo walks a short flow: choose the **drop** player if the roster is full → enter the **FAAB bid** if applicable. Fill both from Phase 1.
4. **Review screen**: Yahoo shows a summary (add, drop, bid, process date) before finalizing.
5. **⛔ CONFIRMATION GATE**: read the summary back to the user verbatim — "Claim Silas Okafor (RB), drop Ironhogs DST, bid $37 of your $124, processes Wed" — and wait for an explicit yes. Only then click Submit/Confirm.
6. **Verify**: navigate to the pending claims area (Yahoo lists pending waiver claims on the My Team/Transactions page). Confirm the claim appears with the right players and bid; report it. Immediate FA adds: verify the player now appears on the roster instead.

## Platform variants

- **ESPN** (`fantasy.espn.com`): Players → **Add** tab; the flow asks for the drop first, then bid (FAAB leagues), ending on a review step with a **Submit** button — that's the gated click. Pending claims appear under the team's Transactions.
- **Sleeper** (`sleeper.com`): league → Players/Waivers tab; tapping a player opens their card with an **Add** button → select drop → enter bid on the claim sheet → **Submit Claim** is the gated click. Sleeper shows pending claims on the team's waivers screen with edit/cancel options — point the user there.

## Failure handling

- Player not found in search: check spelling and the league (multi-league accounts open the wrong team easily — verify the league-name landmark). The player may also be rostered already; check and report who has them.
- Bid exceeds remaining budget: the platform will reject it — reconcile the real remaining budget from the page (the page wins over leagues.md) and re-ask the user.
- Claim vs. add mismatch (expected FA, actually on waivers or vice versa): pause at the gate anyway and tell the user the actual processing time before they confirm.
- Anything on the review screen differs from what the user asked: stop and surface it — never "fix" a discrepancy silently.

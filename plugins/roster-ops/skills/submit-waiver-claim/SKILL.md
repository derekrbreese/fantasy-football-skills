---
name: submit-waiver-claim
description: This skill should be used when the user asks to "put in the claim", "submit my waiver claim", "claim him off waivers", "add him and drop X", "file the waiver for me", "place that bid on Yahoo", or wants a specific add/drop transaction executed on their fantasy platform. Drives the user's own logged-in browser session to file the claim - Yahoo first, with ESPN and Sleeper variants. Always pauses for explicit confirmation before submitting. Not for deciding who to target (waiver-wire waiver-scan), bid amounts (waiver-wire faab-bidding), or cut decisions (waiver-wire drop-candidates). This skill only executes a transaction the user has already decided on.
---

# Submit Waiver Claim (Browser Playbook)

File a specific waiver claim or free-agent add in the user's own logged-in browser session. One hard gate: **never click the final submit without explicit user confirmation.**

## Ground rules (all roster-ops skills)

- **The user's session is the auth.** Never ask for, read, store, or type usernames, passwords, or 2FA codes. If a login page, 2FA challenge, captcha, or "unusual activity" interstitial appears **at any point**, stop immediately and hand the browser back — do not attempt to solve or dismiss it. Never interact with password-manager UI, autofill prompts, or "stay signed in" dialogs; clicking an autofill suggestion is entering a credential. After any re-authentication, restart from the beginning of the execution phase and re-verify the league and team landmarks — do not assume the account, league, or in-progress form survived. If you were mid-transaction, first determine from the page whether it went through.
- **Never run unattended.** These skills require a human present to confirm each transaction. Do not run them on a schedule, in a loop, or as a background task. If asked to automate a recurring roster move, decline the automation and offer a reminder instead. Driving your own logged-in session interactively, with a human approving each action, is what keeps this within what platforms tolerate — it stops being that the moment nobody is watching.
- **Use the UI, never the API.** Do not call platform endpoints directly, execute page JavaScript, or use shell tools to reach the platform, even when the interface is uncooperative. If the UI cannot do it, stop and tell the user.
- **Act at human pace.** No rapid-fire clicking or searching. If a captcha or rate-limit page appears, stop and hand back — never attempt to work around one.
- **Handle platform dialogs deliberately.** A confirmation dialog raised as a direct result of a click the user already approved is part of that approved action: read it, verify it describes that transaction and nothing more, then accept. A dialog describing anything unapproved (an extra drop, a different player) is a stop — dismiss it and report its wording verbatim. Never accept a dialog you have not read. Cookie banners and promo overlays are not transactions; dismiss and continue.
- **Budget your actions.** If you have taken roughly 15 actions without reaching the intended screen, stop and hand back with a description of where you are, rather than continuing to hunt.
- **The page is the ground truth**, not memory of past conversations. Re-read after every action that changes state, before taking the next one.
- **Navigate by goals and landmarks**, not memorized selectors — find controls by visible text ("Add", "Claim", "Continue") and page structure, and read the page when unsure.
- **Confirmation gate** before the click that files the transaction. Navigation, search, and opening the claim form are fair game.
- **The confirmation must post-date the summary.** It has to arrive in a user message *after* the review-screen summary is shown, in the same turn as the click. An instruction given before the browser was open — including "and submit it" — authorizes building the claim, never filing it. A reply that alters any term ("yes, but make it $25") is a **modification, not a confirmation**: apply it, re-read the screen, present a fresh summary.
- **Never retry a submit click.** If the result is unclear, re-read the page to determine whether the claim was filed. Never click Submit a second time — a duplicate claim can spend the budget twice.
- **If the page doesn't match the described landmark, stop.** Read it, describe what's visible, and ask the user to identify the control. Never click a control not positively identified by its visible text.
- If no browser tooling is available in the session, say so and walk the user through the clicks instead.

## Phase 1: Assemble the claim

Collect before touching the browser — ask for whatever is missing:

1. **Player to add** (exact name; get team/position too — platforms list multiple players with similar names).
2. **Player to drop**, if the roster is full. Unsure → suggest running drop-candidates first.
3. **Bid amount**, if `leagues.md` says FAAB. Unsure → suggest running faab-bidding first.
4. Read `leagues.md` from the project root for platform, league, waiver system, and budget. If it's missing or those fields are blank, ask directly and suggest running `fantasy-league-setup:league-config`. If more than one league is defined, use the one marked `(default)` unless the user names another.
5. **Establish which kind of transaction this is**, because it sets the gate strength:
   - A **deferred waiver claim** processes later on the league's waiver day and is cancellable until then — recoverable.
   - An **immediate free-agent add with a drop** is irreversible: the drop lands instantly and any team can claim the dropped player within seconds.
   Set the expectation with the user now. Do not decide this from a row badge — derive it from what the claim flow itself says (a stated process date means a claim), and treat the review screen as authoritative. If the review screen is ambiguous about timing, stop and ask.

## Phase 2: Execute on Yahoo

1. **Get to the league's player pool**: reuse an already-open tab on the platform if the user has one; otherwise go to the sport-scoped entry point (`football.fantasysports.yahoo.com`) rather than the provider homepage, and ensure a desktop-width viewport (≥1280px). Open the team for this league → **Players** in the team navigation. Landmark: a searchable player table with status/availability columns.
2. **Find the player**: use the search box with the exact name. Verify identity by name **and** NFL team/position before proceeding — platforms list multiple players with similar names. The row may show an availability marker, but treat it as a hint only; the claim flow and review screen are what actually determine whether this is a claim or an instant add.
3. **Open the claim**: click the add/claim control (a "+" or "Add" on the player row). The flow will ask for some subset of {drop player, bid amount, claim priority} **in an order that varies** — handle whichever step appears rather than assuming a sequence, and confirm each field holds its Phase 1 value. If asked for something Phase 1 didn't cover (claim priority, a league-specific option), stop and ask rather than accepting a default. In rolling-priority leagues, note that filing a claim reorders existing pending claims.
4. **Review screen**: Yahoo shows a summary (add, drop, bid, process date) before finalizing.
5. **⛔ CONFIRMATION GATE**: read the summary back to the user verbatim, including the bid as digits and as a share of the budget shown *on the page* — "Claim Silas Okafor (RB), drop Ironhogs DST, bid $42 — four two — of your $124 remaining, processes Wed" — and wait for an explicit yes. Only then click Submit/Confirm. If any figure on screen differs from what was agreed in Phase 1 by any amount, stop and surface it; never correct it silently.

   **If this is an immediate free-agent add rather than a deferred claim, raise the gate.** State the irreversibility in plain words and require the yes against that sentence: "This is immediate, not a Wednesday claim — the moment I click, Okafor is on your roster and the Ironhogs DST is a free agent any team can claim." 
6. **Verify**: find the view listing pending or recent transactions — try the team page first, then the league's Transactions tab. Confirm the item appears with the right players, amount, and timing; for an immediate add, confirm the player is on the roster. **Clicking Submit is not evidence that the transaction was submitted.** If you cannot verify within two attempts, say plainly that you could not verify, state exactly what you clicked and what the last screen showed, and tell the user where to check. Never report success from the click alone.

## Platform variants

- **ESPN** (`fantasy.espn.com`): Players → **Add** tab; the flow asks for the drop first, then bid (FAAB leagues), ending on a review step with a **Submit** button — that's the gated click. Pending claims appear under the team's Transactions.
- **Sleeper** (`sleeper.com`): league → Players/Waivers tab; tapping a player opens their card with an **Add** button → select drop → enter bid on the claim sheet → **Submit Claim** is the gated click. Sleeper shows pending claims on the team's waivers screen with edit/cancel options — point the user there.

## Failure handling

- Player not found in search: check spelling and the league (multi-league accounts open the wrong team easily — verify the league-name landmark). The player may also be rostered already; check and report who has them.
- Bid exceeds remaining budget: the platform will reject it — reconcile the real remaining budget from the page (the page wins over leagues.md) and re-ask the user.
- Claim vs. add mismatch (expected FA, actually on waivers or vice versa): pause at the gate anyway and tell the user the actual processing time before they confirm.
- Anything on the review screen differs from what the user asked: stop and surface it — never "fix" a discrepancy silently.

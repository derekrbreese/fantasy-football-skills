---
name: set-lineup
description: This skill should be used when the user asks to "set my lineup", "who should I start", "start him for me", "swap him into my flex", "update my lineup on Yahoo", "fix my lineup before kickoff", "bench him", or wants start/sit decisions executed on their fantasy platform. Decides the optimal lineup, then drives the user's own logged-in browser session to set it - Yahoo first, with ESPN and Sleeper variants. Always pauses for explicit confirmation before saving. Not for adding/dropping players (submit-waiver-claim) or sending trade offers (propose-trade).
---

# Set Lineup (Browser Playbook)

Decide the best starting lineup, then set it on the user's platform through their own logged-in browser session. Two phases, one hard gate: **never save a lineup change without explicit user confirmation.**

## Ground rules (all roster-ops skills)

- **The user's session is the auth.** Never ask for, read, store, or type usernames, passwords, or 2FA codes. If the platform shows a login page, stop and ask the user to log in themselves, then resume.
- **Navigate by goals and landmarks, not memorized selectors.** Platforms redesign constantly; find things by their visible text and structure ("the roster table", "the section labeled Bench"), and read the page when unsure.
- **Confirmation gate**: before any click that commits a change, show the user exactly what is about to change and wait for an explicit yes. Everything before that (navigation, reading, opening dialogs) is fair game.
- **The confirmation must post-date the summary.** It has to arrive in a user message *after* the summary read off the actual page, in the same turn as the click. An instruction given before the browser was open — including "and submit it" or "just do it" — authorizes building the change, never committing it. A reply that alters any term ("yes, but bench Moss instead") is a **modification, not a confirmation**: apply it, re-read the page, present a fresh summary, ask again.
- **Never retry a commit click.** If an action's result is unclear, re-read the page to find out whether it landed. Retry only on positive evidence the change is *absent*. If the page is ambiguous or mid-update, wait and re-read — never click again.
- Browser tooling: use the available browser-automation tools (e.g., Claude in Chrome). If none are available in the session, say so and fall back to advising the moves for the user to click themselves.

## Phase 1: Decide the lineup

1. Read `leagues.md` (platform, scoring, slots, default league). If missing, ask which platform and league.
2. Navigate to the roster (Phase 2 steps 1–2) and **read the current lineup from the page** — the page is the ground truth, not memory of past conversations.
3. Recommend a lineup: fill required slots by expected points for this league's scoring; check injury/questionable tags and bye weeks shown on the page; flex goes to the best remaining eligible player. Where two options are close, say it's close and why the edge goes where it does. Honor overrides — the user's call wins.
4. Present the recommendation as a before/after list of only the slots that change. If nothing should change, say so and stop.

## Phase 2: Execute on Yahoo

1. **Get to the team**: go to `fantasysports.yahoo.com` → find the Fantasy/My Teams area → open the team matching the league name in `leagues.md`. Landmark: a page header with the team name and a navigation row containing "Roster".
2. **Open the roster for the right week**: click Roster; verify the week selector shows the intended week. Landmark: a table of position slots (QB, RB, WR, TE, FLX/W-R-T, K, DEF) with a **Bench (BN)** section below the starters.
3. **Determine the commit model before touching any player.** Read the roster page and look for a Save/Submit/Apply control governing the roster. If there is none, **every swap commits immediately**. When it cannot be determined, assume immediate commit — that is the fail-safe assumption, and it is the working assumption for Yahoo and Sleeper.
4. **⛔ CONFIRMATION GATE** — placed according to the commit model:
   - **Immediate-commit UI (assume this unless a Save control is visible):** the gate comes **before the first swap** and covers the whole set. Restate every change ("Starting Okafor over Trask at RB2; Pruitt in for Vasquez at TE"), get an explicit yes, and only then touch the first player. Once started, complete the entire approved set — a half-applied lineup can leave a slot empty, which scores zero and is worse than the lineup the user started with.
   - **Batched UI (a Save control exists):** stage all swaps, gate, then save. If the user declines, navigate away without saving and confirm to them that nothing changed.
5. **Swap players**: the goal is that player X ends up in slot Y. Depending on build and viewport this is a per-row position control that reveals eligible destinations, drag-and-drop of the row, or tap-source-then-tap-destination. Use whichever affordance is actually visible; if a row exposes no obvious control, read the page and describe its controls rather than guess-clicking. Locked players (games started) show a lock — skip them and tell the user.
6. **Verify**: re-read the roster page; confirm each intended player sits in the intended slot, and that no starting slot is empty. Report the final lineup. Clicking a control is not evidence it worked. If a swap is genuinely absent, retry that swap once; if verification stays unclear after two reads, stop and tell the user exactly what the page shows and where to check.

Note: if the league has Yahoo's **"Start Active Players"** auto-swap enabled, Yahoo may move players on its own. A lineup differing from what was set is not necessarily a failed swap — read before concluding, and never "correct" an auto-move without asking.

## Platform variants

- **ESPN** (`fantasy.espn.com`): Roster page uses per-player **Move** buttons → legal slots show **Here** buttons. Changes generally apply immediately per swap, so apply the confirmation gate *before each Move/Here pair*, not just at the end. Landmark: Starters table above a labeled Bench table.
- **Sleeper** (`sleeper.com`): open the league → Team/Roster. The web app is drag-or-tap: tap a starter, tap the bench player to swap. Swaps commit immediately — there is no Submit Lineup control to gate on, so gate **before the first swap** per step 4. Landmark: starters listed by slot at top, "Bench" list below.

## Failure handling

- Page doesn't match these descriptions: don't guess-click. Read the page, describe what's visible, and ask the user to point at the right control if still ambiguous.
- Player missing from roster page: the user may be in the wrong league (multi-league accounts) — check the league name landmark before anything else.
- Lineup locked (kickoff passed): report which slots are locked; offer to set the remaining days' players only.

## Example run (fictional)

"Set my lineup for week 9" → leagues.md says Yahoo, "Gridiron Gazette". Roster page shows TE Oren Vasquez on **bye** in the TE slot and RB Silas Okafor on the bench.

> Recommendation: TE Harlan Pruitt in for Vasquez (bye); Okafor over Trask at RB2 (lead role, +3.2 proj). Two swaps, nothing else moves. No Save control on this roster page, so each swap commits the moment I make it — confirming both up front. Set it? — *user: yes* — Both swaps applied, then verified by re-reading the page: Pruitt TE, Okafor RB2, Vasquez and Trask to bench. Lineup is legal — no empty slots, no byes starting.

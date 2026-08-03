---
name: set-lineup
description: This skill should be used when the user asks to "set my lineup", "who should I start", "start him for me", "swap him into my flex", "update my lineup on Yahoo", "fix my lineup before kickoff", "bench him", or wants start/sit decisions executed on their fantasy platform. Decides the optimal lineup, then drives the user's own logged-in browser session to set it - Yahoo first, with ESPN and Sleeper variants. Always pauses for explicit confirmation before saving. Not for adding/dropping players (submit-waiver-claim) or sending trade offers (propose-trade).
---

# Set Lineup (Browser Playbook)

Decide the best starting lineup, then set it on the user's platform through their own logged-in browser session. Two phases, one hard gate: **never save a lineup change without explicit user confirmation.**

## Ground rules (all roster-ops skills)

- **The user's session is the auth.** Never ask for, read, store, or type usernames, passwords, or 2FA codes. If the platform shows a login page, stop and ask the user to log in themselves, then resume.
- **Navigate by goals and landmarks, not memorized selectors.** Platforms redesign constantly; find things by their visible text and structure ("the roster table", "the section labeled Bench"), and read the page when unsure.
- **Confirmation gate**: before any click that saves, submits, or confirms a change, show the user exactly what is about to change and wait for an explicit yes. Everything before that (navigation, reading, opening dialogs) is fair game.
- Browser tooling: use the available browser-automation tools (e.g., Claude in Chrome). If none are available in the session, say so and fall back to advising the moves for the user to click themselves.

## Phase 1: Decide the lineup

1. Read `leagues.md` (platform, scoring, slots, default league). If missing, ask which platform and league.
2. Navigate to the roster (Phase 2 steps 1–2) and **read the current lineup from the page** — the page is the ground truth, not memory of past conversations.
3. Recommend a lineup: fill required slots by expected points for this league's scoring; check injury/questionable tags and bye weeks shown on the page; flex goes to the best remaining eligible player. Where two options are close, say it's close and why the edge goes where it does. Honor overrides — the user's call wins.
4. Present the recommendation as a before/after list of only the slots that change. If nothing should change, say so and stop.

## Phase 2: Execute on Yahoo

1. **Get to the team**: go to `fantasysports.yahoo.com` → find the Fantasy/My Teams area → open the team matching the league name in `leagues.md`. Landmark: a page header with the team name and a navigation row containing "Roster".
2. **Open the roster for the right week**: click Roster; verify the week selector shows the intended week. Landmark: a table of position slots (QB, RB, WR, TE, FLX/W-R-T, K, DEF) with a **Bench (BN)** section below the starters.
3. **Swap players**: Yahoo's flow is click the first player's position/slot button → the page highlights legal destinations → click the target slot or player to swap. Locked players (games started) show a lock — skip them and tell the user.
4. **⛔ CONFIRMATION GATE**: with all swaps staged (or before each save if Yahoo saves per-swap), restate the changes ("Starting Okafor over Trask at RB2; Moss to bench") and ask. Only on explicit yes, click the save/confirm control.
5. **Verify**: re-read the roster page; confirm each intended player sits in the intended slot. Report the final lineup. If a swap didn't take, say exactly which one and retry once before asking for help.

## Platform variants

- **ESPN** (`fantasy.espn.com`): Roster page uses per-player **Move** buttons → legal slots show **Here** buttons. Changes generally apply immediately per swap, so apply the confirmation gate *before each Move/Here pair*, not just at the end. Landmark: Starters table above a labeled Bench table.
- **Sleeper** (`sleeper.com`): open the league → Team/Roster. The web app is drag-or-tap: tap a starter, tap the bench player to swap. A **Submit/Save Lineup** control may appear after edits — that's the gated click. Landmark: starters listed by slot at top, "Bench" list below.

## Failure handling

- Page doesn't match these descriptions: don't guess-click. Read the page, describe what's visible, and ask the user to point at the right control if still ambiguous.
- Player missing from roster page: the user may be in the wrong league (multi-league accounts) — check the league name landmark before anything else.
- Lineup locked (kickoff passed): report which slots are locked; offer to set the remaining days' players only.

## Example run (fictional)

"Set my lineup for week 9" → leagues.md says Yahoo, "Gridiron Gazette". Roster page shows TE Oren Vasquez on **bye** in the TE slot and RB Silas Okafor on the bench.

> Recommendation: TE Harlan Pruitt in for Vasquez (bye); Okafor over Trask at RB2 (lead role, +3.2 proj). Two swaps, nothing else moves. Set it? — *user: yes* — Swaps staged, saved, verified: Pruitt TE, Okafor RB2, Vasquez and Trask to bench. Lineup is legal — no empty slots, no byes starting.

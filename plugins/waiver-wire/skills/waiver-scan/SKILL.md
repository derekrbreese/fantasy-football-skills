---
name: waiver-scan
description: This skill should be used when the user asks to "work the wire", "scan the waiver wire", "who should I pick up", "best free agents for my team", "waiver targets this week", "who's worth adding", or wants available players ranked against their roster. Ranks free agents by fit with the user's actual roster holes rather than generic top-add lists. Not for sizing the bid (faab-bidding), choosing who to cut (drop-candidates), or submitting the claim in the browser (roster-ops submit-waiver-claim).
---

# Waiver Scan: Fit Over Fame

Rank available players against **this roster's holes**, not a generic top-adds list. A backup RB one injury from a workload is worth more to a team with a thin RB room than the "consensus #1 add" WR is to a team starting three good WRs.

## Step 1: Load context

Read `leagues.md` (scoring, starters, waiver system, playoff weeks). If missing, ask for scoring type and starting slots minimally, and suggest the setup plugin's league-config skill.

## Step 2: Get the two inputs

1. **The user's roster** — pasted, or fetched if a league-data integration is available in the session. Include current week and any injury designations the user knows.
2. **The available player pool** — a pasted free-agent list from their platform (easiest: sort by rostered% or weekly points and paste the top 30–50), or fetched if an integration is available. Without a pool list, give the *profile* of what to target ("your hole is RB depth — target any back whose starter just got hurt") and ask for the list to name names.

## Step 3: Diagnose roster holes

Order of severity:

1. **Unfillable starting slot** — a bye/injury leaves a required slot empty this week. Must fix now.
2. **Weakest weekly starter** — the starting slot with the lowest expected points relative to positional average. This is the upgrade target.
3. **Missing insurance** — no viable backup behind a starter position where one injury zeroes the slot (typically RB).
4. **Bye-week wall** — a future week where 2+ starters at one position sit. Fix 1–2 weeks ahead, not four.

## Step 4: Score each available player

For each candidate, score fit = opportunity × role match:

- **Opportunity signals outrank talent for in-season adds.** In order: depth-chart promotion (starter injured/traded), snap or route share trending up over 2+ weeks, red-zone/target share, efficiency last (chasing one big game is how waivers are wasted).
- **Role match**: does the player address hole #1 or #2, or just add a redundant 5th WR? A candidate addressing an unfillable slot beats a "better" player who'd ride the bench.
- **Schedule**: for playoff-bound teams (check standings if the user shares them), weight weeks 15–17 matchups; for teams fighting for a spot, weight the next 3 weeks only.
- Streaming slots (DST, K, sometimes QB/TE): rank purely by next-week matchup; season-long pedigree is irrelevant.

## Step 5: Deliver ranked claims

Output a priority-ordered claim list: player, the hole he fills, the signal justifying him, and a claim priority note. Then hand off: "for bid amounts, run faab-bidding; for who to cut, run drop-candidates; to actually file the claim in the browser, run submit-waiver-claim."

## Worked example (fictional)

"Mud Dogs" roster in a 12-team half-PPR: RBs are Tobias Renner + two dart throws; WR room is strong; TE Oren Vasquez on bye week 9.

Available pool includes WR Deion Marsette (consensus top add, 22% rostered) and RB Silas Okafor (backup elevated to starter after an injury, 8% rostered).

> 1. **RB Silas Okafor** — fills hole #3 (no RB insurance) and likely hole #2 (upgrade over both dart throws). Signal: projected lead role, 65% snaps in relief last week. Claim priority: high — lead-back roles don't reach next week's wire.
> 2. **TE Harlan Pruitt** — one-week stream for Vasquez's week-9 bye (hole #1 next week). Low bid, can wait a week if the pool is stable.
> 3. *Skip* WR Deion Marsette despite consensus rank — he'd be your WR5. Fit beats fame; let a WR-needy rival spend on him.

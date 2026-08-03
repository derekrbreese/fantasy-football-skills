---
name: faab-bidding
description: This skill should be used when the user asks "how much should I bid", "what's a fair FAAB bid", "size my bid", "blind bid amount", "how much of my budget is he worth", or wants free-agent auction bid amounts. Sizes FAAB bids from remaining budget, weeks remaining, player class, and the league's observed bid history. Not for choosing which players to target (waiver-scan) or filing the claim in the browser (roster-ops submit-waiver-claim).
---

# FAAB Bid Sizing

Produce a specific dollar bid, not a range and a shrug. Bids are a function of four things: what class of player this is, how much budget and season remain, what this league actually pays, and how contested the claim will be.

## Step 1: Load context

Read `leagues.md`: FAAB budget, whether $0 bids are allowed, waiver day, playoff weeks. Ask the user for: **remaining budget**, the target player(s), and — the highest-leverage question — **recent winning bids in this league** (most platforms show a claim/bid history page). Three or four data points calibrate everything.

## Step 2: Classify the player

Baseline bid as % of the **season-starting** budget (so advice stays stable as budgets shrink):

| Class | Definition | Baseline |
|---|---|---|
| League-winner | Multi-week every-down role appeared (e.g., starting RB lost for season, clear handcuff inherits) | 40–70% |
| Season-long starter | Weekly startable role, not a workhorse (new WR2 role, committee lead) | 15–30% |
| Useful depth / insurance | Bench piece, handcuff, bye coverage with upside | 5–12% |
| Streamer | One-week DST/K/TE/QB matchup play | 0–3% |
| Lottery stash | Role *might* materialize | 1–6% |

## Step 3: Adjust

- **League calibration (apply first)**: if recent winning bids run hot (a committee back went for 35%), shift the whole table up ~1.3×; if the league is passive, shift down. Observed prices beat theory.
- **Time decay**: after mid-season, multiply by roughly `weeks-remaining / weeks-in-season` for everything *except* league-winners — a league-winner in week 10 still justifies most of a remaining budget.
- **Contention**: rebuilding teams shouldn't pay starter prices for 30-year-old rentals; contenders should overpay for playoff-week (15–17) contributors.
- **Roster fit**: if the player fills an unfillable starting slot this week (per waiver-scan), add 20–30% to the bid; redundancy subtracts the same.
- **Budget reality**: never bid more than `remaining budget − $1 × (roster holes still expected this season)`. Going to $0 in week 6 is only correct for a league-winner.

## Step 4: Pick the number

- **Break round numbers**: field bids cluster at 10/15/20/25. Bid $1–2 above the cluster: $22 beats the $20 crowd, costs almost nothing extra.
- **$0-bid leagues**: file $0 claims freely on every marginal player; save real dollars for contested adds.
- **Multiple targets same week**: order claims by priority and make lower claims conditional if the platform supports it; size each bid as if it's the only one, then cap the sum at what the budget survives.
- State a single recommended bid plus a walk-away max ("bid $22, don't chase past $28").

## Worked example (fictional)

"Couch Commissioners," $200 budget, $124 remaining, week 8 of 14 waiver-relevant weeks. Target: RB Silas Okafor, elevated to a projected 3-week lead role behind an injured starter — high-end *useful depth* verging on *starter*, call it 14% baseline = $28. League history: last two lead-back rentals won at $41 and $37 → hot league, ×1.3 → $36. Time decay for a non-league-winner: ×(7/14) is too harsh for a 3-week immediate role; decay applies to season-long value, so hold at $36. User is 5-2 (contender, no discount). Round-number break: field will cluster at $35 and $40.

> **Bid $37, walk away above $44.** That clears the $35 cluster, matches this league's observed price for the role, and leaves $87 for the stretch run.

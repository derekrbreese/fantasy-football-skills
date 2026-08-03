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
- **Opportunity cap, not time decay**: unspent FAAB is worth exactly zero in January, and real markets clear *higher* as a share of remaining budget late in the season, when managers dump budget before the playoffs. Do not shrink bids as the season runs down. Instead cap any single claim at `remaining budget / expected remaining opportunities`, estimating roughly one starter-class-or-better add per 3–4 remaining weeks. That cap rises as a share of what's left — which is the correct direction.
- **Contention**: rebuilding teams shouldn't pay starter prices for 30-year-old rentals; contenders should overpay for playoff-week (15–17) contributors.
- **Roster fit**: if the player fills an unfillable starting slot this week (per waiver-scan), add 20–30% to the bid; redundancy subtracts the same.
- **Budget reality**: never bid more than `remaining budget − $1 × (roster holes still expected this season)`. Going to $0 in week 6 is only correct for a league-winner.

## Step 4: Pick the number

- **Break round numbers**: field bids cluster at 10/15/20/25. Bid $1–2 above the cluster: $22 beats the $20 crowd, costs almost nothing extra.
- **$0-bid leagues**: file $0 claims freely on every marginal player; save real dollars for contested adds.
- **Multiple targets same week**: order claims by priority and make lower claims conditional if the platform supports it; size each bid as if it's the only one, then cap the sum at what the budget survives.
- **Beat the maximum rival bid, not the average.** Blind FAAB is a sealed-bid, first-price auction — one submission, no chance to react. When the league's observed comps for this player class span a range, bid above the *top* of that range, not into the middle of it.
- **Ties go to waiver priority** in most leagues, which is the real mechanical reason $1-above-a-round-number works. A team with poor priority (usually the league leader) must bid *above* a likely tie, not at it.
- State a single recommended bid and the reasoning. There is no "walk away" in blind bidding — a sealed bid is submitted once. Frame the ceiling as "this is your max; if you lose at it, someone valued him more — don't chase by re-adding later at a worse price."

## Worked example (fictional)

"Couch Commissioners," $200 budget, $124 remaining, week 8 with 6 weeks left. Target: RB Silas Okafor, elevated to a projected multi-week lead role behind an injured starter.

- **Classify honestly.** A lead role is a *season-long starter* (15–30% = $30–60), not "useful depth." The league's own comps confirm it: the last two lead-back rentals cleared at $41 and $37 — 20.5% and 18.5% of budget, squarely in the starter band. Classifying this as depth and then rescuing it with a multiplier is how bids end up below market.
- **Respect the observed range.** Comps span $37–41. Beating the *maximum* means clearing $41, not matching the $37 floor — a bid at the bottom of the observed range loses to the same rival who paid $41 last month.
- **Opportunity cap.** 6 weeks left ≈ 2 more starter-class adds; cap = $124 / 2 = $62. Well clear.
- **Round-number break.** The field clusters at $35 and $40. The binding cluster is $40, so bid $1–2 above *that*, not above $35.
- Contender at 5-2, so no rebuilding discount.

> **Bid $42.** It clears the $40 cluster and the $41 comp, sits mid-starter-band for a genuine lead role, stays under the $62 opportunity cap, and leaves $82 for the stretch run. If you lose at $42, someone valued him more — don't chase him at a worse price next week.

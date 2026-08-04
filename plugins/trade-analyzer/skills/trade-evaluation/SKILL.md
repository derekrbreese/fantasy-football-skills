---
name: trade-evaluation
description: This skill should be used when the user asks "is this trade fair", "should I accept this trade", "evaluate this trade", "who wins this trade", "am I getting fleeced", or presents a specific offer (received or about to be sent) for judgment. Runs a two-sided assessment weighing each team's standings and positional needs on top of raw player value. Not for hunting new trade partners (trade-analyzer trade-finder), the back-and-forth after a reply (trade-analyzer trade-negotiation), or browser execution (roster-ops propose-trade).
---

# Trade Evaluation: Two-Sided Assessment

Judge a specific trade from **both** rosters' perspectives. Raw player value is the start, not the verdict — value only counts when it reaches a starting lineup.

## Step 1: Load context

Read `leagues.md` from the project root first — the fields that matter here are scoring, starting slots, roster/bench size, playoff weeks, trade deadline, and whether trades face a veto vote. If the file is missing or blank, ask and suggest running `fantasy-league-setup:league-config`. If more than one league is defined, use the one marked `(default)`.

Gather both full rosters, both records/standings, and the exact terms. Without the other team's roster only half an evaluation is possible — say so and evaluate provisionally.

## Step 2: Who originated the offer? — ask this first

**An incoming offer is adversely selected.** The proposer built it after looking at both rosters and concluded it helps them. That is not bad faith; it is what proposing means. It does change the prior:

- **Offers you received**: require a clearly positive edge, not merely an even one. "Even" plus adverse selection is a small loss on average.
- **Offers you constructed**: even is genuinely fine, and mutual benefit is the normal shape of a good trade.

This is the step most trade advice skips, and it flips the verdict on marginal incoming offers.

## Step 3: Raw value pass

Assign each player a rest-of-season value from projections the user supplies, a fetched consensus source (name it), or reasoned judgment (label it as such). Sum both sides.

Interpret the gap in three bands rather than one:

- **Under ~5%** — genuinely indistinguishable. Decide on lineup fit alone.
- **5–15%** — a real edge you cannot measure confidently. Take it when the lineup-delta test agrees.
- **Over 15%** — one side is being fleeced. Say so bluntly, in whichever direction it runs.

Widen these bands to match measured disagreement between projection sources when more than one is available.

## Step 4: Lineup delta — the real test

For **each** team, compute the optimal weekly starting lineup before and after, using this league's slots:

- **Lineup delta = projected starting-lineup points after − before.** A WR4 traded away costs a 3-WR team real points and a 2-WR team nothing.
- **Bench players are not worth zero** — that shorthand is only true in very shallow leagues. With 6–8 bench spots, a plausible starter carries roughly 20–35% of his projection in option value: injury insurance, bye coverage, and trade currency. Only genuinely unplayable pieces round to zero. This matters most on 2-for-1s, which **transfer risk** as well as value: after any consolidation, ask "if my starter at this position goes down, who starts?"
- Run byes and the configured playoff weeks separately from the season average when the deadline is near — a September trade is about 12 weeks, a November trade about 3.
- **Injury status is usually the largest in-season value swing.** Price a hurt player as games missed × per-game value, discount for re-injury risk and ramp-up, and note that a player returning in week 13 can be worth far more to a contender than his season-average value implies.

Translate the result into something decidable: roughly **+1 point per week ≈ +1% win probability per game** against a typical lineup. A +1.2/week delta over five remaining weeks is about +0.06 wins — real, but small enough to weigh against execution risk.

## Step 5: Standings and rivalry context

- **Contender**: values the configured playoff weeks and ceiling; should pay a premium for the best player and for playoff-schedule advantages.
- **Bubble team**: values the next 3–4 weeks; weight near-term delta 2:1. A deal that wins rest-of-season but loses the next three can eliminate them before it pays.
- **Eliminated/rebuilding**: in keeper formats, values keeper-eligible pieces (route to `draft-strategy:keeper-evaluation`). In pure redraft there is little reason to trade at all.
- Determine these from playoff probability and seeding scenarios, not record alone — a 7-3 team locked into a bye and a 7-3 team fighting for the last spot should behave very differently.
- **Are you arming a rival?** Check two things the raw math misses: whether this team is competing with you for a playoff spot, and whether you play them in the remaining weeks. Upgrading the lineup of the team chasing your seed — or the team you face next Sunday — is a real cost.

## Step 6: Verdict

Deliver **Accept / Decline / Counter**, a confidence level, and two or three sentences of reasoning. If Counter, say what change flips it, then suggest `trade-analyzer:trade-negotiation`. Report both sides' win conditions honestly — mutual benefit is what fair trades look like, and saying so builds the credibility that gets future deals accepted.

If the league uses veto votes, note when a fair deal *looks* lopsided, since appearance is what gets vetoed.

## Worked example (fictional)

"Gridiron Gazette," week 10. User (7-3, contender, thin at RB) **receives an offer**: get RB Quincy Marsh + WR Deion Marsette, send WR Cassius Bell. Opponent is 4-6 (bubble), starts 3 WR, RB-surplus.

- **Origination**: they proposed it, so the bar is a clearly positive edge, not break-even.
- **Raw value**: user +~20% — above the 15% band, so this genuinely favors the user on paper.
- **Lineup delta, user**: Marsh upgrades a dead RB2 (+4.1/wk); losing Bell drops WR2→WR3 (−2.9/wk); Marsette is bench depth (+0 to the lineup, but real option value). Net **+1.2/wk**, and Marsh's playoff schedule is soft.
- **Lineup delta, opponent**: Bell upgrades their WR3 (+3.4/wk); Marsh was their bench RB3; Marsette was their WR5 (−0.4/wk). Net **+3.0/wk**.
- **Rivalry check**: they're 4-6, three games back, and not on the user's remaining schedule. Arming them is low-risk.

> **Accept (moderate-high confidence).** It clears the adverse-selection bar — the raw-value edge is above 15% in your favor and it fixes your RB slot. But be clear-eyed about why they offered: they gain more per week than you do (+3.0 vs +1.2), because near-term lineup points are exactly what a bubble team needs. Accept because it's positive for you, not because you won.

Note the verdict does not revert to the raw-value ledger the moment lineup delta is inconvenient — it reports both and says which one drove the decision.

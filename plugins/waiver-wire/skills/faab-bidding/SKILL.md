---
name: faab-bidding
description: This skill should be used when the user asks "how much should I bid", "what's a fair FAAB bid", "size my bid", "blind bid amount", "how much of my budget is he worth", "should I use my waiver priority on him", or wants to know what a waiver claim is worth. Sizes blind FAAB bids and advises when to spend rolling waiver priority. Not for choosing which players to target (waiver-wire waiver-scan), auction draft bidding (draft-strategy live-draft-assistant), or browser execution (roster-ops submit-waiver-claim).
---

# Waiver Bid Sizing

Produce a specific number, not a range and a shrug. Bids are a function of four things: what class of player this is, how contested the claim will be, how much budget remains against how many chances remain, and what this league actually pays.

## Step 1: Load context

Read `leagues.md` from the project root first — the fields that matter here are the waiver system (FAAB budget or rolling priority), league size, scoring (superflex especially), and playoff weeks. If the file is missing or blank, ask for them and suggest running `fantasy-league-setup:league-config`. If more than one league is defined, use the one marked `(default)`.

Then ask for: **remaining budget**, the target player, and — highest leverage — **recent winning bids in this league** (most platforms show a transaction/bid history page). Also worth knowing: whether $0 bids are allowed, and whether the platform processes claims **conditionally** (only one of your claims can win) or **independently** (every winning claim processes, so three wins can drain the budget). That distinction changes multi-claim advice by a factor of three.

## Step 2: Classify the player

Denominate baselines as a share of **remaining** budget, not the season-starting budget. Remaining budget is what you actually have to allocate, and it keeps the advice correct late in the season when the starting figure has become meaningless.

| Class | Definition | Baseline (% of remaining) |
|---|---|---|
| League-winner | A season-altering role opened: IR/season-ending injury ahead of them, or a permanent depth-chart change. Every-down workload. | 55–85% |
| Season-long starter | Weekly startable role, not a workhorse (new WR2 role, committee lead) | 15–30% early; 25–45% from week 10 |
| Useful depth / insurance | Bench piece, bye coverage, speculative upside | 3–8% (handcuff to the user's *own* RB1: 8–15%) |
| Lottery stash | Role might materialize later | 1–3%, and only if bench space is genuinely free |
| Streamer | One-week DST/K/TE/QB matchup play | **League minimum + $1, in absolute dollars** |

Two notes on the table:

- **Duration, not just quality, sets the class.** The classic FAAB error is paying league-winner money in week 1 of an injury for a backup whose starter returns in three weeks. "Multi-week" must mean season-altering to qualify for the top class.
- **Streamers and lottery tickets are absolute-dollar bids, not percentages.** In a $1,000 league, 3% of remaining is $30 for a one-week defense that will be free again in seven days. Only the top three classes scale with budget size.
- **Superflex changes everything at QB.** A startable quarterback hitting waivers in a superflex league is league-winner class, never a streamer.

## Step 3: Count credible rivals — this sets the number

FAAB is a **first-price sealed-bid auction**. You do not need to bid your valuation; you need to beat the highest opposing bid. So the question is not "how aggressive is my league" but "how many teams will credibly bid on *this* player."

For each rival ask: (a) do they have this roster hole, (b) do they have meaningful budget left (platforms show every team's remaining FAAB — use it), (c) have they bid aggressively before?

- **0–1 credible rivals** → bottom of the class range.
- **2–3** → middle.
- **4+** → top of the range or above it.

Rostered percentage is a useful proxy for how many managers have noticed a player at all.

Layer the league's own history on top **non-parametrically**: bid around the **75th percentile of this league's observed winning bids for comparably contested adds**, matching on how contested the claim was rather than on class label. Do not apply a uniform multiplier to the whole table — real markets bid up the top disproportionately while streamer prices stay pinned at the floor.

## Step 4: Budget discipline

- **Do not decay bids as the season shortens.** Unspent FAAB is worth exactly zero in January, and prices in most leagues *rise* as a share of remaining budget in weeks 9–13 when managers dump budget before the playoffs. A contender should plan to finish the season at or near $0.
- **Opportunity cap**: no single claim should exceed `remaining budget / expected remaining opportunities`, estimating roughly one starter-class-or-better add per 3–4 remaining weeks. Note this cap *rises* as a share of what's left — the correct direction.
- **Reserve**: while a minimum bid exists, keep $1 per remaining waiver week so a week-15 injury doesn't end the season with an unusable roster. Drop the reserve to $0 once the playoff roster is set.
- **Eliminated teams** should bid $0 on everything, and where the platform allows trading FAAB, sell the remaining budget to a contender.

## Step 5: Pick the number

- **Beat the maximum, not the average.** When observed comps span a range, bid above the *top* of it. Matching the middle of a two-point range is a coin flip.
- **Break round numbers.** Field bids cluster hard at 10/15/20/25 and at 25%/50%. Bid $1–2 above the *binding* cluster — the one your bid must clear — never a multiple of 5.
- **Ties go to waiver priority** in most leagues, which is the real mechanical reason this works. A team with poor priority (usually the league leader) must bid *above* a likely tie, not at it. Confirm the league's tiebreaker; it is worth $1.
- **$0-bid leagues**: file $0 claims freely on marginal players and save real dollars for contested adds.
- **Consider waiting.** In most leagues an unclaimed player becomes a free agent 24 hours after waivers process. For low-rostered speculative adds, waiting costs $0.
- **Multiple targets**: with conditional claims, file all of them aggressively since only one can hit. With independent processing, cap the sum at what the budget survives.

**Regret is asymmetric — shade up, not down.** Standard auction theory says shade your bid below your valuation. FAAB inverts this: overpaying costs dollars you can recover from, while losing the player costs the player forever, possibly to the rival you're chasing. Losing a league-winner by $2 is the expensive mistake, not overpaying by $10.

## Rolling-priority leagues

No dollars involved — priority is a depleting asset that resets to last after use. The rule: **spend priority only on a player who would start for you**, or who is a genuine league-winner-class stash. Burning the #1 priority on a bye-week streamer to save a waiver claim is how managers find themselves last in line when a workhorse role opens in week 11. If the target would merely sit on the bench, wait for free agency instead.

## Worked example (fictional)

"Couch Commissioners," $200 season budget, **$124 remaining**, week 8 with 6 weeks left. Target: RB Silas Okafor, elevated to a lead role behind a starter placed on IR.

- **Class**: the starter is on IR, so the role is season-altering — this is the top of *season-long starter* and arguably league-winner. Comps confirm it: the league's last two lead-back rentals cleared at $41 and $37. Starter band on $124 remaining = $19–56 (25–45%, week 10 window approaching).
- **Credible rivals**: four teams have an RB hole and more than $40 left. That's 4+ → top of the range or above.
- **League history**: comps span $37–41; the 75th percentile of comparably contested adds sits around $41.
- **Opportunity cap**: 6 weeks ≈ 2 more starter-class adds → $124 / 2 = $62. Not binding.
- **Reserve**: 6 waiver weeks left → hold $6. Ceiling $118.
- **Cluster**: field will cluster at $35 and $40; the binding cluster is $40.

> **Bid $42.** It clears the $40 cluster and the $41 comp, sits inside the starter band, respects the $62 opportunity cap, and leaves $82. Four credible rivals is exactly the case for the top of the range — and if you lose at $42, don't chase him at a worse price next week.

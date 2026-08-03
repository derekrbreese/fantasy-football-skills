---
name: keeper-evaluation
description: This skill should be used when the user asks "who should I keep", "which keepers should I pick", "is he worth keeping at that price", "keeper value", "what does keeping him cost me", or needs to compare keeper candidates before a draft. Runs keeper cost versus ADP math to rank keeper candidates by surplus value. Not for building the draft board itself (draft-prep) or in-draft picks (live-draft-assistant).
---

# Keeper Evaluation

Rank the user's keeper candidates by **surplus value**: what the player is worth minus what keeping them costs. A good keeper is a player priced below market, not simply the best player on the roster.

## Step 1: Load context

Read `leagues.md` first — the keeper rules line (how many keepers, cost mechanism, escalation) and scoring/roster settings. If keeper rules aren't recorded, ask: How many keepers? What does keeping a player cost (a draft round, an auction dollar amount)? Does the cost escalate year over year? Then offer to save the answers back to `leagues.md`.

## Step 2: Gather candidates

For each candidate the user is weighing: player, keeper cost (round or $), and current ADP or the user's own ranking. Ask the user to supply ADP or fetch current consensus ADP if web access is available (state the source and date).

## Round-based leagues: keeper surplus

**Surplus = keeper cost round − ADP round** (positive = profit).

- Convert ADP to a round for the user's league size (12-team: overall 25–36 = round 3).
- **Keep threshold: surplus ≥ 2 rounds** for a locked call. Surplus of 1 round is a coin flip — break ties with the adjustments below. Surplus ≤ 0 means redraft the player instead; keeping at market price wastes the keeper slot's option value.
- Adjustments (worth ±1 round of surplus):
  - *Tier scarcity*: +1 if the player sits in a top-2 tier at a scarce position for this league's settings — replacement cost exceeds ADP.
  - *Escalation*: −1 if cost escalates and this is the last cheap year of a multi-year hold worth planning around.
  - *Age/situation risk*: −1 for a player whose ADP is propped up by last season's outlier or an unresolved depth-chart battle.
- Opportunity cost check: keeping consumes that round's pick. Surplus already accounts for this **only if** the league charges the stated round; in leagues where keepers cost the *first* pick regardless, compare the player's value directly against a typical round-1 ADP instead.

## Auction leagues

Surplus = market auction value − keeper price, in dollars. Keep threshold: surplus ≥ 10% of the total budget (e.g., $20 on a $200 budget). Same adjustments apply, scaled to dollars.

## Step 3: Rank and recommend

Output a table of candidates sorted by adjusted surplus, mark keep/pass at the league's keeper count, and note the draft-board consequence of each keep ("keeping him burns your 6th — plan for zero-RB through round 5"). Suggest running draft-prep next so the board reflects the keeper-adjusted player pool.

## Worked example (fictional players, "Basement Brawlers" 12-team half-PPR, keep 2, cost = round drafted last year − 1)

| Candidate | Cost | ADP (round) | Raw surplus | Adjustments | Adjusted |
|-----------|------|-------------|-------------|-------------|----------|
| WR Cassius Bell | R11 | 4.08 (R4) | +7 | — | **+7 → KEEP** |
| RB Quincy Marsh | R3 | 2.03 (R2) | +1 | +1 tier scarcity (Tier 2 RB, thin league) | **+2 → KEEP** |
| QB Tug Ridley | R8 | 7.11 (R7) | +1 | −1 (1-QB league, QB replacement is free) | 0 → pass |
| TE Oren Vasquez | R5 | 6.02 (R6) | −1 | — | −1 → pass, redraftable |

Recommendation: keep Bell and Marsh. Bell is the league-winning class of keeper (7 rounds of surplus); Marsh edges Ridley because RB scarcity survives the adjustment and QB never does in a 1-QB league.

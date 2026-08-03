---
name: draft-prep
description: This skill should be used before draft day, when the user asks to "build my draft board", "help me prep for my draft", "make tiers from these rankings", "tier my rankings", "rank players for my league", "adjust rankings for my scoring", or asks about positional scarcity or value-based drafting strategy. Builds a tiered, league-adjusted draft board from rankings the user supplies or that are fetched on request. Not for use during a live draft (live-draft-assistant) or for keeper decisions (keeper-evaluation).
---

# Draft Prep: Tiered Board Construction

Build a draft board that is tiered, value-adjusted, and specific to the user's league settings — not a reprint of generic rankings.

## Step 1: Load league context

Read `leagues.md` from the project root first. The fields that matter here: teams, scoring, starting slots (especially FLEX/superflex), and keeper rules. If the file is missing, ask for those four things (or suggest running the setup plugin's league-config skill), then continue.

## Step 2: Get rankings data

Ask the user which they prefer, in this order:

1. **User-supplied rankings** (best) — a pasted CSV/list from any source they trust, ideally with projected points and ADP columns.
2. **Fetched consensus data** — if web access is available, fetch current consensus rankings and ADP from a public aggregator and tell the user the source and date.
3. **No data available** — build the board structure and decision rules anyway and mark player slots as "fill from your rankings"; never invent projections and present them as real.

Minimum viable columns: player, position, and either projected points or overall rank. ADP unlocks value analysis; bye weeks unlock conflict warnings.

## Step 3: Compute replacement level

Value-based drafting (VBD) prices every player against the last startable player at their position:

- Baseline rank per position = `teams × starters at that position + (teams × flex share)`. Estimate flex share as the fraction of flex slots each flex-eligible position typically absorbs (RB/WR roughly split a standard flex; TE rarely takes it).
- Example: 12 teams, 2 RB + 1 RB/WR/TE flex → RB baseline ≈ 12×2 + 12×0.5 = RB30.
- **VBD value = projected points − baseline player's projected points.** Draft order by VBD, not raw points — this is what makes a QB's 350 points worth less than an RB's 280 in 1-QB leagues.
- Superflex/2QB: add QB to the flex share at ~0.9 (nearly every team starts two). QB values roughly double; say so explicitly in the board notes.
- TE premium: recompute TE projections with the bonus before tiering; elite TEs typically jump 1–2 rounds.

## Step 4: Build tiers

Tiers matter more than ranks — on the clock, the question is "is anyone left in the tier," not "who is ranked 43rd."

- Sort each position by projected points (or rank). Start a new tier where the drop between consecutive players exceeds ~5% of the higher player's projection, or where the gap is clearly larger than the gaps within the current group.
- Cap tiers at ~6 players; a 10-player "tier" is a sorting failure.
- Label each tier with an action note, not just a number: "Tier 3 RB — last group you can trust weekly; if 2 remain at your pick, wait; if 1, take him."

## Step 5: Positional scarcity notes

Add a scarcity summary comparing tier depth to league demand:

- Count startable slots league-wide per position (from Step 3) vs. players in trustworthy tiers. The position where trust runs out soonest is the scarcity priority.
- Flag the "cliff round": the round by which each position's last solid tier will be gone at current ADP.

## Step 6: Deliver the board

Output a markdown table per position (tier, player, projection, VBD, ADP, bye) plus an overall top-100 blended by VBD, the scarcity summary, and 3–5 strategy bullets specific to their settings ("your league starts 3 WR — WR cliff hits round 6, prioritize early").

## Worked example (fictional players and league)

"Gridiron Gazette," 12-team half-PPR, 1 QB / 2 RB / 2 WR / 1 TE / 1 flex:

| Tier | RB | Proj | VBD (vs RB30 ≈ 155) | ADP |
|------|----|------|----------------------|-----|
| 1 | Marcus Vellum | 285 | +130 | 1.02 |
| 1 | Dario Whitlock | 271 | +116 | 1.05 |
| 2 | Tobias Renner | 244 | +89 | 1.11 |
| 2 | Quincy Marsh | 238 | +83 | 2.03 |
| 3 | Errol Fontaine | 209 | +54 | 3.07 |

Board note produced: "Only five RBs clear +50 VBD but your league starts up to 36 RB-eligible slots weekly — take two of these five by round 3 or accept a zero-RB build knowingly."

---
name: draft-prep
description: This skill should be used before draft day, when the user asks to "build my draft board", "help me prep for my draft", "make tiers from these rankings", "tier my rankings", "rank players for my league", "adjust rankings for my scoring", or asks about positional scarcity or value-based drafting strategy. Builds a tiered, league-adjusted draft board from rankings the user supplies or that are fetched on request. Not for use during a live draft (draft-strategy live-draft-assistant) or for keeper decisions (draft-strategy keeper-evaluation).
---

# Draft Prep: Tiered Board Construction

Build a draft board that is tiered, value-adjusted, and specific to the user's league settings — not a reprint of generic rankings.

## Step 1: Load league context

Read `leagues.md` from the project root first — the fields that matter here are teams, scoring (including superflex and TE premium), starting slots, bench size, and keeper rules. If the file is missing or those fields are blank, ask for them directly and suggest running the `fantasy-league-setup:league-config` skill to persist the answers. If `leagues.md` defines more than one league, use the one marked `(default)` unless the user names another.

## Step 2: Get rankings data

Ask the user which they prefer, in this order:

1. **User-supplied rankings** (best) — a pasted CSV/list from any source they trust, ideally with projected points and ADP columns.
2. **Fetched consensus data** — if web access is available, fetch current consensus rankings and ADP from a public aggregator and tell the user the source and date.
3. **No data available** — build the board structure and decision rules anyway and mark player slots as "fill from your rankings"; never invent projections and present them as real.

Minimum viable columns: player, position, and either projected points or overall rank. ADP unlocks value analysis; bye weeks unlock conflict warnings.

**Ask for two sources when possible, and blend them.** Sources routinely disagree by 15–25% on individual players, and the disagreement is itself signal: a player whose projections vary by more than a tier width has a genuinely uncertain role. Flag those explicitly — they are the players to avoid if the roster needs certainty, and to target if it needs upside.

## Step 3: Compute replacement level

Value-based drafting prices every player against what is freely obtainable at their position, not against zero.

**Demand per position** = `teams × (dedicated starters + flex_slots × flex_share)`.

The `flex_slots` term matters and is often dropped: a 2-FLEX league has twice the flex demand of a 1-FLEX league.

**Derive the flex share — do not assume it.** Hardcoded splits are format-specific and wrong outside the format they came from. Instead: pool every flex-eligible player ranked beyond their dedicated-starter baseline, sort by projection, take the top `teams × flex_slots`, and count how many are RB vs. WR vs. TE. That count *is* the flex share, computed from the same projections already in hand. It adapts automatically to PPR, standard, TE premium, superflex, and league size. As a sanity check on the result: full PPR skews the flex toward WR, standard skews it toward RB, and TE premium pulls TEs into it that base scoring never would.

**Then adjust the baseline for streamability**, because "freely obtainable" differs sharply by position:

- **RB/WR**: the computed demand line is right. Replacement really is the last startable player.
- **QB in 1-QB leagues**: streaming the best weekly matchup aggregates to roughly QB8–QB10 season-equivalent output, so true replacement is *better* than the QB12 demand line. Use the streaming estimate. This is the mathematical reason not to draft a QB early in a 1-QB league.
- **TE**: streaming works poorly, because TE production is role-driven rather than matchup-driven. True replacement is *worse* than the TE12 line — roughly TE16–18 — which means elite TEs are worth more than the naive line suggests.
- **Superflex/2QB**: the superflex slot goes to a QB in essentially every lineup, so use a flex share of 1.0 for QB and a baseline near QB24. Do not describe this as a multiplier on QB value; let the recomputed baseline drive the board. What actually changes is that the *entire position* becomes draftable and the QB13–24 range becomes the real scarcity crisis of the draft — there are only about 32 startable NFL quarterbacks against 24 required weekly starts plus backups, so the position cannot be streamed. Plan on a QB in the first two rounds and a second by rounds 4–6.
- **K/DST**: replacement is the best free option every single week, so value over replacement is approximately zero for every kicker and defense. This is the formal reason for the punt rule below.

**Value = projected points − baseline points.** Rank by that, not raw points.

## Step 4: Build tiers

Tiers matter more than ranks — on the clock, the question is "is anyone left in the tier," not "who is ranked 43rd."

- Sort each position by projected points. **Break a tier where a gap between consecutive players is clearly larger than the gaps within the current group** — roughly one standard deviation of that position's gap distribution. A simpler working proxy: players within about 0.75–1.0 points *per game* of each other belong in the same tier.
- Draw tiers relative to projection *uncertainty*, not point level. Two players 8 points apart in a season projection whose sources disagree by 60 points are the same tier regardless of what any percentage rule says.
- **Stop tiering below replacement level.** Near the bottom of a position a 15-player tier is the correct answer — they genuinely are interchangeable, and forcing breaks there invents distinctions that do not exist.
- Label each tier with an action note, not just a number: "Tier 3 RB — last group you can trust weekly; if 2 remain at your pick, wait; if 1, take him."

## Step 5: Positional scarcity and structure notes

- Compare tier depth to league-wide demand from Step 3. The position where trustworthy players run out soonest is the scarcity priority.
- Flag the "cliff round": the round by which each position's last solid tier will be gone at current ADP.
- **Punt K and DST to the final two rounds. No exceptions.** Their value over replacement is approximately zero and free replacements are available all season; every earlier pick spent on them throws away a bench asset. A QB2 in a 1-QB league is nearly as wasteful.
- Name the structure the board implies — zero-RB, hero-RB, robust-RB, late-round QB, superflex double-QB — and say which draft slots can actually execute it. Structures are slot-dependent: advice to pair two players from an early tier is unreachable from most slots.
- Use weeks 15–17 (or the league's configured playoff weeks) strength of schedule as an **intra-tier tiebreaker only**. Full-season SOS at draft time is close to noise, since projections already embed it and preseason defensive rankings are unreliable. Where SOS is used at all, use positional splits, never team-level defensive rank.

## Step 6: Deliver the board

Output a markdown table per position (tier, player, projection, value over replacement, ADP, bye) plus an overall top-100 blended by value, the scarcity summary, and 3–5 strategy bullets specific to their settings.

## Worked example (fictional)

"Gridiron Gazette," 12-team half-PPR, 1 QB / 2 RB / 2 WR / 1 TE / 1 flex. Derived flex share came out RB 0.45 / WR 0.5 / TE 0.05, so RB demand = 12 × (2 + 1 × 0.45) ≈ RB29; call the baseline 155 points.

| Tier | RB | Proj | Value (vs 155) | ADP |
|------|----|------|----------------|-----|
| 1 | Marcus Vellum | 285 | +130 | 1.02 |
| 1 | Dario Whitlock | 271 | +116 | 1.05 |
| 2 | Tobias Renner | 244 | +89 | 1.11 |
| 2 | Quincy Marsh | 238 | +83 | 2.03 |
| 3 | Errol Fontaine | 209 | +54 | 3.07 |

Board note produced: "Only five RBs clear +50, and your league demands about 29 RB-equivalent starts weekly. Those five go at ADPs 1.02, 1.05, 1.11, 2.03, and 3.07 — so only a manager near the turn (slots 10–12) can realistically pair two. From slots 1–9, plan on one of them plus a Tier 3 RB2, or commit to zero-RB deliberately rather than by accident."

Note what the example does: it reports what each draft slot can actually execute, rather than giving advice most of the league cannot follow.

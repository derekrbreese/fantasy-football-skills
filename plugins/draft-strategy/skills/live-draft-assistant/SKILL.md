---
name: live-draft-assistant
description: This skill should be used during a live draft, when the user says "I'm on the clock", "who should I pick", "best available", "my draft is live", "we're drafting now", "should I reach for him", "what's my max bid", "who should I nominate", or reports draft picks as they happen. Tracks a live snake or auction draft in real time - best-available logic, reach/value alerts against ADP, auction budget and nomination strategy, and roster-construction tracking. Not for pre-draft board building (draft-strategy draft-prep), keeper cost decisions (draft-strategy keeper-evaluation), or in-season waiver bids (waiver-wire faab-bidding).
---

# Live Draft Assistant

Run the user's draft in real time: track every pick, keep a best-available view, and warn about reaches, tier cliffs, and roster imbalance. Speed matters — on the clock, lead with the answer, then the reasoning.

## Setup (first message of the draft)

1. Read `leagues.md` from the project root first — the fields that matter here are teams, scoring, and starting slots; snake math depends on them. If the file is missing or those fields are blank, ask for them directly and suggest running the `fantasy-league-setup:league-config` skill to persist the answers. If `leagues.md` defines more than one league, use the one marked `(default)` unless the user names another.
2. Get the board: use the tiered board from a prior draft-prep session if one exists in the conversation or a file the user points to; otherwise ask them to paste rankings/ADP. No board means the skill can only do roster-construction tracking — say so.
3. Get the user's draft slot and confirm format (snake vs. auction; linear third-round-reversal if applicable).

## Draft state tracking

Maintain throughout, and restate briefly every few picks:

- **Picks made** — the user reports picks ("Vellum went 1.03", "I took Renner"). Cross players off the board; log which team took them when the user says.
- **User's roster so far** — filled slots vs. required starters.
- **Snake math** — in an N-team snake at slot `s`, the gap to the next turn alternates by round parity:
  - After an **odd**-round pick (order runs 1→N): the next turn is `2 × (N − s) + 1` selections later.
  - After an **even**-round pick (order runs N→1): the next turn is `2 × s − 1` selections later.
  - Pick labels flip too: slot `s` picks `s` in odd rounds and `N − s + 1` in even rounds.
  - Third-round reversal, if the league uses it: round 3 runs reversed, so compute round 3 onward with the parity swapped.
  - Always show "you pick again in X selections."

## On-the-clock recommendation logic

When the user asks "who should I pick," answer in this order:

1. **Best available by value over replacement** — top 3 remaining, with tier labels.
2. **Tier urgency override** — a tier is dying if it will not survive to the user's next turn. Compare players left in the tier against **expected picks at that position** in the gap, not against total picks: `expected_takes = gap × positional share of picks` (roughly 0.30–0.40 for WR or RB in the middle rounds). Take from the tier now if `players_left ≤ expected_takes + 1`. Comparing against total picks badly overestimates safety — 4 players left across an 11-pick gap is a coin flip, not a comfortable wait.
3. **Roster construction override** — never leave a required *skill* slot unfillable. Counting only QB/RB/WR/TE/FLEX, by round ⌈skill starters × 0.75⌉ the user should have no more than one empty skill-position group. Don't take a third TE while 0 WRs are rostered, no matter the value.
   - **K and DST are excluded from this rule and come in the final two rounds, no exceptions.** They have essentially zero value over replacement and free replacements exist all season. A rule that counts them as required groups will push a kicker into round 7, which throws away a bench asset on the most replaceable position in fantasy. A QB2 in a 1-QB league is nearly as wasteful.
4. **Bye stacking check** — warn (don't block) when a pick creates 3+ shared byes among likely starters.

## Reach and value alerts

- **Reach alert**: fire when **`player's ADP − current pick > picks until your next turn`**. That is literally the test the alert claims to run — "he'll likely be there at your next pick" — and it uses the gap already computed above, so it self-adjusts for league size, draft slot, turn picks, and third-round reversal. A fixed spot-count threshold is wrong at both turns and in every non-12-team league, and it ignores that ADP dispersion widens from ~2–4 picks in round 1 to ~20–30 by round 10: a 12-spot deviation is meaningful early and pure noise late. If the tier-urgency rule justifies the reach, say so — reaching into a dying tier is correct.
- **Value alert**: a player has fallen a full round past ADP → flag proactively, even unasked: "Quincy Marsh (ADP 2.03) is still on the board at 4.01 — value pick."
- Reaches the user makes anyway are their call; update the board and move on without relitigating.

## Worked example (fictional)

12-team snake, user at slot 7, pick 3.07 ("Gridiron Gazette" league). Roster so far: RB Tobias Renner, WR Cassius Bell.

> **Pick now: Errol Fontaine (RB, Tier 3, value +54).** He's the last Tier 3 RB, so the tier dies here by definition. Your next turn is 11 selections away (odd round, `2 × (12 − 7) + 1`, so you're back at 4.06). The WR call is closer than it looks: Deion Marsette (Tier 2, ADP 3.10) has four tier-mates left, but at roughly a 35% WR pick rate across an 11-pick gap, about 4 WRs come off — so `players_left (4) ≤ expected_takes (4) + 1` and that tier is genuinely at risk too. Fontaine still wins because his tier has one player left against four; just don't count on Marsette returning. Reach check: Fontaine's ADP 3.09 is one pick away, far inside your 11-pick gap — no reach. Bye note: Fontaine shares week 9 with Renner — acceptable, but avoid a third week-9 bye.

## Auction variant

If the league drafts by auction:

- **Track live inflation** — `remaining league-wide money / remaining market value of the player pool`. This is the most valuable single number in an auction. If $1,200 chases $1,000 of value, everything left costs about 20% over par and hoarding is a losing strategy; if the ratio is below 1, bargains are coming and patience pays.
- **Hard ceiling** = `budget − open roster slots + 1`. Never exceed it; bidding to it leaves a roster of $1 players.
- **Max meaningful bid** = `budget − Σ(realistic price of remaining slots you still need)`, reserving the going rate for remaining *starter* slots and $1 for bench spots. Quote this, not the hard ceiling — the hard ceiling prices a starting WR2 and a last bench spot identically.
- **Budget shape**: roughly 75–80% of budget on starters, $1–3 total for K and DST.
- **Enforcement pricing**: bid up a player when a rival with that positional hole is the only other bidder — but only to a price you would happily pay yourself, because you will sometimes own him.
- **Nomination**: nominate players the user doesn't want while rivals still have money.

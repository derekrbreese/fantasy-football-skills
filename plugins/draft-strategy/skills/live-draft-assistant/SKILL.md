---
name: live-draft-assistant
description: This skill should be used during a live draft, when the user says "I'm on the clock", "who should I pick", "best available", "my draft is live", "we're drafting now", "should I reach for him", "pick is in — update the board", or reports picks as they happen. Tracks the draft in real time - best-available logic, reach/value alerts against ADP, and roster-construction tracking. Not for pre-draft board building (draft-prep) or keeper cost decisions (keeper-evaluation).
---

# Live Draft Assistant

Run the user's draft in real time: track every pick, keep a best-available view, and warn about reaches, tier cliffs, and roster imbalance. Speed matters — on the clock, lead with the answer, then the reasoning.

## Setup (first message of the draft)

1. Read `leagues.md` (teams, scoring, starters). If missing, get league size, scoring, and starting slots before anything else — snake math depends on them.
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

1. **Best available by VBD** — top 3 remaining, with tier labels.
2. **Tier urgency override** — if a position has exactly 1–2 players left in its current tier and the tier below is a real drop, that player jumps the queue. Rule of thumb: if the tier will not survive until the user's next pick (compare players-left-in-tier vs. picks until next turn), take from it now.
3. **Roster construction override** — never leave a required starting slot unfillable; by round ⌈starters × 0.75⌉, the user should have no more than one empty required-position group. Don't take a third TE while 0 WRs are rostered, no matter the value.
4. **Bye stacking check** — warn (don't block) when a pick creates 3+ shared byes among likely starters.

## Reach and value alerts

- **Reach alert**: user is considering a player more than ~12 ADP spots (one round) early → say "that's a reach of N spots; he'll likely be there at your next pick" and offer the alternative. If the tier-urgency rule justifies the reach, say that too — reaching into a dying tier is fine.
- **Value alert**: a player has fallen a full round past ADP → flag proactively, even unasked: "Quincy Marsh (ADP 2.03) is still on the board at 4.01 — value pick."
- Reaches the user makes anyway are their call; update the board and move on without relitigating.

## Worked example (fictional)

12-team snake, user at slot 7, pick 3.07 ("Gridiron Gazette" league). Roster so far: RB Tobias Renner, WR Cassius Bell.

> **Pick now: Errol Fontaine (RB, Tier 3, VBD +54).** He's the last Tier 3 RB; 11 picks until your next turn (odd round, `2 × (12 − 7) + 1`) and RB tiers won't survive that. Best WR available (Deion Marsette, Tier 2, ADP 3.10) is one of four left in his tier — at least one should return at 4.06. Reach check: Fontaine at ADP 3.09 is on schedule. Bye note: Fontaine shares week 9 with Renner — acceptable, but avoid a third week-9 bye.

## Auction variant

If the league drafts by auction: track remaining budget for every team the user reports, compute max bid (budget − open slots + 1), and flag enforcement prices (bid to the player's value when a rival with a positional hole is the only other bidder). Nomination advice: nominate players the user doesn't want while rivals still have money.

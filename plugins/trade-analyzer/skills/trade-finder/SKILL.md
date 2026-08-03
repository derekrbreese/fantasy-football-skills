---
name: trade-finder
description: This skill should be used when the user asks "find me a trade", "who should I target in a trade", "scan the league for trade partners", "who needs what in my league", "help me get a running back via trade", or wants trade ideas without a specific offer on the table. Scans all league rosters for complementary surpluses and drafts a concrete opening proposal. Not for judging an existing offer (trade-evaluation), handling the back-and-forth (trade-negotiation), or sending the offer in the browser (roster-ops propose-trade).
---

# Trade Finder: Complementary Surplus Scan

Find the trades that *should* exist in this league: pairs of rosters where each team's surplus is the other's hole. Output is a shortlist of partners and one drafted opening proposal — not a vague "you could use a WR."

## Step 1: Load context

Read `leagues.md` (scoring, starters, trade deadline, playoff weeks). Gather every roster in the league plus standings — pasted, or fetched via an available league integration. A partial league scan is fine; say which teams weren't scanned.

## Step 2: Build the surplus/deficit matrix

For each team, at each position, compare **startable-quality players rostered vs. starting slots required** (this league's slots — a 3rd good RB is surplus in a 2-RB league and par in a 2RB+flex league):

- Surplus: more week-in, week-out startable players than slots (+1 or more).
- Deficit: a starting slot filled by waiver-tier production.
- Note bye/playoff-schedule pressure: a team about to hit a triple-bye week has a *temporary* deficit worth exploiting gently.

## Step 3: Rank partner fit

Score each rival as a partner:

1. **Complementarity** (required): their surplus covers the user's deficit AND the user's surplus covers one of theirs. One-directional need means the user must overpay — deprioritize.
2. **Motivation**: bubble teams (records near .500) trade most; first-place teams trade least; eliminated redraft teams trade almost never (and such trades draw scrutiny). Deadline proximity raises everyone's urgency.
3. **History**, if the user knows it: managers who've already made trades this season will trade again.

## Step 4: Draft the opening proposal

For the top partner, construct a specific offer:

- Trade **from surplus into deficit on both sides** — the offer should improve both starting lineups (verify with the lineup-delta test from trade-evaluation thinking: value that doesn't reach a lineup isn't real to either side).
- Open slightly in the user's favor but inside the plausible range — an insulting opener burns the partner permanently; a too-fair opener leaves no negotiating room. Target roughly a 10–15% raw-value edge, never more.
- Include the pitch: two sentences the user can send explaining why it helps *the other team*, referencing their situation ("you've got three startable RBs and a WR2 hole and the deadline's in two weeks").
- Offer 1–2 backup constructions (a smaller version, and a version with a different sweetener) for the negotiation to come.

## Step 5: Hand off

Suggest trade-evaluation to pressure-test the final construction, trade-negotiation when the reply comes back, and roster-ops propose-trade to actually send it.

## Worked example (fictional)

"Basement Brawlers," 12-team, week 8. User (5-3): RB surplus (4 startable for 2+flex), TE deficit (streaming). Scan finds:

| Team | Record | Surplus | Deficit | Fit |
|---|---|---|---|---|
| Turf Burns | 4-4 | TE (elite Oren Vasquez + startable backup) | RB (RB2 slot is waiver-tier) | **Both-ways — top partner** |
| Blitz Krieg | 6-2 | WR | RB | One-way (user has no WR hole) — skip |
| Fumble Bees | 2-6 | QB | everything | Motivated but nothing user needs — skip |

> **Opening offer to Turf Burns**: send RB Errol Fontaine (user's RB4, their instant RB2 upgrade), receive TE Oren Vasquez. Pitch: "You're one RB from a playoff push and I'm streaming TE — Fontaine starts for you Sunday." Value edge ~12% to the user (elite TE premium in this league's TE-premium scoring). Fallback: swap in RB Dewey Sandoval + a bench WR if they balk at value; smaller version targets their backup TE instead.

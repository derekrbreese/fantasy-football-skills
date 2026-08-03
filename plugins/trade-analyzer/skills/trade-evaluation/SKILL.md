---
name: trade-evaluation
description: This skill should be used when the user asks "is this trade fair", "should I accept this trade", "evaluate this trade", "who wins this trade", "am I getting fleeced", or presents a specific offer (received or about to be sent) for judgment. Runs a two-sided assessment that weighs each team's standings and positional needs on top of raw player value. Not for hunting new trade partners (trade-finder), crafting counteroffers (trade-negotiation), or submitting a trade in the browser (roster-ops propose-trade).
---

# Trade Evaluation: Two-Sided Assessment

Judge a specific trade from **both** rosters' perspectives. Raw player value is the start, not the verdict — a trade can be "unfair" on a value chart and still correct to accept, because value only counts when it reaches a starting lineup.

## Step 1: Load context

Read `leagues.md` (scoring, starters, playoff weeks, trade deadline). Gather: both full rosters, both teams' records/standings, and the exact trade terms. Rosters can be pasted or fetched via an available league integration. Without the *other* team's roster, only half an evaluation is possible — say so and evaluate provisionally.

## Step 2: Raw value pass

Assign each player a rest-of-season value from projections the user supplies, a fetched consensus source (name it), or reasoned judgment (label it as such). Sum each side. A gap under ~15% is noise; call it even on raw value.

## Step 3: Lineup delta — the real test

For **each** team, compute the optimal weekly starting lineup before and after the trade, using this league's slots:

- **Lineup delta = projected starting-lineup points after − before.** Bench points are worth ~0. A WR4 traded away costs a 3-WR team real points and a 2-WR team nothing.
- 2-for-1 consolidations: the team getting the best player usually wins the lineup delta *if* their freed slot is filled by a real bench player; the team getting quantity only wins if both incoming pieces crack their actual lineup.
- Run byes and playoff weeks (15–17) separately from the season average when the deadline is near — a September trade is about 12 weeks, a November trade is about 3.

## Step 4: Standings context

- **Contender (playoff position secure or likely)**: values weeks 15–17 and ceiling. Should pay a raw-value premium for the best player in the deal and for playoff-schedule advantages.
- **Bubble team**: values the next 3–4 weeks; a deal that wins "rest of season" but loses the next three weeks can eliminate them before it pays off. Weight near-term delta 2:1.
- **Eliminated/rebuilding**: in redraft with keepers, values keeper-eligible pieces and next year's cost (route to keeper-evaluation math). In pure redraft, an eliminated team has little reason to trade at all — flag lopsided offers *to* such teams, as leagues tend to scrutinize them.

## Step 5: Verdict

Deliver: **Accept / Decline / Counter** plus a confidence level, the reasoning in two or three sentences, and — if Counter — what change flips the verdict (then suggest trade-negotiation for the back-and-forth). State both sides' win conditions honestly: "this is good for you AND for them" is a common and legitimate outcome; that's what fair trades look like.

## Worked example (fictional)

"Gridiron Gazette," week 10. User (7-3, contender, RBs: thin) is offered: receive RB Quincy Marsh + WR Deion Marsette, send WR Cassius Bell. Opponent is 4-6 (bubble), starts 3 WR, has RB surplus.

- Raw value: Bell ≈ Marsh alone; user gains Marsette free → user wins raw value by ~20%.
- Lineup delta, user: Marsh upgrades a dead RB2 slot (+4.1/wk); losing Bell drops WR2→WR3 (−2.9/wk); Marsette rides the bench. Net **+1.2/wk**, and Marsh's weeks 15–17 schedule is soft: contender fit confirmed.
- Lineup delta, opponent: Bell upgrades their WR3 (+3.4/wk); Marsh was their bench RB3 (−0 from lineup); Marsette was their WR5 (−0.4/wk). Net **+3.0/wk** over the next three weeks — exactly what a bubble team needs.

> **Verdict: Accept (high confidence).** You win the value ledger and your RB hole; they win the near-term lineup points that keep their season alive. Both sides should say yes — send it before they rethink the free Marsette throw-in.

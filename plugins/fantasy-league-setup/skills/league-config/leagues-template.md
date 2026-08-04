# Fantasy League Configuration
<!--
  Template for leagues.md — copy this file to your project root as `leagues.md`
  and fill it in, or let the league-config skill interview you and write it.

  Every fantasy-football-skills skill reads this file before giving advice.
  One "## League:" section per league. Mark exactly one league "(default)".
  Delete these comments in your real file. If your project is a public repo,
  consider adding leagues.md to .gitignore — it names your real league.

  Anything you don't know: write `unknown` rather than guessing. Skills will
  ask when it matters. A wrong value here silently biases every recommendation.
-->

## League: <league name> (default)

<!-- Platform hosting the league: yahoo | espn | sleeper | other -->
- Platform: yahoo

<!-- Number of teams. Drives replacement level and scarcity math. -->
- Teams: 12

<!-- standard | half-ppr | ppr. Give magnitudes, not just flags:
     te-premium(+0.5), superflex, 2qb, 6pt-pass-td, ppc(+0.1), idp -->
- Scoring: half-ppr

<!-- Median scoring / all-play, if used. Rewards consistency over ceiling. -->
- Median scoring: no

<!-- Exact starting slots, including what the FLEX accepts and how many. -->
- Starters: 1 QB, 2 RB, 2 WR, 1 TE, 1 FLEX (RB/WR/TE), 1 K, 1 DST

<!-- Bench spots and IR slots. IR eligibility rules differ by platform. -->
- Bench: 6, IR: 1

<!-- faab (season budget, whether $0 bids count) or rolling-priority.
     Include processing day, whether waivers run weekly or daily/continuous,
     and the tie-break rule for equal bids — it's worth $1 on every claim. -->
- Waivers: faab, budget $100, $0 bids allowed, processes Wed, weekly, ties break by waiver priority

<!-- Any cap on adds per week or per season. Changes streaming strategy
     entirely — a capped league can't churn the wire. -->
- Acquisition limit: none

<!-- Can waiver budget be traded between teams? Unlocks real strategy. -->
- FAAB tradeable: no

<!-- Playoff weeks, bracket size, whether top seeds get a first-round bye,
     and the seeding tiebreaker (points-for changes start/sit in blowouts). -->
- Playoffs: weeks 15-17, 6 teams, top 2 seeds get a bye, tiebreaker points-for

<!-- none, or describe: how many keepers, cost (e.g., "costs draft round
     from last year minus 1, escalates yearly"). -->
- Keepers: none

<!-- Week of the trade deadline, or none. -->
- Trade deadline: week 12

<!-- none | commissioner | league-vote. Veto leagues need trades that LOOK
     balanced, not just ones that are. -->
- Trade review: none

<!-- Your team's name, so skills can identify your roster in pasted data. -->
- My team: <your team name>

<!-- Add more leagues by repeating the section:

## League: <second league name>

- Platform: espn
- ...
-->

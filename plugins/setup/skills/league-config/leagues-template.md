# Fantasy League Configuration
<!--
  Template for leagues.md — copy this file to your project root as `leagues.md`
  and fill it in, or let the league-config skill interview you and write it.

  Every fantasy-football-skills skill reads this file before giving advice.
  One "## League:" section per league. Mark exactly one league "(default)".
  Delete these comments in your real file. If your project is a public repo,
  consider adding leagues.md to .gitignore — it names your real league.
-->

## League: <league name> (default)

<!-- Platform hosting the league: yahoo | espn | sleeper | other -->
- Platform: yahoo

<!-- Number of teams. Drives replacement-level and scarcity math. -->
- Teams: 12

<!-- standard | half-ppr | ppr. Add modifiers in parentheses:
     superflex, 2qb, te-premium (+0.5/rec), 6pt-pass-td, idp -->
- Scoring: half-ppr

<!-- Exact starting slots, including what the FLEX accepts. -->
- Starters: 1 QB, 2 RB, 2 WR, 1 TE, 1 FLEX (RB/WR/TE), 1 K, 1 DST

<!-- Bench spots and IR slots. -->
- Bench: 6, IR: 1

<!-- faab (with season budget, whether $0 bids count) or rolling-priority.
     Include the processing day if you know it. -->
- Waivers: faab, budget $100, $0 bids allowed, processes Wed

<!-- Playoff weeks and bracket size. Drives drop/trade timing advice. -->
- Playoffs: weeks 15-17, 6 teams

<!-- none, or describe: how many keepers, cost (e.g., "costs draft round
     from last year minus 1, escalates yearly"). -->
- Keepers: none

<!-- Week of the trade deadline, or none. -->
- Trade deadline: week 12

<!-- Your team's name, so skills can identify your roster in pasted data. -->
- My team: <your team name>

<!-- Add more leagues by repeating the section:

## League: <second league name>

- Platform: espn
- ...
-->

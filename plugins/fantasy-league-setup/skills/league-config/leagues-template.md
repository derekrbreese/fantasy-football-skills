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

<!-- Fantasy season year. Prevents stale keeper/draft context carrying over. -->
- Season: 2026

<!-- Platform hosting the league: yahoo | espn | sleeper | other -->
- Platform: yahoo

<!-- Stable identifier exactly as the platform shows it: Yahoo league key,
     ESPN league ID, Sleeper league ID, etc. Write unknown if you cannot
     confirm it yet. -->
- Platform league ID/key: unknown

<!-- League-local timezone for waiver runs, draft time, and deadlines. -->
- Timezone: America/New_York

<!-- Date and source used to verify these settings. -->
- Verified: 2026-08-04 via league settings page

<!-- Number of teams. Drives replacement level and scarcity math. -->
- Teams: 12

<!-- standard | half-ppr | ppr. Give magnitudes, not just flags:
     te-premium(+0.5), superflex, 2qb, 6pt-pass-td, ppc(+0.1), idp -->
- Scoring: half-ppr

<!-- Spell out the custom rules that actually move advice:
     pass TD points; TE premium; points per carry; return yards/TDs;
     100/150/200-yard bonuses; long-play bonuses; kicker makes/misses
     and whether they are fractional; DST sacks/turnovers/points allowed;
     IDP lineup and tackle/sack/turnover scoring; any negative quirks. -->
- Scoring details: 4-point passing TDs; TE premium none; points per carry none; return scoring none; bonuses none; K: 3/4/5 by distance, misses -1, fractional no; DST: sacks 1, turnovers 2, points-allowed Yahoo default; IDP none; other custom rules none

<!-- Median scoring / all-play, if used. Rewards consistency over ceiling. -->
- Median scoring: no

<!-- Exact starting slots, including what the FLEX accepts and how many. -->
- Starters: 1 QB, 2 RB, 2 WR, 1 TE, 1 FLEX (RB/WR/TE), 1 K, 1 DST

<!-- Bench spots and IR slots. IR eligibility rules differ by platform. -->
- Bench: 6, IR: 1

<!-- Draft type plus the exact scheduled date/time and clock. -->
- Draft: snake, 2026-09-02 20:00 America/New_York, 90-second clock

<!-- Use one of: faab | rolling-priority | weekly-reverse-standings |
     fcfs | hybrid.
     For faab: budget, $0 bids, run time, post-run FCFS windows, equal-bid tie.
     For rolling-priority: whether a successful claim resets you to last.
     For weekly-reverse-standings: whether order recomputes each run/week.
     For hybrid: which windows are waivers versus FCFS. -->
- Waivers: faab, budget $100, $0 bids allowed, runs Wed 03:00 America/New_York, after-run FCFS until kickoff, equal-bid ties break by waiver priority

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

<!-- Optional. Which authenticated browser skills should use when you
     do not name one: ChatGPT built-in | Claude in Chrome
     | <other named tool> | unknown. ChatGPT and Codex are the same app.
     unknown means "use any signed-in session the current assistant has." -->
- Preferred browser: unknown

<!-- Add more leagues by repeating the section:

## League: <second league name>

- Platform: espn
- ...
-->

# Regression checks

Run the zero-dependency checks from the repository root:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

The fixtures are fictional league configurations that preserve the hard cases
the skills must handle: return yards and IDP with recomputed priority; a deep
three-WR FAAB league with vote review; and a keeper/TE-flex league with custom
kicker and pressure-based DST scoring.

The automated checks map each fixture's unusual fields to explicit consumer
rules and protect the repaired worked examples. They are contract tests, not a
simulation of model behavior, and do not pretend to measure weekly
player-advice quality. Before a release, also run the plugin validator commands
in `CONTRIBUTING.md` and manually exercise each fixture with three questions:

1. Does the recommendation explicitly use the fixture's unusual scoring or
   waiver rule rather than silently applying a default?
2. Does missing or stale injury evidence produce a conditional recommendation
   instead of a destructive cut, major bid, or decisive lineup change?
3. Does every proposed browser mutation preserve the correct league identity
   and stop at the final confirmation gate?
4. Does "set up my league" offer to read the settings page before interviewing,
   and does a Preferred browser value change which session is used?
5. Does "what should I do this week" produce one briefing and refuse to click
   a lineup, claim, or trade?

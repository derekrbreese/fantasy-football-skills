---
name: league-config
description: This skill should be used when the user asks to "set up my league", "configure my league", "add my league settings", "update my league config", "onboard my league", "change my scoring settings", or when any fantasy-football-skills skill finds no leagues.md file. Interviews the user once about scoring, roster slots, waiver system, league size, and platform, then writes the answers to a leagues.md file that all other fantasy football skills read.
---

# League Configuration

Interview the user about their fantasy league(s) and persist the answers to `leagues.md` in the project root. Every other fantasy-football-skills skill reads this file first, so a complete interview here means the user is never re-asked for scoring or roster context.

## Workflow

1. **Check for an existing `leagues.md`** in the project root. If it exists, show the current config and ask whether to update a league, add a new one, or start over. Never silently overwrite.
2. **Interview** the user, one short batch of questions at a time (not one giant wall). Collect the fields below for each league.
3. **Write `leagues.md`** using the structure in `leagues-template.md` (in this skill's directory). One `## League:` section per league. Strip the template's explanatory comments from the written file — keep it clean.
4. **Confirm** by echoing back a one-line summary per league (e.g., "Gridiron Gazette — 12-team half-PPR on Yahoo, $100 FAAB").

## Fields to collect

Required (advice quality degrades without these):

- **League name** — used as the section header so multiple leagues can coexist
- **Platform** — `yahoo`, `espn`, `sleeper`, or `other` (drives the roster-ops browser playbooks)
- **Teams** — league size (drives replacement-level math)
- **Scoring** — `standard`, `half-ppr`, or `ppr`; plus modifiers with their **magnitudes**, not just flags: TE premium (+0.5 or +1.0 per reception is a materially different league), superflex/2QB, points per passing TD (4 vs 6), points per carry, big-play bonuses, IDP
- **Median scoring / all-play**, if used — it rewards consistency over ceiling and changes what "contender" means
- **Starting roster slots** — e.g., `1 QB, 2 RB, 2 WR, 1 TE, 1 FLEX (RB/WR/TE), 1 K, 1 DST`
- **Bench size** and IR slots
- **Waiver system** — `faab` (record the season budget and whether $0 bids are allowed) or `rolling-priority`; the processing day, whether waivers run weekly or continuously/daily, and the tie-break rule for equal bids
- **Acquisition limits** — any cap on adds per week or per season. Common on Yahoo and ESPN, and it changes waiver and drop advice substantially, so ask explicitly rather than assuming none

Optional (ask, but accept "skip"):

- **Playoff weeks** — e.g., weeks 15–17 (drives drop-candidates, start/sit, and trade timing). Also ask how many teams make it, whether top seeds get a first-round bye, and what the seeding tiebreaker is — a points-for tiebreaker changes start/sit decisions in blowouts
- **Trade review** — none, commissioner review, or a league veto vote. Veto leagues need trades that *look* balanced, not just ones that are
- **FAAB tradeable?** — some platforms allow trading waiver budget, which unlocks real strategy for both contenders and eliminated teams
- **Keeper rules** — how many keepers, cost mechanism (round-based, auction dollar, escalating)
- **Trade deadline** week
- **The user's team name** — so skills can tell "my roster" apart in exports the user pastes

## Rules

- Ask; never guess. If the user doesn't know a setting, mark it `unknown` in the file rather than inventing a default, and note that skills will ask when it matters.
- Multiple leagues get one section each in the same file. Ask which league is the "default" and mark it — other skills use the default when the user doesn't specify.
- `leagues.md` may contain the user's real league and team names. That is expected — it lives only in their project. Recommend adding `leagues.md` to `.gitignore` if the project is a public repo.
- Never ask for, store, or write passwords, session cookies, or platform credentials. League *settings* only.

## Worked example

User says: "Set up my league — it's a 10-team full PPR on Sleeper called Couch Commissioners, superflex, $200 FAAB."

Interview fills the gaps (roster slots, bench, playoff weeks, keepers), then write:

```markdown
# Fantasy League Configuration

## League: Couch Commissioners (default)

- Platform: sleeper
- Teams: 10
- Scoring: ppr (superflex)
- Starters: 1 QB, 2 RB, 2 WR, 1 TE, 1 FLEX (RB/WR/TE), 1 SUPERFLEX (QB/RB/WR/TE)
- Bench: 6, IR: 2
- Waivers: faab, budget $200, $0 bids allowed, processes Wed
- Playoffs: weeks 15-17, 6 teams
- Keepers: none
- Trade deadline: week 12
- My team: The Replacements
```

Finish by telling the user the file is ready and that draft, waiver, and trade skills will now use it automatically.

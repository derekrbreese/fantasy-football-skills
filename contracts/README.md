# Shared skill contracts

These files are the source of truth for wording that must stay identical
across independently installed plugins. Edit the contract, then copy it
verbatim into every consumer listed below. Do not hand-edit a copy.

| Contract | Consumers |
|---|---|
| `live-source-routing.md` | Every analysis skill that may read a live league or rankings page, including `league-config` and `weekly-briefing` |
| `browser-routing.md` | All three `roster-ops` skills |

A regression test fails if a consumer's copy drifts from the contract file.

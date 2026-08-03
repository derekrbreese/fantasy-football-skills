# fantasy-football-skills

A [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces) of fantasy football skills: draft strategy, waiver-wire management, trade analysis, and browser-driven roster operations. Install a plugin and Claude picks up the right skill from natural phrases like *"who should I start"*, *"work the wire"*, or *"is this trade fair"*.

## Install

```
claude plugin marketplace add derekrbreese/fantasy-football-skills
```

Then install any plugin (start with `setup`):

```
/plugin install setup@fantasy-football-skills
/plugin install draft-strategy@fantasy-football-skills
/plugin install waiver-wire@fantasy-football-skills
/plugin install trade-analyzer@fantasy-football-skills
/plugin install roster-ops@fantasy-football-skills
```

Run the `setup` plugin's league-config skill first ("set up my league") — it interviews you once and writes a `leagues.md` file to your project. Every other skill reads that file for your scoring, roster slots, waiver system, and platform, so you never repeat yourself. A commented template lives at [`plugins/setup/skills/league-config/leagues-template.md`](plugins/setup/skills/league-config/leagues-template.md).

## Plugins and skills

| Plugin | Skill | Say things like |
|---|---|---|
| **setup** | league-config | "set up my league", "change my scoring settings" |
| **draft-strategy** | draft-prep | "build my draft board", "make tiers from these rankings" |
| | live-draft-assistant | "I'm on the clock", "who should I pick", "best available" |
| | keeper-evaluation | "who should I keep", "is he worth keeping at that price" |
| **waiver-wire** | waiver-scan | "work the wire", "who should I pick up" |
| | faab-bidding | "how much should I bid", "size my FAAB bid" |
| | drop-candidates | "who should I drop", "who's safe to cut" |
| **trade-analyzer** | trade-evaluation | "is this trade fair", "should I accept this trade" |
| | trade-finder | "find me a trade", "who needs what in my league" |
| | trade-negotiation | "they countered", "how do I respond to their counter" |
| **roster-ops** | set-lineup | "set my lineup", "who should I start" |
| | submit-waiver-claim | "put in the claim", "add him and drop X" |
| | propose-trade | "send the trade", "submit the trade offer" |

The first four plugins are pure decision support — they work with data you paste (rankings, rosters, free-agent lists) or that Claude fetches when a data source is available. `roster-ops` executes moves in a browser.

## roster-ops security model

The `roster-ops` skills drive a browser session **you are already logged into** (for example via Claude in Chrome). Plainly:

- **Your session is the auth.** The skills never ask for, read, store, or type usernames, passwords, or 2FA codes. If a login page appears, Claude stops and asks you to log in yourself.
- **Nothing is submitted without your explicit confirmation.** Every skill has a hard gate before any save/submit/send click: Claude reads back exactly what is about to happen and waits for your yes. Navigation and reading pages happen freely; transactions never do.
- Playbooks are written as goals and landmarks ("find the roster page, locate the bench section"), not brittle selectors — Yahoo first, with ESPN and Sleeper variants.

## Disclaimer

This is advice tooling for entertainment purposes. It is not affiliated with, endorsed by, or connected to Yahoo, ESPN, Sleeper, the NFL, or any fantasy platform. Player projections and rankings come from sources you supply; verify transactions on your platform before they process. Use browser automation in accordance with your platform's terms of service.

## Contributing

New skills welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for the frontmatter conventions and the no-overlap rule for trigger phrases.

## License

[MIT](LICENSE)

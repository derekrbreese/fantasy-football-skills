# fantasy-football-skills

A [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces) of fantasy football skills: draft strategy, weekly start/sit, waiver-wire management, trade analysis, and browser-driven roster operations. Install a plugin and Claude picks up the right skill from natural phrases like *"who should I start"*, *"work the wire"*, or *"is this trade fair"*.

## Install

```
claude plugin marketplace add derekrbreese/fantasy-football-skills
```

Then install the plugins you want:

```
/plugin install lineup-strategy@fantasy-football-skills
/plugin install draft-strategy@fantasy-football-skills
/plugin install waiver-wire@fantasy-football-skills
/plugin install trade-analyzer@fantasy-football-skills
/plugin install roster-ops@fantasy-football-skills
```

Each of these depends on `fantasy-league-setup`, which installs automatically. The first time you use any skill, say *"set up my league"* — it interviews you once and writes a `leagues.md` file to your project. Every other skill reads that file for your scoring, roster slots, waiver system, and playoff weeks, so you never repeat yourself. A commented template lives at [`leagues-template.md`](plugins/fantasy-league-setup/skills/league-config/leagues-template.md).

### Prerequisites

The first five plugins need nothing but Claude Code. **`roster-ops` additionally requires browser automation** — [Claude in Chrome](https://www.anthropic.com/news/claude-in-chrome) or an equivalent — and the extension must be granted permission for your fantasy platform's site before it can do anything. Without browser tooling, `roster-ops` skills will tell you the clicks to make rather than making them.

## Plugins and skills

| Plugin | Skill | Say things like |
|---|---|---|
| **fantasy-league-setup** | league-config | "set up my league", "change my scoring settings" |
| **draft-strategy** | draft-prep | "build my draft board", "make tiers from these rankings" |
| | live-draft-assistant | "I'm on the clock", "who should I pick", "what's my max bid" |
| | keeper-evaluation | "who should I keep", "is he worth keeping at that price" |
| **lineup-strategy** | start-sit | "who should I start", "start or sit", "A or B at flex" |
| **waiver-wire** | waiver-scan | "work the wire", "who should I pick up", "my guy got hurt, now what" |
| | faab-bidding | "how much should I bid", "size my bid", "should I use my waiver priority on him" |
| | drop-candidates | "who should I drop", "who's safe to cut" |
| **trade-analyzer** | trade-evaluation | "is this trade fair", "should I accept this trade" |
| | trade-finder | "find me a trade", "is he a buy low", "should I sell high on him" |
| | trade-negotiation | "they countered", "how should I respond to their counter" |
| **roster-ops** | set-lineup | "set my lineup", "fix my lineup before kickoff" |
| | submit-waiver-claim | "put in the claim", "add him and drop X" |
| | propose-trade | "send the trade", "submit the trade offer" |

Note the advice/execution split: `start-sit` decides *who* to start and needs no browser; `set-lineup` *applies* that decision on your platform. Same for `waiver-scan` vs. `submit-waiver-claim`, and `trade-evaluation` vs. `propose-trade`.

The first five plugins work with data you paste — rankings, rosters, free-agent lists, bid history — or that Claude fetches when you have a data source available. This marketplace ships no data feed and no API integration of its own.

## roster-ops security model

The `roster-ops` skills drive a browser session **you are already logged into**. Plainly:

- **Your session is the auth.** The skills never ask for, read, store, or type usernames, passwords, or 2FA codes. If a login page, 2FA prompt, or captcha appears, Claude stops and hands the browser back to you.
- **Nothing is submitted without your explicit confirmation**, and the confirmation has to come *after* Claude shows you what the page actually says. Telling Claude "and submit it" up front authorizes building the transaction, never sending it.
- **The gate matches what can't be undone.** A deferred waiver claim is cancellable; an immediate free-agent add drops a player irreversibly; a trade offer is visible to another human the instant it sends. Each gets a correspondingly stronger confirmation.
- **UI only, never the API.** The skills won't call platform endpoints, execute page JavaScript, or script around the interface.
- **Never unattended.** These skills require a human present for every transaction. Don't run them on a schedule or in a loop — that breaks both the confirmation model and the terms under which platforms tolerate this kind of use.
- Playbooks navigate by goals and landmarks ("find the roster page, locate the bench section"), not brittle selectors — Yahoo first, with ESPN and Sleeper variants.

Your `leagues.md` holds real league and team names. It's gitignored here; keep it out of public repos of your own.

## Disclaimer

This is advice tooling for entertainment purposes. It is not affiliated with, endorsed by, or connected to Yahoo, ESPN, Sleeper, the NFL, or any fantasy platform. Projections and rankings come from sources you supply; verify every transaction on your platform. Use browser automation in accordance with your platform's terms of service — note that Yahoo's and ESPN's terms generally restrict automated access, which is why these skills are built around interactive, human-confirmed use of your own session rather than unattended automation.

## Contributing

New skills welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for the frontmatter conventions and the no-overlap rule for trigger phrases.

## License

[MIT](LICENSE)

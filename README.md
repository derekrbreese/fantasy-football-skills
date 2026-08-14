# fantasy-football-skills

Ask your AI assistant *"who should I start"*, *"work the wire"*, or *"is this trade fair"* — and get answers calibrated to **your league's actual scoring, roster slots, and waiver rules**, not generic rankings talk. This is a plugin marketplace for OpenAI's Codex and Anthropic's [Claude Code](https://code.claude.com/docs/en/plugin-marketplaces) covering the full season: draft prep, weekly start/sit, waiver management, trade analysis, and browser-driven roster operations.

Works with Yahoo, ESPN, and Sleeper leagues (Yahoo has the deepest playbooks). There is no server, no API key, and no data feed — advice runs on data you paste or pages read through your own logged-in browser, and nothing ever touches your credentials.

## Quick start

1. **Install** the marketplace and plugins in your assistant (commands below).
2. **Say "set up my league"** — a one-time interview records your scoring, slots, waiver system, and playoff weeks to a `leagues.md` file. Every skill reads it from then on, so you never repeat yourself.
3. **Ask.** *"Build my draft board."* *"Who should I start?"* *"How much should I bid?"* The right skill triggers off natural phrasing — see the [table below](#plugins-and-skills).

## Install in Codex

```
codex plugin marketplace add derekrbreese/fantasy-football-skills
codex plugin add fantasy-league-setup@fantasy-football-skills
codex plugin add draft-strategy@fantasy-football-skills
codex plugin add lineup-strategy@fantasy-football-skills
codex plugin add waiver-wire@fantasy-football-skills
codex plugin add trade-analyzer@fantasy-football-skills
codex plugin add roster-ops@fantasy-football-skills
```

For live platform reads and roster operations, also install and enable the built-in Browser plugin — see [What needs a browser](#what-needs-a-browser).

## Install in Claude Code

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

Every plugin declares `fantasy-league-setup` as a dependency, so it should come along automatically; if your build doesn't pull it in, add it explicitly with `/plugin install fantasy-league-setup@fantasy-football-skills`. (Curious what the league interview will ask? A commented template lives at [`leagues-template.md`](plugins/fantasy-league-setup/skills/league-config/leagues-template.md).)

## What needs a browser

**Nothing, for advice.** Every analysis skill works from information you paste — rankings, rosters, league settings, a trade offer.

**Live reads and `roster-ops` need browser automation**: Codex's built-in Browser, [Claude in Chrome](https://www.anthropic.com/news/claude-in-chrome), or another authenticated browser your assistant supports. You sign into your fantasy platform yourself, once, in that browser — the skills use your session and never see your credentials. Without a browser, analysis skills tell you exactly what live data is missing, and `roster-ops` explains the clicks instead of making them.

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

## Where the data comes from

**This marketplace ships no data feed, platform connector, API integration, or scraper.** It works from two sources: data you paste, and pages read through your own logged-in browser — league rosters and free-agent pools, standings, transaction history, and rankings sites you have open. If you have more than one automated browser available, name the one you want; otherwise the skills use whichever has a signed-in session.

That means two things worth being clear about. There is no server anywhere holding your league data. Browser-assisted reads and `roster-ops` stop when you're logged out, while advice skills can still work from rankings, rosters, or settings you paste. The advice and execution skills share one security model: reading a page is free and needs no confirmation, but the advice skills will never click anything that changes your roster — every state change goes through `roster-ops` and its confirmation gate.

## roster-ops security model

The `roster-ops` skills drive a browser session **you are already logged into**. Plainly:

- **Your session is the auth.** The skills never ask for, read, store, or type usernames, passwords, or 2FA codes. If a login page, 2FA prompt, captcha, consent page, or unusual-activity screen appears, the assistant stops and hands the browser back to you.
- **Nothing is submitted without your explicit confirmation**, and the confirmation has to come *after* the assistant shows you what the page actually says. Saying "and submit it" up front authorizes building the transaction, never sending it.
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

# fantasy-football-skills

A fantasy football plugin marketplace for ChatGPT, Codex, and [Claude Code](https://code.claude.com/docs/en/plugin-marketplaces) — portable to flat-skill harnesses like Grok Bot ([see below](#install-in-a-flat-skill-harness-grok-bot-and-similar)): draft strategy, weekly start/sit, waiver-wire management, trade analysis, and browser-driven roster operations. Install a plugin and your assistant picks up the right skill from natural phrases like *"who should I start"*, *"work the wire"*, or *"is this trade fair"*.

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

Install and enable ChatGPT's built-in Browser plugin when you want the skills to read or operate your live fantasy platform. Sign into the platform yourself in that browser; the skills never handle credentials.

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

Each plugin declares `fantasy-league-setup` as a dependency. Current Claude Code builds expose dependency management, including auto-removal of unused dependencies; if your install does not pull `fantasy-league-setup` in automatically, install it explicitly with `/plugin install fantasy-league-setup@fantasy-football-skills`. The first time you use any skill, say *"set up my league"* — it interviews you once and writes a `leagues.md` file to your project. Every other skill reads that file for your scoring, roster slots, waiver system, and playoff weeks, so you never repeat yourself. A commented template lives at [`leagues-template.md`](plugins/fantasy-league-setup/skills/league-config/leagues-template.md).

## Install in a flat-skill harness (Grok Bot and similar)

Some agent harnesses have no plugin-bundle concept — their unit of installation is a single `SKILL.md` document (Grok Bot's workflow library, for example, imports one markdown file at a time). The skills port fine; the bundle structure doesn't. If you're adapting this marketplace to such a harness:

- Import each of the 14 `plugins/*/skills/*/SKILL.md` files individually.
- Rewrite cross-references: `plugin:skill` names (like `fantasy-league-setup:league-config`) become bare sibling names (`league-config`) — there is no namespace to qualify against.
- Inline [`leagues-template.md`](plugins/fantasy-league-setup/skills/league-config/leagues-template.md) into the bottom of `league-config` if your harness imports single documents without companion files, and point `leagues.md` at a path the agent's runtime can always reach.
- Swap the browser wording for whatever authenticated browser your harness drives; everything in the [security model](#roster-ops-security-model) — session-is-the-auth, confirmation gates, UI-never-API — must survive the port unchanged.

Expect a fork, not a mirror: flat harnesses can't track marketplace versions, so treat the imported copies as a divergent set you update by re-importing.

### Prerequisites

The analysis plugins can work from information you paste. Live reads and **`roster-ops` require browser automation** — ChatGPT's built-in Browser, [Claude in Chrome](https://www.anthropic.com/news/claude-in-chrome), or another supported authenticated browser. Sign into your fantasy platform yourself in that browser. Without browser tooling, analysis skills name the missing live-data gap and `roster-ops` explains the clicks without making them.

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

**This marketplace ships no data feed, platform connector, API integration, or scraper.** It works from data you paste, host-provided connectors, or pages read through your own logged-in browser: league rosters and free-agent pools, standings, transaction history, and rankings sites you have open. For Yahoo, an authenticated browser is the preferred live source. The skills honor a browser you explicitly name; otherwise they prefer ChatGPT's built-in Browser when it has a signed-in Yahoo session, then another available authenticated browser. A Yahoo connector that returns `403` or `unauthorized` is not retried during the same task.

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

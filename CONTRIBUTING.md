# Contributing

New skills and plugins are welcome. The bar is simple: a skill should encode *methodology* — decision rules someone could disagree with — not filler.

## Adding a skill

1. Put it in an existing plugin if it fits the theme, or propose a new plugin under `plugins/<plugin-name>/` with its own `.claude-plugin/plugin.json`.
2. Each skill is a folder: `plugins/<plugin>/skills/<skill-name>/SKILL.md` (kebab-case names).
3. New plugins must be listed in `.claude-plugin/marketplace.json` with a relative `source` path.

## SKILL.md conventions

Frontmatter — `name` and a trigger-rich `description`:

```yaml
---
name: skill-name
description: This skill should be used when the user asks "phrase one", "phrase two", "phrase three"... One sentence on what it does. One sentence on what it is NOT for, pointing to the sibling skill that covers it.
---
```

- **Triggers must not overlap.** Every natural phrase routes to exactly one skill in the marketplace. The authoritative list is the `description` frontmatter of every existing `SKILL.md` — not the README table, which shows only a couple of phrases per skill. Grep the descriptions before choosing yours:

  ```
  grep -h '^description:' plugins/*/skills/*/SKILL.md
  ```

  If your skill is adjacent to an existing one (advice vs. execution is the common case), name the boundary explicitly in both descriptions. When writing a "Not for X" clause, describe the sibling's job at a slightly higher altitude than its own trigger phrases — "Not for bid amounts" rather than "Not for sizing the bid" — so the clause doesn't hand the other skill's literal keywords to yours.
- **Keep rules and worked examples consistent.** When a skill's example contradicts its own stated rule, the model follows the example. If an example needs an exception, write the exception into the rule.
- Write the body in imperative form ("Read leagues.md first", not "You should read...").
- Skills that need league context must read `leagues.md` from the project root first, fall back to asking when it's missing or blank, point at `fantasy-league-setup:league-config` to persist the answers, and honor the `(default)` marker when multiple leagues are defined. Copy the wording from an existing skill verbatim — the contract should read identically everywhere.
- Refer to sibling skills by their full `plugin:skill` name, since that's how Claude Code addresses them. Plugins install independently, so phrase handoffs conditionally. Missing **analysis** can be done inline. Missing **transaction execution** must never be inlined into a read-only skill: provide manual steps while preserving the transaction summary and explicit confirmation boundary.
- Worked examples use **fictional players and fictional league names** only. No real league names, no personal endpoints, no references to any specific person's setup.
- Browser-automation skills (roster-ops style) must: navigate by goals and landmarks rather than brittle selectors, never handle credentials (the user's session is the auth), and pause for explicit user confirmation before any submit/confirm click.
- **Shared routing contracts live in `contracts/`.** Copy `contracts/live-source-routing.md` verbatim into every analysis skill that may read a live league page. Copy `contracts/browser-routing.md` verbatim into every `roster-ops` skill. Do not hand-edit a copy — change the contract file, then sync every consumer. The regression tests fail if a copy drifts. Honor a user-named browser first, then a `Preferred browser` value from `leagues.md`, then any authenticated session the current assistant already has. Do not hardcode ChatGPT (or any other vendor) as the default.

## Before opening a PR

```
claude plugin validate .
claude plugin validate ./plugins/<your-plugin>
```

Both must pass. Then test the install path locally:

```
/plugin marketplace add /path/to/your/clone
/plugin install <your-plugin>@fantasy-football-skills
```

Confirm your skill triggers on its phrases and does not trigger on a sibling skill's phrases.

Then run the repository's zero-dependency regression checks:

```
python3 -m unittest discover -s tests -p 'test_*.py'
```

The checks protect frontmatter, trigger uniqueness, the `leagues.md` contract,
known league-format edge cases, and roster-operation safety language. See
`tests/README.md` for the short fixture-based manual review that accompanies
them; prose checks supplement rather than replace the Claude plugin validator.

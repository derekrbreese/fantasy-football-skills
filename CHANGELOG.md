# Changelog

## 1.2.0 — 2026-08-14

- Made live-data routing generic: honor a named browser, then a
  `Preferred browser` value in `leagues.md`, then any authenticated
  session the current assistant already has. ChatGPT's browser remains a
  supported preference, not a hardcoded default.
- Extracted the routing paragraphs into `contracts/` and added a sync
  test so copies cannot drift.
- Added the live-source contract to live-draft, FAAB, drop-candidates,
  trade-negotiation, and league-config.
- `league-config` now reads the platform settings page first and only
  interviews for gaps.
- Added `lineup-strategy:weekly-briefing` as a read-only weekly
  conductor.
- Documented the Claude Code setup-plugin install command and added CI
  for the contract tests.

## 1.1.0 — 2026-08-04

- Expanded the `leagues.md` contract for season identity, verification,
  platform IDs, exact custom scoring, draft timing, and all major waiver
  priority variants while remaining backward compatible with existing files.
- Added freshness and two-source injury safeguards to lineup, waiver, and trade
  advice.
- Corrected third-round-reversal math, draft baseline labeling, keeper cost-pick
  pricing, weekly reverse-standings strategy, and conflicting trade anchors.
- Added late-swap and global lineup-allocation guidance.
- Added duplicate preflights, complete confirmation envelopes, and explicit
  terminal states to browser roster operations.
- Added fictional edge-format fixtures and zero-dependency regression checks.


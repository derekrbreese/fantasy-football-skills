from __future__ import annotations

import json
import re
import unittest
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = sorted(ROOT.glob("plugins/*/skills/*/SKILL.md"))
FIXTURE_FILES = sorted((ROOT / "tests" / "fixtures").glob("*.md"))
LIVE_SOURCE_CONTRACT = ROOT / "contracts" / "live-source-routing.md"
BROWSER_ROUTING_CONTRACT = ROOT / "contracts" / "browser-routing.md"
LIVE_SOURCE_CONSUMERS = (
    ROOT / "plugins/draft-strategy/skills/draft-prep/SKILL.md",
    ROOT / "plugins/draft-strategy/skills/live-draft-assistant/SKILL.md",
    ROOT / "plugins/draft-strategy/skills/keeper-evaluation/SKILL.md",
    ROOT / "plugins/fantasy-league-setup/skills/league-config/SKILL.md",
    ROOT / "plugins/lineup-strategy/skills/start-sit/SKILL.md",
    ROOT / "plugins/lineup-strategy/skills/weekly-briefing/SKILL.md",
    ROOT / "plugins/waiver-wire/skills/waiver-scan/SKILL.md",
    ROOT / "plugins/waiver-wire/skills/faab-bidding/SKILL.md",
    ROOT / "plugins/waiver-wire/skills/drop-candidates/SKILL.md",
    ROOT / "plugins/trade-analyzer/skills/trade-evaluation/SKILL.md",
    ROOT / "plugins/trade-analyzer/skills/trade-finder/SKILL.md",
    ROOT / "plugins/trade-analyzer/skills/trade-negotiation/SKILL.md",
)


def text(path: Path) -> str:
    """Return the UTF-8 contents of *path*."""
    return path.read_text(encoding="utf-8")


def frontmatter(path: Path) -> dict[str, str]:
    """Parse simple ``key: value`` YAML frontmatter from a skill file."""
    parts = text(path).split("---", 2)
    if len(parts) != 3:
        raise AssertionError(f"Missing YAML frontmatter: {path}")
    values: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values


def extract_paragraph(body: str, start: str) -> str:
    """Return the paragraph in *body* that begins with *start*."""
    idx = body.find(start)
    if idx < 0:
        raise AssertionError(f"missing {start!r}")
    rest = body[idx:]
    end = rest.find("\n\n")
    paragraph = rest if end < 0 else rest[:end]
    return paragraph.strip()


def extract_list_item(body: str, start: str) -> str:
    """Return the markdown list item in *body* that begins with *start*."""
    return extract_paragraph(body, start)


class SkillContractTests(unittest.TestCase):
    def test_skill_names_are_unique(self) -> None:
        names = [frontmatter(path).get("name") for path in SKILL_FILES]
        self.assertGreaterEqual(len(names), 15)
        self.assertNotIn(None, names)
        self.assertEqual(len(names), len(set(names)))

    def test_every_plugin_has_the_release_version(self) -> None:
        manifests = sorted(ROOT.glob("plugins/*/.claude-plugin/plugin.json"))
        self.assertEqual(6, len(manifests))
        for path in manifests:
            with self.subTest(path=path):
                manifest = json.loads(text(path))
                self.assertEqual("1.2.0", manifest.get("version"))

    def test_every_contextual_plugin_declares_setup_dependency(self) -> None:
        manifests = sorted(ROOT.glob("plugins/*/.claude-plugin/plugin.json"))
        for path in manifests:
            if path.parents[1].name == "fantasy-league-setup":
                continue
            with self.subTest(path=path):
                manifest = json.loads(text(path))
                self.assertIn("fantasy-league-setup", manifest.get("dependencies", []))

    def test_live_source_routing_matches_the_canonical_contract(self) -> None:
        """Require every live-data skill to copy the generic routing contract."""
        contract = text(LIVE_SOURCE_CONTRACT).strip()
        self.assertTrue(contract.startswith("**Live platform source routing.**"))
        self.assertIn("Preferred browser", contract)
        self.assertNotIn("ChatGPT's built-in Browser", contract)
        for path in LIVE_SOURCE_CONSUMERS:
            with self.subTest(path=path):
                copied = extract_paragraph(
                    text(path), "**Live platform source routing.**"
                )
                self.assertEqual(contract, copied)

        roster_skills = sorted(ROOT.glob("plugins/roster-ops/skills/*/SKILL.md"))
        self.assertEqual(3, len(roster_skills))
        browser_contract = text(BROWSER_ROUTING_CONTRACT).strip()
        self.assertNotIn("ChatGPT's built-in Browser", browser_contract)
        for path in roster_skills:
            with self.subTest(path=path):
                copied = extract_list_item(text(path), "- **Browser routing.**")
                self.assertEqual(browser_contract, copied)

        readme = text(ROOT / "README.md")
        self.assertIn("Preferred browser", readme)
        self.assertIn("any authenticated browser", readme.casefold())
        marketplace = text(ROOT / ".claude-plugin" / "marketplace.json")
        self.assertNotIn("ChatGPT", marketplace)

    def test_published_skills_do_not_hardcode_a_chatgpt_browser(self) -> None:
        """Keep ChatGPT as a user preference, not a hardcoded default."""
        for path in SKILL_FILES:
            with self.subTest(path=path):
                self.assertNotIn("ChatGPT's built-in Browser", text(path))

    def test_exact_quoted_trigger_phrases_do_not_collide(self) -> None:
        owners: dict[str, set[str]] = defaultdict(set)
        for path in SKILL_FILES:
            description = frontmatter(path)["description"]
            for phrase in re.findall(r'"([^"\n]+)"', description):
                normalized = " ".join(phrase.casefold().split())
                owners[normalized].add(str(path.relative_to(ROOT)))
        collisions = {phrase: paths for phrase, paths in owners.items() if len(paths) > 1}
        self.assertEqual({}, collisions)

    def test_contextual_skills_keep_the_leagues_markdown_contract(self) -> None:
        for path in SKILL_FILES:
            if path.parent.name == "league-config":
                continue
            with self.subTest(path=path):
                self.assertIn("Read `leagues.md` from the project root", text(path))

    def test_league_template_covers_identity_provenance_and_edge_scoring(self) -> None:
        template = text(
            ROOT
            / "plugins/fantasy-league-setup/skills/league-config/leagues-template.md"
        )
        required = (
            "- Season:",
            "- Platform league ID/key:",
            "- Timezone:",
            "- Verified:",
            "- Scoring details:",
            "return yards/TDs",
            "kicker makes/misses",
            "IDP lineup",
            "- Draft:",
            "weekly-reverse-standings",
            "- Acquisition limit:",
            "- Preferred browser:",
        )
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker, template)

    def test_verified_logic_repairs_remain_present(self) -> None:
        live_draft = text(
            ROOT
            / "plugins/draft-strategy/skills/live-draft-assistant/SKILL.md"
        )
        faab = text(ROOT / "plugins/waiver-wire/skills/faab-bidding/SKILL.md")
        start_sit = text(ROOT / "plugins/lineup-strategy/skills/start-sit/SKILL.md")
        trade = text(
            ROOT
            / "plugins/trade-analyzer/skills/trade-evaluation/SKILL.md"
        )
        self.assertIn("round-2-to-round-3 gap is exactly `N` selections", live_draft)
        self.assertIn("`N − 1` intervening picks", live_draft)
        self.assertIn(
            "`expected_takes = intervening_picks × positional share of picks`",
            live_draft,
        )
        self.assertNotIn("expected_takes = gap × positional share", live_draft)
        self.assertIn("Your next-pick gap is 11", live_draft)
        self.assertIn("10 selections occur before your turn", live_draft)
        self.assertIn(
            "the 11-pick gap is for the reach test, but only those 10 intervening selections matter for tier urgency",
            live_draft,
        )
        self.assertIn("those 10 intervening selections", live_draft)
        self.assertIn("Weekly reverse standings / recomputed priority", faab)
        self.assertIn("continual rolling", faab.casefold())
        self.assertIn("late-swap optionality", start_sit)
        self.assertIn("official team/game status", start_sit)
        self.assertIn("opening anchor", trade)
        self.assertIn("final executable offer", trade)

    def test_roster_operations_have_idempotent_terminal_states(self) -> None:
        roster_skills = sorted(ROOT.glob("plugins/roster-ops/skills/*/SKILL.md"))
        self.assertEqual(3, len(roster_skills))
        for path in roster_skills:
            body = text(path)
            with self.subTest(path=path):
                self.assertIn("verified-success", body)
                self.assertIn("verified-absent", body)
                self.assertIn("`unknown`", body)
                self.assertIn("confirmation envelope", body)
                self.assertIn("Never retry from `unknown`", body)
        self.assertIn(
            "full pending queue first",
            text(ROOT / "plugins/roster-ops/skills/submit-waiver-claim/SKILL.md"),
        )
        self.assertIn(
            "pending or outgoing trades",
            text(ROOT / "plugins/roster-ops/skills/propose-trade/SKILL.md"),
        )
        self.assertIn(
            "pre-change baseline",
            text(ROOT / "plugins/roster-ops/skills/set-lineup/SKILL.md"),
        )

    def test_worked_examples_follow_the_repaired_decision_contracts(self) -> None:
        start_sit = text(ROOT / "plugins/lineup-strategy/skills/start-sit/SKILL.md")
        set_lineup = text(ROOT / "plugins/roster-ops/skills/set-lineup/SKILL.md")
        keeper = text(
            ROOT / "plugins/draft-strategy/skills/keeper-evaluation/SKILL.md"
        )
        waiver_scan = text(
            ROOT / "plugins/waiver-wire/skills/waiver-scan/SKILL.md"
        )
        faab = text(ROOT / "plugins/waiver-wire/skills/faab-bidding/SKILL.md")
        trade = text(
            ROOT / "plugins/trade-analyzer/skills/trade-evaluation/SKILL.md"
        )
        draft_prep = text(
            ROOT / "plugins/draft-strategy/skills/draft-prep/SKILL.md"
        )

        self.assertIn("the decision deadline is 12:55 PM", start_sit)
        self.assertIn("Do not pretend Marsette remains a fallback", start_sit)
        self.assertIn("run `lineup-strategy:start-sit`", set_lineup)
        self.assertIn("never greedily fill one row at a time", set_lineup)
        self.assertIn("official status plus a second credible source", set_lineup)
        self.assertIn("captures 11 picks — just under one round", keeper)
        for exact_pick in (
            "11.10 (overall 130)",
            "3.10 (overall 34)",
            "5.10 (overall 58)",
            "8.03 (overall 87)",
        ):
            self.assertIn(exact_pick, keeper)
        self.assertIn("official IR transaction", waiver_scan)
        self.assertIn("independent beat-practice report", waiver_scan)
        self.assertIn("official transaction log", faab)
        self.assertIn("independent beat report", faab)
        self.assertIn("As of Thursday 7:00 PM ET", trade)
        self.assertIn(
            "`teams × (dedicated QB slots + QB-assigned superflex slots)`",
            draft_prep,
        )
        self.assertIn("not a universal constant", draft_prep)

    def test_fixtures_cover_the_three_edge_case_families(self) -> None:
        self.assertEqual(3, len(FIXTURE_FILES))
        combined = "\n".join(text(path).casefold() for path in FIXTURE_FILES)
        for marker in (
            "weekly-reverse-standings",
            "return yards",
            "distance",
            "3 wr",
            "league-vote",
            "rb/wr/te",
            "field-goal yards",
            "fourth-down stop",
            "keepers:",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, combined)
        for path in FIXTURE_FILES:
            body = text(path)
            with self.subTest(path=path):
                self.assertEqual(1, body.count("(default)"))
                self.assertNotIn("derekrbreese", body.casefold())

    def test_fixture_edges_map_to_explicit_consumer_rules(self) -> None:
        return_fixture = text(
            ROOT / "tests/fixtures/return-idp-reverse.md"
        ).casefold()
        wide_fixture = text(
            ROOT / "tests/fixtures/three-wr-faab-vote.md"
        ).casefold()
        keeper_fixture = text(
            ROOT / "tests/fixtures/keeper-teflex-pressure.md"
        ).casefold()
        draft = text(
            ROOT / "plugins/draft-strategy/skills/draft-prep/SKILL.md"
        ).casefold()
        faab = text(
            ROOT / "plugins/waiver-wire/skills/faab-bidding/SKILL.md"
        ).casefold()
        trade = text(
            ROOT / "plugins/trade-analyzer/skills/trade-evaluation/SKILL.md"
        ).casefold()
        keeper = text(
            ROOT / "plugins/draft-strategy/skills/keeper-evaluation/SKILL.md"
        ).casefold()
        lineup = text(
            ROOT / "plugins/lineup-strategy/skills/start-sit/SKILL.md"
        ).casefold()

        self.assertIn("weekly-reverse-standings", return_fixture)
        self.assertIn("weekly reverse standings / recomputed priority", faab)
        self.assertIn("return yards", return_fixture)
        self.assertIn("return yards", draft)
        self.assertIn("idp", return_fixture)
        self.assertIn("idp", draft)

        self.assertIn("3 wr", wide_fixture)
        self.assertIn("teams × (dedicated starters + flex_slots × flex_share)", draft)
        self.assertIn("league-vote", wide_fixture)
        self.assertIn("veto votes", trade)

        self.assertIn("rb/wr/te", keeper_fixture)
        self.assertIn("respect each slot's eligibility", lineup)
        self.assertIn("keepers: up to 2", keeper_fixture)
        self.assertIn("exact pick", keeper)
        self.assertIn("collision rule", keeper)

    def test_league_config_reads_settings_before_interviewing(self) -> None:
        """Require settings-page reads and a Preferred browser field."""
        body = text(
            ROOT / "plugins/fantasy-league-setup/skills/league-config/SKILL.md"
        )
        self.assertIn("settings page", body.casefold())
        self.assertIn("Preferred browser", body)
        self.assertIn("never silently overwrite", body.casefold())
        idx_browser = body.casefold().find("settings page")
        idx_interview = body.find("**Interview**")
        self.assertGreater(idx_browser, 0)
        self.assertGreater(idx_interview, idx_browser)

    def test_weekly_briefing_is_a_read_only_conductor(self) -> None:
        """Require the weekly conductor to hand off and never execute."""
        path = ROOT / "plugins/lineup-strategy/skills/weekly-briefing/SKILL.md"
        body = text(path)
        meta = frontmatter(path)
        self.assertEqual("weekly-briefing", meta["name"])
        self.assertIn("what should I do this week", meta["description"])
        self.assertIn("Read `leagues.md` from the project root", body)
        self.assertIn("lineup-strategy:start-sit", body)
        self.assertIn("waiver-wire:waiver-scan", body)
        self.assertIn("waiver-wire:drop-candidates", body)
        self.assertIn("roster-ops", body)
        self.assertIn("never", body.casefold())
        self.assertIn("confirmation", body.casefold())


if __name__ == "__main__":
    unittest.main()

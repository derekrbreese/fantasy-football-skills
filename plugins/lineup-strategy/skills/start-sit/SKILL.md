---
name: start-sit
description: This skill should be used when the user asks "who should I start", "start or sit", "should I start X or Y", "who do I bench", "is he a must-start", "A or B at flex", "start X over Y?", or wants a start/sit recommendation from a roster they describe or paste. Gives the recommendation itself — no browser session required. Not for applying the change on the platform (roster-ops set-lineup), picking up a replacement off waivers (waiver-wire waiver-scan), or deciding who to cut (waiver-wire drop-candidates).
---

# Start/Sit: The Weekly Call

Answer the most common question in fantasy football — who to start — from a roster the user pastes or describes. **This skill never requires a browser session**, which matters because start/sit questions usually arrive as a quick text with two names in it. If browser automation happens to be available and the user is logged in, reading their roster page saves them the typing — but never make a browser session a precondition for an opinion.

**Reading data with computer use.** If browser automation is available (Claude in Chrome or equivalent) and the user is already logged into their platform, read the pages directly instead of making them paste — league rosters, the free-agent pool, standings, transaction history, and any rankings site they have open. The session rules from `roster-ops` apply unchanged: the user's session is the auth, never ask for or type credentials, use the UI rather than platform APIs, act at human pace, and stop and hand back on any login or captcha screen.

**This skill is read-only.** Reading a page needs no confirmation, but never click anything that changes a roster, files a claim, or sends an offer from here — that is what the `roster-ops` skills and their confirmation gates exist for.

If the user also wants the lineup actually applied on their platform, hand off at the end.

## Step 1: Load league context

Read `leagues.md` from the project root first — the fields that matter here are scoring, starting slots (especially what the FLEX accepts), and playoff weeks. If the file is missing or those fields are blank, ask for them directly and suggest running the `fantasy-league-setup:league-config` skill to persist the answers. If `leagues.md` defines more than one league, use the one marked `(default)` unless the user names another.

## Step 2: Get the roster and the question

Two shapes of question, and they need different amounts of input:

- **Head-to-head** ("start Vellum or Marsh?"): only needs the two players, the slot, and the scoring type. Answer directly — do not demand a full roster.
- **Whole lineup** ("who should I start this week?"): needs the full roster with positions, plus current week. Byes and injury designations if the user has them.

Ask only for what the question actually requires. A user asking about two players does not want an intake interview.

## Step 3: Rank by expected points, then adjust

Fill each required slot with the highest expected scorer, then apply these adjustments in order:

1. **Volume over talent.** Projected touches, targets, and routes run predict weekly scoring far better than name value or last week's box score. A back with 18 touches on a bad offense usually beats a committee back on a good one.
2. **Scoring-format correction.** Slots are not format-neutral: full PPR promotes high-target pass-catching backs and slot receivers; standard scoring promotes goal-line backs; TE premium can push an elite TE ahead of a WR2 for the flex.
3. **Matchup, but only where it moves the needle.** Positional defensive splits matter (a defense stout against the run and porous against the pass), team-level defensive rank does not. Matchup is a tiebreaker between close players, never a reason to bench a clear starter — the range of outcomes for any individual player is far wider than the matchup effect.
4. **Game script and Vegas lines.** A heavy underdog throws more (helps pass-catchers, hurts early-down backs); a heavy favorite runs to close out games. The implied team total is the single best one-number matchup input available.
5. **Weather** only in the extremes — sustained wind above roughly 20 mph is the one condition that reliably suppresses passing and kicking. Cold and light rain are largely noise.

## Step 4: Floor vs. ceiling — the step most advice skips

The right answer depends on whether the user is favored, and this changes the recommendation:

- **Heavy favorite**: start the higher **floor**. Reducing variance protects a lead. Take the predictable 12-point player over the 6-or-24 player.
- **Heavy underdog**: start the higher **ceiling**, deliberately. Winning requires an outlier, and the boom/bust player is the one who supplies it. This is counterintuitive and users resist it — state the reasoning explicitly.
- **Close matchup or unknown**: start the higher median and move on.

Ask for the projected margin if the user hasn't said, or accept "I don't know" and default to median. Two related cases worth flagging: if the league's playoff tiebreaker is **points-for**, a locked-in team should still maximize points rather than coast; and a team already eliminated from playoff contention should ignore this section entirely.

## Step 5: Deliver

Give the call in the first sentence, then the reasoning. Say plainly when it is close — "these two are within a point of each other, start either and don't look back" is a legitimate and useful answer, and pretending to precision that isn't there teaches users to over-manage.

Flag anything genuinely urgent: an empty starting slot, a player on bye in the lineup, or a player already ruled out. Then offer the handoff: "to apply this on your platform, the `roster-ops:set-lineup` skill can do it in your browser — if you don't have that plugin installed, here are the clicks."

## Worked example (fictional)

"Gridiron Gazette," 12-team half-PPR, week 9. User asks: "Flex — Deion Marsette or Silas Okafor?" User is a 3.5-point favorite.

> **Start Okafor.** He's projected 11.8 to Marsette's 12.4 — Marsette is nominally higher, but that projection leans on two long touchdowns in the last three weeks, and his route share has actually fallen. Okafor's 17 projected touches with goal-line work is the steadier number, and as a favorite you want the floor. If you were the underdog I'd flip this and start Marsette for the ceiling.

Note what did the work: volume beat the projection, and the favorite/underdog framing changed the answer rather than decorating it.

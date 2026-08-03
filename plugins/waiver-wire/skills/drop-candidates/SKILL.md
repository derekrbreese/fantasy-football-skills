---
name: drop-candidates
description: This skill should be used when the user asks "who should I drop", "who's safe to cut", "make room on my roster", "who's droppable", "what's my cut list", or needs to free a roster spot for an add. Ranks the user's own roster from most to least cuttable with bye-week and playoff-schedule awareness. Not for picking the incoming player (waiver-scan) or executing the transaction (roster-ops submit-waiver-claim).
---

# Drop Candidates: The Cut List

Rank the user's roster from most-cuttable to untouchable. The default failure mode is cutting the wrong kind of player for the right reasons — this skill exists to stop bye-week panic drops of players who matter in week 16.

## Step 1: Load context

Read `leagues.md`: roster size, starters, playoff weeks, waiver system. Ask for the current roster (with byes and injury notes) and *why* a spot is needed — a one-week streamer justifies a much shallower cut than a season-long add.

## Step 2: Classify every bench player

Cut order, most cuttable first:

1. **Second K or DST** — never roster two of either outside the single week a swap is pre-staged.
2. **Expired streamers** — last week's matchup play whose matchup has passed.
3. **Redundant depth at a deep position** — the 6th WR in a 2-WR league. Redundancy is measured against *this league's* starting slots, not position-agnostic rank.
4. **Stalled lottery tickets** — stashes whose path to a role hasn't moved in 3+ weeks (signal: snap share flat or falling).
5. **Handcuffs to starters the user doesn't roster** — insurance on someone else's player pays out to that manager's schedule, not the user's.
6. **Bye-week players** (see the traps below).
7. **Injured starters and own-handcuffs** — IR-slot them if the league has IR; cutting is last resort.

## Step 3: Apply the vetoes

Before recommending any cut, check three vetoes:

- **The claim-back test**: if this player were dropped, would the user (or a rival) plausibly claim them within two weeks? If yes for a rival, don't cut for a marginal add — releasing a useful player to the league costs more than the add gains. In FAAB leagues, note that cutting hands rivals a free option.
- **Bye-week trap**: a player on bye *this* week is temporarily worthless but may be a top-3 asset. Never cut a weekly starter for their bye; stream around it (cut from classes 1–4 instead). Cutting for a bye is only correct when the player was already class 3–5.
- **Playoff-schedule veto**: from ~week 10 on, weight weeks 15–17. A mediocre bench piece with elite playoff matchups outranks a slightly better player who draws top defenses in 15–17. Conversely, "good so far" players whose playoff schedule is brutal move *up* the cut list — say so explicitly, it's counterintuitive.

## Step 4: Deliver the list

Output the roster ranked most-to-least cuttable with a one-line reason each, mark the recommended cut for the stated need, and flag any veto that applied. If nothing survives the vetoes, say the roster has no safe cut and the add must beat the *least* protected player straight up.

## Worked example (fictional)

"Mud Dogs," week 9, 12-team league, needs one spot for a TE streamer. Bench: RB Colby Trask (handcuff to a rival's starter), WR Jalen Moss (bye this week, WR3 rest of season), RB Dewey Sandoval (stash, snaps flat 4 weeks), DST #2 (Ironhogs D, added for a matchup that passed).

> 1. **Cut: Ironhogs DST** — expired streamer, class 2. Done.
> 2. Next up if another spot is needed: Dewey Sandoval — stalled stash, class 4; claim-back test passes (nobody claims a flat-snap stash).
> 3. Trask stays *ahead of Moss on the cut list* only because it's a rival's handcuff (class 5), but note: if the user faces that rival in weeks 15–17, Trask gains blocking value — playoff veto softens the cut.
> 4. **Never**: Jalen Moss. Bye-week trap — he's a weekly starter next week and a rival claims him in minutes.

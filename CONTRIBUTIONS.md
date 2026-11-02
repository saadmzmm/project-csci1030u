# Contributions

This file records **what each member personally contributed**: the slice they own, and the
commit that proves they did each topic at each milestone. It is how your team proves the
per-student topic rule in [`MILESTONES.md`](MILESTONES.md), and it is what the TA reads at
every checkpoint.

Update it **before every checkpoint** (Weeks 4, 8, 12). Keep every milestone table in this
one file - do not delete the earlier ones; the history matters.

Use each member's full name as it appears in the team table in [`README.md`](README.md),
which is where GitHub usernames are recorded.

---

## Slices

Each member owns **one comparable feature**, built end to end across the term; every
milestone adds its new topics to *each* slice. Agree on these at Milestone 0 and fill them
in - the rest of this file is one row per member, per milestone, against their slice.

| Student | Slice (the feature they own) |
|---------|------------------------------|
| Saad Moazzam | Player movement, scoring, session features, and future agent behavior |
| Irfan Nasery | World, obstacles, goals, treasure, and world validation |

The Milestone 2 file responsibilities and remaining features are described in
[`docs/MILESTONE_2_PLAN.md`](docs/MILESTONE_2_PLAN.md).

<!-- Teams of four: delete the fifth row, here and in the tables below. -->

---

## How to fill in the milestone tables

In each cell, put a **commit hash** (e.g. `a1b2c3d`) - or, if your team is using them, a
**merged pull request** (e.g. `#14`) - **authored by that student** that demonstrates that
topic **in their own slice**.

- One commit or PR can fill two cells if it genuinely covers both topics (a function that
  also holds the feature's state, say).
- A **blank cell** means that student did not demonstrate that topic for that milestone,
  and loses **those individual marks** only - it does not drag down the rest of the team.
- Get a commit hash with `git log --oneline`, and check what a hash actually contains with
  `git show a1b2c3d`. The TA will.

Worked example:

| Student | Planning | Control flow | Collections | Functions |
|---------|----------|--------------|-------------|-----------|
| Alice   | a1b2c3d  | e4f5a6b      | e4f5a6b     | 9f8e7d6   |
| Bob     | b2c3d4e  | 1c2d3e4      | 1c2d3e4     | 7a6b5c4   |

---

## Milestone 1 - Core Prototype (Units 01-02)

| Student | Planning | Control flow | Collections | Functions |
|---------|----------|--------------|-------------|-----------|
| Saad Moazzam | 9da08e0 | c37753d | c37753d | c37753d |
| Irfan Nasery | 9da08e0 | c37753d | c37753d | c37753d |

Irfan's row lists shared project references. See the Milestone 1 note at the bottom.

<!-- Optional but recommended: a line per member saying which function or file to look at. -->

## Milestone 2 - Practical Application (Unit 03)

| Student | OOP | File I/O | Recursion | Command-line args | Interface (TUI/GUI) |
|---------|-----|----------|-----------|-------------------|---------------------|
| Saad Moazzam | | | | | |
| Irfan Nasery | | | | | |

## Milestone 3 - Final Product (Units 04-05)

| Student | Data structure | Algorithm strategy | Sockets | Concurrency |
|---------|----------------|--------------------|---------|-------------|
| <name>  |                |                    |         |             |
| <name>  |                |                    |         |             |
| <name>  |                |                    |         |             |
| <name>  |                |                    |         |             |
| <name>  |                |                    |         |             |

## Milestone 1 note

For Milestone 1 we communicated through Discord. At the beginning Saad was the
only person pushing code to GitHub. Both rows reference the same project commits.
Git records Saad as their author so Irfan's entries are shared references rather
than evidence of commits authored by Irfan.

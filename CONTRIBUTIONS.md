
# Contributions

This file records each Gridworld Arena team member's **assigned feature slice**, their implementation work, and the Git commits supporting each milestone's required topics. The commit references are provided so the lab instructor can inspect the actual changes and their authors.

The project uses a single shared Git repository. Both members collaborate on integration and testing, while the required per-student evidence is tied to **commits authored by that student**, rather than merge commits alone.

## Team and feature slices

| Student | Owned slice |
|---|---|
| **Saad Moazzam** | Player movement, scoring, session state, saves/loads, route hints, and future agent behaviour |
| **Irfan Nasery** | World, obstacles, goals, treasures, map configuration, validation, and board-selection interface |

Team usernames are listed in [README.md](README.md). The historical [Milestone 2 plan](docs/MILESTONE_2_PLAN.md) describes the intended division of work.

## Milestone 1 — Core Prototype (Units 01–02)

| Student | Planning | Control flow | Collections | Functions |
|---|---|---|---|---|
| Saad Moazzam | `9da08e0` | `c37753d` | `c37753d` | `c37753d` |
| Irfan Nasery | `9da08e0` | `c37753d` | `c37753d` | `c37753d` |

**Saad's prototype work:** Initial board display, player movement, boundary/wall checks, action results, and scoring. Relevant history includes `a7ec4cf` (grid display/movement) and `c37753d` (player movement/reward system). Commit `9da08e0` records the shared project plan and assigned slices.

**Milestone 1 authorship clarification:** During the initial prototype stage, Saad handled the GitHub commits for the shared project while the team coordinated through Discord. **Irfan's Milestone 1 cells above reference shared commits authored by Saad; they are not individually authored commit evidence for Irfan.** The original record is preserved for historical accuracy.

## Milestone 2 — Practical Application (Unit 03)

The Lab 08 checkpoint requires one non-trivial, individually authored commit demonstrating each of five topics within each member's slice: OOP, file I/O, recursion, command-line arguments, and interface.

### Contribution matrix

| Student | OOP | File I/O | Recursion | Command-line args | Interface (TUI/GUI) |
|---|---|---|---|---|---|
| **Saad Moazzam** | `a8b4dd3` | `38ef25a` | `38ef25a` | `38ef25a` | `38ef25a` |
| **Irfan Nasery** | `4ad4e80` | `b5be40c` | `b5be40c` | `b5be40c` | `97fcf95` |

A commit may appear in multiple columns when it contains substantive work for multiple concepts. The implementation details below identify the work in each referenced commit. The TA can verify the changes through Git history.

### Saad Moazzam — Player and session features

| Unit 03 topic | Implementation in Saad's slice | Supporting commit(s) |
|---|---|---|
| **OOP** | Added the `HintSession` class in `gridworld/hint_session.py`, with instance state (`self.route`) and methods `__init__()`, `reset()`, and `get_next_hint()`. Integrated the class into `cli.py` so hints persist between requests and reset after loading. Earlier work added state serialization and route methods to `Player`. | `a8b4dd3`; earlier OOP methods: `38ef25a` |
| **File I/O** | Implemented combined JSON saving/loading in `gridworld/storage.py`, including player position/score and world grid; added validation and file-error handling. | `38ef25a`, `4e96d06` |
| **Recursion** | Implemented `Player.find_route()` / `_search_route()` with depth-first exploration, base cases, and visited-position tracking. | `38ef25a` |
| **Command-line args** | Added `--save-file` using `argparse`, including a default save path. | `38ef25a` |
| **Interface (TUI)** | Added `H` for hints, `V` to save, and `L` to load; displayed directions and handled file errors in the game loop. | `38ef25a`, `4e96d06` |

**Class evidence:** Commit `a8b4dd3` (Git author: `saadmzmm`) adds the new, stateful `HintSession` class and integrates it into the terminal interface. This is the primary OOP evidence in Saad's Milestone 2 matrix. The earlier `Player` class was originally introduced in `4ad4e80` by Irfan; Saad's subsequent `Player` methods are supporting work rather than a claim to the original class declaration. Git authorship and disclosure of any coding assistance are separate matters; see [AI-USAGE.md](AI-USAGE.md).

**Additional commits:**

- `601169c` — Connect player movement to treasure rewards.
- `38ef25a` — Add save load and recursive hint features.
- `4e96d06` — Improve save and load error handling.
- `a8b4dd3` — Add HintSession class for player navigation.

### Irfan Nasery — World and map features

| Unit 03 topic | Implementation in Irfan's slice | Supporting commit |
|---|---|---|
| **OOP** | Introduced the class-based structure, including a stateful `World` class with methods to manage the grid and world behaviour. | `4ad4e80` |
| **File I/O** | Added JSON map loading and world serialization/restoration functionality (`load_map`, `get_data`, and `load_data`). | `b5be40c` |
| **Recursion** | Added recursive checking of accessible cells to verify reachability of the goal and treasures. | `b5be40c` |
| **Command-line args** | Added `--map-file` to load a JSON board using `argparse`. | `b5be40c` |
| **Interface (TUI)** | Added the World Menu, board selection, preview, and map-validation controls. | `97fcf95` |

**Supporting commits:**

- `4ad4e80` — Restructure into classes.
- `b5be40c` — Add and loading recursion and option.
- `97fcf95` — Added board selection preview and map check menu.

### Integration and observed tests

The members' functionality was integrated through the shared `Game` and terminal interface. Commit `0111e56` records the merge of board-selection features with save/load and hints; merge commits document integration rather than replacing individually authored implementation evidence.

The team exercised the following scenarios during development:

- World Menu board preview, recursive map validation, and starting gameplay.
- Player movement, score updates, and one-time treasure collection (`+19` net).
- Recursive routes containing valid adjacent positions and reaching the goal without altering player score.
- `HintSession` retaining directional hints along the same route, then resetting/recalculating the route after a successful load.
- Saving and loading player position, score, and collected-treasure state through JSON.
- **Restart persistence:** saved the game at `[2, 0]` with score `18`, exited the program, restarted it, and successfully restored that position, score, and collected treasure.
- Missing or malformed save files, invalid saved player positions (while preserving active state), and unavailable save destinations.
- Combined world-selection and player-session features after the merge.

These are the cases tested; they are not a claim of exhaustive test coverage.

## Milestone 3 — Final Product (Units 04–05)

*Not yet implemented or assessed. Add individually authored commit references as work is completed.*

| Student | Data structure | Algorithm strategy | Sockets | Concurrency |
|---|---|---|---|---|
| Saad Moazzam | — | — | — | — |
| Irfan Nasery | — | — | — | — |

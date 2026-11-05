
# Gridworld Arena

**CSCI 1030U — Group Project | Milestone 2: Practical Application**

Gridworld Arena is a single-machine, terminal-based Python game. The player navigates a grid, avoids walls, collects treasures, and tries to reach the goal while earning a score. Milestone 2 extends the original prototype with classes, JSON file handling, recursion, command-line options, and an interactive terminal interface.

The Milestone 2 features described below have been implemented and tested on the example map. Reinforcement learning, networking, and concurrency are **future goals**, not current functionality.

## Team

| Full name | GitHub username |
|---|---|
| Saad Moazzam | [@saadmzmm](https://github.com/saadmzmm) |
| Irfan Nasery | [@IR-Code4i6](https://github.com/IR-Code4i6) |

Individual implementation commits are recorded in [CONTRIBUTIONS.md](CONTRIBUTIONS.md).

## Requirements and setup

- **Python:** Uses the standard library only; no `pip install` step is needed.
- **Tested environment:** Windows using the `py` launcher. The exact Python version was not recorded in the test logs.
- **Working directory:** Run commands from the repository root so relative `data/` paths resolve correctly.

Start the application:

```powershell
py main.py
```

Alternatively, where `python` is the appropriate command:

```bash
python main.py
```

Use a JSON board and choose a save-file location:

```powershell
py main.py --map-file data/maps/default.json --save-file data/saves/save.json
```

View the command-line options:

```powershell
py main.py --help
```

| Argument | Meaning | Default |
|---|---|---|
| `--map-file PATH` | Load the specified JSON map before opening the World Menu | Original board |
| `--save-file PATH` | File used by the **V** (save) and **L** (load) commands | `data/saves/save.json` |

**Note:** The directory containing the save file must already exist. The program reports a save error rather than creating a missing directory automatically.

## Using the application

### 1. World Menu

On launch, the application displays:

```text
WORLD MENU
1 - Select a board
2 - Preview board
3 - Run map check
4 - Start game
Q - Quit
```

- **1 — Select a board:** Choose the original board (`0`) or a JSON map found in `data/maps/`.
- **2 — Preview board:** Display the selected grid and its symbols.
- **3 — Run map check:** Recursively check that the goal and remaining treasures are reachable from the start.
- **4 — Start game:** Start only when the map passes the reachability check.
- **Q — Quit:** Exit from the World Menu.

For example, `data/maps/default.json` displays:

```text
P . . . T
. # . # .
T . . . .
# . # . .
. . T . G
```

### 2. Gameplay controls

| Key | Action |
|---|---|
| **W** | Move up |
| **A** | Move left |
| **S** | Move down |
| **D** | Move right |
| **H** | Show a hint for the next move toward the goal |
| **V** | Save player and world state to the selected JSON file |
| **L** | Load player and world state from the selected JSON file |
| **Q** | Quit the game |

Input is case-insensitive and surrounding spaces are ignored. Entering `Q`, or ending terminal input, exits cleanly.

**Grid symbols:** `P` = player, `#` = wall, `G` = goal, `T` = uncollected treasure, and `.` = empty cell.

### 3. Scoring

| Action | Score change |
|---|---:|
| Valid move to an empty square | `-1` |
| Blocked move (wall or outside the grid) | `-5` |
| Valid move collecting treasure | `+19` net (`-1` movement + `20` treasure) |
| Entering the goal | `+100` (replaces the normal move penalty) |
| Invalid command or requesting a hint | No change |

When a treasure is collected, its `T` becomes `.`, preventing a second reward for the same treasure. The game ends when the player reaches the goal or quits.

## Milestone 2 features

### Object-oriented design

The code separates responsibilities into four stateful classes and supporting modules:

- **`Player`** (`gridworld/player.py`): position, movement, score, player serialization, and recursive route search.
- **`HintSession`** (`gridworld/hint_session.py`): stores a hint route in `self.route`, returns the next direction, and resets the stored route after loading a game.
- **`World`** (`gridworld/world.py`): grid, walls, goal, treasures, map loading, world serialization, and reachability checks.
- **`Game`** (`gridworld/game.py`): creates and coordinates the player and world, processes turns, and detects completion.
- **`storage.py`**: reads/writes combined JSON game saves.
- **`cli.py`**: command-line options, World Menu, gameplay input, and display.

`main.py` is the entry point; it calls `main()` from `gridworld/cli.py`.

### Saving and loading (JSON)

Press **V** to save or **L** to load. A save file contains two top-level sections:

| JSON section | Data saved |
|---|---|
| `player` | `position` and `score` |
| `world` | Current `grid` and `start_position` |

The saved grid reflects collected treasures, so a treasure already collected does not reappear after loading. Saving uses `json.dump`; loading uses `json.load` and the class-specific `get_data()` / `load_data()` methods.

To avoid damaging the running game, the loader restores data into a **temporary game**, validates the saved player position, and only then replaces the active world and player. The interface also handles missing files, corrupted JSON, invalid saved positions, and unavailable save destinations by displaying an error and continuing gameplay for the tested cases.

### Recursive route hints

Press **H** to ask for a directional hint, such as `Hint: Move DOWN (S)`.

`Player.find_route()` uses recursive **depth-first search (DFS)**. It checks positions against world movement rules, records visited squares to avoid loops, and recursively explores neighbours until a route to the goal is found. A valid route is returned as a sequence of row/column positions. DFS is **not guaranteed to find the shortest route**.

The `HintSession` class remembers a calculated route so successive hints advance along it. If the player leaves that route, `HintSession.get_next_hint(player, world)` calls the recursive player method to calculate a new route. A successful load calls `HintSession.reset()` to clear the previous route. Requesting a hint neither moves the player nor changes the score.

After a reset, the recursive search can choose a **different but still valid** route because it checks neighbours in a fixed order; for example, the first hint after loading may differ from the hint displayed before saving.

### Recursive map validation

`World.check_reachability()` recursively examines accessible squares to verify that the goal and remaining treasures can be reached from the starting position. The World Menu runs this check before starting play. Map file loading also validates the supplied world data.

## Project layout

```text
project-csci1030u/
├── data/
│   ├── maps/
│   │   ├── default.json
│   │   └── README.md
│   └── saves/
│       └── .gitkeep
├── docs/
│   └── MILESTONE_2_PLAN.md
├── gridworld/
│   ├── cli.py
│   ├── game.py
│   ├── hint_session.py
│   ├── player.py
│   ├── storage.py
│   └── world.py
├── .gitignore
├── AI-USAGE.md
├── CONTRIBUTIONS.md
├── main.py
├── MILESTONES.md
└── README.md
```

Runtime save files and Python `__pycache__` output are generated locally and are not part of the source-code layout above.

## Tests performed for Milestone 2

The team manually tested the following scenarios on the example board:

| Area | Verified scenario |
|---|---|
| World interface | Board preview, recursive map check, and starting the game |
| Movement/scoring | Valid movement, treasure collected for `+19` net, and ongoing score updates |
| Recursive hints | Route begins at player, ends at goal, contains valid adjacent steps, and does not change the score |
| `HintSession` integration | Hint before movement (`DOWN`), next hint after moving (`DOWN`), and a valid fresh hint after loading (`UP` in the observed run) |
| Saving | Saved `[2, 0]`, score `18`, and the treasure-free version of that square |
| Loading | Restored position, score, and collected-treasure state |
| Save/load across restart | Saved at `[2, 0]` with score `18`, exited, launched the program again, and restored the same state with `L` |
| File errors | Missing save file, malformed JSON, invalid position `[99, 99]`, and nonexistent save directory |
| Integration | World Menu, player controls, hints, saving, and loading working together after merging changes |

Development checks also completed without errors:

```powershell
py -m compileall -q gridworld main.py
git diff --check
```

These are **observed test cases**, not a claim of exhaustive automated test coverage.

### Quick demonstration sequence

Launch with both options:

```powershell
py main.py --map-file data/maps/default.json --save-file data/saves/save.json
```

In the **World Menu**, choose `2` (preview), `3` (check), then `4` (start). During gameplay, enter `H`, `S`, `H`, `S`, `V`, and `Q`. Relaunch with the same command, choose `4`, then press `L`: the player should resume at `[2, 0]` with score `18`, and the treasure at that position should remain collected. This save/restart/load sequence was successfully demonstrated during Milestone 2 testing.

## Milestone history and future work

**Milestone 1:** Built the original playable prototype using planning, conditionals, loops, lists, functions, keyboard input, movement validation, and score calculations. The world/treasure functionality was extended during Milestone 2.

**Milestone 2:** Developed the class-based single-machine application with file I/O, recursion, command-line arguments, and TUI features described above. Added the stateful `HintSession` class to manage the output of the player's recursive route-finding algorithm.

**Milestone 3 (planned):** Explore reinforcement-learning-style decisions, additional data structures and algorithm strategies, sockets/networking, and concurrency. A possible interaction model is `State → Action → Next State → Reward`; no learning agent or multiplayer networking is claimed as implemented in Milestone 2.

## Project documents

- [MILESTONES.md](MILESTONES.md) — Project milestones and requirements.
- [CONTRIBUTIONS.md](CONTRIBUTIONS.md) — Individual feature ownership and supporting Git commits.
- [AI-USAGE.md](AI-USAGE.md) — Course AI policy and team disclosure.
- [docs/MILESTONE_2_PLAN.md](docs/MILESTONE_2_PLAN.md) — Team's original Milestone 2 work plan (supporting document, not a separate Lab 08 deliverable).
- [data/maps/README.md](data/maps/README.md) — Map data documentation.

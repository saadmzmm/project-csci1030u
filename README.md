# Gridworld Arena

## The Application

Gridworld Arena is a terminal-based grid game where a player navigates through a world containing obstacles and attempts to reach a goal.

The player moves through the grid using `W`, `A`, `S`, and `D`. The game prevents the player from moving outside the grid or through walls and uses a reward system to score different actions.

The project now has a class-based foundation for Milestone 2. The original movement, wall checks, goal, and scoring are playable. Saving/loading, command-line options, recursion, treasures, and TUI menus are upcoming Milestone 2 work. A learning agent and multiplayer networking remain later goals.

The full Milestone 2 definition of done has not been completed yet. See [the work plan](docs/MILESTONE_2_PLAN.md) for the division between Saad and Irfan.

## The Team

| Full name | GitHub username |
|-----------|-----------------|
| Saad Moazzam | @saadmzmm |
| Irfan Nasery | @IR-Code4i6  |

## Technology Plan

The project currently uses only the Python standard library.

No external dependencies are required. The current code is verified with Python 3.11.

Future milestones will continue to use standard-library features where possible, including tools such as `json`, `socket`, `threading` or `asyncio`, and potentially `tkinter` as required by later course topics.

## Running It

From the project directory, run:

```bash
python main.py
```

On Windows, the program can also be started with:

```bash
py main.py
```

The player controls are:

- `W` - move up
- `A` - move left
- `S` - move down
- `D` - move right
- `Q` - quit the game

Current grid symbols:

- `P` - player
- `#` - wall
- `G` - goal
- `.` - empty space

The current reward system is:

- Normal valid move: `-1`
- Blocked move: `-5`
- Reaching the goal: `+100`

The goal reward replaces the normal movement cost. For example, `DDDDSSSS`
reaches the goal in eight moves and scores `93`. Invalid commands do not change
the score. Input accepts uppercase letters and surrounding spaces; Q or the end
of input closes the game cleanly.

## Project Structure

```text
project-csci1030u/
|-- data/
|   |-- maps/
|   |   `-- README.md           # Explains where future map files go
|   `-- saves/
|       `-- .gitkeep            # Keeps the save folder in Git
|-- docs/
|   `-- MILESTONE_2_PLAN.md     # Work plan for Irfan and Saad
|-- gridworld/
|   |-- cli.py                 # Keyboard input and board display
|   |-- game.py                # Connects the player and world
|   |-- player.py              # Player position movement and score
|   `-- world.py               # Board walls goal and position checks
|-- .gitignore                 # Files and folders Git should ignore
|-- AI-USAGE.md
|-- CONTRIBUTIONS.md
|-- main.py                    # Starts the game
|-- MILESTONES.md
`-- README.md
```

Python may create a `__pycache__` folder when the game runs. It stores generated
cache files and is ignored by Git, so it is not included in the structure above.

`Player`, `World`, and `Game` contain game state and rules without terminal input
or printing. `cli.py` handles user interaction, and `main.py` remains the launch
command. The map and save folders reserve space for future file handling; the
application does not read or write them yet.

To prepare a world directly, create it and then call its regular `setup` method:

```python
from gridworld.world import World

world = World()
world.setup()
```

All three game classes use a regular `setup` method. To prepare a complete game:

```python
from gridworld.game import Game

game = Game()
game.setup()
```

The game setup prepares its world and player too. Call `setup` before using a new
object. The launch command already does this for you.

## Milestone 2 Ownership

- **Saad:** extend `Player`, movement and scoring, player save/load, recursive
  hints, the `--save-file` option, and player menu features.
- **Irfan:** extend `World`, boards and treasures, world save/load, recursive
  reachability checks, the `--map-file` option, and world menu features.
- **Shared:** connect the features through `Game` and the console, agree on one
  save format, and verify the complete game. Each member contributes all five
  required Milestone 2 topics through their own feature.

## Milestone 1 Planning

### Saad Moazzam - Player Movement and Reward System

**Purpose:**

Allow the player to move through Gridworld while preventing invalid movement and calculating rewards for the result of each action.

**Data:**

The player's position is stored using a list containing a row and column:

```python
player_position = [0, 0]
```

The world is represented using a nested list where each inner list represents one row of the grid.

**Steps:**

1. Display the player's current position on the grid.
2. Accept movement using `W`, `A`, `S`, or `D`.
3. Calculate the player's requested new position.
4. Check whether the new position is inside the grid.
5. Check whether the new position contains a wall.
6. Reject the movement if the position is invalid.
7. Update the player's position if the movement is valid.
8. Calculate a reward based on the result of the action.
9. Continue running the game until the player reaches the goal or chooses to quit.

**Milestone 1 concepts demonstrated:**

- Planning and problem solving
- Conditionals
- `for` and `while` loops
- Lists and nested lists
- Functions
- User input
- Boolean conditions

### Irfan Nasery - Treasure and World Reward System

**Status:** this section describes planned work. Treasure is not implemented in
the current class-based foundation.

**Purpose:**

Add collectible treasures to the Gridworld environment so the player can earn additional rewards while navigating toward the goal.

**Data:**

Treasure locations are stored in a list. Each treasure contains a row and column position.

Example:

```python
treasures = [
    [0, 4],
    [2, 0],
    [4, 2]
]
```

**Steps:**

1. Store treasure locations in a list.
2. Display remaining treasures using `T`.
3. Check whether the player moves onto a treasure location.
4. Remove a treasure from the list after it is collected.
5. Add the treasure bonus to the player's score.
6. Continue displaying only the treasures that have not already been collected.

**Milestone 1 concepts demonstrated:**

- Planning and problem solving
- Conditionals
- Lists
- Membership checking using `in`
- Functions
- Updating collections

## Reinforcement Learning Direction

The Milestone 1 prototype creates the basic environment needed for reinforcement learning.

The interaction can be represented as:

```text
State -> Action -> Next State -> Reward
```

For example:

```text
State:
Player is at [0, 0]

Action:
Move right

Next State:
Player is at [0, 1]

Reward:
-1
```

The current player manually chooses the actions.

In a future milestone, an AI agent can use these states, actions, and rewards to learn which actions lead to better total rewards.

The reward system encourages the agent to reach useful locations while avoiding unnecessary or invalid movements.

## Design

The full system architecture and Big-O analysis will be added for Milestone 3 as required by the project specification.

## Required Files

| File | What it is |
|------|------------|
| [`MILESTONES.md`](MILESTONES.md) | The project requirements and milestone expectations |
| [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) | Records each team member's feature slice and the commits that demonstrate each required topic |
| [`AI-USAGE.md`](AI-USAGE.md) | Records the team's AI usage and disclosure |
| [`docs/MILESTONE_2_PLAN.md`](docs/MILESTONE_2_PLAN.md) | Divides the next milestone's work between Saad and Irfan |

# Gridworld Arena

## The Application

Gridworld Arena is a terminal-based grid game where a player or AI agent navigates through a world containing obstacles and attempts to reach a goal.

The player moves through the grid using `W`, `A`, `S`, and `D`. The game prevents the player from moving outside the grid or through walls and uses a reward system to score different actions.

As the project develops, an AI agent will use reinforcement learning to learn which actions lead to better rewards. Later milestones will expand the game with persistent data, a user interface, multiplayer networking, and concurrent players.

For Milestone 1, the project is a single-machine terminal prototype using basic Python concepts such as functions, conditionals, loops, strings, lists, and nested lists.

## The Team

| Full name | GitHub username |
|-----------|-----------------|
| Saad Moazzam | @saadmzmm |
| Irfan Nasery | @IR-Code4i6  |

## Technology Plan

The project currently uses only the Python standard library.

No external dependencies are required for Milestone 1.

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
- `T` - treasure

The current reward system is:

- Normal valid move: `-1`
- Blocked move: `-5`
- Treasure: `+20` bonus
- Reaching the goal: `+100`

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

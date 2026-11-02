# Milestone 2 plan

The game runs and the classes are ready to extend. Here is what we still need to do.

## Saad

- Extend `Player` in `gridworld/player.py` with saving and loading of position and score.
- Add a recursive search that finds a route when the player asks for a hint.
- In `gridworld/cli.py` use `argparse` to add `--save-file` and build the player menu with hints and save/load options.

## Irfan

- Extend `World` in `gridworld/world.py` with treasures that can only be collected once.
- Add saving and loading of the board and remaining treasures. Put map files in `data/maps/`.
- Add a recursive check to see whether the goal and treasures can be reached.
- In `gridworld/cli.py` use `argparse` to add `--map-file` and build the board selection and preview menu.

## Together

- Create `gridworld/storage.py` and use one JSON save file with separate player and world sections. Keep saves in `data/saves/`.
- Connect our features in `gridworld/game.py` and agree on the treasure bonus.
- Let each other know before editing shared files.
- Save and close the game. Open it again and check that all progress is restored.
- Update the README and our own rows in `CONTRIBUTIONS.md`.
- Prepare a demo where each of us explains all five topics.

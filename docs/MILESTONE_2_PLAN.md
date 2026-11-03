# Milestone 2 plan

The game runs and the classes are ready to extend. Here is what we still need to do.

## Saad

- Extend `Player` in `gridworld/player.py` with saving and loading of position and score.
- Add a recursive search that finds a route when the player asks for a hint.
- In `gridworld/cli.py` use `argparse` to add `--save-file` and build the player menu with hints and save/load options.

## Irfan

- Done: `World` accepts `T` and returns a bonus of 20 when collected. The cell becomes `.` and cannot give another bonus.
- Done: `load_map` reads JSON maps. `data/maps/default.json` contains the first map.
- Done: `get_data` prepares the world section for saving and `load_data` restores it with the remaining treasures.
- Done: a recursive check explores connected cells and reports unreachable goals and treasures when loading a map.
- Done: `--map-file` uses `argparse` to load the selected board and show clear loading errors.
- Build the board selection and preview menu in `gridworld/cli.py`.

## Together

- Create `gridworld/storage.py` and use one JSON save file with separate player and world sections. Keep saves in `data/saves/`.
- Connect our features in `gridworld/game.py`. Treasure adds 20 to the normal move reward for a total of 19.
- Let each other know before editing shared files.
- Save and close the game. Open it again and check that all progress is restored.
- Update the README and our own rows in `CONTRIBUTIONS.md`.
- Prepare a demo where each of us explains all five topics.

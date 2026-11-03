# Map files

`default.json` contains a board with walls and a goal and three treasures.
Each map file contains `grid` and `start_position` fields.

Load a map from the project folder:

```python
from gridworld.world import World

world = World()
world.load_map("data/maps/default.json")
```

World symbols are `.` for an open cell and `#` for a wall and `G` for the goal
and `T` for treasure. Collected treasures become open cells.

The `--map-file` command-line option is still upcoming work.

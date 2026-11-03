# The game board walls goal and treasures

import json


class World:
    # Store the board and check where the player can move

    def setup(self, grid=None, start_position=None):
        if grid is None:
            grid = [
                [".", ".", ".", ".", "."],
                [".", "#", ".", "#", "."],
                [".", ".", ".", ".", "."],
                ["#", ".", "#", ".", "."],
                [".", ".", ".", ".", "G"],
            ]

        if type(grid) != list:
            raise ValueError("The board must be a list of rows.")

        if len(grid) == 0:
            raise ValueError("The board must contain at least one cell.")

        for row in grid:
            if type(row) != list:
                raise ValueError("Each board row must be a list.")

        column_count = len(grid[0])
        if column_count == 0:
            raise ValueError("The board must contain at least one cell.")

        self.grid = []
        goal_count = 0

        # Check each row and make a separate copy of the board
        for row in grid:
            if len(row) != column_count:
                raise ValueError("Every board row must have the same length.")

            new_row = []
            for tile in row:
                if tile not in [".", "#", "G", "T"]:
                    raise ValueError("Board cells must be '.', '#', 'G', or 'T'.")

                if tile == "G":
                    goal_count = goal_count + 1

                new_row.append(tile)

            self.grid.append(new_row)

        if goal_count != 1:
            raise ValueError("The board must contain exactly one goal.")

        if start_position is None:
            self.start_position = [0, 0]
        else:
            if type(start_position) != list and type(start_position) != tuple:
                raise ValueError("The starting position must contain a row and column.")
            self.start_position = list(start_position)

        if not self.is_valid_position(self.start_position):
            raise ValueError("The starting position must be on an open board cell.")

    def is_valid_position(self, position):
        # Check that a position is on the board and is not a wall
        if type(position) != list and type(position) != tuple:
            return False

        if len(position) != 2:
            return False

        row = position[0]
        column = position[1]

        # Both coordinates must be whole numbers
        if type(row) != int:
            return False
        if type(column) != int:
            return False

        if row < 0 or row >= len(self.grid):
            return False
        if column < 0 or column >= len(self.grid[row]):
            return False

        if self.grid[row][column] == "#":
            return False

        return True

    def is_goal(self, position):
        # Check whether the player is at the goal
        if not self.is_valid_position(position):
            return False

        row = position[0]
        column = position[1]

        if self.grid[row][column] == "G":
            return True

        return False

    def collect_treasure(self, position):
        # Remove treasure and return its bonus only once
        if not self.is_valid_position(position):
            return 0

        row = position[0]
        column = position[1]

        if self.grid[row][column] == "T":
            self.grid[row][column] = "."
            return 20

        return 0

    def explore_cells(self, position, visited):
        # Stop at walls and positions outside the board
        if not self.is_valid_position(position):
            return

        # Do not search the same cell again
        if position in visited:
            return

        visited.append(position.copy())
        row = position[0]
        column = position[1]

        # Search the four cells beside this one
        self.explore_cells([row - 1, column], visited)
        self.explore_cells([row + 1, column], visited)
        self.explore_cells([row, column - 1], visited)
        self.explore_cells([row, column + 1], visited)

    def check_reachability(self):
        # Find every cell connected to the starting position
        visited = []
        self.explore_cells(self.start_position, visited)

        messages = []

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                tile = self.grid[row][column]
                position = [row, column]

                if position not in visited:
                    if tile == "G":
                        messages.append(
                            f"Goal at {position} is not reachable from the starting position."
                        )
                    elif tile == "T":
                        messages.append(
                            f"Treasure at {position} is not reachable from the starting position."
                        )

        return messages

    def load_map(self, file_name):
        # Read a map file and use its world data
        with open(file_name, "r", encoding="utf-8") as map_file:
            data = json.load(map_file)

        self.load_data(data)

    def get_data(self):
        # Copy world data so it can be stored in a save file
        saved_grid = []

        for row in self.grid:
            saved_row = []
            for tile in row:
                saved_row.append(tile)
            saved_grid.append(saved_row)

        data = {
            "grid": saved_grid,
            "start_position": self.start_position.copy()
        }

        return data

    def load_data(self, data):
        # Check loaded data before replacing the current world
        if type(data) != dict:
            raise ValueError("World data must contain a grid and starting position.")

        if "grid" not in data or "start_position" not in data:
            raise ValueError("World data needs grid and start_position fields.")

        if type(data["grid"]) != list:
            raise ValueError("The saved grid must be a list of rows.")

        if type(data["start_position"]) != list:
            raise ValueError("The saved starting position must be a list.")

        loaded_world = World()
        loaded_world.setup(data["grid"], data["start_position"])

        messages = loaded_world.check_reachability()
        if len(messages) > 0:
            raise ValueError(" ".join(messages))

        self.grid = loaded_world.grid
        self.start_position = loaded_world.start_position

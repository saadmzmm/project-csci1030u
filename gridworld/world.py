# The game board walls and goal


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

        if len(grid) == 0:
            raise ValueError("The board must contain at least one cell.")

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
                if tile not in [".", "#", "G"]:
                    raise ValueError("Board cells must be '.', '#', or 'G'.")

                if tile == "G":
                    goal_count = goal_count + 1

                new_row.append(tile)

            self.grid.append(new_row)

        if goal_count != 1:
            raise ValueError("The board must contain exactly one goal.")

        if start_position is None:
            self.start_position = [0, 0]
        else:
            self.start_position = list(start_position)

        if not self.is_valid_position(self.start_position):
            raise ValueError("The starting position must be on an open board cell.")

    def is_valid_position(self, position):
        # Check that a position is on the board and is not a wall
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

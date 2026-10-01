GRID_SIZE = 5

grid = [
    [".", ".", ".", ".", "."],
    [".", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    ["#", ".", "#", ".", "."],
    [".", ".", ".", ".", "G"]
]

player_position = [0, 0]


def display_grid(grid, player_position):
    for row_index in range(len(grid)):
        display_row = []

        for column_index in range(len(grid[row_index])):
            if [row_index, column_index] == player_position:
                display_row.append("P")
            else:
                display_row.append(grid[row_index][column_index])

        print(" ".join(display_row))


def is_valid_position(position, grid):
    row = position[0]
    column = position[1]

    # Check if the row is outside the grid
    if row < 0 or row >= len(grid):
        return False

    # Check if the column is outside the grid
    if column < 0 or column >= len(grid[0]):
        return False

    # Check if the position contains a wall
    if grid[row][column] == "#":
        return False

    return True


def move_player(position, action, grid):
    new_position = position.copy()

    if action == "w":
        new_position[0] -= 1

    elif action == "s":
        new_position[0] += 1

    elif action == "a":
        new_position[1] -= 1

    elif action == "d":
        new_position[1] += 1

    if is_valid_position(new_position, grid):
        return new_position

    return position


def calculate_reward(old_position, new_position, grid):
    # Player tried to move but stayed in the same place
    if old_position == new_position:
        return -5

    row = new_position[0]
    column = new_position[1]

    # Player reached the goal
    if grid[row][column] == "G":
        return 100

    # Normal valid move
    return -1


def main():
    print("GRIDWORLD ARENA")
    print()

    current_position = player_position.copy()
    score = 0

    while True:
        display_grid(grid, current_position)

        print(f"\nScore: {score}")

        action = input("Move using W/A/S/D (Q to quit): ").lower()

        if action == "q":
            print("\nGame ended.")
            print(f"Final score: {score}")
            break

        if action not in ["w", "a", "s", "d"]:
            print("\nInvalid input. Use W, A, S, or D.\n")
            continue

        new_position = move_player(current_position, action, grid)

        reward = calculate_reward(
            current_position,
            new_position,
            grid
        )

        if new_position == current_position:
            print("\nThat move is blocked!")
        else:
            current_position = new_position

        score += reward

        print(f"Reward: {reward}")
        print()

        row = current_position[0]
        column = current_position[1]

        if grid[row][column] == "G":
            display_grid(grid, current_position)

            print("\nYou reached the goal!")
            print(f"Final score: {score}")
            break


if __name__ == "__main__":
    main()
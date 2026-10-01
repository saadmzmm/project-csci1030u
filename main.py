GRID_SIZE = 5 # Stores the size of our world, 5x5 grid

grid = [
    [".", ".", ".", ".", "."], # List containg other lists, one of these is one row
    [".", "#", ".", "#", "."], # In total we have 5 of these rows
    [".", ".", ".", ".", "."], # . = empty space, # = wall, G = goal
    ["#", ".", "#", ".", "."],
    [".", ".", ".", ".", "G"]  # If grid[1][1] = "#", then we have a wall at row 1, column 1
]

player_position = [0, 0] # stores the plater's position

def display_grid(grid, player_position):
    for row_index in range(len(grid)): 
        display_row = []

        for column_index in range(len(grid[row_index])):
            if [row_index, column_index] == player_position:
                display_row.append("P")
            else:
                display_row.append(grid[row_index][column_index])

        print(" ".join(display_row))

def move_player(position, action):
    new_position = position.copy()

    if action == "w":
        new_position[0] -= 1

    elif action == "s":
        new_position[0] += 1

    elif action == "a":
        new_position[1] -= 1

    elif action == "d":
        new_position[1] += 1

    else:
        return position

    return new_position

def main():
    print("GRIDWORLD ARENA")
    print()

    display_grid(grid, player_position)

    action = input("\nMove using W/A/S/D: ").lower()

    new_position = move_player(player_position, action)

    print()
    display_grid(grid, new_position)

if __name__ == "__main__": # If we ran main.py directly, then run the main() function
    main()
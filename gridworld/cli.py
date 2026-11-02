# Console input and display

from gridworld.game import Game


def display_grid(game):
    # Show the board with P at the player position
    grid = game.world.grid
    player_position = game.player.position

    for row_index in range(len(grid)):
        display_row = []

        for column_index in range(len(grid[row_index])):
            if [row_index, column_index] == player_position:
                display_row.append("P")
            else:
                display_row.append(grid[row_index][column_index])

        print(" ".join(display_row))


def main():
    print("GRIDWORLD ARENA\n")
    game = Game()
    game.setup()

    while not game.is_finished():
        display_grid(game)
        print(f"\nScore: {game.player.score}")

        try:
            action = input("Move using W/A/S/D (Q to quit): ")
            action = action.strip()
            action = action.lower()
        except EOFError:
            action = "q"
        except KeyboardInterrupt:
            action = "q"

        if action == "q":
            print("\nGame ended.")
            print(f"Final score: {game.player.score}")
            return

        if action not in ["w", "a", "s", "d"]:
            print("\nInvalid input. Use W, A, S, or D.\n")
            continue

        old_position = game.player.position.copy()
        reward = game.play_turn(action)
        if game.player.position == old_position:
            print("\nThat move is blocked!")
        print(f"Reward: {reward}\n")

    display_grid(game)
    print("\nYou reached the goal!")
    print(f"Final score: {game.player.score}")

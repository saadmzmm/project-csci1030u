# Console input and display

import argparse

from gridworld.game import Game
from gridworld.world import World


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
    parser = argparse.ArgumentParser(description="Play Gridworld Arena")
    parser.add_argument("--map-file", help="Path to a JSON map file")
    arguments = parser.parse_args()

    world = World()

    if arguments.map_file is None:
        world.setup()
    else:
        try:
            world.load_map(arguments.map_file)
        except OSError as error:
            parser.error(f"Cannot open map file '{arguments.map_file}': {error}")
        except ValueError as error:
            parser.error(f"Invalid map file '{arguments.map_file}': {error}")
        except RecursionError:
            parser.error("This map is too large for the recursive check. Use a smaller map.")

    print("GRIDWORLD ARENA\n")
    game = Game()
    game.setup(world)

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

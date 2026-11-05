# Console input and display

import argparse

from gridworld.game import Game
from gridworld.world import World
from gridworld.storage import save_game, load_game # allows cli to call when player selects Save or Load


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
    parser.add_argument("--save-file", default="data/saves/save.json", help="Path to a JSON save file") #4
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
    hint_route = None

    while not game.is_finished():
        display_grid(game)
        print(f"\nScore: {game.player.score}")

        try:
            action = input("W/A/S/D to move, H for hint, V to save, L to load, Q to quit") # added new options
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

        if action == "v":
            save_game(game, arguments.save_file)
            print("\n Game saved successfully! \n")
            continue

        if action == "l":
            load_game(game, arguments.save_file)
            hint_route = None
            print("\n Game loaded successfully! \n")
            continue

        if action == "h":
            if hint_route is None or game.player.position not in hint_route: #player moved out remembered route
                hint_route = game.player.find_route(game.world) # calculate a new route when necessary
            if hint_route is None:
                print("\n No route to the goal found \n")
            else:
                current_index = hint_route.index(game.player.position)

                if current_index == len(hint_route) - 1:
                    print("\nAlready at the goal!\n")
                    continue

                current_position = game.player.position
                next_position = hint_route[current_index + 1]

                if next_position[0] > current_position[0]:
                    print("Hint: Move DOWN (S)")
                elif next_position[0] < current_position[0]:
                    print("Hint: Move UP (W)")
                elif next_position[1] < current_position[1]:
                    print("Hint: Move LEFT (A)")
                elif next_position[1] > current_position[1]:
                    print("Hint: Move RIGHT (D)")
            continue

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

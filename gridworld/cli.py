
# Console input and display

import argparse
import os

from gridworld.game import Game
from gridworld.world import World
from gridworld.storage import save_game, load_game


def display_world(world, player_position):
    # Show the world with P at the player position
    grid = world.grid

    for row_index in range(len(grid)):
        display_row = []

        for column_index in range(len(grid[row_index])):
            if [row_index, column_index] == player_position:
                display_row.append("P")
            else:
                display_row.append(grid[row_index][column_index])

        print(" ".join(display_row))


def display_grid(game):
    # Use the same display for previews and gameplay
    display_world(game.world, game.player.position)


def read_input(prompt):
    # Treat the end of input as quitting
    try:
        text = input(prompt)
    except EOFError:
        return "q"
    except KeyboardInterrupt:
        return "q"

    return text.strip()


def choose_board(world):
    # Find map files inside the project map folder
    code_folder = os.path.dirname(__file__)
    project_folder = os.path.dirname(code_folder)
    maps_folder = os.path.join(project_folder, "data", "maps")

    try:
        file_names = os.listdir(maps_folder)
    except OSError as error:
        print(f"Cannot list map files: {error}")
        file_names = []

    file_names.sort()
    map_files = []

    for file_name in file_names:
        file_path = os.path.join(maps_folder, file_name)
        if file_name.endswith(".json") and os.path.isfile(file_path):
            map_files.append(file_path)

    print("\nBOARD SELECTION")
    print("0 - Original board")

    for index in range(len(map_files)):
        number = index + 1
        file_name = os.path.basename(map_files[index])
        print(f"{number} - {file_name}")

    print("Q - Back to world menu")

    while True:
        choice = read_input("Choose a board: ")
        choice = choice.lower()

        if choice == "q":
            return

        if choice == "0":
            world.setup()
            print("Original board selected.")
            return

        file_path = None
        for index in range(len(map_files)):
            number = index + 1
            if choice == str(number):
                file_path = map_files[index]

        if file_path is None:
            print("Enter a listed board number or Q.")
            continue

        try:
            world.load_map(file_path)
        except OSError as error:
            print(f"Cannot open this map: {error}")
        except ValueError as error:
            print(f"Cannot use this map: {error}")
        except RecursionError:
            print("This map is too large for the recursive check.")
        else:
            file_name = os.path.basename(file_path)
            print(f"Selected board: {file_name}")
            return


def check_board(world):
    # Show the result of the recursive map check
    try:
        messages = world.check_reachability()
    except RecursionError:
        print("This map is too large for the recursive check.")
        return False

    if len(messages) > 0:
        for message in messages:
            print(message)
        return False

    print("Map check passed. The goal and all treasures are reachable.")
    return True


def world_menu(world):
    # Choose and check the board before starting a game
    while True:
        print("\nWORLD MENU")
        print("1 - Select a board")
        print("2 - Preview board")
        print("3 - Run map check")
        print("4 - Start game")
        print("Q - Quit")

        choice = read_input("Choose an option: ")
        choice = choice.lower()

        if choice == "1":
            choose_board(world)
        elif choice == "2":
            print("\nBOARD PREVIEW")
            display_world(world, world.start_position)
            print("P = player  # = wall  G = goal  T = treasure  . = open")
        elif choice == "3":
            check_board(world)
        elif choice == "4":
            if check_board(world):
                return True
        elif choice == "q":
            print("\nGame ended.")
            return False
        else:
            print("Choose 1 to 4 or Q.")


def main():
    parser = argparse.ArgumentParser(description="Play Gridworld Arena")
    parser.add_argument("--map-file", help="Path to a JSON map file")
    parser.add_argument(
        "--save-file",
        default="data/saves/save.json",
        help="Path to a JSON save file"
    )
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

    if not world_menu(world):
        return

    game = Game()
    game.setup(world)
    hint_route = None

    while not game.is_finished():
        display_grid(game)
        print(f"\nScore: {game.player.score}")

        # Combined input handling from both versions
        action = read_input(
            "W/A/S/D to move, H for hint, V to save, L to load, Q to quit: "
        )
        action = action.lower()

        if action == "q":
            print("\nGame ended.")
            print(f"Final score: {game.player.score}")
            return

        # Save game
        if action == "v":
            try:
                save_game(game, arguments.save_file)
            except OSError as error:
                print(f"\nCannot save game: {error}\n")
            else:
                print("\nGame saved successfully!\n")
            continue

        # Load game
        if action == "l":
            try:
                load_game(game, arguments.save_file)
            except (OSError, ValueError) as error:
                print(f"\nCannot load game: {error}\n")
            else:
                hint_route = None
                print("\nGame loaded successfully!\n")
            continue

        # Recursive pathfinding hint
        if action == "h":
            if hint_route is None or game.player.position not in hint_route:
                hint_route = game.player.find_route(game.world)

            if hint_route is None:
                print("\nNo route to the goal found.\n")
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
            print("\nInvalid input. Use W, A, S, D, H, V, L, or Q.\n")
            continue

        old_position = game.player.position.copy()
        reward = game.play_turn(action)

        if game.player.position == old_position:
            print("\nThat move is blocked!")

        print(f"Reward: {reward}\n")

    display_grid(game)
    print("\nYou reached the goal!")
    print(f"Final score: {game.player.score}")

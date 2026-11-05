import json

def save_game(game, file_name):
    data = {
        "player": game.player.get_data(), # retrieves player position and score
        "world": game.world.get_data() # retreives current world incl. its grid
    }
    with open(file_name, "w", encoding="utf-8") as save_file: # open the selected file (writing)
        json.dump(data, save_file, indent=4) # saves dict as json and formats neatly

def load_game(game, file_name):
    with open(file_name, "r", encoding="utf-8") as save_file: # we are reading here
        data = json.load(save_file)

        if not isinstance(data, dict):
            raise ValueError("Save data must be a dictionary.")
        
        if "player" not in data or "world" not in data:
            raise ValueError("Missing player or world data")

        game.world.load_data(data["world"])
        game.player.load_data(data["player"])
        
        if not game.world.is_valid_position(game.player.position): # is the position valid?
            raise ValueError("Saved player position is invalid")

    #json.dump writes python data into json file
    #json.load reads json data from a file into python
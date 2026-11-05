# Player movement and scoring


class Player:
    # Store the player position and score

    def setup(self, position):
        self.position = list(position)
        self.score = 0

    def move(self, action, world):
        # Try one move and update the score before returning the reward
        if action not in ["w", "a", "s", "d"]:
            raise ValueError("Movement must be 'w', 'a', 's', or 'd'.")

        # Try the move on a copy before changing the player position
        new_position = self.position.copy()

        if action == "w":
            new_position[0] = new_position[0] - 1
        elif action == "s":
            new_position[0] = new_position[0] + 1
        elif action == "a":
            new_position[1] = new_position[1] - 1
        elif action == "d":
            new_position[1] = new_position[1] + 1

        if world.is_valid_position(new_position):
            self.position = new_position

            if world.is_goal(new_position):
                reward = 100
            else:
                reward = -1 + world.collect_treasure(new_position) # treasure move + 19
        else:
            reward = -5

        self.score = self.score + reward
        return reward

    def get_data(self): 
        return {
            "position": self.position.copy(),
            "score": self.score
        }

    def load_data(self, data):
        if not isinstance(data, dict): # checks to make sure data is a dictionary
            raise ValueError("Player data must be a dictionary.")
        
        if "position" not in data or "score" not in data: # checsk to make sure positon and score exist
            raise ValueError("Missing player data.")

        if not isinstance(data["position"], list): # checks to make sure the position is a list 
            raise ValueError("Player position must be a list.")

        if len(data["position"]) != 2: # checks to make sure the list is only 2 coordinates
            raise ValueError("Player position must contain two coordinates only. ")

        if not isinstance(data["position"][0], int) or not isinstance (data["position"][1], int): # checks to make sure the column and row are integers
            raise ValueError("Coordinates for row and column are not an integer") 

        if not isinstance(data["score"], int): # checks to make sure score is an integer
            raise ValueError("Score is not an integer")

        self.position = data ["position"].copy() # restore saved position
        self.score = data ["score"] # restore saved score

    def find_route(self, world):
        visited = []
        return self._search_route(world, self.position.copy(), visited)

    def _search_route(self, world, position, visited): #_ indicated its a internal helper method 
        if not world.is_valid_position(position): #if current pos outside grid, stop exploring that route
            return None

        if position in visited: # stops from exploring the same square again
            return None
        visited.append(position)

        if world.is_goal(position):
            return [position] # we need to return a list containing the goal position 

        directions = [
            [-1, 0], #up
            [1, 0],  #down
            [0, -1], #left
            [0, 1]   #right
        ]

        for direction in directions:
            next_position = [
                position[0] + direction[0],
                position[1] + direction[1]
            ]

            route = self._search_route(world, next_position, visited)

            if route is not None:
                return [position] + route
        return None


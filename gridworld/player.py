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

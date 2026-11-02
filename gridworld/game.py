# Connect the player and the world

from gridworld.player import Player
from gridworld.world import World


class Game:
    # Keep one player and one world together for a game

    def setup(self, world=None):
        if world is None:
            self.world = World()
            self.world.setup()
        else:
            self.world = world

        self.player = Player()
        self.player.setup(self.world.start_position)

    def is_finished(self):
        # The game is finished when the player reaches the goal
        return self.world.is_goal(self.player.position)

    def play_turn(self, action):
        # Let the player move if the game is still running
        if self.is_finished():
            raise ValueError("The game has already finished.")

        reward = self.player.move(action, self.world)
        return reward

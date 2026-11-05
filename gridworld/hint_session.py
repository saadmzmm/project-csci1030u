
class HintSession:
    """Keep track of the route used for player hints."""

    def __init__(self):
        self.route = None

    def reset(self):
        """Clear the stored route."""
        self.route = None

    def get_next_hint(self, player, world):
        """Return the next direction toward the goal."""

        # Find a new route if there is no route or the player left it.
        if self.route is None or player.position not in self.route:
            self.route = player.find_route(world)

        if not self.route:
            return "No route to the goal was found."

        current_index = self.route.index(player.position)

        if current_index == len(self.route) - 1:
            return "You are already at the goal."

        current_position = player.position
        next_position = self.route[current_index + 1]

        row_difference = next_position[0] - current_position[0]
        col_difference = next_position[1] - current_position[1]

        if row_difference == -1 and col_difference == 0:
            return "Hint: Move UP (W)"
        elif row_difference == 1 and col_difference == 0:
            return "Hint: Move DOWN (S)"
        elif row_difference == 0 and col_difference == -1:
            return "Hint: Move LEFT (A)"
        elif row_difference == 0 and col_difference == 1:
            return "Hint: Move RIGHT (D)"

        # Defensive check in case the stored route is inconsistent.
        self.reset()
        return "The saved route is invalid. Try requesting another hint."

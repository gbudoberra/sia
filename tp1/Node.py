from ColorGridStatus import Color


class Node:
    def __init__(self, status):
        self.status = status
        self.sons = set()

    def explode_node(self):
        color_values = [color for color in Color]
        for color in color_values:
            self.sons.add(Node(self.status.get_grid_son(color)))
        return self.sons

    def is_complete_state(self) -> bool:
        return self.status.is_grid_complete()

    def draw_node(self):
        self.status.draw_status()

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or type(self) != type(other):
            return False
        return self.status == other.status

    def __hash__(self):
        return hash((self.status, tuple(self.sons)))

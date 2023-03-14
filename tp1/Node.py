from ColorGridStatus import Color


class Node:
    def __init__(self, grid_status):
        self.grid_status = grid_status
        self.sons = []

    def explode_node(self):
        for color in Color.__dict__:
            self.sons.append(Node(self.grid_status.get_grid_son(color)))
        return self

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or type(self) != type(other):
            return False
        return self.grid_status == other.grid_status

    def __hash__(self):
        return hash((self.grid_status, tuple(self.sons)))

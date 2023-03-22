from enum import Enum

import matplotlib.pyplot as plt
from matplotlib import colors


class ColorGridStatus:
    def __init__(self, grid, current_color, border, colored):
        self.grid = grid
        self._current_color = current_color
        self.border = border
        self.colored = colored

    def __eq__(self, obj) -> bool:
        if self is obj:
            return True
        if obj is None or type(self) != type(obj):
            return False
        return self.border == obj.border and self.colored == obj.colored

    def __hash__(self):
        border_tuple = tuple(sorted(self.border))
        colored_tuple = tuple(sorted(self.colored))
        return hash((border_tuple, colored_tuple))

    def update_border(self, new_color):
        border = set(self.border)
        is_updated = False
        while border:
            current_cell = border.pop()
            current_row, current_col = current_cell
            if self.grid[current_row][current_col] == new_color:
                is_updated = True
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_row, new_col = current_row + dr, current_col + dc
                    if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]) and \
                            (new_row, new_col) not in self.colored and (new_row, new_col) not in border \
                            and (new_row, new_col) not in self.border:
                        self.border.add((new_row, new_col))
                        if self.grid[new_row][new_col] == new_color:
                            border.add((new_row, new_col))
                self.border.discard((current_row, current_col))
                self.colored.add((current_row, current_col))
        return is_updated

    def get_grid_son(self, color):
        grid = self.grid
        current_color = color
        border = set(self.border)
        colored = set(self.colored)

        grid_son = ColorGridStatus(grid, current_color, border, colored)
        if grid_son.update_border(current_color):
            return grid_son
        else:
            return None

    def is_grid_complete(self):
        return len(self.colored) == len(self.grid) * len(self.grid)

    def draw_status(self, name):
        matrix_colors = [[cell.value for cell in row] for row in self.grid]
        fig, ax = plt.subplots()
        ax.imshow(matrix_colors)
        plt.savefig("Graphs/" + name)
        # plt.show()
        plt.clf()

    def get_current_color(self):
        return self._current_color


def create_root(grid):
    current_color = grid[0][0]
    border = {(0, 1), (1, 0)}
    colored = {(0, 0)}
    new_status = ColorGridStatus(grid, current_color, border, colored)
    new_status.update_border(current_color)
    return new_status


class Color(Enum):
    RED = colors.to_rgba("red")
    BLUE = colors.to_rgba("blue")
    YELLOW = colors.to_rgba("yellow")
    WHITE = colors.to_rgba("white")
    GREEN = colors.to_rgba("green")
    PURPLE = colors.to_rgba("purple")

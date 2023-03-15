from matplotlib import colors
from enum import Enum
import matplotlib.pyplot as plt



class ColorGridStatus:
    def __init__(self, grid):
        self.grid = [[cell for cell in row] for row in grid]
        self._current_color = grid[0][0]
        self.border = {(0, 1), (1, 0)}
        self.colored = {(0, 0)}
        self._update_border(self._current_color)

    def __eq__(self, obj) -> bool:
        if self is obj:
            return True
        if obj is None or type(self) != type(obj):
            return False
        return self.grid == obj.grid and self.border == obj.border and self.colored == obj.colored

    def __hash__(self):
        grid_tuple = tuple(tuple(row) for row in self.grid)
        border_tuple = tuple(sorted(self.border))
        colored_tuple = tuple(sorted(self.colored))
        return hash((grid_tuple, border_tuple, colored_tuple))

    def _update_border(self, new_color):
        border = set(self.border)
        while border:
            current_cell = border.pop()
            current_row, current_col = current_cell
            if self.grid[current_row][current_col] == new_color:
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
        for current_cell in self.colored:
            current_row, current_col = current_cell
            self.grid[current_row][current_col] = new_color

    def get_grid_son(self, color):
        grid_son = ColorGridStatus(self.grid)
        grid_son._update_border(color)
        return grid_son

    def is_grid_complete(self):
        return len(self.colored) == len(self.grid) * len(self.grid)

    def draw_status(self, name):
        matrix_colors = [[cell.value for cell in row] for row in self.grid]
        fig, ax = plt.subplots()
        ax.imshow(matrix_colors)
        plt.savefig("Graphs/" + name)
        plt.show()
        plt.clf()


class Color(Enum):
    RED = colors.to_rgba("red")
    BLUE = colors.to_rgba("blue")
    YELLOW = colors.to_rgba("yellow")
    WHITE = colors.to_rgba("white")
    GREEN = colors.to_rgba("green")
    PURPLE = colors.to_rgba("purple")

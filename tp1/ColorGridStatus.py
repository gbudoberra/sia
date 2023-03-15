from matplotlib import colors


class ColorGridStatus:
    def __init__(self, grid):
        self._grid = grid
        self._current_color = grid[0][0]
        self._colored_squares = 0

        self._border = set()
        self._border.add((0, 1))
        self._border.add((1, 0))

        self._colored = set()
        self._colored.add((0, 0))

        self._update_border(self._current_color)

    def _update_border(self, new_color):
        border = set(self._border)
        while border:
            current_cell = border.pop()
            current_row, current_col = current_cell
            if self._grid[current_row][current_col] == new_color:
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_row, new_col = current_row + dr, current_col + dc
                    if 0 <= new_row < len(self._grid) and 0 <= new_col < len(self._grid[0]) and \
                            (new_row, new_col) not in self._colored and (new_row, new_col) not in border\
                            and (new_row, new_col) not in self._border:
                        self._border.add((new_row, new_col))
                        if self._grid[new_row][new_col] == new_color:
                            border.add((new_row, new_col))
                self._border.discard((current_row, current_col))
                self._colored.add((current_row, current_col))
        for current_cell in self._colored:
            current_row, current_col = current_cell
            self._grid[current_row][current_col] = new_color

    def get_grid_son(self, color):
        grid_son = ColorGridStatus(self._grid)
        grid_son._update_border(color)
        return grid_son

    def is_grid_complete(self):
        return len(self._colored) == len(self._grid) * len(self._grid)


class Color:
    RED = colors.to_rgba("red")
    BLUE = colors.to_rgba("blue")
    YELLOW = colors.to_rgba("yellow")
    WHITE = colors.to_rgba("white")
    GREEN = colors.to_rgba("green")
    PURPLE = colors.to_rgba("purple")

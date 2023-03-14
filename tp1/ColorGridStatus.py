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
        border_update = True
        border = []
        border.extend(self._border)
        while border_update:
            border_update = False
            for cell in border:
                if self._grid[cell[0]][cell[1]] is new_color:
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        r, c = cell[0] + dr, cell[1] + dc
                        if 0 <= r < len(self._grid) and 0 <= c < len(self._grid[0]):
                            self._border.add((r, c))
                            if self._grid[r][c] is new_color and (r, c) not in self._colored:
                                border.append((r, c))
                                border_update = True
                    self._border.remove((cell[0], cell[1]))
                    self._colored.add((cell[0], cell[1]))
                    border.remove((cell[0], cell[1]))
                else:
                    border.remove((cell[0], cell[1]))
        for cell in self._colored:
            self._grid[cell[0]][cell[1]] = new_color

    def get_grid_son(self, color):
        grid_son = ColorGridStatus(self._grid)
        grid_son._update_border(color)
        return grid_son

    def is_grid_complete(self):
        return len(self._colored) == len(self._grid) * len(self._grid)


class Color:
    RED = 1
    BLUE = 2
    YELLOW = 3
    WHITE = 4
    GREEN = 5
    PURPLE = 6

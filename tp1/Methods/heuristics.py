from tp1.Node import Node


def heuristic_border_colors(node: Node):
    border_colors = set()
    for coordinates in node.status.border:
        x, y = coordinates
        border_colors.add(node.status.grid[x][y])
    return len(border_colors)


def heuristic_grid_remaining_colors(node: Node):
    grid = node.status.grid
    colors = set()

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) in node.status.colored:
                pass
            else:
                colors.add(grid[x][y].name)
    return len(colors)


def heuristic_cells_pending_per_color_remaining(node: Node):
    colors = heuristic_grid_remaining_colors(node)
    if colors == 0:
        return 0
    cells = len(node.status.grid) * len(node.status.grid[0]) - len(node.status.colored)
    return cells / colors


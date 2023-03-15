from tp1.Node import Node


def heuristic_border_colors(node: Node):
    border_colors = set()
    for coordinates in node.status.border:
        x, y = coordinates
        border_colors.add(node.status.grid[x][y])
    return len(border_colors)

from Methods.star_a import StarA
from Methods.dfs import Dfs
from Methods.bfs import Bfs
from Methods.greedy import Greedy

from ColorGridStatus import ColorGridStatus
from queue import LifoQueue
from utils import parse_input_file


if __name__ == '__main__':
    matrix, method = parse_input_file("matrix.txt")
    step = 1
    grid = ColorGridStatus(matrix)

    if method == 'dfs':
        tree = Dfs(grid)
    elif method == 'bfs':
        tree = Bfs(grid)
    elif method == 'A*':
        tree = StarA(grid)
    elif method == 'greedy':
        tree = Greedy(grid)
    else:
        raise IOError("Unknown method provided")

    node = tree.search_solution()
    stack = LifoQueue()
    while node is not None:
        stack.put(node)
        node = node.get_parent()
    while not stack.empty():
        node = stack.get()
        node.draw_node("node_" + str(step))
        step += 1

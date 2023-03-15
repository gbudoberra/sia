from ColorGridStatus import create_root
from Methods.bfs import Bfs
from Methods.dfs import Dfs
from Methods.greedy import Greedy
from Methods.star_a import StarA
from utils import parse_input_file, color_matrix, draw_matrix

if __name__ == '__main__':
    matrix, method = parse_input_file("matrix.txt")
    step = 0
    grid = create_root(matrix)

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
    solution = []
    while node is not None:
        solution.append(node)
        node = node.get_parent()
    solution.reverse()
    for node in solution:
        color_matrix(matrix, node.get_status().get_current_color(), node.get_status().colored)
        draw_matrix(matrix, step)
        step += 1

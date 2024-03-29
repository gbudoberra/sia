import sys
import timeit

from tp1.ColorGridStatus import Color, create_root
from tp1.Methods.bfs import Bfs
from tp1.Methods.dfs import Dfs
from tp1.Methods.greedy import Greedy
from tp1.Methods.heuristics import heuristic_grid_remaining_colors
from tp1.Methods.star_a import StarA
from tp1.utils import color_matrix, parse_input_file, draw_matrix

matrix = [
        [Color.GREEN, Color.PURPLE, Color.BLUE, Color.RED, Color.BLUE, Color.BLUE, Color.WHITE],
        [Color.WHITE, Color.RED, Color.WHITE, Color.GREEN, Color.RED, Color.RED, Color.PURPLE],
        [Color.WHITE, Color.YELLOW, Color.RED, Color.GREEN, Color.YELLOW, Color.GREEN, Color.PURPLE],
        [Color.YELLOW, Color.RED, Color.GREEN, Color.GREEN, Color.BLUE, Color.RED, Color.WHITE],
        [Color.WHITE, Color.PURPLE, Color.PURPLE, Color.PURPLE, Color.WHITE, Color.PURPLE, Color.RED],
        [Color.WHITE, Color.WHITE, Color.WHITE, Color.PURPLE, Color.WHITE, Color.RED, Color.RED],
        [Color.WHITE, Color.WHITE, Color.RED, Color.GREEN, Color.PURPLE, Color.RED, Color.YELLOW]
    ]

node = None


def run() -> None:
    global node
    node = tree.search_solution()


if __name__ == '__main__':
    f = open('output.csv', 'a')
    f_initial_cond = open('initial_conditions.txt', 'a')
    sys.stdout = f
    matrix, method = parse_input_file("conf.json")
    step = 0
    grid = create_root(matrix)

    f_initial_cond.write(str(matrix) + "\n")

    #print("dimension;method;time;cost;boundary_set_size")
    for method in ['dfs', 'greedy', 'A*', 'bfs']:
        for i in range(5):
            if method == 'dfs':
                tree = Dfs(grid)
            elif method == 'bfs':
                tree = Bfs(grid)
            elif method == 'A*':
                tree = StarA(grid, heuristic_grid_remaining_colors)
            elif method == 'greedy':
                tree = Greedy(grid, heuristic_grid_remaining_colors)

            execution_time = timeit.timeit(run, number=1)
            print(str(len(matrix)), end=";")
            print(method, end=";")
            print(str(execution_time), end=";")
            print(str(tree.get_cost()), end=";")
            print(str(tree.boundary_nodes_size()), end=";")
            print(str(tree.get_nodes_exploded_size()), end="\n")

            solution = []
    while node is not None:
        solution.append(node)
        node = node.get_parent()
    solution.reverse()
    # print("Solution: ", end="")
    for node in solution:
        # print(node.get_status().get_current_color().name, end=" ")
        color_matrix(matrix, node.get_status().get_current_color(), node.get_status().colored)
        draw_matrix(matrix, step)
        step += 1

    # Restaura la salida estándar
    sys.stdout = sys.__stdout__
    f.close()

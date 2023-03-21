import sys
import timeit

from ColorGridStatus import create_root
from Methods.heuristics import heuristic_border_colors
from Methods.heuristics import heuristic_cells_pending_per_color_remaining
from Methods.heuristics import heuristic_grid_remaining_colors
from Methods.star_a import StarA
from utils import parse_input_file
from utils import color_matrix, parse_input_file, draw_matrix


node = None


def run() -> None:
    global node
    node = tree.search_solution()


if __name__ == '__main__':
    f = open('heuristic_output.csv', 'a')
    f_initial_cond = open('initial_conditions.txt', 'a')
    sys.stdout = f
    matrix, method = parse_input_file("conf.json")
    step = 0
    grid = create_root(matrix)

    f_initial_cond.write(str(matrix) + "\n")

    # print("dimension;method;time;cost;boundary_set_size")
    for method in ['heuristic_border_colors',
                   'heuristic_grid_remaining_colors', 'heuristic_cells_pending_per_color_remaining']:
        for i in range(5):
            if method == 'heuristic_border_colors':
                tree = StarA(grid, heuristic_border_colors)
            elif method == 'heuristic_grid_remaining_colors':
                tree = StarA(grid, heuristic_grid_remaining_colors)
            elif method == 'heuristic_cells_pending_per_color_remaining':
                tree = StarA(grid, heuristic_cells_pending_per_color_remaining)
            execution_time = timeit.timeit(run, number=1)
            print(str(len(matrix)), end=";")
            print(method, end=";")
            print(str(execution_time), end=";")
            print(str(tree.get_cost()), end=";")
            print(str(tree.boundary_nodes_size()), end="\n")

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

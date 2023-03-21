from tp1.ColorGridStatus import create_root
from tp1.Methods.star_a import StarA
from tp1.utils import random_grid
from tp1.Methods.heuristics import heuristic_border_colors, heuristic_grid_remaining_colors, heuristic_cells_pending_per_color_remaining
import sys

if __name__ == '__main__':
    f_initial_cond = open('matrix.txt', 'a')
    dim = 10
    f = open('heuristic_output_' + str(dim) + '.csv', 'a')
    sys.stdout = f

    print("dimension;method;time;cost;boundary_set_size")
    for i in range(10):
        matrix = random_grid(dim, 6)
        f_initial_cond.write(str(matrix) + "\n")
        tree1 = StarA(create_root(matrix), heuristic_grid_remaining_colors)
        tree2 = StarA(create_root(matrix), heuristic_border_colors)
        tree3 = StarA(create_root(matrix), heuristic_cells_pending_per_color_remaining)

        node1 = tree1.search_solution()
        node2 = tree2.search_solution()
        node3 = tree3.search_solution()

        print(str(len(matrix)), end=";")
        print('heuristic_grid_remaining_colors', end=";")
        print(str(0), end=";")
        print(str(tree1.get_cost()), end=";")
        print(str(tree1.boundary_nodes_size()), end="\n")

        print(str(len(matrix)), end=";")
        print('heuristic_border_colors', end=";")
        print(str(0), end=";")
        print(str(tree2.get_cost()), end=";")
        print(str(tree2.boundary_nodes_size()), end="\n")

        print(str(len(matrix)), end=";")
        print('heuristic_cells_pending_per_color_remaining', end=";")
        print(str(0), end=";")
        print(str(tree3.get_cost()), end=";")
        print(str(tree3.boundary_nodes_size()), end="\n")

    # Restaura la salida estándar
    sys.stdout = sys.__stdout__
    f.close()


from tp1.ColorGridStatus import create_root
from tp1.Methods.star_a import StarA
from tp1.utils import random_grid
from tp1.Methods.heuristics import heuristic_border_colors, heuristic_grid_remaining_colors, heuristic_cells_pending_per_color_remaining
import sys

def print_to_csv(tree, name, dim):
    print(dim, end=";")
    print(name, end=";")
    print(str(0), end=";")
    print(str(tree.get_cost()), end=";")
    print(str(tree.boundary_nodes_size()), end=";")
    print(str(tree.get_nodes_exploded_size()), end="\n")

if __name__ == '__main__':
    f_initial_cond = open('matrix.txt', 'a')
    dim = 10
    f = open('heuristic_output_' + str(dim) + '.csv', 'a')
    sys.stdout = f

    print("dimension;method;time;cost;boundary_set_size;exploded_nodes")
    for i in range(10):
        matrix = random_grid(dim, 6)
        f_initial_cond.write(str(matrix) + "\n")
        tree1 = StarA(create_root(matrix), heuristic_grid_remaining_colors)
        tree2 = StarA(create_root(matrix), heuristic_border_colors)
        tree3 = StarA(create_root(matrix), heuristic_cells_pending_per_color_remaining)

        node1 = tree1.search_solution()
        node2 = tree2.search_solution()
        node3 = tree3.search_solution()

        print_to_csv(tree1, 'heuristic_grid_remaining_colors', dim)
        print_to_csv(tree2, 'heuristic_border_colors', dim)
        print_to_csv(tree3, 'heuristic_cells_pending_per_color_remaining', dim)

    # Restaura la salida estándar
    sys.stdout = sys.__stdout__
    f.close()


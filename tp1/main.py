import sys
import timeit

from tp1.ColorGridStatus import Color, create_root
from tp1.Methods.bfs import Bfs
from tp1.Methods.dfs import Dfs
from tp1.Methods.greedy import Greedy
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
    f = open('output.txt', 'a')
    sys.stdout = f
    matrix, method = parse_input_file("conf.json")
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

    print("--------------------\nDimension: " + str(len(matrix)) + "\nMethod: " + method + "\n\nMemory information:\n")

    execution_time = timeit.timeit(run, number=1)
    print("Time (s): " + str(execution_time))
    print("Costo: " + str(tree.get_cost()))
    print("Cantidad de nodos fronteras: " + str(tree.boundary_nodes_size()))
    solution = []
    while node is not None:
        solution.append(node)
        node = node.get_parent()
    solution.reverse()
    print("Solution: ", end="")
    for node in solution:
        print(node.get_status().get_current_color().name, end=" ")
        color_matrix(matrix, node.get_status().get_current_color(), node.get_status().colored)
        draw_matrix(matrix, step)
        step += 1
    print("")

    # Restaura la salida estándar
    sys.stdout = sys.__stdout__
    f.close()

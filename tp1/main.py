import random
from Methods.dfs import Dfs
from Methods.bfs import Bfs
from ColorGridStatus import ColorGridStatus
from ColorGridStatus import Color
import matplotlib.pyplot as plt
from queue import LifoQueue



def random_grid(dim, colours):
    generating_matrix = []
    for i in range(dim):
        row = []
        for j in range(dim):
            random_colour = random.choice(colours)
            row.append(random_colour)
        generating_matrix.append(row)
    return generating_matrix


if __name__ == '__main__':

    # if len(sys.argv) < 3:
    #     raise Exception("Provide a board dimension and number of colors as parameter")
    # if not sys.argv[1].isnumeric() or sys.argv[1] <= 0:
    #     raise Exception("Provide a correct board dimension")
    # if not sys.argv[2].isnumeric() or sys.argv[2] <= 0:
    #     raise Exception("Provide a correct number of colors")

    #
    colours = [Color.RED, Color.BLUE, Color.YELLOW, Color.WHITE, Color.GREEN, Color.PURPLE]
    # matrix = [[Color.YELLOW, Color.BLUE, Color.RED, Color.RED],
    #           [Color.BLUE, Color.RED, Color.RED, Color.RED],
    #           [Color.RED, Color.RED, Color.RED, Color.RED],
    #           [Color.RED, Color.RED, Color.RED, Color.RED]
    #           ]
    # # crea una figura y un eje
    matrix = random_grid(4, colours)
    matrix_colors = [[cell.value for cell in row] for row in matrix]
    fig, ax = plt.subplots()
    # muestra la matriz en el eje
    ax.imshow(matrix_colors)
    # muestra el gráfico
    plt.show()
    plt.clf()
    step = 1
    grid = ColorGridStatus(matrix)
    tree = Bfs(grid)
    node = tree.search_solution()
    stack = LifoQueue()
    while node is not None:
        stack.put(node)
        node = node.get_parent()
    while not stack.empty():
        node = stack.get()
        node.draw_node("node_" + str(step))
        step += 1

    # grid = ColorGridStatus(matrix)
    #
    # for i in range(100):
    #     color = random.choice(colours);
    #     print("painting " + str(color))
    #     grid._update_border(color)
    #     # crea una figura y un eje
    #     fig, ax = plt.subplots()
    #     # muestra la matriz en el eje
    #     ax.imshow(grid._grid)
    #     # muestra el gráfico
    #     plt.show()
    #     plt.clf()
    #
    # print(grid.is_grid_complete())
    # print(grid._border)
    # print(grid._colored)
    #
    # # root = Node(grid)
    # # graph = Graph(root)
    # # graph.get_solution_by_dfs()

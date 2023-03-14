import random
from ColorGridStatus import Color
from tree import Graph
from ColorGridStatus import ColorGridStatus
from Node import Node
import sys
import matplotlib.pyplot as plt


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

    colours = [Color.RED, Color.BLUE, Color.YELLOW, Color.WHITE, Color.GREEN, Color.PURPLE]
    matrix = [[Color.YELLOW, Color.BLUE, Color.RED, Color.RED],
              [Color.BLUE, Color.RED, Color.RED, Color.RED],
              [Color.RED, Color.RED, Color.RED, Color.RED],
              [Color.RED, Color.RED, Color.RED, Color.RED]
              ]
    # matrix = random_grid(4, colours)
    grid = ColorGridStatus(matrix)

    # crea una figura y un eje
    fig, ax = plt.subplots()

    # muestra la matriz en el eje
    ax.imshow(grid._grid)

    # muestra el gráfico
    plt.show()
    plt.clf()

    grid._update_border(Color.BLUE)

    # crea una figura y un eje
    fig, ax = plt.subplots()

    # muestra la matriz en el eje
    ax.imshow(grid._grid)

    # muestra el gráfico
    plt.show()
    plt.clf()

    grid._update_border(Color.RED)

    # crea una figura y un eje
    fig, ax = plt.subplots()

    # muestra la matriz en el eje
    ax.imshow(grid._grid)

    # muestra el gráfico
    plt.show()
    plt.clf()

    print(grid.is_grid_complete())
    # root = Node(grid)
    # graph = Graph(root)
    # graph.get_solution_by_dfs()

import random

import matplotlib.pyplot as plt

from ColorGridStatus import Color

import json

def random_grid(dim, colors):
    colours = [Color.RED, Color.BLUE, Color.YELLOW, Color.WHITE, Color.GREEN, Color.PURPLE]
    colours = colours[:colors]
    generating_matrix = []
    for i in range(dim):
        row = []
        for j in range(dim):
            random_colour = random.choice(colours)
            row.append(random_colour)
        generating_matrix.append(row)
    return generating_matrix


def parse_input_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        properties = json.loads(content)
        dim = properties['dimension']
        method = properties['method']
        colors = properties['colors']
        if colors > 6:
            raise IOError("The maximum number of colors is 6")
        if colors < 2:
            raise IOError("The minimum number of colors is 2")
        rows = properties['matrix']
        # dim = int(content.split()[0])
        # method = content.split()[1]
        # rows = [row.strip('[]').split() for row in content.split('\n')[2:-1]]
        if len(rows) == 0:
            return random_grid(dim, colors), method
        elif len(rows) == dim:
            raise IOError("The dimension provided does not agree with the matrix provided")
        colour_matrix = []
        for row in rows:
            if len(row) is not dim:
                raise IOError("The dimension provided does not agree with the matrix provided")
            colour_row = []
            for color_value in row:
                colour_enum = Color.__members__.get(color_value)
                colour_row.append(colour_enum)
            colour_matrix.append(colour_row)
    return colour_matrix, method


def color_matrix(matrix, color, coordinates):
    for coords in coordinates:
        matrix[coords[0]][coords[1]] = color
    return matrix


def draw_matrix(matrix, step):
    matrix_colors = [[cell.value for cell in row] for row in matrix]
    fig, ax = plt.subplots()
    ax.imshow(matrix_colors)
    plt.savefig("Graphs/step_" + str(step))
    plt.clf()

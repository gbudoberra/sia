from ColorGridStatus import Color
import random


def random_grid(dim):
    colours = [Color.RED, Color.BLUE, Color.YELLOW, Color.WHITE, Color.GREEN, Color.PURPLE]
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
        dim = int(content.split()[0])
        method = content.split()[1]
        rows = [row.strip('[]').split() for row in content.split('\n')[2:-1]]
        if len(rows) == 0:
            return random_grid(dim), method
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



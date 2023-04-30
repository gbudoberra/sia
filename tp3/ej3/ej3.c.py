from PIL import Image
import numpy as np
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron


def output_matrix(n):
    diag = [-1 for _ in range(n)]
    matriz = -1 * np.eye(n, dtype=int) + np.ones((n, n), dtype=int) + np.diag(diag)
    return -1 * matriz


def load_number_image(png_filename):
    image = Image.open(png_filename)
    array = np.array(image)
    binary_array = (array[:, :, 0] < 128).astype(int)
    return binary_array


def initialize_points(filename):
    parsing_png_points = []
    for i in range(10):
        name = f'{i}' + filename + ".png"
        image_matrix = load_number_image(name)
        parsing_png_points.append(np.ravel(image_matrix))
    return parsing_png_points


if __name__ == '__main__':

    points = initialize_points("_digit")
    points_with_error = initialize_points("_digit_with_error")
    expected = [row.tolist() for row in output_matrix(10)]
    perceptron_by_layer = [len(points[0]) + 1, 50, 20, 10]

    perceptron = MultiLayerPerceptron(perceptron_by_layer, points, "step", expected, 0, 0.1,"adam")
    perceptron.train()

    print("finished")
    for i in range(10):
        test_matrix = load_number_image(str(i) + "_digit_with_error.png")
        test = np.ravel(test_matrix)
        print("--------------------------")
        print("Expected: " + str(i))
        print("Result:" + str(perceptron.get_result(test)))
        print("--------------------------")
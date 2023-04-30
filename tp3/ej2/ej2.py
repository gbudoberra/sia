import csv

import numpy as np
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron


def parse_csv(csv_file="TP3-ej2-conjunto.csv"):
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        parsing_points = []
        parsing_expected = []
        for row in reader:
            x1, x2, x3, y = [float(i) for i in row]
            parsing_points.append([x1, x2, x3])
            parsing_expected.append([y])
        return parsing_points, parsing_expected


def rescale_expected(expected_values, min_from_interval, max_from_interval):
    expected_array = np.ravel(expected_values)
    min_expected = min(expected_array)
    max_expected = max(expected_array)
    rescaled_values = [(value - min_expected) * (max_from_interval - min_from_interval) / (
            max_expected - min_expected) + min_from_interval for value in expected_array]
    return [[value] for value in rescaled_values]


if __name__ == '__main__':
    points, expected = parse_csv()
    expected = rescale_expected(expected, -1, 1)
    perceptron = MultiLayerPerceptron(
        [len(points[0]) + 1,  len(expected[0])],
        points,
        "tanh",
        expected,
        0.01, 0.1, update_method="gradient_descent"
    )
    perceptron.train()
    for point, expected_v in zip(points, expected):
        print("obtenido: " + str(perceptron.get_result(point)) + "; expected: " + str(expected_v))

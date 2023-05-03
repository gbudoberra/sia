from tp3.ej3.utils.ej3_C_utils import vary_update_method, initialize_points, output_matrix, vary_learning_rate
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron

values = [
    {'digit': 0, 'expected': [1, -1, -1, -1, -1, -1, -1, -1, -1, -1]},
    {'digit': 1, 'expected': [-1, 1, -1, -1, -1, -1, -1, -1, -1, -1]},
    {'digit': 2, 'expected': [-1, -1, 1, -1, -1, -1, -1, -1, -1, -1]},
    {'digit': 3, 'expected': [-1, -1, -1, 1, -1, -1, -1, -1, -1, -1]},
    {'digit': 4, 'expected': [-1, -1, -1, -1, 1, -1, -1, -1, -1, -1]},
    {'digit': 5, 'expected': [-1, -1, -1, -1, -1, 1, -1, -1, -1, -1]},
    {'digit': 6, 'expected': [-1, -1, -1, -1, -1, -1, 1, -1, -1, -1]},
    {'digit': 7, 'expected': [-1, -1, -1, -1, -1, -1, -1, 1, -1, -1]},
    {'digit': 8, 'expected': [-1, -1, -1, -1, -1, -1, -1, -1, 1, -1]},
    {'digit': 9, 'expected': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 1]}
]

if __name__ == '__main__':
    points = initialize_points("_digit")
    points_with_error = initialize_points("_digit_with_error")
    expected = [row.tolist() for row in output_matrix(10)]
    perceptron_by_layer = [len(points[0]) + 1, 50, 20, 10]

    perceptron_adam = MultiLayerPerceptron(perceptron_by_layer, points, "step", expected, 0.00001, 0.1, "adam")
    perceptron_adam.train()
    perceptron_gd = MultiLayerPerceptron(perceptron_by_layer, points, "step", expected, 0.00001, 0.1,
                                         "gradient_descent")
    perceptron_gd.train()

    noises = [70, 160, 255]
    times = 100

    vary_update_method(times, noises, values, perceptron_adam, perceptron_gd)

    learning_rates = [(0.1 + 0.1 * i) for i in range(10)]
    perceptrons_a = [MultiLayerPerceptron(perceptron_by_layer, points, "step", expected, 0.00001, learning_rate, "adam")
                   for learning_rate in learning_rates]

    perceptrons_b = [MultiLayerPerceptron(perceptron_by_layer, points, "step", expected, 0.00001, learning_rate, "gradient_descent")
               for learning_rate in learning_rates]

    vary_learning_rate(times, values, perceptrons_a, perceptrons_b, learning_rates, 160)

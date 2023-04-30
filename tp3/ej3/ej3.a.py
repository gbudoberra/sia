from tp3.configurations.jsonReader import JsonReader
from tp3.ej1.ej1 import plot_result, plot_error
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron

if __name__ == '__main__':

    config = JsonReader("./configurations/conf_A.json")

    update_methods = ["adam", "gradient_descent"]

    activation_methods = ["sigmoid", "tanh"]

    or_colors = ['r', 'r', 'b', 'b']

    for activation_method in activation_methods:
        for update_method in update_methods:
            points = config.points
            expected = config.expected
            perceptron = MultiLayerPerceptron(
                [len(points[0]) + 1, 10, 10, len(expected[0])],
                points,
                activation_method,
                expected,
                0.1, 0.1, update_method=update_method
            )
            perceptron.train()
            plot_result(perceptron.weights_by_layer[0][0][0], perceptron.weights_by_layer[0][0][1],
                        perceptron.weights_by_layer[0][0][2], points, or_colors, "./ej3/or_result.png")
            plot_error(perceptron.error_by_iteration, "./ej3/or_error.png")

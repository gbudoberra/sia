from tp3.configurations.jsonReader import JsonReader
from tp3.ej1.ej1 import plot_result, plot_error
from tp3.ej3.utils.graph_utils import plot_multiple_weight, plot_perceptrons_vs_iterations
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron

if __name__ == '__main__':

    config = JsonReader("./configurations/conf_A.json")

    update_methods = ["adam", "gradient_descent"]

    activation_methods = ["step", "step"]

    save_files = ["./ej3a_adam_perceptrons_vs_iter.png", "./ej3a_gradient_perceptrons_vs_iter.png"]

    or_colors = ['r', 'r', 'b', 'b']
    layers = [[[], [], []], [[], [], []]]
    iterations = [[], []]
    for save_file, update_method, activation_method, iteration, layer in zip(save_files, update_methods, activation_methods, iterations, layers):
        for perceptrons in range(1, 10):
            points = config.points
            expected = config.expected
            perceptron = MultiLayerPerceptron(
                [len(points[0]) + 1, perceptrons, len(expected[0])],
                points,
                activation_method,
                expected,
                0.00000001, 0.1, update_method=update_method
            )
            perceptron.train()
            iteration.append(len(perceptron.error_by_iteration))
        layer[0].append(iteration)
        for perceptrons in range(1, 10):
            points = config.points
            expected = config.expected
            perceptron = MultiLayerPerceptron(
                [len(points[0]) + 1, perceptrons, perceptrons, len(expected[0])],
                points,
                activation_method,
                expected,
                0.00000001, 0.1, update_method=update_method
            )
            perceptron.train()
            iteration.append(len(perceptron.error_by_iteration))
        layer[1].append(iteration)
        for perceptrons in range(1, 10):
            points = config.points
            expected = config.expected
            perceptron = MultiLayerPerceptron(
                [len(points[0]) + 1, perceptrons, perceptrons, perceptrons, len(expected[0])],
                points,
                activation_method,
                expected,
                0.00000001, 0.1, update_method=update_method
            )
            perceptron.train()
            iteration.append(len(perceptron.error_by_iteration))
        layer[2].append(iteration)
        print("layer", layer)
        plot_perceptrons_vs_iterations(layer, save_file)

    # plot_perceptrons_vs_iterations(layers[1], save_files[1])

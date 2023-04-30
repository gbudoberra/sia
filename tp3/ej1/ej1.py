import matplotlib.pyplot as plt

from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron
from tp3.configurations.jsonReader import JsonReader

and_colors = ['r', 'r', 'r', 'b']
or_colors = ['r', 'r', 'b', 'b']


def plot_result(w0, w1, w2, graph_points, colors, saving_file):
    plt.clf()
    x_vals = range(-2, 3)
    y_vals = [(w0 - w1 * x) / w2 for x in x_vals]
    plt.plot(x_vals, y_vals)
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    counter = 0
    for p in graph_points:
        plt.scatter(p[0], p[1], color=colors[counter])
        counter += 1
    plt.savefig(saving_file)


def plot_error(errors, filename):
    plt.clf()
    plt.plot(range(len(errors[::1000])), errors[::1000])
    plt.savefig(filename)


if __name__ == '__main__':

    config_files = ["./conf_and.json", "./conf_or_exclusive.json"]
    points_colors = [and_colors, or_colors]
    save_files = ["./and_result.png", "./or_result.png"]
    error_files = ["./and_error.png", "./or_error.png"]

    for file, color, save_file, error_file in zip(config_files, points_colors, save_files, error_files):
        config = JsonReader(file)
        points = config.points
        expected = config.expected
        perceptron = MultiLayerPerceptron(
            [len(points[0]) + 1, len(expected[0])],
            points,
            config.activation_method,
            expected,
            0, 0.1, update_method=config.update_method
        )
        perceptron.train()
        plot_result(perceptron.weights_by_layer[0][0][0], perceptron.weights_by_layer[0][0][1],
                    perceptron.weights_by_layer[0][0][2], points, color, save_file)
        plot_error(perceptron.error_by_iteration, error_file)


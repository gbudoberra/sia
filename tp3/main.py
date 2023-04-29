import matplotlib.pyplot as plt

from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron


def plot_result(w0, w1, w2, graph_points):
    x_vals = list(range(-2, 2))
    y_vals = [(w0 - w1 * x) / w2 for x in x_vals]
    plt.plot(x_vals, y_vals)
    for p in graph_points:
        plt.scatter(p[0], p[1], color='r')
    plt.show()


if __name__ == '__main__':
    points = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    expected = [[1], [1], [-1], [-1]]
    perceptron = MultiLayerPerceptron([3, 2, 1], points, "step", expected, 0.1, 0.1)
    perceptron.train()
    print(type(perceptron.weights_by_layer[0]))
    print(perceptron.weights_by_layer[0][0])

    plot_result(perceptron.weights_by_layer[0][0][0], perceptron.weights_by_layer[0][0][1],
                perceptron.weights_by_layer[0][0][2], points)
    print(perceptron.output_by_layer)
    # perceptron.incremental_iteration()
    # result_weights = perceptron.weights
    # print("Iterations: " + str(perceptron.current_iterations))
    # plot_result(result_weights[0], result_weights[1], result_weights[2], points)

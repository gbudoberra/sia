import numpy as np
from SimplePerceptron  import SimplePerceptron
import matplotlib.pyplot as plt
from multilayer import Multilayer
def plot_result(w0, w1, w2, graph_points):
    x_vals = list(range(-2, 2))
    y_vals = [(w0 - w1 * x) / w2 for x in x_vals]
    plt.plot(x_vals, y_vals)
    for p in graph_points:
        plt.scatter(p[0], p[1], color='r')
    plt.show()


if __name__ == '__main__':
    points = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    expected = [[-1, 0], [-1, 1], [-1, 1], [1, 1]]
    perceptron = Multilayer([3, 2, 2, 2], points, "id", expected, 0.1, 0.1)
    perceptron.batch_iteration()
    # perceptron.incremental_iteration()
    # result_weights = perceptron.weights
    # print("Iterations: " + str(perceptron.current_iterations))
    # plot_result(result_weights[0], result_weights[1], result_weights[2], points)



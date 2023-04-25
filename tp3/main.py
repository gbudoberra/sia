import numpy as np
from SingleLayerPerceptron  import SingleLayerPerceptron
import matplotlib.pyplot as plt


def plot_result(w0, w1, w2, graph_points):
    x_vals = list(range(-2, 2))
    y_vals = [(-w0 - w1 * x) / w2 for x in x_vals]
    plt.plot(x_vals, y_vals)
    for p in graph_points:
        plt.scatter(p[0], p[1], color='r')
    plt.show()


def escalon(x):
    return 1 if x >= 0 else -1

if __name__ == '__main__':
    points = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    expected = [-1, -1, -1, 1]
    perceptron = SingleLayerPerceptron(points, 0.1, expected, 0.1, escalon)
    perceptron.get_solution()
    result_weights = perceptron.weights
    print("Iterations: " + str(perceptron.current_iterations))
    plot_result(result_weights[0], result_weights[1], result_weights[2], points)



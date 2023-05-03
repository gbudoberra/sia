import csv
import numpy as np
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def split_vector(all_points, all_results, alpha):
    associated_values = []
    for p, result in zip(all_points, all_results):
        associated_values.append((p, result))
    training_length = int(alpha * len(associated_values))
    inner_training_points = random.sample(associated_values, training_length)
    generalizing_points = []
    for p in associated_values:
        if (p[0], p[1]) not in inner_training_points:
            generalizing_points.append(p)
    return inner_training_points, generalizing_points


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


def print_result( title, file):
    data = [(('sigmoid', 'adam'), 0.03132415942643508), (('sigmoid', 'adam'), 0.04392158909462643), (('sigmoid', 'adam'), 0.07597313752446842), (('sigmoid', 'adam'), 0.02208998408406998), (('sigmoid', 'adam'), 0.04892797113699527), (('sigmoid', 'adam'), 0.018268080442000026), (('sigmoid', 'adam'), 0.08883977724515081), (('sigmoid', 'adam'), 0.04574821300938939), (('sigmoid', 'adam'), 0.0651108610015363), (('sigmoid', 'adam'), 0.0318935016779679)]
    activations = set([d[0][0] for d in data])
    updates = set([d[0][1] for d in data])

    # Initialize arrays to hold data for each activation and update combination
    means = np.zeros((len(activations), len(updates)))
    stds = np.zeros((len(activations), len(updates)))

    # Populate arrays with means and standard deviations
    for i, act in enumerate(activations):
        for j, upd in enumerate(updates):
            values = [d[1] for d in data if d[0] == (act, upd)]
            means[i, j] = np.mean(values)
            stds[i, j] = np.std(values)

    # Set up plot
    fig, ax = plt.subplots()

    # Set up bar plot
    bar_width = 0.2
    x_positions = np.arange(len(activations))
    colors = ['blue', 'orange']
    for j, upd in enumerate(updates):
        ax.bar(x_positions + (j - 0.5) * bar_width, means[:, j], yerr=stds[:, j], width=bar_width, label=upd,
               color=colors[j])
    # Add legend and axis labels
    ax.legend()
    ax.set_xticks(x_positions)
    ax.set_xticklabels(activations)
    ax.set_xlabel('Activation Method')
    ax.set_ylabel('Value')
    ax.set_title(title)
    plt.savefig(file)


if __name__ == '__main__':
    # activation_methods = ["sigmoid", "tanh", "id"]
    # update_methods = ["adam", "gradient_descent"]
    # rescale_need = [True, True, False]
    # limits = [(0, 1), (-1, 1), None]
    # points, expected = parse_csv()
    # generalize_errors = []
    # training_errors = []
    # for activation, limit, rescale in zip(activation_methods, limits, rescale_need):
    #     for update in update_methods:
    #         g_err_counter = []
    #         t_err_counter = []
    #
    #         for i in range(10):
    #             if activation == "id" and update == "gradient_descent":
    #                 break
    #             if rescale:
    #                 expected = rescale_expected(expected, limit[0], limit[1])
    #             training, generalize = split_vector(points, expected, 0.8)
    #             training_points, training_expected = zip(*training)
    #             perceptron = MultiLayerPerceptron(
    #                 [len(points[0]) + 1, len(expected[0])],
    #                 training_points,
    #                 activation,
    #                 training_expected,
    #                 0.000001, 0.1, update_method=update)
    #             perceptron.train()
    #
    #             t_err_counter.append(((activation, update), perceptron.error() / len(training_points)))
    #             generalize_error = 0
    #             for p, r in generalize:
    #                 generalize_error += np.square(perceptron.get_result(p) - r)
    #             g_err_counter.append(((activation, update), generalize_error / len(generalize)))
    #
    #         generalize_errors.append(np.mean([x[1] for x in g_err_counter]))
    #
    #         training_errors.append([x[1] for x in t_err_counter])

    print_result("Error promedio de generalización.", "ErrorPromedioGeneralizacion.png")
    print_result("Error promedio de entrenamiento.", "ErrorPromedioEntrenamiento.png")

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


def print_result(data, title, file):
    names = [x[0][0] for x in data]
    colors = ['tab:orange' if x[0][1] == 'gradient_descent' else 'tab:blue' for x in data]
    values = [x[1] for x in data]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(names, np.ravel(values), color=colors, capsize=4)
    plt.xticks(horizontalalignment="center")
    ax.set_title(title)
    plt.yscale('log')
    plt.legend(handles=[mpatches.Patch(color='tab:orange', label='gradient_descent'), mpatches.Patch(color='tab:blue', label='adam')], fontsize=12)
    plt.savefig(file)


if __name__ == '__main__':
    activation_methods = ["sigmoid", "tanh", "id"]
    update_methods = ["adam", "gradient_descent"]
    rescale_need = [True, True, False]
    limits = [(0, 1), (-1, 1), None]
    points, expected = parse_csv()
    generalize_errors = []
    training_errors = []
    for activation, limit, rescale in zip(activation_methods, limits, rescale_need):
        for update in update_methods:
            if activation == "id" and update == "gradient_descent":
                break
            if rescale:
                expected = rescale_expected(expected, limit[0], limit[1])
            training, generalize = split_vector(points, expected, 0.8)
            training_points, training_expected = zip(*training)
            perceptron = MultiLayerPerceptron(
                [len(points[0]) + 1, len(expected[0])],
                training_points,
                activation,
                training_expected,
                0.000001, 0.1, update_method=update)
            perceptron.train()
            training_errors.append(((activation, update), perceptron.error() / len(training_points)))
            generalize_error = 0
            for p, r in generalize:
                generalize_error += np.square(perceptron.get_result(p) - r)
            generalize_errors.append(((activation, update), generalize_error / len(generalize)))

    print_result(generalize_errors, "Error promedio de generalización.", "ErrorPromedioGeneralizacion.png")
    print_result(training_errors, "Error promedio de entrenamiento.", "ErrorPromedioEntrenamiento.png")

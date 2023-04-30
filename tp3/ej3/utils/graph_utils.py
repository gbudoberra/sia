from matplotlib import pyplot as plt


def bar_graph(values, labels, filename, x_name, y_name):
    x = range(len(labels))

    fig, ax = plt.subplots()

    ax.bar(x, values)

    ax.set_ylabel('Valores')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title('Gráfico de barras')

    plt.savefig(filename)


def plot_graph(x, y, x_name, y_name, filename):
    # Crear una figura y un conjunto de ejes
    fig, ax = plt.subplots()

    # Trazar la línea del gráfico
    ax.plot(x, y)

    # Añadir etiquetas a los ejes
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)

    # Guardar el gráfico en un archivo
    plt.savefig(filename)


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


def plot_by_weights(weights, x1, x2, color):
    x = range(x1, x2)
    y = [(weights[0] - weights[1] * x_value) / weights[2] for x_value in x]
    plt.plot(x, y, color=color)


def plot_multiple_weight(weights, points1, points2, filename):
    plot_by_weights(weights[0], -2, 3, 'r')
    plot_by_weights(weights[1], -2, 3, 'b')
    for p in points1:
        plt.scatter(p[0], p[1], color='b')
    for p in points2:
        plt.scatter(p[0], p[1], color='g')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.savefig(filename)
    plt.clf()


def plot_error(errors, filename):
    plt.clf()
    plt.scatter(range(len(errors)), errors)
    plt.xlabel('Iterations')
    plt.ylabel('Error')
    plt.savefig(filename)


def plot_perceptrons_vs_iterations(perceptrons, filename):
    num_layers = len(perceptrons)
    print("num_layers", num_layers)
    bar_width = 0.25
    colors = ['r', 'g', 'b']

    fig, ax = plt.subplots()
    for i in range(num_layers):
        x = range(len(perceptrons[i][0]))
        print("x", x)
        y = perceptrons[i][0]
        print("y", y)
        ax.bar([xi + i * bar_width for xi in x],
               y, width=bar_width, color=colors[i],
               label=f'Layer {i + 1}')

    ax.set_xlabel('Amount of perceptrons per layer')
    ax.set_ylabel('Amount of iterations')
    ax.legend()
    plt.savefig(filename)
    # plt.clf()
    # plt.scatter(perceptrons, iterations)
    # plt.xlabel('Perceptrons per layer')
    # plt.ylabel('Iterations')
    # plt.yscale('log')
    # plt.savefig(filename)

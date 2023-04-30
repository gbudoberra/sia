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

    # Mostrar el gráfico
    plt.show()


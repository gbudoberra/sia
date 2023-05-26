import matplotlib.pyplot as plt
import numpy as np


def biplot(result: dict, vectors_x, vectors_y, filename="biplot.png"):
    countries = list(result.keys())
    values = list(result.values())

    plt.figure(figsize=(20, 12))

    # Scatter values
    plt.scatter([coord[0] for coord in values], [coord[1] for coord in values], marker='o', s=15)
    ref = "Referencias\n\n"
    aux = 1
    for i in range(len(countries)):
        if i in [1, 5, 24, 8]:
            plt.text(values[i][0], values[i][1], str(aux), ha='center', va='bottom')
            ref = ref + str(aux) + " = " + countries[i] + "\n"
            aux += 1
        else:
            plt.text(values[i][0], values[i][1], countries[i], ha='center', va='bottom')

    # Plot vectors
    vectors_origin = [-3, 3]
    plt.quiver([vectors_origin[0] for _ in vectors_x], [vectors_origin[1] for _ in vectors_y], vectors_x, vectors_y,
               width=0.0015, headwidth=0, headlength=0)
    vectors_names = ["Área", "GDP", "Inflation", "Life Exp.", "Military", "Pop. Growth", "Unemployment"]
    for i in range(len(vectors_x)):
        plt.text(vectors_x[i] + vectors_origin[0], vectors_y[i] + vectors_origin[1], vectors_names[i], ha='left',
                 va='bottom')
    cuadro_props = dict(boxstyle='round', facecolor='white', edgecolor='black')
    plt.text(4, 2, ref, fontsize=12, bbox=cuadro_props)

    plt.xlabel('PC1')
    plt.xlim(-4, 5)
    plt.ylabel('PC2')
    plt.ylim(-3, 4)
    plt.grid(True)
    plt.title('Valores por país')
    plt.savefig(filename)
    plt.clf()


def plot_y1(data: dict, filename="y_1_bar_plot.png"):
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot()

    ax.bar(keys, [v[0] for v in values])
    ax.set_ylim(-5, 5)
    ax.set_ylabel("PC1")
    plt.title('PC1 por país')
    ax.set_xticklabels(keys, rotation='vertical')
    plt.savefig(filename)
    plt.clf()


def plot_y1_comparison(pca: dict, pca_oja: dict, filename="y_1_bar_plot_comparison.png"):
    keys = list(pca.keys())
    values1 = list(pca.values())
    values2 = list(pca_oja.values())

    fig, ax = plt.subplots(figsize=(12, 12))

    width = 0.35  # Ancho de las barras
    ind = np.arange(len(keys))  # Índices para las barras

    rects1 = ax.bar(ind, [v[0] for v in values1], width, label='pca')
    rects2 = ax.bar(ind + width, [v[0] for v in values2], width, label='oja')

    ax.set_ylim(-5, 5)
    ax.set_ylabel("PC1")
    plt.title('PC1 por país')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(keys, rotation='vertical')
    ax.legend()

    plt.savefig(filename)
    plt.clf()

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def output_matrix(n):
    diag = [-1 for _ in range(n)]
    matriz = -1 * np.eye(n, dtype=int) + np.ones((n, n), dtype=int) + np.diag(diag)
    return -1 * matriz


def load_number_image(png_filename):
    image = Image.open(png_filename)
    array = np.array(image)
    binary_array = (array[:, :, 0] < 128).astype(int)
    return binary_array


def initialize_points(filename):
    parsing_png_points = []
    for i in range(10):
        name = get_image_path(i, 70, False, 0)
        image_matrix = load_number_image(name)
        parsing_png_points.append(np.ravel(image_matrix))
    return parsing_png_points


def get_image_path(num, noise, noisy, i):
    if not noisy:
        return f'./images/noise_{noise}/{num}_digit.png'
    else:
        return f'./images/noise_{noise}/' + str(num) + '_digit_with_error_' + str(i) + '.png'


def vary_update_method(times, noises, values, perceptron_adam, perceptron_gd):
    results_by_noise = []
    for noise in noises:
        adam_correct_percentage = []
        gd_correct_percentage = []
        for num in values:
            result_adam = 0
            result_gd = 0
            for i in range(times):
                test_matrix = load_number_image(get_image_path(num['digit'], noise, True, i))
                test = np.ravel(test_matrix)
                if np.array_equal(np.array(perceptron_gd.get_result(test)), np.array(num['expected'])):
                    result_gd += 1
                if np.array_equal(np.array(perceptron_adam.get_result(test)), np.array(num['expected'])):
                    result_adam += 1
            adam_correct_percentage.append(100 * (result_adam / times))
            gd_correct_percentage.append(100 * (result_gd / times))

        # Crear un array con los índices
        indices = np.arange(len(adam_correct_percentage))

        # Configurar el gráfico de barras
        ancho_barras = 0.35
        fig, ax = plt.subplots()
        rects1 = ax.bar(indices - ancho_barras / 2, adam_correct_percentage, ancho_barras, label='Adam')
        rects2 = ax.bar(indices + ancho_barras / 2, gd_correct_percentage, ancho_barras, label='Gradiente descendente')

        # Añadir etiquetas y leyendas
        ax.set_ylabel('Porcentaje')
        ax.set_xticks(indices)
        ax.set_title('Noise level = ' + str(noise))
        ax.legend()

        plt.savefig(f'Aciertos_vs_Nro_por_ActMetodo_noise_{noise}.png')
        plt.clf()

        # Definir los valores de A y B
        A = sum(adam_correct_percentage) / (len(adam_correct_percentage))
        B = sum(gd_correct_percentage) / (len(gd_correct_percentage))

        results_by_noise.append([A, B])

    # Crear un array con los índices
    indices = np.arange(len(noises))

    # Configurar el gráfico de barras
    ancho_barras = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(indices - ancho_barras / 2, [item[0] for item in results_by_noise], ancho_barras, label='Adam')
    rects2 = ax.bar(indices + ancho_barras / 2, [item[1] for item in results_by_noise], ancho_barras,
                    label='Gradiente descendente')

    # Añadir etiquetas y leyendas
    ax.set_ylabel('Porcentaje de aciertos totales')
    ax.set_xticks(indices)
    ax.set_xticklabels(noises)
    ax.legend()

    plt.savefig('Aciertos_vs_Ruido_por_ActMetodo.png')
    plt.clf()

    plt.plot(perceptron_adam.error_by_iteration, color='blue', label='Adam')
    plt.plot(perceptron_gd.error_by_iteration, color='orange', label='Gradiente descendente')
    plt.legend()
    plt.ylabel('Error')
    plt.xlabel('Epoca')
    plt.savefig('Error_vs_Epoca_por_ActMetodo.png')
    plt.clf()


def basic_learning_rate_bar_graph(x, y, y_label):
    fig, ax = plt.subplots()

    # Ajustar el ancho de las barras
    width = 0.05
    ax.bar(x, y, width, edgecolor='black')

    # Agregar etiquetas y títulos
    ax.set_xlabel('Tasa de aprendizaje')
    ax.set_ylabel(y_label)

    plt.savefig(f'LA_vs_{y_label}.png')
    plt.clf()


def vary_learning_rate(times, values, perceptrons, learning_rates, noise):
    percentage_by_learning_rate = []
    for perceptron in perceptrons:
        perceptron.train()
        result = 0
        for num in values:
            for i in range(times):
                test_matrix = load_number_image(get_image_path(num['digit'], noise, True, i))
                test = np.ravel(test_matrix)
                if np.array_equal(np.array(perceptron.get_result(test)), np.array(num['expected'])):
                    result += 1
        percentage_by_learning_rate.append(100 * (result / (times * len(values))))

    basic_learning_rate_bar_graph(learning_rates, percentage_by_learning_rate, 'Aciertos(%)')

    basic_learning_rate_bar_graph(learning_rates, [perceptron.epochs for perceptron in perceptrons], 'Epocas')

    # Plot error by iteration for 3 cases
    plt.plot(perceptrons[0].error_by_iteration, color='red', label='T.A. = 0.1')
    plt.plot(perceptrons[4].error_by_iteration, color='blue', label='T.A. = 0.5')
    plt.plot(perceptrons[9].error_by_iteration, color='green', label='T.A. = 1.0')
    plt.xlabel('Epoca')
    plt.ylabel('Error')
    plt.legend()
    plt.savefig('Error_vs_Epoca_por_LA.png')
    plt.clf()

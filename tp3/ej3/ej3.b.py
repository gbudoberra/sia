import numpy as np

from tp3.configurations.jsonReader import JsonReader
from tp3.ej3.utils.graph_utils import plot_graph
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.readlines()
        matrices = []
        for i in range(0, len(contenido), 7):
            matriz = np.zeros((7, 5), dtype=int)
            for j in range(7):
                fila = contenido[i + j].strip().split()
                matriz[j] = [int(d) for d in fila]
            matrices.append(matriz)
    return matrices


def num_to_string(arr):
    out = ''
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            out += str(arr[i, j]) + ' '
        out += '\n'
    return out


def get_points():
    nums = leer_archivo('TP3-ej3-digitos.txt')
    points = [np.ravel(m) for m in nums]
    return points, nums


if __name__ == '__main__':
    config = JsonReader("/home/bsquillari/PycharmProjects/sia/tp3/ej3/configurations/conf_B.json")

    points, nums = get_points()
    # Get testing sets
    testing_set = [points.pop(), points.pop()]
    testing_expected = [[-1], [1]]

    perceptron_by_layer = [len(points[0]) + 1, 36, 36, 1]

    # Learning [0, 1, 2, 3, 4, 5, 6, 7]
    perceptron = MultiLayerPerceptron(
        perceptron_by_layer,
        points,
        config.activation_method,
        config.expected,
        config.epsilon,
        config.learning_rate
    )
    perceptron.train()

    # Error vs Iterations
    print(perceptron.error_by_iteration)
    plot_graph(range(len(perceptron.error_by_iteration)), perceptron.error_by_iteration, "Iteraciones", "Error",
               "/home/bsquillari/PycharmProjects/sia/tp3/ej3/graphs/B_error.png")

    # Case 1: Already learned numbers
    print('Casos ya aprendidos:')
    for i in range(len(points)):
        print('---------------------')
        print(num_to_string(nums[i]))
        if perceptron.get_result(points[i]) == 1:
            print('Resultado: Par')
        else:
            print('Resultado: Impar')
        print('---------------------')

    # Case 2: Testing set
    print('Conjunto de testeo:')
    for i in range(len(testing_set)):
        print('---------------------')
        print(num_to_string(nums[i + len(nums) - 2]))
        if perceptron.get_result(testing_set[i]) == 1:
            print('Resultado: Par')
        else:
            print('Resultado: Impar')
        print('---------------------')

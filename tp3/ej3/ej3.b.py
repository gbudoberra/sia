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


def get_points():
    nums = leer_archivo('TP3-ej3-digitos.txt')
    points = [np.ravel(m) for m in nums[0:len(nums) - 1:1]]
    return points


if __name__ == '__main__':
    config = JsonReader("./ej3/configurations/config_A.json")

    points = get_points()



    perceptron_by_layer = [len(points) + 1, 36, 36, 1]

    # Case 1
    # Learning with all values
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
    plot_graph(range(len(perceptron.error_by_iteration)), perceptron.error_by_iteration, "Iteraciones", "Error", "./ej3/graphs/B_error.png")

    #

    # perceptron = MultiLayerPerceptron([36, 36, 36, 1], points, "step", config.expected, 0.1, 0.1)
    # perceptron.train()
    # result = perceptron.get_result(np.ravel(matrices[len(matrices)-1]))
    # print(result)
    # result = perceptron.get_result(np.ravel(matrices[5]))
    # print(result)


    # print(type(perceptron.weights_by_layer[0]))
    # print(perceptron.weights_by_layer[0][0])
    # print(perceptron.output_by_layer)

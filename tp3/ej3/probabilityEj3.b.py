import numpy as np
import os
import random
import matplotlib.pyplot as plt
from tp3.configurations.jsonReader import JsonReader
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
    json_path = os.path.join(os.path.dirname(__file__), 'configurations', 'conf_B.json')

    config = JsonReader(json_path)
    points, nums = get_points()
    success = 0
    total = 1000

    for j in range(total):
        print(j)
        expected = [x for x in config.expected]
        aux_points = [x for x in points]

        testing_index = random.randint(0, len(aux_points) - 1)
        testing_set = [aux_points[testing_index]]
        aux_points = np.delete(aux_points, testing_index, axis=0)
        testing_expected = [1 if testing_index % 2 == 0 else -1]
        expected.pop(testing_index)

        perceptron_by_layer = [len(aux_points[0]) + 1, 36, 36, 1]
        perceptron = MultiLayerPerceptron(
            perceptron_by_layer,
            aux_points,
            config.activation_method,
            expected,
            config.epsilon,
            config.learning_rate
        )
        perceptron.train()
        for i in range(len(testing_set)):
            if perceptron.get_result(testing_set[i]) == config.expected[testing_index]:
                success += 1

    labels = ['Aciertos', 'No aciertos']
    sizes = [success, total - success]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.show()

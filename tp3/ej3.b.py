import numpy as np
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


if __name__ == '__main__':
    matrices = leer_archivo('TP3-ej3-digitos.txt')
    expected = [[1], [-1], [1], [-1], [1], [-1], [1], [-1], [1]]
    points = [np.ravel(m) for m in matrices[0:len(matrices) - 1:1]]
    perceptron = MultiLayerPerceptron([36, 36, 36, 1], points, "step", expected, 0.1, 0.1)
    perceptron.batch_iteration()
    result = perceptron.get_result(np.ravel(matrices[len(matrices)-1]))
    print(result)
    result = perceptron.get_result(np.ravel(matrices[5]))
    print(result)


    # print(type(perceptron.weights_by_layer[0]))
    # print(perceptron.weights_by_layer[0][0])
    # print(perceptron.output_by_layer)

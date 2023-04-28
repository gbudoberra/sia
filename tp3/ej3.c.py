from PIL import Image
import numpy as np
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron


def output_matrix(n):
    diag = [-1 for _ in range(n)]
    matriz = -1 * np.eye(n, dtype=int) + np.ones((n, n), dtype=int) + np.diag(diag)
    return -1*matriz


def load_number_image(png_filename):
    image = Image.open(png_filename)
    array = np.array(image)
    binary_array = (array[:, :, 0] < 128).astype(int)
    return binary_array


if __name__ == '__main__':
    # Carga las imágenes para los números del 0 al 9
    points = []
    for i in range(10):
        filename = f'{i}.png'
        image_matrix = load_number_image(filename)
        points.append(np.ravel(image_matrix))
    identity_matrix = output_matrix(10)
    expected = [row.tolist() for row in identity_matrix]
    perceptron = MultiLayerPerceptron([(35*35)+1,  100,100,100,100, 10], points, "step", expected, 0, 0.1)
    perceptron.batch_iteration()

    print("finished")
    test = np.ravel(load_number_image('0.png'))
    result = perceptron.get_result(test)
    print(result)

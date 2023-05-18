from tp4.kohonen.utils import parse_csv
from oja import Oja
from plot_generator import plot_y1, biplot
from pca import get_result
import matplotlib.pyplot as plt


def plot_error(error):
    tiempo = range(1, len(error) + 1)
    plt.plot(tiempo, error)
    plt.xlabel('Época')
    plt.ylabel('Error')
    plt.title('Error en función de la época')
    plt.savefig("Error_vs_epoch.png")


if __name__ == '__main__':
    normalized_map = parse_csv(True)
    eigv, r = get_result(normalized_map)
    points = [p for p in normalized_map.values()]
    oja = Oja(points, .001, 10000, eigv[:, 0])
    oja.iterate()
    result = {}
    for country, y1 in zip(normalized_map.keys(), oja.get_y1()):
        result[country] = y1, y1

    plot_error(oja.error)
    plot_y1(result, "result_with_oja.png")

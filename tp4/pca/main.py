from oja import Oja
from pca import get_result
from plot_generator import plot_y1, biplot, plot_y1_comparison
from tp4.kohonen.utils import parse_csv
from tp4.pca.oja_pca import plot_error

if __name__ == '__main__':

    normalized_map = parse_csv(True)
    eigv, result = get_result(normalized_map)
    biplot(result, eigv[:, 0], eigv[:, 1])
    plot_y1(result)

    points = [p for p in normalized_map.values()]
    oja = Oja(points, .001, 10000, eigv[:, 0])
    oja.iterate()
    result_with_oja = {}
    for country, y1 in zip(normalized_map.keys(), oja.get_y1()):
        result_with_oja[country] = y1, y1

    plot_error(oja.error)
    plot_y1(result_with_oja, "result_with_oja.png")
    plot_y1_comparison(result, result_with_oja, filename = "y_1_bar_plot_comparison.png")

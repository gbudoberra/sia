from tp4.kohonen.utils import parse_csv
import numpy as np
import pandas as pd
from plot_generator import plot_y1, biplot


def get_result(input_map):
    df = pd.DataFrame.from_dict(input_map, orient='index',
                                columns=['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth',
                                         'Unemployment'])
    correlation_matrix = df.cov()
    eigenvalues, eigenvectors = np.linalg.eig(correlation_matrix)
    points = np.vstack(list(input_map.values()))
    y_1 = np.dot(points, eigenvectors[:, 0])
    y_2 = np.dot(points, eigenvectors[:, 1])
    result_map = {}
    for country, y1, y2 in zip(input_map.keys(), y_1, y_2):
        result_map[country] = y1, y2
    return eigenvectors, result_map


if __name__ == '__main__':
    normalized_map = parse_csv(True)
    eigv, result = get_result(normalized_map)
    biplot(result, eigv[:, 0], eigv[:, 1])
    plot_y1(result)

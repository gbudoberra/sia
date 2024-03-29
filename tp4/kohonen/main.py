import numpy as np

from graph_generators import plot_heat_map, plot_avg_distance, plot_heat_map_with_names, \
    plot_avg_elements_distance_per_k, plot_groups_per_k
from tp4.kohonen.Som import Som
from utils import parse_csv

if __name__ == '__main__':
    country_map = parse_csv()
    points = [points for points in country_map.values()]
    avg_elements = []
    groups_cant = []
    distances = []
    for k in range(3, 10):
        som = Som(k, points, 500, True, True)
        som.train()

        result_map = {}
        category_map = {}
        for country_name, country_point in zip(country_map.keys(), country_map.values()):
            row, col = som.get_row_and_column(country_point)
            result_map.setdefault((row, col), []).append(country_name)
            category_map[country_name] = (row, col)

        plot_heat_map(result_map, k)
        plot_heat_map_with_names(result_map, k)
        avg_distance = som.get_avg_distance()
        distances.append(np.mean(avg_distance))
        print(avg_distance)
        plot_avg_distance(avg_distance, k)
        avg_elements_per_cell, groups = som.get_avg_elements_per_cell(result_map)
        avg_elements.append(avg_elements_per_cell)
        groups_cant.append(groups)
    plot_avg_elements_distance_per_k(avg_elements, distances, np.std(avg_elements), np.std(distances))
    plot_groups_per_k(groups_cant)

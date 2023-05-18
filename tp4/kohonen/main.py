import numpy as np
import pandas as pd
from tp4.kohonen.Som import Som
from graph_generators import plot_heat_map, plot_avg_distance, plot_assigned_categories
from utils import parse_csv

if __name__ == '__main__':
    country_map = parse_csv()
    points = [points for points in country_map.values()]
    k = 8
    som = Som(k, points, 500, False, False)
    som.train()

    result_map = {}
    category_map = {}
    for country_name, country_point in zip(country_map.keys(), country_map.values()):
        row, col = som.get_row_and_column(country_point)
        result_map.setdefault((row, col), []).append(country_name)
        category_map[country_name] = (row, col)

    print(category_map)
    plot_heat_map(result_map)
    avg_distance = som.get_avg_distance()
    print(avg_distance)
    plot_avg_distance(avg_distance, k)
    # plot_assigned_categories(category_map)

import pandas as pd

from graph_generators import plot_assigned_categories, plot_heat_map, plot_avg_distance, plot_heat_map_with_names
from tp4.kohonen.Som import Som


def parse_csv(filename='europe.csv'):
    df = pd.read_csv(filename)
    columns = df.columns[1:]
    mean = df[columns].mean()
    std = df[columns].std()
    standardizes_df = (df[columns] - mean) / std
    standardizes_df = pd.concat([df['Country'], standardizes_df], axis=1)
    standardizes_df = standardizes_df.set_index('Country')
    country_map = {}
    for row_number in range(standardizes_df.shape[0]):
        country_map[standardizes_df.index[row_number]] = standardizes_df.iloc[row_number].values
    return country_map


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

    plot_heat_map(result_map, k)
    plot_heat_map_with_names(result_map, k)
    avg_distance = som.get_avg_distance()
    print(avg_distance)
    plot_avg_distance(avg_distance, k)
    # plot_assigned_categories(category_map)

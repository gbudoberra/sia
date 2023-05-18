import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def parse_csv(box_plot=False, filename='europe.csv'):
    df = pd.read_csv(filename)
    if box_plot:
        plot_box(df, "Variable sin estandarizar", "not_standard.png")
    data = df.iloc[:, 1:].values
    scaler = StandardScaler()
    data_standardized = scaler.fit_transform(data)
    country_map = {}
    for i, country in enumerate(df['Country']):
        country_map[country] = data_standardized[i]
    if box_plot:
        standardized_df = pd.DataFrame.from_dict(country_map, orient='index',
                                                 columns=['Area', 'GDP', 'Inflation', 'Life.expect', 'Military',
                                                          'Pop.growth', 'Unemployment'])
        plot_box(standardized_df, "Variable estandarizada", "standard.png")
    return country_map


def get_distance(u, v):
    return np.sqrt(np.linalg.norm(u - v))


def plot_box(df, title, plot_filename):
    path = f'../pca/{plot_filename}'
    columns = ["Area", "GDP", "Inflation", "Life.expect", "Military", "Pop.growth", "Unemployment"]
    plt.figure(figsize=(10, 6))
    plt.boxplot(df[columns].values, labels=columns)
    plt.title(title)
    plt.savefig(path)
    plt.clf()

import numpy as np

from tp5.font import get_font_as_xis
from tp5.perceptrons.PreTrainedPerceptron import PreTrainedPerceptron
from tp5.utils.JsonReader import JsonReader
from tp5.utils.file_utils import read_weights_from_file

weights_file = "weights_1.txt"
latent_layer = 4

if __name__ == '__main__':
    config = JsonReader()
    data_set = get_font_as_xis()
    result_set = data_set

    pre_trained = PreTrainedPerceptron(
        read_weights_from_file(len(config.activation_method), weights_file),
        config.activation_method,
        latent_layer
    )

    distances = []
    for X in data_set:
        Y = pre_trained.get_result(X)
        distances.append(np.linalg.norm(Y - X))
    print(distances)

    latent_space = []
    for X in data_set:
        Y = pre_trained.get_latent_result(X)
        latent_space.append(Y)
    print(latent_space)

    from_latent = []
    for Z, X in zip(latent_space, data_set):
        Y = pre_trained.generate_from_latent_space(Z)
        from_latent.append(np.linalg.norm(Y - X))
    print(from_latent)

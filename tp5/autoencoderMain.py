import numpy as np

from font import get_font_as_xis
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron
from tp5.utils.JsonReader import JsonReader
from tp5.utils.file_utils import write_weights_to_file

if __name__ == '__main__':
    config = JsonReader()
    data_set = get_font_as_xis()
    result_set = data_set

    nn = MultiLayerPerceptron(
        config.perceptron_by_layer,
        data_set,
        config.activation_method,
        result_set,
        config.epsilon,
        config.learning_rate,
        config.update_method)

    nn.train()

    file_prefix = "weights"
    write_weights_to_file(nn.get_weights(), file_prefix)

    distances = []
    for i in range(len(data_set)):
        result = nn.get_result(data_set[i])
        distances.append(np.linalg.norm(result - data_set[i]))
    print(distances)

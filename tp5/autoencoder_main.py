import numpy as np

from font import get_font_as_xis
from tp5.perceptrons.AutoencoderPerceptron import AutoencoderPerceptron
from tp5.utils.JsonReader import JsonReader
from tp5.utils.file_utils import write_weights_to_file
from tp3.ej3.utils.graph_utils import plot_graph


if __name__ == '__main__':
    config = JsonReader()
    data_set = get_font_as_xis()
    result_set = data_set

    nn = AutoencoderPerceptron(
        config.perceptron_by_layer,
        data_set,
        config.activation_method,
        result_set,
        config.epsilon,
        config.learning_rate,
        config.update_method,
        20000
    )

    nn.train()

    file_prefix = "weights"
    write_weights_to_file(nn.get_weights(), file_prefix)

    distances = []
    for i in range(len(data_set)):
        result = nn.get_result(data_set[i])
        distances.append(np.linalg.norm(result - data_set[i]))
    print(distances)

    plot_graph(range(len(nn.error_by_iteration)), nn.error_by_iteration, "Iteraciones", "Error",
               'error_vs_epoch.png')
    plot_graph(range(len(nn.error_by_iteration)), nn.error_by_iteration, "Iteraciones", "Error",
               'error_vs_epoch_log.png', True)

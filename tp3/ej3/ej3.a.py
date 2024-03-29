from tp3.configurations.jsonReader import JsonReader
from tp3.ej3.utils.graph_utils import plot_perceptrons_vs_iterations, plot_perceptrons_vs_iterations2
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron

if __name__ == '__main__':

    config = JsonReader("./configurations/conf_A.json")

    update_methods = ["adam", "gradient_descent"]

    activation_methods = ["step", "step"]

    save_files = ["./ej3a_adam_perceptrons_vs_iter.png", "./ej3a_gradient_perceptrons_vs_iter.png"]

    or_colors = ['r', 'r', 'b', 'b']
    layers = [[], []]

    points = config.points
    expected = config.expected
    first = len(points[0])+1
    last = len(expected[0])

    for save_file, update_method, activation_method, layer in zip(save_files, update_methods, activation_methods,  layers):
        for i in range(3):
            iteration = []
            for perceptrons in range(1, 10):
                # for count in range(7):
                architecture = [first]
                [architecture.append(perceptrons) for _ in range(i)]
                architecture.append(last)
                perceptron = MultiLayerPerceptron(
                    architecture,
                    points,
                    activation_method,
                    expected,
                    0.0001, 0.1, update_method=update_method
                )
                perceptron.train()
                # average.append()
                iteration.append(len(perceptron.error_by_iteration))
            layer.append(iteration)
        # layer = [[50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001, 50001],
        #          [50001, 50001, 285, 61, 62, 63, 64, 33, 5],
        #          [50001, 50001, 165, 28, 6, 13, 41, 10, 45]]

        print("layer", layer)
        plot_perceptrons_vs_iterations(layer, save_file)


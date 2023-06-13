from tp3.multilayer.multilayerperceptron import activation_methods_dictionary
from tp5.perceptrons.result_functions import get_result, get_latent_result, generate_from_latent_space


class PreTrainedPerceptron:
    def __init__(self, weights, activation_method_by_layer, latent_layer):
        self.weights = weights
        self.activation_method_by_layer = []
        for am in activation_method_by_layer:
            self.activation_method_by_layer.append(activation_methods_dictionary[am][0])
        self.latent_layer = latent_layer

    def get_weights(self):
        return self.weights

    def get_result(self, points):
        return get_result(points, self.activation_method_by_layer, self.weights)

    def get_latent_result(self, points):
        return get_latent_result(points, self.activation_method_by_layer, self.weights, self.latent_layer)

    # receives a point, and multiply back from the latent space to the initial space
    def generate_from_latent_space(self, points):
        return generate_from_latent_space(points, self.activation_method_by_layer, self.weights,
                                          self.latent_layer)

from tp5.update_methods.UpdateMethod import UpdateMethod


class GradientDescendent(UpdateMethod):

    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def get_delta(self, gradient, layer):
        return -1 * self.learning_rate * gradient

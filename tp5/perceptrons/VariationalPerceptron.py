import math

import numpy as np

from tp5.perceptrons.Perceptron import Perceptron


class VariationalPerceptron:

    def __init__(
            self,
            m_encoder: Perceptron,
            s_encoder: Perceptron,
            decoder: Perceptron,
            data_set,
            sample_size
    ):
        self.m_encoder = m_encoder
        self.s_encoder = s_encoder
        self.decoder = decoder
        self.data_set = data_set
        self.sample_size = sample_size

    def train(self):
        while True:
            m = self.m_encoder.feed(np.array(self.data_set).T)
            s = self.s_encoder.feed(np.array(self.data_set).T)

            e = np.random.standard_normal((len(m), self.sample_size))
            z = m + s * e

            result = self.decoder.feed(z)

            current_point_index = 0
            for r, e, input in zip(result.T, self.data_set, z.T):
                dloss = self.decoder.back_propagation(r - e, current_point_index, input)
                # self.m_encoder.back_propagation(dloss * 1 - m[:, current_point_index], current_point_index,
                #                                 e)  # dlossdecoder/dz * dz/dm + dKL/dm = d(MSE + KL) / dm
                # self.s_encoder.back_propagation(dloss * e - 0.5 * (1 - math.e ** s), current_point_index,
                #                                 e)  # dloss/z * dz/ds + dKL/ds
                self.m_encoder.back_propagation([0, 0], current_point_index,
                                                e)  # dlossdecoder/dz * dz/dm + dKL/dm = d(MSE + KL) / dm
                self.s_encoder.back_propagation([1, 1], current_point_index,
                                                e)  # dloss/z * dz/ds + dKL/ds
                current_point_index += 1
                VariationalPerceptron.loss(e, r, m[:, current_point_index], s[:, current_point_index])

    @staticmethod
    def loss(expected, result, mean, std):
        kl = - 0.5 * (1 + std - np.square(mean) - np.exp(std))
        mse = np.linalg.norm(expected - result)
        print(str(mse + kl))
        return mse + kl

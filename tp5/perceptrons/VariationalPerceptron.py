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
        for _ in range(1000):
            m = self.m_encoder.feed(np.array(self.data_set).T)
            s = self.s_encoder.feed(np.array(self.data_set).T)

            e = np.random.standard_normal((len(m), self.sample_size))
            z = m + s * e

            result = self.decoder.feed(z)

            current_point_index = 0
            for r, expected, z_i in zip(result.T, self.data_set, z.T):
                dloss = self.decoder.back_propagation(r - expected, current_point_index, z_i)
                # dlossdecoder/dz * dz/dm + dKL/dm = d(MSE + KL) / dm
                m_dloss = dloss * 1 - m[:, current_point_index]
                self.m_encoder.back_propagation(m_dloss, current_point_index, expected)
                # dloss/z * dz/ds + dKL/ds
                s_dloss = dloss * e.T[current_point_index] - 0.5 * (1 - math.e ** s[:, current_point_index])
                self.s_encoder.back_propagation(s_dloss, current_point_index, expected)
                current_point_index += 1
            VariationalPerceptron.loss(self.data_set, result.T, m, s)

    @staticmethod
    def loss(expected, result, mean, std):
        total_kl = 0
        total_mse = 0
        for i in range(len(expected)):
            kl = - 0.5 * (1 + std[:, i] - np.square(mean[:, i]) - np.exp(std[:, i]))
            mse = np.linalg.norm(expected[i] - result[i])
            total_kl += sum(kl)
            total_mse += mse
        print(f'MSE: {total_mse} --- KL: {total_kl} --- TOTAL: {total_mse + total_kl}')
        return total_kl + total_mse

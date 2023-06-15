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
        m = self.m_encoder.feed(np.array(self.data_set).T)
        s = self.s_encoder.feed(np.array(self.data_set).T)

        # Sample
        # z = []
        e = np.random.standard_normal((len(m), self.sample_size))
        # for m_i, s_i in zip(m.T, s.T):
        #     z.append(m_i + s_i * e)
        z = m + s * e

        result = self.decoder.feed(z)

        dloss = self.decoder.back_propagation(np.array([sum(x) for x in (result - self.data_set.T)]))  # 1 o -1 ?

        self.m_encoder.back_propagation(dloss * 1 - m)  # dlossdecoder/dz * dz/dm + dKL/dm = d(MSE + KL) / dm
        self.s_encoder.back_propagation(dloss * e - 0.5 * (1 - math.e ** s))  # dloss/z * dz/ds + dKL/ds

        return result, m, s

    @staticmethod
    def loss(expected, result, mean, std):
        kl = - 0.5 * (1 + std - np.square(mean) - np.exp(std))
        mse = np.linalg.norm(expected - result)
        return mse + kl

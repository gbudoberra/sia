import matplotlib.pyplot as plt
import numpy as np

from tp5.perceptrons.Perceptron import Perceptron
from tp5.utils.random_utils import mostrar_progreso


class VariacionalSimpleSampling:

    def __init__(
            self,
            m_encoder: Perceptron,
            s_encoder: Perceptron,
            decoder: Perceptron,
            data_set,
            sample_size,
            expected
    ):
        self.m_encoder = m_encoder
        self.s_encoder = s_encoder
        self.decoder = decoder
        self.data_set = data_set
        self.sample_size = sample_size
        self.latent_space = []
        self.expected = expected

        self.mse = []
        self.kl = []

    def train(self):
        repetitions = 5000
        for epoch in range(repetitions):
            if epoch % (repetitions / 10) == 0:
                mostrar_progreso(int(100 * epoch / repetitions))

            m = self.m_encoder.feed(np.array(self.data_set).T)
            s = self.s_encoder.feed(np.array(self.data_set).T)
            e = np.random.standard_normal((len(m), self.sample_size))
            z = m + s * e

            result = self.decoder.feed(z)
            # if epoch % 100 == 0:
            #     for m_i, s_i, x, xp in zip(m.T, s.T, self.data_set, result.T):
            #         self.loss(m_i, s_i, x, xp, epoch)

            current_point_index = 0
            kl_lambda = 0.01
            mse_total = 0
            kl_total = 0
            for r, expected, z_i, m_i, s_i in zip(result.T, self.expected, z.T, m.T, s.T):
                dloss = self.decoder.back_propagation_multiple((r - expected) / np.linalg.norm(expected - r),
                                                               current_point_index, z_i)
                # dlossdecoder/dz * dz/dm + dKL/dm = d(MSE + KL) / dm
                m_dloss = dloss * 1 + kl_lambda * (sum(m[:, current_point_index]))
                self.m_encoder.back_propagation_multiple(m_dloss, current_point_index, expected)
                # dloss/z * dz/ds + dKL/ds
                s_dloss = np.matmul(dloss, np.diag(e.T[current_point_index])) - kl_lambda * 0.5 * sum(
                    1 - np.exp(s[:, current_point_index]))
                self.s_encoder.back_propagation_multiple(s_dloss, current_point_index, expected)
                current_point_index += 1
                mse, kl = VariacionalSimpleSampling.loss(m_i, s_i, expected, r)
                mse_total += mse
                kl_total += kl
            self.mse.append(mse_total)
            self.kl.append(kl_total)

    def feed_forward(self, x):
        m = self.m_encoder.feed(x)
        s = self.s_encoder.feed(x)
        e = np.random.standard_normal(len(m))
        z = m + s * e
        return self.decoder.feed(z)

    @staticmethod
    def loss(m, s, x, xp):
        kl = -0.5 * sum(1 + s - (m ** 2) - np.exp(s))
        mse = np.linalg.norm(x - xp)
        return mse, kl

    def get_z(self, x):
        m = self.m_encoder.feed(x)
        s = self.s_encoder.feed(x)
        e = np.random.standard_normal(len(m))
        return m + s * e

    def plot_errors(self):
        plt.plot(self.mse, label='MSE')
        plt.plot(self.kl, label='KL')
        plt.plot(self.mse + self.kl, label='Total')
        plt.legend()
        plt.show()
        plt.clf()
        plt.plot(self.kl, label='KL')
        plt.legend()
        plt.show()
        plt.clf()
        plt.plot(self.mse, label='MSE')
        plt.legend()
        plt.show()
        plt.clf()
        plt.plot(self.mse, label='MSE')
        plt.plot(self.kl, label='KL')
        plt.legend()
        plt.show()
        plt.clf()
        plt.plot(self.mse + self.kl, label='Total')
        plt.legend()
        plt.show()
        plt.clf()

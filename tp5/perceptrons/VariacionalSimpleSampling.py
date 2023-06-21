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
            kl_lambda = 1
            mse_total = 0
            kl_total = 0
            for r, expected, z_i, m_i, s_i, e_i in zip(result.T, self.expected, z.T, m.T, s.T, e.T):
                dloss = self.decoder.back_propagation_multiple((r - expected),
                                                               current_point_index, z_i)
                # dlossdecoder/dz * dz/dm + dKL/dm = d(MSE + KL) / dm
                dz_dm = np.ones([dloss.size, 2])
                m_dloss = np.dot(dloss, dz_dm) + kl_lambda * m_i
                self.m_encoder.back_propagation_multiple(m_dloss, current_point_index, expected)
                # dloss/z * dz/ds + dKL/ds
                dz_dv = e_i * np.ones([dloss.size, 2])
                s_dloss = np.dot(dloss, dz_dv) - kl_lambda * 0.5 * (1 - np.exp(s_i))
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
    def loss(mean, std, data, result):
        rec = 0.5 * np.mean((data - result) ** 2)
        kl = -0.5 * np.sum(1 + std - mean ** 2 - np.exp(std))

        return rec, kl

    def get_z(self, x):
        m = self.m_encoder.feed(x)
        s = self.s_encoder.feed(x)
        e = np.random.standard_normal(len(m))
        return m + s * e

    def plot_errors(self):
        total = [mse + kl for mse, kl in zip(self.mse, self.kl)]
        plt.plot(self.mse, label='MSE')
        plt.plot(self.kl, label='KL')
        plt.plot(total, label='Total')
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
        plt.plot(total, label='Total')
        plt.legend()
        plt.show()
        plt.clf()

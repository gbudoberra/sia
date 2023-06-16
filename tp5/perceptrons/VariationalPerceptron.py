import matplotlib.pyplot as plt
import numpy as np

from tp5.perceptrons.Perceptron import Perceptron


def transform_to_binary(array):
    binary = []
    for e in array:
        if e > 0.5:
            binary.append(1)
        else:
            binary.append(0)
    return np.array(binary)


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
        self.latent_space = []

    def feed_forward(self, x):
        return

    def train(self):
        for epoch in range(1000):
            m = self.m_encoder.feed(np.array(self.data_set).T)
            s = self.s_encoder.feed(np.array(self.data_set).T)
            e = np.random.standard_normal((len(m), self.sample_size))
            z = m + s * e
            print(m)
            print(s)

            self.latent_space = []
            if epoch % 100 == 0:
                for z_i in z.T:
                    self.latent_space.append(z_i)
                self.plot_latent_space(f'Epoca: {str(epoch)}')

            result = self.decoder.feed(z)

            current_point_index = 0
            for r, expected, z_i in zip(result.T, self.data_set, z.T):
                dloss = self.decoder.back_propagation(transform_to_binary(r) - expected, current_point_index, z_i)
                # dlossdecoder/dz * dz/dm + dKL/dm = d(MSE + KL) / dm
                m_dloss = dloss * 1 + (len(m[:, current_point_index]) * sum(m[:, current_point_index]))
                self.m_encoder.back_propagation(m_dloss, current_point_index, expected)
                # dloss/z * dz/ds + dKL/ds
                s_dloss = dloss * e.T[current_point_index] - 0.5 * len(m[:, current_point_index]) * sum(
                    1 - np.exp(s[:, current_point_index]))
                self.s_encoder.back_propagation(s_dloss, current_point_index, expected)
                current_point_index += 1
            VariationalPerceptron.loss(self.data_set, result.T, m, s)

    @staticmethod
    def loss(expected, result, mean, std):
        total_kl = 0
        total_mse = 0
        for i in range(len(expected)):
            kl = - 0.5 * len(mean[:, i]) * (1 + std[:, i] - np.square(mean[:, i]) - np.exp(std[:, i]))
            # mse = np.linalg.norm(expected[i] - transform_to_binary(result[i]))
            mse = (1 / 2) * sum((expected[i] - transform_to_binary(result[i])) ** 2)
            total_kl += sum(kl)
            total_mse += mse
        print(f'MSE: {total_mse} --- KL: {total_kl} --- TOTAL: {total_mse + total_kl}')
        return total_kl + total_mse

    # receive a point on the latent space and decode it.
    def generate_from(self, z):
        return transform_to_binary(self.decoder.feed(z))

    def get_distribution(self, point):
        m = self.m_encoder.feed(point)
        s = self.s_encoder.feed(point)
        e = np.random.standard_normal(len(m))
        return m + s * e

    def plot_latent_space(self, title):
        plt.scatter(
            [z[0] for z in self.latent_space],
            [z[1] for z in self.latent_space]
        )
        plt.title(title)
        plt.show()
        plt.clf()

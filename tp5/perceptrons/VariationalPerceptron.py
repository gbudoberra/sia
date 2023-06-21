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


def sample(m, s, e):
    a = m + s * e
    return a


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
        self.kls = []
        self.mses = []
        self.e = np.random.standard_normal((2, self.sample_size))

    def feed_forward(self, x):
        return

    def train(self):
        for epoch in range(30):
            print(epoch)
            for point in self.data_set:
                m = self.m_encoder.feed(np.array(point).T)
                s = self.s_encoder.feed(np.array(point).T)
                print(f'm:{m} s:{s}')
                zs = []
                for e_i in self.e.T:
                    zs.append(sample(m, s, e_i))

                if epoch % 10 == 0:
                    plt.scatter([z[0] for z in zs], [z[1] for z in zs])

                kl_lambda = 1
                for i, z in enumerate(zs):
                    result = self.decoder.feed(z)
                    dloss = self.decoder.back_propagation(sum(result - point), z)

                    m_dloss = dloss * 1 + kl_lambda * m
                    self.m_encoder.back_propagation(m_dloss, point)

                    s_dloss = dloss * self.e.T[i] - kl_lambda * 0.5 * (1 - np.exp(s))
                    self.s_encoder.back_propagation(s_dloss, point)
            print(f'Error: {self.loss(point, result, m, s)}')
            plt.show()
            plt.clf()

    def loss(self, x, r, m, s):
        return 0.5 * sum((x - r) ** 2) - 0.5 * (len(m) - sum(m ** 2) - sum(np.exp(s)) + sum(s))


    # receive a point on the latent space and decode it.
    def generate_from(self, z):
        return transform_to_binary(self.decoder.feed(z))

    def get_distribution(self, point):
        m = self.m_encoder.feed(point)
        s = self.s_encoder.feed(point)
        e = np.random.standard_normal(len(m))
        return sample(m, s, e)

    def plot_latent_space(self, title):
        plt.scatter(
            [z[0] for z in self.latent_space],
            [z[1] for z in self.latent_space]
        )
        plt.title(title)
        plt.show()
        plt.clf()

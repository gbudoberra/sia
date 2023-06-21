import numpy as np


class PreTrainedVariational:

    def __init__(self, m_weights, s_weights, decoder_weights, encoder_act, decoder_act):
        self.m_weights = m_weights
        self.s_weights = s_weights
        self.decoder_weights = decoder_weights
        self.encoder_act = encoder_act
        self.decoder_act = decoder_act

    def feed_forward(self, x):
        m = self._feed_m(x)
        s = self._feed_s(x)
        e = np.random.standard_normal(len(m))
        z = m + s * e
        return self._feed_decoder(z)

    def get_z(self, x):
        m = self._feed_m(x)
        s = self._feed_s(x)
        e = np.random.standard_normal(len(m))
        return m + s * e

    def feed_z(self, z):
        return self._feed_decoder(z)

    @staticmethod
    def _feed(x, w, a):
        for i, weights in enumerate(w):
            preactivation = np.matmul(weights, x)
            x = a(preactivation)
        return x

    def _feed_m(self, x):
        return PreTrainedVariational._feed(x, self.m_weights, self.encoder_act)

    def _feed_s(self, x):
        return PreTrainedVariational._feed(x, self.s_weights, self.encoder_act)

    def _feed_decoder(self, x):
        return PreTrainedVariational._feed(x, self.decoder_weights, self.decoder_act)

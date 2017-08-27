import numpy as np
from featureflow import Node


def log_modulus(x):
    return np.sign(x) * np.log(np.abs(x) + 1)


def inverse_log_modulus(x):
    return (np.exp(np.abs(x)) - 1) * np.sign(x)


def decibel(x):
    return 20 * np.log10(x)


def mu_law(x, mu=255):
    s = np.sign(x)
    return s * (np.log(1 + (mu * np.abs(x))) / np.log(1 + mu))


class MuLaw(Node):
    def __init__(self, mu=255, needs=None):
        super(MuLaw, self).__init__(needs=needs)
        self.mu = mu

    def _process(self, data):
        yield mu_law(data, mu=self.mu)
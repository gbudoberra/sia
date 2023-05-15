import numpy as np


def get_distance(u, v):
    return np.sqrt(np.linalg.norm(u - v))

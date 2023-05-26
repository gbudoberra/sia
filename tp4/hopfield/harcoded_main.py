from tp4.hopfield.hopfield import Hopfield
import numpy as np

patterns = [
    [
        -1, 1, -1, -1, 1,  # K
        -1, 1, -1, 1, -1,
        -1, 1, 1, -1, -1,
        -1, 1, -1, 1, -1,
        -1, 1, -1, -1, 1
    ],
    [
        1, -1, -1, -1, -1,  # L
        1, -1, -1, -1, -1,
        1, -1, -1, -1, -1,
        1, -1, -1, -1, -1,
        1, 1, 1, 1, 1
    ],
    [
        -1, -1, 1, -1, -1,  # I
        -1, -1, 1, -1, -1,
        -1, -1, 1, -1, -1,
        -1, -1, 1, -1, -1,
        -1, -1, 1, -1, -1,
    ],
    [
        1, 1, 1, 1, 1,  # P
        1, -1, -1, -1, 1,
        1, 1, 1, 1, 1,
        1, -1, -1, -1, -1,
        1, -1, -1, -1, -1,
    ]
]


def noise_with_p(pattern, p):
    noisy_pattern = []
    for x in pattern:
        rand = np.random.uniform(0, 1)
        if rand < p:
            noisy_pattern.append(1 if x == -1 else -1)
        else:
            noisy_pattern.append(x)
    return noisy_pattern


if __name__ == '__main__':
    hopfield = Hopfield(patterns, 1000)
    modified_p = noise_with_p(patterns[3], 0.3)
    filename = f'./images/results/harcoded_result'
    result = hopfield.get_pattern(modified_p, filename, 5)





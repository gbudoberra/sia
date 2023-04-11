import numpy as np

from tp2.genotype.genotype import Genotype


class ColorGenotype(Genotype):
    def __init__(self, red, green, blue, color_genotype):
        super().__init__()
        self.goal = color_genotype
        self.red = red
        self.green = green
        self.blue = blue

    def get_fitness(self):
        p1 = np.array([self.red, self.green, self.blue])
        p2 = np.array([self.goal.red, self.goal.green, self.goal.blue])
        return -1 * np.linalg.norm(p1 - p2)

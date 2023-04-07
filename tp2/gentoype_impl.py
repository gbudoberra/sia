from random import random

from tp2.genotype import Genotype


class GenotypeImpl(Genotype):
    def __init__(self):
        super().__init__()
        self.value = random()

    def get_fitness(self):
        return self.value

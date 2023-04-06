from generic_genetic import GenericGenetic
from tp2.generic_selection_method import GenericSelectionMethod


def sort_by_fitness(genotype):
    return genotype.get_fitness()


class EliteGenetic(GenericSelectionMethod):

    def __init__(self, size):
        super().__init__(size)

    def _select_parents(self, population):
        genotype_and_fitness = []
        for genotype in population:
            genotype_and_fitness.append(genotype)
        return sorted(genotype_and_fitness, key=sort_by_fitness)[:self.new_generation_size]

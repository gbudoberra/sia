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
        sorted_population = sorted(genotype_and_fitness, key=sort_by_fitness, reverse=True)[:self.new_generation_size]

        survivors = []
        for i in range(len(sorted_population)):
            n_times = self.calculate_individual_times(len(population), i)
            if n_times == 0:
                break
            for j in range(n_times):
                survivors.append(sorted_population[i])
        return survivors

    def calculate_individual_times(self, size, index):
        # we are using constant population size, so the formula is 1 - i/n
        return round(1 - index/size)
from generic_genetic import GenericGenetic


def sort_by_fitness(genotype):
    return genotype.get_fitness()


class EliteGenetic(GenericGenetic) :

    def _select_parents(self):
        pass

    def _crossover(self):
        pass

    def _mutate_population(self):
        pass

    def _generate_new_population(self):
        genotype_and_fitness = []
        for genotype in self.population:
            genotype_and_fitness.append(genotype)
        return sorted(genotype_and_fitness, key=sort_by_fitness)[:self.new_generation_size]

    def acceptable_solution(self):
        pass

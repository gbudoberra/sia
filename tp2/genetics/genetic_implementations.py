
from generic_genetic import GenericGenetic
from tp2.mutation.mutation import mutation_uniform_gen
from tp2.methods.elite_genetic import EliteGenetic
from tp2.methods.roulette_genetic import RouletteGenetic


class EliteUniformMutationGenetics(GenericGenetic):
    def __init__(self, population, size, generated_son, mutation_probability, delta):
        super().__init__(population, size, generated_son, mutation_probability, delta,
                         EliteGenetic(self.generated_son), EliteGenetic(self.population_size))

    def _mutate_each_son(self, son):
        return mutation_uniform_gen(son, self.mutation_probability, self.delta)


class RouletteUniformMutationGenetics(GenericGenetic):
    def __init__(self, population, size, generated_son, mutation_probability, delta):
        super().__init__(population, size, generated_son, mutation_probability, delta,
                         RouletteGenetic(self.generated_son),  RouletteGenetic(self.population_size))

    def _mutate_each_son(self, son):
        return mutation_uniform_gen(son, self.mutation_probability, self.delta)



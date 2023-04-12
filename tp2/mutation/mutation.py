from random import random, randint, uniform
from tp2.genotype.color_genotype import ColorGenotype


def normalize_proportions(new_genotype: ColorGenotype):
    size = len(new_genotype.color_proportion)
    total = sum(new_genotype.color_proportion)
    new_genotype.color_proportion = [new_genotype.color_proportion[i]/total for i in range(size)]
    return new_genotype


def mutation_limited_multigen(mutation_probability, genotype: ColorGenotype):
    new_color_proportion = [proportion for proportion in genotype.color_proportion]
    color_palette_size = len(new_color_proportion)
    mutating_quantity = randint(1, color_palette_size)
    starting_index = randint(0, color_palette_size - 1) % color_palette_size
    for i in range(mutating_quantity):
        if random() < mutation_probability:
            new_color_proportion[(starting_index + i) % color_palette_size] = random()
    return ColorGenotype(genotype.color_palette, new_color_proportion, genotype.goal)


def mutation_uniform_gen(mutation_probability, genotype: ColorGenotype):
    new_color_proportion = [proportion for proportion in genotype.color_proportion]
    color_palette_size = len(new_color_proportion)
    for i in range(color_palette_size):
        if random() < mutation_probability:
            new_color_proportion[i] = random()
    return ColorGenotype(genotype.color_palette, new_color_proportion, genotype.goal)


def complete_mutation(mutation_probability, genotype: ColorGenotype):
    if random() < mutation_probability:
        new_color_proportion = [proportion for proportion in genotype.color_proportion]
        color_palette_size = len(new_color_proportion)
        for i in range(color_palette_size):
            new_color_proportion[i] = random()
        return ColorGenotype(genotype.color_palette, new_color_proportion, genotype.goal)

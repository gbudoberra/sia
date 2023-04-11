from random import random, randint

from tp2.genotype.color_genotype import ColorGenotype


def mutate(value, probability, delta):
    delta = randint(-delta, delta)
    if random() < probability:
        value = (value + delta) % 255
    return value


def mutation_limited_multigen(mutation_probability, genotype: ColorGenotype, delta):
    gens_q = randint(1, 3)
    genotype.red = mutate(genotype.red, mutation_probability, delta)
    if gens_q > 1:
        genotype.green = mutate(genotype.green, mutation_probability, delta)
    if gens_q > 2:
        genotype.blue = mutate(genotype.blue, mutation_probability, delta)
    return genotype


def mutation_uniform_gen(mutation_probability, genotype: ColorGenotype, delta):
    genotype.red = mutate(genotype.red, mutation_probability, delta)
    genotype.green = mutate(genotype.green, mutation_probability, delta)
    genotype.blue = mutate(genotype.blue, mutation_probability, delta)
    return genotype


def complete_mutation(mutation_probability, genotype: ColorGenotype, delta):
    if random() < mutation_probability:
        return ColorGenotype((genotype.red + randint(-delta, delta)) % 255,
                             (genotype.green + randint(-delta, delta)) % 255,
                             (genotype.blue + randint(-delta, delta)) % 255)
    return genotype

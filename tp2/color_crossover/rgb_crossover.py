from random import random

from tp2.genotype.color_genotype import ColorGenotype


def uniform_crossover(dad: ColorGenotype, mom: ColorGenotype):
    dad_properties = [dad.red, dad.blue, dad.green]
    mom_properties = [mom.red, mom.blue, mom.green]
    first_son = []
    second_son = []
    for i in range(len(dad_properties)):
        random_num = random()
        first_son.append(dad_properties[i] if random_num <= 0.5 else mom_properties[i])
        second_son.append(mom_properties[i] if random_num < 0.5 else dad_properties[i])
    return ColorGenotype(first_son[0], first_son[1], first_son[2]), ColorGenotype(second_son[0], second_son[1],
                                                                                  second_son[2])

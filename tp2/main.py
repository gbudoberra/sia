from tp2.deterministic_tournament_genetic import DeterministicTournamentGenetic
from tp2.elite_genetic import EliteGenetic
from tp2.gentoype_impl import GenotypeImpl

if __name__ == '__main__':
    print("Starting")
    genotypes = []
    for i in range(10):
        genotypes.append(GenotypeImpl())
        print(genotypes[i].value)
    print('--------')
    method = DeterministicTournamentGenetic(10, 4)
    parents = method._select_parents(genotypes)
    for p in parents:
        print(p[0].get_fitness())

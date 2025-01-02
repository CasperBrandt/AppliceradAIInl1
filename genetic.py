import pandas as pd
import random
from lager import Lager

CAPACITY = 800
POPULATION_SIZE = 100
GENERATIONS = 100
MUTATION_RATE = 0.5
MAX_MUTATIONS = 5
# CROSSOVER_RATE = 1
    
def create_individual(CHROMOSOME_LENGTH):
    return [0 for _ in range(CHROMOSOME_LENGTH)]
    
def fitness(individual, lager):
    vikt = 0
    fitness = 0
    gene_no = 0
    for x in individual:
        if x == 1:
            # paket = lager_1.lagerstatus.iloc[gene_no]
            # fitness += paket['Förtjänst']
            # vikt += paket['Vikt']
            fitness += int(lager.lagerstatus['Förtjänst'].iloc[gene_no])
            vikt += float(lager.lagerstatus['Vikt'].iloc[gene_no])
        gene_no +=1
    if vikt > CAPACITY:
        fitness = 0
    return fitness

def selection(population, lager):
    tournament_size = 5
    selected = []
    for _ in range(len(population)):
        competitors = random.sample(population, tournament_size)
        winner = max(competitors, key=lambda a:fitness(a, lager))
        selected.append(winner)
    return selected

def crossover(parent1, parent2):
    # if random.random() < CROSSOVER_RATE:
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2
    # else:
    #     return parent1, parent2

def mutate(individual):
    if random.random() < MUTATION_RATE:
        no_mutations = random.randint(1, MAX_MUTATIONS)
        for _ in range(no_mutations):
            mutation_point = random.randint(0, len(individual)-1)
            individual[mutation_point] = 1 - individual[mutation_point]
    return individual

# def mutate(individual):
#     for i in range(len(individual)):
#         if random.random() < MUTATION_RATE:
#             individual[i] = 1 - individual[i]
#     return individual

def find_goat(lager:Lager):
    CHROMOSOME_LENGTH = lager.antal_paket()
    population = [create_individual(CHROMOSOME_LENGTH) for _ in range(POPULATION_SIZE)]
    goat = None
    goat_gen = 0
    for generation in range(GENERATIONS):
        population = sorted(population, key=lambda a:fitness(a, lager), reverse=True)

        best_individual = population[0]
        if goat == None or fitness(best_individual, lager) > fitness(goat, lager):
            goat = best_individual.copy()
            goat_gen = generation
        # print(f"Generation {generation}: Bästa fitness = {fitness(best_individual)} ---- Goat fitness = {fitness(goat)} gen {goat_gen}")

        selected = selection(population, lager)

        next_generation = []

        elite_size = 2
        next_generation.extend(population[:elite_size])

        while len(next_generation) < POPULATION_SIZE:
            parent1, parent2 = random.sample(selected, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            next_generation.extend([child1, child2])

        population = next_generation[:POPULATION_SIZE]
        
    return goat
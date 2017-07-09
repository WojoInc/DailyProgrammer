#################################################################################
# daily_249/genetic_practice.py
# Description:
# This script served as a learning tool to introduce myself to the mechanics of
# genetic algorithms in preparation for completing challenge #249-Intermediate
# from r/DailyProgrammer
#
# Created following tutorial found at:
# https://lethain.com/genetic-algorithms-cool-name-damn-simple/
#
# Created by Thomas John Wesolowski <wojoinc@iastate.edu> on 07/09/2017
#################################################################################

from random import randint, random


def individual(length, min, max):
    'Create a member of the population'
    return [randint(min, max) for x in range(length)]


def population(count, length, min, max):
    'Create a number of individuals equal to count'
    return [individual(length, min, max) for x in range(min, max)]


def fitness(individual, target):
    """
    Determine an individual's fitness

    :param individual: the individual we want to evaluate
    :param target: for this problem, the sum that the sum of the individual is aiming for
    :return: the fitness of the individual, where 0 is a perfect fit.
    """
    res = sum(i for i in individual)
    return abs(target - res)


def grade(population, target):
    'Determine the average fitness for the population'

    summed = sum(fitness(x, target) for x in population)
    return summed / len(population) * 1.0


def evolve(population, target, retain=0.2, rand_select=0.05, mutate=0.01):
    graded = [(fitness(x, target), x) for x in population]  # grade the population
    graded = [x[1] for x in sorted(graded)]  # turn graded into a list of parents
    retain_length = int(len(graded) * retain)  # determine the amount of individuals to retain
    parents = graded[:retain_length]

    # for diversity, add random individuals
    for individual in graded[retain_length:]:
        if rand_select > random():
            parents.append(individual)

    # mutate a few individuals
    for individual in parents:
        if mutate > random():
            mutate_position = randint(0, len(individual) - 1)
            # this function mutates one of the values of the individual, however,
            # the mutation is limited to being within the min and max of the individual
            # as the function is not aware of the min/max values used to create the individual
            individual[mutate_position] = randint(min(individual), max(individual))

    # crossover parents to create children
    parents_len = len(parents)
    child_len = len(population) - parents_len

    children = []

    while len(children) < child_len:
        # choose random parents, make sure that no two parents are the same
        male = randint(0, parents_len - 1)
        female = randint(0, parents_len - 1)
        if female != male:
            # create child by taking half of the values from each parent individual
            male = parents[male]
            female = parents[female]
            half = int(len(male) / 2)
            child = male[:half] + female[half:]
            children.append(child)
    parents.extend(children)
    return parents


# Start of execution, get parameters from the user
# TODO add the ability to tweak the mutation and retention parameters

print("This script will use a genetic algorithm to create a list of N numbers that sum to the target value.")
target = int(input("Enter target sum: "))
length = int(input("Enter a value for N: "))
val_min = int(input("Specify a minimum value for each number: "))
val_max = int(input("Specify a maximum value for each number: "))
p_size = int(input("How large would you like each population? "))

pop = population(p_size, length, val_min, val_max)
fitness_tracker = [grade(pop, target)]

# Keep track of the fitness of each population
# Then stop once the population has achieved a solution
# For other problems, the population could be allowed to 'bounce' around 0, giving multiple
# different solutions to the problem. I will eventually adapt this script to do just that.

while fitness_tracker[-1] != 0:
    pop = evolve(pop, target)
    fitness_tracker.append(grade(pop, target))

i = 0
for data in fitness_tracker:
    print("Population " + str(i) + " fitness rating: " + str(data))
    i += 1
print("Final answer: " + str(pop[0]) + " = " + str(sum(i for i in pop[0])))

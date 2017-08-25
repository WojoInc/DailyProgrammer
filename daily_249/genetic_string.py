# genetic_string
# Description:
#
# Created by Thomas John Wesolowski <wojoinc@iastate.edu> on 7/9/17

# generate an individual
# in this case a string of the same length as the input string, and we
# assume the list of printable ascii characters from 0x20 to 0x7E

from random import randint, random

MIN = 0x20
MAX = 0x7E


def individual(length, min=MIN, max=MAX):
    return [randint(min, max) for x in range(length)]


def population(count, length, min=MIN, max=MAX):
    """
    Returns a population of individuals
    :param count: number of individuals
    :param length: length in chars, of each individual
    :param min: minimum integer value of characters, default=0x20
    :param max: maximum integer value of characters, default=0x7E
    :return: a list of individuals
    """

    return [individual(length, min, max) for x in range(count)]


def fitness(individual, target):
    """
    Use a simple hamming weight to determine fitness of the individual
    :param individual: individual to test
    :param target: target to test against
    :return: the fitness of the individual as a float, closer to 0 is better
    """
    # I will use zip() here, but this could be done by simply iterating through
    # each list by a common index as well, this in fact, should be done if I were
    # using python 2 to avoid massive allocation of a potentially long variable.

    weight = 0
    for a, b in zip(individual, target):
        if a != b:
            weight += 1
    return weight


def grade(population, target):
    'Sum all the individual fitnesses, and give an overall fitness for population'
    fit_sum = sum(fitness(individual, target) for individual in population)
    return fit_sum / len(population) * 1.0


def evolve(population, target, retain=0.1, rand_select=0.15, mutation=0.03):
    # grade the population, create a list of tuples, sort that list
    # then extract the sorted individuals and store in graded
    # this effectively sorts the list by hamming weight in two lines
    graded = [(fitness(x, target), x) for x in population]
    graded = [x[1] for x in sorted(graded)]

    retain_length = int(len(graded) * retain)
    parents = graded[:retain_length]

    # add random individuals
    for individual in graded[retain_length:]:
        if rand_select > random():
            parents.append(individual)

    # randomly mutate parents
    for individual in parents:
        if mutation > random():
            mutate_pos = randint(0, len(individual) - 1)
            # TODO test effect of using global min and max in randomly generating new value
            # here, I am again choosing a new value based on the min and max of
            # the individual, I should come back and examine the effectiveness of
            # a global min max for the random mutation
            individual[mutate_pos] = randint(min(individual), max(individual))

    # create children
    children_len = len(population) - len(parents)
    children = []
    while len(children) < children_len:
        male = randint(0, len(parents) - 1)
        female = randint(0, len(parents) - 1)

        if male != female:
            male = parents[male]
            female = parents[female]
            # TODO update generation of child to be more random?
            # could update half later to randomly choose values from each parent
            # not sure of the effects of this however
            half = int(len(male) / 2)
            child = male[:half] + female[half:]
            children.append(child)
    parents.extend(children)
    return parents


def s_int_l(string):
    'converts string to list of integers representing each characters ASCII value'
    return [ord(char) for char in string]


def i_lst_s(int_list):
    'convert list of integers into a single string'
    return ''.join([chr(char) for char in int_list])


# Start of execution, get parameters from the user
# TODO add the ability to tweak the mutation and retention parameters

print("This script will use a genetic algorithm to determine the input phrase from a randomly generated"
      " population of characters")
target = s_int_l(input("Enter an input phrase: "))
length = len(target)
# p_size = int(input("How large would you like each population? "))
# Scale population based on input length
p_size = length * 5000
print("Using a population of size: ", p_size)

# allow the mutation reate to scale with input length
mutate_rate = 1 / len(target)

# TODO test if this scaling of rand_select and retain actually helps

rand_select = 1 / (len(target))
retain = 1 / (len(target))
pop_size = len(target) * 100

pop = population(pop_size, length)
fitness_tracker = [grade(pop, target)]
most_fit = [(fitness(pop[0], target), pop[0])]

# Keep track of the fitness of each population
# Then stop once the population has achieved a solution, as there is at most one solution for this problem
i = 0
# while the closest individual is not the solution, continue
while most_fit[-1][0] != 0:
    pop = evolve(pop, target, retain=retain, rand_select=rand_select, mutation=mutate_rate)
    fitness_tracker.append(grade(pop, target))
    most_fit.append((fitness(pop[0], target), pop[0]))
    print("Gen " + str(i) + " closest individual: " + i_lst_s(most_fit[i][1])
          + " with FR: " + str(most_fit[i][0]) + " AVG: " + str(fitness_tracker[-1]))
    i += 1

print("Final answer: " + i_lst_s(pop[0]) + " Found in ", i, " generations")

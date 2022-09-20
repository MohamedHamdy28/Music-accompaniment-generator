import random
import string
from random import randint
from music21 import *
from generator import Generator
from genetics import Genetics

def run():
    generator = Generator()
    genetics = Genetics()
    input_song = converter.parse('input1.mid') # parsing the input
    the_key = input_song.analyze('key') # analyzing for the key of the input song
    population_size = 100 # setting the population type
    bars = len(input_song.recurse().getElementsByClass('Measure')) # checking for the number of bars in the input melody
    octave = generator.lowest_octave(input_song) - 1 # choosing the octave for the chords
    population = genetics.generate_population(the_key, bars, octave, population_size) # generating the population
    generation_limit = 1000 # setting the number of generations
    fitness_score = None
    for i in range(generation_limit):
        fitness_score = genetics.fitness(population,input_song,bars,population_size) # calculating the fitness score for each individual
        fitness_score = sorted(fitness_score.items(), key=lambda x: x[1], reverse=True)
        a, b = genetics.select_pair(fitness_score) # selecting random pair based on the fitness score
        a = fitness_score[a]
        b = fitness_score[b]
        offspring_a, offspring_b = genetics.cross_over(population[a[0]], population[b[0]], bars) # making a crossover between offspring a and b
        offspring_a = genetics.mutation(offspring_a, bars, the_key, octave) # calling mutation for the offspring a and b
        offspring_b = genetics.mutation(offspring_b, bars, the_key, octave)
        population[a[0]] = offspring_a # replacing the parents with the offspring
        population[b[0]] = offspring_b
    s = stream.Stream()
    for i in range(bars):
        m = stream.Measure(population[fitness_score[0][0]][i])
        s.append(m)

    s.write('mid','MohamedHamdyOutput1.mid') # writing the best individual to midi file

def main():
    run()


if __name__ == '__main__':
    main()

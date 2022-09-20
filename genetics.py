import random
import string
from random import randint
from generator import Generator
from music21 import *

class Genetics:
    def __init__(self):
        self.major_keys = {
        'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'C#': ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#'],
        'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
        'D#': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],
        'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
        'F': ['F', 'G', 'A', 'A#', 'C', 'D', 'E'],
        'F#': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#'],
        'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
        'G#': ['G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F#'],
        'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
        'A#': ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'],
        'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']
        }
        self.minor_keys = {
            'C': ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#'],
            'C#': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
            'D': ['D', 'E', 'F', 'G', 'A', 'A#', 'C'],
            'D#': ['D#', 'E#', 'F#', 'G#', 'A#', 'B', 'C#'],
            'E': ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
            'F': ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#'],
            'F#': ['F#', 'G', 'A', 'B', 'C#', 'D', 'E'],
            'G': ['G', 'A', 'A#', 'C', 'D', 'D#', 'F'],
            'G#': ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#'],
            'A': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            'A#': ['A#', 'B#', 'C#', 'D#', 'E#', 'F#', 'G#'],
            'B': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']
        }
        self.KEYS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.generator = Generator()

    # this function used to generates the population were each individual
    # is a sequence of random chords
    def generate_population(self, the_key: string, bars: int, octave: int, population_size: int):
        population = []
        root_note = str(the_key).split()[0].capitalize()
        for i in range(population_size):
            rows = []
            for j in range(bars):
                bar = []  # each bar contains 4 chords
                for k in range(4):
                    if the_key.type == 'major':
                        row = self.major_keys.get(root_note)
                        random_note = row[randint(0,6)]
                        the_chord = self.generator.random_chord(random_note,octave)
                        bar.append(the_chord)
                    elif the_key.type == 'minor':
                        row = self.minor_keys.get(root_note)
                        random_note = row[randint(0,6)]
                        the_chord = self.generator.random_chord(random_note,octave)
                        bar.append(the_chord)
                    else:
                        print('Error, the key type was not detected')
                rows.append(bar)
            population.append(rows)
        return population
    
    # this is our fitness function, it is explained in more details in the report
    def fitness(self, population, input_song,bars,population_size):
        fitness_score = {}
        # we are checking if the root note of the chord is equal to the note played at the same offset
        for i in range(population_size):
            current_score = 1000
            for j in range(bars):
                offset = 0.0
                for k in range(4):
                    if not isinstance(population[i][j][k], note.Rest):
                        for l in input_song.recurse():
                            if isinstance(l,note.Note):
                                if l.offset == offset:
                                    root_note = population[i][j][k].root().name
                                    note_name = l.name
                                    if l.name == 'B-':
                                        note_name = 'A#'
                                    distance = abs(self.KEYS.index(note_name) - self.KEYS.index(root_note))
                                    if distance == 0:
                                        current_score += 5
                                    else:
                                        current_score -= distance
                                    break

                    offset += 1.0
            fitness_score[i] = current_score
        return fitness_score

    # The selection technique used is the roulette wheel selection
    def select_pair(self, fitness_score):

        a=[]
        b=[]
        for i in range(len(fitness_score)):
            a.append(fitness_score[i][0])
            b.append(fitness_score[i][1])
        return (random.choices(
            population=a,
            weights=b,
            k=2
        ))
    
    # N point crossover
    def cross_over(self, father,mother, bars):
        offspring_a = []
        offspring_b = []
        for i in range(bars):
            a = []
            b = []
            for j in range(4):
                random_choice = randint(0,1)
                if random_choice == 0:
                    a.append(father[i][j])
                    b.append(mother[i][j])
                else:
                    a.append(mother[i][j])
                    b.append(father[i][j])
            offspring_a.append(a)
            offspring_b.append(b)
        return offspring_a, offspring_b

    # the mutation used is that we choose a random chord in a random bar in the individual
    # and replace it with a random chord with random root note and random chord type
    def mutation(self, citizen, bars, the_key, octave, probability: float = 0.05, num=1):
        root_note = str(the_key).split()[0].capitalize()
        for _ in range(num):
            index1 = random.randrange(bars)
            index2 = random.randrange(3)
            if random.random() < probability:
                r = randint(0, 3)
                if r == 0:
                    if the_key.type == 'major':
                        citizen[index1][index2] = self.generator.gengenerate_first_inversion_major(self.major_keys.get(root_note)[randint(0, 6)],
                                                                                octave)
                    else:
                        citizen[index1][index2] = self.generator.generate_first_inversion_minor(self.minor_keys.get(root_note)[randint(0, 6)],
                                                                                octave)
                elif r == 1:
                    if the_key.type == 'major':
                        citizen[index1][index2] = self.generator.generate_second_inversion_major(self.major_keys.get(root_note)[randint(0, 6)],
                                                                                octave)
                    else:
                        citizen[index1][index2] = self.generator.generate_second_inversion_minor(self.minor_keys.get(root_note)[randint(0, 6)],
                                                                                octave)
                elif r == 2:
                    if the_key.type == 'major':
                        citizen[index1][index2] = self.generator.generate_sus2(self.major_keys.get(root_note)[randint(0, 6)], octave)
                    else:
                        citizen[index1][index2] = self.generator.generate_sus2(self.minor_keys.get(root_note)[randint(0, 6)], octave)
                elif r == 3:
                    if the_key.type == 'major':
                        citizen[index1][index2] = self.generator.generate_sus4(self.major_keys.get(root_note)[randint(0, 6)], octave)
                    else:
                        citizen[index1][index2] = self.generator.generate_sus4(self.minor_keys.get(root_note)[randint(0, 6)], octave)

        return citizen
import random
import string
from random import randint
from music21 import *
# global variables
major_keys = {
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
minor_keys = {
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
KEYS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# this function gets the lowest octave played in the input song
# to use it as an octave for the chords
def lowest_octave(input_song):
    lowest = 100
    for i in input_song.recurse().getElementsByClass('Note'):
        if i.octave < lowest:
            lowest = i.octave
    return lowest

# the following functions generates the different types of chords
# it takes as input the root note for the chord and its octave and return the chord
def generate_major_trait(root: string, octave: int):
    if KEYS.index(root) + 4 > len(KEYS) - 1:
        forth = KEYS[KEYS.index(root) + 4 - (len(KEYS))]
    else:
        forth = KEYS[KEYS.index(root) + 4]
    if KEYS.index(root) + 7 > (len(KEYS) - 1):
        seventh = KEYS[KEYS.index(root) + 7 - (len(KEYS))]
    else:
        seventh = KEYS[KEYS.index(root) + 7]
    theChord = chord.Chord([f'{root}{octave}', f'{forth}{octave}', f'{seventh}{octave}'])
    return theChord
def generate_minor_trait(root: string, octave: int):
    if KEYS.index(root) + 3 > len(KEYS) - 1:
        third = KEYS[KEYS.index(root) + 3 - len(KEYS)]
    else:
        third = KEYS[KEYS.index(root) + 3]
    if KEYS.index(root) + 7 > len(KEYS) - 1:
        seventh = KEYS[KEYS.index(root) + 7 - len(KEYS)]
    else:
        seventh = KEYS[KEYS.index(root) + 7]
    theChord = chord.Chord([f'{root}{octave}', f'{third}{octave}', f'{seventh}{octave}'])
    return theChord
def generate_first_inversion_major(root: string, octave: int):
    if KEYS.index(root) + 4 > len(KEYS) - 1:
        forth = KEYS[KEYS.index(root) + 4 - (len(KEYS))]
    else:
        forth = KEYS[KEYS.index(root) + 4]
    if KEYS.index(root) + 7 > (len(KEYS) - 1):
        seventh = KEYS[KEYS.index(root) + 7 - (len(KEYS))]
    else:
        seventh = KEYS[KEYS.index(root) + 7]
    theChord = chord.Chord([f'{forth}{octave}', f'{seventh}{octave}', f'{root}{octave + 1}'])
    return theChord
def generate_first_inversion_minor(root: string, octave: int):
    if KEYS.index(root) + 3 > len(KEYS) - 1:
        third = KEYS[KEYS.index(root) + 3 - len(KEYS)]
    else:
        third = KEYS[KEYS.index(root) + 3]
    if KEYS.index(root) + 7 > len(KEYS) - 1:
        seventh = KEYS[KEYS.index(root) + 7 - len(KEYS)]
    else:
        seventh = KEYS[KEYS.index(root) + 7]
    theChord = chord.Chord([f'{third}{octave}', f'{seventh}{octave}', f'{root}{octave + 1}'])
    return theChord
def generate_second_inversion_major(root: string, octave: int):
    if KEYS.index(root) + 4 > len(KEYS) - 1:
        forth = KEYS[KEYS.index(root) + 4 - (len(KEYS))]
    else:
        forth = KEYS[KEYS.index(root) + 4]
    if KEYS.index(root) + 7 > (len(KEYS) - 1):
        seventh = KEYS[KEYS.index(root) + 7 - (len(KEYS))]
    else:
        seventh = KEYS[KEYS.index(root) + 7]
    theChord = chord.Chord([f'{forth}{octave + 1}', f'{seventh}{octave}', f'{root}{octave + 1}'])
    return theChord
def generate_second_inversion_minor(root: string, octave: int):
    if KEYS.index(root) + 3 > len(KEYS) - 1:
        third = KEYS[KEYS.index(root) + 3 - len(KEYS)]
    else:
        third = KEYS[KEYS.index(root) + 3]
    if KEYS.index(root) + 7 > len(KEYS) - 1:
        seventh = KEYS[KEYS.index(root) + 7 - len(KEYS)]
    else:
        seventh = KEYS[KEYS.index(root) + 7]
    theChord = chord.Chord([f'{third}{octave + 1}', f'{seventh}{octave}', f'{root}{octave + 1}'])
    return theChord
def generate_diminished(root: string, octave: int):
    if KEYS.index(root) + 3 > len(KEYS) - 1:
        third = KEYS[KEYS.index(root) + 3 - len(KEYS)]
    else:
        third = KEYS[KEYS.index(root) + 3]
    if KEYS.index(root) + 6 > len(KEYS) - 1:
        sixth = KEYS[KEYS.index(root) + 6 - len(KEYS)]
    else:
        sixth = KEYS[KEYS.index(root) + 6]
    theChord = chord.Chord([f'{root}{octave}', f'{third}{octave}', f'{sixth}{octave}'])
    return theChord
def generate_sus2(root: string, octave: int):
    if KEYS.index(root) + 2 > len(KEYS) - 1:
        second = KEYS[KEYS.index(root) + 2 - len(KEYS)]
    else:
        second = KEYS[KEYS.index(root) + 2]
    if KEYS.index(root) + 7 > len(KEYS) - 1:
        seventh = KEYS[KEYS.index(root) + 7 - len(KEYS)]
    else:
        seventh = KEYS[KEYS.index(root) + 7]
    theChord = chord.Chord([f'{root}{octave}', f'{second}{octave}', f'{seventh}{octave}'])
    return theChord
def generate_sus4(root: string, octave: int):
    if KEYS.index(root) + 5 > len(KEYS) - 1:
        fifth = KEYS[KEYS.index(root) + 5 - len(KEYS)]
    else:
        fifth = KEYS[KEYS.index(root) + 5]
    if KEYS.index(root) + 7 > len(KEYS) - 1:
        seventh = KEYS[KEYS.index(root) + 7 - len(KEYS)]
    else:
        seventh = KEYS[KEYS.index(root) + 7]
    theChord = chord.Chord([f'{root}{octave}', f'{fifth}{octave}', f'{seventh}{octave}'])
    return theChord

# this function generates random chord type
def random_chord(root_note, octave):
    chord_type = randint(1, 10)
    the_chord = None
    if chord_type == 1:
        the_chord = generate_major_trait(root_note, octave)
    elif chord_type == 2:
        the_chord = generate_minor_trait(root_note, octave)
    elif chord_type == 3:
        the_chord = generate_first_inversion_major(root_note, octave)
    elif chord_type == 4:
        the_chord = generate_first_inversion_minor(root_note, octave)
    elif chord_type == 5:
        the_chord = generate_second_inversion_major(root_note, octave)
    elif chord_type == 6:
        the_chord = generate_second_inversion_minor(root_note, octave)
    elif chord_type == 7:
        the_chord = generate_diminished(root_note, octave)
    elif chord_type == 8:
        the_chord = generate_sus2(root_note, octave)
    elif chord_type == 9:
        the_chord = generate_sus4(root_note, octave)
    elif chord_type == 10:
        the_chord = note.Rest()
    return the_chord

# this function used to generates the population were each individual
# is a sequence of random chords
def generate_population(the_key: string, bars: int, octave: int, population_size: int):
    population = []
    root_note = str(the_key).split()[0].capitalize()
    for i in range(population_size):
        rows = []
        for j in range(bars):
            bar = []  # each bar contains 4 chords
            for k in range(4):
                if the_key.type == 'major':
                    row = major_keys.get(root_note)
                    random_note = row[randint(0,6)]
                    the_chord = random_chord(random_note,octave)
                    bar.append(the_chord)
                elif the_key.type == 'minor':
                    row = minor_keys.get(root_note)
                    random_note = row[randint(0,6)]
                    the_chord = random_chord(random_note,octave)
                    bar.append(the_chord)
                else:
                    print('Error, the key type was not detected')
            rows.append(bar)
        population.append(rows)
    return population

# this is our fitness function, it is explained in more details in the report
def fitness(population, input_song,bars,population_size):
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
                                distance = abs(KEYS.index(note_name) - KEYS.index(root_note))
                                if distance == 0:
                                    current_score += 5
                                else:
                                    current_score -= distance
                                break

                offset += 1.0
        fitness_score[i] = current_score
    return fitness_score

# The selection technique used is the roulette wheel selection
def select_pair(fitness_score):
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
def cross_over(father,mother,bars):
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
def mutation(citizen, bars, the_key, octave, probability: float = 0.05, num=1):
    root_note = str(the_key).split()[0].capitalize()
    for _ in range(num):
        index1 = random.randrange(bars)
        index2 = random.randrange(3)
        if random.random() < probability:
            r = randint(0, 3)
            if r == 0:
                if the_key.type == 'major':
                    citizen[index1][index2] = generate_first_inversion_major(major_keys.get(root_note)[randint(0, 6)],
                                                                             octave)
                else:
                    citizen[index1][index2] = generate_first_inversion_minor(minor_keys.get(root_note)[randint(0, 6)],
                                                                             octave)
            elif r == 1:
                if the_key.type == 'major':
                    citizen[index1][index2] = generate_second_inversion_major(major_keys.get(root_note)[randint(0, 6)],
                                                                              octave)
                else:
                    citizen[index1][index2] = generate_second_inversion_minor(minor_keys.get(root_note)[randint(0, 6)],
                                                                              octave)
            elif r == 2:
                if the_key.type == 'major':
                    citizen[index1][index2] = generate_sus2(major_keys.get(root_note)[randint(0, 6)], octave)
                else:
                    citizen[index1][index2] = generate_sus2(minor_keys.get(root_note)[randint(0, 6)], octave)
            elif r == 3:
                if the_key.type == 'major':
                    citizen[index1][index2] = generate_sus4(major_keys.get(root_note)[randint(0, 6)], octave)
                else:
                    citizen[index1][index2] = generate_sus4(minor_keys.get(root_note)[randint(0, 6)], octave)

    return citizen


def main():
    input_song = converter.parse('input1.mid') # parsing the input
    the_key = input_song.analyze('key') # analyzing for the key of the input song
    population_size = 100 # setting the population type
    bars = len(input_song.recurse().getElementsByClass('Measure')) # checking for the number of bars in the input melody
    octave = lowest_octave(input_song) - 1 # choosing the octave for the chords
    population = generate_population(the_key, bars, octave, population_size) # generating the population
    generation_limit = 1000 # setting the number of generations
    fitness_score = None
    for i in range(generation_limit):
        fitness_score = fitness(population,input_song,bars,population_size) # calculating the fitness score for each individual
        fitness_score = sorted(fitness_score.items(), key=lambda x: x[1], reverse=True)
        a, b = select_pair(fitness_score) # selecting random pair based on the fitness score
        a = fitness_score[a]
        b = fitness_score[b]
        offspring_a, offspring_b = cross_over(population[a[0]], population[b[0]], bars) # making a crossover between offspring a and b
        offspring_a = mutation(offspring_a, bars, the_key, octave) # calling mutation for the offspring a and b
        offspring_b = mutation(offspring_b, bars, the_key, octave)
        population[a[0]] = offspring_a # replacing the parents with the offspring
        population[b[0]] = offspring_b
    s = stream.Stream()
    for i in range(bars):
        m = stream.Measure(population[fitness_score[0][0]][i])
        s.append(m)

    s.write('mid','MohamedHamdyOutput1.mid') # writing the best individual to midi file


if __name__ == '__main__':
    main()

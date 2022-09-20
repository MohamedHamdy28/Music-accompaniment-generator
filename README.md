# Music-accompaniment-generator
The program takes a monophonic midi file, which represents melody. By using genetic programming (evolutionary algorithm), it generates an accompaniment. The accompaniment is a sequence of chords that can be played with the melody

## Genetic algorithm components:
### Population representation:
- The population is a list of N individuals where each one of them has a random chord sequence, representing one of the possible accompaniments.
- An individual is a sequence of chords, which contain the same number of bars as the input melody. Each bar contains 4 quarter duration chords.
### Fitness function:
- We evaluate each individual based on the distance between the played note and the root note of the chord played at the same offset. So, if the distance between them increases, this means we are far from the chord we need so we decrease its score. If they are the same, then we increase its score.
### Mutation technique:
- We choose a random chord in a random bar in the individual and replace it with a random chord with a random root note and random chord type.
- The probability for a mutation to happen is 5%
### Crossover technique:
- The crossover technique used is N point crossover, which achieved a higher fitness score than a single point and two-point crossover
- It decides whether to swap or not based on a randomly chosen value.
### Population size and selection techniques:
- Population size is defined at the beginning of the main function, it can be increased or decreased. However, the small number of the population gives poor results as there is a small number of variations, and a large number of the population takes time to calculate.
- A value of 100 that balances this trade-off is used for testing.
- The selection technique used is the roulette wheel selection, it is applied using the random.choices() function in python where it uses the relative fitness (ratio of individual fitness and total fitness) of each individual. This means that the individual with a high fitness score has a higher chance of being selected, while there is still a chance for the individual with a low fitness score to be selected, which brings more variation to the results.

## Dependencies
- Music21 which is a python library used to manipulate the midi files and generate melodies. You can install it from [here](https://web.mit.edu/music21/doc/installing/index.html)

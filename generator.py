import random
import string
from random import randint
from music21 import *

class Generator:
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



    def lowest_octave(self, input_song):
        lowest = 100
        for i in input_song.recurse().getElementsByClass('Note'):
            if i.octave < lowest:
                lowest = i.octave
        return lowest

    # the following functions generates the different types of chords
    # it takes as input the root note for the chord and its octave and return the chord
    def generate_major_trait(self, root: string, octave: int):
        if self.KEYS.index(root) + 4 > len(self.KEYS) - 1:
            forth = self.KEYS[self.KEYS.index(root) + 4 - (len(self.KEYS))]
        else:
            forth = self.KEYS[self.KEYS.index(root) + 4]
        if self.KEYS.index(root) + 7 > (len(self.KEYS) - 1):
            seventh = self.KEYS[self.KEYS.index(root) + 7 - (len(self.KEYS))]
        else:
            seventh = self.KEYS[self.KEYS.index(root) + 7]
        theChord = chord.Chord([f'{root}{octave}', f'{forth}{octave}', f'{seventh}{octave}'])
        return theChord

    def generate_minor_trait(self, root: string, octave: int):
        if self.KEYS.index(root) + 3 > len(self.KEYS) - 1:
            third = self.KEYS[self.KEYS.index(root) + 3 - len(self.KEYS)]
        else:
            third = self.KEYS[self.KEYS.index(root) + 3]
        if self.KEYS.index(root) + 7 > len(self.KEYS) - 1:
            seventh = self.KEYS[self.KEYS.index(root) + 7 - len(self.KEYS)]
        else:
            seventh = self.KEYS[self.KEYS.index(root) + 7]
        theChord = chord.Chord([f'{root}{octave}', f'{third}{octave}', f'{seventh}{octave}'])
        return theChord

    def generate_first_inversion_major(self, root: string, octave: int):
        if self.KEYS.index(root) + 4 > len(self.KEYS) - 1:
            forth = self.KEYS[self.KEYS.index(root) + 4 - (len(self.KEYS))]
        else:
            forth = self.KEYS[self.KEYS.index(root) + 4]
        if self.KEYS.index(root) + 7 > (len(self.KEYS) - 1):
            seventh = self.KEYS[self.KEYS.index(root) + 7 - (len(self.KEYS))]
        else:
            seventh = self.KEYS[self.KEYS.index(root) + 7]
        theChord = chord.Chord([f'{forth}{octave}', f'{seventh}{octave}', f'{root}{octave + 1}'])
        return theChord

    def generate_first_inversion_minor(self, root: string, octave: int):
        if self.KEYS.index(root) + 3 > len(self.KEYS) - 1:
            third = self.KEYS[self.KEYS.index(root) + 3 - len(self.KEYS)]
        else:
            third = self.KEYS[self.KEYS.index(root) + 3]
        if self.KEYS.index(root) + 7 > len(self.KEYS) - 1:
            seventh = self.KEYS[self.KEYS.index(root) + 7 - len(self.KEYS)]
        else:
            seventh = self.KEYS[self.KEYS.index(root) + 7]
        theChord = chord.Chord([f'{third}{octave}', f'{seventh}{octave}', f'{root}{octave + 1}'])
        return theChord
    def generate_second_inversion_major(self, root: string, octave: int):
        if self.KEYS.index(root) + 4 > len(self.KEYS) - 1:
            forth = self.KEYS[self.KEYS.index(root) + 4 - (len(self.KEYS))]
        else:
            forth = self.KEYS[self.KEYS.index(root) + 4]
        if self.KEYS.index(root) + 7 > (len(self.KEYS) - 1):
            seventh = self.KEYS[self.KEYS.index(root) + 7 - (len(self.KEYS))]
        else:
            seventh = self.KEYS[self.KEYS.index(root) + 7]
        theChord = chord.Chord([f'{forth}{octave + 1}', f'{seventh}{octave}', f'{root}{octave + 1}'])
        return theChord
    def generate_second_inversion_minor(self, root: string, octave: int):
        if self.KEYS.index(root) + 3 > len(self.KEYS) - 1:
            third = self.KEYS[self.KEYS.index(root) + 3 - len(self.KEYS)]
        else:
            third = self.KEYS[self.KEYS.index(root) + 3]
        if self.KEYS.index(root) + 7 > len(self.KEYS) - 1:
            seventh = self.KEYS[self.KEYS.index(root) + 7 - len(self.KEYS)]
        else:
            seventh = self.KEYS[self.KEYS.index(root) + 7]
        theChord = chord.Chord([f'{third}{octave + 1}', f'{seventh}{octave}', f'{root}{octave + 1}'])
        return theChord

    def generate_diminished(self, root: string, octave: int):
        if self.KEYS.index(root) + 3 > len(self.KEYS) - 1:
            third = self.KEYS[self.KEYS.index(root) + 3 - len(self.KEYS)]
        else:
            third = self.KEYS[self.KEYS.index(root) + 3]
        if self.KEYS.index(root) + 6 > len(self.KEYS) - 1:
            sixth = self.KEYS[self.KEYS.index(root) + 6 - len(self.KEYS)]
        else:
            sixth = self.KEYS[self.KEYS.index(root) + 6]
        theChord = chord.Chord([f'{root}{octave}', f'{third}{octave}', f'{sixth}{octave}'])
        return theChord
    def generate_sus2(self, root: string, octave: int):
        if self.KEYS.index(root) + 2 > len(self.KEYS) - 1:
            second = self.KEYS[self.KEYS.index(root) + 2 - len(self.KEYS)]
        else:
            second = self.KEYS[self.KEYS.index(root) + 2]
        if self.KEYS.index(root) + 7 > len(self.KEYS) - 1:
            seventh = self.KEYS[self.KEYS.index(root) + 7 - len(self.KEYS)]
        else:
            seventh = self.KEYS[self.KEYS.index(root) + 7]
        theChord = chord.Chord([f'{root}{octave}', f'{second}{octave}', f'{seventh}{octave}'])
        return theChord
    def generate_sus4(self, root: string, octave: int):
        if self.KEYS.index(root) + 5 > len(self.KEYS) - 1:
            fifth = self.KEYS[self.KEYS.index(root) + 5 - len(self.KEYS)]
        else:
            fifth = self.KEYS[self.KEYS.index(root) + 5]
        if self.KEYS.index(root) + 7 > len(self.KEYS) - 1:
            seventh = self.KEYS[self.KEYS.index(root) + 7 - len(self.KEYS)]
        else:
            seventh = self.KEYS[self.KEYS.index(root) + 7]
        theChord = chord.Chord([f'{root}{octave}', f'{fifth}{octave}', f'{seventh}{octave}'])
        return theChord

    # this function generates random chord type
    def random_chord(self, root_note, octave):
        chord_type = randint(1, 10)
        the_chord = None
        if chord_type == 1:
            the_chord = self.generate_major_trait(root_note, octave)
        elif chord_type == 2:
            the_chord = self.generate_minor_trait(root_note, octave)
        elif chord_type == 3:
            the_chord = self.generate_first_inversion_major(root_note, octave)
        elif chord_type == 4:
            the_chord = self.generate_first_inversion_minor(root_note, octave)
        elif chord_type == 5:
            the_chord = self.generate_second_inversion_major(root_note, octave)
        elif chord_type == 6:
            the_chord = self.generate_second_inversion_minor(root_note, octave)
        elif chord_type == 7:
            the_chord = self.generate_diminished(root_note, octave)
        elif chord_type == 8:
            the_chord = self.generate_sus2(root_note, octave)
        elif chord_type == 9:
            the_chord = self.generate_sus4(root_note, octave)
        elif chord_type == 10:
            the_chord = note.Rest()
        return the_chord


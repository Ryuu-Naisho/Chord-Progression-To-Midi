#!/usr/bin/env python3


from model import wStrings
from model import Keys
from controller import Chords
from controller import Scales
from controller import CircleOfFifths
import Debug

if __name__ == '__main__':
    Debug.write(wStrings.TITLE)
    Debug.write(wStrings.INTRO)
    keys = Keys.Key()
    key = keys.C
    key.isFlat = False
    '''print(key.name)'''
    chord = Chords.Chord(key, wStrings.MINOR7)
    chords = chord.getAllNotes
    '''for c in chords:
        print(c.name)'''


    scale = Scales.Scale(keys.E, wStrings.MAJOR)
    scale_of_e = scale.scale
    '''for note in scale_of_e:
        print(note.name)'''

    for note in scale_of_e:
        Debug.write(note.name)


    scale = Scales.Scale(keys.E, wStrings.MINOR)
    scale_of_em = scale.scale
    for note in scale_of_em:
        Debug.write(note.name)
    

    Debug.write(wStrings.Progressions.Blues)
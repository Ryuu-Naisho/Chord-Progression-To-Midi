#!/usr/bin/env python3


from model import wStrings
from model import Keys
from controller import Chords
from controller import Scales
from controller import CircleOfFifths
from controller import Progresssions
from controller import StepMaker
from controller import GenerateMidi
import Debug

if __name__ == '__main__':
    Debug.write(wStrings.TITLE)
    Debug.write(wStrings.INTRO)
    keys = Keys.Key()
    key = keys.C
    key.isFlat = False
    '''print(key.name)'''



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


    chord = Chords.Chord(scale_of_em, scale_of_em[0], wStrings.Numeral.v)
    chords = chord.get
    for c in chords:
        print(c.name)



    Debug.write("Progression Chords:")
    progression = Progresssions.Progression(scale_of_em, wStrings.Progressions.Three_Chord)
    chords = progression.get
    for chord in chords:
        notes = chord.get
        for note in notes:
            print(note.name)
        print("\n")



    StepMaker.proc_progression(progression)
    chords = progression.get
    for chord in chords:
        notes = chord.get
        for note in notes:
            print(note.step)
    GenerateMidi.proc_progression(progression)
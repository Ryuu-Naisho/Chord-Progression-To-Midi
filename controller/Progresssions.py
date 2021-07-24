'''
Input a key and progression type, i.e 12 bar blues progression.
Output Chords of that progression.
'''


import Debug
from model import wStrings
from controller import Chords
import random


class Progression:


    def __init__(self, scale, progression_type):
        '''
        Progressions will be noted in lowercase roman numerals. (Regardless of major or minor) that will depend on the scale that is inputed.
        '''
        self._progression_type = progression_type
        self._progression_structure = []
        self._progression = self._proc_progression(scale, progression_type)



    def _proc_chords(self, scale, progression_structer):
        '''Return chords of the progression.'''
        progression = [0] * len(progression_structer) 
        index = 0
        for numeral in progression_structer:
            chords = Chords.Chord(scale,scale[0], numeral)
            progression[index] = chords
            index += 1
        return progression





    def _proc_progression(self, scale, progression_type):
        '''Get progression type and randomly select an available one from wStrings.'''
        progression = []
        progression_structure = []
        random_index = 0
        if progression_type == wStrings.Progressions.Three_Chord:
            progression = wStrings.Three_Chord_Progression_Array
        elif progression_type == wStrings.Progressions.Blues:
            progression = wStrings.Blues_Progression_Array
        elif progression_type == wStrings.Progressions.Trap:
            progression = wStrings.Trap_Progression_Array
        random_index = random.randint(0,len(progression) - 1)
        progression_structure = progression[random_index]
        self._progression_structure = progression_structure
        progression = self._proc_chords(scale, progression_structure)
        return progression



    @property
    def progression_type(self):
        return self._progression_type



    @property
    def get(self):
        '''Return all the chords in the progression.'''
        return self._progression
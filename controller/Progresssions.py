'''
Input a key and progression type, i.e 12 bar blues progression.
Output Chords of that progression.
'''


from model import wStrings
import random


class Progression:


    def __init__(self, progression_type):
        '''
        Progressions will be noted in lowercase roman numerals. (Regardless of major or minor) that will depend on the scale that is inputed.
        '''
        self._i = 0
        self._ii = 0
        self._iii = 0
        self._iv = 0
        self._v = 0
        self._vi = 0
        self._vii = 0
        self._progression_type = progression_type
        self._progression_structure = []




    def _proc_progression(self, progression_type):
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
        random_index = random.randint(0,len(progression))
        progression_structure = progression[random_index]
        self._progression_structure = progression_structure



    @property
    def i(self):
        return self._i



    @property
    def ii(self):
        return self._ii



    @property
    def iii(self):
        return self._iii



    @property
    def iv(self):
        return self._iv



    @property
    def v(self):
        return self._v



    @property
    def vi(self):
        return self._vi



    @property
    def vii(self):
        return self._vii



    @property
    def progression_type(self):
        return self._progression_type
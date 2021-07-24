'''
Input a key and progression type, i.e 12 bar blues progression.
Output Chords of that progression.
'''


from model import wStrings


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



    def _proc_progression(self):
        '''Get progression type and randomly select an available one from wStrings.'''



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
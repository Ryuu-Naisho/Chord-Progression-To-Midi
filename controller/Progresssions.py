'''
Input a key and progression type, i.e 12 bar blues progression.
Output Chords of that progression.
'''


class Progression:


    def __init__(self):
        '''
        Progressions will be noted in lowercase roman numerals. (Regardless of major or minor) that will depend on the scale that is inputed.
        '''
        self.i = 0
        self.ii = 0
        self.iii = 0
        self.iv = 0
        self.v = 0
        self.vi = 0
        self.vii = 0
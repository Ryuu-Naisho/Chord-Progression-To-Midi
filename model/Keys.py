from model import wStrings
from controller import Notes


class Key:
    '''Return primitive keys i.e no sharps or flats.'''


    def __init__(self):
        '''Init all twelve keys.'''
        self._c = Notes.Note(0)
        self._d = Notes.Note(2)
        self._e = Notes.Note(4)
        self._f = Notes.Note(5)
        self._g = Notes.Note(7)
        self._a = Notes.Note(9)
        self._b = Notes.Note(11)


    @property
    def C(self):
        return self._c


    @property
    def D(self):
        return self._d


    @property
    def E(self):
        return self._e


    @property
    def F(self):
        return self._F



    @property
    def G(self):
        return self._g


    @property
    def A(self):
        return self._a


    @property
    def B(self):
        return self._b
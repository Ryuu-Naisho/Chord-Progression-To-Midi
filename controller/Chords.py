'''
    Get chords, input processed scale and no need to mention quality, 7s or aug or dim.
'''
import Debug
from controller import MusicMath
from model import wStrings


class Chord:
    def __init__(self, scale, root, numeral):
        self._scale = scale
        self._root = root
        self._numeral = numeral
        self._numeral_index = self._get_numeral_index()
        self._i = 0
        self._iii = 0
        self._v = 0
        self._vii = -1
        self._hasSeventh = False
        self._proc_triad()
        if wStrings._7 in numeral:
            self._proc_seventh()



    def _get_numeral_index(self):
        index = 0
        numeral = self._numeral
        if numeral == wStrings.Numeral.i:
            index = 0
        elif numeral == wStrings.Numeral.ii:
            index = 1
        elif numeral == wStrings.Numeral.iii:
            index = 2
        elif numeral == wStrings.Numeral.iv:
            index = 3
        elif numeral == wStrings.Numeral.v:
            index = 4
        elif numeral == wStrings.Numeral.vi:
            index = 5
        elif numeral == wStrings.Numeral.vii:
            index = 6
        return index



    def _get_root_index(self):
        index = self._scale.index(self._root)
        return index



    def _proc_triad(self):
        index = self._get_numeral_index()
        self._i = self._scale[index]
        index = MusicMath.process_pitch_scale(index + 2)
        self._iii = self._scale[index]
        index = MusicMath.process_pitch_scale(index + 2)
        self._v = self._scale[index]



    def _proc_seventh(self):
        index = self._numeral_index
        index = MusicMath.process_pitch_scale(index + 6)
        self._vii = self._scale[index]



    @property
    def get(self):
        root = self._i
        third = self._iii
        fifth = self._v
        size = 3
        if self._hasSeventh:
            seventh = self._vii
            size += 1
        chord = [0]*size
        chord[0] = root
        chord[1] = third
        chord[2] = fifth
        if self._hasSeventh:
            chord[3] = seventh
        return chord
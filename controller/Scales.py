'''
To be used as an object to hold notes of a scale. Also, to be used as non-processed scale for circle of fifths.
'''
from model import wStrings
from controller import Notes
from controller import CircleOfFifths
import Debug


class Scale:
    def __init__(self, key, quality):
        '''Params key of the scale. quality : Major or Minor. '''
        self._i = 0
        self._ii = 0
        self._iii = 0
        self._iv = 0
        self._v = 0
        self._vi = 0
        self._vii = 0
        self._scale = []

        self.scale_builder(key)
        unprocessedScale = self._getUnprocessedScale()
        self._proc_scale(unprocessedScale, quality)
    


    def scale_builder(self, key):
        '''Builds the scale regardless of major or minor. Starting with the root.'''
        root_value = key.pitch
        index_value = root_value
        increment_ammount = 2
        intervals = []
        self._i = key
        self._i.numeral = wStrings.i
        
        for index in range(7):
            #Since python midi uses whole numbers instead of semitone, need to increment by 1 at E or B
            #Else the reset increment by 2
            if index_value == 4 or index_value == 11:
                increment_ammount = 1
            else:
                increment_ammount = 2
            index_value += increment_ammount
            intervals.append(index_value)


        self._ii = Notes.Note(intervals[0])
        self._ii.numeral = wStrings.ii
        self._iii = Notes.Note(intervals[1])
        self._iii.numeral = wStrings.iii
        self._iv = Notes.Note(intervals[2])
        self._iv.numeral = wStrings.iv
        self._v = Notes.Note(intervals[3])
        self._v.numeral = wStrings.v
        self._vi = Notes.Note(intervals[4])
        self._vi.numeral = wStrings.vi
        self._vii = Notes.Note(intervals[5])
        self._vii.numeral = wStrings.vii


    def _proc_scale(self, scale, quality):
        C05 = CircleOfFifths.CircleOfFifth(scale, quality)
        self._scale = C05.get_scale()
        self._ii = self._scale[1]
        self._iii = self._scale[2]
        self._iv = self._scale[3]
        self._v = self._scale[4]
        self._vi = self._scale[5]
        self._vii = self._scale[6]



    def _getUnprocessedScale(self):
        intervals = []
        intervals.append(self._i)
        intervals.append(self._ii)
        intervals.append(self._iii)
        intervals.append(self._iv)
        intervals.append(self._v)
        intervals.append(self._vi)
        intervals.append(self._vii)
        return intervals



    @property
    def scale(self):
        return self._scale



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
from model import wStrings
from controller import MusicMath



class Note:
    '''Create note object. 
       param semitone of 7 notes (0=c, 1=c#, 2=d, 3=d#, 4=e, 5=f, 6=f#, 7=g, 8=g#, 9=a, 10=a#, 11=b)
       octave_range default is 0 c4 on a keyboard, only move by +-12
       step is the beat position in one bar.
       duration is the length of the note.'''



    def __init__(self, semitone =0, octave_range = 0, step = 1, duration = 1):
        self._pitch = semitone
        self._octave_range = 0 
        self._step = 0 
        self._duration = 0 
        self._volume = 0
        self._isSharp = False
        self._isFlat = False
        self._name = ''
        self._pitch = MusicMath.processPitch(self._pitch)
        self._setName()



    def _setName(self):
        self._name = wStrings.AllKeys[self._pitch]
    @property
    def pitch(self):
        return self._pitch + self._octave_range


    @property
    def octave_range(self):
        return self._octabe_range


    @property
    def step(self):
        return self._step


    @property
    def duration(self):
        return self._duration


    @property
    def volume(self):
        return self._volume


    @property
    def isSharp(self):
        return self._isSharp


    @property
    def isFlat(self):
        return self._isFlat


    @property
    def name(self):
        return self._name



    @octave_range.setter
    def octave_range(self, octave_range):
        self._octave_range = octave_range


    @step.setter
    def step(self, step):
        self._step = self


    @duration.setter
    def duration(self, duration):
        self._duration = duration


    @volume.setter
    def volume(self, volume):
        self._volume = volume


    @isSharp.setter
    def isSharp(self, sharp):
        if sharp:
            self._isSharp = True
            if self._isFlat:
                self._isFlat = False
            new_pitch = self._pitch + 1
            self._pitch = MusicMath.processPitch(new_pitch)
            self._setName()
        else:
            self.isFlat = True



    @isFlat.setter
    def isFlat(self, flat):
        if flat:
            self._isFlat = flat
            if self._isSharp:
                self._isSharp = False
            new_pitch = self._pitch - 1
            self._pitch = MusicMath.processPitch(new_pitch)
            self._setName()
        else:
            self.isSharp = True
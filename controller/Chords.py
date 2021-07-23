'''
Increment or deminish pitch to create a major, minor, or even major7, minor7 etc... chords.
Get chord as an object which can be grouped in a list for progressions.


Example usage:
keys = Keys.Key()
    key = keys.C
    key.isSharp = True
    print(key.name)
    chord = Chords.Chord(key, wStrings.MINOR7)
    chords = chord.getAllNotes
    for c in chords:
        print(c.name)
    output:

C#/Db
E
G#/Ab
C

'''
from model import wStrings
from controller import Notes

class Chord:
    def __init__(self, key, chord_type):
        self._root = key
        self._root_pitch = key.pitch
        self._third = 0
        self._fifth = 0
        self._seventh = -1

        if chord_type == wStrings.MAJOR:
            self.major()
        elif chord_type == wStrings.MAJOR7:
            self.major7()
        elif chord_type == wStrings.MINOR:
            self.minor()
        elif chord_type == wStrings.MINOR7:
            self.minor7()


            
    def major(self):
        index = self._root_pitch + 4
        self._third = Notes.Note(index)

        index = self._root_pitch + 7
        self._fifth = Notes.Note(index)


    def minor(self):
        index = self._root_pitch + 3
        self._third = Notes.Note(index)

        index = self._root_pitch + 7
        self._fifth = Notes.Note(index)


    def major7(self):
        self.major()
        index = self._root_pitch + 11
        self._seventh = Notes.Note(index)


    def minor7(self):
        self.minor()
        index = self._root_pitch + 11
        self._seventh = Notes.Note(index)


    @property
    def root(self):
        return self._root


    @property
    def third(self):
        return self._third


    @property
    def fifth(self):
        return self._fifth


    @property
    def seventh(self):
        return self._seventh


    @property
    def getAllNotes(self):
        if self._seventh != -1:
            return {self.root, self.third, self.fifth, self.seventh}
        else:
            return {self.root, self.third, self.fifth}
'''
Calculate #s and b's of a scale uing these algorythms for major and minor.
Major and minor:

if n <= 6:
    n + 4 = next_note + 1#
    # = n + 10
elif n > 6:
    n - 4 = next_note + #
    # = n + 4

originally was 11 and 5 but I used note.isSharp to set harp. 11 and 5 would fall on the sharp and no need to make sharp. So I made it 11,4 so I can use note.isSharp
'''
import Debug
from model import wStrings
from controller import Notes
from controller import MusicMath



class CircleOfFifth:
    def __init__(self, scale, quality):
        self._scale = scale
        self._quality = quality
        self._proc_scale()



    def _get_circle_index(self, pitch, circle):
        '''Reutrn index of either side of the cirlce of fifths.'''
        index = 0
        for key, value in circle.items():
            if value == pitch:
                index = key
        return index


    def _get_circle(self):
        circle = {}
        if self._quality == wStrings.MAJOR:
            circle = wStrings.MajorCircleOfFifthPitch
        elif self._quality == wStrings.MINOR:
            circle = wStrings.MinorCircleOfFifthPitch
        return circle



    def _proc_sharps(self, key_index, clockwise):
        '''Rotate through the circle and append the notes that will be sharp.'''
        circle = 0
        for index in range(1, key_index + 1):
            if clockwise:
                circle = wStrings.MajorCircleOfFifthPitch
                sharp_index = MusicMath.processPitch(circle[index] + 10)
            else:
                circle = wStrings.MinorCircleOfFifthPitch
                sharp_index = MusicMath.processPitch(circle[index] + 4)

            for note in self._scale:
                if note.pitch == sharp_index:
                    note.isSharp = True



    def _find_key_position_in_cirlce(self, key, circle):
        '''Return the position in the circle of fifth
        Params key (root note) 
        Params quality (major or minor scale etc..)'''
        index = self._get_circle_index(key.pitch, circle)
        return index



    def _proc_scale(self):
        major_scale = []
        circle = self._get_circle()
        key_index = self._find_key_position_in_cirlce(self._scale[0], circle)
        clockwise = False
        if key_index <= 6:
            clockwise = True
        else:
            clockwise = False
        self._proc_sharps(key_index, clockwise)



    def get_scale(self):
        return self._scale
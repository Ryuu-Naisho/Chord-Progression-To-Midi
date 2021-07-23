TITLE = "Chord Progressions"
INTRO = "Welcome, specify a key, tempo and genre. To generate a chord progression."
MAJOR = "Major"
MINOR = "Minor"
MAJOR7 = "Major7"
MINOR7 = "Minor7"
AllKeys = {0:'C', 1:'C#/Db', 2:'D', 3: 'D#/Eb', 4:'E', 5:'F', 6:'F#/Gb', 7:'G', 8:'G#/Ab', 9:'A', 10:'A#/Bb', 11:'B'}
#CircleOfFifths
#key is the place on the circle of fifth clockwise for major and minor
#i.e 0 is first place on C on the circle of fifth
#Value is the coressponding pitch from AllKeys
#i.e AllKeys[0] = 'C'
#CircleOfFifthNumSharps works both counter and clockwise with minor and major. Position and number of sharps never changes, just the value of the pitch.
MajorCircleOfFifthPitch = {0:0, 1:7, 2:2, 3:9, 4:4, 5:11, 6:6, 7:1, 8:8, 9:3, 10:10, 11:5}
MinorCircleOfFifthPitch = {0:9, 1:4, 2:11, 3:6, 4:1, 5:8, 6:3, 7:10, 8:5, 9:0, 10:7, 11:2}
CircleOfFifthNumSharps = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:5, 8:4, 9:3, 10:2, 11:1}

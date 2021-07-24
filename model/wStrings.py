def enum(**enums):
    return type('Enum', (), enums)



TITLE = "Chord Progressions"
INTRO = "Welcome, specify a key, tempo and genre. To generate a chord progression."
MAJOR = "Major"
MINOR = "Minor"
MAJOR7 = "Major7"
MINOR7 = "Minor7"
_7 = '7'
AllKeys = {0:'C', 1:'C#/Db', 2:'D', 3: 'D#/Eb', 4:'E', 5:'F', 6:'F#/Gb', 7:'G', 8:'G#/Ab', 9:'A', 10:'A#/Bb', 11:'B'}
#Roman numeral strings
Numeral = enum(
i = 'i',
ii = 'ii',
iii = 'iii',
iv = 'iv',
v = 'v',
vi = 'vi',
vii = 'vii',
i7 = 'i7',
ii7 = 'ii7',
iii7 = 'iii7',
iv7 = 'iv7',
v7 = 'v7',
vi7 = 'vi7',
vii7 = 'vii7')
#CircleOfFifths
#key is the place on the circle of fifth clockwise for major and minor
#i.e 0 is first place on C on the circle of fifth
#Value is the coressponding pitch from AllKeys
#i.e AllKeys[0] = 'C'
#CircleOfFifthNumSharps works both counter and clockwise with minor and major. Position and number of sharps never changes, just the value of the pitch.
MajorCircleOfFifthPitch = {0:0, 1:7, 2:2, 3:9, 4:4, 5:11, 6:6, 7:1, 8:8, 9:3, 10:10, 11:5}
MinorCircleOfFifthPitch = {0:9, 1:4, 2:11, 3:6, 4:1, 5:8, 6:3, 7:10, 8:5, 9:0, 10:7, 11:2}
CircleOfFifthNumSharps = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:5, 8:4, 9:3, 10:2, 11:1}
#Progression types
Progressions = enum(Three_Chord = 'Three_Chord_Progression', Blues = 'Blues_Progression', Trap = 'Trap_Progression')
Three_Chord_Progression_Array = [
    ['i','iv','v','v'],
    ['i','i','iv','v'],
    ['i','iv','i','v'],
    ['i','iv','v','iv'],
    ['i','iv','v','i']
]
Blues_Progression_Array = [
    ['i','i','i','i','iv','iv','i','i','v','iv','i','i'],
    ['i7','iv7', 'v7'],
    ['i7','iv7','i7','iv7','i7','vi','ii','v','i7','ii','v']
]
Trap_Progression_Array = [
    ['i','v','vi','iv'],
    ['i','ii','vi'],
    ['iv','v','vi','i'],
    ['i','iii','ii','v'],
    ['i','ii','vi'],
    ['i','vii','v','i'],
    ['v','vi','v','vi'],
    ['i','vii','v'],
    ['i','v','i','v'],
    ['vi','iv','vi','iv'],
    ['i','ii','v','vii'],
    ['iv','v','iii','vii'],
    ['vi','v','vi','v'],
    ['iv','i','iii','ii'],
    ['i','vii','iv','v'],
    ['i','v','iv','vii'],
    ['i','vii','i','vii'],
    ['vi','vii','vi','vii'],
    ['v','vii','v','vii'],
    ['i','vi','v','vi'],
    ['vii','vi','v','vi'],
    ['i','vii','v','i','iii','vi'],
    ['i','vi','iii','vii','i'],
    ['i','v','i','ii'],
    ['iii','i','iii','ii'],
    ['i','vii','vi'],
    ['i','v','iii','ii'],
    ['i','vii','iii'],
    ['i','vii','vii','i'],
    ['i','iii','vii','i'],
    ['i','ii','vii','i'],
    ['i','ii','iii','iv'],
    ['i','v','vi','vii'],
    ['v','vi','v','vii']
]
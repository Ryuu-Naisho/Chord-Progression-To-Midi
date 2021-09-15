from midiutil.MidiFile import MIDIFile
import Debug



track = 0
midi_file = MIDIFile(1)
starting_step = 0
tempo = 120
midi_file.addTrackName(track, starting_step, 'Chordprogressions')
midi_file.addTempo(track, starting_step, tempo)


channel = 0
volume = 100



def write():
    '''Write the midi file.'''
    with open('ChordProgression.mid', 'wb') as outfile:
        midi_file.writeFile(outfile)
    Debug.write('Midi file created.')



def proc_progression(progression):
    '''Add the notes of the progression to the midi-file.'''
    bar = 0
    step = 0
    duration = 0
    pitch = 0
    octave = 60 #C4


    chords = progression.get
    for chord in chords:
        notes = chord.get
        for note in notes:
            step = note.step + bar
            duration = note.duration
            pitch = note.pitch + octave
            midi_file.addNote(track, channel, pitch, step, duration, volume)
        bar += 1
    

    write()
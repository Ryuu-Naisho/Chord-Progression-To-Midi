from model import wStrings
from model import wExceptions
import random
import Debug



def get_step():
    '''Return random step.'''
    steps = wStrings.Steps
    size = len(steps) - 1
    random_index = random.randint(0,size)
    step = steps[random_index]
    return step



def get_durration(step):
    '''Get the durration of a note.
    Param step: Note starts on what beat.'''
    available_durrations = []


    if step == 0:
        available_durrations = wStrings.Seed.First_Beat
    elif step == 1:
        available_durrations = wStrings.Seed.Second_Beat
    elif step == 2:
        available_durrations = wStrings.Seed.Third_Beat
    elif step == 3:
        available_durrations = wStrings.Seed.Fourth_Beat
    else:
        raise(wExceptions.Invalid_Step)



    size = len(available_durrations) - 1
    random_index = random.randint(0, size)
    durration = available_durrations[random_index]
    return durration



def proc_progression(progression):
    '''Generate step and durration for each note in the progression.
    No need to return'''
    chords = progression.get
    for chord in chords:
        notes = chord.get
        for note in notes:
            step = get_step()
            duration = get_durration(step)
            note.step = step
            note.duration = duration
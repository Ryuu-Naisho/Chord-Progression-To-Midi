def processPitch(newPitch):
    index = newPitch
    pitch = 0
    if index >= 12:
        index -= 12
    pitch = index
    return pitch



def process_pitch_scale(new_pitch):
    index = new_pitch
    pitch = 0
    if index >= 8:
        index -=8
    pitch = index
    return pitch
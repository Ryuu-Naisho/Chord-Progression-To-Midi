def processPitch(newPitch):
    index = newPitch
    pitch = 0
    if index >= 12:
        index -= 12
    pitch = index
    return pitch
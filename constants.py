BASE_QUALITIES = {
    "maj": (0, 4, 7),
    "min": (0, 3, 7),
    "dim": (0, 3, 6),
    "aug": (0, 4, 8),
}

# the major and minor scales have the same qualities
MAIN_JAZZ_QUALITY_TO_INTEGERS = {
    "maj7": (0, 4, 7, 11),
    "min7": (0, 3, 7, 10),
    "maj6": (0, 4, 7, 9),
    "min6": (0, 3, 7, 9),
    "dom7": (0, 4, 7, 10),
    "half-dim7": (0, 3, 6, 10),
    "dim": (0, 3, 6, 9),
    "minmaj7": (0, 3, 7, 11),
}

MAIN_JAZZ_INTEGERS_TO_QUALITY = {v : k for k, v in MAIN_JAZZ_QUALITY_TO_INTEGERS.items()}

MAIN_JAZZ_ALTERATIONS = {
    "b9": (1,),
    "9": (2,),
    "#9": (3,),
    "#5": (8,),
    "#11": (6,),
    "4": (5,),
    "13" : (9),
}

OTHER_QUALITIES = {
    "aug7": (0, 4, 8, 10),
}


QUALITY_ALTERATIONS = {
    "b9": (1,),
    "9": (2,),
    "#9": (3,),
    "#5": (8,),
    "#11": (6,),
    "sus4": (5,),
    "sus2": (2,),
}

NOTE_NUMBER_TO_STANDARD_NAME = [
    "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"
]

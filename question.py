import random
from typing import  Tuple

import constants


class Question:
    """
    A question is a minimal amount of information to ask the user for input
    """
    def __init__(self, chord_root: int, key_root: int, intervals: Tuple[int]):
        self.chord_root = chord_root
        self.chord_root_name = constants.NOTE_NUMBER_TO_STANDARD_NAME[chord_root]

        self.key_root = key_root
        self.key_root_name = constants.NOTE_NUMBER_TO_STANDARD_NAME[key_root]

        self.intervals = intervals
        self.intervals_quality_name = constants.MAIN_JAZZ_INTEGERS_TO_QUALITY[intervals]

    def __repr__(self):
        return str(self.__dict__)

def generate_random_intervals() -> Tuple[int]:
    """
    generates a set of intervals and it's name (aka chord)
    """

    intervals_name = random.choice(list(constants.MAIN_JAZZ_QUALITY_TO_INTEGERS.keys()))
    intervals = constants.MAIN_JAZZ_QUALITY_TO_INTEGERS[intervals_name]

    return intervals


def create_question(key_root: int = -1) -> Question:
    """
    Creates and returns a question, optionally you can specify a key root, otherwise
    a random key root is used

    """

    if key_root == -1:
        key_root = random.randint(0, 11)

    chord_root = random.randint(0, 11)
    intervals = generate_random_intervals()

    return Question(chord_root,  key_root,  intervals)


def randomize_sharp_or_flat(standard_note: str) -> str:
    """
    Given a string which is a note in standard notation

    Eg) C#/Db

    this function will randomly choose one of the notes and return it.

    If the note doesn't have a slash in it, it returns the note that was passed in
    :return:
    """
    if "/" in standard_note:
        notes = standard_note.split("/")
        return random.choice(notes)
    else:
        return standard_note


def number_to_note(note_number: int) -> str:
    """
    Given a number which represents a note, convert it to standard notation
    while randomizing if it uses a sharp or flat.
    :param note_number:
    :return:
    """
    return randomize_sharp_or_flat(constants.NOTE_NUMBER_TO_STANDARD_NAME[note_number])


def display_question(question: Question):
    print(f"Key Root: {randomize_sharp_or_flat(question.key_root_name)}, Chord: {randomize_sharp_or_flat(question.chord_root_name) + ' ' + question.intervals_quality_name}")


def display_question_no_key(question: Question):
    print(f"Chord: {randomize_sharp_or_flat(question.chord_root_name) + ' ' + question.intervals_quality_name}")

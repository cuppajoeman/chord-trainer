import random
from dataclasses import dataclass
from typing import List, Tuple

import constants


@dataclass
class Question:
    """
    A question is a minimal amount of information to ask the user for input
    """
    chord_root: int
    chord_root_name: str

    key_root: int
    key_root_name: str

    intervals: Tuple[int]
    intervals_quality_name: str


def generate_note_and_name() -> Tuple[int, str]:
    """
    Generate a note represented by a number and it's standard name
    """
    note = random.randint(0, 11)
    return note, constants.NOTE_NUMBER_TO_STANDARD_NAME[note]


def generate_intervals_and_name() -> Tuple[Tuple[int], str]:
    """
    generates a set of intervals and it's name (aka chord)
    """

    intervals_name = random.choice(list(constants.MAJOR_MINOR_DIATONIC_QUALITIES.keys()))
    intervals = constants.MAJOR_MINOR_DIATONIC_QUALITIES[intervals_name]

    return intervals, intervals_name


def create_question(key_root: int = -1):
    """
    Creates and returns a question, optionally you can specify a key root

    """

    if key_root == -1:
        key_root, key_root_name = generate_note_and_name()
    else:
        key_root_name = constants.NOTE_NUMBER_TO_STANDARD_NAME[key_root]
    

    chord_root, chord_root_name = generate_note_and_name()
    intervals, intervals_name = generate_intervals_and_name()

    return Question(chord_root, chord_root_name, key_root, key_root_name, intervals, intervals_name)


def randomize_sharp_or_flat(standard_note: str):
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

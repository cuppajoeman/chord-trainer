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


def create_question():
    """
    Creates and returns a question
    """

    chord_root, chord_root_name = generate_note_and_name()
    key_root, key_root_name = generate_note_and_name()
    intervals, intervals_name = generate_intervals_and_name()

    return Question(chord_root, chord_root_name, key_root, key_root_name, intervals, intervals_name)


def randomize_standard_note(standard_note: str):
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


def display_question(question: Question):
    print(f"Key Root: {randomize_standard_note(question.key_root_name)}, Chord: {randomize_standard_note(question.chord_root_name) + question.intervals_quality_name}")


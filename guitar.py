from dataclasses import dataclass
import random

import question

@dataclass
class GuitarQuestion(question.Question):
    fret_pos: int
    start_side: str


def create_question():
    """
    Creates and returns a question
    """

    chord_root, chord_root_name = question.generate_note_and_name()
    key_root, key_root_name = question.generate_note_and_name()
    intervals, intervals_name = question.generate_intervals_and_name()

    fret_pos = random.randint(0, 24)
    start_side = ["thin", "thick"][random.choice([0,1])]

    return GuitarQuestion(chord_root, chord_root_name, key_root, key_root_name, intervals, intervals_name, fret_pos, start_side)


def display_question(guitar_question: GuitarQuestion, supress_chord: bool):

    if supress_chord:
        display_str = ""
    else:
        display_str = f"""
        Key Root: {question.randomize_standard_note(guitar_question.key_root_name)} 
        Chord: {question.randomize_standard_note(guitar_question.chord_root_name) + guitar_question.intervals_quality_name}
        """

    display_str += f"""
    Fret Position: {guitar_question.fret_pos}
    Starting Side: {guitar_question.start_side}
    """

    print(display_str)



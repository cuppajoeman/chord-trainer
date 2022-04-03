from dataclasses import dataclass
import random
from typing import Tuple

import question


class GuitarQuestion(question.Question):
    def __init__(self, chord_root: int, key_root: int, intervals: Tuple[int]):
        super().__init__(chord_root, key_root, intervals)
        self.anchor_string = random.randint(0, 5)
        self.anchor_interval = random.choice(self.intervals)


def question_to_guitar_question(q : question.Question) -> GuitarQuestion:
    return GuitarQuestion(q.chord_root, q.key_root, q.intervals)


def create_question(key_root: int = -1) -> GuitarQuestion:
    """
    Creates and returns a question, optionally you can specify a key root, otherwise
    a random key root is used

    """

    if key_root == -1:
        key_root = random.randint(0, 11)

    chord_root = random.randint(0, 11)
    intervals = question.generate_random_intervals()

    return GuitarQuestion(chord_root,  key_root,  intervals)


def display_question(guitar_question: GuitarQuestion):

    display_str = f"""
    Chord: {question.randomize_sharp_or_flat(guitar_question.chord_root_name) + ' ' + guitar_question.intervals_quality_name}
    Anchor String: {guitar_question.anchor_string}
    Anchor Interval: {guitar_question.anchor_interval}
    """

    print(display_str)



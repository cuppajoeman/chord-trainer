from typing import List
import random

import constants
from question import Question


def create_jazz_question_set(key_root: int, alteration_frequency: float = 0.1) -> List[Question]:
    question_set = []
    for chord_root in range(12):
        for integer_quality in constants.MAIN_JAZZ_QUALITY_TO_INTEGERS.values():
            # if random.random() < alteration_frequency:
            question_set.append(Question(chord_root, key_root, integer_quality))
    random.shuffle(question_set)

    return question_set

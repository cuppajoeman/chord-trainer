from dataclasses import dataclass
from typing import List


@dataclass
class Answer:
    key_intervals: List[int]


def get_answer() -> Answer:
    """
    Prop
    :return:
    """
    while True:
        response = input("Answer: ")
        try:
            key_intervals = [int(x) for x in response.split()]
            break
        except ValueError:
            print("Your answer does not follow the format, try again")

    return Answer(key_intervals)

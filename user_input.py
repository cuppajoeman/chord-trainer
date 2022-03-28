import time
from typing import Tuple

from pytimedinput import timedInput

from answer import Answer
from question import Question
from verification import verify


def get_answer_until_correct_or_out_of_time(q: Question, time_to_solve: float) -> None:
    """
    Asks the user the question until they've gotten it right.
    """
    question_correct = False

    started_at = time.time()

    iteration = 0

    while not question_correct:
        if iteration != 0:
            print("Try again")

        time_spent = time.time() - started_at
        time_remaining = time_to_solve - time_spent

        if time_remaining < 0:
            return # out of time

        answer, ran_out_of_time = get_answer_with_time_limit(time_remaining)

        if not ran_out_of_time:
            question_correct = verify(q, answer)
            print(f"question_correct : {question_correct}")
            iteration += 1
        else:
            print("You ran out of time!")
            return

    print("correct")


def get_answer_with_time_limit(time_to_answer: float) -> Tuple[Answer, bool]:
    response, ran_out_of_time = timedInput("Answer: ", timeout=time_to_answer)
    try:
        key_intervals = [int(x) for x in response.split()]
    except ValueError:
        print("Your answer does not follow the format")

    return Answer(key_intervals), ran_out_of_time


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

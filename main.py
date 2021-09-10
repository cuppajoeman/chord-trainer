import answer
import question
import guitar
from verification import verify

import argparse

parser = argparse.ArgumentParser(description='Train chords mentally or on guitar')
parser.add_argument("-g", "--guitar", help="guitar mode, gives user questions, new questions are given when return is pressed", action="store_true")
args = parser.parse_args()

guitar_mode = args.guitar

running = True


def normal_mode_iteration():
    """
    Asks the user a question and only moves until the next until they have given the correct response
    :return:
    """
    q = question.create_question()

    question.display_question(q)

    a = answer.get_answer()

    while not verify(q, a):
        print("try again")
        a = answer.get_answer()

    print("correct")


def guitar_mode_iteration():
    """
    Asks the user a question and waits until they respond with any key
    :return:
    """
    gq = guitar.create_question()

    guitar.display_question(gq)

    input("type any key to continue")


if guitar_mode:
    iteration = guitar_mode_iteration
else:
    iteration = normal_mode_iteration


while running:
    iteration()

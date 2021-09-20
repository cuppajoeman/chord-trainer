import answer
import question
import guitar
import time
import random
from verification import verify

import argparse

parser = argparse.ArgumentParser(description='Train chords mentally or on guitar')
parser.add_argument("-g", "--guitar", help="guitar mode: gives user questions, new questions are given when return is pressed", action="store_true")
parser.add_argument("-s", "--suppress", help="in guitar mode this suppresses chord generation", action="store_true")
parser.add_argument(
    "-c",
    "--continuous",
    help="a variant where new question is shown after n seconds and doesn't check for an answer",
    type=int,
)
args = parser.parse_args()

guitar_mode = args.guitar

running = True


def continuous_mode_iteration(key_root):
    q = question.create_question(key_root)
    question.display_question(q)

    wait_time = args.continuous

    time.sleep(wait_time)


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

    guitar.display_question(gq, args.suppress)

    input("type any key to continue")

iteration_args = []

if guitar_mode:
    iteration = guitar_mode_iteration
elif args.continuous:
    rand_key = random.randint(0, 11)
    iteration_args.append(rand_key)
    iteration = continuous_mode_iteration
else:
    iteration = normal_mode_iteration


while running:
    iteration(*iteration_args)

import answer
import question
import guitar
import random

import question_sets
from verification import verify
import user_input

import argparse

parser = argparse.ArgumentParser(description='Train chords mentally or on guitar')
parser.add_argument("-g", "--guitar", help="guitar mode: gives user questions, new questions are given when return is pressed", action="store_true")
parser.add_argument("-s", "--suppress", help="in guitar mode this suppresses chord generation", action="store_true")
parser.add_argument(
    "-c",
    "--continuous",
    help="a variant where new question is shown after n seconds",
    type=int,
)

parser.add_argument(
    "-j",
    "--jazz-set",
    help="continuous mode over a jazz question set",
    type=int,
)

args = parser.parse_args()

guitar_mode = args.guitar

running = True

def question_set_iteration(q: question.Question, time_to_answer: int):
    question.display_question_no_key(q)

    user_input.get_answer_until_correct_or_out_of_time(q, time_to_answer)


def continuous_mode_iteration(key_root: int, time_to_answer: int):
    q = question.create_question(key_root)

    question.display_question_no_key(q)

    user_input.get_answer_until_correct_or_out_of_time(q, time_to_answer)


def normal_mode_iteration():
    """
    Asks the user a question and only moves until the next until they have given the correct response
    :return:
    """
    q = question.create_question()

    question.display_question(q)

    a = user_input.get_answer()

    while not verify(q, a):
        print("try again")
        a = user_input.get_answer()

    print("correct")


def guitar_mode_iteration():
    """
    Asks the user a question and waits until they respond with any key
    :return:
    """
    gq = guitar.create_question()

    guitar.display_question(gq, args.suppress)

    input("type any key to continue")


def yes_or_no(question: str) -> bool:
    reply = str(input(question + ' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    elif reply[0] == 'n':
        return False
    else:
        return yes_or_no("Please Enter (y/n) ")


iteration_args = []

if guitar_mode:
    iteration = guitar_mode_iteration
elif args.continuous:
    rand_key = random.randint(0, 11)
    iteration_args.append(rand_key)
    time_to_solve = args.continuous
    iteration_args.append(time_to_solve)
    iteration = continuous_mode_iteration

    if not yes_or_no(f"Your key is {question.number_to_note(rand_key)}, are you ready to go?"):
        quit()
elif args.jazz_set:
    rand_key = random.randint(0, 11)
    time_to_solve = args.jazz_set
    iteration_args.append(time_to_solve)

    if not yes_or_no(f"Your key is {question.number_to_note(rand_key)}, are you ready to go?"):
        quit()

else:
    iteration = normal_mode_iteration

if args.jazz_set:
    idx = 0
    question_set = question_sets.create_jazz_question_set(rand_key)
    while idx < len(question_set) and running:
        question_set_iteration(question_set[idx], time_to_solve)
        idx += 1

    if idx == len(question_set):
        print("training complete!")

else:
    while running:
        iteration(*iteration_args)

from answer import get_answer
from question import create_question, display_question
from verification import verify

running = True
while running:
    question = create_question()

    display_question(question)

    answer = get_answer()

    while not verify(question, answer):
        print("try again")
        answer = get_answer()

    print("correct")

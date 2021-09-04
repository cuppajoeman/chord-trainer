from answer import Answer
from question import Question


def verify(question: Question, answer: Answer):
    """
    verifies to see if the user has given the same set of key intervals as the question requires
    :param question:
    :param answer:
    :return:
    """
    true_key_intervals = []
    for interval in question.intervals:
        # adding 12 to keep it positive
        chord_root_key_interval = ((question.chord_root - question.key_root) + 12) % 12
        true_key_intervals.append((interval + chord_root_key_interval) % 12)

    return set(true_key_intervals) == set(answer.key_intervals)





import random

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 99


def is_even(question):
    return question % 2 == 0


def main(max_number):
    question = random.randint(1, max_number)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer

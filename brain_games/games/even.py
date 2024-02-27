import random

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 99


def main(max_number):
    question = random.randint(1, max_number)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer

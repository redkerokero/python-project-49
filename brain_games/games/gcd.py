import random
from math import gcd

GAME_TASK = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 99


def gen_question_answer(max_number):
    first_number = random.randint(1, max_number)
    second_number = random.randint(1, max_number)
    question = f'{first_number} {second_number}'
    answer = str(gcd(first_number, second_number))
    return question, answer

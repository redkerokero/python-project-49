import random

GAME_TASK = 'Find the greatest common divisor of given numbers.'
AMOUNT_OF_ROUNDS = 3
MAX_NUMBER = 99


def main(max_number):
    first_number = random.randint(1, max_number)
    second_number = random.randint(1, max_number)
    question = f'{first_number} {second_number}'
    if first_number < second_number:
        first_number, second_number = second_number, first_number
    remainder = first_number % second_number
    while remainder > 0:
        first_number = second_number
        second_number = remainder
        remainder = first_number % second_number
    answer = str(second_number)
    return (question, answer)

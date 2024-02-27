import random
from math import sqrt, trunc

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 99


def is_prime(number):
    if number <= 1:
        return False
    search_limit = trunc(sqrt(number))
    for remainder in range(2, search_limit + 1):
        if number % remainder == 0:
            return False
    return True


def main(max_number):
    question = random.randint(1, max_number)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer

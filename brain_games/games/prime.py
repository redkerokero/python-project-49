import random
from math import trunc, sqrt


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
AMOUNT_OF_ROUNDS = 3
MAX_NUMBER = 99


def is_prime(number):
    if number <= 1:
        return False
    search_limit = trunc(sqrt(number))
    for remainder in range(2, search_limit + 1):
        if number % remainder == 0:
            return False
    return True


def run_prime_game(max_number):
    question = random.randint(1, max_number)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)

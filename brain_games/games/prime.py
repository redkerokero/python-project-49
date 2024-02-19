import random
from math import trunc, sqrt
from brain_games import engine


def is_prime(number):
    if number <= 1:
        return False
    search_limit = trunc(sqrt(number))
    for remainder in range(2, search_limit + 1):
        if number % remainder == 0:
            return False
    return True


def run_prime_game():
    game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    amount_of_rounds = 3
    max_number = 99
    game_data = []
    for _ in range(amount_of_rounds):
        question = random.randint(1, max_number)
        if is_prime(question):
            answer = 'yes'
        else:
            answer = 'no'
        game_data.append((question, answer))
    engine.main(game_task, game_data)

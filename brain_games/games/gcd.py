import random
from brain_games import engine


def run_gcd_game():
    game_task = 'Find the greatest common divisor of given numbers.'
    amount_of_rounds = 3
    max_number = 99
    game_data = []
    for _ in range(amount_of_rounds):
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
        game_data.append((question, answer))
    engine.main(game_task, game_data)

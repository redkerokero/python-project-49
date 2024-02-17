import random
from brain_games import engine


def is_even(number):
    return number % 2 == 0


def even_game():
    game_description = (
        'Answer "yes" if the number is even, ',
        'otherwise answer "no".',
    )
    amount_of_rounds = 3
    max_number = 99
    game_data = []
    for _ in range(amount_of_rounds):
        question = random.randint(1, max_number)
        if is_even(question):
            answer = 'yes'
        else:
            answer = 'no'
        game_data.append((question, answer))
    engine.main(game_description, game_data)

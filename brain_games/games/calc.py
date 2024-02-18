import random
from brain_games import engine


def run_calc_game():
    game_task = 'What is the result of the expression?'
    amount_of_rounds = 3
    max_number = 99
    game_data = []
    for _ in range(amount_of_rounds):
        first_number = random.randint(1, max_number)
        second_number = random.randint(1, max_number)
        operation = random.choice(['+', '-', '*'])
        match operation:
            case '+':
                question = f'{first_number} + {second_number}'
                answer = str(first_number + second_number)
            case '-':
                question = f'{first_number} - {second_number}'
                answer = str(first_number - second_number)
            case '*':
                question = f'{first_number} * {second_number}'
                answer = str(first_number * second_number)
        game_data.append((question, answer))
    engine.main(game_task, game_data)

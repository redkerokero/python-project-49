import random

GAME_TASK = 'What is the result of the expression?'
AMOUNT_OF_ROUNDS = 3
MAX_NUMBER = 99


def main(max_number):
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
    return (question, answer)

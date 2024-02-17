import random


def is_even(number):
    return number % 2 == 0


def even_game():
    max_number = 99
    question = random.randint(1, max_number)
    if is_even(question):
        return (question, 'yes')
    return (question, 'no')


game_description = 'Answer "yes" if the number is even, otherwise answer "no".'

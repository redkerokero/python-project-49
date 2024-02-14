import prompt
import random


def is_even(number):
    return number % 2 == 0


def main():
    rounds_number = 3
    max_number = 99
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for game_round in range(rounds_number):
        question = random.randint(1, max_number)
        if is_even(question):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was",
                f"'{correct_answer}'.\nLet's try again, {name}!",
            )
            break
        if game_round == rounds_number - 1:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

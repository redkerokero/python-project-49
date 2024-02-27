import prompt

AMOUNT_OF_ROUNDS = 3


def greetings():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    return name


def main(game):
    name = greetings()
    print(game.GAME_TASK)
    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = game.main(game.MAX_NUMBER)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was",
                f"'{correct_answer}'.\nLet's try again, {name}!",
            )
            return
    print(f'Congratulations, {name}!')

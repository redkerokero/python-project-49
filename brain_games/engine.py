import prompt

AMOUNT_OF_ROUNDS = 3


def main(game):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_TASK)
    for game_round in range(AMOUNT_OF_ROUNDS):
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
            break
        if game_round == AMOUNT_OF_ROUNDS - 1:
            print(f'Congratulations, {name}!')

import prompt


def main(game_task, amount_of_rounds, max_number, game):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print(game_task)
    for game_round in range(amount_of_rounds):
        question, correct_answer = game(max_number)
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
        if game_round == amount_of_rounds - 1:
            print(f'Congratulations, {name}!')

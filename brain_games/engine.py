import prompt


def main(game_description, game_data):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print(game_description)
    for game_round, round_data in enumerate(game_data):
        question, correct_answer = round_data
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
        if game_round == len(game_data) - 1:
            print(f'Congratulations, {name}!')

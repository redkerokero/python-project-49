import prompt


def main(description, question, correct_answer):
    rounds_number = 3
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print(description)
    for game_round in range(rounds_number):
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

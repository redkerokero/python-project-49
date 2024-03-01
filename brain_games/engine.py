import prompt

AMOUNT_OF_ROUNDS = 3


def greetings():
    username = prompt.string(
        'Welcome to the Brain Games!\nMay I have your name? ',
    )
    print(f'Hello, {username}!')
    return username


def main(game):
    username = greetings()
    print(game.GAME_TASK)
    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = game.gen_question_answer(game.MAX_NUMBER)
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was",
                f"'{correct_answer}'.\nLet's try again, {username}!",
            )
            return
    print(f'Congratulations, {username}!')

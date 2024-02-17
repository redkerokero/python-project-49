#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import even


def main():
    description = even.game_description
    question, correct_answer = even.even_game()
    #print(description)
    #print(question)
    #print(correct_answer)
    engine.main(description, question, correct_answer)


if __name__ == '__main__':
    main()

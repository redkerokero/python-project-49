#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import even


def main():
    game_task = even.GAME_TASK
    amount_of_rounds = even.AMOUNT_OF_ROUNDS
    max_number = even.MAX_NUMBER
    game = even.run_even_game
    engine.main(game_task, amount_of_rounds, max_number, game)


if __name__ == '__main__':
    main()

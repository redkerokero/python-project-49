#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import calc


def main():
    game_task = calc.GAME_TASK
    amount_of_rounds = calc.AMOUNT_OF_ROUNDS
    max_number = calc.MAX_NUMBER
    game = calc.run_calc_game
    engine.main(game_task, amount_of_rounds, max_number, game)


if __name__ == '__main__':
    main()

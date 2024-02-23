#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import gcd


def main():
    game_task = gcd.GAME_TASK
    amount_of_rounds = gcd.AMOUNT_OF_ROUNDS
    max_number = gcd.MAX_NUMBER
    game = gcd.run_gcd_game
    engine.main(game_task, amount_of_rounds, max_number, game)


if __name__ == '__main__':
    main()

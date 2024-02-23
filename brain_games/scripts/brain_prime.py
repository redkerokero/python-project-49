#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import prime


def main():
    game_task = prime.GAME_TASK
    amount_of_rounds = prime.AMOUNT_OF_ROUNDS
    max_number = prime.MAX_NUMBER
    game = prime.run_prime_game
    engine.main(game_task, amount_of_rounds, max_number, game)


if __name__ == '__main__':
    main()

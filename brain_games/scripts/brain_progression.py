#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import progression


def main():
    game_task = progression.GAME_TASK
    amount_of_rounds = progression.AMOUNT_OF_ROUNDS
    max_number = progression.MAX_NUMBER
    game = progression.run_progression_game
    engine.main(game_task, amount_of_rounds, max_number, game)


if __name__ == '__main__':
    main()

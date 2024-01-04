#!/usr/bin/env python3
from brain_games.scripts.brain_games import greeting
from brain_games.games.prime import PRE_QUESTION, solution
import brain_games.engine


def main():
    user_name = greeting()
    brain_games.engine.game(PRE_QUESTION, solution, user_name)


if __name__ == '__main__':
    main()

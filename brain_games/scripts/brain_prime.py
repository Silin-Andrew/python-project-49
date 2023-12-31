#!/usr/bin/env python3
from random import randint
from brain_games.scripts.brain_gcd import get_multipliers
from brain_games.scripts.brain_games import main as greeting
import brain_games.engine

PRE_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def solution():
    min_number = 1
    max_number = 100
    number = randint(min_number, max_number)
    question = f'Question: {number}'
    multipliers = get_multipliers(number)
    if len(multipliers) == 1:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def main():
    user_name = greeting()
    brain_games.engine.game(PRE_QUESTION, solution, user_name)


if __name__ == '__main__':
    main()

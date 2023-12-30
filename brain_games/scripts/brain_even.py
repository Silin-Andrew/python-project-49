#!/usr/bin/env python3
from random import randint
from brain_games.scripts.brain_games import main as greeting
import brain_games.engine

PRE_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def solution():
    number = randint(1, 20)
    question = f'Question: {number}'
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def main():
    user_name = greeting()
    brain_games.engine.game(PRE_QUESTION, solution, user_name)


if __name__ == '__main__':
    main()

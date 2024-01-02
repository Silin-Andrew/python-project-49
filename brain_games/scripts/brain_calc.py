#!/usr/bin/env python3
from random import randint, choice
from brain_games.scripts.brain_games import greeting
import brain_games.engine

PRE_QUESTION = 'What is the result of the expression?'


def solution():
    MIN_NUMBER = 2
    operation = choice(['-', '+', '*'])
    if operation == "*":
        MAX_NUMBER = 10
    else:
        MAX_NUMBER = 50
    a = randint(MIN_NUMBER, MAX_NUMBER)
    b = randint(MIN_NUMBER, MAX_NUMBER)
    operation = f'{str(a)} {operation} {str(b)}'
    question = f'Question: {operation}'
    correct_answer = str(eval(operation))
    return question, correct_answer


def main():
    user_name = greeting()
    brain_games.engine.game(PRE_QUESTION, solution, user_name)


if __name__ == '__main__':
    main()

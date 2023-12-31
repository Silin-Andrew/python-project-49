#!/usr/bin/env python3
from random import randint, choice
from brain_games.scripts.brain_games import main as greeting
import brain_games.engine

PRE_QUESTION = 'What is the result of the expression?'


def solution():
    min_number = 2
    operation = choice(['-', '+', '*'])
    if operation == "*":
        max_number = 10
    else:
        max_number = 50
    a = randint(min_number, max_number)
    b = randint(min_number, max_number)
    operation = f'{str(a)} {operation} {str(b)}'
    question = f'Question: {operation}'
    correct_answer = str(eval(operation))
    return question, correct_answer


def main():
    user_name = greeting()
    brain_games.engine.game(PRE_QUESTION, solution, user_name)


if __name__ == '__main__':
    main()

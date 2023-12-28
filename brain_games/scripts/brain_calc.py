#!/usr/bin/env python3
from random import randint, choice
from brain_games.scripts.brain_games import main as greeting
import brain_games.engine 

PRE_QUESTION = 'What is the result of the expression?'


def solution():
    operation = choice(['-', '+', '*'])
    if operation == "*":
        end_of_range = 10
    else:
        end_of_range = 50
    a = randint(2, end_of_range)
    b = randint(2, end_of_range)
    operation = f'{str(a)} {operation} {str(b)}'
    question = f'Question: {operation}'
    correct_answer = str(eval(operation))
    return question, correct_answer   


def main():
    user_name = greeting()
    brain_games.engine.game(PRE_QUESTION, solution, user_name)


if __name__ == '__main__':
    main()        

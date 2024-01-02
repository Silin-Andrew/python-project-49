#!/usr/bin/env python3
from random import randint
from brain_games.scripts.brain_games import greeting
import brain_games.engine

PRE_QUESTION = 'What number is missing in the progression?'


def solution():
    MIN_START = 1
    MAX_START = 15
    start = randint(MIN_START, MAX_START)
    MIN_STEP = 2
    MAX_STEP = 9
    step = randint(MIN_STEP, MAX_STEP)
    PROGRESSION_LENGHT = 10
    progression = [start,]
    index = 1
    while index <= PROGRESSION_LENGHT - 1:
        start += step
        progression.append(start)
        index += 1
    hidden_index = randint(0, PROGRESSION_LENGHT - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = 'Question: '
    for element in progression:
        question += str(element) + ' '
    return question, correct_answer


def main():
    user_name = greeting()
    brain_games.engine.game(PRE_QUESTION, solution, user_name)


if __name__ == '__main__':
    main()

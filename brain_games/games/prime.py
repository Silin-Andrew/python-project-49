from random import randint
from brain_games.games.gcd import get_multipliers

PRE_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def solution():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'Question: {number}'
    multipliers = get_multipliers(number)
    if len(multipliers) == 1:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

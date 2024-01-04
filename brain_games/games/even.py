from random import randint

PRE_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def solution():
    MIN_NUMBER = 1
    MAX_NUMBER = 20
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'Question: {number}'
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

from random import randint

PRE_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def is_even(number):
    return number % 2 == 0


def solution():
    number = get_number()
    question = f'Question: {number}'
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

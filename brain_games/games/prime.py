from random import randint

PRE_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def is_prime(number):
    max_multiplier = int(number ** (1 / 2))
    multiplier = 2
    while multiplier <= max_multiplier:
        if number % multiplier == 0:
            return False
        else:
            multiplier += 1
    return True


def get_question_and_correct_answer():
    number = get_number()
    question = number
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

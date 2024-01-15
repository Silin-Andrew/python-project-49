from random import randint

PRE_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def get_multipliers(number):
    multipliers = []
    max_multiplier = int(number ** (1 / 2))
    multiplier = 2
    while multiplier <= max_multiplier:
        if number % multiplier == 0:
            multipliers.append(multiplier)
            number = number / multiplier
        else:
            multiplier += 1
    if number != 1:
        multipliers.append(int(number))
    return multipliers


def is_prime(number):
    return len(get_multipliers(number)) == 1


def solution():
    number = get_number()
    question = number
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

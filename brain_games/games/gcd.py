from random import randint

PRE_QUESTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 2
MAX_NUMBER = 50


def get_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def get_gcd_euclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def get_question_and_correct_answer():
    num1 = get_number()
    num2 = get_number()
    question = f'{num1} {num2}'
    correct_answer = str(get_gcd_euclid(num1, num2))
    return question, correct_answer

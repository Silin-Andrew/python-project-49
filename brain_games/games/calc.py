from random import randint, choice

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

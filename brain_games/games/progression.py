from random import randint

PRE_QUESTION = 'What number is missing in the progression?'
MIN_START = 1
MAX_START = 15
MIN_STEP = 2
MAX_STEP = 9
PROGRESSION_LENGTH = 10


def get_parameters():
    start = randint(MIN_START, MAX_START)
    step = randint(MIN_STEP, MAX_STEP)
    return start, step


def get_progression(start, step, length):
    progression = [start,]
    index = 1
    while index <= length - 1:
        start += step
        progression.append(start)
        index += 1
    return progression


def get_correct_answer(progression):
    hidden_index = randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    return correct_answer, hidden_index


def get_question(progression, hidden_index):
    progression[hidden_index] = '..'
    question = ''
    for element in progression:
        question += str(element) + ' '
    return question


def solution():
    start, step = get_parameters()
    progression = get_progression(start, step, PROGRESSION_LENGTH)
    correct_answer, hidden_index = get_correct_answer(progression)
    question = get_question(progression, hidden_index)
    return question, correct_answer

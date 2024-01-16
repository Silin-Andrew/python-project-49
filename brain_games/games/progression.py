from random import randint

PRE_QUESTION = 'What number is missing in the progression?'
MIN_INITIAL_TERM = 1
MAX_INITIAL_TERM = 15
MIN_COMMON_DIFFERENCE = 2
MAX_COMMON_DIFFERENCE = 9
PROGRESSION_LENGTH = 10


def get_progression(initial_term, common_difference, length):
    progression = [initial_term]
    index = 1
    while index <= length - 1:
        initial_term += common_difference
        progression.append(initial_term)
        index += 1
    return progression


def get_question(progression, hidden_index):
    progression[hidden_index] = '..'
    question = ''
    for element in progression:
        question += str(element) + ' '
    return question


def get_question_and_correct_answer():
    initial_term = randint(MIN_INITIAL_TERM, MAX_INITIAL_TERM)
    common_difference = randint(MIN_COMMON_DIFFERENCE, MAX_COMMON_DIFFERENCE)
    progression = get_progression(initial_term, common_difference, PROGRESSION_LENGTH)
    hidden_index = randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[hidden_index])
    question = get_question(progression, hidden_index)
    return question, correct_answer

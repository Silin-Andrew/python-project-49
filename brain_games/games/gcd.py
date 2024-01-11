from random import randint

PRE_QUESTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 2
MAX_NUMBER = 50


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


def compare_lists(list1, list2):
    if len(list1) > len(list2):
        short_list, long_list = list2, list1
    else:
        short_list, long_list = list1, list2
    return short_list, long_list


def get_intersection(short_list, long_list):
    intersection = []
    for item in short_list:
        if item in long_list:
            intersection.append(item)
            long_list.remove(item)
    return intersection


def get_gcd(intersection):
    gcd = 1
    for item in intersection:
        gcd *= item
    return gcd


def solution():
    num1 = get_number()
    num2 = get_number()
    question = f'Question: {num1} {num2}'
    list1 = get_multipliers(num1)
    list2 = get_multipliers(num2)
    short_list, long_list = compare_lists(list1, list2)
    intersection = get_intersection(short_list, long_list)
    correct_answer = str(get_gcd(intersection))
    return question, correct_answer

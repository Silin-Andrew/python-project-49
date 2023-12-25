#!/usr/bin/env python3
from random import randint
from brain_games.scripts.brain_games import main as greeting
from prompt import string

def iseven():
    number = randint(1, 20)
    print(f'Question: {number}')
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_counter = 0
    while correct_counter < 3:
        correct_answer = iseven()
        users_answer = string('Your answer: ')
        if users_answer == correct_answer:
            print('Correct!')
            correct_counter += 1
        else:
            print(f"'{users_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


def main():
    name = greeting()
    game(name)


if __name__ == '__main__':
    main()

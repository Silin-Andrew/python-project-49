#!/usr/bin/env python3
from random import randint
from brain_games.scripts.brain_games import main as greeting


def even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: ', end='')
    correct_counter = 0
    while correct_counter < 3:
        number = randint(1, 20)
        print(number)
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        # print(f'Correct answer {correct_answer}')
        users_answer = input('Your answer: ')
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
    even(name)


if __name__ == '__main__':
    main()

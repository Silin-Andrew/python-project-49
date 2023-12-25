#!/usr/bin/env python3
from random import randint, choice
from brain_games.scripts.brain_games import main as greeting
from prompt import string


def calculating():
    operation = choice(['-', '+', '*'])
    if operation == "*":
        end_of_range = 10
    else:
        end_of_range = 50
    a = randint(2, end_of_range)
    b = randint(2, end_of_range)
    question = str(a) + ' ' + operation + ' ' + str(b)
    print(f'Question: {question}')
    correct_answer = str(eval(question))
    return correct_answer 


def game(name):
    print('What is the result of the expression?')
    correct_counter = 0
    while correct_counter < 3:
        correct_answer = calculating()
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

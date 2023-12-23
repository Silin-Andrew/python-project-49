#!/usr/bin/env python3
from random import randint, choice
from brain_games.scripts.brain_games import main as greeting
import prompt


def calc(name):
    operations = ['-', '+', '*']
    easy_interval =10
    hard_interval = 50
    print('What is the result of the expression?')
    correct_counter = 0
    while correct_counter < 3:
        operation = choice(operations)
        if operation == "*":
            end = easy_interval
        else:
            end = hard_interval
        a = randint(1, end)
        b = randint(1, end)
        question = str(a) + ' ' + operation + ' ' + str(b)
        print(f'Question: {question}')
        correct_answer = str(eval(question))
        users_answer = prompt.string('Your answer: ')
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
    calc(name)


if __name__ == '__main__':
    main()        

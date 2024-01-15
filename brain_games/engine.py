from prompt import string
from brain_games.scripts.brain_games import greeting

NUMBER_OF_ROUNDS = 3


def run(game):
    user_name = greeting()
    print(game.PRE_QUESTION)
    correct_counter = 0
    while correct_counter < NUMBER_OF_ROUNDS:
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        users_answer = string('Your answer: ')
        if users_answer == correct_answer:
            print('Correct!')
            correct_counter += 1
        else:
            print(f"'{users_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')

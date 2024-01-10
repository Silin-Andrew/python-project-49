from prompt import string
from brain_games.scripts.brain_games import greeting


user_name = greeting()
def game(PRE_QUESTION, solution):
    print(PRE_QUESTION)
    correct_counter = 0
    while correct_counter < 3:
        question, correct_answer = solution()
        print(question)
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

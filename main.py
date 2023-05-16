from random import randint
# TODO: Include an ASCII art logo.
# print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# def random_number():
#     '''A function that chooses random number 1-100'''
#     return randint(1, 100)

# answer = random_number()
answer = randint(1, 100)
print(f"Pssst, the correct answer is {answer}")

# TODO: Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
easy = 10
hard = 5

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = print(f"You have {difficulty} attempts remaining to guess the number")

# TODO: Allow the player to submit a guess for a number between 1 and 100.
guess = int(input("Make a guess: "))

# TODO: Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def check_guess():
    if guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")

# TODO: If they got the answer correct, show the actual answer to the player.
# print(f"You got it! The answer was {answer}")

# TODO: Track the number of turns remaining.

# TODO: If they run out of turns, provide feedback to the player. 
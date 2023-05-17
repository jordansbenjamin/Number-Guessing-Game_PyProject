from random import randint
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'easy':
        return easy
    else:
        return hard

def check_guess():
    if guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")
    else:
        print(f"You got it! The answer was {answer}")

answer = randint(1, 100)
easy = 10
hard = 5
attempts = difficulty()
print(f"Pssst, the correct answer is {answer}")

while True:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    check_guess()
    
    if guess != answer:
        print("Guess again.")
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            break
        continue
    else:
        break
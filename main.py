from random import randint

# print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def difficulty():
    attempts = 0
    if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'easy':
        attempts = easy
    else:
        attempts = hard
    return attempts

def check_guess():
    if guess < answer:
        attempts -= 1
        print("Too low.")
    elif guess > answer:
        attempts -= 1
        print("Too high.")
    else:
        print(f"You got it! The answer was {answer}")

answer = randint(1, 100)
print(f"Pssst, the correct answer is {answer}")

easy = 10
hard = 5
attempts = difficulty()

while True:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    check_guess()

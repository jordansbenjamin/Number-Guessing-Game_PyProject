from random import randint

# print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# def random_number():
#     '''A function that chooses random number 1-100'''
#     return randint(1, 100)

# answer = random_number()
answer = randint(1, 100)
print(f"Pssst, the correct answer is {answer}")

easy = 10
hard = 5
attempts = 0

def difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'easy':
        attempts = easy
    else:
        attempts = hard
    return attempts

attempts = difficulty()

print(f"You have {attempts} attempts remaining to guess the number.")


# guess = int(input("Make a guess: "))


def check_guess():
    if guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")
    # else:
        # print(f"You got it! The answer was {answer}")


import random

print("Welcome to the Number Guessing Game (1-10)!")
secret_number = random.randint(1, 10)
user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess == secret_number:
    print("Congratulations! You guessed it right.")
else:
    print(f"Wrong guess! The number was {secret_number}.")

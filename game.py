import random

number = random.randint(1, 100)
attempts = 0

print("=== Number Guessing Game ===")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        print("Total Attempts:", attempts)
        break

    elif guess < number:
        print("Too Low! Try Again.")

    else:
        print("Too High! Try Again.")

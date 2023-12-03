# Shehryar Khan

import random

def guess_the_number():
    print("Welcome to Guess the Number Game!")

    while True:
        secret_number = random.randint(1, 100)
        attempts = 5

        print("\nGuess a number between 1 and 100.")

        for attempt in range(attempts):
            guess = input(f"\nAttempt {attempt + 1}/{attempts}: Enter your guess (or 'q' to quit): ")

            if guess.lower() == 'q':
                print(f"\nThe secret number was {secret_number}. You quit the game.")
                break

            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")
                continue

            if guess == secret_number:
                print(f"\nCongratulations! You guessed the correct number {secret_number} in {attempt + 1} attempts. You win!")
                break
            elif guess < secret_number:
                print("The secret number is greater than your guess. Try again.")
            else:
                print("The secret number is lesser than your guess. Try again.")

        else:
            print(f"\nSorry, you've run out of attempts. The secret number was {secret_number}. You lose.")

        retry = input("Do you want to play again? (y/n): ")
        if retry.lower() != 'y':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    guess_the_number()

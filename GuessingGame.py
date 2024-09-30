import random

def number_guessing_game():
    """A number guessing game where the user tries to guess a random number.

    Returns:
        The number of attempts it took the user to guess the number correctly.
    """

    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = input("Guess a number between 1 and 100: ")
            if guess.isdigit():
                guess = int(guess)
                break
            else:
                print("Invalid input. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        attempts += 1

        if guess == random_number:
            print("Congratulations!   You guessed the number in", attempts, "attempts.") 

            break
        elif guess.isdigit() and int(guess) < random_number: 
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == '__main__': 
    number_guessing_game()
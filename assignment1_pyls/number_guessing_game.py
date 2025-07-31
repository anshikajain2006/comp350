import random

def generate_secret_number() -> int:
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

def run_guessing_loop(secret: int) -> None:
    """Repeatedly ask the user to guess until correct. Give feedback each time."""
    attempts = 0
    while True:
        guess = get_user_guess()
        attempts += 1
        if is_correct_guess(guess, secret):
            print(f"Correct! You got it in {attempts} attempts!")
            break
        give_feedback_on_guess(guess, secret)

def get_user_guess() -> int:
    """Ask the user for a guess and validate it."""
    while True:
        try:
            user_input = input("Enter your guess between 1–100: ")
            guess = int(user_input)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Your guess must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def is_correct_guess(guess: int, secret: int) -> bool:
    """Check if the guess is correct."""
    return guess == secret

def give_feedback_on_guess(guess: int, secret: int) -> None:
    """Inform the user whether their guess is too low or too high."""
    if guess < secret:
        print("Too low.")
    else:
        print("Too high.")

def play_guessing_game() -> None:
    """Play the game."""
    secret_number = generate_secret_number()
    run_guessing_loop(secret_number)

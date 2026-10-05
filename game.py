import random

MIN, MAX = 1, 100


def read_guess(prompt):
    while True:
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print()  # odřádkování po Ctrl+D / Ctrl+C
            return None

        try:
            guess = int(raw)
        except ValueError:
            print("That is not a whole number, try again")
            continue

        if not (MIN <= guess <= MAX):
            print(f"Please enter a whole number between {MIN} and {MAX}")
            continue

        return guess


def play_round():
    secret = random.randint(MIN, MAX)
    attempts = 0
    print(f"\nI picked a number between {MIN} and {MAX}.")

    while True:
        guess = read_guess("Your turn: ")
        if guess is None:
            return None

        attempts += 1
        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too big!")
        else:
            print("Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            return attempts


def main():
    while True:
        if play_round() is None:          # ukončeno během hádání
            break

        try:
            again = input("Do you want to play again? (yes/no): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            again = "no"

        if again not in ("yes", "y"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

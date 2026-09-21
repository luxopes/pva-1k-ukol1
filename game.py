import random as r

secret_number = r.randint(1, 100)

invalid_attempts = 0

while True:

    user_input = input("Your guess: ")

    try:
        guess = int(user_input.strip())

    except ValueError:

        invalid_attempts += 1

        if invalid_attempts >= 5:
            print("Too many invalid inputs, ending.")
            break

        print("That is not a whole number, try again.")
        continue

    invalid_attempts = 0

    if secret_number < guess:
        print("Too big!")

    elif secret_number > guess:
        print("Too small!")

    else:
        print("Correct!")
        break

print(f"Correct number was {secret_number}")

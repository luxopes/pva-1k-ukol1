import random as r

a = r.randint(1, 100)

spatne = 0

while True:

    text = input("Your guess: ")

    try:
        b = int(text.strip())

    except ValueError:

        spatne += 1

        if spatne >= 5:
            print("Too many invalid inputs, ending.")
            break

        print("That is not a whole number, try again.")
        continue

    spatne = 0

    if a < b:
        print("Too big!")

    elif a > b:
        print("Too small!")

    else:
        print("Correct!")
        break

print(f"Correct number was {a}")

import random as r

while True:
    secret = r.randint(1, 100)
    attempts = 0
    
    print("\nI picked a number between 1 and 100.")
    
    while True:
        user_input = input("Your turn: ")
        
        try:
            guess = int(user_input)
            
            if guess < 1 or guess > 100:
                print("Please enter a whole number between 1 and 100")
                continue
            
        except ValueError:
            print("That is not a whole number, try again")
            continue
            
        attempts += 1
        
        if secret > guess:
            print("Too small!")
            
        elif secret < guess:
            print("Too big!")
            
        else:
            print("Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break
            
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        
    if play_again not in ("yes", "y"):
        print("Thanks for playing!")
        break
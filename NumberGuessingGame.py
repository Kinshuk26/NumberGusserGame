import random

def play_game():                       # Defining a function here!
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess it!\n")

    number = random.randint(1, 100)    # Computer choosing a random number!
    attempts = 0

    while True:                        # Starting a while loop!
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
        else:
            print("Correct! You guessed it in", attempts, "attempts.")
            break

while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ")  # Confirming if the player wants to play again! If yes then reruning the loop else breaking the loop!
    if again.lower() != "yes":
        print("Thanks for playing!")
        break

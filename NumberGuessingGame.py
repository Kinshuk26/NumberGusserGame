import random

def game():                    # Definign a function here
    print("Welcome to the Number Guessing Game!")
    print("You have to guess a number between 1 and 100!")
    print("All the best! \n")

    number = random.randint(1, 100)  # Computer choosing a random number!
    attempts = 0

    while True:                    # Using a while loop!
        guess = int(input("Enter your number: "))
        attempts += 1

        if guess < number:
           print ("Too Low!")
        elif guess > number:
            print ("Too high!")
        else:
            print ("Correct! You have guessed the number in", attempts , "attemps.")  # Ending the loop once the number is guessed. Shows the number of attempts in the final answer!
            break

while True:
    game()
    again = input ("Do you want to play the game again? (Yes/No): ") # Confirming if the player wants to play again!
    if again.lower() != "yes":
        print ("Thanks for playing!")
        break

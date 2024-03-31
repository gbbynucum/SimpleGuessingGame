import random

def play_game():
    # Generate a random number between 1 and 10
    hidden_number = random.randint(1, 10)

    # Number of chances the user gets
    chances = 3

    # Iterate through the chances
    for attempt in range(chances, 0, -1):
        guess = int(input(f"You have {attempt} {'chance' if attempt == 1 else 'chances'} left. Guess the number between 1 and 10: "))

        # Check if the guess matches the hidden number
        if guess == hidden_number:
            print("Congratulations! You guessed the correct number!")
            return  # Exit the function if the guess is correct
        else:
            if guess < hidden_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")

    # If the loop completes without a correct guess
    print(f"Sorry, you've run out of chances. The correct number was {hidden_number}.")

# Main loop to allow the user to play again
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing!")
        break

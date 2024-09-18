import random

def play_game():
    answer = random.randint(1, 100)
    guesses = 0

    print("\nPython Number Guessing Game")
    print("Guess the number between 1 and 100. Type 'q' to quit.")

    while True:
        guess = input('Enter your guess: ')

        if guess.lower() == 'q':
            print("You chose to quit. Goodbye!")
            break

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < 1 or guess > 100:
                print("The number is out of range. Please select a number between 1 and 100.")
            elif guess < answer:
                print('Too low, try again.')
            elif guess > answer:
                print('Too high, try again.')
            else:
                print(f'Correct! The answer was {answer}.')
                print(f'Number of guesses: {guesses}')
                break
        else:
            print("Invalid input. Please enter a valid number between 1 and 100, or 'q' to quit.")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

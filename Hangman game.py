import random

words = ('javascript', 'python', 'java', 'rust', 'php')
answer = random.choice(words)
wrong_guess = 0
correct_guesses = []
max_attempts = 6

hangman = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\"),
}

def hangman_display(attempts):
    print('***************')
    for line in hangman[attempts]:
        print(line)
    print('***************')

def words_display(answer, correct_guesses):
    display = ''.join(letter if letter in correct_guesses else '_' for letter in answer)
    print(display)

while wrong_guess < max_attempts:
    hangman_display(wrong_guess)
    words_display(answer, correct_guesses)
    
    guess = input('\nEnter a letter: ').lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue
    
    if guess in correct_guesses:
        print("You've already guessed that letter!")
        continue

    if guess in answer:
        correct_guesses.append(guess)
        if all(letter in correct_guesses for letter in answer):
            print(f"Congratulations! You've guessed the word: {answer}")
            break
    else:
        wrong_guess += 1
        print(f"Wrong guess! You have {max_attempts - wrong_guess} attempts left.")

if wrong_guess == max_attempts:
    hangman_display(wrong_guess)
    print(f"Game over! The word was: {answer}")

import random
import string

# Define characters and create a shuffled key
characters = string.punctuation + string.digits + string.ascii_letters + " "
characters = list(characters)
key = characters.copy()
random.shuffle(key)

def encrypt():
    plain_txt = input('Enter a message to encrypt: ').strip()

    if not plain_txt:
        print("Error: Empty input! Please enter a valid message.")
        return

    encrypted_msg = ""
    for letter in plain_txt:
        if letter in characters:
            index = characters.index(letter)
            encrypted_msg += key[index]
        else:
            print(f"Warning: '{letter}' is not a valid character, skipping.")
            encrypted_msg += letter

    print(f'Original Message : {plain_txt}')
    print(f'Encrypted Message: {encrypted_msg}')

def decrypt():
    encrypted_msg = input('Enter a message to decrypt: ').strip()

    if not encrypted_msg:
        print("Error: Empty input! Please enter a valid message.")
        return

    decrypted_msg = ""
    for letter in encrypted_msg:
        if letter in key:
            index = key.index(letter)
            decrypted_msg += characters[index]
        else:
            print(f"Warning: '{letter}' is not a valid character, skipping.")
            decrypted_msg += letter

    print(f'Encrypted Message: {encrypted_msg}')
    print(f'Decrypted Message: {decrypted_msg}')

# Main loop
while True:
    user_option = input("\nWhat would you like to do? (E)ncrypt, (D)ecrypt, or (Q)uit: ").strip().lower()

    if user_option == 'e':
        encrypt()
    elif user_option == 'd':
        decrypt()
    elif user_option == 'q':
        print("Finished")
        break
    else:
        print("Invalid option. Please enter 'E', 'D', or 'Q'.")

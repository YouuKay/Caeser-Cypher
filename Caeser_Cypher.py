def caesar(text, shift, encrypt=True):
    # Ensure that the shift offset is a valid integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Restrict shift range to standard single-alphabet shifts (1 to 25)
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Reference alphabet to shift against
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # If decrypting, reverse the shift direction
    if not encrypt:
        shift = -shift

    # Create the shifted version of the alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Map both lowercase and uppercase letters to their shifted counterparts
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

    # Translate the entire string using the mapping table
    return text.translate(translation_table)

def encrypt(text, shift):
    """Encrypts a text string with a given integer shift."""
    return caesar(text, shift)

def decrypt(text, shift):
    """Decrypts a text string with a given integer shift."""
    return caesar(text, shift, encrypt=False)

user_text = input("Enter the message: ")
user_shift = int(input("Enter shift key (1-25): "))

# Keep prompting the user until they provide a valid mode ('E' or 'D')
while True:
    mode = input("Type 'E' to encrypt or 'D' to decrypt: ").strip().upper()

    if mode == 'E':
        print("Result:", encrypt(user_text, user_shift))
        break # Exit the loop after successful encryption
    elif mode == 'D':
        print("Result:", decrypt(user_text, user_shift))
        break # Exit the loop after successful decryption
    else:
        print("Invalid mode! Please enter 'E' for encryption or 'D' for decryption.\nLet's try again.\n")

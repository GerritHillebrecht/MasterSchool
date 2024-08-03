from string import ascii_lowercase, ascii_uppercase


def encrypt_char(char: str, key: int) -> str:
    """
    Encrypts a given char by the given key.
    :param char: Char to encrypt.
    :param key: The size of the shift the char shall make.
    :return: The shifted char.
    """
    # select ascii_charset according to the given char.
    char_set = ascii_lowercase if char.islower() else ascii_uppercase

    # if char is a-z or A-Z, encrypt based on selected char_set.
    if char.islower() or char.isupper():
        return encrypt_char_type(char, key, char_set)

    # Return the char if it's not a letter.
    return char


def encrypt_char_type(char: str, key: int, char_set: str) -> str:
    """
    Encrypts a given character depending on the given char_set and key.
    :param char: The char to encrypt.
    :param key: The key to encrypt the char by.
    :param char_set: lower or upper ascii set.
    :return: The encrypted char.
    """
    # ensure too large keys still work.
    encryption_key = key % len(char_set)
    encrypted_char_dec = ord(char) + encryption_key

    # Check if encrypted_char_dec is within set-range.
    if ord(char_set[0]) <= encrypted_char_dec <= ord(char_set[-1]):
        return chr(encrypted_char_dec)

    # If it's above subtract the char_set-range
    if encrypted_char_dec > ord(char_set[-1]):
        return chr(encrypted_char_dec - len(char_set))

    # Else add the char_set-range
    return chr(encrypted_char_dec + len(char_set))


def encrypt_caesar(text: str, key: int) -> str:
    """
    Encrypts a given text by the given key.
    :param text: The text to encrypt.
    :param key: The key to encrypt by.
    :return: The encrypted text.
    """
    return "".join([encrypt_char(char, key) for char in text])


def decrypt_caesar(ciphertext: str, key: int) -> str:
    """
    Decrypts a text by using the encryption function
    with the reversed key.
    :param ciphertext: The encrypted text.
    :param key: The key used to encrypt the text.
    :return: The decrypted text.
    """
    return encrypt_caesar(ciphertext, -key)


dispatcher = {
    "encrypt": encrypt_caesar,
    "decrypt": decrypt_caesar
}


def prompt_method():
    """
    Prompts the user whether he wants to decrypt or encrypt.
    :return: The validated selected method.
    """
    while True:
        selected_method = input(f'Do you want to {"/".join(dispatcher)}? ')
        if selected_method in dispatcher:
            return selected_method
        print(f'Please select {" or ".join(dispatcher)}')


def main() -> None:
    """
    Starts a never ending encryption / decryption loop.
    Lets the user choose the text and the key for the
    encryption or decryption.
    """
    while True:
        method = prompt_method()
        text_to_encrypt = input(f'The string to {method}: ')
        encryption_key = int(input("The encryption key (as int): "))
        print(dispatcher[method](text_to_encrypt, encryption_key))


if __name__ == "__main__":
    main()

class Vigenere:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def encrypt(plaintext, key):
        plaintext = plaintext.lower()
        plaintext = plaintext.strip()
        # hitung len
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        encrypted_string = ""
        keys = key
        # pencocokan key dan plaintext
        if len(plaintext) != len(key):
            if len(plaintext) > len(key):
                total = len(plaintext) - len(key)
                for i in range((total)):
                    keys += key
                keys = keys[: len(plaintext)]
            elif len(plaintext) < len(key):
                keys = key[: len(plaintext)]
            else:
                keys = key

        p_to_index = []
        k_to_index = []
        for character in plaintext:
            p_to_index.append(ord(character) - 97)
        for character in keys:
            k_to_index.append(ord(character) - 97)

        # encrypt
        # print(p_to_index)
        # print(k_to_index)
        for char in range(len(keys)):
            # print(((p_to_index[char] + k_to_index[char]) % 25))
            if plaintext[char] not in alphabet:
                encrypted_string += plaintext[char]
            else:
                encrypted_string += alphabet[
                    ((p_to_index[char] + k_to_index[char]) % 26)
                ]
        return encrypted_string.upper()

    def decrypt(plaintext, key):
        plaintext = plaintext.lower()
        plaintext = plaintext.strip()
        # hitung len
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        encrypted_string = ""
        keys = ""
        if len(plaintext) != len(key):
            if len(plaintext) > len(key):
                total = len(plaintext) - len(key)
                for i in range((total % len(key)) + 4):
                    keys += key
                keys = keys[: len(plaintext)]
            elif len(plaintext) < len(key):
                keys = key[: len(plaintext)]
            else:
                keys = key
        p_to_index = []
        k_to_index = []
        for character in plaintext:
            p_to_index.append(ord(character) - 97)
        for character in keys:
            k_to_index.append(ord(character) - 97)

        # encrypt
        # print(p_to_index)
        # print(k_to_index)
        for char in range(len(keys)):
            # print(((p_to_index[char] + k_to_index[char]) % 25))
            if plaintext[char] not in alphabet:
                encrypted_string += plaintext[char]
            else:
                encrypted_string += alphabet[
                    ((p_to_index[char] - k_to_index[char]) % 26)
                ]
        return encrypted_string.lower()

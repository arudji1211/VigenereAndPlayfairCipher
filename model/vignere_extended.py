class Vignere_extended:
    def encrypt_data(key, data):
        extended = key
        while len(extended) < len(data):
            extended += key
        key = extended[: len(data)]
        encrypted_data = bytearray()
        for i in range(len(data)):
            char = data[i]
            shift = ord(key[i % len(key)])
            encrypted_char = char ^ shift
            encrypted_data.append(encrypted_char)
        return encrypted_data

    def decrypt_data(key, data):
        extended = key
        while len(extended) < len(data):
            extended += key
        key = extended[: len(data)]
        decrypted_data = bytearray()
        for i in range(len(data)):
            char = data[i]
            shift = ord(key[i % len(key)])
            encrypted_char = char ^ shift
            decrypted_data.append(encrypted_char)
        return decrypted_data

def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def encrypt(message, key):
    encrypted_text = []
    key = generate_key(message, key)
    for i in range(len(message)):
        if message[i].isalpha():
            shift = ord(key[i].upper()) - 65
            if message[i].isupper():
                encrypted_text.append(chr((ord(message[i]) + shift - 65) % 26 + 65))
            else:
                encrypted_text.append(chr((ord(message[i]) + shift - 97) % 26 + 97))
        else:
            encrypted_text.append(message[i])
    return ''.join(encrypted_text)

def decrypt(encrypted_message, key):
    decrypted_text = []
    key = generate_key(encrypted_message, key)
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():
            shift = ord(key[i].upper()) - 65
            if encrypted_message[i].isupper():
                decrypted_text.append(chr((ord(encrypted_message[i]) - shift - 65) % 26 + 65))
            else:
                decrypted_text.append(chr((ord(encrypted_message[i]) - shift - 97) % 26 + 97))
        else:
            decrypted_text.append(encrypted_message[i])
    return ''.join(decrypted_text)

def main():
    print("Name: Ankur Suman")
    print("Registration No.: 21BDS0097")
    key = input("Enter the key: ").upper()
    message = input("Enter the message for encryption: ").upper()

    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print("\nString:", message)
    print("Encrypted message: Cipher Text =", encrypted_message)
    print("Decrypted message: Plain Text =", decrypted_message)

if __name__ == "__main__":
    main()
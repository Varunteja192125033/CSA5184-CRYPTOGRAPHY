def rsa_encrypt(plaintext, e, n):
    ciphertext = []
    for char in plaintext:
        encrypted_char = pow(ord(char), e, n)
        ciphertext.append(encrypted_char)
    return ciphertext

def rsa_decrypt(ciphertext, d, n):
    plaintext = []
    for encrypted_char in ciphertext:
        decrypted_char = chr(pow(encrypted_char, d, n))
        plaintext.append(decrypted_char)
    return ''.join(plaintext)

def main():
    n = 2537  # Modulus
    e = 17    # Public exponent
    d = 2753  # Private exponent

    message = "HELLO"
    print("Original Message:", message)

    ciphertext = rsa_encrypt(message, e, n)
    print("Encrypted:", ciphertext)

    decrypted_message = rsa_decrypt(ciphertext, d, n)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
Original Message: HELLO
Encrypted: [2284, 1955, 894, 894, 264]
Decrypted Message: Ԝǌֻֻ

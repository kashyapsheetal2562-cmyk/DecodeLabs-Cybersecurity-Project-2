def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def main():
    print("=" * 50)
    print("       DecodeLabs Encryption & Decryption")
    print("              Caesar Cipher")
    print("=" * 50)

    text = input("\nEnter text: ")

    while True:
        try:
            shift = int(input("Enter shift key (1-25): "))

            if 1 <= shift <= 25:
                break

            print("Please enter a shift between 1 and 25.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    encrypted_text = caesar_encrypt(text, shift)
    decrypted_text = caesar_decrypt(encrypted_text, shift)

    print("\n" + "=" * 50)
    print("RESULT")
    print("=" * 50)

    print(f"Original Text  : {text}")
    print(f"Shift Key      : {shift}")
    print(f"Encrypted Text : {encrypted_text}")
    print(f"Decrypted Text : {decrypted_text}")

    print("=" * 50)


if __name__ == "__main__":
    main()

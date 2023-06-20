import random
import string

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, include_uppercase, include_numbers, include_symbols)

    print("Generated Password:", password)

if __name__ == '__main__':
    main()

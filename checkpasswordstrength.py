import re

def check_password_strength(password):
    score = 0

    # Check length of password
    if len(password) >= 8:
        score += 1

    # Check if password contains both uppercase and lowercase letters
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1

    # Check if password contains at least one digit
    if re.search(r'\d', password):
        score += 1

    # Check if password contains at least one special character
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1

    return score


def main():
    password = input("Enter a password: ")
    strength = check_password_strength(password)

    if strength == 0:
        print("Weak password")
    elif strength == 1:
        print("Medium password")
    elif strength == 2:
        print("Strong password")
    elif strength == 3:
        print("Very strong password")


if __name__ == '__main__':
    main()

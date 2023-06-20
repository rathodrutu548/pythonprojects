import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess == number:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break
        elif guess < number:
            print("Too low! Try guessing a higher number.")
        else:
            print("Too high! Try guessing a lower number.")

def main():
    print("Welcome to the Guess the Number game!")
    guess_number()

if __name__ == '__main__':
    main()

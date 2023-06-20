import random

def select_word():
    word_list = ["apple", "banana", "orange", "grape", "pineapple"]
    return random.choice(word_list)

def play_hangman():
    word = select_word()
    guessed_letters = []
    tries = 6
    guessed_word = ["_"] * len(word)

    while tries > 0 and "_" in guessed_word:
        print("\n")
        print(" ".join(guessed_word))
        print("Tries left:", tries)
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
            continue
        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            tries -= 1
            print("Wrong guess!")

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Out of tries! The word was:", word)

def main():
    print("Welcome to Hangman!")
    play_hangman()

if __name__ == '__main__':
    main()

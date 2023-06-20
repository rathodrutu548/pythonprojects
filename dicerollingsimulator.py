import random

def roll_dice():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        roll = input("Press Enter to roll the dice or 'Q' to quit: ")
        if roll.lower() == 'q':
            print("Thank you for playing!")
            break
        else:
            dice_result = roll_dice()
            print("You rolled a", dice_result)

if __name__ == '__main__':
    main()

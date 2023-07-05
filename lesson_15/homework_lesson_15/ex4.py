"""
Imbunatatiti exercitiul de mai sus pentru a permite utilizatorului sa aleaga cate laturi va avea
zarul si cate zaruri sa arunce.
Dupa ce zarurile au fost configurate, permiteti utilizatorului sa arunce de un numar
indefinit de ori (pan la STOP).
"""
import random


def roll_dice(num_dice, num_sides):
    dice_values = []
    total = 0
    for _ in range(num_dice):
        dice_value = random.randint(1, num_sides)
        dice_values.append(dice_value)
        total += dice_value
    return dice_values, total


def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        num_dice = int(input("Enter the number of dice: "))
        num_sides = int(input("Enter the number of sides on each die: "))

        dice_values, total = roll_dice(num_dice, num_sides)

        print(f"Dice values: {dice_values}")
        print(f"Total: {total}")
        print()

        roll_again = input("Press Enter to roll again (or type 'stop' to quit): ")
        if roll_again.lower() == 'stop':
            break


if __name__ == '__main__':
    main()

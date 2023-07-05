"""
Utilizand modulul random, creati un program care va simula 2 zaruri cu 6 laturi.
Utilizatorul are optinuea sa arunce zarurile.
Programul va afisa valorile pentru fiecare zar si valoarea totala.
"""
import random

def roll_dice():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    total = dice_1 + dice_2
    return dice_1, dice_2, total

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        roll = input("Press Enter to roll the dice (or type 'q' to quit): ")
        if roll.lower() == 'q':
            break
        dice_1, dice_2, total = roll_dice()
        print(f"Dice 1: {dice_1}")
        print(f"Dice 2: {dice_2}")
        print(f"Total: {total}")
        print()

if __name__ == '__main__':
    main()
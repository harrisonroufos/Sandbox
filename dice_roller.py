"""
Dice roll simulator
For fun
"""
import random


def main():
    """Simulate a die/dice roll"""
    print("Welcome to the dice roll simulator.")
    print("Enter a negative number to quit.")
    number_of_die = int(input("Number of die: "))
    while number_of_die > 0:
        simulate_dice_roll(number_of_die)
        print("Enter a negative number to quit.")
        number_of_die = int(input("Number of die: "))
    print("Farewell")


def simulate_dice_roll(number_of_die):
    """Simulate dice roll"""
    for i in range(number_of_die):
        print(random.randint(1, 6))


main()

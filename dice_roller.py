"""
Dice roll simulator
For fun
"""
import random


def main():
    """Simulate a die/dice roll"""
    print("Welcome to the dice roll simulator.")
    print("Enter 0 to quit.")
    number_of_die = get_valid_die_amount()
    while number_of_die != 0:
        simulate_dice_roll(number_of_die)
        print("Enter 0 to quit.")
        number_of_die = get_valid_die_amount()
    print("Farewell")


def simulate_dice_roll(number_of_die):
    """Simulate die/dice roll"""
    for i in range(number_of_die):
        print(random.randint(1, 6))


def get_valid_die_amount():
    """Get valid die/dice amount"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number_of_die = int(input("Number of die: "))
            is_valid_input = True
        except ValueError:
            print("Invalid")
    return number_of_die


main()

"""CP1402 PRAC 2 EXTENSION with extra"""
import random


def main():
    for i in range(15):
        random_temperature_fahrenheit = random.uniform(-200, 200)
        print(f"{random_temperature_fahrenheit} F -> {convert_fahrenheit_to_celsius(random_temperature_fahrenheit)} C")


def convert_fahrenheit_to_celsius(fahrenheit: float):
    """Convert fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()

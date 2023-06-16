"""CP1402 PRAC 2 EXTENSION with extra"""
import random

OUT_FILE = "temps_input.txt"  # is a file with 15 random float value between -200 and +200


def main():
    out_file = open(OUT_FILE, "w")

    for i in range(15):
        random_temperature_fahrenheit = random.uniform(-200, 200)
        print(f"{random_temperature_fahrenheit}", file=out_file)

    out_file.close()


def convert_fahrenheit_to_celsius(fahrenheit: float):
    """Convert fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()

"""CP1402 PRAC 2 EXTENSION with extra"""
IN_FILE = "temps_input.txt"  # a file with any amount of floats each on their own line
OUT_FILE = "temps_output.txt"  # a file that will collect the fahrenheit to celsius numbers


def main():
    """Converts fahrenheit temp from file and converts to celsius and outputs to file """
    out_file = open(OUT_FILE, "w")
    in_file = open(IN_FILE, "r")

    for line in in_file:
        line = float(line)
        convert_temp = convert_fahrenheit_to_celsius(line)
        print(f"{convert_temp}", file=out_file)
    out_file.close()
    in_file.close()
    print("Finished")


def convert_fahrenheit_to_celsius(fahrenheit: float):
    """Convert fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()

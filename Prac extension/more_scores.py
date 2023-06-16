"""CP1402 PRAC 2 EXTENSION with extra"""
import random

FILE_NAME = "results.txt"


def main():
    outfile = open(FILE_NAME, "w")
    number_of_scores = get_valid_number()
    for i in range(number_of_scores):
        random_number = random.randint(1, 100)
        result = determine_score_category(random_number)
        print(f"{random_number} is {result}", file=outfile)
    outfile.close()


def determine_score_category(score):
    """Determines score category"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


def get_valid_number():
    """Get valid number"""
    is_valid_number = False
    while not is_valid_number:
        try:
            number_of_scores = int(input("Number of scores: "))
            is_valid_number = True
        except ValueError:
            print("Invalid input")
    return number_of_scores


main()

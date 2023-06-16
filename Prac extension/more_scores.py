"""CP1402 PRAC 2 EXTENSION with extra"""
import random


def main():
    number_of_scores = int(input("Number of scores: "))
    for i in range(number_of_scores):
        random_number = random.randint(1, 100)
        result = determine_score_category(random_number)
        print(f"{random_number} is {result}")


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


main()

"""
program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    score_status = determine_score_status(score)
    print(score_status)
    random_score = random.randint(0, 100)
    score_status = determine_score_status(random_score)
    print(f"Random score is {random_score}")
    print(score_status)


def determine_score_status(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
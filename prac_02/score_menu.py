"""

"""
MENU = "(G)et a score between 1-100\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>")
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            score_status = determine_score_status(score)
            print(f"That score is {score_status}")
        elif choice == "S":
            stars = generate_stars(score)
            print(stars)
        choice = input(">>")
    print("Good bye")


def get_valid_score():
    score = int(input("Input score >> "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = int(input("Input score >> "))
    return score


def determine_score_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def generate_stars(score):
    stars = ""
    for i in range(score):
        stars += "*"
    return stars


main()
"""
program for checking password is an appropriate length
converting password to stars
"""


def main():
    minimum_password_length = 5
    password = get_password(minimum_password_length)
    convert_password_to_stars(password)


def convert_password_to_stars(password):
    for i in range(len(password)):
        print("*", end="")


def get_password(minimum_password_length):
    password = input("Enter Password >>")
    while len(password) < minimum_password_length:
        print("Please enter a longer password")
        password = input("Enter Password >>")
    return password

main()
"""
program for checking password is an appropriate length
converting password to stars
"""


minimum_password_length = 5
password = input("Enter Password >>")
while len(password) < minimum_password_length:
    print("Please enter a longer password")
    password = input("Enter Password >>")
for i in range(len(password)):
    print("*", end="")
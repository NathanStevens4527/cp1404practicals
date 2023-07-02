"""
Program for getting emails and deriving names
if a name can't be derived from and email the program will ask for a name
the emails and names will be stored in a dictionary.
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name}, ({email})")


def get_name(email):
    name = email.split("@")
    name = " ".join(name[0].title().split("."))
    confirm_name = input(f"Is your name {name}? (Y/n)")
    if confirm_name != "Y" and confirm_name != "":
        name = input("Name: ")
    return name


main()

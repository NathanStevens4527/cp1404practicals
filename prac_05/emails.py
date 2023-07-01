"""
Program for getting emails and deriving names
if a name can't be derived from and email the program will ask for a name
the emails and names will be stored in a dictionary.
"""


def main():
    emails_to_names = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        emails_to_names[email] = name
        email = input("Email: ")
    for email, name in emails_to_names.items():
        print(f"{name}, ({email})")


def get_name(email):
    name = email.split("@")
    name = " ".join(name[0].title().split("."))
    confirm_name = input(f"Is your name {name}? (Y/n)")
    if confirm_name != "Y" and confirm_name != "":
        name = input("Name: ")
    return name


main()

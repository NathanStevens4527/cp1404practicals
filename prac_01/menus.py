"""
simple program for demonstrating menu loop
"""
MENU_TEXT = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU_TEXT)
choice = input(">>> ")
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU_TEXT)
    choice = input(">>> ")
print("Finished")
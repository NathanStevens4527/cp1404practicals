"""
Program for testing various functions for reading and writing files.
"""


name = input("Enter Name >>")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

name = ""
print(f"Your name is {name}")
in_file = open("name.txt", "r")
name = in_file.readline()
in_file.close()
print(f"Your name is {name}")
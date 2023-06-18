"""
Program for testing various functions for reading and writing files.
"""


name = input("Enter Name >>")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()


print(f"Your name is {name}")
in_file = open("name.txt", "r")
name = in_file.readline()
in_file.close()
print(f"Your name is {name}")


result = 0
in_file = open("numbers.txt", "r")
for i in range (0, 2):
    number = int(in_file.readline())
    result += number
print(f"The sum of the first 2 numbers in numbers.txt is {result}")
in_file.close()


total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
print(f"The total sum of numbers in numbers.txt is {total}")
in_file.close()

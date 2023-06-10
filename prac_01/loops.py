"""
program for testing for loops with range parameters
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("number of stars: "))
for i in range(0, number_of_stars):
    print("*", end='')
print()

line = ""
for i in range(0, number_of_stars):
    line += "*"
    print(line)

print()
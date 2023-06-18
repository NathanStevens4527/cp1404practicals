"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if anything other than an integer is entered.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if 0 is entered for either the numerator or denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
An error checking while loop could be implemented to keep asking for an integer
 until the user enters a non zero integer
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
"""
Answers to the questions for random number questions
Code to generate a random number between 1-100.
"""
# line 1 was run 3 times an returned 12, 19 and 9.
# 5 is the smallest number that could be produced and 20 is the largest.

# line 2 returned 3, 9 and 9.
# 3 is the smallest number that could be produced and 9 is the largest.
# line 2 could not have produced a 4 as it is counting in steps of 2 starting at 3.

# line 3 returned 5.078715327938616, 3.7734531446367297 and 5.237331840967361.
# 2.5 is the smallest number that could have been produced and 5.5 is the largest.


import random


print(random.randint(1, 100))

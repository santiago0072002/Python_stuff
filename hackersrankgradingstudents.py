#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade >= 38:
            mod5 = grade % 5
            
            if mod5 >= 3:
                grade += (5 - mod5)
        result.append(grade)
    return result


grades1 = [25, 67, 78, 80]
print(gradingStudents(grades1))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     grades_count = int(input().strip())

#     grades = []

#     for _ in range(grades_count):
#         grades_item = int(input().strip())
#         grades.append(grades_item)

#     result = gradingStudents(grades)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()


#video explanation https://www.youtube.com/watch?v=tTTJPtrc0xM&ab_channel=HackersRealm

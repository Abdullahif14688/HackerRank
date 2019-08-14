#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0
    valleys = 0
    for i in s:
        if i == 'U':
            altitude += 1
            if altitude == 0:
                valleys += 1
        elif i == 'D':
            altitude -= 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()


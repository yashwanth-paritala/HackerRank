#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    counter = 0
    mcounter = 0
    for a in range(steps):
        if path[a] == "U":
            counter += 1
        else:
            counter -= 1
        if counter == 0 and path[a] != "D":
            mcounter += 1
        #print(counter,mcounter)
    return mcounter
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

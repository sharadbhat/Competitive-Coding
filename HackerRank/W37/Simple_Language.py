# HACKERRANK
# https://www.hackerrank.com/contests/w37/challenges/simple-language

import os
import sys

def maximumProgramValue(n):
    val = 0
    for i in range(n):
        i = input()
        do = i.split()[0]
        amount = i.split()[1]
        if do == 'set':
            if int(amount) > val:
                val = int(amount)
        else:
            if int(amount) + val > val:
                val += int(amount)
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = maximumProgramValue(n)

    fptr.write(str(result) + '\n')

    fptr.close()

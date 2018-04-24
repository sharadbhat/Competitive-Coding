# HACKERRANK
# https://www.hackerrank.com/challenges/maximum-draws/problem

import os
import sys

def maximumDraws(n):
    return n + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = maximumDraws(n)

        fptr.write(str(result) + '\n')

    fptr.close()

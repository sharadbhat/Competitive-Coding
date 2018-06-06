# HACKERRANK
# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem

import os
import sys

def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse = True)
    for i in range(len(sticks) - 2):
        a = sticks[i]
        b = sticks[i+1]
        c = sticks[i+2]
        if (a+b>c) and (b+c>a) and (a+c>b):
            return [c,b,a]
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

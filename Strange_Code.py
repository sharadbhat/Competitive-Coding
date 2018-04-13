# HACKERRANK
# https://www.hackerrank.com/challenges/strange-code/problem

import os
import sys

def strangeCounter(t):
    initial_time = 1
    maximum = 3
    while t >= (maximum + initial_time):
        initial_time += maximum
        maximum *= 2
    diff = abs(t - initial_time)
    return (maximum - diff)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

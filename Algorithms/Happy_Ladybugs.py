# HACKERRANK
# https://www.hackerrank.com/challenges/happy-ladybugs/problem

import os
import sys

def happyLadybugs(b):
    is_happy = True
    if len(b) == 1:
        if b[0] != '_':
            return "NO"
        else:
            return "YES"
    if b[0] != b[1]:
        is_happy = False
    for i in range(1, len(b) - 1):
        if b[i] != '_':
            if b[i] != b[i + 1] and b[i-1] != b[i]:
                is_happy = False
    if b[-1] != b[-2]:
        is_happy = False

    if is_happy == True:
        return "YES"

    b = [i for i in b]
    d = {i:b.count(i) for i in b}

    for i in d:
        if i != '_' and d[i] == 1:
            return "NO"

    if '_' not in d:
        return "NO"

    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

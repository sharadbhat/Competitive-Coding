# HACKERRANK
# https://www.hackerrank.com/challenges/save-the-prisoner/problem

import sys

def saveThePrisoner(people, sweets, start):
    sweets = sweets % people
    if sweets == 0:
        if start == 1:
            return people
        else:
            return (start - 1)
    else:
        a = (start + sweets - 1) % people
        if a != 0:
            return a
        else:
            return people

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)

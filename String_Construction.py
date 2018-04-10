# HACKERRANK
# https://www.hackerrank.com/challenges/string-construction/problem

import sys

def stringConstruction(s):
    p = []
    cost = 0
    for i in s:
        if i not in p:
            p.append(i)
            cost += 1
    return cost

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = stringConstruction(s)
        print(result)

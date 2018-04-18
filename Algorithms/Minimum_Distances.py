# HACKERRANK
# https://www.hackerrank.com/challenges/minimum-distances/problem

import sys

def minimumDistances(a):
    d = {}
    length = len(a)
    minimum = length
    for i in range(length)):
        if a[i] in d:
            dist = abs(d[a[i]] - i)
            if minimum > dist:
                minimum = dist
        d[a[i]] = i
    if minimum == len(a):
        return -1
    else:
        return minimum

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = minimumDistances(a)
    print(result)

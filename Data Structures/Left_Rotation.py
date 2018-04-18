# HACKERRANK
# https://www.hackerrank.com/challenges/array-left-rotation/problem

import os
import sys

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    a = [str(i) for i in a[d%n:] + a[:d%n]]
    print(" ".join(a))

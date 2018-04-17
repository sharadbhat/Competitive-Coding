# HACKERRANK
# https://www.hackerrank.com/challenges/fibonacci-modified/problem

import sys

def fibonacciModified(t1, t2, n):
    count = 2
    while count < n:
        t3 = t1 + t2**2
        t1 = t2
        t2 = t3
        count += 1
    return t3

if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print(result)

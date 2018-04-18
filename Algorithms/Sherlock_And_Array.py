# HACKERRANK
# https://www.hackerrank.com/challenges/sherlock-and-array/problem

import sys

def solve(a):
    if len(a) == 1:
        return "YES"
    left = sum(a[:0])
    right = sum(a[1:])
    curr = a[0]
    next_ele = 1
    while next_ele < len(a):
        if left == right:
            return "YES"
        left += curr
        right -= a[next_ele]
        curr = a[next_ele]
        next_ele += 1
    return "NO"

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)

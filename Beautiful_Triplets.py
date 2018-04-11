# HACKERRANK
# https://www.hackerrank.com/challenges/beautiful-triplets/problem

import sys

def beautifulTriplets(d, arr):
    count = 0
    for i in arr:
        if (i+d) in arr and (i+2*d) in arr:
            count += 1
    return count

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    arr = list(map(int, input().strip().split(' ')))
    result = beautifulTriplets(d, arr)
    print(result)

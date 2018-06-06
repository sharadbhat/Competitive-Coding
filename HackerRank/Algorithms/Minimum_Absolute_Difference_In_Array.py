# HACKERRANK
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

import sys

def minimumAbsoluteDifference(n, arr):
    arr = sorted(arr)
    min = abs(arr[0] - arr[1])
    for i in range(0, n - 1):
        min2 = abs(arr[i] - arr[i + 1])
        if min2 < min:
            min = min2
    return min

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)

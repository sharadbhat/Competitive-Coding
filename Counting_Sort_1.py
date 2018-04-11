# HACKERRANK
# https://www.hackerrank.com/challenges/countingsort1/problem

import sys

def countingSort(arr):
    barr = []
    for i in range(max(arr) + 1):
        barr.append(arr.count(i))
    return barr

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))

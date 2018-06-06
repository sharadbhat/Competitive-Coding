# HACKERRANK
# https://www.hackerrank.com/challenges/countingsort2/problem

import sys

def countingSort(arr):
    a = {}
    for i in arr:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    arr2 = []
    for i in range(max(arr) + 1):
        if i in a:
            for j in range(a[i]):
                arr2.append(i)
    return arr2

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))

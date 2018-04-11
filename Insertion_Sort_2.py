# HACKERRANK
# https://www.hackerrank.com/challenges/insertionsort2/problem

import sys

def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = 0
        while key > arr[j] and j < i:
            j += 1
        del arr[i]
        arr.insert(j, key)
        print(" ".join([str(i) for i in arr]))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)

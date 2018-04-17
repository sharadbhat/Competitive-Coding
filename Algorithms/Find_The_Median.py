# HACKERRANK
# https://www.hackerrank.com/challenges/find-the-median/submissions/code/70741414

import sys

def findMedian(arr):
    arr.sort()
    return arr[len(arr)//2]

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = findMedian(arr)
    print(result)

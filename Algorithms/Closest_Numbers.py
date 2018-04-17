# HACKERRANK
# https://www.hackerrank.com/challenges/closest-numbers/problem

import sys

def closestNumbers(arr):
    numbers = []
    minimum = max(arr) - min(arr)
    arr.sort()
    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]
        if diff == minimum:
            numbers.append(arr[i])
            numbers.append(arr[i+1])
        elif diff < minimum:
            numbers = [arr[i], arr[i+1]]
            minimum = diff
    return numbers


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)
    print (" ".join(map(str, result)))

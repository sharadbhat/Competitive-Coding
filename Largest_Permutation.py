# HACKERANK
# https://www.hackerrank.com/challenges/largest-permutation/problem

# Credits to https://www.hackerrank.com/rednithin

import sys

def largestPermutation(k, arr):
    d = {}
    for i, num in enumerate(arr):
        d[num] = i
    for i, num  in enumerate(arr):
        if k == 0:
            break
        if num == len(arr) - i:
            continue
        i1 = d[num]
        i2 = d[len(arr)-i]

        arr[i], arr[d[len(arr)-i]] = arr[d[len(arr)-i]], arr[i]
        d[num] = i2
        d[len(arr)-i] = i1
        k -= 1
    return arr

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = largestPermutation(k, arr)
    print (" ".join(map(str, result)))

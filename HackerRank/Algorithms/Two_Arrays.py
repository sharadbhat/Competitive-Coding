# HACKERRANK
# https://www.hackerrank.com/challenges/two-arrays/problem

import sys

def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    count = 0
    i = 0
    while i < len(A):
        if A[i] + B[i] < k:
            return "NO"
        i += 1
    return "YES"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        A = list(map(int, input().strip().split(' ')))
        B = list(map(int, input().strip().split(' ')))
        result = twoArrays(k, A, B)
        print(result)

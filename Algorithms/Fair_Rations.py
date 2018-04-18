# HACKERRANK
# https://www.hackerrank.com/challenges/fair-rations/problem

import sys

def fairRations(B):
    count = 0
    odd = 0
    for i in B:
        if i%2 != 0:
            odd += 1
    if odd%2 != 0:
        return "NO"
    b = [i for i in B]
    for i in range(len(b)):
        if b[i]%2 != 0:
            b[i] += 1
            b[i+1] += 1
            count += 2

    for i in b:
        if i%2 != 0:
            return "NO"

    return count


if __name__ == "__main__":
    N = int(input().strip())
    B = list(map(int, input().strip().split(' ')))
    result = fairRations(B)
    print(result)

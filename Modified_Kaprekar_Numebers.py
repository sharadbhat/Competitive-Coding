# HACKERRANK
# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

import sys

def kaprekarNumbers(p, q):
    res =[]
    for i in range(p, q + 1):
        square = str(i**2)
        left = int(0 if square[:len(square)//2] == '' else square[:len(square)//2])
        right = int(square[len(square)//2:])
        if left + right == i:
            res.append(i)
    return res

if __name__ == "__main__":
    p = int(input().strip())
    q = int(input().strip())
    result = kaprekarNumbers(p, q)
    if result == []:
        print("INVALID RANGE")
    else:
        print (" ".join(map(str, result)))

# HACKERRANK
# https://www.hackerrank.com/challenges/flipping-bits/problem

import sys

def flippingBits(N):
    a = "{0:b}".format(N)
    a = "0"*(32-len(a)) + a
    b = ""
    for i in a:
        if i == '1':
            b += "0"
        else:
            b += "1"
    return int(b, 2)

if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        N = int(input().strip())
        result = flippingBits(N)
        print(result)

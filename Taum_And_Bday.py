# HACKERRANK
# https://www.hackerrank.com/challenges/taum-and-bday/problem

import os
import sys

def taumBday(b, w, bc, wc, z):
    smaller = ((b+w) * bc + w*z) if ((b+w) * bc + w*z) < ((b+w)*wc+b*z) else ((b+w)*wc+b*z)
    if (b * bc + w * wc) <= smaller:
        return (b * bc + w * wc)
    else:
        return smaller

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        bw = input().split()

        b = int(bw[0])

        w = int(bw[1])

        bcWcz = input().split()

        bc = int(bcWcz[0])

        wc = int(bcWcz[1])

        z = int(bcWcz[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()

# HACKERRANK
# https://www.hackerrank.com/challenges/circular-array-rotation/problem

import sys

def circularArrayRotation(a, m):
    for i in range(k):
        ele = a[-1]
        del a[-1]
        a.insert(0, ele)
    return [a[i] for i in m]

if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    m = []
    m_i = 0
    for m_i in range(q):
        m_t = int(input().strip())
        m.append(m_t)
    result = circularArrayRotation(a, m)
    print ("\n".join(map(str, result)))

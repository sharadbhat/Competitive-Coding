# HACKERANK
# https://www.hackerrank.com/challenges/pairs/problem

import sys

def pairs(k, arr):
    count = 0
    l = {}
    for i in arr:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1
    for i in l:
        if (i+k) in l:
            if l[i] == l[i+k]:
                count += l[i]
            else:
                if l[i] < l[i+k]:
                    count += l[i]
                else:
                    count += l[i+k]
    return count

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(k, arr)
    print(result)

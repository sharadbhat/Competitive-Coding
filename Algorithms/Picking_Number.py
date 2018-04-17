# HACKERRANK
# https://www.hackerrank.com/challenges/picking-numbers/problem

import sys

def pickingNumbers(s):
    maximum = 0
    for i in s:
        count = s.count(i) + s.count(i + 1)
        if count >= maximum:
            maximum = count
    return maximum

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)

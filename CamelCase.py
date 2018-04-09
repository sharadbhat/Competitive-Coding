# HACKERRANK
# https://www.hackerrank.com/challenges/camelcase/problem

import sys

def camelcase(s):
    count = 1
    for i in s:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count += 1
    return count

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)

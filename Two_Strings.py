# HACKERRANK
# https://www.hackerrank.com/challenges/two-strings/problem

import sys

def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return "YES"
    return "NO"

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)

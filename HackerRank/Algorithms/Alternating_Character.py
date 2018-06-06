# HACKERRANK
# https://www.hackerrank.com/challenges/alternating-characters/problem

import sys

def alternatingCharacters(s):
    count = 0
    s = [i for i in s]
    prev = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            prev = s[i]
    return count

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)

# HACKERRANK
# https://www.hackerrank.com/challenges/reduced-string/problem

import sys

def super_reduced_string(s):
    s = [i for i in s]
    while True:
        changed = 0
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                del s[i]
                del s[i]
                changed += 1
                break
        if changed == 0:
            break
    if len(s) == 0:
        return "Empty String"
    return "".join(s)

s = input().strip()
result = super_reduced_string(s)
print(result)

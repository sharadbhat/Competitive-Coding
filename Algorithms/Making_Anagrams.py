# HACKERRANK
# https://www.hackerrank.com/challenges/making-anagrams/problem

import sys

def makingAnagrams(s1, s2):
    d1 = {i:s1.count(i) for i in s1}
    d2 = {i:s2.count(i) for i in s2}
    if d1 == d2:
        return 0
    count = 0
    for i in d1:
        if i in d2:
            count += abs(d1[i] - d2[i])
        else:
            count += d1[i]
    for i in d2:
        if i not in d1:
            count += d2[i]
    return count

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)

# HACKERRANK
# https://www.hackerrank.com/challenges/anagram/problem

import sys

def anagram(s):
    if len(s)%2 != 0:
        return -1
    count = 0
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:] if len(s)%2==0 else s[len(s)//2+1:]
    d1 = {i:s1.count(i) for i in s1}
    d2 = {i:s2.count(i) for i in s2}
    for i in d1:
        if i in d2:
            count += abs(d1[i] - d2[i])
        else:
            count += d1[i]
    for i in d2:
        if i not in d1:
            count += d2[i]

    return count//2

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)

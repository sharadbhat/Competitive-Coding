# HACKERRANK
# https://www.hackerrank.com/challenges/append-and-delete/problem

import sys

def appendAndDelete(s, t, k):
    count = 0
    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
    if (len(s) + len(t) <= k + 2*i):
        if ((len(s) + len(t))%2 == k%2) or (len(s) + len(t) < k):
            return "Yes"
    return "No"

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)

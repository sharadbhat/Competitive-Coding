# HACKERRANK
# https://www.hackerrank.com/challenges/repeated-string/problem

import sys

def repeatedString(s, n):
    a_count = s.count('a')
    a_count *= (n//len(s))
    a_count += s[:n%len(s)].count('a')
    return a_count

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)

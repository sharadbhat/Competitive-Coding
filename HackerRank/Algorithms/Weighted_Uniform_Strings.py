# HACKERRANK
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import os
import sys

def get_weight(a):
    return (ord(a) - ord('a') + 1)

def weightedUniformStrings(s, queries):
    prev = 'a'
    count = 0
    d = {}
    for i in range(len(s)):
        if s[i] == prev:
            count += 1
        else:
            prev = s[i]
            count = 1
        value = get_weight(prev) * count
        if value not in d:
            d[value] = True
    res = []
    for i in queries:
        if i in d:
            res.append("Yes")
        else:
            res.append("No")

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

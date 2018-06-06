# HACKERRANK
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import sys

def isValid(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    maximum = 0
    minimum = len(s)
    for i in d:
        if d[i] < minimum:
            minimum = d[i]
        if d[i] > maximum:
            maximum = d[i]
    num_of_min = 0
    num_of_max = 0
    for i in d:
        if d[i] == minimum:
            num_of_min += d[i]
        if d[i] == maximum:
            num_of_max += d[i]

    diff = {}
    for i in d:
        diff[d[i]] = True
    diff_values = len(diff)
    if diff_values > 2:
        return "NO"

    if minimum == maximum:
        return "YES"
    else:
        if abs(minimum - maximum) == 1:
            if num_of_min == minimum or num_of_max == maximum:
                return "YES"
            else:
                return "NO"
        else:
            if num_of_min == 1 or num_of_max == 1:
                return "YES"
        return "NO"

s = input().strip()
result = isValid(s)
print(result)

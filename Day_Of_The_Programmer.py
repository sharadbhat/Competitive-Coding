# HACKERANK
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import sys

def solve(year):
    is_leap = False

    if year < 1918:
        if year%4 == 0:
            is_leap = True
    elif year > 1918:
        if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
            is_leap = True
    else:
        return "26.09." + str(year)

    if is_leap == True:
        return "12.09." + str(year)
    return "13.09." + str(year)

year = int(input().strip())
result = solve(year)
print(result)

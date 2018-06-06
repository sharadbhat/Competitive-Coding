# HACKERRANK
# https://www.hackerrank.com/challenges/marcs-cakewalk/problem

import sys

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
total = 0
calories = sorted(calories, reverse=True)
for i in range(0, n):
    total = total + ((2**i) * calories[i])
print(total)

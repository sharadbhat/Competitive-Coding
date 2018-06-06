# HACKERRANK
# https://www.hackerrank.com/challenges/greedy-florist/problem

import sys
import math

def getMinimumCost(n, k, c):
    c.sort(reverse=True)
    cost = 0
    for i in range(math.ceil(n/k)):
        cost += (i + 1) * sum(c[i*k:i*k+k])
    return cost

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)

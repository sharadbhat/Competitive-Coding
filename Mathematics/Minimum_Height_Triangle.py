# HACKERRANK
# https://www.hackerrank.com/challenges/lowest-triangle/problem

import sys

def lowestTriangle(base, area):
    h = (2 * area)//base
    while 0.5*base*h < area:
        h += 1
    return h

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)

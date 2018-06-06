# HACKERRANK
# https://www.hackerrank.com/challenges/flatland-space-stations/problem

import sys
import math

def flatlandSpaceStations(n, c):
    maximum = -1
    c.sort()
    for i in range(len(c) - 1):
        cities = c[i+1] - c[i] - 1
        if cities > maximum:
            maximum = cities
    maximum = (maximum + 1) // 2
    start = abs(0 - c[0])
    end = abs(n - 1 - c[-1])
    if maximum < start or maximum < end:
        if end < start:
            return start
        return end
    return maximum

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    result = flatlandSpaceStations(n, c)
    print(result)

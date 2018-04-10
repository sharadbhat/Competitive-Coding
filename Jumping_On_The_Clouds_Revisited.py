# HACKERRANK
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

import sys

def jumpingOnClouds(c, k):
    energy = 100
    current = 0
    while True:
        current = (current + k)%len(c)
        energy -= 1
        if c[current] == 1:
            energy -= 2
        if current == 0:
            break
    return energy

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, k)
    print(result)

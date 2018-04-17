# HACKERRANK
# https://www.hackerrank.com/challenges/halloween-sale/problem

import sys

def howManyGames(p, d, m, s):
    cost = p
    count = 0
    while s > 0:
        if s < cost:
            break
        count += 1
        s -= cost
        if (cost - d) > m:
            cost -= d
        else:
            cost = m
    return count

if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)

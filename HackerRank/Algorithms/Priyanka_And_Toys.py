# HACKERRANK
# https://www.hackerrank.com/challenges/priyanka-and-toys/problem

import sys

def toys(w):
    w.sort()
    count = 0
    while len(w) > 0:
        count += 1
        maximum = w[0] + 4
        delete = [i for i in w if i <= maximum]
        for i in delete:
            w.remove(i)
    return count

if __name__ == "__main__":
    n = int(input().strip())
    w = list(map(int, input().strip().split(' ')))
    result = toys(w)
    print(result)

# HACKERRANK
# https://www.hackerrank.com/challenges/mark-and-toys/problem

import sys

def maximumToys(prices, k):
    prices.sort()
    count = 0
    for i in prices:
        if k > i:
            count += 1
            k -= i
    return count

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(' ')))
    result = maximumToys(prices, k)
    print(result)

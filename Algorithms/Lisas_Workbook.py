# HACKERRANK
# https://www.hackerrank.com/challenges/lisa-workbook/problem

import sys

def workbook(n, k, arr):
    page = 1
    count = 0
    for problems in arr:
        for problem in range(1, problems + 1):
            if problem == page:
                count += 1
            if problem%k == 0 or problem == problems:
                page += 1
    return count

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = workbook(n, k, arr)
    print(result)

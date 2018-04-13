# HACKERRANK
# https://www.hackerrank.com/challenges/service-lane/problem

import sys

def serviceLane(n, cases):
    res = []
    for i in cases:
        res.append(min(width[i[0]:i[1]+1]))
    return res

if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    width = list(map(int, input().strip().split(' ')))
    cases = []
    for cases_i in range(t):
        cases_t = [int(cases_temp) for cases_temp in input().strip().split(' ')]
        cases.append(cases_t)
    result = serviceLane(n, cases)
    print ("\n".join(map(str, result)))

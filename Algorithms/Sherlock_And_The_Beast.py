# HACKERRANK
# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    pivot = n
    while pivot > 0:
        if pivot%3 == 0:
            break
        else:
            pivot -= 5
    if pivot < 0:
        print("-1")
    else:
        a = ""
        for i in range(pivot//3):
            a += "555"
        for i in range((n - pivot)//5):
            a += "33333"
        print(a)

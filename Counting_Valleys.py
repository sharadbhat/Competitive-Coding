# HACKERRANK
# https://www.hackerrank.com/challenges/counting-valleys/problem

import sys

def countingValleys(n, s):
    height = 0
    arr = []
    prev_neg = False
    valleys = 0
    for i in s:
        if i == "D":
            height -= 1
        else:
            height += 1
        if height < 0 and prev_neg == False:
            valleys += 1
            prev_neg = True
        if height >= 0:
            prev_neg = False
    return valleys

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)

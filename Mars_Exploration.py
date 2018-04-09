# HACKERRANK
# https://www.hackerrank.com/challenges/mars-exploration/problem

import sys

def marsExploration(s):
    count = 0
    for i in range(len(s)//3):
        j = 3*i
        if s[j] != "S":
            count += 1
        if s[j+1] != "O":
            count += 1
        if s[j+2] != "S":
            count += 1
    return count

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)

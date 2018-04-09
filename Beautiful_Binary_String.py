# HACKERRANK
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem

import sys

def beautifulBinaryString(b):
    b = [i for i in b]
    changes = 0
    for i in range(len(b) - 2):
        if [b[i],b[i+1],b[i+2]] == ['0','1','0']:
            b[i+2] = 1
            changes += 1
    return changes

if __name__ == "__main__":
    n = int(input().strip())
    b = input().strip()
    result = beautifulBinaryString(b)
    print(result

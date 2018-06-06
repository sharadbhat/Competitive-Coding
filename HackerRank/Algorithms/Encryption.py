# HACKERRANK
# https://www.hackerrank.com/challenges/encryption/problem

import sys
import math

def encryption(s):
    rows = math.floor(math.sqrt(len(s)))
    columns = math.ceil(math.sqrt(len(s)))
    while rows * columns < len(s):
        rows += 1
    length = len(s)
    string = ""
    for j in range(columns):
        i = j
        while i < length:
            string += s[i]
            i += columns
        string += " "
    return string

if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)

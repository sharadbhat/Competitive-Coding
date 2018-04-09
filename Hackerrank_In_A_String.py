# HACKERRANK
# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

import sys

def hackerrankInString(s):
    string_list = [i for i in "hackerrank"]
    for i in s:
        if i == string_list[0]:
            del string_list[0]
        if len(string_list) == 0:
            return "YES"
    return "NO"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)

# HACKERRANK
# https://www.hackerrank.com/challenges/strong-password/problem

import sys

def minimumNumber(n, password):
    chars = ["0123456789", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "!@#$%^&*()-+"]
    satisfied = [0, 0, 0, 0]
    for i in password:
        for j in range(len(chars)):
            if i in chars[j]:
                satisfied[j] = 1
    count = 0
    count += satisfied.count(0)
    if (6 - len(password) > count):
        count += (6 - len(password) - count)
    return count

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)

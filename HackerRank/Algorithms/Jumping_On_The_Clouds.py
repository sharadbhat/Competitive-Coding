# HACKERRANK
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

position = 0
count = 0
while position != (n-1):
    if position!= (n-2) and c[position + 2] == 0:
        count += 1
        position += 2
    else:
        count += 1
        position += 1
print(count)

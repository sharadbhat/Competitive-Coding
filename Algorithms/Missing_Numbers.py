# HACKERANK
# https://www.hackerrank.com/challenges/missing-numbers/problem

n1 = int(input())
l1 = input().split(' ')

n2 = int(input())
l2 = input().split(' ')

elements = {}

for i in l1:
    if i in elements:
        elements[i] += 1
    else:
        elements[i] = 1

for i in l2:
    elements[i] -= 1

diff = sorted([int(i) for i in elements if elements[i] != 0])

for i in diff:
    print(i, end=" ")

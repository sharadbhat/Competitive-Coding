# HACKERRANK
# https://www.hackerrank.com/challenges/gem-stones/problem

import sys

def gemstones(arr):
    count = 0
    let = {}
    for i in arr:
        for letter in i:
            if letter in let:
                let[letter] += 1
            else:
                let[letter] = 1
    for i in let:
        is_gem = True
        if let[i] < len(arr):
            continue
        for j in arr:
            if i not in j:
                is_gem = False
        if is_gem:
            count += 1
    return count

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
    arr_t = str(input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)

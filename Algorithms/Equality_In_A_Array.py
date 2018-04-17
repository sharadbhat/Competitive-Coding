# HACKERRANK
# https://www.hackerrank.com/challenges/equality-in-a-array/problem


import sys

def equalizeArray(arr):
    maximum_element = 0
    for i in set(arr):
        if arr.count(i) > arr.count(maximum_element):
            maximum_element = i

    return (len(arr) - arr.count(maximum_element))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)

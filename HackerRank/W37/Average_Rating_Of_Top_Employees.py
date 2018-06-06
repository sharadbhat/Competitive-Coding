# HACKERRANK
# https://www.hackerrank.comcontestsw37challengesthe-average-rating-of-top-employees

import os
import sys

def averageOfTopEmployees(rating):
    count = 0
    total = 0
    for i in rating:
        if i >= 90:
            total += i
            count += 1
    str_average = str(total / count)
    length = len(str_average)
    if length == 4:
        str_average += "0"
    elif length > 5:
        str_average = str_average[:6]
        if str_average[-1] >= "5":
            str_average = str_average[:4] + str(int(str_average[-2]) + 1)
        else:
            str_average = str_average[:5]
    print(str_average)

if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)

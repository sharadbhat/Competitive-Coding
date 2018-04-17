# HACKERANK
# https://www.hackerrank.com/challenges/luck-balance/problem

import sys

def luckBalance(n, k, contests):
    luck = 0
    impo_count = 0
    impo_weights = []
    for i in contests:
        if i[1] == 1:
            impo_weights.append(i[0])
            impo_count += 1
        else:
            luck += i[0]
    impo_weights.sort()
    if k <= impo_count:
        can_lose = impo_weights[:(impo_count-k)]
    else:
        can_lose = []
    luck -= sum(can_lose)
    for i in contests:
        if i[1] == 1:
            if i[0] in can_lose:
                can_lose.remove(i[0])
            else:
                luck += i[0]
    return luck


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    contests = []
    for contests_i in range(n):
        contests_t = [int(contests_temp) for contests_temp in input().strip().split(' ')]
        contests.append(contests_t)
    result = luckBalance(n, k, contests)
    print(result)

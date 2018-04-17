# HACKERRANK
# https://www.hackerrank.com/challenges/correctness-invariant/problem

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = 0
        while key > l[j] and j < i:
            j += 1
        del l[i]
        l.insert(j, key)
    return l


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))

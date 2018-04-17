# HACKERRANK
# https://www.hackerrank.com/challenges/bon-appetit/problem

a = input().split()
no_of_items, doesnt_eat = int(a[0]), int(a[1])

bill = [int(i) for i in input().split()]
anna_amount = int(input())

actual_amount = 0
for i in range(no_of_items):
    if i != doesnt_eat:
        actual_amount += bill[i]

if actual_amount//2 == anna_amount:
    print("Bon Appetit")
else:
    print(abs(anna_amount - actual_amount//2))

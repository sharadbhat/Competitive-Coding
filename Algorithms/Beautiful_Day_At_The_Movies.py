# HACKERRANK
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

a = input().split(' ')

def reverse(x):
    Reverse = 0.
    while(x > 0):
        Reminder = x %10
        Reverse = (Reverse *10) + Reminder
        x = int(x / 10)
    return int(Reverse)

count = 0
for i in range(int(a[0]), int(a[1]) + 1):
    revi = reverse(i)
    if abs(i - revi) % int(a[2]) == 0:
        count += 1

print(count)

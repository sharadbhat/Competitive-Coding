# HACKERRANK
# https://www.hackerrank.com/challenges/the-time-in-words/problem

import sys

def timeInWords(h, m):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    if m == 0:
        return (numbers[h-1] + " o' clock")
    hour = numbers[h - 1] if m <= 30 else numbers[h]
    hour = "one" if hour == "thirteen" else hour
    minutes = ""
    if m < 20 or m > 40:
        if m == 15 or m == 45:
            minutes = "quarter "
        else:
            minutes = numbers[m - 1] if m < 20 else numbers[59 - m]
            minutes += " minute " if m == 1 or (60 - m) == 1 else " minutes "
    elif m == 30:
        minutes = "half "
    elif m == 20 or m == 40:
        minutes = "twenty minutes "
    elif m > 20 or m < 40:
        minutes = "twenty "
        minutes += numbers[m-21] if m < 30 else numbers[39 - m]
        minutes += " minutes "

    if m <= 30:
        minutes += "past "
    else:
        minutes += "to "

    return (minutes + hour)


if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)

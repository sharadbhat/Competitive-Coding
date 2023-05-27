# Leetcode
# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        is_neg = False
        started = False
        out = 0
        for i in s:
            if i in '1234567890':
                out = out * 10 + int(i)
                started = True
            elif i in '+-' and not started:
                is_neg = True if i == '-' else False
                started = True
            elif i in 'abcdefghijklmnopqrstuvwxyz.' and not started:
                break
            elif started:
                break
        
        out = out if not is_neg else -out
        if out < -(2 ** 31):
            out = -(2 ** 31)
        elif out >= 2 ** 31:
            out = 2 ** 31 - 1
        
        return out
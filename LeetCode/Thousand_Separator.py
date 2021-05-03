# Leetcode
# https://leetcode.com/problems/thousand-separator/


class Solution:
    def thousandSeparator(self, n: int) -> str:
        out = ''
        count = 0

        while n > 0:
            digit = n % 10
            n //= 10
            if count == 3:
                out = '.' + out
                count = 0
            out = str(digit) + out
            count += 1

        return out if out != '' else '0'

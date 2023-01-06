# Leetcode
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution:
    def countDigits(self, num: int) -> int:
        og = num
        count = 0
        while num > 0:
            digit = num % 10
            num = num // 10
            if og % digit == 0:
                count += 1
        return count
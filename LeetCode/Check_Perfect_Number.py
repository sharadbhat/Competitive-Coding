# Leetcode
# https://leetcode.com/problems/perfect-number/


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 1 if num > 1 else 0
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                total += i
                if i != 1:
                    total += num // i
        return total == num

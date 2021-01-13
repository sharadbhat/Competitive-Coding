# leetcode
# https://leetcode.com/problems/calculate-money-in-leetcode-bank


class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for i in range((n // 7) + 1):
            days_in_week = 7 if n >= 7 else n
            n -= 7
            total += self.calcSum(days_in_week + i) - self.calcSum(i)
        return total

    def calcSum(self, n: int) -> int:
        return (n * (n + 1)) // 2

# Leetcode
# https://leetcode.com/problems/arranging-coins/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 1
        while n >= rows:
            n -= rows
            rows += 1
        return rows - 1

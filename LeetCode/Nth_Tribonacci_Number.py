# Leetcode
# https://leetcode.com/problems/n-th-tribonacci-number/


class Solution:
    def tribonacci(self, n: int, d={0: 0, 1: 1, 2: 1}) -> int:
        if n in d:
            return d[n]

        d[n] = self.tribonacci(
            n - 1, d) + self.tribonacci(n - 2, d) + self.tribonacci(n - 3, d)

        return d[n]

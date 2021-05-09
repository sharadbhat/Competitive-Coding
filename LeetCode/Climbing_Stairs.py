# Leetcode
# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb({1: 1, 2: 2}, n)

    def climb(self, d: dict, n: int) -> int:
        if n in d:
            return d[n]

        count = 0
        for i in [1, 2]:
            count += self.climb(d, n-i)

        d[n] = count
        return count

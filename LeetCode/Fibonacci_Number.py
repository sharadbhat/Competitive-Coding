# Leetcode
# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, n: int) -> int:
        d = {0: 0, 1: 1}

        def helper(n):
            if n in d:
                return d[n]

            d[n] = helper(n - 1) + helper(n - 2)

            return d[n]

        return helper(n)

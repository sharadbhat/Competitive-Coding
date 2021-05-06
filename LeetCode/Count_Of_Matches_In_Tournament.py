# Leetcode
# https://leetcode.com/problems/count-of-matches-in-tournament/


class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while n > 1:
            temp = n // 2
            if n > 1 and n % 2 == 1:
                temp += 1
            total += n - temp
            n = temp
        return total

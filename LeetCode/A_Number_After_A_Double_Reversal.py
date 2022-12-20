# Leetcode
# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return int(str(int(str(num)[::-1]))[::-1]) == num
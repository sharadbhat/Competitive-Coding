# Leetcode
# https://leetcode.com/problems/number-of-good-pairs/


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        out = 0
        for i in nums:
            d[i] = d.get(i, 0) + 1
            out += d[i] - 1
        return out

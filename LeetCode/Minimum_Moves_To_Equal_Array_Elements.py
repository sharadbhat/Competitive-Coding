# Leetcode
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        return sum([i - min_val for i in nums])

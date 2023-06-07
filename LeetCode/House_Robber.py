# Leetcode
# https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        best = [nums[-1]]

        if len(nums) > 1:
            best = [max(nums[-2], nums[-1])] + best

        for i in nums[-3::-1]:
            best = [max(i, i + best[1], best[0])] + best

        return best[0]

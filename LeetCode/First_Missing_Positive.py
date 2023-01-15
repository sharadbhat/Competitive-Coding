# Leetcode
# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        bigger = max(nums)
        if bigger <= 0:
            return 1
        for i in range(1, bigger + 2):
            if i not in nums:
                return i
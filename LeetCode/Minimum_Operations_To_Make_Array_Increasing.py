# Leetcode
# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                count += (prev + 1 - nums[i])
                prev += 1
            else:
                prev = nums[i]
        return count

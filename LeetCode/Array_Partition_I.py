# Leetcode
# https://leetcode.com/problems/array-partition-i/


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

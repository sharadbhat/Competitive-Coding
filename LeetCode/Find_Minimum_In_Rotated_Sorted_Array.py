# Leetcode
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        min_val = nums[-1]
        start_pos = -2
        while nums[start_pos] < min_val:
            min_val = nums[start_pos]
            start_pos -= 1

        return min_val

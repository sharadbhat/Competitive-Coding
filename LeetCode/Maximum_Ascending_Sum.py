# Leetcode
# https://leetcode.com/problems/maximum-ascending-subarray-sum/


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        stop = 1
        prev = 0

        curr_max = nums[0]
        global_max = nums[0]

        while stop < len(nums):
            if nums[prev] >= nums[stop]:
                prev = stop
                curr_max = nums[stop]
            else:
                curr_max += nums[stop]
                prev += 1

            global_max = max(curr_max, global_max)
            stop += 1

        return global_max

# Leetcode
# https://leetcode.com/problems/find-pivot-index/


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for i in range(len(nums)):
            left += nums[i]

            if left == right:
                return i

            right -= nums[i]

        return -1

# Leetcode
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_len = 1

        while right < len(nums) - 1:
            right += 1
            if nums[right] > nums[right - 1]:
                max_len = max(max_len, right - left + 1)
            else:
                left = right

        return max_len

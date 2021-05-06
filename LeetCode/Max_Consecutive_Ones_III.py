# Leetcode
# https://leetcode.com/problems/max-consecutive-ones-iii/


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, stop, width = 0, 0, 0
        zero_count = 0

        while stop < len(nums):
            if nums[stop] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1

            width = max(width, stop - start + 1)
            stop += 1

        return width

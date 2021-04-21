# LeetCode
# https://leetcode.com/problems/move-zeroes/description/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        og_len = len(nums)
        i = 0
        while i < og_len:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                og_len -= 1
            else:
                i += 1

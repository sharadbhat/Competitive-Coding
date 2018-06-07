# LeetCode
# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = nums.count(0)
        x = [i for i in nums if i != 0]
        nums[:] = x + [0] * a

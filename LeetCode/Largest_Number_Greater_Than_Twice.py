# LeetCode
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = nums[0]
        pos = 0
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]
                pos = i
        for i in nums:
            if 2 * i > largest and i != largest:
                return -1
        return pos

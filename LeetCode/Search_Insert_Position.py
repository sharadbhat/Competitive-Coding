# LeetCode
# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)

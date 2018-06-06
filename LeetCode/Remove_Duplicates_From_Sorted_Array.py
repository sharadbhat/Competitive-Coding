# LeetCode
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp_list = []
        i = 0
        while i < len(nums):
            if nums[i] in temp_list:
                del nums[i]
            else:
                temp_list.append(nums[i])
                i += 1
        return len(nums)

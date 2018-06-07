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
        if len(nums) > 0:
            prev = nums[0]
            temp_list = [prev]
            for i in range(1, len(nums)):
                if nums[i] != prev:
                    temp_list.append(nums[i])
                    prev = nums[i]
            nums[:] = temp_list
        return len(nums)

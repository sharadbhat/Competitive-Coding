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
        temp_dict = {}
        for i in range(len(nums)):
            if nums[i] not in temp_dict:
                temp_list.append(nums[i])
                temp_dict[nums[i]] = 1
        nums[:] = temp_list
        return len(nums)

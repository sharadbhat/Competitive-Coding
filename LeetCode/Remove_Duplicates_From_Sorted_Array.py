# LeetCode
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        unique_vals = 0
        i = 0
        while i < len(nums):
            if prev == None or prev != nums[i]:
                prev = nums[i]
                unique_vals += 1
                i += 1
            else:
                nums.pop(i)
        return unique_vals

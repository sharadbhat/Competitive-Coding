# Leetcode
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        i = 0
        while i < len(nums):
            d[nums[i]] = d.get(nums[i], 0) + 1
            if d[nums[i]] > 2:
                nums.pop(i)
            else:
                i += 1

        return len(nums)

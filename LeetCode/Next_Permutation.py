# Leetcode
# https://leetcode.com/problems/next-permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        pos = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                pos = i

        left, right = 0, len(nums) - 1
        
        if pos != 0:
            swap_pos = pos
            for i in range(pos, len(nums)):
                if nums[i] > nums[pos - 1]:
                    swap_pos = i

            nums[pos - 1], nums[swap_pos] = nums[swap_pos], nums[pos - 1]

            left, right = pos, len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return
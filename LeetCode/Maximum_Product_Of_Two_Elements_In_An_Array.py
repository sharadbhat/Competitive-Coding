# Leetcode
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        small = min(nums[0], nums[1])
        big = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            if nums[i] >= big:
                small = big
                big = nums[i]
            elif nums[i] > small:
                small = nums[i]

        return (small - 1) * (big - 1)

# Leetcode
# https://leetcode.com/problems/product-of-array-except-self


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        curr_mul = 1
        for i in nums:
            arr.append(curr_mul)
            curr_mul *= i

        curr_mul = 1
        for i in range(len(nums)):
            arr[-(i + 1)] *= curr_mul
            curr_mul *= nums[-(i + 1)]

        return arr

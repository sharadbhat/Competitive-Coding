# Leetcode
# https://leetcode.com/problems/product-of-array-except-self


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prodRev = [1]
        out = [1]

        for i in nums[:-1]:
            prod *= i
            out.append(prod)

        prod = 1
        for i in range(len(nums) - 1, 0, -1):
            prod *= nums[i]
            out[i - 1] = out[i - 1] * prod

        return out

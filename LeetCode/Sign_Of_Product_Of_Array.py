# Leetcode
# https://leetcode.com/problems/sign-of-the-product-of-an-array


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        curr = 1
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                curr *= -1
        return curr

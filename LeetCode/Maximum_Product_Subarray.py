# Leetcode
# https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        out = max(nums)

        currMax, currMin = 1, 1

        for i in nums:
            if i == 0:
                currMax, currMin = 1, 1
            else:
                temp = i * currMax
                currMax = max(temp, i * currMin, i)
                currMin = min(temp, i * currMin, i)
            
                out = max(currMax, out)
        
        return out
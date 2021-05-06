# Leetcode
# https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curr_prod = nums[0]
        start = 0
        end = 1
        count = 1

        while end < len(nums):
            curr_prod *= nums[end]

            while start < len(nums) and curr_prod >= k:
                curr_prod //= nums[start]
                start += 1

            count += (end - start + 1)

            end += 1

        return count

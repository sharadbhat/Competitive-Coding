# LeetCode
# https://leetcode.com/problems/single-number/description/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

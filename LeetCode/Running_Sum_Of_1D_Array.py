# Leetcode
# https://leetcode.com/problems/running-sum-of-1d-array/


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        curr_sum = 0
        for i in nums:
            curr_sum += i
            out.append(curr_sum)
        return out

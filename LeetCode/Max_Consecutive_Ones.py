# Leetcode
# https://leetcode.com/problems/max-consecutive-ones/


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = currCount = 0
        for i in nums:
            if i == 1:
                currCount += 1
                maxCount = max(maxCount, currCount)
            else:
                currCount = 0
        return maxCount

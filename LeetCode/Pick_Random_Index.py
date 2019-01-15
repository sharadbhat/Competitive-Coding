# LeetCode
# https://leetcode.com/problems/random-pick-index/

from random import choice
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = {}
        for i in range(len(nums)):
            if nums[i] not in self.d:
                self.d[nums[i]] = [i]
            else:
                self.d[nums[i]].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return choice(self.d[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

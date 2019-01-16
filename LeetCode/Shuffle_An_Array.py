# LeetCode
# https://leetcode.com/problems/shuffle-an-array/

from random import shuffle

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums[:]
        self.temp = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.temp = self.original[:]
        return self.temp

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffle(self.temp)
        return self.temp

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

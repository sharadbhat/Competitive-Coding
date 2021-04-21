# LeetCode
# https://leetcode.com/problems/rotate-array/description/


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            nums.insert(0, nums.pop(-1))
            i += 1

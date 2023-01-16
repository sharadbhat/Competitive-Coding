# Leetcode
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        temp = self.subsets(nums[1:])
        out = []
        for i in temp:
            out.append(i)
            out.append([nums[0]] + i)
        return out
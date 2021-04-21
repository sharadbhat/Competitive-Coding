# LeetCode
# https://leetcode.com/problems/two-sum


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_num = {}
        for i in range(len(nums)):
            if nums[i] in complement_num:
                return [complement_num[nums[i]], i]
            else:
                complement_num[target - nums[i]] = i

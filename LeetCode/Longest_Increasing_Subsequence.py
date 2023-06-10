# Leetcode
# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        global_max = 1
        local_maxs = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            local_max = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    local_max = max(local_max, 1 + local_maxs[j])
            
            local_maxs[i] = local_max
            global_max = max(global_max, local_max)
        
        return global_max

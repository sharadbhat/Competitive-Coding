# Leetcode
# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0]

        nums = nums[::-1]

        for i in range(1, len(nums)):
            val = i
            for j in range(1, nums[i] + 1):
                if len(dp) >= j:
                    val = min(val, 1 + dp[j - 1])
            
            dp = [val] + dp
        
        return dp[0]
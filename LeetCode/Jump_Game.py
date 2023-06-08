# Leetcode
# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [True]

        nums = nums[::-1]

        for i in range(1, len(nums)):
            is_possible = False

            for j in range(1, nums[i] + 1):
                if dp[j - 1]:
                    dp = [True] + dp
                    is_possible = True
                    break

            if not is_possible:
                dp = [False] + dp
        
        return dp[0]
# Leetcode
# https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        for candidate in candidates:
            for i in range(1, target + 1):
                if candidate < i:
                    for j in dp[i - candidate]:
                        dp[i].append(j + [candidate])
                if candidate == i:
                    dp[i].append([candidate])
        
        return dp[target]
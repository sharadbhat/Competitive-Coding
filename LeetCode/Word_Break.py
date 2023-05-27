# Leetcode
# https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s[i:].startswith(word):
                    dp[i] = dp[i + len(word)]
                    if dp[i] == True:
                        break

        return dp[0]
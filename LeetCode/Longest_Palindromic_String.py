# Leetcode
# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ''
        for center in range(len(s)):
            l, r = center, center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(out) < r - l + 1:
                    out = s[l:r + 1]
                l -= 1
                r += 1
            
            l, r = center, center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(out) < r - l + 1:
                    out = s[l:r + 1]
                l -= 1
                r += 1
        
        return out

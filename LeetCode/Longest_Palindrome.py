# Leetcode
# https://leetcode.com/problems/longest-palindrome


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_present = False
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        palindrome = 0
        for i in d:
            palindrome += d[i]
            if d[i] % 2 != 0:
                palindrome -= 1
                odd_present = True
        return palindrome + 1 if odd_present else palindrome

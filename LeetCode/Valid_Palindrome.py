# LeetCode
# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s_temp = ""
        for i in s:
            if (ord(i) >= 48 and ord(i) <= 57) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
                s_temp += i
        if s_temp == s_temp[::-1]:
            return True
        return False

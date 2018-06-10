# LeetCode
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end = len(s) - 1
        vowels = set(list('aeiouAEIOU'))
        while start < end:
            while s[start] not in vowels and start < end:
                start += 1

            while s[end] not in vowels and start < end:
                end -= 1

            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)

# LeetCode
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        elif l == 1:
            return 1
        curr = 0
        max_count = 0
        d = {s[curr] : curr}
        while curr < l:
            if s[curr] not in d:
                d[s[curr]] = curr
            else:
                dl = len(d)
                if max_count < dl:
                    max_count = dl
                if curr == l - 1:
                    break
                pos = d[s[curr]]
                d = {i:d[i] for i in d if d[i] > pos}
                d[s[curr]] = curr
            dl = len(d)
            if max_count < dl:
                max_count = dl
            curr += 1
        return max_count

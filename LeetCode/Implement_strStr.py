# LeetCode
# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not len(needle):
            return 0
        if not len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                found = True
                for j in range(len(needle)):
                    if needle[j] != haystack[i + j]:
                        found = False
                        break
                if found:
                    return i
        return -1

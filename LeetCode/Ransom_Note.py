# LeetCode
# https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d2 = {}
        for i in magazine:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1

        d1 = {}
        for i in ransomNote:
            if i not in d2:
                return False
            else:
                d2[i] -= 1
                if d2[i] == -1:
                    return False
        return True

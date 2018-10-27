# LeetCode
# https://leetcode.com/problems/long-pressed-name/

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        pos1 = 0
        pos2 = 0
        letter = name[0]
        while pos1 < len(name) and pos2 < len(typed):
            count1 = 0
            count2 = 0
            while pos1 < len(name) and name[pos1] == letter:
                count1 += 1
                pos1 += 1
            while pos2 < len(typed) and typed[pos2] == letter:
                count2 += 1
                pos2 += 1

            if count2 < count1:
                return False

            if pos1 < len(name):
                if pos2 < len(typed):
                    letter = name[pos1]
                else:
                    return False

        return True

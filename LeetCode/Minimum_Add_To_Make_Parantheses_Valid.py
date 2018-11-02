# LeetCode
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        p_count = 0
        count = 0
        i = 0
        for i in S:
            if i == "(":
                p_count += 1
            else:
                p_count -= 1
                if p_count < 0:
                    count -= p_count
                    p_count = 0
        return count if p_count == 0 else count + p_count

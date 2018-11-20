# LeetCode
# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        output = []
        I_val = 0
        D_val = len(S)
        for i in S:
            if i == 'I':
                output.append(I_val)
                I_val += 1
            else:
                output.append(D_val)
                D_val -= 1
        if S[-1] == 'I':
            output.append(D_val)
        else:
            output.append(I_val)
        return output

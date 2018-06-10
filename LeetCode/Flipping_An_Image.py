# LeetCode
# https://leetcode.com/problems/flipping-an-image/description/

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = []
        for i in A:
            t = []
            for j in i:
                if j == 1:
                    t.append(0)
                else:
                    t.append(1)
            B.append(t[::-1])
        return B

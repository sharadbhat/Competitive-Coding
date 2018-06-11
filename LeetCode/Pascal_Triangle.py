# LeetCode
# https://leetcode.com/problems/pascals-triangle/description/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        l = [[1]]
        for i in range(1, numRows):
            k = [1]
            for j in range(1, i):
                k.append(l[i - 1][j - 1] + l[i - 1][j])
            k.append(1)
            l.append(k)
        return l

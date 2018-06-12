# LeetCode
# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = [[1]]
        for i in range(1, rowIndex + 1):
            k = [1]
            for j in range(1, i):
                k.append(l[i - 1][j - 1] + l[i - 1][j])
            k.append(1)
            l.append(k)
        return l[-1]

# LeetCode
# https://leetcode.com/problems/lexicographical-numbers/

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [int(i) for i in sorted([str(j) for j in range(1, n + 1)])]

# LeetCode
# https://leetcode.com/problems/sort-array-by-parity/description/

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = sorted([i for i in A if i % 2 == 0])
        odd = sorted([i for i in A if i % 2 == 1])

        return even + odd

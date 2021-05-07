# LeetCode
# https://leetcode.com/problems/smallest-range-i/

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 1:
            return 0
        minimum = min(A) + K
        maximum = max(A) - K
        return (maximum - minimum) if (maximum - minimum) >= 0 else 0

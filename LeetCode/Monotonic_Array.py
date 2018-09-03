# LeetCode
# https://leetcode.com/problems/monotonic-array/description/

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        pos = 0
        increasing = True
        for pos in range(len(A) - 1):
            if A[pos] > A[pos + 1]:
                increasing = False
                break
            elif A[pos] < A[pos + 1]:
                break
        for pos in range(pos + 1, len(A) - 1):
            if A[pos] > A[pos + 1] and increasing == True:
                return False
            elif A[pos] < A[pos + 1] and increasing == False:
                return False
        return True

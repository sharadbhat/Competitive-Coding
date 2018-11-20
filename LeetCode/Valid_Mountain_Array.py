# LeetCode
# https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False

        if A[1] <= A[0]:
            return False
        i = 1
        went_up = False
        went_down = False
        while i < len(A) and A[i] > A[i - 1]:
            i += 1
            went_up = True
        while i < len(A) and A[i] < A[i - 1]:
            i += 1
            went_down = True
        if i == len(A) and went_up and went_down:
            return True
        return False

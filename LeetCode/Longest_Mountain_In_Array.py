# LeetCode
# https://leetcode.com/problems/longest-mountain-in-array/description/

class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_count = 0
        i = 0
        j = len(A) - 1
        while i < (len(A) - 1) and A[i] >= A[i + 1]: # Beginning descending and plateau
            i += 1
        while j > 0 and A[j] >= A[j - 1]: # Ending ascending and plateau
            j -= 1
        if (j - i + 1) < 3: # Minimum height for mountain
            return 0

        start = i
        curr = i + 1

        while curr < j:
            if A[curr - 1] > A[curr] and A[curr] < A[curr + 1]:
                if max_count < (curr - start + 1):
                    max_count = curr - start + 1
                start = curr
            if A[curr] == A[curr + 1]:
                while curr < j:
                    if A[curr] < A[curr + 1]:
                        start = curr
                        curr += 1
                        break
                    else:
                        curr += 1
                        start = curr
            else:
                curr += 1
            if max_count < (curr - start + 1) and (curr - start) > 1:
                max_count = curr - start + 1
        return max_count

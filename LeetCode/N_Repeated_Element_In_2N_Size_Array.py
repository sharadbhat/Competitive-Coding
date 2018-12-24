# LeetCode
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A) // 2
        d = {}
        candidates = set()
        for i in A:
            d[i] = d.get(i, 0) + 1
            if d[i] == n:
                candidates.add(i)
            if d[i] > n:
                candidates.remove(i)
        return candidates.pop()

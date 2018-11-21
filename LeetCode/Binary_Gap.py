# LeetCode
# https://leetcode.com/problems/binary-gap/

class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = bin(N)[2:]
        d = {}
        longest = 0
        for i in range(len(n)):
            if n[i] == '1':
                if 1 in d:
                    val = i - d[1]
                    if val > longest:
                        longest = val
                d[1] = i
        return longest

# LeetCode
# https://leetcode.com/problems/reverse-bits/


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rev_n = 0
        for i in range(32):
            rev_n = rev_n << 1
            rev_n = rev_n | (n & 1)
            n = n >> 1
        return rev_n

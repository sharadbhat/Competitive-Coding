# LeetCode
# https://leetcode.com/problems/reverse-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        output = 0
        for i in range(32):
            output = output << 1
            if n & 1:
                output = output | 1
            n = n >> 1
        return output

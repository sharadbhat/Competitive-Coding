# Leetcode
# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x = x ^ y
        while (x):
            count += 1 if x & 1 else 0
            x = x >> 1
        return count
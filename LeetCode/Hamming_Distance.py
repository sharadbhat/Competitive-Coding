# Leetcode
# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while (x > 0 or y > 0):
            if x % 2 != y % 2:
                count += 1
            x = x >> 1
            y = y >> 1
        return count
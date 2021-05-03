# Leetcode
# https://leetcode.com/problems/water-bottles/


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        curr = total = numBottles
        while curr >= numExchange:
            new = curr // numExchange
            total += new
            curr = new + curr % numExchange

        return total

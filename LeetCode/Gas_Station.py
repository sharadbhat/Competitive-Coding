# Leetcode
# https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        a = []
        for i, j in zip(gas, cost):
            a.append(i - j)

        if sum(a) < 0:
            return -1
        
        total = 0
        start = 0

        for i in range(len(a)):
            total += a[i]

            if total < 0:
                total = 0
                start = i + 1
        
        return start
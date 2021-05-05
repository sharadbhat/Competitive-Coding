# Leetcode
# https://leetcode.com/problems/maximum-score-from-removing-stones/

from heapq import heapify, heappush, heappop


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapify(heap)
        count = 0
        while len(heap) > 1:
            count += 1
            stone1 = heappop(heap) + 1
            stone2 = heappop(heap) + 1
            if stone1 != 0:
                heappush(heap, stone1)

            if stone2 != 0:
                heappush(heap, stone2)

        return count

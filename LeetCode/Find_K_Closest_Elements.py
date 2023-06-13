# Leetcode
# https://leetcode.com/problems/find-k-closest-elements

from heapq import heapify, heappop
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [(abs(i - x), i) for i in arr]
        heapify(heap)

        out = [heappop(heap)[1] for _ in range(k)]

        return sorted(out)
# Leetcode
# https://leetcode.com/problems/top-k-frequent-words/

from heapq import heapify, heappush, heappop


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            d[i] = d.get(i, 0) - 1

        heap = [[d[i], i] for i in d]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]

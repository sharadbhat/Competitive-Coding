# Leetcode
# https://leetcode.com/problems/task-scheduler

from heapq import heapify, heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for i in tasks:
            d[i] = d.get(i, 0) + 1
        
        heap = [(-d[i], i) for i in d]
        temp_heap = []

        heapify(heap)
        heapify(temp_heap)

        i = 0
        while len(heap) > 0 or len(temp_heap) > 0:
            if len(heap) > 0:
                item = heappop(heap)
                if item[0] < -1:
                    item = (item[0] + 1, item[1])
                    heappush(temp_heap, (i, item))

            if len(temp_heap) and temp_heap[0][0] + n <= i:
                temp_item = heappop(temp_heap)
                heappush(heap, temp_item[1])
            i += 1

        return i